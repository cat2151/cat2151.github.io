Last updated: 2026-09-16

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト用のリポジトリ一覧を自動生成します。
- 生成されたMarkdownはJekyllベースのサイトに最適化され、各リポジトリの3行概要を含みます。
- 検索エンジンやLLMによるリポジトリ情報の参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesサイトの基盤として使用され、生成されたMarkdownファイルを静的サイトとしてレンダリングします。
    - **Markdown**: リポジトリ一覧ページコンテンツの出力形式です。
    - **HTML/CSS/JavaScript**: Jekyllサイトを構成する標準的なWeb技術であり、生成されたページに適用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得とMarkdown生成の中核を担います。
    - **Git**: ソースコードのバージョン管理に使用されます。
    - **GitHub API**: GitHubリポジトリの情報をプログラム的に取得するために利用されます。
- テスト:
    - **pytest**: Pythonコードの単体テストおよび結合テストを行うためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: プロジェクト自体がMarkdownファイルを生成（ビルド）する役割を担います。
- 言語機能:
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に利用されます。
    - **TOML**: 設定ファイル（`ruff.toml`, `secrets.toml`）の記述に利用されます。
    - **JSON**: JSON-LDテンプレートの定義やGitHub APIレスポンスの処理に使用されます。
- 自動化・CI/CD:
    - **GitHub Actions (スクリプト)**: `.github_automation` ディレクトリには、大規模ファイルチェックなどの自動化スクリプトが含まれる可能性があります。ただし、プロジェクトはローカル開発重視とされています。
- 開発標準:
    - **Ruff**: Pythonコードのスタイルガイド強制と静的解析を行うためのLinterおよびフォーマッターです。

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルを検出するための自動化スクリプトとその設定を格納します。
        -   **`README.md`**: `check_large_files` 機能の説明ドキュメントです。
        -   **`check-large-files.toml`**: 大容量ファイルチェックの設定ファイルです。
        -   **`scripts/check_large_files.py`**: 大容量ファイルを検出するPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けヒントなどをまとめた主要なドキュメントファイルです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどの情報を保持します。
-   **`assets/`**: サイトで使用される静的リソース（画像、ファビコンなど）を格納するディレクトリです。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: サイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズ画像です。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを行うためのスクリプトです。
-   **`generated-docs/`**: 自動生成されたドキュメントやデータが格納される場所ですが、本プロジェクトではリポジトリごとの概要ファイルが期待される場所です。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト所有権確認に使用される可能性のある認証用HTMLファイルです。
-   **`index.md`**: メインのPythonスクリプトによって生成される、リポジトリ一覧を含むMarkdownファイルです。GitHub Pagesのトップページとして機能します。
-   **`issue-notes/`**: 開発中の課題やアイデア、メモなどを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモや議論が記述されたMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを定義するファイルです。ホーム画面への追加やオフライン対応に利用されます。
-   **`pytest.ini`**: `pytest` テストフレームワークの挙動をカスタマイズするための設定ファイルです。
-   **`requirements-dev.txt`**: 開発時およびテスト時にのみ必要となるPythonライブラリとそのバージョンを一覧化したファイルです。
-   **`requirements.txt`**: プロジェクトが実行時に必要とする主要なPythonライブラリとそのバージョンを一覧化したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは除外するかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのスタイルガイド強制および静的解析ツール `Ruff` の設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるルートディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧生成のメインロジックを含むPythonパッケージです。
        -   **`__init__.py`**: `generate_repo_list` パッケージであることを示すファイルです。
        -   **`badge_generator.py`**: リポジトリのプログラミング言語やステータスなどに基づいて、バッジのMarkdownを生成するロジックを実装しています。
        -   **`config.yml`**: プロジェクト概要取得機能などのスクリプトの動作を制御するための各種設定パラメータを定義するYAML形式の設定ファイルです。
        -   **`config_manager.py`**: 設定ファイル（例: `config.yml`, `secrets.toml`）の読み込み、解析、管理を行うユーティリティです。
        -   **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメインエントリポイントとなるスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        -   **`json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートを定義するファイルで、SEOの向上に寄与します。
        -   **`language_info.py`**: リポジトリで使用されているプログラミング言語の情報を取得し、処理するためのロジックを実装します。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報と抽出された概要を元に、最終的なMarkdownコンテンツを構築する役割を担います。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出・取得するロジックを実装します。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出、整形、フィルタリングなどの中間処理を行うロジックを実装します。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計する機能を提供します。
        -   **`strings.yml`**: プロジェクト内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するためのYAMLファイルです。
        -   **`template_processor.py`**: Markdown生成などで使用されるテンプレート（文字列、ファイルなど）を読み込み、データに基づいて埋め込み処理を行う汎用的なテンプレート処理機能を提供します。
        -   **`url_utils.py`**: URLの構築、解析、検証など、URLに関連するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能に関する単体テストまたは統合テストを記述したファイルです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義するためのファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator.py` の統合テストを記述したファイルです。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
    -   **`test_config.py`**: 設定管理（`config_manager.py`など）に関するテストを記述したファイルです。
    -   **`test_date_formatter.py`**: 日付フォーマットユーティリティ（`date_formatter.py`）のテストを記述したファイルです。
    -   **`test_environment.py`**: 実行環境に関するテスト（依存関係のチェックなど）を記述したファイルです。
    -   **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストを記述したファイルです。
    -   **`test_markdown_generator.py`**: Markdown生成機能（`markdown_generator.py`）のテストを記述したファイルです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能（`project_overview_fetcher.py`）のテストを記述したファイルです。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能（`readme_badge_extractor.py`）のテストを記述したファイルです。
    -   **`test_repository_processor.py`**: リポジトリ処理機能（`repository_processor.py`）のテストを記述したファイルです。

## 関数詳細説明
プロジェクト情報から具体的な関数の詳細なシグネチャや実装が提供されていないため、主要なモジュールに含まれるであろう一般的な関数とその役割を、プロジェクトの目的とファイル名から推測して説明します。

-   **`generate_repo_list.py`**:
    -   `main()`: プログラムの主要なエントリポイント。コマンドライン引数の解析、設定の読み込み、リポジトリ情報の取得、Markdownコンテンツの生成、ファイルへの出力といった一連の処理を調整し、プログラム全体の実行フローを管理します。
-   **`repository_processor.py`**:
    -   `fetch_repositories(username: str, limit: Optional[int] = None) -> List[Dict]`: 指定されたGitHubユーザー名のリポジトリ情報をGitHub APIから取得します。`limit` が指定された場合は、処理するリポジトリ数を制限します。取得したデータは、後続の処理で利用しやすい形式に整形されます。
    -   `process_repository_data(repo_data: Dict) -> Dict`: 単一のリポジトリの生データを受け取り、必要な情報（名前、説明、URL、言語、スター数、最終更新日など）を抽出し、標準化された形式で返します。
-   **`project_overview_fetcher.py`**:
    -   `get_project_overview(repo_url: str, config: Dict) -> Optional[str]`: 指定されたリポジトリのURL内の特定のパス（`generated-docs/project-overview.md`）から、プロジェクトの3行概要テキストを抽出します。`config` に基づいて、抽出対象のセクションやタイムアウトなどの設定が適用されます。
-   **`markdown_generator.py`**:
    -   `generate_repo_list_markdown(repositories: List[Dict], seo_config: Dict, strings: Dict) -> str`: 処理済みのリポジトリ情報のリストを受け取り、SEOテンプレートや定義された文言（`strings`）を適用しながら、最終的なリポジトリ一覧のMarkdown文字列を生成します。
-   **`config_manager.py`**:
    -   `load_yaml_config(file_path: str) -> Dict`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
-   **`badge_generator.py`**:
    -   `generate_language_badge(language: str) -> str`: 特定のプログラミング言語名を受け取り、その言語を示すバッジのMarkdown文字列を生成します。
    -   `generate_status_badge(status: str) -> str`: リポジトリのステータス（例: "Active", "Archived"）に応じたバッジのMarkdown文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-16 07:11:50 JST
