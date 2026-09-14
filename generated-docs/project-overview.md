Last updated: 2026-09-15

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得するシステムです。
- GitHub Pagesサイト向けにSEOを考慮したMarkdownファイル群を生成します。
- ユーザーのリポジトリ一覧と各プロジェクトの魅力を効果的に表示します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages): 静的サイトジェネレーターとしてGitHub Pagesの基盤を形成し、生成されたMarkdownファイルを公開します。Markdown: 生成されるコンテンツのフォーマットであり、SEOに最適化された静的ページを作成します。
- 音楽・オーディオ: (該当なし)
- 開発ツール: Python: コアリポジトリ情報取得、処理、Markdown生成ロジックを実装するための主要なプログラミング言語です。GitHub API: GitHubからリポジトリ情報をプログラム的に取得するためのインターフェースです。
- テスト: pytest: Pythonコードの単体テストおよび統合テストフレームワークとして利用されます。
- ビルドツール: (このプロジェクト自体がPythonスクリプトによってMarkdownファイルを生成するため、特定のビルドツールは使用していません。)
- 言語機能: Python: 汎用プログラミング言語として、リポジトリ情報のフェッチ、解析、整形、Markdown生成など、システムの中核機能を担います。
- 自動化・CI/CD: Pythonスクリプト: GitHub APIからの情報取得とMarkdownファイル生成を自動化するためのスクリプトです。
- 開発標準: ruff: Pythonコードの静的解析とフォーマットを自動的に行うツールで、コード品質と一貫性を保ちます。.editorconfig: エディタ間の設定を統一し、コードの一貫性を維持します。
- 設定・データ形式: YAML: プロジェクトの設定（例: `config.yml`, `strings.yml`, `seo_template.yml`）や表示メッセージの管理に使用されます。TOML: 秘密情報（例: `secrets.toml`）や特定のツール設定（例: `ruff.toml`, `check-large-files.toml`）の記述に利用されます。

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードスタイル（インデント、改行など）を統一するための設定ファイルです。
- **`.gitignore`**: Gitによるバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクト自体の説明、セットアップ方法、使用方法などを記述した主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の共通設定ファイルです。テーマ、プラグイン、パーマリンク構造などを定義します。
- **`assets/`**: GitHub Pagesサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用スクリプトです。
- **`generated-docs/`**: 生成されたドキュメントや関連ファイルが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認ファイルです。
- **`index.md`**: メインのPythonスクリプトによって生成されたリポジトリ一覧が書き込まれるマークダウンファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: プロジェクトに関するメモや特定の課題について記述されたファイルを格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルで、アプリのメタデータを提供します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。
- **`requirements-dev.txt`**: 開発やテストに必要なPythonライブラリのリストです。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonライブラリのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: Ruff linter/formatterの設定ファイルです。Pythonコードのスタイルや静的解析のルールを定義します。
- **`test_project_overview.py`**: プロジェクト概要取得機能のテストスクリプトです。
- **`tests/`**: プロジェクトのテストコードを格納するディレクトリです。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`src/generate_repo_list/__init__.py`**: Pythonパッケージの初期化ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（画像リンク）を生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを含む、システム全体の主要な設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、設定値を管理するモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリポイントとなるスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートファイルで、SEOメタデータを定義します。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語に関する情報を処理するモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: リポジトリ情報をもとに、Jekyll互換のMarkdownコンテンツを生成するモジュールです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: README.mdファイルから特定のバッジ情報を抽出するモジュールです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形・加工する主要なロジックを管理するモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: SEOメタデータや構造化データ（JSON-LD）のテンプレート定義が含まれる設定ファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するモジュールです。
- **`src/generate_repo_list/strings.yml`**: 表示メッセージや文言を一元管理するための設定ファイルです。
- **`src/generate_repo_list/template_processor.py`**: Jekyllテンプレートやその他のテンプレート処理を担当するモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成や解析に関するユーティリティ機能を提供します。

## 関数詳細説明
プロジェクト情報から個別の関数の詳細な説明（役割、引数、戻り値、機能）は提供されていないため、記述できません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-15 07:12:40 JST
