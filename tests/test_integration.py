#!/usr/bin/env python3
"""統合テスト

このモジュールは全体のワークフローの統合テストを提供します。
"""

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)


class TestIntegration:
    """統合テストクラス"""

    @pytest.fixture
    def temp_config_dir(self):
        """テンポラリ設定ディレクトリのフィクスチャ"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 必要な設定ファイルを作成
            config_content = """
repository_filter:
  exclude_private: true
  require_readme: true
date_format: "%Y年%m月%d日"
statistics:
  top_languages_count: 3
language_badge:
  replacements:
    " ": "_"
topic_badge:
  replacements:
    " ": "_"
console:
  separator_length: 60
  separator_char: "="
"""

            strings_content = """
console:
  app_title: "GitHub リポジトリ一覧生成ツール"
  fetching_repos: "リポジトリ取得中: {username}"
  found_repos: "発見: {total}件"
  processing_repo: "処理中 ({current}/{total}): {name}"
  classifying: "分類中"
  sorting: "ソート中"
  filtering_repos: "フィルタリング中"
  generating_markdown: "Markdown生成中"
  saving_to: "保存中: {path}"
  saved_success: "保存完了"
  completed: "完了"
  file_size: "ファイルサイズ: {size}"
classification:
  active: "アクティブ: {count}"
  archived: "アーカイブ: {count}"
  forks: "フォーク: {count}"
markdown:
  main_title: "{username}のGitHubリポジトリ"
  last_updated: "更新日: {date}"
  sections:
    stats: "統計"
    active: "アクティブ"
    archived: "アーカイブ"
    forks: "フォーク"
  stats:
    main_languages_title: "主要言語"
    badges:
      repositories: "リポジトリ"
      active: "アクティブ"
      archived: "アーカイブ"
      forks: "フォーク"
      stars: "スター"
  processing:
    included: "✓"
    private_repo: "プライベート"
    no_readme: "README無し"
    no_description: "説明なし"
    no_pages: "Pages無し"
  repo_details:
    fork_description: "フォーク"
  section_messages:
    archived_empty: "アーカイブなし"
seo:
  og_description_template: "総計{total}個のリポジトリ"
"""

            strings_content = """
console:
  fetching_repos: "リポジトリ取得中: {username}"
  found_repos: "見つけたリポジトリ: {total}件"
  processing_repo: "処理中 ({current}/{total}): {name}"
  filtered_repos: "フィルタリング後: {count}件"
  classifying: "リポジトリを分類中..."
  sorting: "リポジトリをソート中..."
  generating_markdown: "Markdown生成中..."
classification:
  active: "アクティブ: {count}件"
  archived: "アーカイブ: {count}件"
  forks: "フォーク: {count}件"
markdown:
  main_title: "{username}のGitHubリポジトリ一覧"
  last_updated: "最終更新: {date}"
  sections:
    toc: "目次"
    stats: "統計情報"
    active: "アクティブなリポジトリ"
    archived: "アーカイブされたリポジトリ"
    forks: "フォークしたリポジトリ"
  toc_items:
    - "[統計情報](#統計情報)"
    - "[アクティブなリポジトリ](#アクティブなリポジトリ)"
  stats:
    main_languages_title: "主要言語"
    no_language_info: "言語情報なし"
    badges:
      repositories: "リポジトリ"
      active: "アクティブ"
      archived: "アーカイブ"
      forks: "フォーク"
      stars: "スター"
  processing:
    included: "✓"
    private_repo: "プライベート"
    no_readme: "README無し"
    no_description: "説明なし"
    no_pages: "Pages無し"
  repo_details:
    fork_description: "以下は他のリポジトリをフォークしたものです。"
    github_label: "GitHub"
    pages_label: "GitHub Pages"
    description_label: "説明"
  section_messages:
    archived_empty: "アーカイブなし"
seo:
  og_description_template: "総計{total}個のリポジトリ"
"""

            seo_content = """
title: "Test Title"
description: "Test Description"
"""

            json_ld_content = """
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "{username}"
}
"""

            # ファイルを作成
            Path(tmpdir, "config.yml").write_text(config_content, encoding="utf-8")
            Path(tmpdir, "strings.yml").write_text(strings_content, encoding="utf-8")
            Path(tmpdir, "seo_template.yml").write_text(seo_content, encoding="utf-8")
            Path(tmpdir, "json_ld_template.json").write_text(json_ld_content, encoding="utf-8")

            yield tmpdir

    def test_config_loading_integration(self, temp_config_dir):
        """設定読み込みの統合テスト"""
        from config_manager import ConfigManager

        config_manager = ConfigManager(script_dir=temp_config_dir)

        # 各設定ファイルが正しく読み込まれることを確認
        config = config_manager.load_config()
        strings = config_manager.load_strings()
        seo = config_manager.load_seo_template()
        json_ld = config_manager.load_json_ld_template()

        assert config["repository_filter"]["exclude_private"] is True
        assert strings["console"]["fetching_repos"] is not None
        assert seo["title"] == "Test Title"
        assert json_ld["@context"] == "https://schema.org"

    @patch("repository_processor.Github")
    def test_repository_processing_integration(self, mock_github_class, temp_config_dir):
        """リポジトリ処理の統合テスト"""
        from config_manager import ConfigManager
        from repository_processor import RepositoryProcessor

        # 設定読み込み
        config_manager = ConfigManager(script_dir=temp_config_dir)
        config = config_manager.load_config()
        strings = config_manager.load_strings()

        # プロセッサ初期化
        processor = RepositoryProcessor(config, strings)

        # モックリポジトリ作成
        mock_repo = Mock()
        mock_repo.name = "test-repo"
        mock_repo.private = False
        mock_repo.get_readme.return_value = Mock()

        # モックGitHubユーザー
        mock_github_user = Mock()
        mock_github_user.get_repos.return_value = [mock_repo]

        # テスト実行
        repos = processor.fetch_repositories(mock_github_user, "testuser")

        assert len(repos) == 1
        assert repos[0]["name"] == "test-repo"

    def test_markdown_generation_integration(self, temp_config_dir):
        """Markdown生成の統合テスト"""
        from datetime import datetime

        from config_manager import ConfigManager
        from markdown_generator import MarkdownGenerator

        # 設定読み込み
        config_manager = ConfigManager(script_dir=temp_config_dir)
        config = config_manager.load_config()
        strings = config_manager.load_strings()
        seo_config = config_manager.load_seo_template()
        json_ld_template = config_manager.load_json_ld_template()

        # ジェネレータ初期化
        generator = MarkdownGenerator(config, strings)

        # テストデータ
        sample_repo = {
            "name": "test-repo",
            "url": "https://github.com/test/test-repo",
            "pages_url": "https://test.github.io/test-repo/",
            "description": "テストリポジトリ",
            "archived": False,
            "has_pages": True,
            "fork": False,
            "updated_at": datetime(2024, 1, 1),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test"],
        }

        # Markdown生成テスト
        result = generator.generate_markdown(
            username="testuser",
            active=[sample_repo],
            archived=[],
            forks=[],
            seo_config=seo_config,
            json_ld_template=json_ld_template,
        )

        # 結果検証
        assert "testuserのGitHubリポジトリ一覧" in result
        assert "test-repo" in result
        assert "統計情報" in result
        assert "アクティブなリポジトリ" in result

    @patch.dict(os.environ, {"GITHUB_TOKEN": "test_token"})
    def test_token_acquisition_integration(self, temp_config_dir):
        """トークン取得の統合テスト"""
        from config_manager import ConfigManager

        config_manager = ConfigManager(script_dir=temp_config_dir)
        token = config_manager.get_github_token()

        assert token == "test_token"

    def test_url_safety_integration(self, temp_config_dir):
        """URL安全化の統合テスト"""
        from config_manager import ConfigManager
        from markdown_generator import MarkdownGenerator

        config_manager = ConfigManager(script_dir=temp_config_dir)
        config = config_manager.load_config()
        strings = config_manager.load_strings()

        generator = MarkdownGenerator(config, strings)

        # 複雑な文字列のURL安全化テスト
        test_cases = [
            ("C++", "C++"),  # 設定に含まれていない文字は変換されない
            ("Node.js Test", "Node.js_Test"),  # space → _
            ("Test Framework", "Test_Framework"),  # space → _
        ]

        replacements = config["language_badge"]["replacements"]
        for input_str, expected in test_cases:
            result = generator.url_utils.make_url_safe(input_str, replacements)
            assert result == expected


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
