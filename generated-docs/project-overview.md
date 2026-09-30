Last updated: 2026-10-01

# Project Overview

## プロジェクト概要
- GitHub APIでリポジトリ情報を取得し、GitHub Pages向けMarkdownを自動生成するシステムです。
- Jekyllサイトのリポジトリ一覧と詳細ページをSEO最適化し、検索エンジンへの露出を向上させます。
- 各リポジトリのプロジェクト概要を自動取得し、動的な情報表示を実現します。

## 技術スタック
- フロントエンド: Jekyll（静的サイトジェネレータ）、Markdown（コンテンツ記述）、HTML/CSS/JavaScript（サイト構成）
- 音楽・オーディオ: 該当なし
- 開発ツール: Python（メインスクリプト言語）、GitHub API（リポジトリ情報取得）、PyYAML（設定ファイル処理）、TOML（設定ファイル処理）、Git（バージョン管理）
- テスト: pytest（テストフレームワーク）
- ビルドツール: Pythonスクリプト（Markdown生成）、Jekyll（最終的なウェブサイト構築）
- 言語機能: Python（スクリプト、モジュール、オブジェクト指向の一部特性）
- 自動化・CI/CD: GitHub Automation (check_large_filesスクリプトなど、特定の開発補助自動化に利用)
- 開発標準: Ruff（Pythonコードフォーマッタ・リンター）、EditorConfig（エディタ共通設定）

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
- **`.editorconfig`**: 異なるエディタ間でのコーディングスタイル（インデント、改行など）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどを用いた自動化スクリプトや設定を格納するディレクトリです。
  - **`check_large_files/README.md`**: `check_large_files` ディレクトリの目的や使い方を説明するMarkdownファイルです。
  - **`check-large-files.toml`**: 大容量ファイルを検出するための設定ファイルです。
  - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されたファイルです。
- **`README.md`**: プロジェクトの概要、機能、セットアップ方法、使用方法などを説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定（サイトタイトル、テーマ、プラグインなど）を定義するファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
  - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（アイコン）ファイルで、様々なデバイスや表示サイズに対応します。
- **`debug_project_overview.py`**: `project_overview` 機能のデバッグや挙動確認のために使用されるPythonスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されたドキュメントや一時ファイルを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: GitHub Pagesサイトのメインページ（リポジトリ一覧）として生成されるMarkdownファイルです。
- **`issue-notes/`**: 開発中の特定の課題に関するメモや詳細を格納するディレクトリです。
  - **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや考察が記されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブアプリマニフェストファイルです。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの検出ルールやオプションを定義します。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェック（リンティング）とフォーマットを行うRuffツールの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
  - **`__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成の主要ロジックを含むPythonパッケージです。
    - **`__init__.py`**: `generate_repo_list` パッケージとして認識させるためのファイルです。
    - **`badge_generator.py`**: リポジトリの言語やステータスなどのバッジを生成するロジックを実装したモジュールです。
    - **`config.yml`**: リポジトリ情報の取得設定やプロジェクト概要機能の設定など、プロジェクトの技術的パラメータを定義するYAMLファイルです。
    - **`config_manager.py`**: YAML形式の設定ファイル（`config.yml`など）を読み込み、管理するためのモジュールです。
    - **`date_formatter.py`**: 日付や時刻の情報を特定の表示形式に整形するためのユーティリティ関数を提供するモジュールです。
    - **`generate_repo_list.py`**: プログラムのメインエントリーポイント。GitHub APIからの情報取得からMarkdown生成までの全体フローを制御します。
    - **`json_ld_template.json`**: SEOのために使用されるJSON-LD形式の構造化データテンプレートです。
    - **`language_info.py`**: リポジトリの使用言語に関する情報を処理・整形するモジュールです。
    - **`markdown_generator.py`**: 取得および整形されたリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックをカプセル化したモジュールです。
    - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動的に取得するモジュールです。
    - **`readme_badge_extractor.py`**: リポジトリの `README.md` から既存のバッジ情報を抽出するモジュールです。
    - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に整形するモジュールです。
    - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュールです。
    - **`strings.yml`**: アプリケーション内で使用される表示メッセージや静的な文言を管理するためのYAMLファイルです。
    - **`template_processor.py`**: Markdownテンプレートやその他のテキストテンプレートに動的なデータを埋め込む処理を行うモジュールです。
    - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関する単体テストを記述したPythonスクリプトです。
- **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。
  - **`conftest.py`**: pytestのフィクスチャやテストの共通設定を定義するファイルです。
  - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
  - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
  - **`test_config.py`**: 設定ファイルの読み込みや処理に関するテストを記述したファイルです。
  - **`test_date_formatter.py`**: 日付整形機能のテストを記述したファイルです。
  - **`test_environment.py`**: 実行環境（依存関係など）のセットアップや状態に関するテストを記述したファイルです。
  - **`test_integration.py`**: 主要なコンポーネント間の連携に関する統合テストを記述したファイルです。
  - **`test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
  - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述したファイルです。
  - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを記述したファイルです。

## 関数詳細説明
- **`generate_repo_list.py`内の主要関数**:
  - `main(username: str, output_file: str, limit: Optional[int])`: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、処理し、最終的なMarkdownファイルを出力するプログラムのエントリーポイントです。
- **`repository_processor.py`内の主要関数**:
  - `process_repository_data(repo_data: Dict) -> Dict`: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすいように整形・加工します。
- **`project_overview_fetcher.py`内の主要関数**:
  - `fetch_project_overview(repo_name: str, owner: str, config: Dict) -> Optional[str]`: 指定されたリポジトリから `generated-docs/project-overview.md` ファイルを取得し、その中から3行のプロジェクト概要を抽出して返します。
- **`markdown_generator.py`内の主要関数**:
  - `generate_markdown(repos_list: List[Dict], seo_data: Dict, template_config: Dict) -> str`: 処理済みのリポジトリリストとSEO関連データを基に、GitHub Pages用のMarkdown形式のコンテンツを生成します。
- **`badge_generator.py`内の主要関数**:
  - `create_language_badge(language: str) -> str`: 指定されたプログラミング言語に対応するバッジのMarkdown/URLを生成します。
- **`config_manager.py`内の主要関数**:
  - `load_config(config_path: str) -> Dict`: 指定されたパスのYAML形式設定ファイルを読み込み、辞書として返します。
- **`date_formatter.py`内の主要関数**:
  - `format_date_for_display(iso_date_string: str) -> str`: ISO 8601形式の日付文字列を、ユーザーにとって読みやすい表示形式に整形します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-01 07:14:33 JST
