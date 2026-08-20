Last updated: 2026-08-21

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEOを意識したリポジトリ一覧Markdownを自動生成します。
- これにより、検索エンジンでのサイトの可視性を高め、各種AIからのリポジトリ参照を促進します。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: GitHub Pages上で動作する静的サイトジェネレーターで、MarkdownファイルをHTMLに変換し、ウェブサイトを構築します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語として、GitHub APIからの情報取得、ファイル生成、データ処理を行います。
    - **GitHub API**: GitHubリポジトリの公開情報をプログラムから取得するために使用されます。
    - **YAML**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）や表示メッセージの管理に利用されます。
    - **TOML**: シークレット情報（例: GitHubトークン）の安全な管理に使用される設定ファイル形式です。
    - **JSON-LD**: 検索エンジン最適化（SEO）のための構造化データを提供するメタデータの形式です。
- テスト:
    - **Pytest**: Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Jekyll**: フロントエンドで記載の通り、MarkdownからHTMLを生成する静的サイトジェネレーターとしての役割も果たします。
- 言語機能:
    - **Python**: 高度なスクリプト記述とデータ処理能力を提供します。
- 自動化・CI/CD:
    - **GitHub Actions (概念的)**: `.github_automation` ディレクトリの存在から、リポジトリ内のファイルの自動チェックなどの自動化プロセスにGitHub Actionsが利用される可能性が示唆されます。ただし、プロジェクト説明ではCI/CDはローカル開発重視とされています。
- 開発標準:
    - **Ruff**: Pythonコードのスタイルチェック（リンター）と自動フォーマットを行う高速なツールです。
    - **requirements.txt / requirements-dev.txt**: プロジェクトの実行時および開発時に必要なPythonパッケージとそのバージョンを管理します。
    - **.editorconfig**: 異なるエディタやIDE間でコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイルです。

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
- **.editorconfig**: 開発チーム全体でコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルに関する自動チェック機能。
        - **README.md**: `check_large_files` 機能の説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        - **scripts/check_large_files.py**: 指定された閾値を超える大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
- **LICENSE**: 本プロジェクトのライセンス（MITライセンス）情報が記述されています。
- **README.md**: プロジェクト全体の目的、機能、使い方、設定方法などを説明する主要なドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトタイトル、テーマ、プラグインなどを定義します。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の様々な解像度ファイル。
- **debug_project_overview.py**: `project_overview_fetcher.py` の機能を個別にデバッグするためのスクリプトです。
- **generated-docs/**: スクリプトによって生成されたドキュメントや一時ファイルを格納するディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイト所有権の確認に使用されるファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって自動生成される、GitHubリポジトリ一覧のMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: プロジェクトの課題や検討事項に関するノートを格納するディレクトリ。
    - **22.md**: 特定の課題（例: Issue #22）の詳細や進捗に関するメモ。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応に利用されるメタデータを定義します。
- **pytest.ini**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの発見方法や実行オプションを定義します。
- **requirements-dev.txt**: 開発環境でのみ必要となるPythonパッケージ（テストツール、リンターなど）とそのバージョンを記述します。
- **requirements.txt**: プロジェクトの実行に最低限必要なPythonパッケージとそのバージョンを記述します。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードの高速リンター/フォーマッターであるRuffの設定ファイルです。コードスタイルや静的解析ルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **generate_repo_list/**: リポジトリ一覧を生成する機能に特化したPythonモジュール群。
        - **badge_generator.py**: リポジトリの言語やスター数などを示すバッジ（アイコン）の生成ロジックを扱います。
        - **config.yml**: リポジトリ一覧生成プロセスの詳細な設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義します。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体で設定値にアクセスするための機能を提供します。
        - **date_formatter.py**: 日付・時刻データを指定された形式で整形するユーティリティ機能を提供します。
        - **generate_repo_list.py**: 本プロジェクトの**メインスクリプト**です。GitHub APIからリポジトリ情報を取得し、その情報を基にMarkdown形式のリポジトリ一覧ファイルを生成します。
        - **json_ld_template.json**: 検索エンジンにサイトコンテンツを理解させるための構造化データ (JSON-LD) のテンプレートファイルです。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つデータを提供するモジュールです。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツ（特にSEOメタデータを含む）を生成するロジックを実装しています。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（`project-overview.md`など）からプロジェクトの3行概要を自動的に取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: 状態、ビルド結果など）を抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に加工・整形する役割を担います。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するテンプレート設定やメタデータ記述を管理するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIに表示される各種メッセージや文言を集中管理するためのファイルです。多言語化や文言変更を容易にします。
        - **template_processor.py**: Markdown生成に使用するテンプレートファイルの読み込み、変数の置換など、テンプレート処理全般を扱います。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能に関するテストスクリプトです。
- **tests/**: プロジェクトのテストコードを格納するディレクトリ。
    - **conftest.py**: Pytestで共通的に利用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator.py` の統合的な動作を確認するためのテストです。
    - **test_check_large_files.py**: `check_large_files.py` スクリプトの機能に関するテストです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストです。
    - **test_date_formatter.py**: 日付整形機能のテストです。
    - **test_environment.py**: プロジェクトの実行環境に関するテストです。
    - **test_integration.py**: プロジェクトの主要な機能が全体として正しく連携するかを確認する統合テストです。
    - **test_markdown_generator.py**: Markdown生成機能のテストです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
このプロジェクトでは、主にPythonスクリプトとして機能がモジュール化されています。提供された情報からは具体的な関数の引数や戻り値の詳細は分析できませんでしたが、各モジュールの役割から推測される主要な機能について説明します。

-   **`generate_repo_list.py`内の主要関数**:
    -   **役割**: プロジェクトの実行エントリポイントとして、リポジトリ一覧生成の全体フローを制御します。
    -   **機能**: CLI引数の解析、GitHub APIからのリポジトリ情報取得、取得したデータの加工、Markdown生成モジュールへの連携、最終的な出力ファイルへの書き込みを行います。
-   **`project_overview_fetcher.py`内の主要関数**:
    -   **役割**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの3行概要を抽出・取得します。
    -   **機能**: GitHub APIを通じてリモートのファイルを読み込み、設定されたセクションタイトルに基づいて概要テキストをパースし、必要に応じてキャッシュを利用して結果を返します。
-   **`markdown_generator.py`内の主要関数**:
    -   **役割**: 整形されたリポジトリ情報や設定情報に基づいて、SEOに適したMarkdown形式の文字列を生成します。
    -   **機能**: テンプレートと動的なデータを組み合わせて、最終的なリポジトリ一覧ページ（`index.md`）のコンテンツを作成します。
-   **`repository_processor.py`内の主要関数**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形します。
    -   **機能**: リポジトリのフィルタリング（アーカイブ、フォークなど）、必要な情報の抽出、統計情報（スター数など）の計算、言語情報の処理、プロジェクト概要の付加などを行います。
-   **`config_manager.py`内の主要関数**:
    -   **役割**: プロジェクト全体で使用される設定ファイル（`config.yml`など）を読み込み、管理します。
    -   **機能**: YAMLファイルから設定値をロードし、プログラムの他の部分から容易にアクセスできるように提供します。
-   **`badge_generator.py`内の主要関数**:
    -   **役割**: リポジトリのプログラミング言語やスター数などの情報に基づき、バッジ画像（またはそのURL）を生成します。
    -   **機能**: 視覚的にリポジトリの情報を表現するためのロジックを提供します。
-   **`date_formatter.py`内の主要関数**:
    -   **役割**: 日付・時刻データを特定のフォーマット文字列に従って整形します。
    -   **機能**: GitHub APIから取得するISO形式の日付などを、ユーザーにとって読みやすい形式に変換します。
-   **`url_utils.py`内の主要関数**:
    -   **役割**: URLの生成、解析、検証など、URLに関連する汎用的なユーティリティ機能を提供します。
    -   **機能**: GitHubリポジトリのURLやAPIエンドポイントの構築を支援します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-08-21 07:08:02 JST
