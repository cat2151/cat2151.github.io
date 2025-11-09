"""統計計算モジュール

このモジュールはリポジトリ統計の計算を担当します。
"""

from typing import Dict, List, Tuple


class StatisticsCalculator:
    """統計計算クラス"""

    def __init__(self, config: Dict):
        """初期化

        Args:
            config: 設定辞書
        """
        self.config = config

    def calculate_basic_stats(self, active: List[Dict], archived: List[Dict], forks: List[Dict]) -> Dict[str, int]:
        """基本統計を計算する

        Args:
            active: アクティブなリポジトリ
            archived: アーカイブされたリポジトリ
            forks: フォークされたリポジトリ

        Returns:
            統計情報の辞書
        """
        all_repos = active + archived + forks
        total_stars = sum(repo["stargazers_count"] for repo in all_repos)

        return {
            "total": len(all_repos),
            "active": len(active),
            "archived": len(archived),
            "forks": len(forks),
            "total_stars": total_stars,
        }

    def calculate_language_stats(self, repos: List[Dict]) -> Dict[str, int]:
        """言語統計を計算する

        Args:
            repos: リポジトリリスト

        Returns:
            言語名と出現回数の辞書
        """
        languages = {}
        for repo in repos:
            if repo["language"]:
                languages[repo["language"]] = languages.get(repo["language"], 0) + 1
        return languages

    def get_top_languages(self, repos: List[Dict], limit: int = None) -> List[Tuple[str, int]]:
        """上位言語リストを取得する

        Args:
            repos: リポジトリリスト
            limit: 上位何位まで取得するか（Noneの場合は設定から取得）

        Returns:
            (言語名, 出現回数)のタプルのリスト
        """
        if limit is None:
            limit = self.config["statistics"]["top_languages_count"]

        languages = self.calculate_language_stats(repos)
        return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:limit]

    def get_top_languages_text(self, repos: List[Dict], limit: int = None) -> str:
        """上位言語をテキスト形式で取得する

        Args:
            repos: リポジトリリスト
            limit: 上位何位まで取得するか

        Returns:
            言語名を「、」で区切った文字列
        """
        top_languages = self.get_top_languages(repos, limit)
        return "、".join([lang for lang, _ in top_languages])

    def calculate_language_percentages(self, repos: List[Dict], limit: int = 5) -> List[Tuple[str, int, float]]:
        """言語の使用率を計算する

        Args:
            repos: リポジトリリスト
            limit: 上位何位まで計算するか

        Returns:
            (言語名, 出現回数, 使用率)のタプルのリスト
        """
        total_repos = len(repos)
        if total_repos == 0:
            return []

        languages = self.calculate_language_stats(repos)
        top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:limit]

        return [(lang, count, (count / total_repos) * 100) for lang, count in top_languages]
