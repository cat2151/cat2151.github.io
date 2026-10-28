Last updated: 2026-10-29

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジンからのクロールを促進し、各リポジトリの可視性を高めることを目的としています。
- 各リポジトリの概要、バッジ、分類情報を含むSEO最適化されたMarkdownを出力します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、生成されたMarkdownファイルをレンダリングします)、Markdown (生成されるリポジトリ一覧の出力形式であり、JekyllによってHTMLに変換されます)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (Pythonコードのテストフレームワーク。クイックテスト実行に使用されます)、ruff (PythonコードのLinterおよびフォーマッター。コードスタイルの一貫性を保ちます)
- テスト: pytest (Pythonコードの単体テスト、結合テストの実行に用いられます)
- ビルドツール: Python (スクリプト言語として、リポジトリ情報の取得、処理、Markdown生成のメインロジックを実行します)
- 言語機能: Python (メインのスクリプト言語です)、YAML (設定ファイル `config.yml` や `strings.yml`、`seo_template.yml` に使用され、各種パラメータや表示文言を管理します)、TOML (シークレット情報 `secrets.toml` の管理に使用されます)
- 自動化・CI/CD: GitHub API (GitHubからリポジトリ情報を自動的に取得するために使用されます)
- 開発標準: ruff (コードの品質とスタイルを自動的にチェック・修正し、開発標準を維持します)、.editorconfig (複数のエディタやIDEでコードのスタイル設定を統一するためのファイルです)

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
- **.editorconfig**: 異なるエディタやIDE間でコードのインデント、改行コードなどの書式設定を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsや自動化スクリプトに関連するファイルを格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック用のスクリプトと設定を格納します。
        - **README.md**: `check_large_files` ディレクトリの概要と使用方法を説明します。
        - **check-large-files.toml**: 大容量ファイルチェックのルールや閾値を定義する設定ファイルです。
        - **scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを定義します。ビルド生成物や一時ファイルなどが含まれます。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、設定方法、使用方法、クイックテスト手順などを説明する主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **assets/**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（アイコン）の様々なサイズを格納します。
- **debug_project_overview.py**: `project_overview` 機能のデバッグ用スクリプトです。
- **generated-docs/**: 各リポジトリのプロジェクト概要などの生成済みドキュメントを格納するプレースホルダーディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、GitHubリポジトリ一覧のメインMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **issue-notes/22.md**: 特定のIssueに関連するメモやドラフトを格納するファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルです。アプリの表示名、アイコン、表示モードなどを定義します。
- **pytest.ini**: `pytest` の設定ファイルです。テストの検出ルールやオプションなどを指定します。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonパッケージの依存関係を記述したファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係を記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールして良いか、または避けるべきかを指示するファイルです。
- **ruff.toml**: `ruff` の設定ファイルです。コードスタイルのルールやチェック対象などを定義します。
- **src/**: プロジェクトのソースコードを格納するディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示す空ファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックを格納するパッケージです。
        - **__init__.py**: Pythonサブパッケージであることを示す空ファイルです。
        - **badge_generator.py**: リポジトリのバッジ（例: 言語バッジ、ステータスバッジ）を生成するロジックを含みます。
        - **config.yml**: リポジトリ情報取得やプロジェクト概要機能などの技術的パラメータを定義する設定ファイルです。
        - **config_manager.py**: 設定ファイル (`config.yml` など) の読み込み、管理、およびアクセスを提供するモジュールです。
        - **date_formatter.py**: 日付や時刻のフォーマットに関連するユーティリティ関数を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインスクリプトです。
        - **json_ld_template.json**: SEOのためのJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つデータに変換するモジュールです。
        - **markdown_generator.py**: 処理済みのリポジトリデータから、最終的なMarkdownコンテンツを生成するロジックを含みます。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル (`generated-docs/project-overview.md`) から3行のプロジェクト概要を抽出する機能を提供します。
        - **readme_badge_extractor.py**: READMEファイルから既存のバッジ情報を抽出し、解析するモジュールです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリ情報を処理し、必要な形式に整形するロジックを含みます。
        - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータや構造化データのテンプレート設定を定義します。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - **strings.yml**: UIに表示されるメッセージや文言を国際化・一元管理するための設定ファイルです。
        - **template_processor.py**: Markdown生成時に使用するテンプレートファイルの処理やレンダリングを行うモジュールです。
        - **url_utils.py**: URLの構築、検証、解析など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
- **tests/**: プロジェクトのテストコードを格納するディレクトリです。
    - **conftest.py**: `pytest` の設定やテストフィクスチャを定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator` の統合テストです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    - **test_config.py**: 設定ファイル (`config.yml` など) の読み込みと処理のテストです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストです。
    - **test_environment.py**: 実行環境のテストです。
    - **test_integration.py**: プロジェクト全体の主要な機能の統合テストです。
    - **test_markdown_generator.py**: Markdown生成機能のテストです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    - **test_readme_badge_extractor.py**: READMEバッジ抽出機能のテストです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
- **generate_repo_list.py::main()**:
    - 役割: プログラムのエントリポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、処理、Markdown生成、ファイル出力までの一連のプロセスをオーケストレートします。
    - 引数: `username` (str): GitHubユーザー名, `output` (str): 出力ファイル名, `limit` (int, optional): 処理するリポジトリ数の上限 (デフォルト: なし)
    - 戻り値: None (ファイルに結果を書き込みます)
- **repository_processor.py::process_repositories(username, github_token, config)**:
    - 役割: 指定されたGitHubユーザーのリポジトリ情報をGitHub APIから取得し、必要な情報（名前、説明、言語、スター数など）を抽出・整形します。アーカイブ、フォーク、アクティブなどの分類も行います。
    - 引数: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIアクセストークン, `config` (dict): プロジェクトの設定
    - 戻り値: list[dict]: 整形されたリポジトリ情報のリスト
- **project_overview_fetcher.py::fetch_project_overview(repository_info, config)**:
    - 役割: 各リポジトリ内の特定のパス (`generated-docs/project-overview.md`) から「プロジェクト概要」セクションの3行説明を読み込み、抽出します。キャッシュ機能もサポートしています。
    - 引数: `repository_info` (dict): 単一のリポジトリ情報, `config` (dict): プロジェクトの設定
    - 戻り値: str: 抽出された3行のプロジェクト概要（見つからない場合は空文字列）
- **markdown_generator.py::generate_markdown(processed_repositories, config, strings)**:
    - 役割: 処理済みのリポジトリデータのリストを受け取り、Jekyll形式に適したMarkdown文字列を生成します。各リポジトリの詳細、バッジ、分類などを整形して含めます。
    - 引数: `processed_repositories` (list[dict]): 整形されたリポジトリ情報のリスト, `config` (dict): プロジェクトの設定, `strings` (dict): 表示文言
    - 戻り値: str: 生成されたMarkdownコンテンツ
- **badge_generator.py::create_badge_markdown(badge_type, value)**:
    - 役割: 指定されたタイプと値に基づいて、GitHub Pagesサイトで表示するためのバッジのMarkdownコードを生成します。
    - 引数: `badge_type` (str): バッジのカテゴリ (例: "language", "status"), `value` (str): バッジに表示する値
    - 戻り値: str: 生成されたバッジのMarkdown文字列

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-29 07:08:55 JST
