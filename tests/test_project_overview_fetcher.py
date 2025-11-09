#!/usr/bin/env python3
"""ProjectOverviewFetcherのユニットテスト

このモジュールはProjectOverviewFetcherクラスの各機能をpytestでテストします。
"""

import base64
import os
import sys
from unittest.mock import Mock

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from github.GithubException import GithubException, UnknownObjectException  # noqa: E402
from project_overview_fetcher import ProjectOverviewFetcher, ProjectOverviewSectionNotFoundError  # noqa: E402


class TestProjectOverviewFetcher:
    """ProjectOverviewFetcherのテストクラス"""

    @pytest.fixture
    def mock_github_api(self):
        """GitHub APIクライアントのモック"""
        return Mock()

    @pytest.fixture
    def mock_config(self):
        """設定のフィクスチャ"""
        return {
            "project_overview": {
                "enabled": True,
                "target_file": "generated-docs/project-overview.md",
                "section_title": "プロジェクト概要",
                "max_retries": 1,
                "timeout_seconds": 10,
                "enable_cache": True,
                "parallel_fetch": False,
            }
        }

    @pytest.fixture
    def mock_config_disabled(self):
        """機能無効設定のフィクスチャ"""
        return {
            "project_overview": {
                "enabled": False,
                "target_file": "generated-docs/project-overview.md",
                "section_title": "プロジェクト概要",
                "max_retries": 1,
                "timeout_seconds": 10,
                "enable_cache": True,
                "parallel_fetch": False,
            }
        }

    @pytest.fixture
    def fetcher(self, mock_github_api, mock_config):
        """ProjectOverviewFetcherのフィクスチャ"""
        return ProjectOverviewFetcher(mock_github_api, mock_config)

    @pytest.fixture
    def sample_markdown_content(self):
        """サンプルMarkdownコンテンツ"""
        return """# プロジェクトタイトル

## プロジェクト概要
- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に
- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK
- ✅ メンテは一括、プロジェクト開発に集中できます

## その他のセクション
他の内容...
"""

    def test_init_with_config(self, mock_github_api, mock_config):
        """設定付き初期化のテスト"""
        fetcher = ProjectOverviewFetcher(mock_github_api, mock_config)

        assert fetcher.github == mock_github_api
        assert fetcher.config == mock_config
        assert fetcher.enabled is True
        assert fetcher.target_file == "generated-docs/project-overview.md"
        assert fetcher.section_title == "プロジェクト概要"
        assert fetcher.max_retries == 1
        assert fetcher.enable_cache is True

    def test_init_with_defaults(self, mock_github_api):
        """デフォルト設定での初期化のテスト"""
        config = {}
        fetcher = ProjectOverviewFetcher(mock_github_api, config)

        assert fetcher.enabled is True
        assert fetcher.target_file == "generated-docs/project-overview.md"
        assert fetcher.section_title == "プロジェクト概要"
        assert fetcher.max_retries == 1

    def test_fetch_overview_disabled(self, mock_github_api, mock_config_disabled):
        """機能が無効の場合のテスト"""
        fetcher = ProjectOverviewFetcher(mock_github_api, mock_config_disabled)
        result = fetcher.fetch_overview("test-repo", "test-user")

        assert result == []
        assert not mock_github_api.get_repo.called

    def test_fetch_overview_file_not_exists(self, fetcher):
        """ファイルが存在しない場合のテスト"""
        # モック設定
        mock_repo = Mock()
        mock_repo.get_contents.side_effect = UnknownObjectException(404, "Not Found")
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher.fetch_overview("test-repo", "test-user")

        assert result == []
        fetcher.github.get_repo.assert_called_with("test-user/test-repo")

    def test_fetch_overview_success(self, fetcher, sample_markdown_content):
        """正常に概要を取得する場合のテスト"""
        # モック設定
        mock_file_content = Mock()
        mock_file_content.content = base64.b64encode(sample_markdown_content.encode("utf-8")).decode("utf-8")

        mock_repo = Mock()
        mock_repo.get_contents.return_value = mock_file_content
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher.fetch_overview("test-repo", "test-user")

        expected = [
            "- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に",
            "- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK",
            "- ✅ メンテは一括、プロジェクト開発に集中できます",
        ]
        assert result == expected

    def test_fetch_overview_with_cache(self, fetcher, sample_markdown_content):
        """キャッシュ機能のテスト"""
        # モック設定
        mock_file_content = Mock()
        mock_file_content.content = base64.b64encode(sample_markdown_content.encode("utf-8")).decode("utf-8")

        mock_repo = Mock()
        mock_repo.get_contents.return_value = mock_file_content
        fetcher.github.get_repo.return_value = mock_repo

        # 1回目の呼び出し
        result1 = fetcher.fetch_overview("test-repo", "test-user")
        # 2回目の呼び出し（キャッシュから取得）
        result2 = fetcher.fetch_overview("test-repo", "test-user")

        # 結果は同じ
        assert result1 == result2
        # GitHub APIは1回だけ呼ばれる
        assert fetcher.github.get_repo.call_count == 2  # _check_file_exists と _fetch_markdown_content で2回

    def test_check_file_exists_true(self, fetcher):
        """ファイル存在確認：存在する場合"""
        mock_repo = Mock()
        mock_repo.get_contents.return_value = Mock()
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher._check_file_exists("test-repo", "test-user")

        assert result is True
        fetcher.github.get_repo.assert_called_with("test-user/test-repo")
        mock_repo.get_contents.assert_called_with("generated-docs/project-overview.md")

    def test_check_file_exists_false(self, fetcher):
        """ファイル存在確認：存在しない場合"""
        mock_repo = Mock()
        mock_repo.get_contents.side_effect = UnknownObjectException(404, "Not Found")
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher._check_file_exists("test-repo", "test-user")

        assert result is False

    def test_parse_overview_section_success(self, fetcher, sample_markdown_content):
        """プロジェクト概要セクションの正常パース"""
        result = fetcher._parse_overview_section(sample_markdown_content)

        expected = [
            "- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に",
            "- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK",
            "- ✅ メンテは一括、プロジェクト開発に集中できます",
        ]
        assert result == expected

    def test_parse_overview_section_not_found(self, fetcher):
        """プロジェクト概要セクションが見つからない場合は例外発生"""
        markdown_content = """# プロジェクトタイトル

## はじめに
説明文

## 機能
- 機能1
- 機能2
"""
        with pytest.raises(ProjectOverviewSectionNotFoundError):
            fetcher._parse_overview_section(markdown_content)

    def test_extract_bullet_points_max_three(self, fetcher):
        """箇条書き抽出：最大3行のテスト"""
        section_content = """- 1行目の説明
- 2行目の説明
- 3行目の説明
- 4行目の説明（これは含まれない）
- 5行目の説明（これも含まれない）"""

        result = fetcher._extract_bullet_points(section_content)

        assert len(result) == 3
        assert result[0] == "- 1行目の説明"
        assert result[1] == "- 2行目の説明"
        assert result[2] == "- 3行目の説明"

    def test_extract_bullet_points_mixed_content(self, fetcher):
        """箇条書き抽出：混在コンテンツのテスト"""
        section_content = """説明文

- 🚀 1行目の説明
通常のテキスト
- 🔗 2行目の説明

- ✅ 3行目の説明
その他の内容"""

        result = fetcher._extract_bullet_points(section_content)

        assert len(result) == 3
        assert "🚀" in result[0]
        assert "🔗" in result[1]
        assert "✅" in result[2]

    def test_extract_bullet_points_empty(self, fetcher):
        """箇条書き抽出：空のセクションのテスト"""
        result = fetcher._extract_bullet_points("")
        assert result == []

    def test_get_statistics(self, fetcher):
        """統計情報取得のテスト"""
        # キャッシュにデータを追加
        fetcher.cache = {
            "user1/repo1": ["- 説明1", "- 説明2"],
            "user2/repo2": [],  # 失敗ケース
            "user3/repo3": ["- 説明3"],
        }

        stats = fetcher.get_statistics()

        assert stats["cache_size"] == 3
        assert stats["success_count"] == 2  # 成功は2件
        assert stats["enabled"] is True

    def test_clear_cache(self, fetcher):
        """キャッシュクリアのテスト"""
        # キャッシュにデータを追加
        fetcher.cache = {"user1/repo1": ["• 説明1"]}

        fetcher.clear_cache()

        assert len(fetcher.cache) == 0

    def test_github_exception_handling(self, fetcher):
        """GitHub例外のハンドリングテスト"""
        mock_repo = Mock()
        mock_repo.get_contents.side_effect = GithubException(500, "Internal Server Error")
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher.fetch_overview("test-repo", "test-user")

        assert result == []

    def test_retry_mechanism(self, fetcher):
        """リトライ機能のテスト"""
        # 1回目は失敗、2回目は成功のシナリオ
        mock_file_content = Mock()
        mock_file_content.content = base64.b64encode("## プロジェクト概要\n- テスト".encode("utf-8")).decode("utf-8")

        mock_repo = Mock()
        # ファイル存在確認は成功
        mock_repo.get_contents.side_effect = [
            Mock(),  # _check_file_exists用
            GithubException(500, "Server Error"),  # 1回目の失敗
            mock_file_content,  # 2回目の成功
        ]
        fetcher.github.get_repo.return_value = mock_repo

        result = fetcher.fetch_overview("test-repo", "test-user")

        assert result == ["- テスト"]
        # get_contents が3回呼ばれる（存在確認1回 + リトライ2回）
        assert mock_repo.get_contents.call_count == 3

    def test_extract_bullet_points_different_markers(self, fetcher):
        """箇条書き抽出：ハイフンのみ対応の確認テスト"""
        section_content = """説明文

• 🚀 ビューレット記号での説明（対応していない）
- 🔗 ハイフンでの説明（対応している）
* ✅ アスタリスクでの説明（対応していない）

その他の内容"""

        result = fetcher._extract_bullet_points(section_content)

        # ハイフンのみ抽出される
        assert len(result) == 1
        assert "🔗" in result[0] and result[0].startswith("- ")

    def test_extract_bullet_points_hyphen_only(self, fetcher):
        """箇条書き抽出：ハイフンのみのテスト（実際のgithub-actionsリポジトリ形式）"""
        section_content = """- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に
- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK
- ✅ メンテは一括、プロジェクト開発に集中できます"""

        result = fetcher._extract_bullet_points(section_content)

        assert len(result) == 3
        assert result[0] == "- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に"
        assert result[1] == "- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK"
        assert result[2] == "- ✅ メンテは一括、プロジェクト開発に集中できます"

    def test_extract_bullet_points_no_bullets(self, fetcher):
        """箇条書き抽出：箇条書きがない場合のテスト"""
        section_content = """プロジェクトの説明

これは通常のテキストです。
改行もあります。

+ プラス記号は対応していません
> 引用も対応していません"""

        result = fetcher._extract_bullet_points(section_content)
        assert result == []

    def test_parse_overview_section_missing_raises_exception(self, fetcher):
        """プロジェクト概要セクションが見つからない場合は例外発生"""
        markdown_content = """# プロジェクトタイトル

## はじめに
説明文

## 機能
- 機能1
- 機能2
"""
        with pytest.raises(ProjectOverviewSectionNotFoundError) as exc_info:
            fetcher._parse_overview_section(markdown_content)

        assert "プロジェクト概要セクション" in str(exc_info.value)
        assert "が見つかりません" in str(exc_info.value)

    def test_fetch_overview_section_not_found_raises_exception(self, fetcher):
        """fetch_overview: ファイルは存在するがセクションが見つからない場合は例外発生"""
        # モック設定: ファイルは存在するが、プロジェクト概要セクションがない
        markdown_content = """# プロジェクトタイトル

## はじめに
説明文

## 機能
- 機能1
- 機能2
"""
        mock_file_content = Mock()
        mock_file_content.content = base64.b64encode(markdown_content.encode("utf-8")).decode("utf-8")

        mock_repo = Mock()
        mock_repo.get_contents.return_value = mock_file_content
        fetcher.github.get_repo.return_value = mock_repo

        with pytest.raises(ProjectOverviewSectionNotFoundError):
            fetcher.fetch_overview("test-repo", "test-user")
