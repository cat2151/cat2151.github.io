Last updated: 2026-01-05

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHubリポジトリ情報を自動で取得・整形するシステムです。
- 取得した情報からJekyllベースのGitHub Pagesサイト向けに最適化されたMarkdownファイルを自動生成します。
- 検索エンジンからのクロール性向上とLLMの参照失敗緩和を目指し、リポジトリ一覧と各リポジトリ概要を公開します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式), HTML/CSS (MarkdownからJekyllによってレンダリングされる要素)
- 音楽・オーディオ: 言及なし
- 開発ツール: Python (主要な開発言語), GitHub API (リポジトリ情報取得), GitHub Pages (自動生成されたサイトのホスティング環境)
- テスト: pytest (Pythonのテストフレームワーク)
- ビルドツール: Python (スクリプト自体がMarkdownファイルの生成・ビルドプロセスを実行)
- 言語機能: Python (汎用プログラミング言語)
- 自動化・CI/CD: GitHub Pages (自動デプロイ先), GitHub Actions (プロジェクト概要機能のコンテキストで共通ワークフローの利用が示唆されており、自動化連携の可能性を持つ)
- 開発標準: ruff (Pythonコードのフォーマッター兼リンター), .editorconfig (エディタのコードスタイル設定を統一)

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されているファイル。
- **README.md**: プロジェクトの概要、機能、使用方法、設定、開発者向けヒントなどを記述したメインドキュメント。
- **_config.yml**: Jekyll静的サイトジェネレータのサイト全体の構成設定ファイル。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
  - **favicon-*.png**: Webサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグやテストに特化したスクリプト。
- **generated-docs/**: プロジェクト内で生成されるドキュメントや一時ファイルを格納するためのディレクトリ（現在は空またはプレースホルダー）。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによって生成されるメインのMarkdownファイル。GitHub Pagesのトップページとしてリポジトリ一覧を表示する。
- **issue-notes/**: 開発過程で発生した課題や検討事項に関するメモをMarkdown形式で整理したファイル群。
  - **10.md**, **12.md** など: 個別の課題やメモを記述したファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）としてウェブサイトを定義するための設定ファイル。アプリの名称、アイコン、表示モードなどを指定。
- **pytest.ini**: pytestテストフレームワークの動作設定を記述するファイル。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonライブラリとそのバージョンをリスト化したファイル。
- **requirements.txt**: プロジェクトの実行に必要な本番環境のPythonライブラリとそのバージョンをリスト化したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはしないべきかを指示するファイル。
- **ruff.toml**: Pythonコードのリンターおよびフォーマッターであるruffの設定ファイル。コード品質とスタイルを維持するために使用される。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリ。
  - **__init__.py**: Pythonがディレクトリをパッケージとして扱うために必要なファイル。
  - **generate_repo_list/**: リポジトリ一覧を生成するロジックをまとめたPythonパッケージ。
    - **__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す。
    - **badge_generator.py**: リポジトリの言語やステータスを示すバッジ（アイコン）を生成するロジックを実装。
    - **config.yml**: `generate_repo_list`スクリプトの動作に関する設定（例: プロジェクト概要取得機能の有効/無効、ファイルパス、タイムアウトなど）。
    - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュール。
    - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供。
    - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIからのリポジトリ取得、データ処理、Markdown生成までの一連のフローを制御。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を生成するためのテンプレートファイル。
    - **language_info.py**: リポジトリが使用するプログラミング言語の情報を取得し、整形・分析する機能を提供。
    - **markdown_generator.py**: 処理されたリポジトリ情報を受け取り、最終的なMarkdown形式の出力を生成するモジュール。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出する機能。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、表示やMarkdown生成に適した形式に変換・整形するモジュール。
    - **seo_template.yml**: SEO関連のメタデータや、検索エンジンに表示されるコンテンツのテンプレート設定を管理。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能。
    - **strings.yml**: プロジェクト内で表示される様々なメッセージ、ラベル、文言などを管理するための設定ファイル（多言語対応や文言の一元管理に利用）。
    - **template_processor.py**: Markdown生成時に使用されるテンプレート（Jinja2などのテンプレートエンジン）のレンダリングを処理するモジュール。
    - **url_utils.py**: URLの検証、整形、生成などのユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得と解析）に関する単体テストスクリプト。
- **tests/**: プロジェクトの各種テストスクリプトを格納するディレクトリ。
  - **test_config.py**: 設定ファイル（`config.yml`など）の読み込みや解析に関するテスト。
  - **test_date_formatter.py**: `date_formatter.py`モジュールの日付整形機能に関するテスト。
  - **test_environment.py**: プロジェクトの実行環境や依存関係に関するテスト。
  - **test_integration.py**: 複数のモジュールやシステムコンポーネントが連携して正しく動作するかを確認する統合テスト。
  - **test_markdown_generator.py**: `markdown_generator.py`モジュールのMarkdown生成機能に関するテスト。
  - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`モジュールの詳細なテスト。
  - **test_repository_processor.py**: `repository_processor.py`モジュールのリポジトリデータ処理機能に関するテスト。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**
    - `main()`: プログラムのエントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、各リポジトリの処理、Markdownファイルの生成といった全体のワークフローを orchestrate します。
        - 引数: なし (コマンドライン引数は内部で解析)
        - 戻り値: なし
    - `parse_arguments()`: コマンドライン引数を解析し、GitHubユーザー名、出力ファイルパス、処理リポジトリ数の上限（`--limit`）などのオプションを取得します。
        - 引数: なし
        - 戻り値: `argparse.Namespace`オブジェクト (解析された引数を含む)
- **src/generate_repo_list/badge_generator.py**
    - `generate_badges(repo_data)`: リポジトリデータに基づいて、言語バッジやアーカイブステータスバッジなどのMarkdown形式のバッジ文字列を生成します。
        - 引数: `repo_data` (dict, リポジトリ情報)
        - 戻り値: `str` (生成されたバッジのMarkdown文字列)
- **src/generate_repo_list/config_manager.py**
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (str, 設定ファイルへのパス)
        - 戻り値: `dict` (設定内容)
- **src/generate_repo_list/date_formatter.py**
    - `format_date(iso_date_string, format_string)`: ISO 8601形式の日付文字列を、指定されたフォーマット文字列に従って整形します。
        - 引数: `iso_date_string` (str, ISO形式の日付), `format_string` (str, 望ましい出力フォーマット)
        - 戻り値: `str` (整形された日付文字列)
- **src/generate_repo_list/language_info.py**
    - `get_language_statistics(repo_name, owner, token)`: 特定のリポジトリの言語使用率に関する統計情報をGitHub APIから取得し、処理します。
        - 引数: `repo_name` (str), `owner` (str), `token` (str, GitHub APIトークン)
        - 戻り値: `dict` (言語統計情報)
- **src/generate_repo_list/markdown_generator.py**
    - `generate_markdown_for_repository(processed_repo_data, template_config)`: 処理済みのリポジトリデータとテンプレート設定を使用して、個々のリポジトリに対応するMarkdownコンテンツを生成します。
        - 引数: `processed_repo_data` (dict), `template_config` (dict)
        - 戻り値: `str` (生成されたMarkdown文字列)
    - `generate_repo_list_markdown(all_repo_data, config)`: 全リポジトリのデータと設定を基に、最終的なリポジトリ一覧のMarkdownファイルを生成します。
        - 引数: `all_repo_data` (list of dicts), `config` (dict)
        - 戻り値: `str` (生成されたリポジトリ一覧のMarkdown文字列)
- **src/generate_repo_list/project_overview_fetcher.py**
    - `fetch_project_overview(repo_name, owner, token, config)`: 指定されたリポジトリ内の特定のMarkdownファイルから「プロジェクト概要」セクションの3行説明を抽出し、返します。
        - 引数: `repo_name` (str), `owner` (str), `token` (str), `config` (dict, 概要取得設定)
        - 戻り値: `str` (抽出された概要テキスト) または `None`
- **src/generate_repo_list/repository_processor.py**
    - `fetch_all_repositories(username, token)`: GitHub APIを使用して、指定されたユーザーの公開リポジトリ（およびフォークなど設定に応じたもの）をすべて取得します。
        - 引数: `username` (str), `token` (str, GitHub APIトークン)
        - 戻り値: `list of dicts` (取得した生のリポジトリデータ)
    - `process_repository_data(raw_repo_data, config)`: 生のリポジトリデータを受け取り、表示やMarkdown生成に適した形式に整形・追加情報を付与（例: 概要の取得、バッジ生成）します。
        - 引数: `raw_repo_data` (dict), `config` (dict)
        - 戻り値: `dict` (処理済みのリポジトリデータ)
- **src/generate_repo_list/statistics_calculator.py**
    - `calculate_overall_statistics(all_repo_data)`: 全リポジトリのデータから、スター総数、言語分布などの集計統計情報を計算します。
        - 引数: `all_repo_data` (list of dicts)
        - 戻り値: `dict` (計算された統計情報)
- **src/generate_repo_list/template_processor.py**
    - `render_template(template_path, context)`: 指定されたテンプレートファイルにコンテキストデータを適用し、最終的なテキスト（例: Markdown）をレンダリングします。
        - 引数: `template_path` (str, テンプレートファイルへのパス), `context` (dict, テンプレートに渡すデータ)
        - 戻り値: `str` (レンダリングされたテキスト)
- **src/generate_repo_list/url_utils.py**
    - `validate_url(url)`: URLが有効な形式であるかを検証します。
        - 引数: `url` (str)
        - 戻り値: `bool` (有効ならTrue, 無効ならFalse)

## 関数呼び出し階層ツリー
```
generate_repo_list.py (mainスクリプト)
├── parse_arguments()
├── config_manager.load_config()
├── repository_processor.fetch_all_repositories()
│   └── (GitHub API呼び出し)
└── repository_processor.process_repository_data() (各リポジトリに対してループ)
    ├── project_overview_fetcher.fetch_project_overview()
    │   └── (GitHub API呼び出し)
    ├── badge_generator.generate_badges()
    ├── language_info.get_language_statistics()
    │   └── (GitHub API呼び出し)
    └── (その他のデータ整形処理)
├── statistics_calculator.calculate_overall_statistics()
├── markdown_generator.generate_repo_list_markdown()
│   └── markdown_generator.generate_markdown_for_repository() (各リポジトリに対してループ)
│       └── template_processor.render_template()
└── (出力ファイルへの書き込み)

---
Generated at: 2026-01-05 07:06:15 JST
