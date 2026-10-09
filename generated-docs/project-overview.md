Last updated: 2026-10-10

# Project Overview

## プロジェクト概要
- GitHub Pagesサイトでリポジトリ一覧を自動生成し、閲覧性を向上させるシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownを出力します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照失敗の問題を緩和します。

## 技術スタック
- フロントエンド: Jekyll: GitHub Pages上で静的サイトを構築するためのフレームワーク。生成されたMarkdownコンテンツがJekyllによってレンダリングされます。Markdown: Jekyllサイトでコンテンツを記述するための軽量マークアップ言語。
- 音楽・オーディオ: 該当なし。
- 開発ツール: Python: プロジェクトの主要な開発言語として、リポジトリ情報の取得、処理、Markdown生成スクリプトに利用されます。Git/GitHub: ソースコードのバージョン管理とリポジトリホスティングに利用されます。TOML: 設定ファイル（例: `ruff.toml`, `secrets.toml`）の記述形式として使用されます。YAML: 設定ファイル（例: `config.yml`, `strings.yml`）およびテンプレートファイルの記述形式として使用されます。
- テスト: pytest: Pythonアプリケーションのユニットテストおよび統合テストを行うためのテストフレームワークです。
- ビルドツール: Markdown: GitHub Pagesにデプロイされるコンテンツの出力形式です。Jekyllと連携してHTMLに変換されます。
- 言語機能: Python: スクリプト記述に使用されるプログラミング言語そのものです。
- 自動化・CI/CD: GitHub Pages: GitHubリポジトリから静的ウェブサイトを自動的にデプロイするサービスです。
- 開発標準: ruff: Pythonコードのフォーマット、リンティング、スタイルチェックを行うツールです。コード品質と一貫性を保ちます。

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
- **.editorconfig**: 複数のエディタやIDEでコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルがないかをチェックする機能に関連するファイル群です。
        - **README.md**: `check_large_files`機能の概要や使用方法を説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **scripts/check_large_files.py**: 指定された条件に基づいてリポジトリ内の大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイルです。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使用方法などが記載された主要なドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を含みます。
- **assets/**: サイトで使用される画像、アイコン、フォントなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズです。
- **debug_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher`）のデバッグやテストを行うための補助スクリプトです。
- **generated-docs/**: スクリプトによって自動生成されたドキュメントやデータが格納されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される主要なMarkdownファイルで、GitHub Pagesサイトのリポジトリ一覧ページとして機能します。
- **issue-notes/22.md**: プロジェクトの特定の課題やノートを記録するためのMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の設定ファイルで、ウェブアプリの表示方法や動作を定義します。
- **pytest.ini**: `pytest`フレームワークの実行設定を定義するファイルです。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に必要な本番環境のPythonパッケージの依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonのコードフォーマッター兼リンターである`ruff`の設定ファイルです。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成機能の中核をなすPythonモジュール群です。
        - **__init__.py**: `generate_repo_list`パッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのライセンスや言語などのバッジ画像を生成またはそのMarkdownを組み立てる機能を提供します。
        - **config.yml**: リポジトリ一覧生成に関する各種設定（例: project_overview機能の有効/無効、対象ファイルなど）を定義するファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プログラムからアクセスしやすく管理する機能を提供します。
        - **date_formatter.py**: 日付や時刻の文字列を特定のフォーマットに変換するユーティリティ関数を提供します。
        - **generate_repo_list.py**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式のリポジトリ一覧を生成します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式のメタデータテンプレートです。
        - **language_info.py**: リポジトリの使用言語に関する情報処理や表示に関する機能を提供します。
        - **markdown_generator.py**: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツ（特にリポジトリ一覧や個々のリポジトリセクション）を生成する機能を提供します。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすいように整形、フィルタリング、分類する機能を提供します。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するテンプレート設定を定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - **strings.yml**: プロジェクト内で使用される表示メッセージや文言を集中管理するファイルで、多言語対応や文言変更を容易にします。
        - **template_processor.py**: テンプレートエンジン（Jekyllなど）と連携して、データとテンプレートから最終的な出力（例: HTML、Markdown）を生成する機能を提供します。
        - **url_utils.py**: URLの検証、構築、パースなど、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher`機能のユニットテストおよび統合テストを行うスクリプトです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **conftest.py**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイルで、複数のテストファイルで共有されます。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの結合テストを行うスクリプトです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストを行うスクリプトです。
    - **test_config.py**: 設定ファイル（`config.yml`など）の読み込みや設定値へのアクセスに関するテストを行うスクリプトです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストを行うスクリプトです。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを行うスクリプトです。
    - **test_integration.py**: プロジェクトの主要なコンポーネント間の連携を検証する統合テストスクリプトです。
    - **test_markdown_generator.py**: Markdown生成機能のテストを行うスクリプトです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテストを行うスクリプトです。
    - **test_readme_badge_extractor.py**: READMEファイルからのバッジ抽出機能のテストを行うスクリプトです。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテストを行うスクリプトです。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main()`: スクリプトのエントリーポイント。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成までの一連の主要な処理フローを制御します。引数: なし。戻り値: なし。
    - `get_repositories(username)`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIを通じて取得します。引数: `username` (str)。戻り値: リポジトリデータのリスト (list)。
    - `process_repository(repo_data)`: GitHub APIから取得した単一のリポジトリデータを、プロジェクト内で使用される統一された形式に整形し、必要な情報を抽出します。引数: `repo_data` (dict)。戻り値: 整形されたリポジトリ情報 (dict)。
    - `generate_markdown(processed_repos, output_file)`: 処理済みのリポジトリ情報リストに基づいて、GitHub Pages用のMarkdownファイルを生成し、指定されたファイルに出力します。引数: `processed_repos` (list), `output_file` (str)。戻り値: なし。
- **badge_generator.py**:
    - `generate_badge(badge_type, value)`: 指定された種類と値に基づき、適切なバッジのMarkdown文字列を生成します。引数: `badge_type` (str), `value` (str)。戻り値: バッジのMarkdown文字列 (str)。
- **config_manager.py**:
    - `load_config(config_path)`: YAML形式の設定ファイルを指定されたパスから読み込み、設定値を管理するオブジェクトを返します。引数: `config_path` (str)。戻り値: 設定管理オブジェクト (ConfigManager)。
    - `get_setting(key_path)`: ドット区切りのパス（例: `"project_overview.enabled"`）を指定して、設定ファイル内の特定の値を安全に取得します。引数: `key_path` (str)。戻り値: 設定値 (any)。
- **date_formatter.py**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を、人間が読みやすい形式（例: "YYYY年MM月DD日"）に変換します。引数: `iso_date_string` (str)。戻り値: フォーマットされた日付文字列 (str)。
- **markdown_generator.py**:
    - `create_repo_section(repo_info)`: 単一のリポジトリ情報から、そのリポジトリの詳細を含むMarkdown形式のセクション（タイトル、説明、リンクなど）を生成します。引数: `repo_info` (dict)。戻り値: リポジトリセクションのMarkdown文字列 (str)。
    - `create_index_page(repo_list)`: 複数のリポジトリセクションを統合し、GitHub Pagesのメインページとなる`index.md`全体のMarkdownコンテンツを生成します。引数: `repo_list` (list)。戻り値: インデックスページの全Markdownコンテンツ (str)。
- **project_overview_fetcher.py**:
    - `fetch_overview(repo_url, config)`: 指定されたリポジトリの特定のパスにある`project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出し、取得します。APIリクエストやキャッシュ機能を利用する場合があります。引数: `repo_url` (str), `config` (dict)。戻り値: プロジェクト概要の3行説明のリスト (list) またはNone。
- **repository_processor.py**:
    - `normalize_repo_data(github_api_data)`: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で一貫して利用できるような標準化された形式に変換します。引数: `github_api_data` (dict)。戻り値: 標準化されたリポジトリデータ (dict)。
    - `classify_repository(repo_data)`: リポジトリデータを「アクティブ」「アーカイブ」「フォーク」などのカテゴリに分類するための情報を提供します。引数: `repo_data` (dict)。戻り値: 分類タイプ (str)。
- **template_processor.py**:
    - `render_template(template_path, data)`: 指定されたテンプレートファイルと提供されたデータを使用して、最終的なテキストコンテンツ（Markdownなど）をレンダリングします。引数: `template_path` (str), `data` (dict)。戻り値: レンダリングされた文字列 (str)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-10 07:13:02 JST
