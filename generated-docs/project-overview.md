Last updated: 2026-02-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けのMarkdownファイルを自動生成するシステムです。
- 検索エンジン最適化を図り、リポジトリ一覧や個々のリポジトリページがより発見されやすくします。
- 各リポジトリの概要表示、分類、Jekyll/GitHub Pages対応など、豊富な機能を備えています。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: 静的サイトジェネレータとして機能し、生成されたMarkdownファイルをWebサイトとして公開するために使用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なプログラミング言語として、GitHub APIからのデータ取得、処理、Markdown生成ロジックの実装に使用されます。
    - **Git**: ソースコードのバージョン管理システムとして使用されます。
    - **GitHub API**: リポジトリ情報の取得元となるGitHubの公式APIです。
- テスト: **pytest**: Pythonアプリケーションのテストフレームワークとして、コードの品質と信頼性を保証するために使用されます。
- ビルドツール: **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルを静的サイトとしてビルドし、GitHub Pagesにデプロイするプロセスを担います。
- 言語機能: **Python**: Python言語の標準機能やライブラリを活用し、データ処理、ファイルI/O、文字列操作などを行います。
- 自動化・CI/CD: 明示的なCI/CDツールは記述されていませんが、GitHub Pagesへの自動デプロイはGitHub Actionsなどを用いて実現されることが一般的です。
- 開発標準: **Ruff**: Pythonコードのリンティングおよびフォーマットツールとして、コードスタイルの一貫性を保ち、品質を向上させるために使用されます。

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
  📄 test_readme_extractor.py
  📄 test_repository_processor.py
```

## ファイル詳細説明

*   **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義するための設定ファイルです。
*   **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトや設定を格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルを検出するための自動化スクリプトが含まれています。
        *   **README.md**: `check_large_files` ディレクトリに関する説明が記述されています。
        *   **check-large-files.toml**: 大容量ファイルチェックの設定ファイルです。
        *   **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト本体です。
*   **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイルです。
*   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
*   **README.md**: プロジェクトの概要、目的、使用方法などが記述されたメインのドキュメントファイルです。
*   **_config.yml**: Jekyllの設定ファイルで、サイトのタイトル、テーマ、プラグインなどの全体設定を定義します。
*   **assets/**: サイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
    *   **favicon-*.png**: サイトのファビコン（Webサイトのアイコン）ファイル群です。
*   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ用のスクリプトです。
*   **generated-docs/**: 生成されたドキュメントや一時ファイルを格納するディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイルです。
*   **index.md**: メインのGitHubリポジトリ一覧が自動生成されるMarkdownファイルです。
*   **issue-notes/**: 開発中に記録された課題やメモをMarkdown形式で保存するディレクトリです。
*   **manifest.json**: プログレッシブウェブアプリ（PWA）用のマニフェストファイルで、アプリのメタデータを提供します。
*   **pytest.ini**: pytestの実行設定を定義するファイルです。
*   **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージの依存関係をリスト化したファイルです。
*   **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係をリスト化したファイルです。
*   **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
*   **ruff.toml**: Ruff（Pythonリンター/フォーマッター）の設定ファイルです。
*   **src/**: プロジェクトのソースコードを格納するディレクトリです。
    *   **__init__.py**: Pythonパッケージの初期化ファイルです。
    *   **generate_repo_list/**: リポジトリ一覧生成ロジックの主要なモジュール群です。
        *   **__init__.py**: Pythonサブパッケージの初期化ファイルです。
        *   **badge_generator.py**: リポジトリのステータスに応じたバッジのMarkdownを生成するロジックを含みます。
        *   **config.yml**: `generate_repo_list` スクリプトの技術的な設定パラメータを定義します。
        *   **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するロジックを含みます。
        *   **date_formatter.py**: 日付フォーマットに関するユーティリティ関数を提供します。
        *   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
        *   **json_ld_template.json**: SEO目的のJSON-LDデータのテンプレートです。
        *   **language_info.py**: リポジトリのプログラミング言語に関する情報を処理するロジックを含みます。
        *   **markdown_generator.py**: 取得したリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを含みます。
        *   **project_overview_fetcher.py**: 各リポジトリの特定のファイルからプロジェクト概要の3行説明を抽出するロジックを含みます。
        *   **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ情報を抽出するロジックを含みます。
        *   **repository_processor.py**: GitHub APIから取得したリポジトリデータを処理・整形する主要なロジックを含みます。
        *   **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義します。
        *   **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算するロジックを含みます。
        *   **strings.yml**: UIに表示されるメッセージや文言を管理するためのファイルです。
        *   **template_processor.py**: MarkdownやJSON-LDのテンプレートに変数を適用して最終出力を生成するロジックを含みます。
        *   **url_utils.py**: URLの構築や検証に関するユーティリティ関数を提供します。
*   **test_project_overview.py**: `project_overview_fetcher` 機能の単体テストまたは統合テスト用のスクリプトです。
*   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    *   **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
    *   **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    *   **test_config.py**: 設定ファイルの読み込み・管理機能のテストです。
    *   **test_date_formatter.py**: 日付フォーマット機能のテストです。
    *   **test_environment.py**: テスト実行環境に関するテストです。
    *   **test_integration.py**: プロジェクト全体の主要な統合テストです。
    *   **test_markdown_generator.py**: Markdown生成機能のテストです。
    *   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    *   **test_readme_extractor.py**: READMEからのバッジ抽出機能のテストです。
    *   **test_repository_processor.py**: リポジトリデータ処理機能のテストです。

## 関数詳細説明

*   `src/generate_repo_list/generate_repo_list.py`:
    *   **`main()`**: プロジェクトの主要なエントリーポイント。コマンドライン引数を受け取り、GitHub APIからのリポジトリ情報の取得、データの加工、Markdown生成をオーケストレーションします。通常、プログラムの実行を制御し、結果としてファイル出力や実行ステータスを返します。
*   `src/generate_repo_list/badge_generator.py`:
    *   **`generate_badge(status: str, label: str) -> str`**: 指定されたステータスとラベルに基づき、Markdown形式のバッジ文字列を生成します。通常、リポジトリの状態（例: アクティブ、アーカイブ）を視覚的に表現するために使用されます。
*   `src/generate_repo_list/config_manager.py`:
    *   **`load_config(config_path: str) -> dict`**: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として設定データを提供します。設定値の取得や管理に使用されます。
*   `src/generate_repo_list/date_formatter.py`:
    *   **`format_date(date_str: str, format_str: str) -> str`**: 日付文字列を指定されたフォーマット文字列に従って整形します。通常、APIから取得した日付データをユーザーフレンドリーな形式で表示するために使用されます。
*   `src/generate_repo_list/language_info.py`:
    *   **`get_language_data(repository_data: dict) -> list`**: リポジトリデータから主要なプログラミング言語の情報を抽出し、整形されたリストとして返します。
*   `src/generate_repo_list/markdown_generator.py`:
    *   **`generate_repository_list_markdown(repositories: list, template: str) -> str`**: 処理されたリポジトリデータのリストとMarkdownテンプレートを受け取り、GitHub Pages向けの整形されたリポジトリ一覧Markdownコンテンツを生成します。
*   `src/generate_repo_list/project_overview_fetcher.py`:
    *   **`fetch_project_overview_from_repo(repo_full_name: str, config: dict) -> list`**: GitHub APIを通じて、指定されたリポジトリの特定ファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、リストとして返します。
*   `src/generate_repo_list/readme_badge_extractor.py`:
    *   **`extract_badges_from_readme(readme_content: str) -> list`**: READMEファイルのコンテンツから、Markdown形式のバッジ情報を解析し、抽出されたバッジのリストを返します。
*   `src/generate_repo_list/repository_processor.py`:
    *   **`fetch_and_process_repositories(username: str, github_token: str, limit: int) -> list`**: GitHub APIを介して指定ユーザーのリポジトリ情報を取得し、必要なデータ（名前、説明、URLなど）に加工・整形してリストとして返します。
*   `src/generate_repo_list/statistics_calculator.py`:
    *   **`calculate_repo_statistics(repository_data: dict) -> dict`**: リポジトリのデータを受け取り、スター数やフォーク数などの統計情報を計算して辞書形式で返します。
*   `src/generate_repo_list/template_processor.py`:
    *   **`apply_template(template_content: str, data: dict) -> str`**: テンプレート文字列とデータ辞書を受け取り、テンプレート内のプレースホルダーをデータで置き換えて最終的な文字列を生成します。
*   `src/generate_repo_list/url_utils.py`:
    *   **`build_github_api_url(endpoint: str, username: str) -> str`**: GitHub APIのエンドポイントとユーザー名を受け取り、完全なAPIリクエストURLを構築します。
*   `.github_automation/check_large_files/scripts/check_large_files.py`:
    *   **`check_files(config_path: str) -> bool`**: 指定された設定ファイルに基づき、リポジトリ内の大規模ファイルをチェックするロジックを実行します。検出されたファイルに応じて真偽値を返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-22 07:07:07 JST
