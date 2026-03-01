"""プロジェクト概要自動取得モジュール

このモジュールは各リポジトリの generated-docs/project-overview.md ファイルから
「プロジェクト概要」の3行説明を自動取得する機能を提供します。
"""

import base64
import re
from typing import Dict, List, Optional

from github import Github
from github.GithubException import GithubException, UnknownObjectException


class ProjectOverviewSectionNotFoundError(Exception):
    """プロジェクト概要セクションが見つからない場合の例外"""

    pass


class ProjectOverviewFetcher:
    """プロジェクト概要自動取得クラス"""

    def __init__(self, github_api: Github, config: Dict):
        """初期化

        Args:
            github_api: GitHub APIクライアント
            config: 設定辞書
        """
        self.github = github_api
        self.config = config
        self.cache = {}  # 同一実行内でのキャッシュ

        # 設定値の取得（デフォルト値付き）
        overview_config = self.config.get("project_overview", {})
        self.enabled = overview_config.get("enabled", True)
        self.target_file = overview_config.get("target_file", "generated-docs/project-overview.md")
        self.section_title = overview_config.get("section_title", "プロジェクト概要")
        self.max_retries = overview_config.get("max_retries", 1)
        self.timeout_seconds = overview_config.get("timeout_seconds", 10)
        self.enable_cache = overview_config.get("enable_cache", True)

    def fetch_overview(self, repo_name: str, username: str) -> List[str]:
        """指定リポジトリからプロジェクト概要3行を取得

        Args:
            repo_name: リポジトリ名
            username: ユーザー名（オーナー名）

        Returns:
            プロジェクト概要の行リスト（最大3行）。取得できない場合は空リスト。
        """
        if not self.enabled:
            return []

        cache_key = f"{username}/{repo_name}"

        # キャッシュから取得
        if self.enable_cache and cache_key in self.cache:
            return self.cache[cache_key]

        try:
            # ファイルの存在確認
            if not self._check_file_exists(repo_name, username):
                result = []
            else:
                # Markdownファイルの内容取得
                markdown_content = self._fetch_markdown_content(repo_name, username)
                if markdown_content:
                    # プロジェクト概要セクションの抽出
                    overview_lines = self._parse_overview_section(markdown_content)
                    result = overview_lines
                else:
                    result = []

        except ProjectOverviewSectionNotFoundError as e:
            # ファイルは存在するがセクションが見つからない場合はフォールバックメッセージを使用
            # (fail fastせず可用性を優先し、不具合を生成物に表示する)
            print(f"⚠️  {repo_name}: {str(e)}")
            fallback_message = self.config.get("project_overview", {}).get(
                "error_fallback_message", "- (プロジェクト概要を取得できませんでした)"
            )
            result = [fallback_message]
        except Exception as e:
            print(f"⚠️  {repo_name}: プロジェクト概要の取得でエラーが発生しました - {str(e)}")
            result = []

        # キャッシュに保存
        if self.enable_cache:
            self.cache[cache_key] = result

        return result

    def _check_file_exists(self, repo_name: str, username: str) -> bool:
        """project-overview.md ファイルの存在確認

        Args:
            repo_name: リポジトリ名
            username: ユーザー名

        Returns:
            ファイルが存在する場合True
        """
        try:
            repo = self.github.get_repo(f"{username}/{repo_name}")
            repo.get_contents(self.target_file)
            return True
        except (UnknownObjectException, GithubException):
            # ファイルが存在しない、またはアクセスできない
            return False

    def _fetch_markdown_content(self, repo_name: str, username: str) -> Optional[str]:
        """GitHub API経由でMarkdownファイルを取得

        Args:
            repo_name: リポジトリ名
            username: ユーザー名

        Returns:
            Markdownファイルの内容。取得できない場合はNone。
        """
        retry_count = 0

        while retry_count <= self.max_retries:
            try:
                repo = self.github.get_repo(f"{username}/{repo_name}")
                file_content = repo.get_contents(self.target_file)

                # Base64デコード
                if hasattr(file_content, "content"):
                    decoded_content = base64.b64decode(file_content.content).decode("utf-8")
                    return decoded_content
                else:
                    print(f"⚠️  {repo_name}: ファイル内容の取得に失敗")
                    return None

            except GithubException as e:
                retry_count += 1
                if retry_count > self.max_retries:
                    if e.status == 404:
                        # ファイルが存在しない場合は警告を出さない
                        return None
                    else:
                        print(
                            f"⚠️  {repo_name}: GitHub API エラー - {e.status} {e.data.get('message', 'Unknown error')}"
                        )
                        return None
                else:
                    print(f"🔄 {repo_name}: リトライ中... ({retry_count}/{self.max_retries})")
            except Exception as e:
                print(f"⚠️  {repo_name}: 予期しないエラー - {str(e)}")
                return None

        return None

    def _parse_overview_section(self, markdown_content: str) -> List[str]:
        """Markdownから「## プロジェクト概要」セクションを抽出

        Args:
            markdown_content: Markdownファイルの内容

        Returns:
            プロジェクト概要の箇条書きリスト（最大3行）

        Raises:
            ProjectOverviewSectionNotFoundError: プロジェクト概要セクションが見つからない場合
        """
        try:
            # セクション抽出パターン
            section_pattern = rf"##\s*{re.escape(self.section_title)}\s*\n(.*?)(?=\n##|\Z)"
            match = re.search(section_pattern, markdown_content, re.DOTALL | re.IGNORECASE)

            if not match:
                raise ProjectOverviewSectionNotFoundError(
                    f"プロジェクト概要セクション '{self.section_title}' が見つかりません"
                )

            section_content = match.group(1).strip()
            return self._extract_bullet_points(section_content)

        except ProjectOverviewSectionNotFoundError:
            raise  # 再発生
        except Exception as e:
            print(f"⚠️  Markdownパースエラー: {str(e)}")
            return []

    def _extract_bullet_points(self, section_content: str) -> List[str]:
        """- で始まる3行の説明を抽出

        Args:
            section_content: プロジェクト概要セクションの内容

        Returns:
            箇条書きの行リスト（最大3行）
        """
        bullet_points = []
        lines = section_content.split("\n")

        for line in lines:
            line = line.strip()
            # - で始まる行を抽出
            if line.startswith("- "):
                bullet_points.append(line)
                # 最大3行まで
                if len(bullet_points) >= 3:
                    break

        return bullet_points

    def get_statistics(self) -> Dict[str, int]:
        """取得統計を返す

        Returns:
            統計情報（キャッシュサイズ、成功件数等）
        """
        return {
            "cache_size": len(self.cache) if self.enable_cache else 0,
            "success_count": len([v for v in self.cache.values() if v]) if self.enable_cache else 0,
            "enabled": self.enabled,
        }

    def clear_cache(self) -> None:
        """キャッシュをクリアする"""
        self.cache.clear()
