Last updated: 2026-06-22

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジン最適化（SEO）とLLMによる参照性を高め、リポジトリの可視性を向上させます。
- 各リポジトリの概要、バッジ、分類などを自動表示し、GitHub Pagesのサイト管理を効率化します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll) - 生成されたMarkdownファイルがデプロイされる静的サイトの基盤。Markdown - 生成されるコンテンツのフォーマット。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python - リポジトリ情報の取得、処理、Markdown生成を行う主要なスクリプト言語。GitHub API - GitHubのリポジトリメタデータを取得するために利用。
- テスト: Pytest - プロジェクトの機能が正しく動作することを保証するためのテストフレームワーク。
- ビルドツール: Pythonスクリプト - GitHub APIから取得した情報に基づき、Markdownファイルを生成するプロセスを担う。
- 言語機能: Python - プロジェクト全体のロジックがPythonで実装されている。
- 自動化・CI/CD: GitHub Actions - このシステムによって生成されたMarkdownファイルをGitHub Pagesにデプロイするなどの、関連する自動化ワークフローで利用されることが想定される。
- 開発標準: Ruff - Pythonコードの品質を維持し、一貫したスタイルを適用するための高速なLinterおよびFormatter。EditorConfig - 異なるエディタやIDE間でコーディングスタイルの一貫性を保つための設定ファイル。

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
- **`.editorconfig`**: 異なるIDEやエディタ間でコーディングスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きいファイルをチェックするためのスクリプトです。このプロジェクトでは、GitHub Pagesのリポジトリ管理の一環として利用されます。
- **`.gitignore`**: Gitでバージョン管理から除外するファイルやディレクトリのパターンを定義します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: このプロジェクト自体の目的、機能、使用方法などが記載された主要なドキュメントです。
- **`_config.yml`**: GitHub Pages (Jekyll) のサイト全体の動作やレイアウトに関する設定を定義するファイルです。
- **`assets/`**: faviconなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリからプロジェクト概要を自動取得する際に参照される可能性のある、ドキュメントを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されたファイルです。
- **`index.md`**: このプロジェクトによって生成されるGitHub Pagesのメインページで、ユーザーの全リポジトリの一覧が表示されます。
- **`issue-notes/`**: 開発時に発生した特定の課題やメモを記録するためのディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリの名前、アイコン、表示設定などを定義するマニフェストファイルです。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルで、テストの実行方法やオプションなどを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonライブラリの一覧を定義します。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonライブラリの一覧を定義します。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルガイド（Linter/Formatter）である`Ruff`の設定ファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックが格納されているディレクトリです。
    - **`src/generate_repo_list/generate_repo_list.py`**: メインスクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式で出力します。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やスター数などの情報から、Webページに表示するバッジのURLやマークアップを生成するロジックを含みます。
    - **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得設定、タイムアウト時間など、システムの動作パラメータを定義します。
    - **`src/generate_repo_list/config_manager.py`**: YAMLファイルから設定を読み込み、管理するためのモジュールです。
    - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を整形するためのユーティリティ関数を提供します。
    - **`src/generate_repo_list/json_ld_template.json`**: SEO目的で構造化データ（JSON-LD）を生成するためのテンプレートファイルです。
    - **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語に関する情報（例: 色など）を管理するモジュールです。
    - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報と設定に基づき、GitHub Pagesに適したMarkdown形式のコンテンツを生成します。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの3行概要を抽出する機能を提供します。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出する機能を提供します。
    - **`src/generate_repo_list/repository_processor.py`**: 個々のGitHubリポジトリの情報を解析し、表示に必要なデータを抽出・整理します。
    - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレートを定義するファイルです。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュールです。
    - **`src/generate_repo_list/strings.yml`**: UIに表示される各種文言やメッセージ（例: リポジトリのステータス名など）を管理します。
    - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用するテンプレートを処理するためのモジュールです。
    - **`src/generate_repo_list/url_utils.py`**: URLの生成や整形など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
- **`tests/`**: プロジェクト全体の各種テストコードを格納するディレクトリです。

## 関数詳細説明
具体的な関数名はプロジェクト情報から検出されませんでしたが、各モジュールの役割から推測される主要な関数とその機能は以下の通りです。

- **`src/generate_repo_list/generate_repo_list.py` 内の関数**:
    - **`main()`**: プログラムのエントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報の取得、取得したデータの処理、最終的なMarkdownファイルの出力など、システム全体の実行フローをオーケストレートします。
    - **`generate_repo_list(username, output_file, limit)`**: 指定されたユーザー名のリポジトリ情報を取得し、Markdown形式で整形して指定されたファイルに出力する主要なロジックを含みます。
- **`src/generate_repo_list/project_overview_fetcher.py` 内の関数**:
    - **`fetch_project_overview(repo_url, config)`**: 指定されたGitHubリポジトリから、設定ファイルに定義されたパスとセクションタイトルに基づき、プロジェクトの3行概要テキストを抽出します。GitHub APIを介してファイル内容を取得し、パースする役割を担います。
- **`src/generate_repo_list/markdown_generator.py` 内の関数**:
    - **`generate_markdown(repo_data, config)`**: 処理済みのリポジトリデータを受け取り、それをGitHub Pagesで表示可能なMarkdown形式の文字列に変換します。テンプレート処理や日付整形、URL生成などの他のモジュールと連携します。
- **`src/generate_repo_list/badge_generator.py` 内の関数**:
    - **`generate_badge_markup(language, stars)`**: リポジトリの主要言語やスター数などの情報から、Webページに表示するためのバッジ（例: Shields.ioのSVGバッジ）のHTMLまたはMarkdownマークアップを生成します。
- **`src/generate_repo_list/repository_processor.py` 内の関数**:
    - **`process_repository(repo_json, config)`**: GitHub APIから取得した生のリポジトリJSONデータを受け取り、表示に必要な情報（説明、URL、言語、スター数、最終更新日など）を抽出し、整形します。他のモジュール（例: `project_overview_fetcher`）を呼び出して追加情報を取得することもあります。
- **`src/generate_repo_list/config_manager.py` 内の関数**:
    - **`load_config(config_path)`**: YAML形式の設定ファイルを読み込み、プログラム内で利用できるPythonオブジェクトとして提供します。

## 関数呼び出し階層ツリー
関数呼び出し階層は提供された情報からは分析できませんでしたが、プロジェクトの目的とファイル構造から推測される主要な実行フローは以下のようになります。

```
generate_repo_list.py (main実行関数)
├── config_manager.py (設定ファイルの読み込み)
├── repository_processor.py (各リポジトリ情報の処理)
│   ├── project_overview_fetcher.py (各リポジトリの概要取得)
│   │   └── url_utils.py (URL操作)
│   └── readme_badge_extractor.py (READMEからのバッジ情報抽出)
├── statistics_calculator.py (リポジトリ統計情報の計算)
├── badge_generator.py (表示用バッジの生成)
├── language_info.py (言語情報の整形)
└── markdown_generator.py (最終Markdownコンテンツの生成)
    ├── template_processor.py (Markdownテンプレートの適用)
    ├── date_formatter.py (日付の整形)
    └── seo_template.yml (SEOメタデータの適用)

---
Generated at: 2026-06-22 07:29:25 JST
