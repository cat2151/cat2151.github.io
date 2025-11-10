"""バッジ生成モジュール

このモジュールは各種バッジの生成を担当します。
"""

from typing import Dict, List

try:
    # 通常のパッケージインポート（本番環境用）
    from .language_info import LanguageInfo
    from .statistics_calculator import StatisticsCalculator
    from .url_utils import URLUtils
except ImportError:
    # 絶対インポート（テスト環境用）
    from language_info import LanguageInfo
    from statistics_calculator import StatisticsCalculator
    from url_utils import URLUtils


class BadgeGenerator:
    """バッジ生成クラス"""

    def __init__(self, config: Dict, strings: Dict, url_utils: URLUtils = None):
        """初期化

        Args:
            config: 設定辞書
            strings: 文字列リソース辞書
            url_utils: URLユーティリティ（オプション）
        """
        self.config = config
        self.strings = strings
        self.language_info = LanguageInfo()
        self.stats_calculator = StatisticsCalculator(config)
        self.url_utils = url_utils or URLUtils()

    def generate_statistics_badges(self, active: List[Dict], archived: List[Dict], forks: List[Dict]) -> str:
        """統計情報バッジを生成する

        Args:
            active: アクティブなリポジトリ
            archived: アーカイブされたリポジトリ
            forks: フォークされたリポジトリ

        Returns:
            統計バッジの文字列
        """
        stats = self.stats_calculator.calculate_basic_stats(active, archived, forks)

        badges = [
            f"![Repositories](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['repositories']}-{stats['total']}-blue)",
            f"![Active](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['active']}-{stats['active']}-green)",
            f"![Archived](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['archived']}-{stats['archived']}-yellow)",
            f"![Forks](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['forks']}-{stats['forks']}-purple)",
            f"![Stars](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['stars']}-{stats['total_stars']}-gold)",
        ]

        return " ".join(badges)

    def generate_language_badges(self, repos: List[Dict]) -> str:
        """言語バッジを生成する

        Args:
            repos: リポジトリリスト

        Returns:
            言語バッジの文字列
        """
        total = len(repos)
        if total == 0:
            return self.strings["markdown"]["stats"]["no_language_info"]

        language_percentages = self.stats_calculator.calculate_language_percentages(repos, limit=5)

        if not language_percentages:
            return self.strings["markdown"]["stats"]["no_language_info"]

        language_badges = []
        for lang, count, percentage in language_percentages:
            lang_safe = self.url_utils.make_url_safe(lang, self.config["language_badge"]["replacements"])

            # 言語固有のカラフルな色とロゴを使用
            color = self.language_info.get_color(lang)
            logo = self.language_info.get_logo(lang)
            # パーセンテージの%記号をURLエンコード
            percentage_text = f"{count}_({percentage:.1f}%25)"
            language_badges.append(
                f"![{lang}](https://img.shields.io/badge/{lang_safe}-{percentage_text}-{color}?style=flat&logo={logo})"
            )

        return " ".join(language_badges)

    def generate_repository_badges(self, repo: Dict, is_fork: bool = False, username: str = None) -> str:
        """個別リポジトリのバッジを生成する

        Args:
            repo: リポジトリ情報
            is_fork: フォークかどうか
            username: GitHubユーザー名（オプション）

        Returns:
            リポジトリバッジの文字列
        """
        badges = []

        # README.ja.md が存在する場合、Japaneseバッジを左端に追加
        if repo.get("has_readme_ja", False):
            readme_ja_url = (
                f"{repo['pages_url']}README.ja.html" if repo["has_pages"] else f"{repo['url']}/blob/main/README.ja.md"
            )
            japanese_badge = (
                f'<a href="{readme_ja_url}"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg"></a>'
            )
            badges.append(japanese_badge)

        # README.html が存在する場合、Englishバッジを追加
        if repo.get("has_readme_en", False):
            readme_en_url = (
                f"{repo['pages_url']}README.html" if repo["has_pages"] else f"{repo['url']}/blob/main/README.html"
            )
            english_badge = (
                f'<a href="{readme_en_url}"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg"></a>'
            )
            badges.append(english_badge)

        if repo["has_pages"]:
            badges.append("![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Available-brightgreen)")

        if is_fork:
            badges.append("![Fork](https://img.shields.io/badge/Fork-orange)")

        if repo["stargazers_count"] > 0:
            badges.append(f"![Stars](https://img.shields.io/badge/Stars-{repo['stargazers_count']}-yellow)")

        if repo["language"] and username:
            # 言語固有のカラフルな色とロゴを使用
            color = self.language_info.get_color(repo["language"])
            logo = self.language_info.get_logo(repo["language"])
            badges.append(
                f"![{repo['language']}](https://img.shields.io/badge/{repo['language']}-{color}?style=flat&logo={logo})"
            )

        # トピックバッジ
        for topic in repo.get("topics", []):
            topic_safe = self.url_utils.make_url_safe(topic, self.config["topic_badge"]["replacements"])
            badges.append(f"![Topic: {topic}](https://img.shields.io/badge/Topic-{topic_safe}-lightblue)")

        return " ".join(badges) if badges else ""
