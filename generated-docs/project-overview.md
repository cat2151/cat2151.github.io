Last updated: 2026-08-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得・整理するシステムです。
- 取得した情報から、GitHub Pagesサイト用のSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンからのリポジトリ発見性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベース) を利用し、Markdown形式でコンテンツを生成します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: GitHub APIを使用してリポジトリ情報を取得します。ローカル開発・テストには `pytest` を、コードスタイルチェックには `ruff` を使用しています。
- テスト: `pytest` を用いてユニットテストおよび結合テストを実行し、コードの品質と信頼性を確保します。
- ビルドツール: Pythonスクリプトが主要なビルドロジック（Markdown生成）を担います。依存関係管理には `requirements.txt` と `requirements-dev.txt` が利用されます。
- 言語機能: Pythonを主要な開発言語として使用しており、YAMLやTOML形式の設定ファイル (`config.yml`, `ruff.toml` など) のパースに標準的なライブラリや機能を使用します。
- 自動化・CI/CD: GitHub APIを介した情報取得とPythonスクリプトによるMarkdown生成が主要な自動化プロセスです。`.github_automation` ディレクトリには、GitHub Actionsなどで活用される可能性のあるスクリプトが含まれます。
- 開発標準: `ruff` によるコードスタイル強制と `.editorconfig` によるエディタ設定の統一により、コード品質と可読性を維持します。

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
- **`.editorconfig`**: 複数のエディタやIDE間で一貫したコーディングスタイルを定義する設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。`check_large_files/` は大規模なファイルの検出スクリプトを含みます。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報 (MITライセンス) を定義するファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、開発者向けヒントなどを記述したメインのドキュメントファイルです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定を定義するファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコン（`favicon-*.png`）などの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグを支援するためのスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動生成されるドキュメントや概要ファイルが一時的に置かれる可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: プロジェクトのメインスクリプトによって生成される、リポジトリ一覧を含むGitHub Pagesのトップページです。
- **`issue-notes/22.md`**: 開発中の特定の課題（Issue #22）に関するメモや詳細を記述したファイルです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、PWA（Progressive Web App）機能を提供するために使用されます。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: PythonのLinter/Formatterである `ruff` の設定ファイルで、コードスタイルと品質を定義します。
- **`src/generate_repo_list/__init__.py`**: Pythonパッケージの初期化ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（例: 使用言語、最終更新日など）を生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的なパラメータを定義する主要な設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` や外部のシークレットファイル (`secrets.toml` など) から設定を読み込み、管理するためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の形式にフォーマットするためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
- **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のために構造化データ（JSON-LD）を生成する際のテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示可能な形式に変換するモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリ情報から、GitHub Pages向けに最適化されたMarkdownコンテンツを生成するロジックを提供します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を自動的に抽出し取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出し解析するモジュールです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、分類（アクティブ、アーカイブ、フォークなど）や必要な情報抽出を行うモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータや記述のテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算し、整理する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: プロジェクトで表示される各種メッセージ、ラベル、文言などを一元的に管理するためのファイルです。
- **`src/generate_repo_list/template_processor.py`**: 生成されるMarkdownコンテンツの構造を定義するテンプレートを処理し、動的なデータを埋め込む機能を提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能に関する具体的なテストケースを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。`conftest.py` はpytestのフィクスチャ定義に、その他の `test_*.py` ファイルは各モジュールの単体・結合テストに用いられます。

## 関数詳細説明
提供された情報では関数の詳細な説明を生成できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-31 07:10:54 JST
