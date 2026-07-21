Last updated: 2026-07-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得・整理するシステムです。
- 取得した情報から、JekyllベースのGitHub Pages向けにSEO最適化されたリポジトリ一覧を自動生成します。
- これにより、検索エンジンによるクロールを促進し、LLMを含む外部参照からのリポジトリ発見性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレーターとして最終的なウェブページを構築)、Markdown (GitHub Pagesのコンテンツ形式、SEO最適化された出力を生成)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語としてデータ取得、処理、ファイル生成を実行)、GitHub API (リポジトリ情報の取得元)、YAML (設定ファイル `config.yml`, `strings.yml`, `seo_template.yml` の定義に使用)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Python (スクリプト自体がMarkdownファイルの生成・「ビルド」を担う)、pip/requirements.txt (Pythonパッケージの依存関係管理)
- 言語機能: Python (汎用プログラミング言語としての各種機能)
- 自動化・CI/CD: (このプロジェクト自体が「自動化」ツールとしての役割を持つ。ただし、CI/CDパイプラインとしての自動化ではなく、ローカル実行を重視している)
- 開発標準: ruff (PythonコードのLinterおよびフォーマッター)、.editorconfig (異なるエディタ間でのコーディングスタイル統一設定)

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
  📄 conftest.py
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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリ。
    - **`check_large_files/README.md`**: 大容量ファイルチェック自動化スクリプトの説明。
    - **`check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイル。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの目的、機能、使用方法など、全体的な説明を記述したメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイル。
- **`assets/`**: ウェブサイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリ。
    - `favicon-*.png`: 各種サイズのファビコン画像。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用スクリプト。
- **`generated-docs/`**: `project-overview.md` など、他のリポジトリから取得・生成されるドキュメントを格納するプレースホルダー。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイル。
- **`index.md`**: メインスクリプトによって自動生成される、リポジトリ一覧を含むGitHub Pagesのトップページ。
- **`issue-notes/22.md`**: 特定のイシュー（課題）に関するメモや詳細情報。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。
- **`pytest.ini`**: `pytest` テストフレームワークの設定ファイル。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージの依存関係リスト。
- **`requirements.txt`**: 本番環境で必要なPythonパッケージの依存関係リスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールするか・しないかを指示するファイル。
- **`ruff.toml`**: PythonコードのLinter/Formatterである `ruff` の設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能の中核をなすモジュール群。
        - **`badge_generator.py`**: リポジトリの各種バッジ（言語、スター数など）を生成する機能を提供。
        - **`config.yml`**: プロジェクト概要取得機能など、スクリプトの技術的パラメータを設定するファイル。
        - **`config_manager.py`**: 設定ファイル (`config.yml`, `secrets.toml` など) の読み込みと管理を行うモジュール。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形する機能。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプト。
        - **`json_ld_template.json`**: JSON-LD形式のSEOメタデータテンプレート。
        - **`language_info.py`**: リポジトリの使用言語情報を処理する機能。
        - **`markdown_generator.py`**: リポジトリ一覧のMarkdownコンテンツを構造化して生成するモジュール。
        - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出する機能。
        - **`readme_badge_extractor.py`**: READMEファイルから既存のバッジ情報を抽出する機能。
        - **`repository_processor.py`**: 取得したGitHubリポジトリの生データを処理し、必要な情報に変換する中心的なロジック。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定。
        - **`statistics_calculator.py`**: リポジトリの統計情報（スター数、フォーク数など）を計算する機能。
        - **`strings.yml`**: 表示されるメッセージや文言を管理する国際化/ローカライズ対応ファイル。
        - **`template_processor.py`**: MarkdownやJSON-LDのテンプレートを処理し、動的なデータを埋め込む機能。
        - **`url_utils.py`**: URL関連のユーティリティ関数（生成、解析など）。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールのテストスクリプト。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **`conftest.py`**: pytestのフィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`test_config.py`**: 設定管理機能のテスト。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`test_environment.py`**: 開発環境のセットアップに関するテスト。
    - **`test_integration.py`**: 主要な機能間の統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテスト。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数名、引数、戻り値、またはその機能に関する詳細な記述が含まれていませんでした。そのため、個々の関数の詳細な役割や仕様を説明することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-22 07:20:44 JST
