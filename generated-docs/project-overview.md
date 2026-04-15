Last updated: 2026-04-16

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、個人のGitHubリポジトリ情報を自動取得するシステムです。
- 取得した情報からJekyll/GitHub Pages向けのSEO最適化されたリポジトリ一覧Markdownを生成します。
- これにより、GitHub Pagesの検索エンジン可視性を高め、リポジトリの発見性を向上させます。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベース) - 静的サイトジェネレーターJekyllを利用したGitHub Pagesサイトを対象とし、最終的な出力はSEO最適化されたMarkdown形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - Python: プロジェクトの主要な開発言語として、スクリプトの作成、GitHub APIとの連携、ファイルの生成などに使用されています。
    - GitHub API: リポジトリ情報の取得元として、GitHubの公式APIを利用しています。
    - PyYAML: `config.yml` や `strings.yml` などのYAML形式の設定ファイルを読み込むために使用されます。
    - TOML: `pytest.ini` や `ruff.toml`、`secrets.toml` など、設定ファイルの記述形式として使用されます。
    - argparse: コマンドライン引数を解析し、スクリプトの動作を制御するために使用されます。
- テスト:
    - pytest: Pythonプロジェクトのテストフレームワーク。単体テストや統合テストの実行、結果の検証に利用されています。
- ビルドツール:
    - Pythonスクリプト: 専用のビルドツールは使用せず、Pythonスクリプト自体がリポジトリ情報からMarkdownファイルを生成する役割を担います。
- 言語機能:
    - Python言語機能: オブジェクト指向プログラミング、ファイルI/O、HTTPリクエスト処理など、Pythonの標準的な機能が幅広く活用されています。
- 自動化・CI/CD:
    - GitHub Actions (一部): `.github_automation` ディレクトリ内のスクリプトは、大容量ファイルチェックなど、一部の自動化タスクにGitHub Actionsが使用されている可能性を示唆します。主要なリポジトリ一覧生成プロセスはローカル実行を重視しています。
- 開発標準:
    - Ruff: Pythonコードの品質と一貫性を保つための高速リンター・フォーマッターです。`ruff.toml`で設定を管理しています。

## ファイル階層ツリー
```
📄 .editorconfig
📁 .github_automation/
  📁 check_large_files/
    📖 README.md
    📄 check-large_files.toml
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
- **.github_automation/**: GitHub Actionsなど、GitHub上での自動化ワークフローに関連するスクリプトや設定を格納するディレクトリ。
    - **check_large_files/**: リポジトリ内の大容量ファイルをチェックするためのスクリプト群。
        - **README.md**: `check_large_files` 機能の説明。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）が記述されたファイル。
- **README.md**: プロジェクトの概要、目的、セットアップ方法、使い方、オプション、ライセンスなどの基本的な情報が記述されたメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の共通設定ファイル。テーマ、プラグイン、変数の定義などが含まれます。
- **assets/**: GitHub Pagesサイトで利用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像。複数のサイズが用意されています。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグや単体テストを目的としたスクリプト。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメントやデータ（例: `project-overview.md`）が一時的に格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインのMarkdownファイル。JekyllによってHTMLに変換され、サイトのトップページとして機能します。
- **issue-notes/22.md**: 特定の課題や検討事項に関するメモファイル。
- **manifest.json**: Progressive Web App (PWA) の設定ファイル。ウェブアプリケーションのメタデータ（アプリ名、アイコン、表示モードなど）を定義します。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テストの発見ルール、プラグイン、実行オプションなどが定義されます。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonの依存ライブラリを列挙したファイル。
- **requirements.txt**: プロジェクトの実行環境（本番環境）で必要となるPythonの依存ライブラリを列挙したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイル。
- **ruff.toml**: Pythonのリンター/フォーマッターであるRuffの設定ファイル。コードのスタイルや品質に関するルールが定義されます。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    - **__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるためのファイル。
    - **generate_repo_list/**: リポジトリ一覧生成ロジックの中核をなすPythonパッケージ。
        - **__init__.py**: `generate_repo_list` パッケージを初期化するためのファイル。
        - **badge_generator.py**: リポジトリの言語、ステータス、ライセンスなどを示すバッジの生成ロジックを担当。
        - **config.yml**: リポジトリ一覧生成スクリプト自体の設定を定義するファイル（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）。
        - **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するユーティリティ。
        - **date_formatter.py**: 日付や時刻の情報を特定のフォーマットに整形する機能を提供。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIからのデータ取得、リポジトリ処理、Markdown生成の全体フローを orchestrate します。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形に整形するロジック。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリから `generated-docs/project-overview.md` ファイルを読み込み、プロジェクト概要を抽出する機能。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するロジック。
        - **repository_processor.py**: GitHub APIから取得した個々のリポジトリデータを整形し、Markdown生成に必要な情報（説明、言語、スター数など）を抽出・加工する役割。
        - **seo_template.yml**: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレート。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算するロジック。
        - **strings.yml**: UIに表示される各種メッセージや文言を一元管理するためのファイル。多言語対応や文言の調整に利用されます。
        - **template_processor.py**: Markdown生成の際に利用されるテンプレートエンジン（例: Jinja2）を介して、データとテンプレートを結合し最終的な文字列を生成する役割。
        - **url_utils.py**: URLの検証、整形、生成など、URLに関連するユーティリティ機能。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの機能に関するテストスクリプト。
- **tests/**: pytestテストフレームワークで実行されるテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャ、フック、その他の設定を定義するためのファイル。
    - **test_badge_generator_integration.py**: `badge_generator` の機能の統合テスト。
    - **test_check_large_files.py**: `.github_automation/check_large_files` スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテスト。
    - **test_date_formatter.py**: `date_formatter` モジュールのテスト。
    - **test_environment.py**: 実行環境の設定や依存関係に関するテスト。
    - **test_integration.py**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator` モジュールのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールのテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor` モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor` モジュールのテスト。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルが特定の役割を担っています。具体的な関数名はコード解析なしには特定できませんが、ファイル名から推測される主要な機能単位を関数として説明します。

- **generate_repo_list.py**:
    - **main()**: プロジェクト全体の実行エントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、各リポジトリの処理、Markdown生成、最終的な出力ファイルの書き込みといった一連のフローを制御します。
- **repository_processor.py**:
    - **process_repository_data(repo_data)**: GitHub APIから取得した個々のリポジトリデータ（`repo_data`）を受け取り、必要な情報（リポジトリ名、説明、URL、スター数、最終更新日など）を抽出し、Markdown生成に適した形式に整形して返します。
- **project_overview_fetcher.py**:
    - **fetch_project_overview(repo_url, config)**: 特定のリポジトリ（`repo_url`）から設定ファイル（`config`）で指定されたパス（例: `generated-docs/project-overview.md`）のコンテンツを取得し、そこから指定されたセクション（例: "プロジェクト概要"）の3行の説明文を抽出して返します。
- **markdown_generator.py**:
    - **generate_markdown_for_repo(processed_repo_data, templates)**: 整形された単一のリポジトリデータ（`processed_repo_data`）とMarkdownテンプレート（`templates`）を受け取り、そのリポジトリに関するMarkdownスニペットを生成して返します。
    - **generate_full_repo_list_markdown(all_repo_data, global_templates)**: 処理された全リポジトリのデータ（`all_repo_data`）とサイト全体のテンプレート（`global_templates`）を使用して、最終的なリポジトリ一覧のMarkdownファイルを生成します。
- **badge_generator.py**:
    - **create_language_badge_url(language)**: 指定されたプログラミング言語（`language`）に対応するバッジ画像のURLを生成します。
    - **create_status_badge_url(status)**: リポジトリのステータス（例: "active", "archived"）に応じたバッジ画像のURLを生成します。
- **date_formatter.py**:
    - **format_date_human_readable(iso_date_string)**: ISO形式の日付文字列（`iso_date_string`）を受け取り、"YYYY年MM月DD日"のような人間が読みやすい形式に変換して返します。
- **config_manager.py**:
    - **load_config(config_path)**: 指定されたパス（`config_path`）からYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
- **statistics_calculator.py**:
    - **calculate_repo_statistics(repo_data)**: リポジトリデータ（`repo_data`）からスター数、フォーク数、ウォッチ数などの統計情報を抽出し、集計して返します。
- **url_utils.py**:
    - **construct_repo_page_url(username, repo_name)**: GitHubユーザー名（`username`）とリポジトリ名（`repo_name`）を受け取り、対応するGitHub Pagesサイト上のリポジトリ詳細ページへのURLを構築して返します。
- **template_processor.py**:
    - **render_template(template_content, context_data)**: テンプレート文字列（`template_content`）とレンダリングに使用するコンテキストデータ（`context_data`）を受け取り、データを埋め込んだ最終的な文字列を生成して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-16 07:18:08 JST
