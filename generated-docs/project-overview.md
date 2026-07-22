Last updated: 2026-07-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages用のリポジトリ一覧Markdownを自動生成します。
- 検索エンジンからのクロールを促進し、各リポジトリの発見性を高めることを目的としています。
- LLMによるリポジトリ参照失敗の緩和も期待される、SEO最適化されたコンテンツ生成システムです。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として使用されており、生成されたMarkdownファイルを表示するために機能します。), Markdown (自動生成されるコンテンツの形式であり、JekyllによってHTMLに変換されます。)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語として、GitHub APIからの情報取得とMarkdown生成の中核を担います。), Pytest (Pythonコードの単体テストおよび結合テストを行うためのテストフレームワークです。), Ruff (Pythonコードのフォーマットとリンティングを自動的に行い、コード品質と一貫性を維持します。)
- テスト: Pytest (Pythonコードの機能が期待通りに動作するかを検証するためのテストフレームワークです。)
- ビルドツール: Pythonスクリプト (Pythonで書かれたメインスクリプト自体が、リポジトリ情報からMarkdownファイルを「ビルド」する役割を果たします。)
- 言語機能: Python (汎用プログラミング言語として、API通信、データ処理、ファイルI/Oなど、プロジェクトの全般的なロジックを実装します。)
- 自動化・CI/CD: このプロジェクトはローカル開発重視であり、CI/CDによる自動化は明示されていません。
- 開発標準: Ruff (コードのスタイルを統一し、潜在的なエラーを検出するためのリンター/フォーマッターとして機能します。)

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのインデントや文字コードなどの基本的な書式設定を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化関連スクリプトや設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトの説明が記述されています。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイル検出スクリプトの設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリ（例: ビルド生成物、ログファイル、一時ファイル）を指定するファイルです。
- **`LICENSE`**: プロジェクトのソフトウェアライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法などが記述されたメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`assets/favicon-16x16.png`**, **`assets/favicon-192x192.png`**, **`assets/favicon-32x32.png`**, **`assets/favicon-512x512.png`**: 異なるサイズのファビコン（ウェブサイトのアイコン）画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストに使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが格納されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのメインページとして機能するMarkdownファイルです。このプロジェクトでは、ここにリポジトリ一覧が自動生成されます。
- **`issue-notes/`**: 開発中の課題やメモを格納するためのディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（ID: 22）に関するメモファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを提供するJSONファイルで、ホーム画面への追加やオフライン機能の設定に使用されます。
- **`pytest.ini`**: Pytestテストフレームワークの設定ファイルです。テストの実行方法やオプションが定義されます。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境で必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはクロールしてはならないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのリンティングおよびフォーマットツールであるRuffの設定ファイルです。
- **`src/`**: プロジェクトのソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを認識させるための空ファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックが格納されているパッケージです。
        - **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして`generate_repo_list`ディレクトリを認識させるための空ファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示するバッジ（例: 言語、ライセンス）を生成するロジックを含みます。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの技術的な設定パラメータ（例: プロジェクト概要取得機能の有効/無効、タイムアウト設定）を定義するファイルです。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル(`config.yml`)の読み込みと管理を行うモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプトです。
        - **`src/generate_repo_list/json_ld_template.json`**: SEOのためにJSON-LD形式の構造化データを生成するためのテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理および整形するモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するロジックを含みます。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの`generated-docs/project-overview.md`からプロジェクト概要の3行説明を抽出する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出するモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換する主要なロジックを含みます。
        - **`src/generate_repo_list/seo_template.yml`**: SEOメタデータ生成のためのテンプレート設定ファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数、最終更新日）を計算または集計するモジュールです。
        - **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言を管理するためのファイルです。多言語対応や文言の一元管理に利用されます。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートの読み込み、解析、およびデータ埋め込みを処理します。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成や解析、正規化など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`tests/conftest.py`**: Pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストコードです。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトのテストコードです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストコードです。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストコードです。
    - **`tests/test_environment.py`**: 開発環境や依存関係が正しく設定されているかを確認するテストコードです。
    - **`tests/test_integration.py`**: プロジェクト全体の主要なモジュール間の連携を検証する統合テストコードです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストコードです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
    - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストコードです。
    - **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテストコードです。

## 関数詳細説明
本プロジェクトの主要な機能はPythonスクリプトによって提供されており、以下の主要な役割を持つ関数群が存在すると考えられます。具体的な引数や戻り値は提供されていませんが、それぞれの役割は以下の通りです。

- **`generate_repo_list.py` 内の主要関数**:
    - **`main()`**: プログラムのエントリーポイント。コマンドライン引数をパースし、設定を読み込み、リポジトリ情報の取得からMarkdown生成までの全体のフローを orchestrate します。
- **`repository_processor.py` 内の主要関数**:
    - **`fetch_repositories(username, token)`**: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub API経由で取得します。認証のためのトークンを使用します。
    - **`process_repository_data(repo_data)`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（例: 説明、言語、スター数、最終更新日）を抽出・整形します。
- **`project_overview_fetcher.py` 内の主要関数**:
    - **`get_project_overview(repo_url, config)`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を非同期的に取得します。設定ファイルで指定されたパスとタイムアウトを使用します。
- **`markdown_generator.py` 内の主要関数**:
    - **`generate_markdown(repositories_info, template_data)`**: 処理済みのリポジトリ情報とMarkdownテンプレートのデータを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- **`config_manager.py` 内の主要関数**:
    - **`load_config(config_path)`**: 指定されたパスから設定ファイル（例: `config.yml`）を読み込み、Pythonオブジェクトとして提供します。
- **`badge_generator.py` 内の主要関数**:
    - **`create_badge_markdown(badge_data)`**: リポジトリの言語やライセンスなどの情報に基づいて、対応するバッジのMarkdownスニペットを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-23 07:24:03 JST
