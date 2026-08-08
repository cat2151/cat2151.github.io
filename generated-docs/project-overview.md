Last updated: 2026-08-09

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定されたGitHubユーザーのリポジトリ情報を自動で収集・整理します。
- 収集した情報に基づき、JekyllベースのGitHub Pagesサイト向けにSEOを考慮したリポジトリ一覧のMarkdownファイルを生成します。
- 各リポジトリの概要、バッジ、分類などを自動で組み込み、サイトの検索エンジン最適化と可読性向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレーターで、生成されたMarkdownからウェブページを構築します), Markdown (リポジトリ一覧のコンテンツを生成するマークアップ言語), HTML/CSS (Jekyllが最終的に出力するウェブページの基盤技術)
- 音楽・オーディオ: (このプロジェクトでは音楽・オーディオ関連技術は使用されていません)
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成の中核を担います), Git/GitHub (リポジトリ管理とGitHub APIからの情報取得に利用), pytest (Pythonコードのテストフレームワーク), Ruff (コードの整形と静的解析を行うリンター兼フォーマッター)
- テスト: pytest (Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです)
- ビルドツール: Pythonスクリプト (GitHub APIからデータを取得し、Markdownファイルを自動生成します), Jekyll (生成されたMarkdownファイルを用いて静的ウェブサイトを構築します)
- 言語機能: Python (汎用プログラミング言語として、データ処理、API通信、ファイル操作などに活用されています)
- 自動化・CI/CD: Pythonスクリプト (リポジトリ情報の取得とMarkdown生成プロセスを自動化します), GitHub Actions (他のリポジトリのGitHub Actionsワークフロー管理のためのMarkdown生成を支援する文脈で言及されています)
- 開発標準: Ruff (コードスタイルの一貫性を保ち、品質を向上させるための設定), .editorconfig (異なるエディタやIDE間でコーディングスタイルを統一するための設定ファイル)

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
- **`.editorconfig`**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: 大容量ファイルがないかチェックするための自動化スクリプトや設定が含まれるディレクトリです。
    - **`README.md`**: `check_large_files` サブプロジェクトの説明ドキュメントです。
    - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイルです。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクト全体の目的、機能、セットアップ方法、使用方法など、主要な情報を提供するドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイルで、サイトのタイトル、テーマ、プラグイン、生成されるページのパスなどを定義します。
- **`assets/`**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得・生成されたドキュメントや概要ファイルが一時的に格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイルです。
- **`index.md`**: このプロジェクトによって自動生成される、GitHub Pagesサイトのリポジトリ一覧のメインページとなるMarkdownファイルです。
- **`issue-notes/22.md`**: 特定のIssueに関連するメモや詳細情報が記載されたファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリのホーム画面アイコン、表示モード、起動URLなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法や検出ルールなどを指定します。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージの依存関係を定義するファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージの依存関係を定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードの整形と静的解析を行うRuffの設定ファイルです。コードの品質とスタイルを維持するためのルールを定義します。
- **`src/generate_repo_list/`**: リポジトリ一覧を生成するメインのPythonコードが含まれるディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すファイルです。
    - **`badge_generator.py`**: リポジトリの言語やステータスを示すバッジ（画像やマークダウン形式）を生成する機能を提供します。
    - **`config.yml`**: プロジェクト概要取得機能などの、技術的な設定パラメータを定義するYAMLファイルです。
    - **`config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、プロジェクト全体で利用可能な設定を管理するモジュールです。
    - **`date_formatter.py`**: GitHub APIから取得した日付やタイムスタンプを、人間が読みやすい形式に整形するユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: このプロジェクトのメイン実行スクリプトです。GitHub APIと連携し、リポジトリ情報を取得・処理し、最終的なMarkdownファイルを生成するオーケストレーションを行います。
    - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレートを定義します。
    - **`language_info.py`**: 各プログラミング言語に関する情報（例：表示名、色コード）を管理し、バッジ生成や表示に利用します。
    - **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成するモジュールです。
    - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルから、指定されたセクション（例：「プロジェクト概要」）の3行説明を自動で抽出する機能を提供します。
    - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報（例：shields.ioバッジ）を抽出する機能を提供します。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（スター数、最終更新日、言語、バッジなど）に加工・整形する役割を担います。
    - **`seo_template.yml`**: 検索エンジン最適化 (SEO) のためのメタデータテンプレートを定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリの統計情報（例：スター数、フォーク数、最終更新からの日数など）を計算・集計する機能を提供します。
    - **`strings.yml`**: プロジェクト内で使用される表示メッセージや文言を管理し、国際化や文言の一元管理を容易にするYAMLファイルです。
    - **`template_processor.py`**: Jekyllテンプレートやその他のマークアップテンプレートを処理し、動的にコンテンツを埋め込む機能を提供します。
    - **`url_utils.py`**: URLの構築、解析、エンコード/デコードなど、URL関連のユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールのテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト設定やフィクスチャを定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストコードです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストコードです。
    - **`test_config.py`**: 設定ファイル読み込み・管理機能のテストコードです。
    - **`test_date_formatter.py`**: 日付整形機能のテストコードです。
    - **`test_environment.py`**: 実行環境に関するテストコードです。
    - **`test_integration.py`**: プロジェクト全体の統合テストコードです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストコードです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストコードです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストコードです。

## 関数詳細説明
このプロジェクトはPythonモジュールとして構成されており、各ファイルが特定の役割を持つ関数群を提供します。以下に主要なモジュールとその中核となる機能（関数群）の概要を説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **役割**: プログラムのエントリーポイントとして、リポジトリ一覧生成プロセスの全体をオーケストレーションします。
    -   **主要機能**:
        -   `main()`: コマンドライン引数を解析し、設定を読み込み、GitHub APIからのリポジトリ取得、データ処理、Markdown生成を順序立てて実行します。
        -   `fetch_repositories(username, limit=None)`: 指定されたGitHubユーザーのリポジトリ情報をGitHub API経由で取得し、生のJSONデータを返します。
        -   `generate_output_markdown(processed_repos, output_file)`: 処理済みのリポジトリデータを受け取り、最終的なMarkdownコンテンツを生成し、指定されたファイルに書き出します。

-   **`src/generate_repo_list/repository_processor.py`**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形します。
    -   **主要機能**:
        -   `process_repository(repo_data, config, strings)`: 個々のリポジトリの生データを受け取り、スター数、最終更新日、主要言語、プロジェクト概要、バッジ情報などを抽出し、整形された辞書形式のデータを返します。
        -   `get_repository_languages(repo_data)`: リポジトリの主要言語情報を抽出し、整形します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **役割**: 各リポジトリ内の特定のファイルからプロジェクト概要の3行説明を抽出します。
    -   **主要機能**:
        -   `get_project_overview(repo_url, target_file, section_title, config)`: 指定されたリポジトリのURLとファイルパスから、Markdown内の特定のセクション（例: "プロジェクト概要"）に記載された3行の説明をフェッチします。

-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **役割**: 処理済みのリポジトリデータとテンプレートを用いて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   **主要機能**:
        -   `create_repo_list_markdown(processed_repos, config, strings)`: 処理済みのリポジトリデータのリストと、設定情報、文言情報を受け取り、Jekyll形式に準拠した完全なMarkdown文字列を生成します。
        -   `generate_repository_section(repo_info, strings)`: 個々のリポジトリ情報から、そのリポジトリ表示用のMarkdownセクションを生成します。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   **役割**: リポジトリの属性（言語、ステータスなど）を示すバッジのHTMLまたはMarkdownコードを生成します。
    -   **主要機能**:
        -   `generate_language_badge(language, language_color)`: 指定された言語と色に基づいて、言語バッジのHTML/Markdownを生成します。
        -   `generate_status_badge(is_archived, is_fork, strings)`: リポジトリがアーカイブされているか、フォークであるかに応じて、ステータスバッジを生成します。

-   **`src/generate_repo_list/config_manager.py`**:
    -   **役割**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）の読み込みと管理を行います。
    -   **主要機能**:
        -   `load_config(config_path)`: 指定されたパスからYAML設定ファイルを読み込み、辞書として返します。
        -   `load_strings(strings_path)`: 表示メッセージなどを定義したYAMLファイルを読み込みます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層ツリーは分析できませんでした。

---
Generated at: 2026-08-09 07:08:19 JST
