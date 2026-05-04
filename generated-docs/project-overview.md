Last updated: 2026-05-05

# Project Overview

## プロジェクト概要
- GitHub API を活用し、自身のGitHubリポジトリ情報を自動で取得します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEOに最適化されたリポジトリ一覧Markdownを生成します。
- これにより、リポジトリが検索エンジンにインデックスされやすくなり、LLMの参照失敗といった課題の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) とMarkdown生成によって、静的なウェブサイトとしてコンテンツを表示します。
- 音楽・オーディオ: 該当なし。
- 開発ツール:
    - Python: プロジェクトの主要なロジックを実装するために使用されるプログラミング言語です。
    - GitHub API: リポジトリ情報を動的に取得するためのインターフェースとして利用されます。
- テスト:
    - Pytest: Pythonで書かれた強力なテストフレームワークで、プロジェクトのテストコードの実行と管理に使用されます。
- ビルドツール:
    - Pythonスクリプト: GitHub APIからの情報取得とMarkdownファイル生成のプロセスを自動化します。
- 言語機能:
    - Pythonの標準ライブラリ: ファイル操作、データ処理、HTTPリクエストなど、基本的なプログラミングタスクに利用されます。
- 自動化・CI/CD:
    - GitHub Pages: 生成されたMarkdownファイルをホスティングし、ウェブサイトとして公開するプラットフォームです。
    - `.github_automation`: 将来的なGitHub Actionsによる自動化処理（例: 大容量ファイルチェック）を想定したディレクトリ構造です。
- 開発標準:
    - Ruff: Pythonコードのリンティングとフォーマットを自動化し、コード品質と一貫性を維持するためのツールです。
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを定義・適用するためのファイル形式です。

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
- **`.editorconfig`**: さまざまなエディタやIDEで一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連ファイルを格納するためのディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックする自動化スクリプト群を格納します。
        - **`README.md`**: `check_large_files`機能に関する説明を提供します。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定（しきい値など）を定義します。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: このプロジェクトのライセンス（MITライセンス）に関する情報が記載されています。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などを説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイト全体のグローバル設定を定義するファイルです（テーマ、プラグイン、カスタム変数など）。
- **`assets/`**: Jekyllサイトで使用される静的アセット（画像ファイルなど）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）のさまざまなサイズの画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得された`project-overview.md`のような自動生成ドキュメントが配置されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のためのファイルです。
- **`index.md`**: プロジェクトのメインページとして機能し、生成されたリポジトリ一覧がここに書き出されます。JekyllによってHTMLに変換されます。
- **`issue-notes/`**: 開発中に発生した課題やメモを記録するためのディレクトリです。
    - **`22.md`**: 特定の課題（Issue #22）に関するメモや詳細が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、ウェブアプリのメタデータ（名前、アイコン、表示モードなど）を定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしています。
- **`requirements.txt`**: プロジェクトの本番環境で実行するために必要なPythonパッケージとそのバージョンをリストアップしています。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロール・インデックスすべきか、またはしないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。
- **`src/`**: プロジェクトのソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成に関するコアロジックを格納するPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの言語やライセンスなどの情報からバッジ画像を生成するロジックを含みます。
        - **`config.yml`**: プロジェクト概要取得機能などの技術的パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: `config.yml`や`strings.yml`といった設定ファイルを読み込み、管理する役割を持ちます。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプトで、リポジトリ情報の取得からMarkdown生成までを一貫して実行します。
        - **`json_ld_template.json`**: SEOのために構造化データ（JSON-LD形式）を生成する際のテンプレートファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形するロジックを含みます。
        - **`markdown_generator.py`**: 取得および処理されたリポジトリデータから、最終的なMarkdownコンテンツを生成する役割を担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形する役割を持ちます。
        - **`seo_template.yml`**: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するYAMLファイルです。多言語対応（i18n）の基盤となります。
        - **`template_processor.py`**: Markdown生成時に特定のテンプレート（Jinja2など）を処理し、動的なコンテンツを埋め込む機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するさまざまなユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストを記述したファイルです。
- **`tests/`**: プロジェクトの単体テスト、統合テスト、機能テストなどを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト実行時に使用される共通フィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能のテストを記述したファイルです。
    - **`test_date_formatter.py`**: 日付整形機能のテストを記述したファイルです。
    - **`test_environment.py`**: 実行環境（依存関係など）に関するテストを記述したファイルです。
    - **`test_integration.py`**: プロジェクト全体の主要なフローの統合テストを記述したファイルです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを記述したファイルです。

## 関数詳細説明
- `src/generate_repo_list/generate_repo_list.py`
    - `main()`: このスクリプトのエントリポイントです。コマンドライン引数をパースし、設定を読み込み、リポジトリ情報を取得・処理し、最終的なMarkdownファイルを生成する一連のプロセスをオーケストレーションします。
- `src/generate_repo_list/repository_processor.py`
    - `fetch_repositories(username: str, limit: int = None) -> list`: 指定されたGitHubユーザー名のリポジトリ情報をGitHub APIから取得します。`limit`オプションが指定された場合、取得するリポジトリ数を制限します。
    - `process_repository_data(repo_data: dict, config: dict) -> dict`: GitHub APIから取得した個々のリポジトリデータ（辞書形式）を、Markdown生成に適した形式に加工・整形します。この処理には、日付のフォーマットや特定の情報抽出などが含まれます。
- `src/generate_repo_list/project_overview_fetcher.py`
    - `get_project_overview(repo_full_name: str, target_file: str, section_title: str, enable_cache: bool) -> str`: 指定されたリポジトリから特定のファイル（例: `generated-docs/project-overview.md`）の内容を読み込み、指定されたセクションタイトル（例: "プロジェクト概要"）の下にある3行説明を抽出して返します。キャッシュ機能もサポートしています。
- `src/generate_repo_list/markdown_generator.py`
    - `generate_markdown(processed_repos: list, config: dict, json_ld_template: dict) -> str`: 処理済みのリポジトリ情報と設定、JSON-LDテンプレートに基づき、リポジトリ一覧のMarkdown形式コンテンツ全体を生成します。
- `src/generate_repo_list/badge_generator.py`
    - `generate_badges_markdown(repo_info: dict) -> str`: 特定のリポジトリ情報（言語、ライセンスなど）から、表示用のバッジ（例: Shields.io形式）を生成し、Markdown形式で返します。
- `src/generate_repo_list/config_manager.py`
    - `load_config(config_path: str, strings_path: str) -> dict`: `config.yml`と`strings.yml`のYAML設定ファイルを読み込み、結合して一つの設定辞書として返します。
- `src/generate_repo_list/date_formatter.py`
    - `format_date(date_string: str) -> str`: ISO 8601形式などの日付文字列を受け取り、指定されたユーザーフレンドリーな形式（例: "YYYY年MM月DD日"）に整形して返します。
- `src/generate_repo_list/url_utils.py`
    - `create_github_repo_url(username: str, repo_name: str) -> str`: GitHubのユーザー名とリポジトリ名から、そのリポジトリのGitHub.com上のURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-05 07:24:14 JST
