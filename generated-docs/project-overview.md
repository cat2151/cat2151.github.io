Last updated: 2026-08-02

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ一覧のMarkdownファイルを自動生成するシステムです。
- 検索エンジンからのクロールやLLMによる参照性を向上させ、プロジェクトの可視性を高めることを目的としています。
- GitHub APIを活用し、リポジトリの概要、バッジ、分類などを自動取得・表示します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式), HTML (生成されるページの表示形式)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), Git (バージョン管理)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: Pythonスクリプト (実質的なファイル生成処理), YAML (設定ファイル), TOML (設定ファイル)
- 言語機能: Python (スクリプト開発), YAML (データ構造定義), JSON (データ構造、JSON-LDテンプレート)
- 自動化・CI/CD: GitHub Pages (成果物のホスティングと公開), Pythonスクリプト (実行の自動化)
- 開発標準: ruff (Pythonコードのリンター・フォーマッター), .editorconfig (エディタ間のコーディングスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `.github_automation/check_large_files` ディレクトリに格納されている、大きなファイルチェック機能に関する説明文書です。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大きなファイルチェック機能の設定ファイルです。チェック対象のファイルサイズ閾値などを定義します。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きなファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方、設定、ライセンスなど、プロジェクト全体の概要を説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を行います。
- **`assets/`**: GitHub Pagesサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **`assets/favicon-*.png`**: サイトのブラウザタブやブックマークアイコンとして使用されるファビコン画像ファイル群です。
- **`debug_project_overview.py`**: プロジェクト概要自動取得機能の動作確認やデバッグを目的としたPythonスクリプトです。
- **`generated-docs/`**: このディレクトリは、各リポジトリから自動取得される `project-overview.md` ファイルが期待される場所を示す論理的なパスです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: このプロジェクトのスクリプトによって生成される、リポジトリ一覧のMarkdownファイルです。Jekyllによって処理され、GitHub Pagesサイトのメインページとして公開されます。
- **`issue-notes/22.md`**: プロジェクト開発中に発生した特定の問題（Issue 22）に関するメモや詳細情報を記録したファイルです。
- **`manifest.json`**: Webアプリケーションマニフェストファイルであり、サイトをPWA（Progressive Web App）としてインストール可能にするための設定情報を含みます。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の挙動を制御するための設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonライブラリをリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境用のPythonライブラリをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンターおよびフォーマッターである`ruff`の設定ファイルです。コーディング規約や自動修正ルールを定義します。
- **`src/generate_repo_list/__init__.py`**: `src/generate_repo_list` ディレクトリがPythonパッケージであることを示す空のファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスなどの情報を視覚的なバッジとして生成するロジックを含むPythonモジュールです。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成プロセスの詳細な設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパス、タイムアウトなど）を定義するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` や `strings.yml` など、プロジェクトで使用される各種設定ファイルを読み込み、管理するためのPythonモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: リポジトリの最終更新日などの日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供するPythonモジュールです。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメイン実行スクリプトです。GitHub APIからのリポジトリ情報取得、処理、Markdown生成、ファイル出力までの一連の流れを制御します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、JSON-LD形式の構造化データを出力する際のテンプレートとなるJSONファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報などを取得し、表示用に処理・整形するロジックを含むPythonモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを含むPythonモジュールです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要3行を自動的に抽出し取得するロジックを含むPythonモジュールです。
- **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、特定の形式で埋め込まれたバッジ情報を抽出するためのロジックを含むPythonモジュールです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリの生データを整形し、必要な情報（名前、説明、URL、スター数など）を抽出・加工するロジックを含むPythonモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: サイトのSEO関連のメタデータや、Jekyllサイトに適用されるSEO設定のテンプレートを定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計するためのロジックを含むPythonモジュールです。
- **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートを処理し、動的なデータを埋め込んで最終的なコンテンツを作成するためのロジックを含むPythonモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するPythonモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/conftest.py`**: `pytest`のフィクスチャやヘルパー関数など、複数のテストファイルで共有される設定やリソースを定義するファイルです。
- **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを行うPythonスクリプトです。
- **`tests/test_check_large_files.py`**: 大きなファイルチェック機能（`.github_automation/check_large_files/scripts/check_large_files.py`）のテストケースを記述したPythonスクリプトです。
- **`tests/test_config.py`**: `config_manager`モジュールなど、設定ファイルの読み込みや管理機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/test_date_formatter.py`**: `date_formatter`モジュールの日付整形機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/test_environment.py`**: プロジェクトの実行環境が正しく設定されているかを確認するためのテストケースを記述したPythonスクリプトです。
- **`tests/test_integration.py`**: プロジェクトの主要コンポーネントが連携して正しく動作するかを確認する統合テストケースを記述したPythonスクリプトです。
- **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールのMarkdown生成機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの機能に関するテストケースを記述したPythonスクリプトです（`test_project_overview.py`と同様、またはより広範囲なテスト）。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのREADMEからのバッジ抽出機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/test_repository_processor.py`**: `repository_processor`モジュールのリポジトリ情報処理機能に関するテストケースを記述したPythonスクリプトです。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、それぞれが特定の役割を担う関数群を提供しています。以下に主要なモジュールとそこに属する可能性のある関数の役割を説明します。具体的な引数や戻り値の型はコードベースを参照する必要がありますが、役割は以下の通りです。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`: スクリプトのエントリポイント。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、各リポジトリを処理し、最終的なMarkdownコンテンツを生成して指定されたファイルに出力する一連の流れを制御します。
    -   `parse_arguments()`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、処理リミットなどのオプションを取得します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   `process_repository(repo_data, config)`: GitHub APIから取得した単一のリポジトリデータを受け取り、プロジェクト概要の取得、バッジ情報の抽出、言語情報、統計情報などの追加処理を行い、整形されたリポジトリ情報を返します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown(repo_list, config, strings)`: 処理済みリポジトリのリスト、設定、および表示文言を受け取り、それらを基にリポジトリ一覧の最終的なMarkdownコンテンツ文字列を生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLと設定に基づき、そのリポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）からプロジェクトの概要3行を抽出して取得します。
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書またはオブジェクトとして設定データを提供します。
    -   `load_strings(strings_path)`: 指定されたパスからYAML形式の文言ファイルを読み込み、表示メッセージのデータを提供します。
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_language_badge(language)`: 指定された言語名に基づいて、言語を示すMarkdown形式のバッジ文字列を生成します。
    -   `generate_status_badge(status)`: リポジトリのアクティブ、アーカイブなどのステータスを示すMarkdown形式のバッジ文字列を生成します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式（例: "YYYY年MM月DD日"）に整形して返します。
-   **`src/generate_repo_list/url_utils.py`**
    -   `create_github_repo_url(username, repo_name)`: GitHubのユーザー名とリポジトリ名から、該当リポジトリのURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-02 07:20:34 JST
