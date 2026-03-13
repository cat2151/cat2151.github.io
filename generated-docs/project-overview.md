Last updated: 2026-03-14

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定したGitHubユーザーのリポジトリ情報を自動で取得します。
- 取得した情報をもとに、GitHub Pagesサイト（Jekyllベース）向けにSEO最適化されたMarkdown形式のリポジトリ一覧ページを生成します。
- 各リポジトリの概要、バッジ、分類などを自動で表示し、リポジトリの可視性と検索エンジンによるインデックス化を向上させます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤となる静的サイトジェネレーター。MarkdownファイルをHTMLに変換し、ウェブサイトを構築します。
    - **Markdown**: Jekyllサイトのコンテンツ記述に利用される軽量マークアップ言語。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語として、リポジトリ情報の取得、処理、Markdown生成スクリプトに使用されています。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために使用されます。
    - **requests**: HTTPリクエストを送信するためのPythonライブラリ。GitHub APIとの通信に使用されます。
    - **argparse**: Pythonスクリプトにコマンドライン引数解析機能を提供し、柔軟な実行を可能にします。
    - **PyYAML**: YAML形式の設定ファイル（`config.yml`, `strings.yml` など）を読み書きするためのPythonライブラリです。
    - **toml**: TOML形式の設定ファイル（`secrets.toml` など）を扱うためのPythonライブラリです。
- テスト:
    - **pytest**: Python用の強力なテストフレームワーク。プロジェクトの各モジュールの機能検証に使用されます。
- ビルドツール:
    - **Jekyll**: GitHub Pagesの環境でMarkdownコンテンツを静的HTMLサイトとして「ビルド」する役割を担います。
    - **Pythonスクリプト**: 厳密なビルドツールではありませんが、Markdownファイルを「生成」するという意味でコンテンツ生成の中心を担います。
- 言語機能:
    - **Python**: スクリプト開発とデータ処理の中心となるプログラミング言語です。
- 自動化・CI/CD:
    - **GitHub Actions (示唆)**: `.github_automation` ディレクトリの存在から、GitHub上での自動化ワークフロー（例えば、大容量ファイルチェックなど）が利用されている可能性が示唆されます。
- 開発標準:
    - **Ruff**: Pythonコードのスタイルチェック（リンター）と自動フォーマット機能を提供し、コード品質と一貫性を保ちます。

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
-   **`.editorconfig`**: 異なる開発環境（エディタやIDE）間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定ファイルを格納するディレクトリです。
    -   **`check_large_files/README.md`**: `check_large_files` 機能に関する説明が記述されています。
    -   **`check_large_files/check-large-files.toml`**: リポジトリ内の大容量ファイルをチェックするための設定ファイルです。
    -   **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の指定したサイズを超えるファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）が記載されたファイルです。
-   **`README.md`**: プロジェクトの目的、機能、使い方、設定方法、実行コマンドなどを説明する主要なドキュメントファイルです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの動作を制御します。
-   **`assets/`**: ウェブサイトで使用されるファビコンなどの静的リソース（画像ファイルなど）を格納するディレクトリです。
    -   **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるウェブサイトのアイコン画像ファイルです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや個別テストに利用されるPythonスクリプトです。
-   **`generated-docs/`**: プロジェクトによって生成されるドキュメント（例えば、各リポジトリの概要説明など）を格納するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトでは、生成されたリポジトリ一覧がこのファイルに出力されます。
-   **`issue-notes/22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや解決策を記述したMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示情報や動作を定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の設定ファイルで、テスト実行時の振る舞いを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト環境でのみ必要なPythonパッケージの依存関係をリストするファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要なすべてのPythonパッケージの依存関係をリストするファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンターおよびフォーマッターである`Ruff`の設定ファイルで、コードスタイルや静的解析のルールを定義します。
-   **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして識別するためのファイルです。
-   **`src/generate_repo_list/`**: リポジトリ一覧生成機能に関連するPythonモジュール群を格納するパッケージです。
    -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして識別するためのファイルです。
    -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや使用技術を示すバッジのMarkdownを生成する機能を提供します。
    -   **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行時設定（API設定、プロジェクト概要取得設定など）を定義するYAML形式の設定ファイルです。
    -   **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`, `secrets.toml` など）の読み込み、管理、アクセスを担うモジュールです。
    -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の文字列を、人間が読みやすい形式に整形するユーティリティ関数を提供します。
    -   **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成するプロジェクトのメイン実行スクリプトです。
    -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用されるJSON-LD形式の構造化データテンプレートです。
    -   **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報を取得し、処理する機能を提供します。
    -   **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報から、最終的なMarkdown形式のコンテンツを生成するモジュールです。
    -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出する機能を提供します。
    -   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、埋め込まれたバッジの情報を抽出する機能を提供します。
    -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するモジュールです。
    -   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
    -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言（UIテキストなど）を一元管理するYAMLファイルです。
    -   **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用するテンプレート（例: Jinja2）を処理し、動的にデータを埋め込む機能を提供します。
    -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能のテストです。
    -   **`test_date_formatter.py`**: 日付整形ユーティリティのテストです。
    -   **`test_environment.py`**: テスト環境のセットアップや依存関係に関するテストです。
    -   **`test_integration.py`**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テストです。
    -   **`test_markdown_generator.py`**: Markdown生成モジュールのテストです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
    -   **`test_repository_processor.py`**: リポジトリデータ処理モジュールのテストです。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、各ファイルが特定の役割を持つ関数群を提供しています。具体的な引数や戻り値の定義はコード実装に依存しますが、ここでは各モジュールが提供するであろう主要な関数の役割と機能について説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   **`main()`**:
        -   役割: コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成という一連の処理フローを管理・実行します。
        -   機能: プロジェクトの主要なエントリーポイントとして、システムの全体的な動作を制御します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   **`process_repositories(username, limit=None)`**:
        -   役割: GitHub APIを通じて指定されたユーザーのリポジトリ一覧を取得し、必要な情報（説明、言語、スター数など）を抽出・整形して返します。
        -   引数: `username` (文字列): GitHubユーザー名, `limit` (整数, オプション): 処理するリポジトリ数の上限。
        -   機能: APIからの生データを、後のMarkdown生成に適した形式に変換するデータ処理の中心を担います。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   **`generate_markdown(repo_data_list, config)`**:
        -   役割: 処理済みのリポジトリデータリストと設定情報に基づいて、最終的なMarkdown形式のコンテンツを生成します。
        -   引数: `repo_data_list` (リスト): 処理済みリポジトリ情報のリスト, `config` (辞書): Markdown生成に関連する設定。
        -   機能: Jekyllが読み込める形で、SEO最適化されたリポジトリ一覧ページコンテンツを作成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **`fetch_project_overview(repo_name, owner)`**:
        -   役割: 特定のリポジトリ（`repo_name`）の指定されたファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を非同期で取得します。
        -   引数: `repo_name` (文字列): リポジトリ名, `owner` (文字列): リポジトリのオーナー名。
        -   機能: 各リポジトリの特定のドキュメントファイルから、概要説明を自動で読み込むことで、一覧表示に動的な情報を提供します。
-   **`src/generate_repo_list/badge_generator.py`**
    -   **`generate_badge_markdown(status, language)`**:
        -   役割: リポジトリのステータス（例: "active", "archived"）や使用されているプログラミング言語に基づいて、対応するバッジのMarkdownコードを生成します。
        -   引数: `status` (文字列): リポジトリのステータス, `language` (文字列): 主要なプログラミング言語。
        -   機能: リポジトリの視覚的な識別や情報の要約を助けるバッジを動的に作成し、一覧の視認性を高めます。
-   **`src/generate_repo_list/config_manager.py`**
    -   **`load_config(file_path)`**:
        -   役割: 指定されたファイルパスからYAMLまたはTOML形式の設定ファイルを読み込み、辞書オブジェクトとして返します。
        -   引数: `file_path` (文字列): 設定ファイルのパス。
        -   機能: アプリケーション全体で使用されるさまざまな設定（APIキー、動作モードなど）を一元的に管理し、提供します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   **`format_date(iso_date_string)`**:
        -   役割: ISO 8601形式の日付文字列を、人間が読みやすい特定のフォーマットに変換します。
        -   引数: `iso_date_string` (文字列): ISO 8601形式の日付文字列。
        -   機能: リポジトリの最終更新日などをユーザーフレンドリーな形式で表示できるようにします。
-   **`src/generate_repo_list/readme_badge_extractor.py`**
    -   **`extract_badges_from_readme(readme_content)`**:
        -   役割: リポジトリのREADMEファイルのコンテンツから、特定のパターンに合致するバッジのMarkdownまたはURLを抽出します。
        -   引数: `readme_content` (文字列): READMEファイルのテキスト内容。
        -   機能: 各リポジトリのREADMEに埋め込まれたバッジ情報を解析し、一覧ページに表示するために再利用します。
-   **`src/generate_repo_list/statistics_calculator.py`**
    -   **`calculate_repository_stats(repo_data)`**:
        -   役割: 単一リポジトリのデータから、スター数、フォーク数、最終更新日などの統計情報を計算または集計します。
        -   引数: `repo_data` (辞書): 単一リポジトリの詳細データ。
        -   機能: リポジトリの人気の度合いや活動状況を示す数値データを提供します。
-   **`src/generate_repo_list/template_processor.py`**
    -   **`render_template(template_string, data)`**:
        -   役割: 指定されたテンプレート文字列（Jinja2などのテンプレートエンジン形式）と、埋め込むデータ辞書を使用して、最終的なコンテンツをレンダリングします。
        -   引数: `template_string` (文字列): テンプレートの内容, `data` (辞書): テンプレートに埋め込むデータ。
        -   機能: Markdownの構造を定義するテンプレートに動的にデータを挿入し、柔軟なコンテンツ生成を可能にします。
-   **`src/generate_repo_list/url_utils.py`**
    -   **`build_github_api_url(endpoint, username=None, repo_name=None)`**:
        -   役割: GitHub APIのエンドポイントやユーザー名、リポジトリ名などの情報に基づいて、完全なAPIリクエストURLを構築します。
        -   引数: `endpoint` (文字列): APIのエンドポイントパス, `username` (文字列, オプション), `repo_name` (文字列, オプション)。
        -   機能: GitHub APIへのアクセスに必要なURLを簡潔かつ正確に生成し、API通信の効率を高めます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-14 07:10:18 JST
