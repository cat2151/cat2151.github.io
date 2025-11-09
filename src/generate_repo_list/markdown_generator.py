"""Markdown生成モジュール (リファクタリング版)

このモジュールはMarkdownコンテンツの生成を担当します。
"""

from datetime import datetime
from typing import Any, Dict, List

try:
    # 通常のパッケージインポート（本番環境用）
    from .badge_generator import BadgeGenerator
    from .statistics_calculator import StatisticsCalculator
    from .template_processor import TemplateProcessor
    from .url_utils import URLUtils
except ImportError:
    # 絶対インポート（テスト環境用）
    from badge_generator import BadgeGenerator
    from statistics_calculator import StatisticsCalculator
    from template_processor import TemplateProcessor
    from url_utils import URLUtils


class MarkdownGenerator:
    """Markdown生成クラス（リファクタリング版）"""

    def __init__(self, config: Dict[str, Any], strings: Dict[str, Any], jekyll_config: Dict[str, Any] = None):
        """初期化

        Args:
            config: 設定辞書
            strings: 文字列リソース辞書
            jekyll_config: Jekyll設定辞書（オプション）
        """
        self.config = config
        self.strings = strings
        self.jekyll_config = jekyll_config or {}

        # ユーティリティクラスを初期化
        self.url_utils = URLUtils(jekyll_config)
        self.badge_generator = BadgeGenerator(config, strings, self.url_utils)
        self.stats_calculator = StatisticsCalculator(config)
        self.template_processor = TemplateProcessor()

    def generate_markdown(
        self,
        username: str,
        active: List[Dict],
        archived: List[Dict],
        forks: List[Dict],
        seo_config: Dict,
        json_ld_template: Dict,
    ) -> str:
        """完全なMarkdownドキュメントを生成する

        Args:
            username: GitHubユーザー名
            active: アクティブなリポジトリ
            archived: アーカイブされたリポジトリ
            forks: フォークされたリポジトリ
            seo_config: SEO設定
            json_ld_template: JSON-LDテンプレート

        Returns:
            生成されたMarkdown文字列
        """
        print(f"\n{self.strings['console']['generating_markdown']}")

        today = datetime.now().strftime(self.config["date_format"])

        # 統計情報を計算
        stats = self.stats_calculator.calculate_basic_stats(active, archived, forks)
        lang_list = self.stats_calculator.get_top_languages_text(active + archived + forks)

        # 動的なOGP説明文を生成
        og_description = self.strings["seo"]["og_description_template"].format(
            total=stats["total"], total_stars=stats["total_stars"], lang_list=lang_list
        )

        # 各セクションを生成
        frontmatter = self.template_processor.generate_frontmatter(
            username, og_description, seo_config, json_ld_template, stats["total"]
        )
        stats_section = self._generate_statistics_section(active, archived, forks)
        toc = self._generate_toc()

        # メインコンテンツ生成
        main_title = self.strings["markdown"]["main_title"].format(username=username)
        last_updated = self.strings["markdown"]["last_updated"].format(date=today)

        active_section = self._generate_section(active, username=username)
        archived_section = self._generate_section(archived, "archived", username=username)
        forks_section = self._generate_fork_section(forks, username=username)

        return f"""{frontmatter}

# {main_title}

{last_updated}

{toc}

{stats_section}

---

## {self.strings["markdown"]["sections"]["active"]}

{active_section}

---

## {self.strings["markdown"]["sections"]["archived"]}

{archived_section}

---

## {self.strings["markdown"]["sections"]["forks"]}

{self.strings["markdown"]["repo_details"]["fork_description"]}

{forks_section}
"""

    def _generate_toc(self) -> str:
        """目次を生成する"""
        toc_items = "\n".join(f"- {item}" for item in self.strings["markdown"]["toc_items"])
        return f"""## {self.strings["markdown"]["sections"]["toc"]}

{toc_items}

"""

    def _generate_statistics_section(self, active: List[Dict], archived: List[Dict], forks: List[Dict]) -> str:
        """統計情報セクションを生成する"""
        all_repos = active + archived + forks

        # 統計バッジを生成
        stat_badges = self.badge_generator.generate_statistics_badges(active, archived, forks)

        # 言語バッジを生成
        language_badges = self.badge_generator.generate_language_badges(all_repos)

        return f"""## {self.strings["markdown"]["sections"]["stats"]}

{stat_badges}

### {self.strings["markdown"]["stats"]["main_languages_title"]}

{language_badges}
"""

    def _generate_section(self, repos: List[Dict], section_type: str = "default", username: str = None) -> str:
        """リポジトリセクションを生成する"""
        if not repos:
            if section_type == "archived":
                return self.strings["markdown"]["section_messages"]["archived_empty"]
            return ""

        return "\n".join(self._generate_repo_item(repo, username=username) for repo in repos)

    def _generate_fork_section(self, repos: List[Dict], username: str = None) -> str:
        """フォークセクションを生成する"""
        return "\n".join(self._generate_repo_item(repo, is_fork=True, username=username) for repo in repos)

    def _generate_repo_item(self, repo: Dict, is_fork: bool = False, username: str = None) -> str:
        """個別リポジトリ項目を生成する"""
        main_url = repo["pages_url"] if repo["has_pages"] else repo["url"]
        updated_date = repo["updated_at"].strftime(self.config["date_format"])

        # 情報行を組み立て
        info_parts = [f"📅 {updated_date}"]
        info_line = " | ".join(info_parts)

        # バッジを生成
        badge_line = self.badge_generator.generate_repository_badges(repo, is_fork, username)

        # 結果を組み立て
        lines = [f"## [{repo['name']}]({main_url})"]
        if badge_line:
            lines.extend([badge_line, ""])

        # GitHub URL を明示的なリンクとして生成
        github_url = self.url_utils.get_github_repo_url(repo["name"], username)
        github_link = f"[{github_url}]({github_url})"

        # Pages URL も明示的なリンクとして生成（利用可能な場合）
        if repo["has_pages"]:
            pages_link = f"[{repo['pages_url']}]({repo['pages_url']})"
        else:
            pages_link = self.strings["markdown"]["processing"]["no_pages"]

        lines.extend(
            [
                f"- **{self.strings['markdown']['repo_details']['github_label']}**: {github_link}",
                f"- **{self.strings['markdown']['repo_details']['pages_label']}**: {pages_link}",
                f"- **{self.strings['markdown']['repo_details']['description_label']}**: {repo['description']}",
                f"- {info_line}",
                "",
            ]
        )

        return "\n".join(lines)

    # 後方互換性のためのプロパティとメソッド
    @property
    def github_base_url(self) -> str:
        """後方互換性のためのプロパティ"""
        return self.url_utils.get_github_base_url()

    def _make_url_safe(self, text: str, replacements: dict) -> str:
        """後方互換性のためのメソッド"""
        return self.url_utils.make_url_safe(text, replacements)

    def _get_github_repo_url(self, repo_name: str, username: str = None) -> str:
        """後方互換性のためのメソッド"""
        return self.url_utils.get_github_repo_url(repo_name, username)

    def _get_top_languages(self, repos: list) -> str:
        """後方互換性のためのメソッド"""
        return self.stats_calculator.get_top_languages_text(repos)

    def _generate_language_badges(self, repos: list, total: int) -> str:
        """後方互換性のためのメソッド"""
        # total引数は古いAPIとの互換性のためだが、新実装では不要
        return self.badge_generator.generate_language_badges(repos)

    def _generate_frontmatter(
        self,
        username: str,
        og_description: str,
        seo_config: dict,
        json_ld_template: dict,
        total: int,
        _total_stars: int = None,
        _lang_list: str = None,
    ) -> str:
        """後方互換性のためのメソッド"""
        # _total_stars, _lang_listは古いAPIとの互換性のためだが、新実装では不要
        return self.template_processor.generate_frontmatter(
            username, og_description, seo_config, json_ld_template, total
        )
