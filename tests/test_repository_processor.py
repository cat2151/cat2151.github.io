#!/usr/bin/env python3
"""RepositoryProcessorのユニットテスト

このモジュールはRepositoryProcessorクラスの各機能をpytestでテストします。
"""

import os
import sys
from datetime import datetime
from unittest.mock import Mock

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from repository_processor import RepositoryProcessor  # noqa: E402


class TestRepositoryProcessor:
    """RepositoryProcessorのテストクラス"""

    @pytest.fixture
    def mock_config(self):
        """設定のフィクスチャ"""
        return {
            "repository_filter": {"exclude_private": True, "require_readme": True},
            "messages": {
                "included": "✓ 含める",
                "private_repo": "✗ プライベート",
                "no_readme": "✗ README無し",
                "no_description": "説明なし",
                "no_pages": "Pages無し",
            },
        }

    @pytest.fixture
    def mock_strings(self):
        """文字列リソースのフィクスチャ"""
        return {
            "console": {
                "fetching_repos": "リポジトリ取得中: {username}",
                "found_repos": "見つけたリポジトリ: {total}件",
                "processing_repo": "処理中 ({current}/{total}): {name}",
                "filtered_repos": "フィルタリング後: {count}件",
                "classifying": "リポジトリを分類中...",
                "sorting": "リポジトリをソート中...",
            },
            "classification": {
                "active": "アクティブ: {count}",
                "archived": "アーカイブ: {count}",
                "forks": "フォーク: {count}",
            },
            "markdown": {
                "processing": {
                    "included": "✓ 含める",
                    "private_repo": "✗ プライベート",
                    "no_readme": "✗ README無し",
                    "no_description": "説明なし",
                    "no_pages": "Pages無し",
                },
            },
        }

    @pytest.fixture
    def processor(self, mock_config, mock_strings):
        """RepositoryProcessorのフィクスチャ"""
        return RepositoryProcessor(mock_config, mock_strings)

    @pytest.fixture
    def mock_repo(self):
        """モックリポジトリのフィクスチャ"""
        repo = Mock()
        repo.name = "test-repo"
        repo.html_url = "https://github.com/test/test-repo"
        repo.description = "テストリポジトリ"
        repo.archived = False
        repo.has_pages = True
        repo.fork = False
        repo.updated_at = datetime(2024, 1, 1, 12, 0, 0)
        repo.stargazers_count = 5
        repo.language = "Python"
        repo.private = False
        repo.get_readme.return_value = Mock()
        repo.get_topics.return_value = ["test", "example"]
        return repo

    def test_init(self, mock_config, mock_strings):
        """初期化テスト"""
        processor = RepositoryProcessor(mock_config, mock_strings)
        assert processor.config == mock_config
        assert processor.strings == mock_strings

    def test_should_process_repo_valid(self, processor, mock_repo):
        """有効なリポジトリの処理判定テスト"""
        assert processor._should_process_repo(mock_repo) is True

    def test_should_process_repo_private(self, processor, mock_repo):
        """プライベートリポジトリの処理判定テスト"""
        mock_repo.private = True
        assert processor._should_process_repo(mock_repo) is False

    def test_should_process_repo_no_readme(self, processor, mock_repo):
        """README無しリポジトリの処理判定テスト"""
        from github.GithubException import GithubException

        mock_repo.get_readme.side_effect = GithubException(status=404, data={})
        assert processor._should_process_repo(mock_repo) is False

    def test_should_process_repo_no_readme_not_required(self, processor, mock_repo):
        """README無しでも処理対象となるテスト"""
        from github.GithubException import GithubException

        processor.config["repository_filter"]["require_readme"] = False
        mock_repo.get_readme.side_effect = GithubException(status=404, data={})
        assert processor._should_process_repo(mock_repo) is True

    def test_get_exclusion_reason_private(self, processor, mock_repo):
        """プライベートリポジトリの除外理由テスト"""
        mock_repo.private = True
        reason = processor._get_exclusion_reason(mock_repo)
        assert reason == "✗ プライベート"

    def test_get_exclusion_reason_no_readme(self, processor, mock_repo):
        """README無しの除外理由テスト"""
        from github.GithubException import GithubException

        mock_repo.private = False
        mock_repo.get_readme.side_effect = GithubException(status=404, data={})
        reason = processor._get_exclusion_reason(mock_repo)
        assert reason == "✗ README無し"

    def test_create_repo_data(self, processor, mock_repo):
        """リポジトリデータ作成テスト"""
        username = "testuser"
        data = processor._create_repo_data(mock_repo, username)

        expected = {
            "name": "test-repo",
            "url": "https://github.com/test/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "archived": False,
            "has_pages": True,
            "fork": False,
            "updated_at": datetime(2024, 1, 1, 12, 0, 0),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "example"],
        }

        assert data == expected

    def test_create_repo_data_no_description(self, processor, mock_repo):
        """説明なしリポジトリのデータ作成テスト"""
        mock_repo.description = None
        username = "testuser"
        data = processor._create_repo_data(mock_repo, username)
        assert data["description"] == "説明なし"

    def test_create_repo_data_no_language(self, processor, mock_repo):
        """言語なしリポジトリのデータ作成テスト"""
        mock_repo.language = None
        username = "testuser"
        data = processor._create_repo_data(mock_repo, username)
        assert data["language"] == ""

    def test_fetch_repositories(self, processor, mock_repo, capsys):
        """リポジトリ取得テスト"""
        # GitHub userオブジェクトをモック
        github_user = Mock()
        github_user.get_repos.return_value = [mock_repo]

        result = processor.fetch_repositories(github_user, "testuser")

        # 結果の検証
        assert len(result) == 1
        assert result[0]["name"] == "test-repo"

        # 出力の検証
        captured = capsys.readouterr()
        assert "リポジトリ取得中: testuser" in captured.out
        assert "見つけたリポジトリ: 1件" in captured.out
        assert "✓ 含める" in captured.out

    def test_fetch_repositories_with_filtered(self, processor, mock_repo, capsys):
        """フィルタリングされるリポジトリを含む取得テスト"""
        # プライベートリポジトリを追加
        private_repo = Mock()
        private_repo.name = "private-repo"
        private_repo.private = True

        github_user = Mock()
        github_user.get_repos.return_value = [mock_repo, private_repo]

        result = processor.fetch_repositories(github_user, "testuser")

        # 結果の検証（パブリックリポジトリのみ）
        assert len(result) == 1
        assert result[0]["name"] == "test-repo"

        # 出力の検証
        captured = capsys.readouterr()
        assert "見つけたリポジトリ: 2件" in captured.out
        assert "フィルタリング後: 1件" in captured.out

    def test_classify_repositories(self, processor, capsys):
        """リポジトリ分類テスト"""
        # テストデータ作成
        active_repo = {"name": "active", "archived": False, "fork": False, "updated_at": datetime(2024, 1, 3)}
        archived_repo = {"name": "archived", "archived": True, "fork": False, "updated_at": datetime(2024, 1, 2)}
        fork_repo = {"name": "fork", "archived": False, "fork": True, "updated_at": datetime(2024, 1, 1)}

        repos = [active_repo, archived_repo, fork_repo]

        active, archived, forks = processor.classify_repositories(repos)

        # 結果の検証
        assert len(active) == 1
        assert len(archived) == 1
        assert len(forks) == 1

        assert active[0]["name"] == "active"
        assert archived[0]["name"] == "archived"
        assert forks[0]["name"] == "fork"

        # 出力の検証
        captured = capsys.readouterr()
        assert "リポジトリを分類中..." in captured.out
        # 出力メッセージをテスト
        assert "アクティブ: 1" in captured.out
        assert "アーカイブ: 1" in captured.out
        assert "フォーク: 1" in captured.out

    def test_classify_repositories_sorting(self, processor):
        """リポジトリソートテスト"""
        # 日付順でソートされることをテスト
        repo1 = {"name": "repo1", "archived": False, "fork": False, "updated_at": datetime(2024, 1, 1)}
        repo2 = {"name": "repo2", "archived": False, "fork": False, "updated_at": datetime(2024, 1, 3)}
        repo3 = {"name": "repo3", "archived": False, "fork": False, "updated_at": datetime(2024, 1, 2)}

        repos = [repo1, repo2, repo3]

        active, archived, forks = processor.classify_repositories(repos)

        # 新しい順（降順）にソートされていることを確認
        assert len(active) == 3
        assert active[0]["name"] == "repo2"  # 2024/1/3
        assert active[1]["name"] == "repo3"  # 2024/1/2
        assert active[2]["name"] == "repo1"  # 2024/1/1

    def test_classify_repositories_empty(self, processor, capsys):
        """空のリポジトリリストの分類テスト"""
        repos = []

        active, archived, forks = processor.classify_repositories(repos)

        assert len(active) == 0
        assert len(archived) == 0
        assert len(forks) == 0

        # 出力の検証
        captured = capsys.readouterr()
        assert "アクティブ: 0" in captured.out
        assert "アーカイブ: 0" in captured.out
        assert "フォーク: 0" in captured.out


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
