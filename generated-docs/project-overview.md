Last updated: 2026-02-01

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- 検索エンジンの視認性を高め、LLMによるリポジトリ参照の精度向上を目的としています。

## 技術スタック
- フロントエンド:
    - **Jekyll**: 静的サイトジェネレータ。GitHub Pagesサイトの基盤として利用され、生成されたMarkdownファイルをHTMLページに変換します。
    - **GitHub Pages**: Jekyllによって生成された静的サイトをホストするためのGitHubのサービス。
- 音楽・オーディオ:
    - このプロジェクトにおいて、音楽・オーディオ関連の特定の技術は使用されていません。
- 開発ツール:
    - **Python**: メインの開発言語。リポジトリ情報の取得、解析、Markdown生成ロジックの実装に使用されます。
    - **pytest**: Pythonアプリケーションのテストフレームワーク。コードの品質と信頼性を確保するためのテスト実行に使用されます。
    - **ruff**: Pythonコードの高速なLinterおよびフォーマッター。コードスタイルの一貫性を保ち、潜在的なエラーを検出するために使用されます。
- テスト:
    - **pytest**: 上記「開発ツール」で説明した通り、ユニットテストや統合テストの実行に用いられます。
- ビルドツール:
    - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py` が主要なビルドスクリプトとして機能し、Markdownファイルを生成します。
    - **Jekyll**: 最終的なウェブページへの変換はJekyllが行いますが、このプロジェクト自体はMarkdown生成までを担当します。
- 言語機能:
    - **Pythonの標準ライブラリ**: ファイルI/O、HTTPリクエスト、文字列処理、日付処理など、多岐にわたる処理にPythonの標準機能が活用されています。
- 自動化・CI/CD:
    - **GitHub Actions (関連)**: 直接的なCI/CD設定ファイルは提供されていませんが、このシステムがGitHub Actionsと連携してリポジトリの概要を自動取得する機能を持っているため、自動化の文脈で関連性が高い技術です。
- 開発標準:
    - **Ruff**: コードスタイルの一貫性を保つためのリンタ・フォーマッター。`.ruff.toml`でルールが定義されています。
    - **EditorConfig**: 異なるエディタやIDE間で基本的なコードフォーマット（インデントスタイル、文字コードなど）を統一するための設定です。

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
- **`.editorconfig`**: 異なる開発環境間でのコードスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、主要機能、使用方法、設定方法、ライセンスなどの概要を説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定（サイト名、テーマ、プラグインなど）を定義するファイルです。
- **`assets/`**: Jekyllサイトで使用される静的リソース（ファビコン画像など）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイルです。
- **`debug_project_overview.py`**: `project_overview`機能の動作確認やデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要（`project-overview.md`）のようなドキュメントが一時的に格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **`index.md`**: メインのPythonスクリプトによって、生成されたリポジトリ一覧のコンテンツが書き込まれるMarkdownファイルです。これがGitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録したMarkdownファイル群を格納するディレクトリです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、PWA (Progressive Web App) としての振る舞いを定義します（ホーム画面への追加、表示モードなど）。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの発見方法や実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境で必要となるPythonの依存パッケージをリストしたファイルです。
- **`requirements.txt`**: 本番環境で必要となるPythonの依存パッケージをリストしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびフォーマッターである`ruff`の設定ファイルです。コードスタイルのルールやチェック項目を定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
- **`src/generate_repo_list/`**: GitHubリポジトリ一覧生成ロジックをまとめたPythonパッケージです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`badge_generator.py`**: リポジトリの言語やライセンスなどのバッジ情報を生成するロジックを扱います。
    - **`config.yml`**: プロジェクト固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）を定義する設定ファイルです。
    - **`config_manager.py`**: `config.yml`のような設定ファイルを読み込み、プログラム内で利用可能な形式で管理するモジュールです。
    - **`date_formatter.py`**: 日付や時刻のフォーマット、相対時間表示などを処理するユーティリティモジュールです。
    - **`generate_repo_list.py`**: プロジェクトのメインエントリポイントとなるスクリプト。GitHub APIから情報を取得し、最終的なMarkdownファイルを生成します。
    - **`json_ld_template.json`**: SEOを強化するためにHTMLに埋め込む構造化データ（JSON-LD）のテンプレートです。
    - **`language_info.py`**: リポジトリの主要言語情報やその割合などを処理するロジックを含みます。
    - **`markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けの整形されたMarkdownコンテンツを生成する主要なモジュールです。
    - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で取得する機能を担当します。
    - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、プロジェクト独自のバッジ情報などを抽出するロジックです。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形する処理を行います。
    - **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやページタイトルの生成に関するテンプレート設定です。
    - **`statistics_calculator.py`**: リポジトリ数、言語ごとの統計、更新頻度など、各種統計情報を計算するモジュールです。
    - **`strings.yml`**: ユーザーインターフェースに表示されるテキストメッセージや文言を集中管理するためのファイル（国際化対応の基盤）。
    - **`template_processor.py`**: Markdown生成において、特定のテンプレート構文を処理し、動的にコンテンツを埋め込む役割を担います。
    - **`url_utils.py`**: URLの構築、検証、解析など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュール（プロジェクト概要取得機能）の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能に関するテストです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストです。
    - **`test_environment.py`**: 実行環境の設定や依存関係に関するテストです。
    - **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
プロジェクト情報には個別の関数に関する詳細な説明が提供されていません。しかし、各ファイルはその目的を果たすために、以下のような種類の関数を含んでいると推測されます。

- **`badge_generator.py`**:
    - `generate_badge(type, value)`: 指定されたタイプと値に基づいてバッジのMarkdown文字列を生成します。
    - `create_language_badge(language, percentage)`: 言語とその割合を示すバッジを生成します。
- **`config_manager.py`**:
    - `load_config(file_path)`: YAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
    - `get_setting(key_path, default_value)`: 設定ファイルから特定のキーパスに対応する値を取得します。
- **`date_formatter.py`**:
    - `format_date(iso_date, format_string)`: ISO形式の日付文字列を指定されたフォーマットに変換します。
    - `get_relative_time(iso_date)`: ISO形式の日付文字列から「N日前」のような相対的な時間表現を生成します。
- **`generate_repo_list.py` (メインスクリプト)**:
    - `main()`: コマンドライン引数をパースし、リポジトリ一覧生成の主要な処理フローを orchestrate します。
    - `generate_repo_list(username, output_file, limit)`: 指定されたユーザーのリポジトリ情報を取得し、Markdownファイルを生成する中心的な関数です。
- **`markdown_generator.py`**:
    - `generate_markdown(repositories, seo_data, strings_data)`: 処理されたリポジトリデータ、SEOデータ、文言データから最終的なリポジトリ一覧のMarkdownテキスト全体を生成します。
    - `create_repository_section(repo_data)`: 個々のリポジトリに対応するMarkdownセクションを生成します。
- **`project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_url, target_file, section_title)`: 指定されたリポジトリから対象の概要ファイルを取得し、特定のセクションから概要を抽出します。
    - `extract_overview_lines(content, section_title)`: ファイルコンテンツから指定されたセクションの3行説明を抽出します。
- **`repository_processor.py`**:
    - `process_repository(github_api_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、整形・加工してアプリケーションで扱いやすい形式に変換します。
    - `filter_repositories(repositories, filter_type)`: リポジトリのリストをアクティブ、アーカイブ、フォークなどでフィルタリングします。
- **`statistics_calculator.py`**:
    - `calculate_language_statistics(repositories)`: 全リポジトリの言語使用状況に関する統計を計算します。
    - `get_top_languages(statistics, count)`: 最も使用頻度の高い言語を上位N件取得します。
- **`template_processor.py`**:
    - `render_template(template_content, data)`: テンプレート文字列とデータを受け取り、データをテンプレートに埋め込んで最終的な文字列を生成します。
- **`url_utils.py`**:
    - `build_github_api_url(username)`: GitHub APIのエンドポイントURLを構築します。
    - `is_valid_url(url)`: 指定された文字列が有効なURLであるかを検証します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-01 07:06:15 JST
