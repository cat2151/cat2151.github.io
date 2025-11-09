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
                },
                "section_messages": {
                    "archived_empty": "アーカイブされたリポジトリはありません。",
                },
                "processing": {
                    "no_pages": "Pages無し",
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
        assert generator.github_base_url == "https://github.com/test_user"

    def test_init_without_jekyll_config(self, mock_config, mock_strings):
        """Jekyll設定なしの初期化テスト"""
        generator = MarkdownGenerator(mock_config, mock_strings)
        assert generator.jekyll_config == {}
        assert generator.github_base_url == "https://github.com"

    def test_get_github_repo_url(self, mock_config, mock_strings):
        """GitHub リポジトリURL生成テスト"""
        jekyll_config = {
            "github": {
                "username": "test_user",
                "repository_url_base": "https://github.com/test_user",
            }
        }
        generator = MarkdownGenerator(mock_config, mock_strings, jekyll_config)

        # Jekyll設定のユーザー名を使用
        url = generator._get_github_repo_url("test_repo")
        assert url == "https://github.com/test_user/test_repo"

        # 引数のユーザー名を優先（ただしベースURLは Jekyll設定のもの）
        url = generator._get_github_repo_url("test_repo", "other_user")
        assert url == "https://github.com/test_user/other_user/test_repo"

    def test_get_github_repo_url_fallback(self, mock_config, mock_strings):
        """GitHub リポジトリURL生成テスト（フォールバック）"""
        generator = MarkdownGenerator(mock_config, mock_strings)

        # Jekyll設定なしでデフォルトベースURL使用
        url = generator._get_github_repo_url("test_repo", "test_user")
        assert url == "https://github.com/test_user/test_repo"

    def test_make_url_safe(self, generator):
        """URL安全化テスト"""
        result = generator._make_url_safe("C++ Test", {"++": "plus", " ": "_"})
        assert result == "Cplus_Test"

    def test_get_top_languages(self, generator, sample_repos):
        """上位言語取得テスト"""
        all_repos = sample_repos["active"] + sample_repos["archived"] + sample_repos["forks"]
        result = generator._get_top_languages(all_repos)
        # Python, JavaScript, Go の順
        assert "Python" in result
        assert "JavaScript" in result
        assert "Go" in result

    def test_get_top_languages_empty(self, generator):
        """空のリポジトリリストでの上位言語取得テスト"""
        result = generator._get_top_languages([])
        assert result == ""

    def test_generate_language_badges(self, generator, sample_repos):
        """言語バッジ生成テスト"""
        all_repos = sample_repos["active"] + sample_repos["archived"] + sample_repos["forks"]
        total = len(all_repos)
        result = generator._generate_language_badges(all_repos, total)

        assert "Python" in result
        assert "JavaScript" in result
        assert "Go" in result
        assert "33.3%" in result  # 1/3 = 33.3%

    def test_generate_language_badges_empty(self, generator):
        """空のリポジトリリストでの言語バッジ生成テスト"""
        result = generator._generate_language_badges([], 0)
        assert result == "言語情報なし"

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

    def test_generate_frontmatter(self, generator, mock_seo_config, mock_json_ld_template):
        """フロントマター生成テスト"""
        og_description = "テスト説明文"
        result = generator._generate_frontmatter(
            username="testuser",
            og_description=og_description,
            seo_config=mock_seo_config,
            json_ld_template=mock_json_ld_template,
            total=3,
            _total_stars=15,
            _lang_list="Python、JavaScript",
        )

        assert "---" in result
        assert 'title: "Test Title - testuser"' in result
        assert 'description: "テスト説明文"' in result
        assert "json_ld: |" in result
        assert "testuser" in result


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
