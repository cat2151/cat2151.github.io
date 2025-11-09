#!/usr/bin/env python3
"""プロジェクト概要取得機能のテスト用スクリプト"""

import os
import sys

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

# モジュールレベルのインポートをここでは回避し、関数内でimportする


def main():
    """メイン関数"""
    # ここでモジュールをインポート
    from config_manager import ConfigManager
    from github import Github
    from project_overview_fetcher import ProjectOverviewFetcher

    print("プロジェクト概要取得機能のテスト")
    print("=" * 50)

    # 設定とGitHub APIの初期化
    config_manager = ConfigManager()
    config = config_manager.load_config()

    try:
        token = config_manager.get_github_token()
        github_api = Github(token)
        print("✓ GitHub API初期化成功")

        # ProjectOverviewFetcherの初期化
        fetcher = ProjectOverviewFetcher(github_api, config)
        print("✓ ProjectOverviewFetcher初期化成功")

        # テスト対象リポジトリ
        test_repos = [
            "github-actions",  # プロジェクト概要があることが確認済み
            "cat-clipboard-launcher",  # プロジェクト概要がない可能性
            "nonexistent-repo",  # 存在しないリポジトリ
        ]

        username = "cat2151"

        for repo_name in test_repos:
            print(f"\n📁 テスト中: {repo_name}")
            print("-" * 30)

            try:
                overview = fetcher.fetch_overview(repo_name, username)

                if overview:
                    print(f"✓ プロジェクト概要取得成功 ({len(overview)}行)")
                    for i, line in enumerate(overview, 1):
                        print(f"  {i}. {line}")
                else:
                    print("ℹ️  プロジェクト概要なし（ファイルが存在しないか、セクションが見つからない）")

            except Exception as e:
                print(f"❌ エラー: {str(e)}")

        # 統計情報の表示
        print("\n📊 統計情報:")
        stats = fetcher.get_statistics()
        for key, value in stats.items():
            print(f"  {key}: {value}")

    except Exception as e:
        print(f"❌ 初期化エラー: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
