"""Shared pytest fixtures for repository tests."""

import os
import sys
from datetime import datetime

import pytest

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from markdown_generator import MarkdownGenerator  # noqa: E402


@pytest.fixture
def mock_config():
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
def mock_strings():
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
def generator(mock_config, mock_strings):
    """MarkdownGeneratorのフィクスチャ"""
    return MarkdownGenerator(mock_config, mock_strings)


@pytest.fixture
def sample_repos():
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
def mock_seo_config():
    """SEO設定のフィクスチャ"""
    return {
        "title": "Test Title - {username}",
        "description": "{og_description}",
        "keywords": ["github", "repositories"],
    }


@pytest.fixture
def mock_json_ld_template():
    """JSON-LDテンプレートのフィクスチャ"""
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "{username}",
        "description": "{og_description}",
    }
