#!/usr/bin/env python3
"""ConfigManagerのユニットテスト

このモジュールはConfigManagerクラスの各機能をpytestでテストします。
"""

import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from config_manager import ConfigManager  # noqa: E402


class TestConfigManager:
    """ConfigManagerのテストクラス"""

    @pytest.fixture
    def temp_dir(self):
        """テンポラリディレクトリのフィクスチャ"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield tmpdir

    @pytest.fixture
    def mock_config_files(self, temp_dir):
        """モック設定ファイルのフィクスチャ"""
        config_data = {
            "repository_filter": {"exclude_private": True, "require_readme": True},
            "messages": {"included": "✓", "private_repo": "プライベート", "no_readme": "README無し"},
        }

        strings_data = {"console": {"fetching_repos": "取得中: {username}", "found_repos": "発見: {total}件"}}

        seo_data = {"title": "Test Title", "description": "Test Description"}

        json_ld_data = {"@context": "https://schema.org", "@type": "Person", "name": "{username}"}

        # ファイルを作成
        config_path = Path(temp_dir) / "config.yml"
        strings_path = Path(temp_dir) / "strings.yml"
        seo_path = Path(temp_dir) / "seo_template.yml"
        json_ld_path = Path(temp_dir) / "json_ld_template.json"

        with open(config_path, "w", encoding="utf-8") as f:
            yaml.dump(config_data, f)
        with open(strings_path, "w", encoding="utf-8") as f:
            yaml.dump(strings_data, f)
        with open(seo_path, "w", encoding="utf-8") as f:
            yaml.dump(seo_data, f)
        with open(json_ld_path, "w", encoding="utf-8") as f:
            json.dump(json_ld_data, f)

        return {"config": config_data, "strings": strings_data, "seo": seo_data, "json_ld": json_ld_data}

    def test_init_default_script_dir(self):
        """デフォルトスクリプトディレクトリの初期化テスト"""
        config_manager = ConfigManager()
        assert config_manager.script_dir is not None
        assert os.path.exists(config_manager.script_dir)

    def test_init_custom_script_dir(self, temp_dir):
        """カスタムスクリプトディレクトリの初期化テスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        assert config_manager.script_dir == temp_dir

    def test_load_config(self, temp_dir, mock_config_files):
        """設定ファイル読み込みテスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        config = config_manager.load_config()

        assert config == mock_config_files["config"]
        assert config["repository_filter"]["exclude_private"] is True

    def test_load_strings(self, temp_dir, mock_config_files):
        """文字列リソース読み込みテスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        strings = config_manager.load_strings()

        assert strings == mock_config_files["strings"]
        assert "console" in strings

    def test_load_seo_template(self, temp_dir, mock_config_files):
        """SEOテンプレート読み込みテスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        seo = config_manager.load_seo_template()

        assert seo == mock_config_files["seo"]
        assert "title" in seo

    def test_load_json_ld_template(self, temp_dir, mock_config_files):
        """JSON-LDテンプレート読み込みテスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        json_ld = config_manager.load_json_ld_template()

        assert json_ld == mock_config_files["json_ld"]
        assert json_ld["@context"] == "https://schema.org"

    def test_caching(self, temp_dir, mock_config_files):
        """キャッシュ機能テスト"""
        config_manager = ConfigManager(script_dir=temp_dir)

        # 最初の読み込み
        config1 = config_manager.load_config()
        # 2回目の読み込み（キャッシュから）
        config2 = config_manager.load_config()

        assert config1 is config2  # 同一オブジェクトであることを確認

    @patch.dict(os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_TOKEN": "test_token"})
    def test_is_github_actions_environment_true(self):
        """GitHub Actions環境判定テスト（True）"""
        config_manager = ConfigManager()
        assert config_manager.is_github_actions_environment() is True

    @patch.dict(os.environ, {}, clear=True)
    def test_is_github_actions_environment_false(self):
        """GitHub Actions環境判定テスト（False）"""
        config_manager = ConfigManager()
        assert config_manager.is_github_actions_environment() is False

    @patch.dict(os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_TOKEN": "gh_actions_token"})
    def test_get_github_token_github_actions(self):
        """GitHub Actions環境でのトークン取得テスト"""
        config_manager = ConfigManager()
        token = config_manager.get_github_token()
        assert token == "gh_actions_token"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_github_token_local_secrets(self, temp_dir):
        """ローカル環境でのsecretsファイルからのトークン取得テスト"""
        # ConfigManagerの実際のディレクトリ構造を模倣
        # temp_dir/src/generate_repo_list -> temp_dir/secrets/secrets.toml
        src_dir = Path(temp_dir) / "src" / "generate_repo_list"
        src_dir.mkdir(parents=True, exist_ok=True)

        secrets_dir = Path(temp_dir) / "secrets"
        secrets_dir.mkdir(exist_ok=True)
        secrets_file = secrets_dir / "secrets.toml"

        with open(secrets_file, "w", encoding="utf-8") as f:
            f.write('[github]\ntoken = "local_token"\n')

        config_manager = ConfigManager(script_dir=str(src_dir))
        token = config_manager.get_github_token()
        assert token == "local_token"

    @patch.dict(os.environ, {"GITHUB_TOKEN": "env_token"}, clear=False)
    def test_get_github_token_fallback_env(self, temp_dir):
        """環境変数フォールバックでのトークン取得テスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        token = config_manager.get_github_token()
        assert token == "env_token"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_github_token_no_token(self, temp_dir):
        """トークンが見つからない場合のテスト"""
        config_manager = ConfigManager(script_dir=temp_dir)
        token = config_manager.get_github_token()
        assert token == ""

    def test_load_secrets_file_not_exists(self, temp_dir):
        """secretsファイルが存在しない場合のテスト"""
        # 新しい独立したテンポラリディレクトリを作成
        with tempfile.TemporaryDirectory() as isolated_temp_dir:
            # プロジェクト構造を模擬: generate_repo_list ディレクトリを作成
            script_dir = Path(isolated_temp_dir) / "src" / "generate_repo_list"
            script_dir.mkdir(parents=True, exist_ok=True)

            config_manager = ConfigManager(script_dir=str(script_dir))
            secrets = config_manager.load_secrets()
            assert secrets == {}

    def test_get_username_from_secrets(self):
        """secretsファイルからusernameを取得するテスト"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # secrets ディレクトリとファイルを作成 (実際のプロジェクト構造に合わせる)
            # temp_dir は generate_repo_list ディレクトリ相当
            # secrets は src の兄弟ディレクトリ（2階層上の兄弟）
            src_dir = Path(temp_dir).parent  # src 相当
            project_root = src_dir.parent  # プロジェクトルート相当
            secrets_dir = project_root / "secrets"
            secrets_dir.mkdir(exist_ok=True)
            secrets_file = secrets_dir / "secrets.toml"
            with open(secrets_file, "w", encoding="utf-8") as f:
                f.write('[github]\nusername = "test_user"\n')

            config_manager = ConfigManager(script_dir=str(temp_dir))
            username = config_manager.get_username()
            assert username == "test_user"

    @patch.dict(os.environ, {"GITHUB_USERNAME": "env_user"}, clear=False)
    def test_get_username_from_env(self):
        """環境変数からusernameを取得するテスト"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # プロジェクト構造を模擬: generate_repo_list ディレクトリを作成
            script_dir = Path(temp_dir) / "src" / "generate_repo_list"
            script_dir.mkdir(parents=True, exist_ok=True)

            config_manager = ConfigManager(script_dir=str(script_dir))
            username = config_manager.get_username()
            assert username == "env_user"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_username_no_username(self):
        """usernameが見つからない場合のテスト"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # プロジェクト構造を模擬: generate_repo_list ディレクトリを作成
            script_dir = Path(temp_dir) / "src" / "generate_repo_list"
            script_dir.mkdir(parents=True, exist_ok=True)

            config_manager = ConfigManager(script_dir=str(script_dir))
            username = config_manager.get_username()
            assert username == ""


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
