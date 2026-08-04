Last updated: 2026-08-05

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたJekyll対応のMarkdownファイルは、検索エンジンのクロールを促進し、サイトの可視性を向上させます。
- 各リポジトリの概要を自動取得・表示することで、情報の網羅性を高め、LLMによるリポジトリ参照失敗の緩和も期待されます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages): GitHub Pagesサイトの構築基盤として使用され、生成されたMarkdownファイルを静的サイトとして公開します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: プロジェクトの主要なプログラミング言語であり、リポジトリ情報の取得、処理、Markdown生成スクリプトを実行します。
    - **GitHub API**: GitHubのリポジトリ情報をプログラム的に取得するためのインターフェースとして利用されます。
    - **pytest**: Pythonコードのテストフレームワーク。単体テストや統合テストの実行に利用されます。
    - **ruff**: Pythonコードの高速なLinterおよびFormatter。コード品質とスタイルの一貫性を保つために使用されます。
- テスト: **pytest**: コードの正確性と信頼性を確保するためのテスト実行環境です。
- ビルドツール:
    - **Python スクリプト**: `generate_repo_list.py` を中心としたPythonスクリプト群が、リポジトリ情報を取得しMarkdownファイルを生成するビルドプロセスを担います。
    - **Markdown**: 生成される最終的なドキュメント形式です。
- 言語機能: **Python**: 汎用的なプログラミング言語として、データ処理、API通信、ファイル操作など、システムの中核機能を提供します。
- 自動化・CI/CD:
    - **GitHub Actions (間接的)**: GitHub Pagesへのデプロイやトークン管理など、本システムはGitHub Actionsとの連携を想定した設計となっています。
    - **Pythonスクリプト**: リポジトリ一覧の生成プロセス自体が自動化されたタスクとして実行されます。
- 開発標準: **ruff**: コードの整形と静的解析により、プロジェクト全体のコードスタイルと品質を統一します。

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
- **.editorconfig**: 異なるエディタやIDE間でコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイル。
- **.github_automation/**: GitHub Actionsなど、GitHub上での自動化ワークフローに関連するスクリプトや設定を格納するディレクトリ。
- **.github_automation/check_large_files/**: 大容量ファイルのチェック機能に関するファイル群。
- **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明ドキュメント。
- **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェックのルールや設定を定義するTOML形式の設定ファイル。
- **.github_automation/check_large_files/scripts/**: 大容量ファイルチェックの実行スクリプトを格納するディレクトリ。
- **.github_automation/check_large_files/scripts/check_large_files.py**: プロジェクト内の大容量ファイルを特定し、警告またはエラーを出すためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されたファイル。
- **README.md**: プロジェクトの概要、目的、使い方、インストール手順、開発者向け情報などを説明するメインドキュメント。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトタイトル、テーマ、プラグインなどの設定を含みます。
- **assets/**: GitHub Pagesサイトで使用される画像、ファビコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリ。
- **assets/favicon-*.png**: 各種デバイスやブラウザで使用されるファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher` などのプロジェクト概要取得機能の動作確認やデバッグを目的としたスクリプト。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメントや概要データが格納されることを想定したディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧をまとめたメインのMarkdownファイル。Jekyllサイトのトップページとして機能します。
- **issue-notes/**: 開発中の課題や検討事項、メモなどをMarkdown形式で記録するディレクトリ。
- **issue-notes/22.md**: 特定の課題（Issue #22など）に関する詳細なメモや議論が記述されたMarkdownファイル。
- **manifest.json**: Progressive Web App (PWA) のマニフェストファイル。アプリのアイコン、表示モード、起動URLなどを定義します。
- **pytest.ini**: `pytest` テストフレームワークの設定ファイル。テストの検出ルールやオプションを定義します。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: プロジェクトの実行に必要な本番環境用のPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはならないかを指示するファイル。
- **ruff.toml**: PythonのLinterおよびFormatterである`ruff`の設定ファイル。コードスタイルルールや無視する項目を定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
- **src/__init__.py**: Pythonパッケージの初期化ファイル。`src` ディレクトリがPythonパッケージであることを示します。
- **src/generate_repo_list/**: リポジトリ一覧を生成するコアロジックを含むPythonパッケージ。
- **src/generate_repo_list/__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
- **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（例: Shields.io）を生成または管理するロジック。
- **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプト固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するファイル。
- **src/generate_repo_list/config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するクラスや関数を提供します。
- **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付情報を、ユーザーフレンドリーな形式に整形するためのユーティリティ関数を提供します。
- **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成をオーケストレートします。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のため、JSON-LD形式の構造化データテンプレートを定義するファイル。
- **src/generate_repo_list/language_info.py**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するロジック。
- **src/generate_repo_list/markdown_generator.py**: 取得・処理されたリポジトリ情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジック。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出するロジック。
- **src/generate_repo_list/readme_badge_extractor.py**: 各リポジトリのREADMEファイルから、既存のバッジ情報を抽出・解析するロジック。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換する処理を担当します。
- **src/generate_repo_list/seo_template.yml**: 各リポジトリのページや一覧ページのSEOメタデータ（タイトル、説明など）を生成するためのテンプレート設定ファイル。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジック。
- **src/generate_repo_list/strings.yml**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元管理するためのYAMLファイル。多言語対応の基盤にもなり得ます。
- **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレートファイル（例: Jinja2テンプレートなど）を読み込み、データに基づいてレンダリングするロジック。
- **src/generate_repo_list/url_utils.py**: GitHubリポジトリやプロフィールページなど、URLの生成や解析を行うユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能に対するテストケースを記述したファイル。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
- **tests/conftest.py**: `pytest` のフィクスチャ（テストのための準備や後処理を行う関数）や共通設定を定義するファイル。
- **tests/test_badge_generator_integration.py**: `badge_generator.py` の機能を他のモジュールと連携させた際の統合テスト。
- **tests/test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
- **tests/test_config.py**: `config_manager.py` や `config.yml` などの設定関連モジュールのテスト。
- **tests/test_date_formatter.py**: 日付フォーマットユーティリティのテスト。
- **tests/test_environment.py**: 実行環境の設定や依存関係が正しく準備されているかを確認するテスト。
- **tests/test_integration.py**: システム全体の主要なフローが正しく機能するかを確認する統合テスト。
- **tests/test_markdown_generator.py**: `markdown_generator.py` が正しいMarkdownを生成するかどうかのテスト。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher.py` が正しくプロジェクト概要を抽出できるかどうかのテスト。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor.py` がREADMEからバッジ情報を正確に抽出できるかどうかのテスト。
- **tests/test_repository_processor.py**: `repository_processor.py` がリポジトリデータを正しく処理・整形できるかどうかのテスト。

## 関数詳細説明
提供されたプロジェクト情報から具体的な関数シグネチャは抽出できませんでしたが、主要なスクリプトファイルに基づき、想定される関数の役割を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main()`**: プログラムのエントリポイント。コマンドライン引数をパースし、リポジトリ情報の取得、処理、Markdown生成という一連のワークフローを orchestrate します。
        - 役割: プログラム全体の実行フローを制御。
        - 引数: コマンドライン引数（ユーザー名、出力ファイル名、リミットなど）。
        - 戻り値: なし (サイドエフェクトとしてファイル出力)。
    - **`fetch_repositories(username, limit)`**: GitHub APIを呼び出し、指定されたユーザーのリポジトリ情報を取得します。
        - 役割: GitHubからリポジトリデータを取得。
        - 引数: `username` (GitHubユーザー名)、`limit` (取得するリポジトリ数の上限、オプション)。
        - 戻り値: リポジトリデータのリスト。
    - **`generate_markdown_output(processed_repos, output_path)`**: 処理済みのリポジトリデータを受け取り、Markdown形式で整形して指定されたファイルに出力します。
        - 役割: Markdownコンテンツを生成し、ファイルに書き込む。
        - 引数: `processed_repos` (処理済みリポジトリデータのリスト)、`output_path` (出力ファイルのパス)。
        - 戻り値: なし。

- **`src/generate_repo_list/repository_processor.py`**:
    - **`process_repository_data(repo_data)`**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、Markdown生成に適した内部データ構造に変換・整形します。
        - 役割: リポジトリの生データを整形・フィルタリング。
        - 引数: `repo_data` (単一のリポジトリ生データ)。
        - 戻り値: 処理済みのリポジトリデータ辞書。

- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_name, owner, config)`**: 指定されたリポジトリから `project-overview.md` ファイルの内容を取得し、その中から「プロジェクト概要」セクションの3行説明を抽出します。
        - 役割: 各リポジトリの概要説明を外部ファイルから取得・解析。
        - 引数: `repo_name` (リポジトリ名)、`owner` (リポジトリの所有者)、`config` (設定オブジェクト)。
        - 戻り値: 3行のプロジェクト概要文字列（またはデフォルト値）。

- **`src/generate_repo_list/markdown_generator.py`**:
    - **`create_repo_list_markdown(processed_repos, strings)`**: 処理済みの全リポジトリデータと表示文字列テンプレートを用いて、最終的なリポジトリ一覧のMarkdownコンテンツ全体を構築します。
        - 役割: テンプレートとデータを用いてMarkdownテキストを生成。
        - 引数: `processed_repos` (処理済みリポジトリデータのリスト)、`strings` (表示メッセージ文字列)。
        - 戻り値: 生成されたMarkdown文字列。

- **`src/generate_repo_list/config_manager.py`**:
    - **`load_config(config_path)`**: 指定されたパスからYAML設定ファイルを読み込み、設定オブジェクトとして返します。
        - 役割: 設定ファイルの読み込み。
        - 引数: `config_path` (設定ファイルのパス)。
        - 戻り値: 設定データ辞書またはオブジェクト。

- **`src/generate_repo_list/date_formatter.py`**:
    - **`format_github_date(date_str)`**: GitHub APIから返されるISO 8601形式の日付文字列を、人間が読みやすい形式に変換します。
        - 役割: 日付文字列の整形。
        - 引数: `date_str` (日付の文字列)。
        - 戻り値: 整形された日付文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-08-05 07:26:12 JST
