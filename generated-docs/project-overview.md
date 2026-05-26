Last updated: 2026-05-27

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのGitHubリポジトリ一覧を自動で取得・処理するシステムです。
- 取得したリポジトリ情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたMarkdownファイルを生成します。
- これにより、リポジトリの検索エンジンでの可視性を高め、LLMがリポジトリ情報を参照できない課題の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) は最終的な出力・表示プラットフォームとして利用されます。システム自体は直接的なフロントエンド技術を使用せず、Markdownファイルを生成します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - GitHub API: リポジトリ情報の取得に利用されます。
    - Git: ソースコードのバージョン管理システムとして使用されます。
- テスト: `pytest`は、Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール: Pythonスクリプト自体が、リポジトリ情報の処理とMarkdownファイルの生成という「ビルド」プロセスを実行します。
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語であり、API連携、データ処理、Markdown生成のロジックを実装します。
    - YAML: システム設定 (`config.yml`, `strings.yml`, `seo_template.yml`) や、リポジトリ概要のフォーマット、Jekyllサイトの設定 (`_config.yml`) に使用されます。
    - Markdown: 生成されるリポジトリ一覧の出力形式です。
    - JSON: 構造化データ (`json_ld_template.json`) やAPIレスポンスの処理に使用されます。
    - TOML: プロジェクトの設定ファイル (`ruff.toml`, `secrets.toml`) に使用されます。
- 自動化・CI/CD: Pythonスクリプト (`generate_repo_list.py`) が自動化された生成プロセスを実行します。プロジェクトはローカル開発を重視しており、明示的なCI/CDパイプラインは推奨されていませんが、自動生成自体が自動化の核となります。
- 開発標準:
    - `ruff`: Pythonコードのスタイルチェック（lint）と自動フォーマットを行う高速なツールです。
    - `.editorconfig`: 異なるエディタやIDE間でコードスタイルを統一するための設定ファイルです。

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  22.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間でコードのインデントスタイル、文字コードなどの設定を統一するためのファイル。
- **`.github_automation/check_large_files/`**: 大容量ファイルをチェックするための補助的な自動化スクリプト群。
    - **`README.md`**: `check_large_files`スクリプトの目的と使い方を説明するドキュメント。
    - **`check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイル。
    - **`scripts/check_large_files.py`**: リポジトリ内の特定の条件（例: ファイルサイズ）に合致するファイルをチェックするPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトがMITライセンスであることを示すファイル。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明するメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の挙動や設定（テーマ、プラグインなど）を定義するファイル。
- **`assets/`**: Jekyllサイトで使用される画像（ファビコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン画像ファイル。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用途で使用されるスクリプト。
- **`generated-docs/`**: 生成されたドキュメントや一時ファイルを格納するディレクトリ（内容が空または動的に生成される場合）。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイル。
- **`index.md`**: メインのGitHub Pagesコンテンツ。このプロジェクトによって生成されたリポジトリ一覧が出力されるターゲットファイル。
- **`issue-notes/22.md`**: 開発中の特定の問題（Issue 22）に関するメモや詳細を記録したファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを定義するファイル。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイル。テストの実行方法やオプションを定義。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリのリスト。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonライブラリのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **`ruff.toml`**: Ruff linter/formatterの設定ファイル。コードの品質基準や自動修正ルールを定義。
- **`src/`**: プロジェクトのソースコードを格納するメインディレクトリ。
    - **`__init__.py`**: Pythonパッケージを示すためのファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むパッケージ。
        - **`__init__.py`**: Pythonサブパッケージを示すためのファイル。
        - **`badge_generator.py`**: リポジトリの特性（言語、ステータスなど）に応じたバッジ情報を生成するロジックを実装。
        - **`config.yml`**: プロジェクト概要取得機能やAPI設定など、本システムの技術的パラメータを定義する主要な設定ファイル。
        - **`config_manager.py`**: 設定ファイル（config.ymlなど）の読み込みと管理を行うモジュール。
        - **`date_formatter.py`**: 日付や時刻のフォーマットに関するユーティリティ関数を提供。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、それを処理してMarkdown形式で出力するメインスクリプト。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレート。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理・解析する機能を提供。
        - **`markdown_generator.py`**: 処理されたリポジトリデータからGitHub Pages用のMarkdownコンテンツを作成するコアロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出し、取得する機能。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を整形し、Markdown生成に適した形式に変換する処理を担う。
        - **`seo_template.yml`**: SEOメタデータやJSON-LDのテンプレート設定を管理するファイル。
        - **`statistics_calculator.py`**: リポジトリに関する各種統計情報（スター数、フォーク数など）を計算する機能。
        - **`strings.yml`**: UIに表示される各種メッセージや文言（例: カテゴリ名、説明文のプレフィックスなど）を一元管理するファイル。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（JekyllのLiquidタグなど）を処理する機能。
        - **`url_utils.py`**: URLの構築、検証、変換など、URL処理に関するユーティリティ関数を提供。
- **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストを定義したファイル。
- **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリ。
    - **`conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`test_config.py`**: 設定ファイルの読み込み・管理機能のテスト。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`test_environment.py`**: 開発環境のセットアップや依存関係のテスト。
    - **`test_integration.py`**: システム全体の主要な統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
このプロジェクトは複数のモジュールで構成されており、各ファイルが特定の役割を持つ関数群を内包しています。以下に主要なファイルにおける主要関数の役割を説明します。具体的な引数や戻り値の型はコードベースに依存しますが、その機能はファイル名から推察されます。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: プログラムのエントリーポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力までの一連のフローをオーケストレートします。
- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge_info()`: リポジトリの言語、ステータス（アクティブ、アーカイブ、フォークなど）といった特性に基づいて、表示用のバッジ情報を生成します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config()`: 指定されたパスからYAML設定ファイルを読み込み、設定値をプログラム内で利用可能な形式で提供します。
- **`src/generate_repo_list/date_formatter.py`**:
    - `format_date()`: 日付オブジェクトを受け取り、指定されたフォーマットに従って日付文字列に変換します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_markdown_content()`: 処理されたリポジトリデータのリストを受け取り、Jekyll/GitHub Pagesに適したMarkdown形式の文字列コンテンツを構築します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview()`: 指定されたリポジトリの特定のパス（例: `generated-docs/project-overview.md`）にあるファイルから、プロジェクト概要の3行説明を抽出し、取得します。
- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repository_data()`: GitHub APIから取得した生のリポジトリ情報（JSON形式など）を解析し、Markdown生成や表示に適した、整形されたデータ構造に変換します。
- **`src/generate_repo_list/url_utils.py`**:
    - `build_github_api_url()`: GitHub APIのエンドポイントやパラメータを組み合わせて、APIリクエスト用の完全なURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-05-27 07:32:04 JST
