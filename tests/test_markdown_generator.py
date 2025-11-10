#!/usr/bin/env python3
"""MarkdownGeneratorのユニットテスト

このモジュールはMarkdownGeneratorクラスの各機能をpytestでテストします。
"""

import os
import sys
from datetime import datetime
from unittest.mock import patch

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from markdown_generator import MarkdownGenerator  # noqa: E402


class TestMarkdownGenerator:
    """MarkdownGeneratorのテストクラス"""

    @pytest.fixture
    def mock_config(self):
        """設定のフィクスチャ"""
        return {
            "date_format": "%Y年%m月%d日",
            "statistics": {
                "top_languages_count": 3,
            },
            "language_badge": {
                "replacements": {" ": "_", "-": "--"},
                "colors": {
                    "JavaScript": "f7df1e",
                    "Python": "3776ab",
                    "Rust": "000000",
                    "HTML": "e34f26",
                    "default": "blue",
                },
            },
            "topic_badge": {"replacements": {" ": "_", "-": "--"}},
        }

    @pytest.fixture
    def mock_strings(self):
        """文字列リソースのフィクスチャ"""
        return {
            "console": {"generating_markdown": "Markdown生成中..."},
            "markdown": {
                "main_title": "{username}のGitHubリポジトリ一覧",
                "last_updated": "最終更新: {date}",
                "sections": {
                    "toc": "目次",
                    "stats": "統計情報",
                    "active": "アクティブなリポジトリ",
                    "archived": "アーカイブされたリポジトリ",
                    "forks": "フォークしたリポジトリ",
                },
                "toc_items": ["[統計情報](#統計情報)", "[アクティブなリポジトリ](#アクティブなリポジトリ)"],
                "stats": {
                    "main_languages_title": "主要言語",
                    "no_language_info": "言語情報なし",
                    "badges": {
                        "repositories": "リポジトリ",
                        "active": "アクティブ",
                        "archived": "アーカイブ",
                        "forks": "フォーク",
                        "stars": "スター",
                    },
                },
                "repo_details": {
                    "fork_description": "以下は他のリポジトリをフォークしたものです。",
                    "github_label": "GitHub",
                    "pages_label": "GitHub Pages",
                    "description_label": "説明",
                    "project_highlights": "Project Highlights",
                },
                "section_messages": {
                    "archived_empty": "アーカイブされたリポジトリはありません。",
                    "ai_disclaimer": "*注意: 一部のプロジェクトには「Project Highlights」セクションが含まれていますが、これらはAIが自動生成した内容であり、不正確な場合があります。*",
                },
                "processing": {
                    "no_pages": "Pages無し",
                    "no_description": "No description available",
                },
            },
            "seo": {
                "og_description_template": "総計{total}個のリポジトリ、{total_stars}スター、主要言語: {lang_list}",
            },
        }

    @pytest.fixture
    def generator(self, mock_config, mock_strings):
        """MarkdownGeneratorのフィクスチャ"""
        return MarkdownGenerator(mock_config, mock_strings)

    @pytest.fixture
    def sample_repos(self):
        """サンプルリポジトリデータのフィクスチャ"""
        return {
            "active": [
                {
                    "name": "active-repo",
                    "url": "https://github.com/test/active-repo",
                    "pages_url": "https://test.github.io/active-repo/",
                    "description": "アクティブなリポジトリ",
                    "archived": False,
                    "has_pages": True,
                    "fork": False,
                    "updated_at": datetime(2024, 1, 1),
                    "stargazers_count": 10,
                    "language": "Python",
                    "topics": ["test", "python"],
                }
            ],
            "archived": [
                {
                    "name": "archived-repo",
                    "url": "https://github.com/test/archived-repo",
                    "pages_url": "https://test.github.io/archived-repo/",
                    "description": "アーカイブされたリポジトリ",
                    "archived": True,
                    "has_pages": False,
                    "fork": False,
                    "updated_at": datetime(2023, 12, 1),
                    "stargazers_count": 5,
                    "language": "JavaScript",
                    "topics": ["archived"],
                }
            ],
            "forks": [
                {
                    "name": "forked-repo",
                    "url": "https://github.com/test/forked-repo",
                    "pages_url": "https://test.github.io/forked-repo/",
                    "description": "フォークされたリポジトリ",
                    "archived": False,
                    "has_pages": False,
                    "fork": True,
                    "updated_at": datetime(2023, 11, 1),
                    "stargazers_count": 0,
                    "language": "Go",
                    "topics": [],
                }
            ],
        }

    @pytest.fixture
    def mock_seo_config(self):
        """SEO設定のフィクスチャ"""
        return {
            "title": "Test Title - {username}",
            "description": "{og_description}",
            "keywords": ["github", "repositories"],
        }

    @pytest.fixture
    def mock_json_ld_template(self):
        """JSON-LDテンプレートのフィクスチャ"""
        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "{username}",
            "description": "{og_description}",
        }

    def test_init(self, mock_config, mock_strings):
        """初期化テスト"""
        generator = MarkdownGenerator(mock_config, mock_strings)
        assert generator.config == mock_config
        assert generator.strings == mock_strings

    def test_init_with_jekyll_config(self, mock_config, mock_strings):
        """Jekyll設定ありの初期化テスト"""
        jekyll_config = {
            "github": {
                "username": "test_user",
                "repository_url_base": "https://github.com/test_user",
            }
        }
        generator = MarkdownGenerator(mock_config, mock_strings, jekyll_config)
        assert generator.config == mock_config
        assert generator.strings == mock_strings
        assert generator.jekyll_config == jekyll_config

    def test_init_without_jekyll_config(self, mock_config, mock_strings):
        """Jekyll設定なしの初期化テスト"""
        generator = MarkdownGenerator(mock_config, mock_strings)
        assert generator.jekyll_config == {}

    def test_generate_repo_item_basic(self, generator, sample_repos):
        """基本的なリポジトリ項目生成テスト"""
        repo = sample_repos["active"][0]
        result = generator._generate_repo_item(repo, username="test")

        assert "## [active-repo]" in result
        assert "https://test.github.io/active-repo/" in result
        assert "アクティブなリポジトリ" in result
        assert "Python-3572A5" in result  # Pythonのカスタム色が含まれていることを確認
        assert "test" in result
        assert "python" in result
        assert "GitHub Pages" in result
        assert "2024年01月01日" in result

    def test_generate_repo_item_fork(self, generator, sample_repos):
        """フォークリポジトリの項目生成テスト"""
        repo = sample_repos["forks"][0]
        result = generator._generate_repo_item(repo, is_fork=True, username="test")

        assert "Fork" in result
        assert "forked-repo" in result

    def test_generate_repo_item_no_pages(self, generator, sample_repos):
        """GitHub Pages無しリポジトリの項目生成テスト"""
        repo = sample_repos["archived"][0]
        result = generator._generate_repo_item(repo, username="test")

        assert "Pages無し" in result
        assert "https://github.com/test/archived-repo" in result

    def test_generate_section_active(self, generator, sample_repos):
        """アクティブセクション生成テスト"""
        result = generator._generate_section(sample_repos["active"], username="test")
        assert "active-repo" in result
        assert len(result) > 0

    def test_generate_section_empty_archived(self, generator):
        """空のアーカイブセクション生成テスト"""
        result = generator._generate_section([], "archived")
        assert result == "アーカイブされたリポジトリはありません。"

    def test_generate_fork_section(self, generator, sample_repos):
        """フォークセクション生成テスト"""
        result = generator._generate_fork_section(sample_repos["forks"], username="test")
        assert "forked-repo" in result
        assert "Fork" in result

    def test_generate_toc(self, generator):
        """目次生成テスト"""
        result = generator._generate_toc()
        assert "## 目次" in result
        assert "[統計情報]" in result
        assert "[アクティブなリポジトリ]" in result

    def test_generate_statistics_section(self, generator, sample_repos):
        """統計情報セクション生成テスト"""
        active = sample_repos["active"]
        archived = sample_repos["archived"]
        forks = sample_repos["forks"]

        result = generator._generate_statistics_section(active, archived, forks)

        assert "## 統計情報" in result
        assert "リポジトリ-3-blue" in result  # 総数3
        assert "アクティブ-1-green" in result  # アクティブ1
        assert "アーカイブ-1-yellow" in result  # アーカイブ1
        assert "フォーク-1-purple" in result  # フォーク1
        assert "スター-15-gold" in result  # 合計スター15

    @patch("markdown_generator.datetime")
    def test_generate_markdown_complete(
        self, mock_datetime, generator, sample_repos, mock_seo_config, mock_json_ld_template
    ):
        """完全なMarkdown生成テスト"""
        # 現在時刻をモック
        mock_now = datetime(2024, 1, 15, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        result = generator.generate_markdown(
            username="testuser",
            active=sample_repos["active"],
            archived=sample_repos["archived"],
            forks=sample_repos["forks"],
            seo_config=mock_seo_config,
            json_ld_template=mock_json_ld_template,
        )

        # フロントマターの確認
        assert "---" in result
        assert "title:" in result
        assert "testuser" in result

        # メインコンテンツの確認
        assert "# testuserのGitHubリポジトリ一覧" in result
        assert "最終更新: 2024年01月15日" in result
        assert "## 目次" in result
        assert "## 統計情報" in result
        assert "## アクティブなリポジトリ" in result
        assert "## アーカイブされたリポジトリ" in result
        assert "## フォークしたリポジトリ" in result

        # リポジトリ情報の確認
        assert "active-repo" in result
        assert "archived-repo" in result
        assert "forked-repo" in result

    def test_generate_repo_item_with_project_overview(self, generator):
        """プロジェクト概要付きリポジトリアイテム生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "project_overview": [
                "🚀 テストリポジトリの1番目の説明",
                "🔗 テストリポジトリの2番目の説明",
                "✅ テストリポジトリの3番目の説明",
            ],
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "https://github.com/testuser/test-repo" in result
        assert "**GitHub**: " in result
        assert "**GitHub Pages**: " in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # プロジェクト概要セクションの確認
        assert "### Project Highlights" in result
        assert "🚀 テストリポジトリの1番目の説明" in result
        assert "🔗 テストリポジトリの2番目の説明" in result
        assert "✅ テストリポジトリの3番目の説明" in result

    def test_generate_repo_item_without_project_overview(self, generator):
        """プロジェクト概要なしリポジトリアイテム生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            # project_overviewフィールドなし
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # プロジェクト概要セクションがないことの確認
        assert "### Project Highlights" not in result
        assert "🚀" not in result

    def test_generate_repo_item_with_readme_ja_and_pages(self, generator):
        """README.ja.md が存在しGitHub Pagesを持つリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジの確認
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "https://testuser.github.io/test-repo/README.ja.html" in result
        assert '<a href="https://testuser.github.io/test-repo/README.ja.html">' in result
        assert '<img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg">' in result

    def test_generate_repo_item_with_readme_ja_no_pages(self, generator):
        """README.ja.md が存在しGitHub Pagesを持たないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": False,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジの確認 (GitHub URLにリンク)
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "https://github.com/testuser/test-repo/blob/main/README.ja.md" in result
        assert '<a href="https://github.com/testuser/test-repo/blob/main/README.ja.md">' in result

    def test_generate_repo_item_without_readme_ja(self, generator):
        """README.ja.md が存在しないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジがないことの確認
        assert "🇯🇵" not in result
        assert "README.ja" not in result

    def test_generate_repo_item_with_readme_en_and_pages(self, generator):
        """README.html が存在しGitHub Pagesを持つリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result

        # Englishバッジの確認
        assert "🇺🇸" in result
        assert "English" in result
        assert "https://testuser.github.io/test-repo/README.html" in result
        assert '<a href="https://testuser.github.io/test-repo/README.html">' in result
        assert '<img src="https://img.shields.io/badge/🇺🇸-English-blue.svg">' in result

    def test_generate_repo_item_with_readme_en_no_pages(self, generator):
        """README.html が存在しGitHub Pagesを持たないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": False,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result

        # Englishバッジの確認 (GitHub URLにリンク)
        assert "🇺🇸" in result
        assert "English" in result
        assert "https://github.com/testuser/test-repo/blob/main/README.html" in result
        assert '<a href="https://github.com/testuser/test-repo/blob/main/README.html">' in result

    def test_generate_repo_item_with_both_readme_ja_and_en(self, generator):
        """README.ja.mdとREADME.htmlの両方が存在する場合のバッジ順序テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 両方のバッジが存在することを確認
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "🇺🇸" in result
        assert "English" in result

        # バッジの順序を確認: Japanese -> English -> GitHub Pages
        ja_badge_pos = result.find("🇯🇵")
        en_badge_pos = result.find("🇺🇸")
        pages_badge_pos = result.find("GitHub_Pages")

        assert ja_badge_pos < en_badge_pos, "Japaneseバッジが左端にあること"
        assert en_badge_pos < pages_badge_pos, "EnglishバッジがGitHub Pagesバッジの前にあること"

    def test_generate_repo_item_with_no_description(self, generator):
        """概要情報なしリポジトリの項目生成テスト（箇条書きに表示されることを確認）"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "No description available",  # 概要情報なし
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test"],
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result

        # 概要情報がない場合は箇条書きに「Overview: No description available」が表示される
        assert "**説明**: No description available" in result

        # リポジトリ名の次の行には表示されない（空行のみ）
        lines = result.split("\n")
        repo_name_index = next(i for i, line in enumerate(lines) if "## [test-repo]" in line)
        # リポジトリ名の次の行は空行であるべき
        assert lines[repo_name_index + 1] == ""


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
