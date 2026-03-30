Last updated: 2026-03-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を自動取得するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンからの参照性やLLMによるリポジトリ参照の精度向上を目指し、各リポジトリの概要自動取得機能などを提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの静的サイトジェネレーターとして利用), **Markdown** (生成されるコンテンツの形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **pytest** (Pythonテストフレームワーク), **ruff** (Pythonリンター/フォーマッター), **toml** (設定ファイル形式), **YAML** (設定ファイル形式)
- テスト: **pytest** (ユニットテスト、統合テストの実行)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報の取得、処理、Markdown生成の中心), **Jekyll** (GitHub Pagesによるサイトの最終的なビルド)
- 言語機能: **Python** (スクリプトの主要言語)
- 自動化・CI/CD: **GitHub Actions** (プロジェクトの意図として、リポジトリ更新時の自動生成フローでの利用が想定されます)
- 開発標準: **ruff** (コードスタイルの自動修正・チェック), **.editorconfig** (エディタ間でのコードスタイルの一貫性維持)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどと連携して自動化処理を行うスクリプト群を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルをチェックするためのサブディレクトリ。
        - **README.md**: `check_large_files`機能に関する説明。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイル。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイル。
- **README.md**: プロジェクトの概要、目的、機能、使用方法、設定、テスト方法などを記述したプロジェクトのメイン説明書。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの設定に関連します。
- **assets/**: GitHub Pagesサイトで利用される画像やアイコンなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像。
- **debug_project_overview.py**: `project_overview`機能の動作確認やデバッグのために一時的に使用されるスクリプト。
- **generated-docs/**: 他のリポジトリから取得された`project-overview.md`などのドキュメントや、生成されたドキュメントの出力先を模倣するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによってリポジトリ一覧が生成され、GitHub Pagesサイトのトップページとして機能するMarkdownファイル。
- **issue-notes/**: 特定のGitHub Issueに関する詳細なメモや考察を格納するディレクトリ。
    - **22.md**: Issue番号22に関連するメモや議論を記録したMarkdownファイル。
- **manifest.json**: PWA（Progressive Web App）機能を提供するためのWebアプリマニフェストファイル。アプリの表示情報などを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの発見方法や実行オプションなどを定義します。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイル。
- **ruff.toml**: Pythonの高速リンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや静的解析ルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成システムの核心となるPythonモジュール群を格納するディレクトリ。
        - **__init__.py**: Pythonパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの技術スタックやステータスを示すバッジ（アイコン）画像を生成するためのロジックを含む。
        - **config.yml**: `generate_repo_list.py`スクリプトの実行に関する各種設定（例: project_overview機能の有効/無効、タイムアウト時間など）を定義するファイル。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、設定値を提供する機能。
        - **date_formatter.py**: GitHub APIから取得した日付情報をユーザーフレンドリーな形式に整形する機能。
        - **generate_repo_list.py**: **このプロジェクトのメインスクリプト**。GitHub APIからリポジトリ情報を取得し、各処理モジュールを呼び出して最終的なMarkdownファイルを生成する。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレート。
        - **language_info.py**: リポジトリの主要言語情報などを処理し、表示に適した形に整形する機能。
        - **markdown_generator.py**: 処理されたリポジトリデータから、最終的なMarkdownコンテンツ（リポジトリ一覧）を構築する機能。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動的に抽出し、取得する機能。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を解析・抽出する機能。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（スター数、フォーク数、最終更新日など）を抽出・整形する機能。
        - **seo_template.yml**: SEO関連のメタデータや構造化データを生成するためのテンプレート設定ファイル。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算し、Markdown出力に含める準備をする機能。
        - **strings.yml**: UIメッセージ、キャプション、説明文など、スクリプトが出力する様々なテキスト文字列を一元的に管理するファイル。
        - **template_processor.py**: Markdown生成時に使用するテンプレートファイル（またはテンプレート文字列）を読み込み、データに基づいて埋め込み処理を行う機能。
        - **url_utils.py**: URLの生成、解析、バリデーションなど、URLに関連するユーティリティ関数を提供する。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールのテストコード。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャ（テスト実行前に必要なセットアップ）やヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: `badge_generator`機能の統合テスト。
    - **test_check_large_files.py**: `check_large_files.py`スクリプトのテスト。
    - **test_config.py**: 設定ファイル（`config.yml`, `strings.yml`など）の読み込みと解析に関するテスト。
    - **test_date_formatter.py**: `date_formatter`モジュールのテスト。
    - **test_environment.py**: テスト環境のセットアップや依存関係の確認に関するテスト。
    - **test_integration.py**: `generate_repo_list`モジュールの主要な機能フロー全体を検証する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator`モジュールのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor`モジュールのテスト。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**:
    - `main()`: このスクリプトのエントリポイント。コマンドライン引数をパースし、設定を読み込み、GitHub APIからリポジトリ情報を取得し、加工してMarkdownとして出力する一連の処理を orchestrate します。
    - `fetch_repositories(username, token, limit)`: 指定されたGitHubユーザー名とトークンを使用して、GitHub APIからリポジトリ一覧を取得します。`limit`オプションで取得数を制限できます。
    - `process_repository(repo_data, config, token, cache)`: 単一のリポジトリデータを受け取り、`project_overview_fetcher`などを用いて追加情報を取得・加工し、Markdown生成に適した形式に整形します。
    - `generate_markdown(processed_repos, strings_config, seo_config)`: 処理済みのリポジトリデータのリストと設定情報をもとに、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- **src/generate_repo_list/project_overview_fetcher.py**:
    - `fetch_project_overview(repo_full_name, config, token, enable_cache, cache)`: 指定されたリポジトリのフルネーム (`owner/repo`) と設定情報をもとに、対象リポジトリ内の`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出し、返します。APIリクエストのキャッシュ機能もサポートします。
- **src/generate_repo_list/markdown_generator.py**:
    - `generate_repository_entry(repo_info, strings_config)`: 単一の整形済みリポジトリ情報を受け取り、そのリポジトリに関する個別のMarkdownセクション（タイトル、説明、バッジなど）を生成します。
    - `generate_full_markdown(repo_list, strings_config, seo_config)`: 複数のリポジトリエントリーとSEO設定を含む、サイト全体のMarkdownコンテンツ（HTMLヘッダーやフッター、JSON-LDなどを含む）を生成します。
- **src/generate_repo_list/config_manager.py**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書形式で返します。
    - `load_strings(strings_path)`: 指定されたパスからYAML形式の文字列定義ファイルを読み込み、テキスト辞書として返します。
- **src/generate_repo_list/repository_processor.py**:
    - `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリ辞書を受け取り、必要なキーだけを抽出し、日付の整形やデフォルト値の設定などを行い、簡潔で使いやすい辞書形式に整形します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-31 07:14:13 JST
