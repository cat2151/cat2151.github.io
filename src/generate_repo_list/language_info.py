"""言語情報管理モジュール

このモジュールはプログラミング言語の色・ロゴ情報の管理を担当します。
"""

from typing import Dict


class LanguageInfo:
    """言語情報管理クラス"""

    def __init__(self):
        """初期化"""
        # よく使われる言語の公式色（GitHub Linguist準拠）
        # 目的: shields.ioバッジの見た目統一とブランド色の一貫性確保
        # GitHub公式やshields.ioで使われる標準色と合わせることで、
        # 他のGitHubリポジトリや開発ツールとの視覚的統一性を維持
        self._language_colors = {
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

        # 言語名からSimple Iconsのロゴ名へのマッピング
        # 目的: shields.ioバッジでの正確なロゴ表示
        # Simple Iconsの正式なslug名を使用することで、
        # バッジにブランド公式のロゴアイコンを表示できる
        self._language_logos = {
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

    def get_color(self, language: str) -> str:
        """言語名から色を取得する

        GitHub Linguist準拠の公式色を使用。未知の言語にはデフォルト色を返す。

        Args:
            language: プログラミング言語名

        Returns:
            16進数カラーコード（例: "f1e05a"）
        """
        # 既知の言語の場合は公式色を使用、未知の場合はニュートラルなグレー
        return self._language_colors.get(language, "6c757d")

    def get_logo(self, language: str) -> str:
        """言語名からSimple Icons対応のロゴ名を取得する

        各言語の公式ロゴを使用。未知の言語にはgithubロゴをフォールバック。

        Args:
            language: プログラミング言語名

        Returns:
            Simple Iconsのロゴ名
        """
        # 既知の言語の場合は専用ロゴ、未知の場合はデフォルト
        return self._language_logos.get(language, "github")

    def get_supported_languages(self) -> Dict[str, str]:
        """サポートされている言語とその色の辞書を取得する

        Returns:
            言語名と色のマッピング
        """
        return self._language_colors.copy()

    def get_supported_logos(self) -> Dict[str, str]:
        """サポートされている言語とそのロゴの辞書を取得する

        Returns:
            言語名とロゴのマッピング
        """
        return self._language_logos.copy()
