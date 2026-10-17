Last updated: 2026-10-18

# Project Overview

## プロジェクト概要
- GitHubユーザーのリポジトリ情報を自動で取得し、GitHub PagesサイトにSEO最適化された一覧を公開するシステムです。
- リポジトリの情報はMarkdown形式で自動生成され、検索エンジンやLLM（大規模言語モデル）から発見されやすくなります。
- このシステムにより、個々のリポジトリの可視性を高め、情報共有とアクセシビリティを向上させます。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルを元に、静的なWebサイトを構築・公開するためのGitHub Pagesの基盤技術。**Markdown**: リポジトリ一覧や各リポジトリの概要を記述する軽量マークアップ言語。
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python**: プロジェクトの主要なスクリプト言語。**GitHub API**: GitHubのリポジトリ情報をプログラムから取得するためのインターフェース。**pytest**: Pythonコードのテストを容易にするためのフレームワーク。**ruff**: 高速なPythonコードリンターおよびフォーマッター。
- テスト: **pytest**: Pythonアプリケーションのテストフレームワーク。単体テスト、結合テスト、統合テストを実行するために使用されます。
- ビルドツール: **Pythonスクリプト**: リポジトリ情報からMarkdownファイルを生成するカスタムビルドロジックを実装。**Jekyll**: GitHub Pagesが内部的に利用する静的サイトジェネレーター。
- 言語機能: **Python**: スクリプトの記述と言語処理全般に使用されるプログラミング言語。
- 自動化・CI/CD: **GitHub Actions**: リポジトリ一覧の自動生成プロセスを継続的に実行し、GitHub Pagesへのデプロイを自動化するためのCI/CDプラットフォーム（`.github_automation`ディレクトリから推測）。
- 開発標準: **ruff**: コードの品質を維持し、スタイルガイドに準拠させるための自動整形・静的解析ツール。**.editorconfig**: 異なるエディタやIDE間でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイル。

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
- **`.editorconfig`**: コードエディタ間でインデント、エンコーディングなどの基本的なコードスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するためのディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定を定義します。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、警告するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法などを説明するメインのドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の構成設定を定義するファイルです。
- **`assets/`**: Webサイトで使用するファビコン、アイコンなどの静的アセットを格納するディレクトリです。
    - **`assets/favicon-*.png`**: ブラウザのタブやブックマークなどに表示されるサイトアイコンの画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに特化したスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した「プロジェクト概要」などのドキュメントを一時的に格納したり、参照したりするためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧のメインのMarkdownファイルです。これがGitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定のIssue（開発課題）に関連する詳細なメモや考察を記録したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加、オフライン機能などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツールである`ruff`の設定を定義するファイルです。
- **`src/`**: プロジェクトのソースコードを格納するトップレベルディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージの初期化ファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージの初期化ファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのプロパティ（例：言語、ステータス）に基づいてバッジ（アイコン）を生成するロジックを扱います。
        - **`src/generate_repo_list/config.yml`**: プロジェクトの実行時設定や技術的パラメータ（例：APIキー、タイムアウト、プロジェクト概要取得設定）を定義する設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`やシークレットファイルから設定値を読み込み、管理するクラスや関数を提供します。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの中心となるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownコンテンツを生成します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために構造化データを記述するJSON-LD形式のテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するロジックを扱います。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdown形式のコンテンツを生成するロジックを提供します。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）から、そのリポジトリの概要説明を抽出する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例：CI/CDステータスバッジ）を抽出するロジックです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形する主要なロジックを担います。
        - **`src/generate_repo_list/seo_template.yml`**: サイト全体のSEOメタデータやページ固有のSEO設定を定義するテンプレートファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジックです。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、文言、ラベルなどを一元的に管理する設定ファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用するテンプレートファイル（例：Jinja2テンプレート）を読み込み、データに基づいてレンダリングするロジックを提供します。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能のテストケースを記述したスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するためのディレクトリです。
    - **`tests/conftest.py`**: `pytest`のテスト実行時に共通して使用されるフィクスチャ（テストデータやセットアップ関数）を定義するファイルです。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストケースを記述します。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストケースを記述します。
    - **`tests/test_config.py`**: 設定ファイル (`config.yml`など) の読み込みや管理機能に関するテストケースを記述します。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストケースを記述します。
    - **`tests/test_environment.py`**: 開発・実行環境のセットアップや依存関係に関するテストケースを記述します。
    - **`tests/test_integration.py`**: システム全体の主要なフローに関する統合テストケースを記述します。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストケースを記述します。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストケースを記述します。
    - **`tests/test_readme_badge_extractor.py`**: READMEファイルからのバッジ情報抽出機能のテストケースを記述します。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストケースを記述します。

## 関数詳細説明
このプロジェクトでは、主に`src/generate_repo_list/`内のモジュールに関数が分散されており、それぞれ特定の役割を担っています。具体的な引数や戻り値はコードを参照する必要がありますが、役割に基づいて主要な関数の説明を以下に示します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   **`main()`**:
        -   **役割**: スクリプトのエントリポイントであり、リポジトリ一覧生成の全体的なフローを制御します。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、処理し、最終的なMarkdownファイルを生成する一連のプロセスをオーケストレーションします。
        -   **機能**: 引数解析、設定読み込み、リポジトリデータ取得、データ整形、Markdown生成、ファイル出力。

-   **`src/generate_repo_list/repository_processor.py`**
    -   **`process_repository_data(repo_data)`**:
        -   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、Markdown生成に適した形に整形・加工します。
        -   **引数**: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
        -   **機能**: 必要な情報の抽出、欠損値のハンドリング、アクティブ/アーカイブ/フォークの分類、バッジ情報やプロジェクト概要の追加（他のモジュールと連携）。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **`fetch_project_overview(repo_name, owner_name, config)`**:
        -   **役割**: 指定されたリポジトリから、`generated-docs/project-overview.md`などのファイルに記述されたプロジェクト概要の3行説明を非同期で取得します。
        -   **引数**: `repo_name` (str), `owner_name` (str), `config` (dict): 取得対象のリポジトリ名、所有者名、設定情報。
        -   **機能**: GitHub APIを介して特定ファイルの内容を取得し、設定されたセクションから概要テキストを抽出。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   **`generate_markdown(processed_repos, config)`**:
        -   **役割**: 処理済みリポジトリデータのリストと設定情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
        -   **引数**: `processed_repos` (list): `repository_processor`によって整形されたリポジトリデータのリスト。`config` (dict): 設定情報。
        -   **機能**: テンプレートエンジンを用いて、各リポジトリの情報、バッジ、概要などを盛り込んだMarkdown文字列を構築。

-   **`src/generate_repo_list/badge_generator.py`**
    -   **`generate_badge_html(repo_status)`**:
        -   **役割**: リポジトリのステータス（アクティブ、アーカイブなど）や言語情報に基づいて、表示用のHTMLバッジを生成します。
        -   **引数**: `repo_status` (str), `language` (str, optional): リポジトリのステータスや主要言語。
        -   **機能**: 特定の条件に合致するバッジ（例：アーカイブバッジ、Pythonバッジ）のHTMLスニペットを返す。

-   **`src/generate_repo_list/config_manager.py`**
    -   **`load_config(config_path)` / `load_secrets(secrets_path)`**:
        -   **役割**: `config.yml`や`secrets.toml`などの設定ファイルから、プログラムが必要とする設定値や秘密情報を読み込みます。
        -   **引数**: `config_path` (str) / `secrets_path` (str): 設定ファイルのパス。
        -   **機能**: ファイルを解析し、ディクショナリ形式で設定データを返す。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-18 07:10:15 JST
