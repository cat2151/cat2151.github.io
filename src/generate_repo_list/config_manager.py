"""設定管理モジュール

このモジュールは各種設定ファイルの読み込みを担当します。
"""

import json
import os
from typing import Any, Dict

import yaml

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # fallback for older versions


class ConfigManager:
    """設定管理クラス"""

    def __init__(self, script_dir: str = None):
        """初期化

        Args:
            script_dir: スクリプトディレクトリのパス。Noneの場合は自動検出。
        """
        if script_dir is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_dir = script_dir
        self._cache = {}

    def load_seo_template(self) -> Dict[str, Any]:
        """SEOテンプレートファイルを読み込む"""
        if "seo_template" not in self._cache:
            path = os.path.join(self.script_dir, "seo_template.yml")
            with open(path, "r", encoding="utf-8") as f:
                self._cache["seo_template"] = yaml.safe_load(f)
        return self._cache["seo_template"]

    def load_json_ld_template(self) -> Dict[str, Any]:
        """JSON-LDテンプレートファイルを読み込む"""
        if "json_ld_template" not in self._cache:
            path = os.path.join(self.script_dir, "json_ld_template.json")
            with open(path, "r", encoding="utf-8") as f:
                self._cache["json_ld_template"] = json.load(f)
        return self._cache["json_ld_template"]

    def load_config(self) -> Dict[str, Any]:
        """設定ファイルを読み込む"""
        if "config" not in self._cache:
            path = os.path.join(self.script_dir, "config.yml")
            with open(path, "r", encoding="utf-8") as f:
                self._cache["config"] = yaml.safe_load(f)
        return self._cache["config"]

    def load_strings(self) -> Dict[str, Any]:
        """文字列リソースファイルを読み込む"""
        if "strings" not in self._cache:
            path = os.path.join(self.script_dir, "strings.yml")
            with open(path, "r", encoding="utf-8") as f:
                self._cache["strings"] = yaml.safe_load(f)
        return self._cache["strings"]

    def load_secrets(self) -> Dict[str, Any]:
        """secretsファイル（TOML）を読み込む"""
        if "secrets" not in self._cache:
            # secretsディレクトリはスクリプトディレクトリの2つ上の階層
            secrets_dir = os.path.join(os.path.dirname(os.path.dirname(self.script_dir)), "secrets")
            path = os.path.join(secrets_dir, "secrets.toml")
            if os.path.exists(path):
                with open(path, "rb") as f:
                    self._cache["secrets"] = tomllib.load(f)
            else:
                # secretsファイルが見つからない場合は空の辞書を返す
                self._cache["secrets"] = {}
        return self._cache["secrets"]

    def get_github_token(self) -> str:
        """GitHub tokenを取得する

        取得優先順位:
        1. GitHub Actions環境: 環境変数 GITHUB_TOKEN
        2. ローカル環境: secrets.toml ファイル
        3. フォールバック: 環境変数 GITHUB_TOKEN
        """
        # GitHub Actions環境の判定
        is_github_actions = os.environ.get("GITHUB_ACTIONS") == "true"

        if is_github_actions:
            # GitHub Actions環境では環境変数を優先
            token = os.environ.get("GITHUB_TOKEN")
            if token:
                return token
            else:
                print("⚠️  GitHub Actions環境ですが GITHUB_TOKEN 環境変数が設定されていません")
        else:
            # ローカル環境ではsecretsファイルを優先
            secrets = self.load_secrets()
            token = secrets.get("github", {}).get("token", "")
            if token:
                return token

            # secretsファイルにない場合は環境変数をチェック
            token = os.environ.get("GITHUB_TOKEN")
            if token:
                print("💡 secretsファイルが見つからないため、環境変数 GITHUB_TOKEN を使用します")
                return token

        return ""

    def get_username(self) -> str:
        """GitHub usernameを取得する

        取得優先順位:
        1. secrets.toml ファイル
        2. 環境変数 GITHUB_USERNAME
        3. デフォルト値（空文字列）
        """
        # secretsファイルからusernameを取得
        secrets = self.load_secrets()
        username = secrets.get("github", {}).get("username", "")
        if username:
            return username

        # 環境変数をチェック
        username = os.environ.get("GITHUB_USERNAME", "")
        if username:
            return username

        return ""

    def is_github_actions_environment(self) -> bool:
        """GitHub Actions環境かどうかを判定する"""
        return os.environ.get("GITHUB_ACTIONS") == "true"
