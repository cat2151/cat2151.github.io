#!/usr/bin/env python3
"""BadgeGeneratorの統合テスト

このモジュールはBadgeGeneratorクラスのバッジマージング機能をテストします。
"""

import os
import sys

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from badge_generator import BadgeGenerator  # noqa: E402


class TestBadgeGeneratorIntegration:
    """BadgeGeneratorの統合テストクラス"""

    @pytest.fixture
    def config(self):
        """設定のフィクスチャ"""
        return {
            "language_badge": {"replacements": {"+": "%2B", " ": "_", "#": "%23"}},
            "topic_badge": {"replacements": {"-": "--", "_": "__", " ": "_"}},
        }

    @pytest.fixture
    def strings(self):
        """文字列リソースのフィクスチャ"""
        return {}

    @pytest.fixture
    def badge_generator(self, config, strings):
        """BadgeGeneratorのフィクスチャ"""
        return BadgeGenerator(config, strings)

    def test_readme_badges_appended_after_existing(self, badge_generator):
        """README.mdから抽出されたバッジが既存バッジの後に追加されるか"""
        repo = {
            "name": "test-repo",
            "has_readme_ja": False,
            "has_readme_en": False,
            "has_pages": True,
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test"],
            "readme_badges": [
                {
                    "markdown": "[![CI](https://img.shields.io/badge/CI-passing-green)](https://ci.example.com)",
                    "type": "ci_cd",
                    "priority": 10,
                    "alt_text": "CI",
                    "image_url": "https://img.shields.io/badge/CI-passing-green",
                    "link_url": "https://ci.example.com",
                }
            ],
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # バッジが含まれていることを確認
        assert "GitHub_Pages" in badges  # 既存バッジ
        assert "Python" in badges  # 既存バッジ
        assert "CI-passing" in badges  # READMEバッジ

        # 順序を確認（既存バッジが先）
        github_pages_pos = badges.index("GitHub_Pages")
        python_pos = badges.index("Python")
        ci_pos = badges.index("CI-passing")

        assert github_pages_pos < ci_pos
        assert python_pos < ci_pos

    def test_priority_based_sorting(self, badge_generator):
        """優先順位に基づいてバッジがソートされるか"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/test/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "has_readme_ja": True,
            "has_readme_en": False,
            "has_pages": True,
            "stargazers_count": 10,
            "language": "JavaScript",
            "topics": [],
            "readme_badges": [
                {
                    "markdown": "[![Coverage](https://img.shields.io/badge/coverage-90-green)](https://example.com)",
                    "type": "coverage",
                    "priority": 11,
                    "alt_text": "Coverage",
                    "image_url": "https://img.shields.io/badge/coverage-90-green",
                    "link_url": "https://example.com",
                },
                {
                    "markdown": "[![CI](https://img.shields.io/badge/CI-passing-green)](https://ci.example.com)",
                    "type": "ci_cd",
                    "priority": 10,
                    "alt_text": "CI",
                    "image_url": "https://img.shields.io/badge/CI-passing-green",
                    "link_url": "https://ci.example.com",
                },
            ],
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # 既存バッジが最初に来る
        assert badges.startswith("<a href=")  # Japanese badge (priority 0)

        # README バッジの中では CI (priority 10) が Coverage (priority 11) より先
        ci_pos = badges.index("CI-passing")
        coverage_pos = badges.index("coverage-90")
        assert ci_pos < coverage_pos

    def test_deduplication_prevents_duplicate_badge_types(self, badge_generator):
        """重複したバッジタイプが除外されるか（言語バッジはREADMEバッジより既存バッジを優先）"""
        repo = {
            "name": "test-repo",
            "has_readme_ja": False,
            "has_readme_en": False,
            "has_pages": False,
            "stargazers_count": 0,
            "language": "Python",
            "topics": [],
            "readme_badges": [
                {
                    "markdown": "![Python](https://img.shields.io/badge/Python-blue)",
                    "type": "language",  # 既存のlanguageバッジと重複
                    "priority": 5,
                    "alt_text": "Python",
                    "image_url": "https://img.shields.io/badge/Python-blue",
                    "link_url": None,
                }
            ],
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # languageタイプのバッジは既存のものが優先され、READMEバッジは除外される
        # 既存のPythonバッジ（色付き、ロゴ付き）のみが表示される
        assert "Python" in badges
        assert "3572A5" in badges  # 既存バッジの色コード
        # READMEバッジ（シンプルなblue）は含まれない
        assert "Python-blue" not in badges  # READMEバッジのパターンは含まれない

    def test_readme_badge_priority_offset_applied(self, badge_generator):
        """README_BADGE_PRIORITY_OFFSETが正しく適用されるか"""
        repo = {
            "name": "test-repo",
            "has_readme_ja": False,
            "has_readme_en": False,
            "has_pages": False,
            "stargazers_count": 0,
            "language": None,
            "topics": [],
            "readme_badges": [
                {
                    "markdown": "[![Custom](https://img.shields.io/badge/Custom-badge-red)](https://example.com)",
                    "type": "custom",
                    "priority": 999,  # 元の優先度
                    "alt_text": "Custom",
                    "image_url": "https://img.shields.io/badge/Custom-badge-red",
                    "link_url": "https://example.com",
                },
                {
                    "markdown": "[![CI](https://img.shields.io/badge/CI-passing-green)](https://ci.example.com)",
                    "type": "ci_cd",
                    "priority": 10,
                    "alt_text": "CI",
                    "image_url": "https://img.shields.io/badge/CI-passing-green",
                    "link_url": "https://ci.example.com",
                },
            ],
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # README_BADGE_PRIORITY_OFFSET (100) が適用されるため
        # CI (10 + 100 = 110) が Custom (999 + 100 = 1099) より先
        ci_pos = badges.index("CI-passing")
        custom_pos = badges.index("Custom-badge")
        assert ci_pos < custom_pos

    def test_empty_readme_badges_handled(self, badge_generator):
        """readme_badgesが空の場合も正常に動作するか"""
        repo = {
            "name": "test-repo",
            "has_readme_ja": False,
            "has_readme_en": False,
            "has_pages": True,
            "stargazers_count": 0,
            "language": "Python",
            "topics": [],
            "readme_badges": [],
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # 既存バッジのみが表示される
        assert "GitHub_Pages" in badges
        assert "Python" in badges

    def test_readme_badges_field_missing(self, badge_generator):
        """readme_badgesフィールドがない場合も正常に動作するか"""
        repo = {
            "name": "test-repo",
            "has_readme_ja": False,
            "has_readme_en": False,
            "has_pages": True,
            "stargazers_count": 0,
            "language": "Python",
            "topics": [],
            # readme_badges フィールドなし
        }

        badges = badge_generator.generate_repository_badges(repo, username="testuser")

        # 既存バッジのみが表示される
        assert "GitHub_Pages" in badges
        assert "Python" in badges
