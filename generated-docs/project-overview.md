Last updated: 2026-07-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages用のマークダウンを自動生成するシステムです。
- 生成されたリポジトリ一覧は、検索エンジン最適化（SEO）とLLMによるリポジトリ参照の改善を目指します。
- 各リポジトリの概要文、バッジ、分類などを自動で整理し、視覚的に分かりやすい表示を提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages) - MarkdownファイルをHTMLに変換し、静的サイトを構築するために使用されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **pytest**: Pythonアプリケーションのテストフレームワークです。単体テストや統合テストの実行に利用されます。
    - **ruff**: Pythonコードのスタイルチェックとフォーマットを高速に行うLinterおよびFormatterです。コード品質と一貫性を保ちます。
- テスト: **pytest** - 上記の通り、プロジェクトの各種機能の検証に用いられます。
- ビルドツール: 該当なし（PythonスクリプトがMarkdown生成を担います）
- 言語機能: **Python** - プロジェクトの主要なプログラミング言語であり、リポジトリ情報の取得、処理、Markdown生成の全てを実行します。
- 自動化・CI/CD: **GitHub API** - GitHubリポジトリのメタデータをプログラム的に取得するために使用されます。
- 開発標準: **ruff** - コードの品質と統一されたコーディングスタイルを維持するために導入されています。

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
- **`.editorconfig`**: 異なる開発環境間でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイル。
- **`.github_automation/`**: GitHub関連の自動化スクリプトや設定を格納するディレクトリ。
    - **`check_large_files/README.md`**: `.github_automation/check_large_files`サブディレクトリの目的と使用方法を説明するドキュメント。
    - **`check-large-files.toml`**: リポジトリ内の大容量ファイルをチェックするツールの設定ファイル。
    - **`scripts/check_large_files.py`**: GitHubリポジトリ内の指定されたサイズを超えるファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイル。
- **`LICENSE`**: プロジェクトがMITライセンスの下で公開されていることを示すライセンス条項を記載したファイル。
- **`README.md`**: プロジェクトの概要、機能、セットアップ方法、使用方法、開発者向けのヒントなどを説明する主要なドキュメント。
- **`_config.yml`**: Jekyllサイトの全体設定ファイル。サイトタイトル、テーマ、プラグインなどの設定を含む。
- **`assets/`**: Jekyllサイトで使用される静的なリソース（画像、ファビコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイル。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグや単体テストを目的としたスクリプト。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが配置されることを想定したディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでウェブサイトの所有権を確認するために配置されるファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。本プロジェクトによりリポジトリ一覧が生成され、このファイルに出力される。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリ。
    - **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記述したファイル。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの表示名、アイコン、表示モードなどを定義する。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。テスト実行時のオプションなどを指定する。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンをリストアップしたファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどのページをクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **`ruff.toml`**: Pythonコードのスタイルチェックツール`ruff`の設定ファイル。コーディング規約や自動修正ルールを定義する。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリ。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するロジックをカプセル化したPythonパッケージ。
        - **`badge_generator.py`**: リポジトリのプロパティ（言語、スター数など）に基づいて表示用のバッジ情報を生成する。
        - **`config.yml`**: リポジトリ一覧生成に関する各種設定（プロジェクト概要の取得設定など）を定義するYAMLファイル。
        - **`config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で設定値にアクセスするための機能を提供する。
        - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するユーティリティ機能を提供する。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプト。GitHub APIからの情報取得、処理、Markdown生成までの一連のフローを制御する。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ`JSON-LD`を生成するためのテンプレート。
        - **`language_info.py`**: リポジトリのプログラミング言語情報に関連する処理（例: 人気度、色）を行う。
        - **`markdown_generator.py`**: 整形されたリポジトリ情報と抽出されたプロジェクト概要を基に、最終的なMarkdownコンテンツを生成する。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）からプロジェクトの3行概要を抽出する機能を提供する。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報（説明、言語、スター数など）を抽出し、Markdown生成に適した形式に整形する。
        - **`seo_template.yml`**: SEO関連のメタタグやその他の設定を定義するためのテンプレートファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算または集計する。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するためのYAMLファイル。
多言語対応や文言修正を容易にする。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイル（例: Jinja2テンプレート）を処理し、データと結合する。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供する。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプト。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **`conftest.py`**: `pytest`のテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合的な動作を検証するテスト。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトの機能を検証するテスト。
    - **`test_config.py`**: 設定ファイルの読み込みや管理を行う`config_manager`モジュールの機能を検証するテスト。
    - **`test_date_formatter.py`**: `date_formatter`モジュールの日付フォーマット機能のテスト。
    - **`test_environment.py`**: プロジェクトの実行環境が適切に設定されているかを確認するテスト。
    - **`test_integration.py`**: `generate_repo_list`パッケージ全体の主要なフローが正しく連携して動作するかを検証する統合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator`モジュールのMarkdown生成機能を検証するテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの機能、特に概要文の抽出ロジックを検証するテスト。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールの機能、特にREADMEからのバッジ抽出ロジックを検証するテスト。
    - **`test_repository_processor.py`**: `repository_processor`モジュールの機能、特にリポジトリデータ処理ロジックを検証するテスト。

## 関数詳細説明
提供された情報では個別の関数シグネチャや詳細な呼び出し関係は分析されていませんが、各モジュールが担う主要な機能に基づいて、一般的に期待される関数の役割を説明します。

- **`generate_repo_list.py`内の主要関数**:
    - **役割**: プログラムのエントリーポイントとして、リポジトリ情報の取得からMarkdownファイル生成までの一連の処理を統括します。
    - **機能**: 引数としてGitHubユーザー名や出力ファイル名を受け取り、`config_manager`を通じて設定を読み込み、`repository_processor`や`project_overview_fetcher`、`markdown_generator`などの各モジュールを呼び出して全体のワークフローを orchestrate します。
- **`repository_processor.py`内の主要関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを処理し、Markdown生成に適した構造に整形します。
    - **機能**: 各リポジトリオブジェクトを受け取り、必要な情報（名前、説明、URL、スター数、言語など）を抽出し、加工して標準化された形式で返します。
- **`project_overview_fetcher.py`内の主要関数**:
    - **役割**: 各リポジトリ内の指定されたファイルからプロジェクト概要の3行説明を自動で抽出します。
    - **機能**: リポジトリのURLやファイルパスを受け取り、該当ファイルをHTTPリクエストで取得し、マークダウンの特定のセクションから指定された行数をパースして返します。
- **`markdown_generator.py`内の主要関数**:
    - **役割**: 整形されたリポジトリ情報と抽出されたプロジェクト概要を基に、最終的なMarkdownコンテンツを生成します。
    - **機能**: 複数のリポジトリデータを受け取り、内部で定義されたテンプレートや`badge_generator`などを利用して、SEOに最適化されたリポジトリ一覧のMarkdown文字列を構築します。
- **`config_manager.py`内の主要関数**:
    - **役割**: 設定ファイル（`config.yml`, `secrets.toml`）を読み込み、アプリケーション全体で設定値にアクセスするためのインターフェースを提供します。
    - **機能**: 設定ファイルをパースし、キーに基づいて設定値を安全に取得するメソッドを提供します。シークレット情報の管理も行います。
- **`badge_generator.py`内の主要関数**:
    - **役割**: リポジトリの各種情報に基づいて、表示用のバッジ（例: 言語、スター数）のMarkdownまたはURLを生成します。
    - **機能**: リポジトリの言語やスター数などのデータを受け取り、バッジ画像を指すURLや、それを埋め込むためのMarkdownスニペットを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-31 07:25:31 JST
