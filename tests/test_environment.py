#!/usr/bin/env python3
"""環境判定のユニットテスト

このモジュールは環境判定機能をpytestでテストします。
"""

import os
import sys
from unittest.mock import patch

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from config_manager import ConfigManager  # noqa: E402


class TestEnvironment:
    """環境判定のテストクラス"""

    @patch.dict(os.environ, {"GITHUB_ACTIONS": "true"})
    def test_github_actions_detection(self, capsys):
        """GitHub Actions環境検出テスト"""
        config_manager = ConfigManager()

        # 環境判定
        is_github_actions = config_manager.is_github_actions_environment()
        assert is_github_actions is True

        print("🔧 GitHub Actions環境として判定されました")
        print("   → 環境変数 GITHUB_TOKEN を優先して使用します")

        captured = capsys.readouterr()
        assert "GitHub Actions環境として判定されました" in captured.out

    @patch.dict(os.environ, {}, clear=True)
    def test_local_environment_detection(self, capsys):
        """ローカル環境検出テスト"""
        config_manager = ConfigManager()

        # 環境判定
        is_github_actions = config_manager.is_github_actions_environment()
        assert is_github_actions is False

        print("💻 ローカル環境として判定されました")
        print("   → secrets/secrets.toml を優先して使用します")

        captured = capsys.readouterr()
        assert "ローカル環境として判定されました" in captured.out

    @patch.dict(os.environ, {"GITHUB_ACTIONS": "false"})
    def test_github_actions_false_value(self):
        """GITHUB_ACTIONS=falseの場合のテスト"""
        config_manager = ConfigManager()
        is_github_actions = config_manager.is_github_actions_environment()
        assert is_github_actions is False

    @patch.dict(os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_TOKEN": "test_token_123"})
    def test_token_acquisition_github_actions(self):
        """GitHub Actions環境でのトークン取得テスト"""
        config_manager = ConfigManager()
        token = config_manager.get_github_token()
        assert token == "test_token_123"

    @patch.dict(os.environ, {}, clear=True)
    @patch("config_manager.ConfigManager.load_secrets")
    def test_token_acquisition_no_token(self, mock_load_secrets):
        """トークンが設定されていない場合のテスト"""
        # secretsファイルが存在しない場合をモック
        mock_load_secrets.return_value = {}
        config_manager = ConfigManager()
        token = config_manager.get_github_token()
        assert token == ""

    def test_environment_variables_exist(self):
        """環境変数の存在確認テスト"""
        # 最低限必要な環境変数が存在することをテスト
        path_env = os.environ.get("PATH")
        assert path_env is not None
        assert len(path_env) > 0


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    print("🔍 環境判定サンプル")
    print("=" * 50)

    config_manager = ConfigManager()

    # 環境変数の確認
    github_actions_env = os.environ.get("GITHUB_ACTIONS")
    print(f"GITHUB_ACTIONS環境変数: {github_actions_env}")

    # 環境判定
    is_github_actions = config_manager.is_github_actions_environment()
    print(f"GitHub Actions環境: {is_github_actions}")

    if is_github_actions:
        print("🔧 GitHub Actions環境として判定されました")
        print("   → 環境変数 GITHUB_TOKEN を優先して使用します")
    else:
        print("💻 ローカル環境として判定されました")
        print("   → secrets/secrets.toml を優先して使用します")

    print("\n" + "=" * 50)

    # token取得テスト
    token = config_manager.get_github_token()
    if token:
        print("✅ GitHub token取得成功")
    else:
        print("❌ GitHub token取得失敗")

    # pytestでテストを実行
    print("\npytestでテスト実行...")
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())
