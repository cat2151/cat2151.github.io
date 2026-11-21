Last updated: 2026-11-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報をもとに、JekyllベースのGitHub Pagesサイト向けMarkdownファイルを生成します。
- これにより、GitHub PagesのSEOを強化し、検索エンジンやLLMからの参照可能性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll, GitHub Pages** (Markdownファイルが生成され、JekyllによってGitHub Pagesサイトとして公開されます)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語として使用され、リポジトリ情報の取得・処理・Markdown生成ロジックを実装しています。
    - **GitHub API**: GitHubからリポジトリ情報をプログラムで取得するために利用されます。
    - **PyYAML**: 設定ファイル(`config.yml`, `strings.yml`, `seo_template.yml`)の読み書きに使用されます。
    - **requests**: HTTP通信を行うためのライブラリで、GitHub APIへのリクエストに使用されます。
    - **`ruff`**: Pythonコードのスタイルチェックとフォーマットを自動化するためのツールです。
    - **`pytest`**: プロジェクトのテストを記述・実行するためのフレームワークです。
- テスト: **`pytest`** (Pythonアプリケーションのテストコードを実行するために使用されます。)
- ビルドツール: (このプロジェクト自体は特定のビルドツールを使用せず、Pythonスクリプトが直接Markdownファイルを生成します。生成されたMarkdownはJekyllによって処理されます。)
- 言語機能: **Python** (データ処理、ファイルI/O、文字列操作など、Pythonの豊富な標準ライブラリと構文を活用しています。)
- 自動化・CI/CD: (ローカル開発が重視されていますが、将来的にはGitHub ActionsなどのCI/CD環境での利用も想定され、自動的なリポジトリ一覧生成フローを構築可能です。)
- 開発標準: **`ruff`** (コードの品質と統一性を保つためのリンターおよびフォーマッターとして活用されます。)

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
- **`.editorconfig`**: さまざまなエディタ間で一貫したコーディングスタイルを定義する設定ファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトに関連するファイルを格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックする自動化スクリプト群です。
        - **`README.md`**: `check_large_files`機能に関する説明です。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定ファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを定義するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定など、概要情報を提供します。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesの振る舞いを定義します。
- **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテスト実行に特化したスクリプトです。
- **`generated-docs/`**: 各リポジトリのプロジェクト概要ファイル（`project-overview.md`）が格納されることを想定しているディレクトリです。このプロジェクトはここから概要を読み取ります。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のためのHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのメインページとなるMarkdownファイルです。このプロジェクトによってリポジトリ一覧が生成され、ここに出力されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
- **`manifest.json`**: ウェブサイトをプログレッシブウェブアプリ（PWA）として動作させるための設定ファイルです。
- **`pytest.ini`**: `pytest`フレームワークの全体的な設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリのリストです。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonライブラリのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールするか、しないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルと品質を管理する`ruff`ツールの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の中心となるPythonモジュール群です。
        - **`__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして識別します。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを提供します。
        - **`config.yml`**: プロジェクト概要取得機能などの、スクリプトの技術的なパラメータを設定するファイルです。
        - **`config_manager.py`**: YAML設定ファイルを読み込み、管理するためのユーティリティを提供します。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するための機能を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式で一覧ファイルを生成するメインスクリプトです。
        - **`json_ld_template.json`**: SEO目的で使用されるJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理・整形する機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要を自動取得する機能を提供します。
        - **`readme_badge_extractor.py`**: READMEファイルから既存のバッジ情報を抽出するロジックを実装しています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を、Markdown生成に適した形式に加工・処理する役割を担います。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するテンプレートや設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元管理するためのファイルです。
        - **`template_processor.py`**: Markdown生成のためのテンプレート処理を行うロジックを実装しています。
        - **`url_utils.py`**: URLの生成や解析など、URLに関連するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュール（プロジェクト概要取得機能）の単体テストコードです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: `pytest`のテストフィクスチャやフックを定義するためのファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定管理機能のテストです。
    - **`test_date_formatter.py`**: 日付整形機能のテストです。
    - **`test_environment.py`**: 実行環境に関するテストです。
    - **`test_integration.py`**: 主要なコンポーネント間の統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルが特定の役割を持つ関数やクラスを提供しています。プロジェクト情報に具体的な関数名や引数、戻り値の形式は記載されていませんが、各モジュールの機能から想定される主要な関数について説明します。

-   **`generate_repo_list.py`内のメイン実行関数（例: `main()`関数、またはスクリプト直下の処理）**
    -   **役割**: プロジェクトのエントリポイントとして機能し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、そして最終的なファイル出力の一連の流れを orchestrate します。
    -   **引数**: `username` (str, GitHubユーザー名), `output_file` (str, 出力するMarkdownファイル名), `limit` (int, オプション、処理するリポジトリ数の上限)。
    -   **戻り値**: なし（指定された出力ファイルにMarkdownコンテンツを書き込みます）。

-   **`repository_processor.py`内のリポジトリ情報取得・処理関数（例: `fetch_and_process_repositories()`）**
    -   **役割**: 指定されたGitHubユーザーのリポジトリリストをGitHub APIを通じて取得し、JekyllのMarkdown生成に適した形式に加工します。これには、リポジトリ名、説明、スター数、言語情報、最終更新日などの抽出が含まれます。
    -   **引数**: `username` (str, GitHubユーザー名), `github_token` (str, GitHub API認証トークン)。
    -   **戻り値**: `list` (加工されたリポジトリ情報の辞書リスト)。

-   **`project_overview_fetcher.py`内のプロジェクト概要取得関数（例: `fetch_project_overview_from_repo()`）**
    -   **役割**: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）からプロジェクトの3行概要を抽出し、取得します。ネットワークリクエストやキャッシュ処理を含みます。
    -   **引数**: `repo_owner` (str), `repo_name` (str), `file_path` (str, 概要ファイルへのパス), `config` (dict, 設定オブジェクト)。
    -   **戻り値**: `str` (抽出されたプロジェクト概要テキスト、または空文字列)。

-   **`markdown_generator.py`内のMarkdown生成関数（例: `generate_repository_markdown()`）**
    -   **役割**: 加工されたリポジトリ情報と取得されたプロジェクト概要をもとに、個々のリポジトリ項目や全体のリポジトリ一覧を含むMarkdown形式の文字列を生成します。
    -   **引数**: `repository_data` (dict, 単一のリポジトリ情報), `project_overview` (str, 取得されたプロジェクト概要), `template_processor` (オブジェクト, テンプレート処理ユーティリティ)。
    -   **戻り値**: `str` (生成されたMarkdownコンテンツの一部)。

-   **`badge_generator.py`内のバッジ生成関数（例: `create_badge_markdown()`）**
    -   **役割**: リポジトリの言語や状態（アクティブ、アーカイブ、フォーク）に基づいて、Markdown形式のバッジ文字列を生成します。
    -   **引数**: `language` (str, プログラミング言語), `is_archived` (bool), `is_fork` (bool)。
    -   **戻り値**: `str` (生成されたバッジのMarkdown文字列)。

-   **`config_manager.py`内の設定読み込み関数（例: `load_config()`）**
    -   **役割**: YAML形式の設定ファイル（例: `config.yml`, `strings.yml`）を読み込み、Pythonの辞書オブジェクトとして提供します。
    -   **引数**: `file_path` (str, 設定ファイルへのパス)。
    -   **戻り値**: `dict` (読み込まれた設定データ)。

## 関数呼び出し階層ツリー
```

---
Generated at: 2026-11-22 07:07:07 JST
