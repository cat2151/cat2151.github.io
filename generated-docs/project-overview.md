Last updated: 2026-01-09

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定されたGitHubユーザーのリポジトリ情報を自動的に取得します。
- 取得したリポジトリ情報に基づき、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたマークダウンファイル（リポジトリ一覧）を生成します。
- 生成された一覧は、リポジトリのSEO向上、LLMからの参照性改善、および開発効率の向上を目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages): 自動生成されたMarkdownファイルを公開し、Webサイトとして表示するための基盤として利用されます。
- 音楽・オーディオ: N/A
- 開発ツール:
    - Python: プロジェクトの主要なプログラミング言語であり、リポジトリ情報の取得、処理、Markdown生成ロジックを実装しています。
    - GitHub API: GitHubのリポジトリ情報をプログラムから取得するために使用されるインターフェースです。
    - YAML: `config.yml`, `strings.yml`, `seo_template.yml` などの設定ファイルやテンプレートファイルの記述に使用されます。
    - TOML: `pytest.ini`, `ruff.toml` などの設定ファイルや、APIトークンを管理する `secrets.toml` で使用されます。
- テスト: pytest: Pythonコードの単体テストおよび統合テストを実行するためのテストフレームワークです。
- ビルドツール: N/A (Pythonスクリプト自体がMarkdown生成の役割を担い、JekyllがそれをビルドしてWebサイトにします)
- 言語機能: Python: 標準ライブラリに加え、ファイルI/O、HTTPリクエスト処理、文字列操作など、生成システムの各機能で活用されています。
- 自動化・CI/CD: N/A (このプロジェクト自体はCI/CDを不要とし、ローカル開発を重視しています)
- 開発標準:
    - ruff: Pythonコードのスタイルチェックと自動フォーマットを行うリンター兼フォーマッターです。
    - requirements.txt / requirements-dev.txt: プロジェクトの依存関係にあるPythonライブラリを管理するために使用されます。
    - .editorconfig: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
- **.editorconfig**: 異なるエディタ間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定します。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述しています。
- **README.md**: プロジェクトの概要、使い方、設定方法、開発者向けのヒントなどが記載されたメインドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ブラウザタブなどに表示されるアイコン）の各種サイズです。
- **debug_project_overview.py**: `project_overview` 機能のデバッグや単体テストを行うための補助スクリプトです。
- **generated-docs/**: 他のリポジトリから取得された `project-overview.md` ファイルが一時的に保存される、あるいはそのパスが参照されることを想定したディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権の確認に使用されるファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインコンテンツが出力されるMarkdownファイルです。
- **issue-notes/**: 開発中に発生した課題や検討事項をMarkdown形式で記録したメモファイル群です。
    - `10.md`, `12.md`, `14.md`, `16.md`, `2.md`, `4.md`, `6.md`, `8.md`: 各々が特定の課題やアイデアについてのノートです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示設定など）を定義するファイルです。
- **pytest.ini**: Pythonのテストフレームワークである `pytest` の設定ファイルです。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記述したファイルです。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、あるいはクロールすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonのリンター兼フォーマッターである `ruff` の設定ファイルです。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための空ファイルです。
- **src/generate_repo_list/__init__.py**: `generate_repo_list` サブディレクトリをPythonパッケージとして認識させるための空ファイルです。
- **src/generate_repo_list/badge_generator.py**: リポジトリの言語やスター数などに応じたバッジ（SVG/PNG形式の小さな画像やMarkdown記法）を生成するロジックを扱います。
- **src/generate_repo_list/config.yml**: プロジェクト概要取得機能など、システム全体の技術的なパラメータ設定を定義するYAMLファイルです。
- **src/generate_repo_list/config_manager.py**: YAML形式の設定ファイル（`config.yml`, `strings.yml` など）を読み込み、管理するためのユーティリティ関数を提供します。
- **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付情報を、表示に適した形式にフォーマットする機能を提供します。
- **src/generate_repo_list/generate_repo_list.py**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を制御します。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のためにJSON-LD形式の構造化データを生成する際のテンプレートです。
- **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に利用する機能を提供します。
- **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックを実装しています。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出し、取得する機能を提供します。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出・分類するための処理ロジックを実装しています。
- **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやキーワードなどのテンプレートを定義するYAMLファイルです。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
- **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言調整に利用されます。
- **src/generate_repo_list/template_processor.py**: Markdownテンプレート内のプレースホルダーを実際のリポジトリ情報で置き換え、最終的なMarkdownコンテンツを生成する機能を提供します。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` で実装されているプロジェクト概要取得機能のテストケースを定義するスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - `test_config.py`: 設定ファイルの読み込みや管理機能に関するテストです。
    - `test_date_formatter.py`: 日付フォーマット機能のテストです。
    - `test_environment.py`: プロジェクトの実行環境に関するテストです。
    - `test_integration.py`: 各モジュールの連携を含む統合的なテストです。
    - `test_markdown_generator.py`: Markdown生成機能のテストです。
    - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストです。
    - `test_repository_processor.py`: リポジトリデータ処理機能のテストです。

## 関数詳細説明
- **main() (in `src/generate_repo_list/generate_repo_list.py`)**:
    - **役割**: プログラムのメインエントリポイント。コマンドライン引数の解析、設定の読み込み、GitHubリポジトリの取得と処理、最終的なMarkdownファイルの生成という一連のフローを制御します。
    - **引数**: なし（コマンドライン引数は `argparse` などで内部的に処理）。
    - **戻り値**: なし。
    - **機能**: 設定の初期化、GitHub APIからのリポジトリ取得、各リポジトリの詳細処理、Markdownコンテンツの組み立て、ファイルへの書き出し。

- **load_config(config_path) (in `src/generate_repo_list/config_manager.py`)**:
    - **役割**: 指定されたパスのYAML設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    - **引数**: `config_path` (str): 読み込むYAMLファイルのパス。
    - **戻り値**: dict: 読み込まれた設定内容を含む辞書。
    - **機能**: YAMLファイルをオープンし、内容をパースしてデータ構造に変換します。

- **fetch_repositories(username, token, limit=None) (in `src/generate_repo_list/repository_processor.py` または関連モジュール)**:
    - **役割**: 指定されたGitHubユーザー名と認証トークンを使用して、GitHub APIからリポジトリ情報を取得します。
    - **引数**: `username` (str): GitHubユーザー名。 `token` (str): GitHub API認証トークン。`limit` (int, optional): 取得するリポジトリ数の上限。
    - **戻り値**: list: 取得したリポジトリデータのリスト。
    - **機能**: GitHub APIのエンドポイントにHTTPリクエストを送信し、JSON形式で返されるリポジトリデータを取得します。

- **process_repository(repo_data, config) (in `src/generate_repo_list/repository_processor.py`)**:
    - **役割**: GitHub APIから取得した個々の生のリポジトリデータを受け取り、表示に必要な情報（名前、説明、URL、言語、統計など）に整形します。
    - **引数**: `repo_data` (dict): 生のリポジトリデータ。 `config` (dict): 設定情報。
    - **戻り値**: dict: 整形されたリポジトリデータ。
    - **機能**: 必要なフィールドの抽出、日付のフォーマット、言語情報の処理、アーカイブ/フォークの分類などを行います。

- **get_project_overview(repo_name, owner, target_file, config) (in `src/generate_repo_list/project_overview_fetcher.py`)**:
    - **役割**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出して取得します。
    - **引数**: `repo_name` (str): リポジトリ名。 `owner` (str): リポジトリの所有者。 `target_file` (str): 概要が記述されているファイル名。 `config` (dict): 設定情報。
    - **戻り値**: str: 抽出されたプロジェクト概要のテキスト、または空文字列。
    - **機能**: GitHub APIを通じてリポジトリ内のファイルコンテンツを取得し、特定のセクションから説明文をパースします。

- **generate_markdown(processed_repo_list, seo_data, strings_data, config) (in `src/generate_repo_list/markdown_generator.py`)**:
    - **役割**: 処理済みのリポジトリリストとテンプレート情報を用いて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    - **引数**: `processed_repo_list` (list): 整形されたリポジトリデータのリスト。 `seo_data` (dict): SEO関連データ。 `strings_data` (dict): 表示文言データ。 `config` (dict): 設定情報。
    - **戻り値**: str: 生成されたMarkdown文字列。
    - **機能**: テンプレートを読み込み、各リポジトリデータを埋め込み、Markdown記法に沿った文字列を構築します。

## 関数呼び出し階層ツリー
```
main()
├── config_manager.load_config(config_path) // 設定ファイル (config.yml, strings.yml, seo_template.yml) を読み込む
├── repository_processor.fetch_repositories(username, token, limit) // GitHub APIからリポジトリ一覧を取得
├── for each repository in fetched_repositories:
│   ├── repository_processor.process_repository(repo_data, config) // 個々のリポジトリデータを整形
│   ├── project_overview_fetcher.get_project_overview(repo_name, owner, target_file, config) // リポジトリの概要を取得
│   ├── badge_generator.generate_badge(repo_data) // 必要に応じてバッジ情報を生成
│   └── date_formatter.format_date(date_string) // 日付表示を整形
└── markdown_generator.generate_markdown(processed_repo_list, seo_data, strings_data, config) // 整形されたデータからMarkdownを生成

---
Generated at: 2026-01-09 07:06:46 JST
