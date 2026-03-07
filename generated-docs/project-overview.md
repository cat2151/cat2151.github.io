Last updated: 2026-03-08

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・整形します。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、検索エンジンでの視認性を高め、LLMによるリポジトリ参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの構築・ホスティング), Markdown (リポジトリ一覧コンテンツの記述形式), HTML/CSS/JavaScript (GitHub Pagesでレンダリングされるウェブ技術)
- 音楽・オーディオ: なし (このプロジェクトには関連する技術は使用されていません)
- 開発ツール: Python (メインのスクリプト言語), Git (バージョン管理), GitHub API (リポジトリ情報取得), PyYAML (YAML設定ファイルの処理)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: なし (生成されるMarkdownはGitHub PagesのJekyllにより処理されるため、明示的なビルドツールは使用されていません)
- 言語機能: Python標準ライブラリ (requests, argparse, datetimeなど、API通信やデータ処理に使用), f-strings (文字列フォーマット)
- 自動化・CI/CD: GitHub Pages (静的サイトの自動デプロイ), GitHub Actions (`.github_automation` ディレクトリから推測される、ファイルサイズチェックなどの自動タスク実行)
- 開発標準: ruff (Pythonコードのリンター・フォーマッター), .editorconfig (複数エディタ間でのコードスタイル統一設定)

## ファイル階層ツリー
```
📄 .editorconfig
📁 .github_automation/
  📁 check_large_files/
    📖 README.md
    📄 check-large-files.toml
    📁 scripts/
      📄 check_large_files.py
📄 .gitignore
📄 LICENSE
📖 README.md
📄 _config.yml
📁 assets/
  📄 favicon-16x16.png
  📄 favicon-192x192.png
  📄 favicon-32x32.png
  📄 favicon-512x512.png
📄 debug_project_overview.py
📁 generated-docs/
🌐 googled947dc864c270e07.html
📖 index.md
📁 issue-notes/
  📖 22.md
📊 manifest.json
📄 pytest.ini
📄 requirements-dev.txt
📄 requirements.txt
📄 robots.txt
📄 ruff.toml
📁 src/
  📄 __init__.py
  📁 generate_repo_list/
    📄 __init__.py
    📄 badge_generator.py
    📄 config.yml
    📄 config_manager.py
    📄 date_formatter.py
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 readme_badge_extractor.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_badge_generator_integration.py
  📄 test_check_large_files.py
  📄 test_config.py
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_readme_badge_extractor.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタ間でのコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    -   **`check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    -   **`check_large_files/scripts/check_large_files.py`**: 指定された閾値を超える大容量ファイルを検出するPythonスクリプトです。
-   **`.gitignore`**: Gitによってバージョン管理から除外されるファイルやディレクトリを指定する設定ファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法などを説明するメインのドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の挙動を設定するファイルです。
-   **`assets/`**: サイトで使用されるファビコンやその他の静的ファイルを格納するディレクトリです。
    -   **`favicon-*.png`**: サイトのファビコン画像ファイル群です。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを行うためのスクリプトです。
-   **`generated-docs/`**: 自動生成されたドキュメントや、参照される外部ドキュメントを格納するためのディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト所有権確認に使用されるファイルです。
-   **`index.md`**: 自動生成されたリポジトリ一覧のメインページとなるMarkdownファイルです。
-   **`issue-notes/22.md`**: 特定のIssue（問題報告や改善提案）に関するメモやドキュメントを格納するファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示方法や動作を定義します。
-   **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージのリストです。
-   **`requirements.txt`**: 本番環境で必要なPythonパッケージのリストです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
-   **`ruff.toml`**: Ruffリンターおよびフォーマッターの設定ファイルで、Pythonコードの品質とスタイルを維持します。
-   **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるための初期化ファイルです。
-   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための初期化ファイルです。
-   **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種情報（言語、ライセンスなど）を示すバッジを生成するロジックを実装しています。
-   **`src/generate_repo_list/config.yml`**: プロジェクトの実行時設定を定義するYAMLファイルです。特にプロジェクト概要取得機能などのパラメータを含みます。
-   **`src/generate_repo_list/config_manager.py`**: `config.yml` などの設定ファイルを読み込み、管理する機能を提供します。
-   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のフォーマットに関連するユーティリティ機能を提供します。
-   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
-   **`src/generate_repo_list/json_ld_template.json`**: SEO強化のためのJSON-LD形式の構造化データテンプレートです。
-   **`src/generate_repo_list/language_info.py`**: リポジトリの言語情報（使用割合など）を処理・表示するためのロジックを含みます。
-   **`src/generate_repo_list/markdown_generator.py`**: リポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを実装しています。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得する機能を提供します。
-   **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報（例: 状態、ビルド状況）を抽出するロジックを実装しています。
-   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理・整形するためのクラスや関数を提供します。
-   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
-   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリの統計情報（例: スター数、フォーク数）を計算・集計する機能を提供します。
-   **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージや文言を管理するYAMLファイルです。
-   **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用されるテンプレートの処理ロジックを実装しています。
-   **`src/generate_repo_list/url_utils.py`**: URLの操作や検証など、URLに関連するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
-   **`tests/`**: プロジェクトの各種テストスクリプトを格納するディレクトリです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストを行います。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを行います。
    -   **`test_config.py`**: 設定ファイル管理機能のテストを行います。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテストを行います。
    -   **`test_environment.py`**: 実行環境設定や依存関係のテストを行います。
    -   **`test_integration.py`**: 主要機能の結合テストを行います。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテストを行います。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行います。
    -   **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを行います。
    -   **`test_repository_processor.py`**: リポジトリ処理機能のテストを行います。

## 関数詳細説明
プロジェクト情報には、`googled947dc864c270e07.html` に「関数: なし」と記載されているのみで、その他のファイルやPythonスクリプト内の個別の関数に関する詳細な説明は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-08 07:06:49 JST
