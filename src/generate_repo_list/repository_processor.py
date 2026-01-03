"""リポジトリ処理モジュール

このモジュールはGitHubリポジトリの取得、フィルタリング、分類を担当します。
"""

import re
from typing import Any, Dict, List, Tuple

from github import Github
from github.GithubException import GithubException
from project_overview_fetcher import ProjectOverviewFetcher


class RepositoryProcessor:
    """リポジトリ処理クラス"""

    def __init__(self, config: Dict[str, Any], strings: Dict[str, Any], github_api: Github = None):
        """初期化

        Args:
            config: 設定辞書
            strings: 文字列リソース辞書
            github_api: GitHub APIクライアント（プロジェクト概要取得用）
        """
        self.config = config
        self.strings = strings
        self.github_api = github_api

        # プロジェクト概要取得機能の初期化
        if self.github_api is not None:
            self.project_overview_fetcher = ProjectOverviewFetcher(self.github_api, self.config)
        else:
            self.project_overview_fetcher = None

    def fetch_repositories(self, github_user: Github, username: str, limit: int = None) -> List[Dict[str, Any]]:
        """指定ユーザーのリポジトリを取得してフィルタリングする

        Args:
            github_user: GitHubユーザーオブジェクト
            username: ユーザー名
            limit: 処理するリポジトリ数の上限（開発用、有効なリポジトリN件を取得）

        Returns:
            フィルタリングされたリポジトリ情報のリスト
        """
        print(self.strings["console"]["fetching_repos"].format(username=username))
        repos = []
        all_repos = list(github_user.get_repos())
        total = len(all_repos)

        if limit is not None:
            print(f"🔧 開発モード: 有効なリポジトリを {limit} 件取得します（全体: {total} 件）")

        print(self.strings["console"]["found_repos"].format(total=total))

        processed_count = 0
        for repo in all_repos:
            processed_count += 1
            print(
                self.strings["console"]["processing_repo"].format(current=processed_count, total=total, name=repo.name),
                end=" ",
            )

            if self._should_process_repo(repo):
                repo_data = self._create_repo_data(repo, username)
                repos.append(repo_data)
                print(self.strings["markdown"]["processing"]["included"])

                # limitが指定されていて、その件数に達したら終了
                if limit is not None and len(repos) >= limit:
                    print(f"🎯 目標件数 {limit} 件に達したため処理を終了")
                    break
            else:
                reason = self._get_exclusion_reason(repo)
                print(reason)

        print(f"\n{self.strings['console']['filtered_repos'].format(count=len(repos))}")
        return repos

    def classify_repositories(
        self, repos: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
        """リポジトリを3グループに分類してソートする

        Args:
            repos: リポジトリ情報のリスト

        Returns:
            (active, archived, forks)のタプル
        """
        print(f"\n{self.strings['console']['classifying']}")

        # forkを分離
        non_forks = [r for r in repos if not r["fork"]]
        forks = [r for r in repos if r["fork"]]

        # non-forksを2グループに分類
        active = [r for r in non_forks if not r["archived"]]
        archived = [r for r in non_forks if r["archived"]]

        print(f"  {self.strings['classification']['active'].format(count=len(active))}")
        print(f"  {self.strings['classification']['archived'].format(count=len(archived))}")
        print(f"  {self.strings['classification']['forks'].format(count=len(forks))}")

        print(f"\n{self.strings['console']['sorting']}")
        for group in [active, archived, forks]:
            group.sort(key=lambda r: r["updated_at"], reverse=True)

        return active, archived, forks

    def _should_process_repo(self, repo) -> bool:
        """リポジトリを処理すべきかどうかを判定する"""
        # プライベートリポジトリのチェック
        if repo.private and self.config["repository_filter"]["exclude_private"]:
            return False

        # READMEのチェック
        if self.config["repository_filter"]["require_readme"]:
            try:
                repo.get_readme()
                return True
            except GithubException:
                return False

        return True

    def _get_exclusion_reason(self, repo) -> str:
        """除外理由を取得する"""
        if repo.private:
            return self.strings["markdown"]["processing"]["private_repo"]

        try:
            repo.get_readme()
        except GithubException:
            return self.strings["markdown"]["processing"]["no_readme"]

        return "Unknown reason"

    def _check_readme_ja_exists(self, repo) -> bool:
        """README.ja.md が存在するかチェックする

        Args:
            repo: GitHubリポジトリオブジェクト

        Returns:
            README.ja.md が存在する場合 True
        """
        try:
            repo.get_contents("README.ja.md")
            return True
        except GithubException:
            return False

    def _check_readme_en_exists(self, repo) -> bool:
        """README.html が存在するかチェックする

        Args:
            repo: GitHubリポジトリオブジェクト

        Returns:
            README.html が存在する場合 True
        """
        try:
            repo.get_contents("README.html")
            return True
        except GithubException:
            return False

    def _check_deepwiki_badge(self, repo) -> str:
        """README.mdにDeepWikiバッジが存在するかチェックし、URLを返す

        Args:
            repo: GitHubリポジトリオブジェクト

        Returns:
            DeepWikiバッジのURLが存在する場合はそのURL、存在しない場合は空文字列
        """
        try:
            readme = repo.get_readme()
            content = readme.decoded_content.decode("utf-8")

            # DeepWikiバッジの明示的なパターンのみを検索（誤検出を防ぐため）
            # パターン1: [![DeepWiki](https://img.shields.io/badge/DeepWiki-...)](https://deepwiki.com/...)
            # パターン2: [deepwiki-link]: https://deepwiki.com/...

            # Markdownリンク形式のDeepWikiバッジを検索
            pattern = r"\[!\[DeepWiki\].*?\]\((https://deepwiki\.com/[^\)]+)\)"
            match = re.search(pattern, content)
            if match:
                url = match.group(1)
                return self._validate_deepwiki_url(url)

            # 参照スタイルのリンクを検索
            pattern_ref = r"\[deepwiki-link\]:\s*(https://deepwiki\.com/[^\s]+)"
            match_ref = re.search(pattern_ref, content, re.IGNORECASE)
            if match_ref:
                url = match_ref.group(1)
                return self._validate_deepwiki_url(url)

            return ""
        except (GithubException, UnicodeDecodeError):
            return ""

    def _validate_deepwiki_url(self, url: str) -> str:
        """DeepWiki URLを検証する

        Args:
            url: 検証するURL

        Returns:
            有効なURLの場合はそのURL、無効な場合は空文字列
        """
        # 基本的なURL形式の検証
        # https://deepwiki.com/owner/repo 形式であることを確認
        pattern = r"^https://deepwiki\.com/[\w\-\.]+/[\w\-\.]+/?$"
        if re.match(pattern, url):
            return url
        return ""

    def _create_repo_data(self, repo, username: str) -> Dict[str, Any]:
        """リポジトリデータを作成する"""
        repo_data = {
            "name": repo.name,
            "url": repo.html_url,
            "pages_url": f"https://{username}.github.io/{repo.name}/",
            "description": repo.description or self.strings["markdown"]["processing"]["no_description"],
            "archived": repo.archived,
            "has_pages": repo.has_pages,
            "fork": repo.fork,
            "updated_at": repo.updated_at,
            "stargazers_count": repo.stargazers_count,
            "language": repo.language or "",
            "topics": repo.get_topics(),
            "has_readme_ja": self._check_readme_ja_exists(repo),
            "has_readme_en": self._check_readme_en_exists(repo),
            "deepwiki_url": self._check_deepwiki_badge(repo),
        }

        # プロジェクト概要を取得（ProjectOverviewFetcherが利用可能な場合のみ）
        if self.project_overview_fetcher is not None:
            project_overview = self.project_overview_fetcher.fetch_overview(repo.name, username)
            if project_overview:
                repo_data["project_overview"] = project_overview

        return repo_data
