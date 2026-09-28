Last updated: 2026-09-29

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、リポジトリの発見性向上と検索エンジンへのインデックスを促進します。
- 各リポジトリの概要を自動取得・表示することで、情報の包括性とLLMによる参照の成功率向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) が生成されたMarkdownをレンダリングし、Webサイトとして公開します。出力はMarkdown形式で、静的サイトジェネレーターによる表示を前提としています。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Pythonを主要なスクリプト言語として使用し、GitHub APIを通じてリポジトリ情報を取得します。Pytestはテストフレームワークとして、Ruffはコード品質チェックとフォーマットツールとして開発を支援します。
- テスト: Pytestが単体テストおよび統合テストの実行に利用されており、`pytest.ini`でテスト設定が管理されています。
- ビルドツール: 本プロジェクト自体はMarkdownファイルを生成しますが、その後のWebサイトとしての「ビルド」と公開はGitHub PagesのJekyll機能によって行われます。
- 言語機能: Pythonの標準ライブラリ群、コマンドライン引数解析、YAML/JSONファイルの処理機能などが活用されています。
- 自動化・CI/CD: 本プロジェクトのREADMEでは「CI/CD不要のローカル開発重視」とされており、直接的なCI/CDパイプラインは記述されていません。生成されたMarkdownのデプロイはGitHub Pagesの仕組みに依存します。
- 開発標準: Ruff (`ruff.toml`で設定) によるコードスタイルの自動修正と品質チェック、および.editorconfigによるエディタ間のスタイル統一が行われています。

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、エンコーディングなど）を維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルの検出に関する自動化処理を格納するサブディレクトリ。
        - **README.md**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックのための設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理対象から除外するファイルやディレクトリを指定する設定ファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの概要、目的、使用方法、設定方法などを説明する主要なドキュメント。
- **_config.yml**: Jekyllサイト全体の挙動を制御する設定ファイル。GitHub Pagesの基本的な設定が含まれる。
- **assets/**: Webサイトで使用される画像、ファビコン、CSSなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズで提供されるファビコン画像ファイル群。
- **debug_project_overview.py**: `project_overview_fetcher.py`のデバッグやテストに用いられる可能性のあるスクリプト。
- **generated-docs/**: プロジェクト概要を自動取得する際に参照される可能性のある、生成されたドキュメントを格納するためのプレースホルダーディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: 本システムによって生成される、リポジトリ一覧を記述したメインのMarkdownファイル。GitHub Pagesのトップページとして表示される。
- **issue-notes/**: 課題や議論のメモを格納するディレクトリ。
    - **22.md**: 特定の課題（Issue #22）に関するメモや議論を記録したMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示設定など）を定義するファイル。
- **pytest.ini**: `pytest` テストフレームワークの設定ファイル。テスト検出ルールやテストオプションなどを定義する。
- **requirements-dev.txt**: 開発環境やテスト環境で必要なPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールしてはいけないかを指示するファイル。
- **ruff.toml**: `ruff` ツールの設定ファイル。リンティングルールやフォーマットオプションなどを定義する。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージの初期化ファイル。
    - **generate_repo_list/**: リポジトリ一覧生成機能に関連するモジュールを格納するサブパッケージ。
        - **__init__.py**: Pythonサブパッケージの初期化ファイル。
        - **badge_generator.py**: リポジトリの言語やスター数などのバッジ（Markdown形式）を生成する機能を含むモジュール。
        - **config.yml**: プロジェクト概要取得機能など、システム全体の動作を制御する技術的パラメータを定義する設定ファイル。
        - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティモジュール。
        - **generate_repo_list.py**: プロジェクトのメインエントリスクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdownファイルを生成する処理を orchestrate する。
        - **json_ld_template.json**: SEO強化のために使用されるJSON-LD形式の構造化データを生成するためのテンプレートファイル。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理、整形するモジュール。
        - **markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するモジュール。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイルからプロジェクト概要を抽出し、取得するモジュール。
        - **readme_badge_extractor.py**: READMEファイルからバッジ情報を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した個々のリポジトリデータを処理し、表示に適した形に整形するモジュール。
        - **seo_template.yml**: SEO関連のメタデータや設定を定義するテンプレートファイル。
        - **statistics_calculator.py**: リポジトリに関する統計情報（例：言語の使用割合）を計算するモジュール。
        - **strings.yml**: 表示メッセージ、UIテキスト、文言などを一元的に管理する設定ファイル。
        - **template_processor.py**: Markdown生成時に使用されるテンプレートを処理するモジュール。
        - **url_utils.py**: URLの生成や解析に関連するユーティリティ関数を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher.py`機能の単体テストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: `pytest` のフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    - **test_badge_generator_integration.py**: `badge_generator.py` の統合テストスクリプト。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストスクリプト。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストスクリプト。
    - **test_date_formatter.py**: 日付フォーマット機能のテストスクリプト。
    - **test_environment.py**: プロジェクトの実行環境に関するテストスクリプト。
    - **test_integration.py**: プロジェクト全体の主要な機能の統合テストスクリプト。
    - **test_markdown_generator.py**: Markdown生成機能のテストスクリプト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストスクリプト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストスクリプト。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテストスクリプト。

## 関数詳細説明
- **badge_generator.py**:
    - `generate_language_badge(language: str) -> str`: 指定されたプログラミング言語のバッジ（Markdown形式）を生成します。
    - `generate_star_badge(stars: int) -> str`: 指定されたスター数に対応するバッジ（Markdown形式）を生成します。
- **config_manager.py**:
    - `load_config(config_path: str) -> dict`: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
- **date_formatter.py**:
    - `format_date(date_string: str, format_str: str = "%Y-%m-%d") -> str`: 指定された日付文字列を指定されたフォーマットで整形します。
- **generate_repo_list.py**:
    - `main()`: プロジェクトの主要な実行エントリポイント。GitHub APIからリポジトリ情報を取得し、整形してMarkdownファイルを生成します。
    - `parse_arguments() -> argparse.Namespace`: コマンドライン引数を解析し、ユーザー名や出力ファイル名などを取得します。
- **language_info.py**:
    - `get_language_details(language: str) -> dict`: 指定されたプログラミング言語に関する詳細情報（色、アイコンなど）を取得します。
- **markdown_generator.py**:
    - `generate_repository_entry(repo_data: dict) -> str`: 個々のリポジトリデータに基づいて、リポジトリ一覧のエントリ（Markdown形式）を生成します。
    - `generate_full_markdown(repo_list: list) -> str`: 複数のリポジトリエントリを結合し、最終的なMarkdownコンテンツを生成します。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_url: str, config: dict) -> str`: 指定されたリポジトリURLから、プロジェクト概要ファイルを取得し、設定に基づいて概要テキストを抽出します。
- **readme_badge_extractor.py**:
    - `extract_badges_from_readme(readme_content: str) -> list`: READMEコンテンツからバッジの情報を抽出します。
- **repository_processor.py**:
    - `process_repository_data(repo_raw_data: dict, config: dict) -> dict`: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形に変換します。
- **statistics_calculator.py**:
    - `calculate_language_stats(repo_list: list) -> dict`: リポジトリリストから言語ごとの統計情報（使用割合など）を計算します。
- **template_processor.py**:
    - `render_template(template_path: str, data: dict) -> str`: 指定されたテンプレートファイルにデータを適用し、レンダリングされた文字列を返します。
- **url_utils.py**:
    - `build_github_api_url(username: str) -> str`: 指定されたGitHubユーザー名からGitHub APIのエンドポイントURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-29 07:13:12 JST
