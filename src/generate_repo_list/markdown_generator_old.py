"""Markdown生成モジュール

このモジュールはMarkdownコンテンツの生成を担当します。
"""

import hashlib
import json
from datetime import datetime
from typing import Any, Dict, List

import yaml


class MarkdownGenerator:
    """Markdown生成クラス"""

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

        # GitHub URLベースを設定（Jekyll設定優先、フォールバックでデフォルト値）
        self.github_base_url = self.jekyll_config.get("github", {}).get("repository_url_base", "https://github.com")

    def _get_language_color(self, language: str) -> str:
        """言語名から一意のカラフルな色を生成する

        Args:
            language: プログラミング言語名

        Returns:
            16進数カラーコード（例: "f1e05a"）
        """
        # よく使われる言語の公式色（GitHub Linguist準拠）
        language_colors = {
            "JavaScript": "f1e05a",
            "Python": "3572A5",
            "Rust": "dea584",
            "HTML": "e34c26",
            "CSS": "563d7c",
            "C": "555555",
            "C++": "f34b7d",
            "Java": "b07219",
            "Go": "00ADD8",
            "TypeScript": "3178c6",
            "PHP": "4F5D95",
            "Ruby": "701516",
            "Swift": "fa7343",
            "Kotlin": "A97BFF",
            "Shell": "89e051",
            "Dockerfile": "384d54",
            "YAML": "cb171e",
            "JSON": "292929",
            "Markdown": "083fa1",
            "Vue": "41b883",
            "Svelte": "ff3e00",
            "PEG.js": "40be89",
            "Batchfile": "8b407a",
            "Haskell": "a59b78",
        }

        # 既知の言語の場合は公式色を使用
        if language in language_colors:
            return language_colors[language]

        # 未知の言語の場合はハッシュベースで一意の色を生成
        # 言語名をハッシュ化して安定した色を生成
        hash_object = hashlib.md5(language.encode())
        hex_dig = hash_object.hexdigest()

        # ハッシュから6桁の16進数カラーコードを生成
        # 最初の6文字を使って、適度に明るい色になるよう調整
        r = int(hex_dig[0:2], 16)
        g = int(hex_dig[2:4], 16)
        b = int(hex_dig[4:6], 16)

        # 暗すぎる色を避けるため、最低値を設定
        r = max(r, 64)
        g = max(g, 64)
        b = max(b, 64)

        # 明るすぎる色も避ける
        r = min(r, 220)
        g = min(g, 220)
        b = min(b, 220)

        return f"{r:02x}{g:02x}{b:02x}"

    def _get_language_logo(self, language: str) -> str:
        """言語名からSimple Icons対応のロゴ名を取得する

        Args:
            language: プログラミング言語名

        Returns:
            Simple Iconsのロゴ名
        """
        # 言語名からSimple Iconsのロゴ名へのマッピング
        language_logos = {
            "JavaScript": "javascript",
            "Python": "python",
            "Rust": "rust",
            "HTML": "html5",
            "CSS": "css3",
            "C": "c",
            "C++": "cplusplus",
            "Java": "openjdk",
            "Go": "go",
            "TypeScript": "typescript",
            "PHP": "php",
            "Ruby": "ruby",
            "Swift": "swift",
            "Kotlin": "kotlin",
            "Shell": "gnubash",
            "Dockerfile": "docker",
            "YAML": "yaml",
            "JSON": "json",
            "Markdown": "markdown",
            "Vue": "vuedotjs",
            "Svelte": "svelte",
            "PEG.js": "javascript",
            "Batchfile": "windowsterminal",
            "Haskell": "haskell",
        }

        # 既知の言語の場合は専用ロゴを使用
        if language in language_logos:
            return language_logos[language]

        # 未知の言語の場合はデフォルトのgithubロゴを使用
        return "github"

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
        stats_section = self._generate_statistics_section(active, archived, forks)
        toc = self._generate_toc()

        # 統計情報を計算
        total = len(active) + len(archived) + len(forks)
        total_stars = sum(repo["stargazers_count"] for repo in active + archived + forks)

        # 主要言語を取得
        lang_list = self._get_top_languages(active + archived + forks)

        # 動的なOGP説明文を生成
        og_description = self.strings["seo"]["og_description_template"].format(
            total=total, total_stars=total_stars, lang_list=lang_list
        )

        # フロントマター生成
        frontmatter = self._generate_frontmatter(
            username, og_description, seo_config, json_ld_template, total, total_stars, lang_list
        )

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

    def _generate_frontmatter(
        self,
        username: str,
        og_description: str,
        seo_config: Dict,
        json_ld_template: Dict,
        total: int,
        total_stars: int,
        lang_list: str,
    ) -> str:
        """フロントマターを生成する"""

        # JSON-LDテンプレートの値を置換（再帰的に処理）
        def format_template_recursively(obj, **kwargs):
            if isinstance(obj, str):
                return obj.format(**kwargs)
            elif isinstance(obj, dict):
                return {key: format_template_recursively(value, **kwargs) for key, value in obj.items()}
            elif isinstance(obj, list):
                return [format_template_recursively(item, **kwargs) for item in obj]
            else:
                return obj

        json_ld_formatted = format_template_recursively(
            json_ld_template, username=username, total=total, og_description=og_description
        )

        # JSON-LDを生成
        json_ld_str = json.dumps(json_ld_formatted, ensure_ascii=False, indent=2)

        # フロントマターを生成
        frontmatter_lines = ["---"]
        for key, value in seo_config.items():
            if isinstance(value, str):
                formatted_value = value.format(username=username, og_description=og_description)
                # YAML安全性のためクォートを適切に処理
                if '"' in formatted_value or "'" in formatted_value or "\n" in formatted_value:
                    # 複雑な文字列はYAMLリテラルで表現
                    frontmatter_lines.append(f"{key}: |")
                    for line in formatted_value.split("\n"):
                        frontmatter_lines.append(f"  {line}")
                else:
                    frontmatter_lines.append(f'{key}: "{formatted_value}"')
            elif isinstance(value, list):
                # リストはYAMLの流れスタイルで出力
                yaml_output = yaml.dump(value, default_flow_style=True, allow_unicode=True).strip()
                frontmatter_lines.append(f"{key}: {yaml_output}")
            else:
                # その他の型（bool、int、floatなど）は直接文字列化
                frontmatter_lines.append(f"{key}: {value}")

        # JSON-LDを追加
        frontmatter_lines.append("json_ld: |")

        # JSON-LDの各行にインデントを追加
        for line in json_ld_str.split("\n"):
            frontmatter_lines.append(f"  {line}")

        # フロントマターを閉じる
        frontmatter_lines.append("---")

        return "\n".join(frontmatter_lines)

    def _generate_toc(self) -> str:
        """目次を生成する"""
        toc_items = "\n".join(f"- {item}" for item in self.strings["markdown"]["toc_items"])
        return f"""## {self.strings["markdown"]["sections"]["toc"]}

{toc_items}

"""

    def _generate_statistics_section(self, active: List[Dict], archived: List[Dict], forks: List[Dict]) -> str:
        """統計情報セクションを生成する"""
        total = len(active) + len(archived) + len(forks)
        total_stars = sum(repo["stargazers_count"] for repo in active + archived + forks)

        # 統計情報バッジを生成
        stat_badges = [
            f"![Repositories](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['repositories']}-{total}-blue)",
            f"![Active](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['active']}-{len(active)}-green)",
            f"![Archived](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['archived']}-{len(archived)}-yellow)",
            f"![Forks](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['forks']}-{len(forks)}-purple)",
            f"![Stars](https://img.shields.io/badge/{self.strings['markdown']['stats']['badges']['stars']}-{total_stars}-gold)",
        ]
        stat_badges_line = " ".join(stat_badges)

        # 言語統計を生成
        language_badges_line = self._generate_language_badges(active + archived + forks, total)

        return f"""## {self.strings["markdown"]["sections"]["stats"]}

{stat_badges_line}

### {self.strings["markdown"]["stats"]["main_languages_title"]}

{language_badges_line}
"""

    def _get_top_languages(self, repos: List[Dict]) -> str:
        """上位言語リストを取得する"""
        languages = {}
        for repo in repos:
            if repo["language"]:
                languages[repo["language"]] = languages.get(repo["language"], 0) + 1

        top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[
            : self.config["statistics"]["top_languages_count"]
        ]
        return "、".join([lang for lang, _ in top_languages])

    def _generate_language_badges(self, repos: List[Dict], total: int) -> str:
        """言語バッジを生成する"""
        languages = {}
        for repo in repos:
            if repo["language"]:
                languages[repo["language"]] = languages.get(repo["language"], 0) + 1

        top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]

        if not top_languages:
            return self.strings["markdown"]["stats"]["no_language_info"]

        language_badges = []
        for lang, count in top_languages:
            percentage = (count / total) * 100
            lang_safe = self._make_url_safe(lang, self.config["language_badge"]["replacements"])

            # 言語固有のカラフルな色とロゴを使用
            color = self._get_language_color(lang)
            logo = self._get_language_logo(lang)
            language_badges.append(
                f"![{lang}](https://img.shields.io/badge/{lang_safe}-{count}個_({percentage:.1f}%)-{color}?style=flat&logo={logo})"
            )

        return " ".join(language_badges)

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
        badges = []
        if is_fork:
            badges.append("![Fork](https://img.shields.io/badge/Fork-orange)")
        if repo["has_pages"]:
            badges.append("![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Available-brightgreen)")
        if repo["stargazers_count"] > 0:
            badges.append(f"![Stars](https://img.shields.io/badge/Stars-{repo['stargazers_count']}-yellow)")
        if repo["language"] and username:
            # 言語固有のカラフルな色とロゴを使用
            color = self._get_language_color(repo["language"])
            logo = self._get_language_logo(repo["language"])
            badges.append(
                f"![{repo['language']}](https://img.shields.io/badge/{repo['language']}-{color}?style=flat&logo={logo})"
            )

        # トピックバッジ
        for topic in repo.get("topics", []):
            topic_safe = self._make_url_safe(topic, self.config["topic_badge"]["replacements"])
            badges.append(f"![Topic: {topic}](https://img.shields.io/badge/Topic-{topic_safe}-lightblue)")

        badge_line = " ".join(badges) if badges else ""

        # 結果を組み立て
        lines = [f"## [{repo['name']}]({main_url})"]
        if badge_line:
            lines.extend([badge_line, ""])

        # GitHub URL を明示的なリンクとして生成
        github_url = self._get_github_repo_url(repo["name"], username)
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

    def _make_url_safe(self, text: str, replacements: Dict[str, str]) -> str:
        """文字列をURL安全な形式に変換する"""
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def _get_github_repo_url(self, repo_name: str, username: str = None) -> str:
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
