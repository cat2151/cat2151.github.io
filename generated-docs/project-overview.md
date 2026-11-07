Last updated: 2026-11-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動で取得するシステムです。
- 取得した情報から、GitHub Pages向けのSEO最適化されたリポジトリ一覧Markdownを生成します。
- これにより、リポジトリの検索エンジンからの発見性を高め、LLMからの参照性向上も期待されます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータとして利用され、生成されたMarkdownファイルを美しいWebページに変換します。)、**Markdown** (リポジトリ一覧のコンテンツを記述するフォーマットであり、SEO最適化されたWebページとして出力されます。)、**GitHub Pages** (静的サイトホスティングサービスで、JekyllとMarkdownによって構築されたリポジトリ一覧サイトを公開します。)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **GitHub API** (リポジトリ情報を取得するための主要なインターフェースです。)、**Python** (メインのスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成ロジックを実装しています。)、**YAML** (設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、各種パラメータや文言を管理します。)、**TOML** (シークレット情報 (`secrets.toml`) や一部設定ファイル (`ruff.toml`, `check-large-files.toml`) の記述に使用されます。)
- テスト: **pytest** (Pythonプロジェクトの単体テスト、結合テスト、および統合テストを実行するためのフレームワークです。)
- ビルドツール: **Pythonスクリプト** (`src/generate_repo_list/generate_repo_list.py` が実質的なビルドスクリプトとして機能し、Markdownファイルを生成します。)、**Jekyll** (GitHub Pagesのビルドプロセスの一部として、生成されたMarkdownからHTMLを構築します。)
- 言語機能: **Python** (スクリプト言語として、データ処理やAPI連携、ファイル操作などの中核を担います。)、**Markdown** (生成される最終コンテンツのフォーマットです。)、**YAML** (構造化された設定データを定義するために使用されます。)、**JSON** (GitHub APIからのデータ形式や、SEOメタデータ (`json_ld_template.json`) に使用されます。)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在と、プロジェクト内のドキュメントの言及から、CI/CDや自動化にGitHub Actionsが使用されている可能性が高いです。例えば、大容量ファイルチェックなど。)
- 開発標準: **ruff** (Pythonコードのリンティングとフォーマットを自動的に行うツールで、コード品質と一貫性を保ちます。)、**.editorconfig** (異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。)

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
- **`.editorconfig`**: コードエディタ間でインデントスタイル、文字コードなどの基本設定を統一するためのファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトが格納されるディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明です。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの目的、主な機能、使い方、開発者向けのヒントなどが記述された、プロジェクトの玄関となるドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの動作に影響を与えます。
- **`assets/`**: Webサイトで使用される画像やアイコンなどの静的リソースを格納するディレクトリです。
    - **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグを目的としたスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得・生成されたドキュメント（特に`project-overview.md`）が一時的に格納される、または参照される場所です。
- **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認用ファイルです。
- **`index.md`**: メインの出力ファイルであり、生成されたリポジトリ一覧が記述されるMarkdownファイルです。これがGitHub Pagesで公開されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細情報が記述されているファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルで、Webサイトをネイティブアプリのようにインストール可能にするための情報を含みます。
- **`pytest.ini`**: `pytest` のテスト実行に関する設定を記述するファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを定義するファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境用のPythonパッケージとそのバージョンを定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか、しないかを指示するファイルです。
- **`ruff.toml`**: `ruff` リンターおよびフォーマッターの動作設定を定義するファイルです。
- **`src/__init__.py`**: Pythonパッケージの初期化ファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むPythonパッケージです。
    - **`src/generate_repo_list/__init__.py`**: Pythonサブパッケージの初期化ファイルです。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示するバッジを生成するロジックを実装しています。
    - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、スクリプトの技術的パラメータを設定するYAMLファイルです。
    - **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）を読み込み、管理するためのモジュールです。
    - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
    - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトであり、リポジトリ情報の取得からMarkdown生成までの全体プロセスを orchestrate します。
    - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレートです。
    - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理します。
    - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式の出力を生成する主要なモジュールです。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` から概要説明を抽出する機能を提供します。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報（例: ビルドステータス、ライセンスなど）を抽出するモジュールです。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に整形する役割を担います。
    - **`src/generate_repo_list/seo_template.yml`**: SEOメタデータを設定するためのテンプレートファイルです。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するモジュールです。
    - **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownファイル内で使用される各種メッセージや文言を国際化・一元管理するためのYAMLファイルです。
    - **`src/generate_repo_list/template_processor.py`**: Markdown生成におけるテンプレート処理を担当するモジュールです。
    - **`src/generate_repo_list/url_utils.py`**: URLの操作や検証に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher`) の単体テストを目的としたスクリプトです。
- **`tests/`**: プロジェクト全体のテストケースを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義するファイルです。
    - **`tests/test_*.py`**: 各モジュールや機能の単体テスト、統合テストが含まれます。

## 関数詳細説明
- **GitHubリポジトリ情報取得機能**: GitHub APIを介して、指定されたユーザーのリポジトリリスト、詳細情報、およびREADMEコンテンツを取得します。引数としてユーザー名や認証トークンを受け取り、リポジトリデータのリストを返します。
- **プロジェクト概要抽出機能**: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）から、指定されたセクション（例: 「プロジェクト概要」）の3行説明を解析し、抽出します。引数としてリポジトリURLやファイルパスを受け取り、抽出された概要文字列を返します。
- **Markdown生成機能**: 処理されたリポジトリ情報と抽出された概要に基づき、Jekyll/GitHub Pagesに適したSEO最適化されたMarkdownファイルを生成します。引数としてリポジトリデータのリスト、出力ファイルパスを受け取り、Markdownファイルを生成します。
- **設定管理機能**: プロジェクト全体の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、アプリケーション全体で利用可能な設定オブジェクトとして提供します。引数なし、または設定ファイルのパスを受け取り、設定オブジェクトを返します。
- **バッジ生成機能**: リポジトリのステータスや特性（アクティブ、アーカイブ、フォークなど）を示すバッジのHTMLまたはMarkdownスニペットを生成します。引数としてリポジトリの属性を受け取り、バッジ文字列を返します。
- **リポジトリデータ処理機能**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換します。引数として生のリポジトリデータを受け取り、処理済みリポジトリオブジェクトを返します。

## 関数呼び出し階層ツリー
```
利用可能な情報からは関数呼び出し階層を生成できませんでした。

---
Generated at: 2026-11-08 07:06:57 JST
