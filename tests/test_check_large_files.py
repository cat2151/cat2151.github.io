#!/usr/bin/env python3
"""check_large_files.py のユニットテスト

このモジュールは check_large_files.py の各機能をpytestでテストします。
"""

import os
import sys

import pytest

# プロジェクトルートの.github_automationディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
script_dir = os.path.join(project_root, ".github_automation", "check_large_files", "scripts")
sys.path.insert(0, script_dir)

from check_large_files import (  # noqa: E402
    count_lines,
    find_large_files,
    generate_issue_body,
    should_exclude,
)


class TestCountLines:
    """count_lines関数のテストクラス"""

    def test_empty_file(self, tmp_path):
        """空ファイルの行数は0"""
        test_file = tmp_path / "empty.txt"
        test_file.write_bytes(b"")
        assert count_lines(str(test_file)) == 0

    def test_single_line_with_newline(self, tmp_path):
        """改行で終わる1行ファイル"""
        test_file = tmp_path / "single.txt"
        test_file.write_bytes(b"line1\n")
        assert count_lines(str(test_file)) == 1

    def test_single_line_without_newline(self, tmp_path):
        """改行で終わらない1行ファイル"""
        test_file = tmp_path / "single_no_newline.txt"
        test_file.write_bytes(b"line1")
        assert count_lines(str(test_file)) == 1

    def test_multiple_lines_with_newline(self, tmp_path):
        """改行で終わる複数行ファイル"""
        test_file = tmp_path / "multiple.txt"
        test_file.write_bytes(b"line1\nline2\nline3\n")
        assert count_lines(str(test_file)) == 3

    def test_multiple_lines_without_newline(self, tmp_path):
        """改行で終わらない複数行ファイル"""
        test_file = tmp_path / "multiple_no_newline.txt"
        test_file.write_bytes(b"line1\nline2\nline3")
        assert count_lines(str(test_file)) == 3

    def test_large_file(self, tmp_path):
        """大きなファイルのテスト（チャンク読み込みの確認）"""
        test_file = tmp_path / "large.txt"
        # 2MBを超えるファイルを作成（チャンクサイズは1MB）
        lines = 100000
        test_file.write_bytes(b"line\n" * lines)
        assert count_lines(str(test_file)) == lines

    def test_nonexistent_file(self):
        """存在しないファイルは0を返す"""
        assert count_lines("/nonexistent/file.txt") == 0


class TestShouldExclude:
    """should_exclude関数のテストクラス"""

    def test_exact_file_match(self):
        """完全一致でファイルを除外"""
        exclude_files = ["src/file.py", "test.txt"]
        assert should_exclude("src/file.py", [], exclude_files) is True
        assert should_exclude("test.txt", [], exclude_files) is True
        assert should_exclude("other.py", [], exclude_files) is False

    def test_glob_pattern_match(self):
        """グロブパターンで除外"""
        exclude_patterns = ["**/*.test.py", "**/*.md"]
        assert should_exclude("tests/test_module.test.py", exclude_patterns, []) is True
        assert should_exclude("README.md", exclude_patterns, []) is True
        assert should_exclude("src/module.py", exclude_patterns, []) is False

    def test_directory_pattern(self):
        """ディレクトリパターンで除外"""
        exclude_patterns = ["**/node_modules/**", "dist/**"]
        # Path.match matches from the right, so these patterns work differently
        assert should_exclude("src/node_modules/file.js", exclude_patterns, []) is True
        # For "dist/**" pattern with endswith check
        assert should_exclude("dist/bundle.js", exclude_patterns, []) is True
        assert should_exclude("src/main.js", exclude_patterns, []) is False

    def test_pattern_starting_with_double_star(self):
        """**/ で始まるパターンのテスト"""
        exclude_patterns = ["**/*.json"]
        assert should_exclude("config.json", exclude_patterns, []) is True
        assert should_exclude("src/config.json", exclude_patterns, []) is True

    def test_combined_patterns_and_files(self):
        """パターンとファイルリストの組み合わせ"""
        exclude_patterns = ["**/*.test.py"]
        exclude_files = ["src/main.py"]
        assert should_exclude("src/main.py", exclude_patterns, exclude_files) is True
        assert should_exclude("tests/test_main.test.py", exclude_patterns, exclude_files) is True
        assert should_exclude("src/module.py", exclude_patterns, exclude_files) is False


class TestFindLargeFiles:
    """find_large_files関数のテストクラス"""

    @pytest.fixture
    def temp_repo(self, tmp_path):
        """テスト用のリポジトリ構造を作成"""
        # ソースファイル
        src_dir = tmp_path / "src"
        src_dir.mkdir()
        (src_dir / "large.py").write_text("\n" * 600)  # 600行
        (src_dir / "small.py").write_text("\n" * 100)  # 100行

        # テストファイル
        tests_dir = tmp_path / "tests"
        tests_dir.mkdir()
        (tests_dir / "test_large.py").write_text("\n" * 700)  # 700行

        # ドキュメント
        (tmp_path / "README.md").write_text("\n" * 800)  # 800行

        return tmp_path

    def test_find_files_exceeding_threshold(self, temp_repo):
        """閾値を超えるファイルを検出"""
        config = {
            "settings": {"max_lines": 500},
            "scan": {
                "include_patterns": ["**/*"],
                "exclude_patterns": ["**/*.md", "**/tests/**"],
                "exclude_files": [],
            },
        }

        large_files = find_large_files(config, str(temp_repo))

        # src/large.py のみが検出されるべき
        assert len(large_files) == 1
        assert large_files[0]["path"] == "src/large.py"
        assert large_files[0]["lines"] == 600

    def test_exclude_patterns_work(self, temp_repo):
        """除外パターンが機能する"""
        config = {
            "settings": {"max_lines": 500},
            "scan": {
                "include_patterns": ["**/*.py"],  # Python files only
                "exclude_patterns": ["**/*.py"],  # Exclude all Python files
                "exclude_files": [],
            },
        }

        large_files = find_large_files(config, str(temp_repo))

        # すべてのPythonファイルが除外される
        assert len(large_files) == 0

    def test_no_files_exceed_threshold(self, tmp_path):
        """閾値を超えるファイルがない場合"""
        (tmp_path / "small.py").write_text("\n" * 100)

        config = {
            "settings": {"max_lines": 500},
            "scan": {
                "include_patterns": ["**/*"],
                "exclude_patterns": [],
                "exclude_files": [],
            },
        }

        large_files = find_large_files(config, str(tmp_path))
        assert len(large_files) == 0

    def test_missing_max_lines_exits(self, tmp_path):
        """max_linesが設定されていない場合は終了"""
        config = {"settings": {}, "scan": {"include_patterns": ["**/*"]}}

        with pytest.raises(SystemExit) as exc_info:
            find_large_files(config, str(tmp_path))
        assert exc_info.value.code == 1


class TestGenerateIssueBody:
    """generate_issue_body関数のテストクラス"""

    def test_single_file(self):
        """単一ファイルの場合"""
        large_files = [{"path": "src/large.py", "lines": 600}]
        config = {"settings": {"max_lines": 500}}

        body = generate_issue_body(large_files, config)

        assert "src/large.py" in body
        assert "600" in body
        assert "+100" in body  # 超過行数
        assert "リファクタリング" in body

    def test_multiple_files(self):
        """複数ファイルの場合"""
        large_files = [
            {"path": "src/file1.py", "lines": 700},
            {"path": "src/file2.py", "lines": 550},
        ]
        config = {"settings": {"max_lines": 500}}

        body = generate_issue_body(large_files, config)

        assert "src/file1.py" in body
        assert "src/file2.py" in body
        assert "700" in body
        assert "550" in body

    def test_sorted_by_line_count(self):
        """行数の多い順にソートされる"""
        large_files = [
            {"path": "src/small.py", "lines": 550},
            {"path": "src/large.py", "lines": 800},
            {"path": "src/medium.py", "lines": 650},
        ]
        config = {"settings": {"max_lines": 500}}

        body = generate_issue_body(large_files, config)

        # 大きい順に並んでいることを確認
        large_pos = body.find("src/large.py")
        medium_pos = body.find("src/medium.py")
        small_pos = body.find("src/small.py")

        assert large_pos < medium_pos < small_pos

    def test_includes_recommendations(self):
        """推奨事項が含まれる"""
        large_files = [{"path": "src/large.py", "lines": 600}]
        config = {"settings": {"max_lines": 500}}

        body = generate_issue_body(large_files, config)

        assert "推奨事項" in body
        assert "機能ごとに分割" in body
        assert "共通ロジック" in body


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
