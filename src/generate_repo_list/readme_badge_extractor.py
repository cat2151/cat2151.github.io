"""README.mdからバッジを抽出するモジュール

このモジュールはREADME.mdファイルからバッジを抽出し、解析します。
"""

import re
from typing import Dict, List

from github.GithubException import GithubException


class ReadmeBadgeExtractor:
    """README.mdからバッジを抽出するクラス"""

    # バッジタイプとその優先順位の定義（単一の情報源）
    BADGE_PRIORITIES = {
        "japanese": 0,
        "english": 1,
        "github_pages": 2,
        "fork": 3,
        "stars": 4,
        "language": 5,
        "topic": 6,
        "deepwiki": 7,
        "deepseek_wiki": 8,
        "livedemo": 9,
        "ci_cd": 10,
        "coverage": 11,
        "license": 12,
        "version": 13,
        "custom": 999,
    }

    def __init__(self):
        """初期化"""
        # 既知のバッジタイプ（優先順位順）- BADGE_PRIORITIESから自動生成
        self.known_badge_types = sorted(
            [k for k in self.BADGE_PRIORITIES.keys() if self.BADGE_PRIORITIES[k] < 100],
            key=lambda k: self.BADGE_PRIORITIES[k],
        )

    def extract_badges_from_readme(self, repo) -> List[Dict[str, str]]:
        """README.mdからバッジを抽出する

        Args:
            repo: GitHubリポジトリオブジェクト

        Returns:
            バッジ情報のリスト。各要素は{"markdown": "...", "type": "...", "priority": int}の辞書
        """
        try:
            readme = repo.get_readme()
            content = readme.decoded_content.decode("utf-8")
            return self._parse_badges_from_content(content)
        except (GithubException, UnicodeDecodeError):
            return []

    def _parse_badges_from_content(self, content: str) -> List[Dict[str, str]]:
        """README.mdの内容からバッジを抽出する

        Args:
            content: README.mdの内容

        Returns:
            バッジ情報のリスト
        """
        badges = []

        # READMEの先頭部分のみを対象とする（最初の見出しまで、または最初の100行）
        lines = content.split("\n")
        header_section = []
        line_count = 0

        for line in lines:
            line_count += 1
            # 最初の## 見出し（## で始まる行）が見つかったら終了
            # ただし、#（単一の#）は含めない（これはタイトルなのでスキップ）
            if line.strip().startswith("##") and not line.strip().startswith("###"):
                break
            # 最大100行まで
            if line_count > 100:
                break
            header_section.append(line)

        header_content = "\n".join(header_section)

        # マッチした位置を追跡（重複を防ぐため）
        # メモリ効率のため、(start, end)のタプルで管理
        matched_ranges = []

        def is_overlapping(start, end):
            """新しい範囲が既存の範囲と重複するかチェック"""
            for existing_start, existing_end in matched_ranges:
                if start < existing_end and end > existing_start:
                    return True
            return False

        # バッジのパターンを検索
        # パターン1: [![...](...)](...) 形式（クリック可能なバッジ）
        pattern1 = r"\[!\[([^\]]*)\]\(([^\)]+)\)\]\(([^\)]+)\)"
        for match in re.finditer(pattern1, header_content):
            alt_text = match.group(1)
            image_url = match.group(2)
            link_url = match.group(3)
            badge_markdown = match.group(0)

            badge_type = self._identify_badge_type(badge_markdown, alt_text, image_url, link_url)
            priority = self._get_badge_priority(badge_type)

            badges.append(
                {
                    "markdown": badge_markdown,
                    "type": badge_type,
                    "priority": priority,
                    "alt_text": alt_text,
                    "image_url": image_url,
                    "link_url": link_url,
                }
            )
            # マッチした範囲を記録
            matched_ranges.append((match.start(), match.end()))

        # パターン2: ![...](...) 形式（クリック不可能なバッジ）
        pattern2 = r"!\[([^\]]*)\]\(([^\)]+)\)"
        for match in re.finditer(pattern2, header_content):
            # パターン1で既にマッチしている位置はスキップ
            if is_overlapping(match.start(), match.end()):
                continue

            alt_text = match.group(1)
            image_url = match.group(2)
            badge_markdown = match.group(0)

            badge_type = self._identify_badge_type(badge_markdown, alt_text, image_url, None)
            priority = self._get_badge_priority(badge_type)

            badges.append(
                {
                    "markdown": badge_markdown,
                    "type": badge_type,
                    "priority": priority,
                    "alt_text": alt_text,
                    "image_url": image_url,
                    "link_url": None,
                }
            )
            # マッチした範囲を記録
            matched_ranges.append((match.start(), match.end()))

        # パターン3: <a href="..."><img src="..." ...></a> 形式（HTMLバッジ）
        # パターン詳細:
        # - <a\s+href="([^"]+)">: <a> タグとhref属性（リンクURL）
        # - \s*<img\s+src="([^"]+)": <img> タグとsrc属性（画像URL）
        # - [^>]*>: その他の属性
        # - \s*</a>: 閉じタグ
        pattern3 = r'<a\s+href="([^"]+)">\s*<img\s+src="([^"]+)"[^>]*>\s*</a>'
        for match in re.finditer(pattern3, header_content, re.IGNORECASE):
            # パターン1,2で既にマッチしている位置はスキップ
            if is_overlapping(match.start(), match.end()):
                continue

            link_url = match.group(1)
            image_url = match.group(2)
            badge_html = match.group(0)

            # alt属性を取得
            alt_match = re.search(r'alt="([^"]*)"', badge_html)
            alt_text = alt_match.group(1) if alt_match else ""

            badge_type = self._identify_badge_type(badge_html, alt_text, image_url, link_url)
            priority = self._get_badge_priority(badge_type)

            badges.append(
                {
                    "markdown": badge_html,
                    "type": badge_type,
                    "priority": priority,
                    "alt_text": alt_text,
                    "image_url": image_url,
                    "link_url": link_url,
                }
            )

        return badges

    def _identify_badge_type(self, badge_markdown: str, alt_text: str, image_url: str, link_url: str) -> str:
        """バッジのタイプを識別する

        Args:
            badge_markdown: バッジのMarkdown/HTML
            alt_text: バッジのalt属性テキスト
            image_url: バッジの画像URL
            link_url: バッジのリンクURL（存在する場合）

        Returns:
            バッジタイプ（"deepwiki", "language", "topic", "custom"など）
        """
        # DeepWiki バッジ
        if link_url and "deepwiki.com" in link_url.lower():
            return "deepwiki"
        if "deepwiki" in alt_text.lower() or "deepwiki" in badge_markdown.lower():
            return "deepwiki"

        # DeepSeek Wiki バッジ
        if link_url and "deepseek" in link_url.lower():
            return "deepseek_wiki"
        if "deepseek" in alt_text.lower():
            return "deepseek_wiki"

        # LiveDemo バッジ
        if "livedemo" in alt_text.lower() or "live-demo" in alt_text.lower() or "live demo" in alt_text.lower():
            return "livedemo"
        if link_url and ("demo" in link_url.lower() or "livedemo" in link_url.lower()):
            # shields.ioのdemoバッジかチェック
            if "img.shields.io" in image_url and ("demo" in image_url.lower() or "live" in image_url.lower()):
                return "livedemo"

        # Japanese バッジ
        if "🇯🇵" in badge_markdown or "japanese" in alt_text.lower():
            return "japanese"

        # English バッジ
        if "🇺🇸" in badge_markdown or "english" in alt_text.lower():
            return "english"

        # GitHub Pages バッジ
        if "github" in alt_text.lower() and "pages" in alt_text.lower():
            return "github_pages"
        if "github_pages" in image_url.lower():
            return "github_pages"

        # Fork バッジ
        if "fork" in alt_text.lower() and "img.shields.io" in image_url:
            return "fork"

        # Stars バッジ
        if "stars" in alt_text.lower() and "img.shields.io" in image_url:
            return "stars"

        # Language バッジ（プログラミング言語）
        if "img.shields.io" in image_url and any(
            lang.lower() in image_url.lower()
            for lang in [
                "python",
                "javascript",
                "typescript",
                "rust",
                "go",
                "java",
                "csharp",
                "cpp",
                "ruby",
                "php",
            ]
        ):
            return "language"

        # Topic バッジ
        if "topic" in alt_text.lower() and "img.shields.io" in image_url:
            return "topic"

        # Coverage バッジ（CI/CDより先にチェック）
        if "coverage" in alt_text.lower() or "codecov" in image_url.lower():
            return "coverage"

        # CI/CD バッジ
        if any(
            ci in image_url.lower()
            for ci in ["github/workflow", "workflows", "travis-ci", "circleci", "gitlab", "actions", "/badge.svg"]
        ) or any(ci in alt_text.lower() for ci in ["ci", "build", "test"]):
            return "ci_cd"

        # License バッジ
        if "license" in alt_text.lower():
            return "license"

        # Version/Release バッジ
        if any(keyword in alt_text.lower() for keyword in ["version", "release", "npm", "pypi", "crates"]):
            return "version"

        # その他のカスタムバッジ
        return "custom"

    def _get_badge_priority(self, badge_type: str) -> int:
        """バッジタイプの優先順位を取得する

        Args:
            badge_type: バッジタイプ

        Returns:
            優先順位（小さいほど優先度が高い）
        """
        return self.BADGE_PRIORITIES.get(badge_type, self.BADGE_PRIORITIES["custom"])
