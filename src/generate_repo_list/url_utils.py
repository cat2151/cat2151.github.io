"""URLユーティリティモジュール

このモジュールはURL操作とGitHub URL生成を担当します。
"""

from typing import Dict


class URLUtils:
    """URL操作ユーティリティクラス"""

    def __init__(self, jekyll_config: Dict = None):
        """初期化

        Args:
            jekyll_config: Jekyll設定辞書（オプション）
        """
        self.jekyll_config = jekyll_config or {}
        self.github_base_url = self.jekyll_config.get("github", {}).get("repository_url_base", "https://github.com")

    def make_url_safe(self, text: str, replacements: Dict[str, str]) -> str:
        """文字列をURL安全な形式に変換する

        Args:
            text: 変換対象のテキスト
            replacements: 置換ルール辞書

        Returns:
            URL安全な文字列
        """
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def get_github_repo_url(self, repo_name: str, username: str = None) -> str:
        """GitHub リポジトリURLを生成する

        Jekyll設定のrepository_url_baseを使用し、フォールバックでデフォルトを使用する

        Args:
            repo_name: リポジトリ名
            username: GitHubユーザー名（オプション）

        Returns:
            GitHub リポジトリURL
        """
        # Jekyll設定からユーザー名を取得（引数優先）
        if username is None:
            username = self.jekyll_config.get("github", {}).get("username", "")

        # URLベースからユーザー名部分を構築
        if self.github_base_url.endswith(f"/{username}"):
            # 既にユーザー名が含まれている場合
            return f"{self.github_base_url}/{repo_name}"
        else:
            # ユーザー名を追加する必要がある場合
            return f"{self.github_base_url}/{username}/{repo_name}"

    def get_github_base_url(self) -> str:
        """GitHub ベースURLを取得する

        Returns:
            GitHub ベースURL
        """
        return self.github_base_url
