Last updated: 2026-04-01

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、自身のGitHubリポジトリ情報を自動で取得します。
- 取得した情報から、GitHub Pages向けのSEOに強いリポジトリ一覧を生成します。
- 検索エンジンやLLMによる参照性を高め、情報アクセスを容易にすることを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として利用)、Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用されていません。
- 開発ツール: pytest (テストフレームワーク)、ruff (コードスタイルリンター/フォーマッター)、EditorConfig (IDE間のコーディングスタイル統一)
- テスト: pytest (Pythonコードの単体テストおよび結合テスト)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得、Markdownの生成、設定ファイルのパースなどの処理を自作スクリプトで実行)
- 言語機能: Python (スクリプト開発の主要言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得)、Pythonスクリプトによる自動ファイル生成 (継続的なファイル更新を可能にする)
- 開発標準: ruff (Pythonコードの品質と一貫性の維持)、EditorConfig (プロジェクト全体のコーディング規約統一)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub ActionsなどのGitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するサブディレクトリ。
        - **README.md**: `check_large_files`機能に関する説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックのための設定を定義するTOML形式のファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報が記述されたファイル（MITライセンス）。
- **README.md**: プロジェクトの概要、目的、設定方法、使い方などを説明するメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の基本的な設定を定義するファイル。
- **assets/**: GitHub Pagesサイトで使用される静的リソース（ファビコンなどの画像）を格納するディレクトリ。
    - **favicon-16x16.png**: 16x16ピクセルのファビコン画像。
    - **favicon-192x192.png**: 192x192ピクセルのファビコン画像（高解像度ディスプレイ用など）。
    - **favicon-32x32.png**: 32x32ピクセルのファビコン画像。
    - **favicon-512x512.png**: 512x512ピクセルのファビコン画像（アプリケーションアイコン用など）。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグや単体テストを行うためのスクリプト。
- **generated-docs/**: リポジトリの概要など、外部から取得したドキュメントや生成されたドキュメントのキャッシュを格納する（あるいは元データが配置される）ディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイル。
- **index.md**: 生成されたリポジトリ一覧が記述される、GitHub PagesサイトのトップページとなるMarkdownファイル。
- **issue-notes/**: プロジェクトの課題やメモを記録するためのディレクトリ。
    - **22.md**: 特定の課題（Issue #22）に関連する詳細なメモや情報。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、アプリケーションの表示方法や動作を定義します。
- **pytest.ini**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイル。
- **requirements-dev.txt**: 開発環境で必要となるPythonライブラリの依存関係をリストアップしたファイル。
- **requirements.txt**: 本番環境（または最小実行環境）で必要となるPythonライブラリの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、または避けるべきかを指示するファイル。
- **ruff.toml**: Pythonのコードスタイルをチェック・整形するruffツールの設定ファイル。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージとして`src`ディレクトリを識別させるためのファイル。
    - **generate_repo_list/**: リポジトリ一覧生成システムの主要モジュール群を格納するパッケージ。
        - **__init__.py**: Pythonパッケージとして`generate_repo_list`ディレクトリを識別させるためのファイル。
        - **badge_generator.py**: リポジトリの言語やステータスなどに基づいてバッジ（アイコン）を生成する機能を提供します。
        - **config.yml**: `generate_repo_list`モジュール固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するYAMLファイル。
        - **config_manager.py**: 複数の設定ファイル（例: `config.yml`, `secrets.toml`）を読み込み、一元的に管理する機能を提供します。
        - **date_formatter.py**: 日付や時刻の情報を整形し、読みやすい形式で出力するための機能を提供します。
        - **generate_repo_list.py**: GitHub APIを介してリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインのスクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレート。
        - **language_info.py**: リポジトリの使用言語に関する情報を取得・処理する機能を提供します。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、Jekyll互換のMarkdownコンテンツを生成する機能を提供します。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を解析・抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、システム内部で扱いやすい形式に変換する機能を提供します。
        - **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: プロジェクト内で使用される表示メッセージや文言を管理するためのYAMLファイル。
        - **template_processor.py**: Markdown生成に使用するテンプレートの読み込みとデータ埋め込みを処理する機能を提供します。
        - **url_utils.py**: GitHub関連のURL生成や解析など、URL処理に関するユーティリティ機能を提供します。
- **test_project_overview.py**: `project_overview_fetcher`モジュールのテストスクリプト。
- **tests/**: プロジェクトの各種テストスクリプトを格納するディレクトリ。
    - **conftest.py**: pytestのテスト実行時に使用される共通のフィクスチャやフックを定義するファイル。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの統合テスト。
    - **test_check_large_files.py**: `check_large_files.py`スクリプトのテスト。
    - **test_config.py**: 設定ファイル読み込み・管理機能のテスト。
    - **test_date_formatter.py**: 日付整形機能のテスト。
    - **test_environment.py**: 実行環境に関するテスト。
    - **test_integration.py**: システム全体の主要機能の統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEファイルからのバッジ情報抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供された情報には具体的な関数の詳細（引数、戻り値）が含まれていませんが、各Pythonファイルが担当する主要な処理に基づいて、想定される関数の役割を説明します。

- **badge_generator.py**: リポジトリの言語やステータス（例: "Archived"）に応じたSVGバッジのURLやマークダウン形式のバッジを生成する関数群を含みます。
- **config_manager.py**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、設定値をキーで取得する関数（例: `load_config(path: str) -> dict`, `get_setting(key: str, default=None) -> Any`）を含みます。
- **date_formatter.py**: GitHub APIから取得した日付文字列を、指定されたフォーマット（例: "YYYY年MM月DD日"）に変換する関数（例: `format_date(date_str: str, fmt: str) -> str`）を含みます。
- **generate_repo_list.py**: プログラムのエントリポイントとなる関数（例: `main()`) を含み、コマンドライン引数の解析、GitHub APIからのデータ取得、リポジトリ処理、Markdown生成、ファイル出力といった一連の処理をオーケストレートします。
- **language_info.py**: リポジトリのプログラミング言語ごとの使用率や、主要言語情報を抽出・整形する関数群（例: `get_top_languages(repo_data: dict) -> list`）を含みます。
- **markdown_generator.py**: 処理済みのリポジトリデータを受け取り、リポジトリ一覧の各項目や全体構成をJekyll互換のMarkdown形式で生成する関数（例: `generate_repo_markdown(repo_data: dict) -> str`）を含みます。
- **project_overview_fetcher.py**: 各リポジトリの指定されたパス（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を非同期または同期的に取得・パースする関数（例: `fetch_project_overview(repo_url: str, file_path: str) -> list[str]`）を含みます。
- **readme_badge_extractor.py**: リポジトリのREADMEファイルの内容を解析し、既存のバッジのURLやマークダウンを抽出する関数（例: `extract_badges_from_readme(readme_content: str) -> list[str]`）を含みます。
- **repository_processor.py**: GitHub APIから取得した生のリポジトリJSONデータを受け取り、必要な情報（名前、説明、URL、スター数など）を抽出し、内部で扱いやすい構造（辞書など）に変換する関数（例: `process_repo_data(raw_data: dict) -> dict`）を含みます。
- **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの数値統計情報を計算・集計する関数群（例: `calculate_repo_stats(repo_list: list[dict]) -> dict`）を含みます。
- **template_processor.py**: Markdown生成時に使用するテンプレートファイル（例: JekyllのLiquid構文やカスタムテンプレート）を読み込み、データで埋め込んで最終的な文字列を生成する関数（例: `render_template(template_path: str, context: dict) -> str`）を含みます。
- **url_utils.py**: GitHubリポジトリのURL、APIエンドポイントのURLなどを構築・解析するユーティリティ関数（例: `build_github_api_url(username: str) -> str`）を含みます。
- **.github_automation/check_large_files/scripts/check_large_files.py**: 指定された閾値を超えるファイルサイズを持つファイルを検出し、レポートする関数（例: `find_large_files(directory: str, max_size_mb: int) -> list[str]`）を含みます。

## 関数呼び出し階層ツリー
```
提供されたプロジェクト情報には、具体的な関数の呼び出し階層を分析するための詳細な情報（例: 各関数の実装コード）が含まれていませんでした。そのため、関数呼び出し階層ツリーを生成することはできません。

---
Generated at: 2026-04-01 07:13:48 JST
