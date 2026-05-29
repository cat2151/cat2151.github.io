Last updated: 2026-05-30

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けにマークダウンコンテンツを自動生成するシステムです。
- 生成されたコンテンツは、ユーザーのGitHub Pagesサイトにリポジトリ一覧を公開し、SEOとLLMからの参照性を向上させます。
- 各リポジトリの概要文やバッジの自動取得、Jekyll/GitHub Pagesに対応した出力により、効率的な情報公開を実現します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (静的サイトジェネレーター), Markdown (コンテンツ記述言語)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), PowerShell (実行コマンド例)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: PythonスクリプトによるMarkdown生成 (Jekyllが最終的なサイトビルドを担当)
- 言語機能: Python (CLI引数解析、ファイルI/O、データ処理、YAML/JSONパーシングなど)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリによる特定タスクの自動化、例: 大容量ファイルチェック)
- 開発標準: ruff (Pythonコードフォーマッター・リンター), .editorconfig (エディタ設定の統一)

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
- **.editorconfig**: 異なるIDEやエディタ間でコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsで自動化されたタスク関連のファイルを格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するディレクトリです。
        - **README.md**: `check_large_files` 機能の説明ドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **README.md**: プロジェクトの概要、目的、使い方、設定方法などが記述されたメインのドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を含みます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: 異なるサイズで提供されるWebサイトのアイコン（ファビコン）です。
- **debug_project_overview.py**: `project_overview` 機能のデバッグ目的で使用されるスクリプトです。
- **generated-docs/**: プロジェクトによって自動生成されたドキュメントやデータが格納されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧を記述したメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **issue-notes/22.md**: 特定の課題（Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
- **manifest.json**: Webサイトをプログレッシブウェブアプリ（PWA）として動作させるためのマニフェストファイルです。アプリの表示方法やアイコンなどを定義します。
- **pytest.ini**: pytestテストフレームワークの設定ファイルです。テストの発見ルールやオプションなどを指定します。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージの依存関係を記述したファイルです。
- **requirements.txt**: プロジェクトの実行に必要な本番環境のPythonパッケージの依存関係を記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンティングとフォーマットに使用されるRuffツールの設定ファイルです。
- **src/**: プロジェクトのソースコードを格納するメインディレクトリです。
    - **generate_repo_list/**: リポジトリ一覧を生成する主要なロジックを格納するパッケージです。
        - **__init__.py**: Pythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのステータスや技術を示すバッジ画像を生成するロジックを含みます。
        - **config.yml**: `generate_repo_list` スクリプトの実行時設定（例: プロジェクト概要取得機能の設定）を定義するファイルです。
        - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するためのユーティリティです。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するための関数を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
        - **json_ld_template.json**: SEO最適化のために、Webページに構造化データ（JSON-LD形式）を追加するためのテンプレートファイルです。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示するためのロジックを含みます。
        - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成する役割を担います。
        - **project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要（3行説明）を抽出・取得するためのロジックです。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するための機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形に整形するためのロジックです。
        - **seo_template.yml**: SEO関連のメタデータや設定を定義するためのテンプレートファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するための機能を提供します。
        - **strings.yml**: UIメッセージ、見出し、説明文など、アプリケーションで使用されるすべての文字列を外部化して管理するためのファイルです。
        - **template_processor.py**: Markdown生成時に使用されるテンプレートを処理し、データで埋め込むためのユーティリティです。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher` 機能の単体テストを含むファイルです。
- **tests/**: プロジェクトのテストコードを格納するディレクトリです。
    - **conftest.py**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **test_badge_generator_integration.py**: `badge_generator` の統合テストです。
    - **test_check_large_files.py**: `check_large_files` スクリプトのテストです。
    - **test_config.py**: 設定ファイルの読み込み・管理機能のテストです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストです。
    - **test_environment.py**: 実行環境に関するテストです。
    - **test_integration.py**: 主要なコンポーネント間の連携をテストする統合テストです。
    - **test_markdown_generator.py**: Markdown生成機能のテストです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` 機能のテストです。
    - **test_readme_badge_extractor.py**: READMEバッジ抽出機能のテストです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
- **generate_repo_list.py**
    - `main()`: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、整形して最終的なMarkdownファイルを生成するプロジェクトの主要な実行エントリポイントです。
- **badge_generator.py**
    - `generate_badge(repo_info)` (推測): リポジトリ情報に基づき、言語、ステータス、アーカイブ状態などを示すバッジ（Markdown形式）を生成します。
- **config_manager.py**
    - `load_config(config_path)` (推測): 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
- **date_formatter.py**
    - `format_date(datetime_obj)` (推測): datetimeオブジェクトを受け取り、指定された形式（例: "YYYY-MM-DD"）の文字列としてフォーマットします。
- **language_info.py**
    - `get_language_details(repo_languages)` (推測): リポジトリの言語使用率情報を受け取り、主要言語やその視覚的な表現（例: 色）に関する詳細を提供します。
- **markdown_generator.py**
    - `generate_markdown_for_repo(repo_data)` (推測): 単一のリポジトリデータを受け取り、そのリポジトリに関するMarkdownスニペットを生成します。
    - `generate_full_repo_list_markdown(all_repo_data)` (推測): 複数のリポジトリデータを受け取り、それらをまとめて完全なリポジトリ一覧のMarkdownコンテンツを生成します。
- **project_overview_fetcher.py**
    - `fetch_project_overview(repo_name, github_token, config)` (推測): 指定されたリポジトリ名と設定に基づき、そのリポジトリ内の `generated-docs/project-overview.md` から3行のプロジェクト概要をHTTPリクエストで取得します。
- **readme_badge_extractor.py**
    - `extract_badges(readme_content)` (推測): READMEのMarkdownコンテンツを解析し、含まれるバッジ（例: Shields.io形式）のURLやテキスト情報を抽出します。
- **repository_processor.py**
    - `process_repository_data(raw_repo_json)` (推測): GitHub APIから取得した生のリポジトリJSONデータを受け取り、必要な情報を抽出し、整形して、後続のMarkdown生成に適した形式に変換します。
- **statistics_calculator.py**
    - `calculate_repo_statistics(repo_list)` (推測): リポジトリのリストを受け取り、総スター数、フォーク数、アクティブなリポジトリ数などの集計統計情報を計算します。
- **template_processor.py**
    - `render_template(template_string, data)` (推測): テンプレート文字列とデータを結合し、最終的なコンテンツ（例: JSON-LD、Markdownの一部）を生成します。
- **url_utils.py**
    - `build_github_api_url(username)` (推測): GitHubのユーザー名に基づいて、リポジトリ情報を取得するためのAPIエンドポイントURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-05-30 07:34:25 JST
