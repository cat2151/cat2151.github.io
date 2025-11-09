#!/usr/bin/env python3
"""GitHub リポジトリ一覧を生成する

このスクリプトは単一責任の原則に従って以下のモジュールに分割されています:
- config_manager: 設定ファイル管理
- repository_processor: リポジトリ取得・処理
- markdown_generator: Markdown生成
- file_handler: ファイル入出力 (このスクリプト内)

GitHub token取得の自動分岐:
- GitHub Actions環境: 環境変数 GITHUB_TOKEN を使用
- ローカル環境: secrets/secrets.toml を優先、フォールバックで環境変数

ローカル実行時の設定方法:
    方法1: secrets/secrets.toml ファイルに設定（推奨）
    [github]
    token = "your_github_token_here"

    方法2: 環境変数設定
    set GITHUB_TOKEN=your_github_token_here

    スクリプト実行:
    python src/generate_repo_list/generate_repo_list.py --username <your_username> --output index.md

GitHub Actions:
    - 毎日UTC 22時（日本時間7時）に自動実行
    - 手動実行も可能（workflow_dispatch）
    - リポジトリの GITHUB_TOKEN secret を自動使用
"""

import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from config_manager import ConfigManager
from github import Auth, Github
from markdown_generator import MarkdownGenerator
from repository_processor import RepositoryProcessor


class FileHandler:
    """ファイル処理クラス"""

    @staticmethod
    def save_markdown(content: str, output_path: str, strings: dict) -> None:
        """Markdownファイルを保存する"""
        print(f"\n{strings['console']['saving_to'].format(path=output_path)}")

        # ディレクトリが存在する場合のみ作成
        dirname = os.path.dirname(output_path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(strings["console"]["saved_success"])
        print(f"  {strings['console']['file_size'].format(size=len(content))}")


class GitHubRepositoryListGenerator:
    """GitHub リポジトリ一覧生成器のメインクラス"""

    def __init__(self):
        """初期化"""
        self.config_manager = ConfigManager()
        self.config = self.config_manager.load_config()
        self.strings = self.config_manager.load_strings()
        self.jekyll_config = self.config_manager.load_jekyll_config()
        self.repo_processor = RepositoryProcessor(self.config, self.strings)
        self.markdown_generator = MarkdownGenerator(self.config, self.strings, self.jekyll_config)
        self.file_handler = FileHandler()

    def run(self, username: str, output_path: str, limit: int = None) -> bool:
        """メイン処理を実行する

        Args:
            username: GitHubユーザー名
            output_path: 出力ファイルパス
            limit: 処理するリポジトリ数の上限（開発用）
        """
        self._print_header()

        # GitHub API初期化
        github_user = self._initialize_github_api(username)
        if not github_user:
            return False

        # リポジトリ処理
        repos = self.repo_processor.fetch_repositories(github_user, username, limit)
        active, archived, forks = self.repo_processor.classify_repositories(repos)

        # Markdown生成
        markdown = self._generate_markdown(username, active, archived, forks)

        # ファイル保存
        self.file_handler.save_markdown(markdown, output_path, self.strings)

        self._print_footer()
        return True

    def _print_header(self):
        """ヘッダーを出力する"""
        separator = self.config["console"]["separator_char"] * self.config["console"]["separator_length"]
        print(separator)
        print(self.strings["console"]["app_title"])
        print(separator)

    def _print_footer(self):
        """フッターを出力する"""
        separator = self.config["console"]["separator_char"] * self.config["console"]["separator_length"]
        print(f"\n{separator}")
        print(self.strings["console"]["completed"])
        print(separator)

    def _initialize_github_api(self, username: str):
        """GitHub APIを初期化する"""
        # 環境判定と適切なメッセージ表示
        is_github_actions = self.config_manager.is_github_actions_environment()

        if is_github_actions:
            print("🔧 GitHub Actions環境で実行中...")
        else:
            print("💻 ローカル環境で実行中...")

        # GitHub tokenを取得
        github_token = self.config_manager.get_github_token()

        if not github_token:
            if is_github_actions:
                print("❌ GitHub Actions環境でGITHUB_TOKEN環境変数が設定されていません")
                print("   リポジトリの Secrets 設定を確認してください")
            else:
                print("❌ GitHub tokenが見つかりません")
                print("   以下のいずれかの方法でtokenを設定してください:")
                print("   1. secrets/secrets.toml ファイルに設定")
                print("   2. 環境変数 GITHUB_TOKEN を設定")
            return None

        print(f"\n{self.strings['console']['initializing_api']}")
        try:
            auth = Auth.Token(github_token)
            g = Github(auth=auth)
            user = g.get_user(username)
            print(self.strings["console"]["authenticated_as"].format(login=user.login))
            return user
        except Exception as e:
            print(self.strings["errors"]["auth_failed"].format(error=e))
            return None

    def _generate_markdown(self, username: str, active: list, archived: list, forks: list) -> str:
        """Markdownを生成する"""
        seo_config = self.config_manager.load_seo_template()
        json_ld_template = self.config_manager.load_json_ld_template()

        return self.markdown_generator.generate_markdown(
            username, active, archived, forks, seo_config, json_ld_template
        )


def main():
    """エントリーポイント"""
    parser = ArgumentParser(
        description="GitHub リポジトリ一覧を生成する",
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 基本的な使用方法
  python src/generate_repo_list/generate_repo_list.py --username <your_username> --output index.md

  # 開発時（最初の1件のみ処理）
  python src/generate_repo_list/generate_repo_list.py --username <your_username> --output index.md --limit 1

  # GitHub Actionsでの使用例
  python src/generate_repo_list/generate_repo_list.py --username ${{ github.repository_owner }} --output index.md
        """,
    )
    parser.add_argument("--username", required=True, help="GitHubのユーザー名")
    parser.add_argument("--output", required=True, help="出力ファイルのパス (例: index.md)")
    parser.add_argument("--limit", type=int, help="処理するリポジトリ数の上限（開発用、例: --limit 1）")

    args = parser.parse_args()

    generator = GitHubRepositoryListGenerator()
    success = generator.run(username=args.username, output_path=args.output, limit=args.limit)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
