Last updated: 2026-02-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（`<username>.github.io`）用に、リポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成することで検索エンジンへの露出を向上させます。
- 各リポジトリの概要説明やバッジも自動で表示し、LLMからの参照性向上と開発効率の改善を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤技術)、Markdown (リポジトリ一覧の出力形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要な開発言語)、requests (HTTP通信ライブラリ、GitHub APIアクセス用)、PyYAML (YAML設定ファイル処理)、toml (TOML設定ファイル処理)、Git (バージョン管理システム)、GitHub API (リポジトリ情報取得)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: Pythonスクリプト (Markdownファイルを生成する実質的なビルドツール)
- 言語機能: Python 3.x (f-stringsなどの標準機能、標準ライブラリ)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリ内の大型ファイルチェックなど、自動化スクリプトの実行環境として想定)
- 開発標準: ruff (Pythonコードのリンターおよびフォーマッター)、.editorconfig (エディタ設定の統一)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
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
-   **`.editorconfig`**: 複数人で開発する際のエディタ設定（インデント、文字コードなど）を統一するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsなど、自動化タスクに関連するスクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/`**: 大容量ファイルがリポジトリに追加されるのを防ぐためのチェック機能関連。
        -   **`README.md`**: `check_large_files` 機能に関する説明。
        -   **`check-large-files.toml`**: `check_large_files` スクリプトの設定ファイル。
        -   **`scripts/check_large_files.py`**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの目的、機能、使用方法などを記述したメインのドキュメント。
-   **`_config.yml`**: Jekyllサイトの設定ファイル。サイトのタイトル、テーマ、プラグインなどを定義。
-   **`assets/`**: ウェブサイトで使用する画像やアイコンなどの静的アセットを格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのファビコン画像ファイル群。
-   **`debug_project_overview.py`**: `project_overview_fetcher.py` 機能のデバッグを補助するためのスクリプト。
-   **`generated-docs/`**: 他のリポジトリから自動取得・生成されたドキュメント（例: プロジェクト概要）を参照する際の基準となるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認用ファイル。
-   **`index.md`**: 生成されたリポジトリ一覧を格納する、GitHub PagesのメインページとなるMarkdownファイル。
-   **`issue-notes/`**: 開発中に発生した問題、アイデア、検討事項などをメモしたMarkdownファイルを格納するディレクトリ。
-   **`manifest.json`**: Progressive Web App (PWA) の設定ファイル。アプリのメタデータや表示設定を定義。
-   **`pytest.ini`**: `pytest` テストフレームワークの設定ファイル。テストの実行オプションなどを指定。
-   **`requirements-dev.txt`**: 開発環境やテスト環境で必要なPythonパッケージの依存関係リスト。
-   **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要なPythonパッケージの依存関係リスト。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またどのページを避けるべきかを指示するファイル。
-   **`ruff.toml`**: `ruff` リンター・フォーマッターの設定ファイル。Pythonコードのスタイルルールを定義。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージ。
        -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成する機能を提供。
        -   **`config.yml`**: `generate_repo_list` スクリプトの実行時設定を定義するYAMLファイル。
        -   **`config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、管理する機能。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ機能。
        -   **`generate_repo_list.py`**: プロジェクトのエントリポイント。GitHub APIからリポジトリ情報を取得し、Markdownを生成するメインスクリプト。
        -   **`json_ld_template.json`**: SEO強化のため、リポジトリ情報をJSON-LD形式で構造化データとして埋め込むためのテンプレート。
        -   **`language_info.py`**: リポジトリの主要言語情報を処理・整形する機能。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成する機能。
        -   **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` から概要を自動取得する機能。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報を抽出する機能。
        -   **`repository_processor.py`**: GitHub APIから取得したリポジトリデータを処理・加工する主要なロジックを格納。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや設定を定義するテンプレート。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算する機能。
        -   **`strings.yml`**: 表示メッセージや文言を管理するためのYAMLファイル。
        -   **`template_processor.py`**: Markdown生成時に使用されるテンプレートを処理し、データと結合する機能。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ機能。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプト。
-   **`tests/`**: プロジェクト全体の単体テストや統合テストを格納するディレクトリ。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能のテスト。
    -   **`test_date_formatter.py`**: 日付整形機能のテスト。
    -   **`test_environment.py`**: 実行環境のセットアップや依存関係のテスト。
    -   **`test_integration.py`**: プロジェクトの主要な機能間の統合テスト。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    -   **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテスト。
    -   **`test_repository_processor.py`**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
（提供された情報からは具体的な関数リストが直接得られなかったため、主要なファイル名から推測される代表的な関数を記述します。引数や戻り値は一般的な役割を示します。）

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   **`main()`**:
        -   **役割**: プロジェクトのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdown生成までのプロセス全体を orchestrate します。
        -   **引数**: なし（コマンドライン引数を内部で解析）。
        -   **戻り値**: なし。
    -   **`generate_repository_list_markdown(username, output_file, limit=None)`**:
        -   **役割**: 指定されたGitHubユーザー名のリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成して指定されたファイルに出力します。
        -   **引数**: `username` (str): GitHubユーザー名、`output_file` (str): 出力ファイル名、`limit` (int, optional): 処理するリポジトリ数の上限（開発用）。
        -   **戻り値**: なし。

-   **`src/generate_repo_list/repository_processor.py`**
    -   **`fetch_repositories(username, token)`**:
        -   **役割**: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧データを取得します。
        -   **引数**: `username` (str): GitHubユーザー名、`token` (str): GitHubパーソナルアクセストークン。
        -   **戻り値**: リポジトリデータのリスト (list of dict)。
    -   **`process_repository_data(repo_data)`**:
        -   **役割**: 生のGitHubリポジトリAPIデータを受け取り、表示に必要な情報を抽出・加工して整形します。
        -   **引数**: `repo_data` (dict): 単一のリポジトリを表す辞書データ。
        -   **戻り値**: 処理・整形されたリポジトリ情報 (dict)。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **`fetch_project_overview(repo_name, config)`**:
        -   **役割**: 指定されたリポジトリの `generated-docs/project-overview.md` ファイルから、プロジェクト概要の3行説明をリモートで読み込み、抽出します。
        -   **引数**: `repo_name` (str): リポジトリ名、`config` (dict): プロジェクト概要取得機能の設定。
        -   **戻り値**: 抽出された3行の概要説明 (list of str)、または空のリスト。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   **`generate_markdown(repo_list, seo_data)`**:
        -   **役割**: 処理されたリポジトリデータのリストとSEOデータに基づいて、最終的なMarkdownコンテンツ（リポジトリ一覧）を生成します。
        -   **引数**: `repo_list` (list of dict): 処理済みリポジトリ情報のリスト、`seo_data` (dict): サイト全体のSEOメタデータ。
        -   **戻り値**: 生成されたMarkdown文字列 (str)。

-   **`src/generate_repo_list/config_manager.py`**
    -   **`load_config(config_path)`**:
        -   **役割**: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
        -   **引数**: `config_path` (str): 設定ファイルのパス。
        -   **戻り値**: 設定内容 (dict)。

-   **`src/generate_repo_list/badge_generator.py`**
    -   **`generate_badge_markdown(badge_info)`**:
        -   **役割**: バッジ情報（種類、テキストなど）から、Markdown形式で表示されるバッジの文字列を生成します。
        -   **引数**: `badge_info` (dict): バッジに関する情報。
        -   **戻り値**: 生成されたMarkdown形式のバッジ文字列 (str)。

## 関数呼び出し階層ツリー
```
提供された情報からは関数呼び出し階層の詳細な分析ができませんでした。
しかし、プロジェクトのエントリポイントである `src/generate_repo_list/generate_repo_list.py` の `main()` 関数が起点となり、
以下のような主要な処理フローで各モジュールの関数を呼び出していると推測されます。

main()
  ├── config_manager.load_config()
  ├── repository_processor.fetch_repositories()
  │     └── requests.get() など
  ├── repository_processor.process_repository_data()
  │     ├── project_overview_fetcher.fetch_project_overview()
  │     ├── readme_badge_extractor.extract_badges()
  │     ├── language_info.get_language_info()
  │     ├── statistics_calculator.calculate_statistics()
  │     └── date_formatter.format_date()
  └── markdown_generator.generate_markdown()
        ├── template_processor.process_template()
        └── badge_generator.generate_badge_markdown()

---
Generated at: 2026-02-17 07:09:19 JST
