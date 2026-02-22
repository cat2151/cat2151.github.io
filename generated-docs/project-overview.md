Last updated: 2026-02-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用して、GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- リポジトリ情報からSEOに最適化されたMarkdownファイルを生成し、サイトの検索エンジンでの発見性を高めます。
- 各リポジトリの概要も自動取得して表示することで、LLMによる参照精度向上も期待されます。

## 技術スタック
- フロントエンド: Jekyll / GitHub Pages: 生成されたMarkdownファイルをホスティングし、Webサイトとして公開するための基盤。
- 開発ツール:
    - Pytest: Pythonアプリケーションのテストフレームワーク。単体テストや結合テストを実行します。
    - Ruff: Pythonの高速なLinterおよびFormatter。コードの品質維持とスタイル統一に貢献します。
    - TOML: 設定ファイルの形式。GitHubトークンなどの機密情報を安全に管理するために使用されます。
- テスト: Pytest: プロジェクトのコードが期待通りに動作するかを検証するための主要なテストツール。
- ビルドツール: なし（Pythonスクリプトがコンテンツを生成し、Jekyllがそれをサイトとして構築します。）
- 言語機能: Python: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得、処理、Markdown生成を行います。
- 自動化・CI/CD:
    - GitHub API: リポジトリ情報をプログラム的に取得するためのインターフェース。
    - GitHub Pages: 生成されたサイトコンテンツをデプロイし、公開するためのサービス。
- 開発標準: Ruff: コードの一貫性を保ち、品質を向上させるための静的解析ツール。

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
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

*   **.editorconfig**: さまざまなエディタ間でコーディングスタイル（インデント、改行コードなど）の一貫性を定義する設定ファイルです。
*   **.github_automation/**: GitHub Actionsなど、リポジトリに関連する自動化スクリプトや設定を格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルの存在をチェックするためのサブディレクトリです。
        *   **README.md**: `check_large_files` ディレクトリの目的と使用方法を説明するファイルです。
        *   **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。チェック対象のファイルサイズや除外パスなどを定義します。
        *   **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
*   **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを指定するファイルです。
*   **LICENSE**: プロジェクトのライセンス情報（この場合はMITライセンス）を記載したファイルです。
*   **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、使用方法などをまとめたメインのドキュメントファイルです。
*   **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが設定されます。
*   **assets/**: Jekyllサイトで使用される画像、CSS、JavaScript、アイコンなどの静的アセットを格納するディレクトリです。
    *   **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）のさまざまな解像度バージョンです。
*   **debug_project_overview.py**: `project_overview` 機能の動作をデバッグするための補助スクリプトです。
*   **generated-docs/**: `project-overview.md` など、他のリポジトリから取得・生成されたドキュメントを一時的に格納する可能性のあるディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイルです。
*   **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインコンテンツとなるMarkdownファイルです。
*   **issue-notes/**: GitHubのIssueに関連するメモや詳細情報をMarkdown形式で保存するディレクトリです。
*   **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示設定など）を定義するファイルです。
*   **pytest.ini**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの実行方法や検出ルールなどを定義します。
*   **requirements-dev.txt**: 開発環境やテスト環境で必要なPythonライブラリをリストアップしたファイルです。
*   **requirements.txt**: プロジェクトを本番環境で実行する際に必要なPythonライブラリをリストアップしたファイルです。
*   **robots.txt**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
*   **ruff.toml**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルやルール違反の検出基準を定義します。
*   **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    *   **generate_repo_list/**: リポジトリ一覧生成機能の中核となるPythonモジュール群です。
        *   **__init__.py**: Pythonパッケージであることを示すファイルです。
        *   **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを管理します。
        *   **config.yml**: リポジトリ一覧生成スクリプトの実行に関する詳細な設定（例: プロジェクト概要取得の有効/無効、タイムアウト設定）を定義します。
        *   **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するためのユーティリティモジュールです。
        *   **date_formatter.py**: 日付や時刻の表示形式を整形するための関数群を提供します。
        *   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力するメインスクリプトです。このプロジェクトのエントリポイントの一つです。
        *   **json_ld_template.json**: 構造化データ（JSON-LD形式）のテンプレートファイルです。SEOのためにリポジトリ情報に付加されます。
        *   **language_info.py**: GitHubリポジトリの主要なプログラミング言語に関する情報を処理・表示するためのロジックを扱います。
        *   **markdown_generator.py**: 取得したリポジトリデータに基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
        *   **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するロジックを提供します。
        *   **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ情報を解析・抽出する機能を提供します。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出・加工する役割を担います。
        *   **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイルです。
        *   **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        *   **strings.yml**: UIメッセージや表示されるテキスト、文言などを一元管理するためのファイルです。多言語対応や文言変更を容易にします。
        *   **template_processor.py**: Markdown生成の際に使用するテンプレートを処理するためのロジックです。
        *   **url_utils.py**: URLの検証、構築、パースなど、URL関連のユーティリティ関数を提供します。
*   **test_project_overview.py**: `project_overview_fetcher` 機能の単体テストまたは統合テストを記述したファイルです。
*   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    *   **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
    *   **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    *   **test_config.py**: 設定ファイルの読み込みや管理に関するテストです。
    *   **test_date_formatter.py**: 日付フォーマット関数のテストです。
    *   **test_environment.py**: 実行環境の設定や依存関係に関するテストです。
    *   **test_integration.py**: プロジェクトの主要なコンポーネント間の統合テストです。
    *   **test_markdown_generator.py**: Markdown生成機能のテストです。
    *   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    *   **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
    *   **test_repository_processor.py**: リポジトリデータ処理機能のテストです。

## 関数詳細説明

*   `generate_repo_list.py`
    *   `main()`: スクリプトのエントリポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力の一連の処理を調整します。
*   `repository_processor.py`
    *   `fetch_repositories(username, token)`: 指定されたGitHubユーザー名とアクセストークンを使用して、そのユーザーが所有するリポジトリの一覧をGitHub APIから取得します。
    *   `process_repository_data(repository_raw_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（名前、説明、言語、スター数など）を抽出し、整形します。
*   `project_overview_fetcher.py`
    *   `fetch_project_overview(repo_url, target_file_path, config)`: 指定されたリポジトリのURLとファイルパス（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出し、返します。`config`オブジェクトからタイムアウトやリトライ回数を参照します。
*   `markdown_generator.py`
    *   `generate_markdown(repositories_list, options)`: 処理済みのリポジトリ情報リストとMarkdown生成に関するオプションを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
*   `badge_generator.py`
    *   `generate_badge_markdown(badge_info)`: リポジトリの言語やステータスなどのバッジ情報を受け取り、対応するMarkdown形式のバッジ文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-02-23 07:07:27 JST
