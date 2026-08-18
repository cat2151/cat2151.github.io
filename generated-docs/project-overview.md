Last updated: 2026-08-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- リポジトリ情報からJekyllに対応したMarkdownファイルを生成し、公開用のウェブページを構築します。
- 検索エンジン最適化とLLMからの参照改善を目的とし、リポジトリ一覧と各リポジトリへのリンクを提供します。

## 技術スタック
- フロントエンド: **Jekyll** - GitHub Pagesサイトの構築に利用される静的サイトジェネレーターです。
- 音楽・オーディオ: なし
- 開発ツール: **GitHub API** - GitHubからリポジトリ情報をプログラム的に取得するためのインターフェースです。
- テスト: **pytest** - Pythonで書かれた強力なテストフレームワークで、機能の検証に用いられます。
- ビルドツール: なし (JekyllがGitHub Pagesのビルドを担いますが、本Pythonスクリプト自体はMarkdown生成が主です。)
- 言語機能: **Python** - プロジェクトの主要な開発言語であり、リポジトリ情報の取得・加工・Markdown生成ロジックを実装しています。
- 自動化・CI/CD: **GitHub Pages** - 生成された静的サイトをホスティングするためのサービスです。自動化の文脈で**GitHub Actions**も関与する可能性があります。
- 開発標準: **ruff** - Pythonコードのフォーマットとリンティングを高速に行い、コード品質と一貫性を保ちます。

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化関連スクリプトを格納するディレクトリです。
  - **check_large_files/**: 大容量ファイルチェック機能に関連するファイル群です。
    - **README.md**: `check_large_files` ディレクトリの目的と使用方法を説明します。
    - **check-large-files.toml**: 大容量ファイルチェックの設定を定義します。
    - **scripts/check_large_files.py**: 指定された条件に基づいてリポジトリ内の大容量ファイルをチェックするPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定します。
- **LICENSE**: プロジェクトのライセンス情報 (MITライセンス) を含みます。
- **README.md**: プロジェクトの概要、セットアップ方法、主要機能、実行コマンドなど、プロジェクト全体に関する主要な情報を提供します。
- **_config.yml**: Jekyllサイト全体の共通設定を定義するファイルです。GitHub Pagesの挙動に影響します。
- **assets/**: Webサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
  - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイル群です。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグや単体テストを目的としたスクリプトです。
- **generated-docs/**: スクリプトによって生成されたドキュメントや一時ファイルを格納するためのディレクトリとして使用されます。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのWebサイト所有権確認のための認証ファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。本プロジェクトのスクリプトによってこのファイルにリポジトリ一覧が生成されます。
- **issue-notes/22.md**: 特定の課題に関するメモや詳細情報が記述されたファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するマニフェストファイルで、アプリのホーム画面アイコンや表示モードなどを制御します。
- **pytest.ini**: `pytest`フレームワークの実行設定を定義するファイルです。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリの依存関係をリストアップします。
- **requirements.txt**: プロジェクトが本番環境で実行するために必要なPythonライブラリの依存関係をリストアップします。
- **robots.txt**: 検索エンジンクローラーに対して、どのページをクロールするか、しないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター兼フォーマッターである`ruff`の設定ファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
  - **__init__.py**: Pythonパッケージを初期化するためのファイルです。
  - **generate_repo_list/**: リポジトリ一覧生成に関する具体的なロジックを含むサブパッケージです。
    - **__init__.py**: `generate_repo_list`サブパッケージを初期化するためのファイルです。
    - **badge_generator.py**: リポジトリの言語やステータスなどを示すバッジ（アイコン）を生成するロジックを実装しています。
    - **config.yml**: プロジェクト概要取得機能など、スクリプトの動作を制御する設定値を定義します。
    - **config_manager.py**: YAML設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのユーティリティを提供します。
    - **date_formatter.py**: 日付情報を読みやすい形式に整形するための機能を提供します。
    - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、加工してMarkdown形式の出力ファイルを生成するメインスクリプトです。
    - **json_ld_template.json**: 検索エンジン最適化 (SEO) のため、構造化データを提供するJSON-LD形式のテンプレートです。
    - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、集計するための機能を提供します。
    - **markdown_generator.py**: 処理されたリポジトリデータに基づいて、最終的なMarkdownコンテンツを生成するロジックを実装しています。
    - **project_overview_fetcher.py**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、概要を抽出する機能を提供します。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能を提供します。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に整形・加工する役割を担います。
    - **seo_template.yml**: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義します。
    - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
    - **strings.yml**: UIに表示される各種メッセージや文言を一元的に管理するためのファイルです。
    - **template_processor.py**: Markdown生成時に使用するテンプレートファイルの読み込みと変数置換などの処理を行います。
    - **url_utils.py**: URLの検証や整形など、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能のテストスクリプトです。
- **tests/**: プロジェクトの各種機能に対するテストスクリプトを格納するディレクトリです。
  - **conftest.py**: `pytest`のテスト実行時に使用されるフィクスチャやヘルパー関数など、テスト共通の設定を提供します。
  - **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
  - **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
  - **test_config.py**: 設定ファイルの読み込みと管理に関するテストです。
  - **test_date_formatter.py**: 日付フォーマット機能のテストです。
  - **test_environment.py**: 実行環境の設定や依存関係に関するテストです。
  - **test_integration.py**: プロジェクトの主要なフローや複数のモジュールにまたがる統合テストです。
  - **test_markdown_generator.py**: Markdown生成ロジックのテストです。
  - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
  - **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能のテストです。
  - **test_repository_processor.py**: リポジトリデータの処理機能のテストです。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャや詳細な動作を直接特定することはできませんでしたが、プロジェクトの目的とファイル構造から、主要なモジュールが担う機能について一般的な関数の役割として説明します。

- **generate_repo_list.py** (例: `main`関数または`run_generation`関数)
  - **役割**: プログラムのエントリーポイントとして、GitHub APIからリポジトリ情報を取得し、それを処理して最終的なMarkdown出力を生成する一連のプロセスをオーケストレーションします。
  - **引数**: GitHubユーザー名、出力ファイル名、オプションで処理するリポジトリ数の上限など。
  - **戻り値**: なし（ファイル出力が主な結果）。
  - **機能**: 引数のパース、設定の読み込み、リポジトリデータのフェッチ、加工、Markdown生成、ファイル書き込み。

- **project_overview_fetcher.py** (例: `fetch_project_overview`関数)
  - **役割**: 指定されたGitHubリポジトリ内の特定のパスから、プロジェクトの概要説明テキスト（3行要約など）を非同期的に取得します。
  - **引数**: リポジトリ名、対象ファイルパス、抽出するセクションタイトルなど。
  - **戻り値**: 抽出されたプロジェクト概要の文字列リスト、または取得失敗時には空のリスト/エラー情報。
  - **機能**: GitHub APIを介したファイル内容の取得、Markdownテキストからの特定セクションのパース。

- **markdown_generator.py** (例: `generate_repo_list_markdown`関数)
  - **役割**: 処理済みのリポジトリデータと設定に基づいて、GitHub Pages用のリポジトリ一覧を記述したMarkdown文字列を生成します。
  - **引数**: 処理済みリポジトリ情報のリスト、設定オブジェクトなど。
  - **戻り値**: 生成されたMarkdown形式の文字列。
  - **機能**: テンプレートへのデータ適用、バッジ情報や統計情報の埋め込み、Markdownフォーマットの調整。

- **repository_processor.py** (例: `process_repository_data`関数)
  - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を受け取り、アプリケーション内で利用しやすい構造化されたデータ形式に変換・加工します。
  - **引数**: 生のリポジトリデータオブジェクト、設定など。
  - **戻り値**: 整理・加工されたリポジトリ情報の辞書またはオブジェクト。
  - **機能**: 不要な情報のフィルタリング、日付の変換、URLの整形、統計情報の集計（必要に応じて）。

- **badge_generator.py** (例: `create_language_badges`関数)
  - **役割**: リポジトリの主要言語やその他の属性に基づいて、表示用のバッジ（例: Shield.io形式のMarkdown）を生成します。
  - **引数**: リポジトリの言語情報、スター数などの統計情報。
  - **戻り値**: バッジを示すMarkdown文字列のリスト。
  - **機能**: 渡されたデータから適切なバッジURLを構築し、Markdown形式で出力。

- **date_formatter.py** (例: `format_iso_date_to_display`関数)
  - **役割**: ISO 8601形式などの日付文字列を受け取り、人間が読みやすい形式に整形して返します。
  - **引数**: 日付文字列。
  - **戻り値**: 整形された日付文字列。
  - **機能**: 日付オブジェクトへの変換、指定されたフォーマットでの文字列出力。

- **config_manager.py** (例: `load_configuration`関数)
  - **役割**: 設定ファイル（`config.yml`や`strings.yml`など）を読み込み、プログラム全体で利用可能な設定オブジェクトを提供します。
  - **引数**: 設定ファイルのパス。
  - **戻り値**: 設定値を含む辞書またはオブジェクト。
  - **機能**: YAMLファイルのパース、デフォルト値の設定、設定値のバリデーション。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-08-19 07:05:57 JST
