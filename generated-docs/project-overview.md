Last updated: 2026-01-10

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動で取得します。
- 取得した情報から、GitHub Pages向けのSEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- 生成されたコンテンツは、検索エンジンのクロールを促進し、各リポジトリの可視性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの静的コンテンツ生成フレームワーク)、**Markdown** (コンテンツ記述形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (メインスクリプト言語、データ処理)、**GitHub API** (リポジトリ情報の取得)、**TOML** (シークレット管理)、**YAML** (設定ファイル、SEOテンプレート、文字列管理)
- テスト: **pytest** (Python用テストフレームワーク)
- ビルドツール: **Python** (スクリプト実行によるMarkdownコンテンツ生成)、**Jekyll** (GitHub Pagesによるサイト最終ビルド)
- 言語機能: **Python** (オブジェクト指向プログラミング、標準ライブラリを活用したデータ処理、ネットワーク通信など)
- 自動化・CI/CD: 本プロジェクトはCI/CDを必須とはしていませんが、GitHub Actionsと連携して自動生成プロセスを定期的に実行することが可能です。
- 開発標準: **ruff** (Pythonコードのスタイルチェックと自動修正ツール)

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 2.md
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
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されており、ソフトウェアの利用条件を定めます。
- **`README.md`**: プロジェクトの概要、目的、設定方法、使用方法、開発者向けのヒントなどを説明する主要なドキュメントです。
- **`_config.yml`**: JekyllによってGitHub Pagesサイトがビルドされる際の設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどを制御します。
- **`assets/`**: faviconなどのウェブサイトで使用される静的リソース（画像ファイルなど）を格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたドキュメント（例: project-overview.md）が格納されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のためのファイルです。
- **`index.md`**: メインスクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧を含むMarkdownファイルです。このファイルがサイトのトップページとして表示されます。
- **`issue-notes/`**: プロジェクト開発中の課題や検討事項、メモなどをMarkdown形式で記録するためのディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるマニフェストファイルです。ウェブアプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonパッケージの一覧を定義するファイルです。
- **`requirements.txt`**: プロジェクトの実行（本番環境）に必要となるPythonパッケージの一覧を定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックと自動修正ツール`ruff`の設定ファイルです。コード品質を統一するためのルールを定義します。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdown形式のリポジトリ一覧を生成するメインのPythonスクリプトです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（アクティブ、アーカイブなど）に応じたバッジの生成や表示に関連するロジックを管理するモジュールです。
- **`src/generate_repo_list/config.yml`**: `generate_repo_list.py`スクリプトの動作を制御するための技術的なパラメータ（例：プロジェクト概要取得機能の有効/無効、タイムアウト設定）を定義するファイルです。
- **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）やシークレットファイル（`secrets.toml`）を読み込み、管理するためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: GitHub APIから取得される日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供するモジュールです。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データであるJSON-LD形式のテンプレートを定義するファイルです。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの言語情報を処理し、表示に適した形式に変換するモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックをカプセル化したモジュールです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリに存在する `generated-docs/project-overview.md` ファイルから、プロジェクト概要の3行説明を自動取得する機能を提供するモジュールです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に必要な情報（名前、説明、URLなど）を抽出し整形するモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや表示設定を含むテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計するためのモジュールです。
- **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示される各種メッセージや文言、ラベルなどを一元的に管理するためのファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用するテンプレートファイルの読み込みや、データを用いたレンダリング処理を行うモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、整形など、URLに関連するユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能に関するテストを記述したスクリプトです。
- **`tests/`**: プロジェクト全体のユニットテストや統合テストを格納するディレクトリです。

## 関数詳細説明
このプロジェクトでは、以下の主要な関数群が連携してリポジトリ一覧の生成を行います。

- **`main()` (src/generate_repo_list/generate_repo_list.py)**:
    - **役割**: プログラムのエントリポイントであり、リポジトリ一覧生成プロセスの全体を orchestrate します。
    - **機能**: コマンドライン引数の解析、設定とシークレットの読み込み、GitHub APIからのリポジトリ情報取得、リポジトリデータの処理、Markdownコンテンツの生成、そして最終的なファイルへの出力を行います。
    - **引数**: なし（コマンドライン引数は内部で解析）。
    - **戻り値**: なし。

- **`parse_arguments()` (src/generate_repo_list/generate_repo_list.py)**:
    - **役割**: コマンドライン引数を解析し、必要な情報を取得します。
    - **機能**: `--username`、`--output`、`--limit` などのオプションを解釈し、プログラムに渡します。
    - **引数**: なし。
    - **戻り値**: 解析された引数を含むオブジェクト。

- **`fetch_repositories(username, token)` (src/generate_repo_list/repository_processor.py 内に相当)**:
    - **役割**: GitHub APIを介して、指定されたユーザーの公開リポジトリ情報を取得します。
    - **機能**: 認証トークンを使用してGitHub APIにリクエストを送信し、リポジトリデータのリストを取得します。
    - **引数**: `username` (str): GitHubユーザー名、`token` (str): GitHub APIアクセストークン。
    - **戻り値**: リポジトリ情報のリスト（辞書形式）。

- **`process_repository_data(repo_data, config)` (src/generate_repo_list/repository_processor.py 内に相当)**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換します。
    - **機能**: 各リポジトリから必要な情報（名前、説明、URL、最終更新日など）を抽出し、特定のルールに基づいて分類・加工します。必要に応じてプロジェクト概要の取得も連携します。
    - **引数**: `repo_data` (dict): GitHub APIからのリポジトリ生データ、`config` (dict): プロジェクト設定。
    - **戻り値**: 処理済みのリポジトリ情報オブジェクトのリスト。

- **`fetch_project_overview(repo_url, config)` (src/generate_repo_list/project_overview_fetcher.py)**:
    - **役割**: 指定されたリポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出します。
    - **機能**: リポジトリのURLを使用して、対象ファイルを読み込み、設定されたセクションタイトルに基づいて概要テキストをパースします。
    - **引数**: `repo_url` (str): リポジトリのURL、`config` (dict): プロジェクト概要取得に関する設定。
    - **戻り値**: 抽出された3行のプロジェクト概要（リスト形式）、または空のリスト。

- **`generate_markdown(repositories, config)` (src/generate_repo_list/markdown_generator.py)**:
    - **役割**: 処理済みのリポジトリ情報リストと設定に基づき、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成します。
    - **機能**: 各リポジトリの情報、バッジ、概要などを整形し、テンプレートを使用してMarkdown文字列を構築します。
    - **引数**: `repositories` (list): 処理済みのリポジトリ情報オブジェクトのリスト、`config` (dict): プロジェクト設定。
    - **戻り値**: 生成されたMarkdown文字列。

- **`load_config(config_path)` (src/generate_repo_list/config_manager.py)**:
    - **役割**: 指定されたパスからYAML形式の設定ファイルを読み込みます。
    - **機能**: ファイルをパースし、設定値を辞書形式で提供します。
    - **引数**: `config_path` (str): 設定ファイルのパス。
    - **戻り値**: 設定値を含む辞書。

- **`load_secrets(secrets_path)` (src/generate_repo_list/config_manager.py)**:
    - **役割**: 指定されたパスからTOML形式のシークレットファイル（例: GitHubトークン）を読み込みます。
    - **機能**: ファイルをパースし、シークレット値を安全に提供します。
    - **引数**: `secrets_path` (str): シークレットファイルのパス。
    - **戻り値**: シークレット値を含む辞書。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-01-10 07:07:02 JST
