Last updated: 2026-11-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pagesサイト向けにマークダウンファイルを自動生成するシステムです。
- 生成されたリポジトリ一覧ページは検索エンジンにクロールされやすく、LLMによるリポジトリ参照失敗の緩和が期待されます。
- バッジ表示、アクティブ/アーカイブ/フォーク分類、各リポジトリの概要自動取得など、豊富な機能を提供します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesサイトの静的サイト生成フレームワークとして、本プロジェクトで生成されたMarkdownファイルをレンダリングするために利用されます。
    - Markdown: リポジトリ一覧のコンテンツ形式として使用され、JekyllによってHTMLに変換されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - GitHub API: リポジトリ情報の取得における主要なインターフェースです。
    - pytest: Pythonで書かれたテストコードを実行するためのフレームワークです。
    - ruff: Pythonのコードスタイルをチェックし、自動でフォーマットするためのツールです。
- テスト:
    - pytest: プロジェクトの各機能の単体テスト、統合テスト、および環境テストを実行するために使用されます。
- ビルドツール:
    - Python: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得、処理、Markdown生成など、すべてのロジックの実行環境として機能します。
- 言語機能:
    - Python: プロジェクト全体の実装に使用されているプログラミング言語です。
- 自動化・CI/CD:
    - (直接的なCI/CDツールは明記されていませんが、生成物がGitHub Pagesで利用されるため、間接的にGitHub Actions等のデプロイ機構と連携します。)
- 開発標準:
    - ruff: コードの品質と一貫性を保つためのリンティングとフォーマットに使用されます。
    - .editorconfig: 複数の開発者やエディタ間でのコードスタイルの一貫性を強制するために使用されます。

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
- **.editorconfig**: エディタのコードスタイル設定を定義し、プロジェクト全体で一貫したコーディングスタイルを維持します。
- **.github_automation/**: GitHub Actionsなどによる自動化スクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェックに関するスクリプト群です。
        - **README.md**: `check_large_files` ディレクトリの目的と使用方法を説明します。
        - **check-large-files.toml**: 大容量ファイルチェックのルールと設定が記述されています。
        - **scripts/check_large_files.py**: 指定されたしきい値を超える大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義します。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、設定など、プロジェクト全体に関する詳細な情報を提供する主要なドキュメントです。
- **_config.yml**: JekyllベースのGitHub Pagesサイトにおけるグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの情報を保持します。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: 各種デバイスやブラウザで表示されるファビコン画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグや単体テストを目的としたスクリプトです。
- **generated-docs/**: 各リポジトリから取得された `project-overview.md` など、動的に生成されるドキュメントやデータが格納されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。本プロジェクトによって生成されたリポジトリ一覧コンテンツがここに出力されます。
- **issue-notes/**: プロジェクトの特定の課題（Issue）に関するメモや詳細情報を格納するディレクトリです。
    - **22.md**: Issue番号22に関するノートまたはドキュメントです。
- **manifest.json**: PWA (Progressive Web App) のマニフェストファイルで、Webアプリの表示方法や動作を定義します。
- **pytest.ini**: `pytest` テストフレームワークの設定ファイルで、テストの挙動やオプションを定義します。
- **requirements-dev.txt**: 開発時およびテスト時に必要となるPythonの依存ライブラリをリストアップします。
- **requirements.txt**: プロジェクトを本番環境で実行する際に必要となるPythonの依存ライブラリをリストアップします。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、または避けるべきかを指示するファイルです。
- **ruff.toml**: `ruff` リンターおよびフォーマッターの設定ファイルで、Pythonコードのスタイルルールを定義します。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
- **src/generate_repo_list/**: GitHubリポジトリ一覧生成の主要なロジックを格納するPythonパッケージです。
    - **__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（例: Shields.io）をMarkdown形式で生成するロジックを扱います。
    - **config.yml**: リポジトリ一覧生成に関する各種設定（例: `project_overview` 機能の有効/無効、対象ファイルパス、タイムアウト時間など）を定義するYAMLファイルです。
    - **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、プロジェクト全体で設定値にアクセスするためのインターフェースを提供するモジュールです。
    - **date_formatter.py**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するユーティリティ関数を提供します。
    - **generate_repo_list.py**: このプロジェクトのメインスクリプトであり、GitHub APIからのリポジトリ情報取得からMarkdownファイルの生成・出力までの一連の処理を調整します。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートファイルです。
    - **language_info.py**: リポジトリで使用されているプログラミング言語の情報を処理し、表示に適した形式に変換するロジックを扱います。
    - **markdown_generator.py**: 処理済みのリポジトリデータに基づいて、最終的なリポジトリ一覧を含むMarkdownコンテンツを生成するコアロジックを担います。
    - **project_overview_fetcher.py**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動で取得する機能を提供します。
    - **readme_badge_extractor.py**: 各リポジトリのREADME.mdファイルから、特定のパターンに合致するバッジ情報を抽出するロジックです。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、表示に必要な情報に整形・フィルタリングする主要な処理を担います。
    - **seo_template.yml**: SEO関連のメタデータや構造化データのテンプレート設定を定義するファイルです。
    - **statistics_calculator.py**: 各リポジトリに関連する統計情報（スター数、フォーク数など）を計算し、表示用のデータを準備します。
    - **strings.yml**: プロジェクト内で使用される各種メッセージ、ラベル、文言などを一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
    - **template_processor.py**: Markdown生成時に特定のテンプレート（JekyllのLiquidタグなど）を処理し、動的なコンテンツを埋め込むロジックを扱います。
    - **url_utils.py**: URLの検証、構築、パースなど、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの単体テストを記述したファイルです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **conftest.py**: `pytest` のテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義します。
    - **test_badge_generator_integration.py**: `badge_generator` の機能が他のモジュールと連携して正しく動作するかを確認する統合テストです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストコードです。
    - **test_config.py**: 設定ファイルの読み込みやアクセスが正しく行われるかを確認するテストです。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテストコードです。
    - **test_environment.py**: プロジェクトの実行環境に関するテスト（例: 必須環境変数の存在チェック）です。
    - **test_integration.py**: プロジェクトの主要なフローが全体として正しく機能するかを確認する包括的な統合テストです。
    - **test_markdown_generator.py**: Markdown生成ロジックのテストコードです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` が期待通りにリポジトリ概要を取得できるかを確認するテストです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストコードです。
    - **test_repository_processor.py**: リポジトリデータ処理ロジックのテストコードです。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main(username, output_file, limit)`: プロジェクトのエントリポイント。指定されたGitHubユーザー名のリポジトリ情報を取得し、整形してMarkdownファイルとして出力します。`username` (str): GitHubユーザー名, `output_file` (str): 出力ファイル名, `limit` (int, optional): 処理するリポジトリ数の上限。
- **repository_processor.py**:
    - `fetch_repositories(username)`: GitHub APIを使用して、指定されたユーザー名の公開リポジトリ一覧を取得します。`username` (str): GitHubユーザー名。戻り値: (list) リポジトリデータのリスト。
    - `process_repository_data(repo_data)`: GitHub APIから取得した個々のリポジトリの生データを、プロジェクトで利用しやすい形式（例: 表示名、URL、説明、言語など）に整形・加工します。`repo_data` (dict): 単一のリポジトリの生データ。戻り値: (dict) 整形されたリポジトリデータ。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_full_name, target_file, section_title)`: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、指定されたセクション（例: "プロジェクト概要"）の3行説明を抽出します。`repo_full_name` (str): `owner/repo` 形式のリポジトリ名, `target_file` (str): 概要ファイルパス, `section_title` (str): 抽出対象セクションタイトル。戻り値: (list of str) 概要の行リスト、または空リスト。
- **markdown_generator.py**:
    - `generate_markdown(processed_repositories)`: 処理済みのリポジトリデータリストを受け取り、それらをJekyll互換のMarkdown形式の文字列に変換します。各リポジトリの情報（概要、バッジなど）を適切な形式で埋め込みます。`processed_repositories` (list of dict): 整形されたリポジトリデータのリスト。戻り値: (str) 生成されたMarkdown文字列。
- **badge_generator.py**:
    - `create_badge_markdown(label, message, color)`: ラベル、メッセージ、色に基づいてShields.io形式のMarkdownバッジ文字列を生成します。`label` (str): バッジのラベル, `message` (str): バッジに表示されるメッセージ, `color` (str): バッジの色。戻り値: (str) Markdown形式のバッジ文字列。
- **config_manager.py**:
    - `load_config(file_path)`: YAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。`file_path` (str): 設定ファイルのパス。戻り値: (dict) 設定内容。
    - `get_string(key)`: `strings.yml` から指定されたキーに対応する文字列を取得します。`key` (str): 取得したい文字列のキー。戻り値: (str) 対応する文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-04 07:07:12 JST
