#!/usr/bin/env python3
"""ReadmeBadgeExtractorのユニットテスト

このモジュールはReadmeBadgeExtractorクラスの各機能をpytestでテストします。
"""

import os
import sys
from unittest.mock import Mock

import pytest
from github.GithubException import GithubException

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from readme_badge_extractor import ReadmeBadgeExtractor  # noqa: E402


class TestReadmeBadgeExtractor:
    """ReadmeBadgeExtractorのテストクラス"""

    @pytest.fixture
    def extractor(self):
        """ReadmeBadgeExtractorのフィクスチャ"""
        return ReadmeBadgeExtractor()

    @pytest.fixture
    def mock_repo_with_badges(self):
        """バッジ付きREADMEを持つモックリポジトリ"""

        repo = Mock()
        repo.name = "test-repo"

        # バッジを含むREADME
        readme_content = """# Test Repository

[![DeepWiki](https://img.shields.io/badge/DeepWiki-test--repo-blue)](https://deepwiki.com/user/test-repo)
![CI](https://github.com/user/test-repo/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/user/test-repo/branch/main/graph/badge.svg)](https://codecov.io/gh/user/test-repo)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Description

This is a test repository.
"""
        mock_readme = Mock()
        mock_readme.decoded_content = readme_content.encode("utf-8")
        repo.get_readme.return_value = mock_readme

        return repo

    @pytest.fixture
    def mock_repo_no_badges(self):
        """バッジなしREADMEを持つモックリポジトリ"""
        repo = Mock()
        repo.name = "test-repo"

        readme_content = """# Test Repository

## Description

This is a test repository without badges.
"""
        mock_readme = Mock()
        mock_readme.decoded_content = readme_content.encode("utf-8")
        repo.get_readme.return_value = mock_readme

        return repo

    @pytest.fixture
    def mock_repo_no_readme(self):
        """README.mdを持たないモックリポジトリ"""
        repo = Mock()
        repo.name = "test-repo"
        repo.get_readme.side_effect = GithubException(status=404, data={})

        return repo

    def test_extract_badges_from_readme_with_badges(self, extractor, mock_repo_with_badges):
        """バッジ付きREADMEからバッジを正しく抽出できるか"""
        badges = extractor.extract_badges_from_readme(mock_repo_with_badges)

        # バッジが抽出されていることを確認
        assert len(badges) > 0

        # DeepWikiバッジが含まれていることを確認
        deepwiki_badges = [b for b in badges if b["type"] == "deepwiki"]
        assert len(deepwiki_badges) == 1
        assert "deepwiki.com" in deepwiki_badges[0]["link_url"]  # noqa: S105 (test assertion)

        # CI/CDバッジが含まれていることを確認
        ci_badges = [b for b in badges if b["type"] == "ci_cd"]
        assert len(ci_badges) > 0

        # Coverageバッジが含まれていることを確認
        coverage_badges = [b for b in badges if b["type"] == "coverage"]
        assert len(coverage_badges) == 1

        # Licenseバッジが含まれていることを確認
        license_badges = [b for b in badges if b["type"] == "license"]
        assert len(license_badges) == 1

    def test_extract_badges_from_readme_no_badges(self, extractor, mock_repo_no_badges):
        """バッジなしREADMEからは空のリストが返されるか"""
        badges = extractor.extract_badges_from_readme(mock_repo_no_badges)
        assert len(badges) == 0

    def test_extract_badges_from_readme_no_readme(self, extractor, mock_repo_no_readme):
        """README.mdがない場合は空のリストが返されるか"""
        badges = extractor.extract_badges_from_readme(mock_repo_no_readme)
        assert len(badges) == 0

    def test_parse_badges_markdown_format(self, extractor):
        """Markdown形式のバッジを正しく解析できるか"""
        content = """# Test

[![Build](https://img.shields.io/badge/build-passing-green)](https://example.com/build)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

## Content
"""
        badges = extractor._parse_badges_from_content(content)

        assert len(badges) == 2
        # クリック可能なバッジ
        assert badges[0]["link_url"] == "https://example.com/build"
        # クリック不可能なバッジ
        assert badges[1]["link_url"] is None

    def test_parse_badges_html_format(self, extractor):
        """HTML形式のバッジを正しく解析できるか"""
        content = """# Test

<a href="https://example.com"><img src="https://img.shields.io/badge/test-badge-blue.svg" alt="Test Badge"></a>

## Content
"""
        badges = extractor._parse_badges_from_content(content)

        assert len(badges) == 1
        assert badges[0]["link_url"] == "https://example.com"
        assert badges[0]["alt_text"] == "Test Badge"

    def test_identify_badge_type_deepwiki(self, extractor):
        """DeepWikiバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "[![DeepWiki](https://img.shields.io/badge/DeepWiki-test-blue)](https://deepwiki.com/user/test)",
            "DeepWiki",
            "https://img.shields.io/badge/DeepWiki-test-blue",
            "https://deepwiki.com/user/test",
        )
        assert badge_type == "deepwiki"

    def test_identify_badge_type_deepseek(self, extractor):
        """DeepSeekバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "[![DeepSeek](https://img.shields.io/badge/DeepSeek-wiki-blue)](https://deepseek.com/user/test)",
            "DeepSeek",
            "https://img.shields.io/badge/DeepSeek-wiki-blue",
            "https://deepseek.com/user/test",
        )
        assert badge_type == "deepseek_wiki"

    def test_identify_badge_type_livedemo(self, extractor):
        """LiveDemoバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "[![LiveDemo](https://img.shields.io/badge/Live-Demo-green)](https://example.com/demo)",
            "LiveDemo",
            "https://img.shields.io/badge/Live-Demo-green",
            "https://example.com/demo",
        )
        assert badge_type == "livedemo"

    def test_identify_badge_type_ci_cd(self, extractor):
        """CI/CDバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "![CI](https://github.com/user/repo/workflows/CI/badge.svg)",
            "CI",
            "https://github.com/user/repo/workflows/CI/badge.svg",
            None,
        )
        assert badge_type == "ci_cd"

    def test_identify_badge_type_coverage(self, extractor):
        """Coverageバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "[![codecov](https://codecov.io/gh/user/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/user/repo)",
            "codecov",
            "https://codecov.io/gh/user/repo/branch/main/graph/badge.svg",
            "https://codecov.io/gh/user/repo",
        )
        assert badge_type == "coverage"

    def test_identify_badge_type_license(self, extractor):
        """Licenseバッジを正しく識別できるか"""
        badge_type = extractor._identify_badge_type(
            "![License](https://img.shields.io/badge/License-MIT-green.svg)",
            "License",
            "https://img.shields.io/badge/License-MIT-green.svg",
            None,
        )
        assert badge_type == "license"

    def test_get_badge_priority(self, extractor):
        """バッジの優先順位が正しく設定されているか"""
        # 既知のバッジタイプ
        assert extractor._get_badge_priority("japanese") == 0
        assert extractor._get_badge_priority("deepwiki") == 7

        # 新しいバッジタイプ
        assert extractor._get_badge_priority("deepseek_wiki") == 8
        assert extractor._get_badge_priority("livedemo") == 9
        assert extractor._get_badge_priority("ci_cd") == 10
        assert extractor._get_badge_priority("coverage") == 11
        assert extractor._get_badge_priority("license") == 12

        # カスタムバッジ
        assert extractor._get_badge_priority("custom") == 999

    def test_badges_only_from_header_section(self, extractor):
        """バッジがヘッダーセクションからのみ抽出されるか"""
        content = """# Test Repository

![Badge1](https://img.shields.io/badge/header-badge-blue)

## Section 1

![Badge2](https://img.shields.io/badge/section-badge-red)

This badge should not be extracted.
"""
        badges = extractor._parse_badges_from_content(content)

        # ヘッダーセクションのバッジのみが抽出される
        assert len(badges) == 1
        assert "header-badge" in badges[0]["image_url"]
        assert "section-badge" not in str(badges)

    def test_stops_at_double_hash_heading(self, extractor):
        """## 見出しで抽出が停止するか"""
        content = """# Test Repository

![Badge1](https://img.shields.io/badge/before-heading-blue)

## First Heading

![Badge2](https://img.shields.io/badge/after-heading-red)
"""
        badges = extractor._parse_badges_from_content(content)

        # ## より前のバッジのみが抽出される
        assert len(badges) == 1
        assert "before-heading" in badges[0]["image_url"]
