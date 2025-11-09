#!/usr/bin/env python3
"""プロジェクト概要取得機能の詳細デバッグ用スクリプト"""

import os
import sys

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)


def debug_project_overview_fetcher():
    """ProjectOverviewFetcherのデバッグ"""
    from config_manager import ConfigManager
    from github import Github
    from project_overview_fetcher import ProjectOverviewFetcher

    print("プロジェクト概要取得機能 詳細デバッグ")
    print("=" * 60)

    # 設定とGitHub APIの初期化
    config_manager = ConfigManager()
    config = config_manager.load_config()

    try:
        token = config_manager.get_github_token()
        github_api = Github(token)
        print("✓ GitHub API初期化成功")

        # ProjectOverviewFetcherの初期化
        fetcher = ProjectOverviewFetcher(github_api, config)
        print("✓ ProjectOverviewFetcher初期化成功")
        print(f"  - enabled: {fetcher.enabled}")
        print(f"  - target_file: {fetcher.target_file}")
        print(f"  - section_title: {fetcher.section_title}")
        print(f"  - enable_cache: {fetcher.enable_cache}")

        # github-actionsリポジトリで詳細テスト
        repo_name = "github-actions"
        username = "cat2151"

        print(f"\n🔍 詳細テスト: {username}/{repo_name}")
        print("-" * 50)

        # ステップ1: ファイル存在確認
        print("ステップ1: ファイル存在確認")
        try:
            exists = fetcher._check_file_exists(repo_name, username)
            print(f"  結果: {exists}")
            if not exists:
                print("  ❌ ファイルが存在しません")
                return
        except Exception as e:
            print(f"  ❌ エラー: {str(e)}")
            return

        # ステップ2: ファイル内容取得
        print("\nステップ2: ファイル内容取得")
        try:
            content = fetcher._fetch_markdown_content(repo_name, username)
            if content:
                print(f"  成功: {len(content)} 文字")
                print(f"  最初の200文字: {content[:200]}...")
            else:
                print("  ❌ ファイル内容の取得に失敗")
                return
        except Exception as e:
            print(f"  ❌ エラー: {str(e)}")
            return

        # ステップ3: セクション抽出
        print("\nステップ3: プロジェクト概要セクション抽出")
        try:
            overview_lines = fetcher._parse_overview_section(content)
            print(f"  抽出結果: {len(overview_lines)} 行")
            for i, line in enumerate(overview_lines, 1):
                print(f"    {i}. {line}")
        except Exception as e:
            print(f"  ❌ エラー: {str(e)}")

        # ステップ4: 統合テスト
        print("\nステップ4: 統合テスト（fetch_overview）")
        try:
            overview = fetcher.fetch_overview(repo_name, username)
            print(f"  最終結果: {len(overview)} 行")
            for i, line in enumerate(overview, 1):
                print(f"    {i}. {line}")
        except Exception as e:
            print(f"  ❌ エラー: {str(e)}")

        # ステップ5: セクションテスト（手動パース）
        print("\nステップ5: 手動セクション検索")
        import re

        section_patterns = [
            rf"##\s*{re.escape(fetcher.section_title)}\s*\n(.*?)(?=\n##|\Z)",
            r"##\s*プロジェクト概要\s*\n(.*?)(?=\n##|\Z)",
            r"##\s*Project\s+Overview\s*\n(.*?)(?=\n##|\Z)",
        ]

        for i, pattern in enumerate(section_patterns, 1):
            print(f"  パターン{i}: {pattern}")
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                section_content = match.group(1).strip()
                print(f"    ✓ マッチ: {len(section_content)} 文字")
                print(f"    内容: {section_content[:200]}...")

                # 箇条書き検索
                bullets = []
                for line in section_content.split("\n"):
                    line = line.strip()
                    if line.startswith("• "):
                        bullets.append(line)
                        if len(bullets) >= 3:
                            break

                print(f"    箇条書き: {len(bullets)} 行")
                for j, bullet in enumerate(bullets, 1):
                    print(f"      {j}. {bullet}")
            else:
                print("    ❌ マッチしません")

    except Exception as e:
        print(f"❌ 初期化エラー: {str(e)}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    debug_project_overview_fetcher()
