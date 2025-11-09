"""テンプレート処理モジュール

このモジュールはフロントマターとJSON-LD処理を担当します。
"""

import json
from typing import Any, Dict

import yaml


class TemplateProcessor:
    """テンプレート処理クラス"""

    def generate_frontmatter(
        self,
        username: str,
        og_description: str,
        seo_config: Dict,
        json_ld_template: Dict,
        total: int,
    ) -> str:
        """フロントマターを生成する

        Args:
            username: GitHubユーザー名
            og_description: OG説明文
            seo_config: SEO設定
            json_ld_template: JSON-LDテンプレート
            total: 総リポジトリ数

        Returns:
            フロントマター文字列
        """
        # JSON-LDテンプレートの値を置換
        json_ld_formatted = self._format_template_recursively(
            json_ld_template, username=username, total=total, og_description=og_description
        )

        # JSON-LDを生成
        json_ld_str = json.dumps(json_ld_formatted, ensure_ascii=False, indent=2)

        # フロントマターを生成
        frontmatter_lines = ["---"]
        for key, value in seo_config.items():
            if isinstance(value, str):
                formatted_value = value.format(username=username, og_description=og_description)
                # YAML安全性のためクォートを適切に処理
                if '"' in formatted_value or "'" in formatted_value or "\n" in formatted_value:
                    # 複雑な文字列はYAMLリテラルで表現
                    frontmatter_lines.append(f"{key}: |")
                    for line in formatted_value.split("\n"):
                        frontmatter_lines.append(f"  {line}")
                else:
                    frontmatter_lines.append(f'{key}: "{formatted_value}"')
            elif isinstance(value, list):
                # リストはYAMLの流れスタイルで出力
                yaml_output = yaml.dump(value, default_flow_style=True, allow_unicode=True).strip()
                frontmatter_lines.append(f"{key}: {yaml_output}")
            else:
                # その他の型（bool、int、floatなど）は直接文字列化
                frontmatter_lines.append(f"{key}: {value}")

        # JSON-LDを追加
        frontmatter_lines.append("json_ld: |")

        # JSON-LDの各行にインデントを追加
        for line in json_ld_str.split("\n"):
            frontmatter_lines.append(f"  {line}")

        # フロントマターを閉じる
        frontmatter_lines.append("---")

        return "\n".join(frontmatter_lines)

    def _format_template_recursively(self, obj: Any, **kwargs) -> Any:
        """テンプレートの値を再帰的に置換する

        Args:
            obj: 置換対象のオブジェクト
            **kwargs: 置換パラメータ

        Returns:
            置換されたオブジェクト
        """
        if isinstance(obj, str):
            return obj.format(**kwargs)
        elif isinstance(obj, dict):
            return {key: self._format_template_recursively(value, **kwargs) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._format_template_recursively(item, **kwargs) for item in obj]
        else:
            return obj
