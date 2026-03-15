Last updated: 2026-03-16

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ一覧を自動生成し表示するシステムです。
- GitHub APIを活用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを構築します。
- 各リポジトリの概要、分類、バッジなどを自動で表示し、検索エンジンやLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレータとして、GitHub Pagesサイトの最終的な表示コンテンツを生成する基盤技術です。)
- 音楽・オーディオ: (該当なし)
- 開発ツール:
    - pip: Pythonパッケージのインストールと管理に使用されるツールです。
    - pytest: Pythonで書かれたテストコードを実行するためのフレームワークです。
    - ruff: 高速なPythonリンターおよびフォーマッターで、コード品質の維持と統一されたコーディングスタイルを保証します。
- テスト: pytest (Pythonコードの単体テスト、統合テストの実行に使用されます。)
- ビルドツール: (該当なし - Pythonスクリプトがコンテンツ生成の主要な役割を担います。)
- 言語機能: Python (プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得からMarkdown生成まで一連の処理を実行します。)
- 自動化・CI/CD: GitHub Pages (生成されたMarkdownファイルをホスティングし、公開するためのプラットフォームであり、コンテンツのデプロイ自動化の側面を持ちます。)
- 開発標準: ruff (プロジェクト全体で統一されたコードスタイルと品質を維持するための静的解析ツールです。)

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
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
    - **.github_automation/check_large_files/scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: 本プロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイルです。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使用方法などを記述した主要なドキュメントファイルです。
- **_config.yml**: Jekyll静的サイトジェネレータの設定ファイルで、サイトの全体的な構成を定義します。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **assets/favicon-*.png**: ウェブサイトのブラウザタブやブックマークなどに表示されるファビコン画像です。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグや単体テストを行うためのスクリプトです。
- **generated-docs/**: 生成されたドキュメントや、他のリポジトリから取得されるプロジェクト概要ファイルの一時的な格納場所として利用されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するための認証用HTMLファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして機能し、生成されたリポジトリ一覧コンテンツがここに書き込まれます。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを記録するためのディレクトリです。
    - **issue-notes/22.md**: 特定の課題（ID: 22）に関する詳細なメモや議論が記述されたファイルです。
- **manifest.json**: Progressive Web App (PWA) の設定ファイルで、ホーム画面への追加、オフライン機能などを定義します。
- **pytest.ini**: pytestフレームワークの実行設定を定義するファイルです。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またどのページをクロールすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonコードリンター/フォーマッターである`ruff`の設定ファイルで、コーディングスタイルや規約を定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示す初期化ファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧を生成するための主要なロジックが格納されたPythonパッケージです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`パッケージであることを示す初期化ファイルです。
        - **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや情報に応じたMarkdown形式のバッジ（例: アクティブ、アーカイブ）を生成するモジュールです。
        - **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプトの実行に関する技術的な設定パラメータ（例: プロジェクト概要取得機能のON/OFF、タイムアウト時間）を定義するYAMLファイルです。
        - **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`など）を読み込み、管理するためのユーティリティモジュールです。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を特定のフォーマットに整形するための関数を提供するモジュールです。
        - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整・実行します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のためにWebページに構造化データ（JSON-LD形式）を追加するためのテンプレートファイルです。
        - **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・表示するためのモジュールです。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報から、GitHub Pagesで表示するためのMarkdownコンテンツを生成する主要モジュールです。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイルからプロジェクトの概要（3行説明など）を自動で取得・抽出するモジュールです。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出し、利用するモジュールです。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIを通じてリポジトリ情報を取得し、その生データを必要な形式に加工・整形するための主要な処理を行うモジュールです。
        - **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータや、検索エンジンからの視認性を高めるためのテンプレート設定を定義するYAMLファイルです。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するためのモジュールです。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を一元的に管理するためのYAMLファイルで、国際化（i18n）に対応しやすくします。
        - **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレートファイルに、動的にデータを埋め込み、最終的なコンテンツをレンダリングするモジュールです。
        - **src/generate_repo_list/url_utils.py**: URLの構築、検証、解析など、URLに関連するユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **tests/test_badge_generator_integration.py**: バッジ生成機能と他のモジュールとの連携が正しく行われるかを検証する統合テストです。
    - **tests/test_check_large_files.py**: 大容量ファイルチェック機能の正確性を検証するテストです。
    - **tests/test_config.py**: 設定ファイルの読み込みや管理ロジックの正確性を検証するテストです。
    - **tests/test_date_formatter.py**: 日付フォーマット機能が期待通りに動作するかを検証するテストです。
    - **tests/test_environment.py**: 実行環境の設定や依存関係が正しく構成されているかを検証するテストです。
    - **tests/test_integration.py**: システム全体の主要なフロー（リポジトリ取得からMarkdown生成まで）が正しく連携するかを検証する統合テストです。
    - **tests/test_markdown_generator.py**: Markdown生成モジュールの出力が期待通りであるかを検証するテストです。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要の取得機能が正しく動作するかを検証するテストです。
    - **tests/test_readme_badge_extractor.py**: READMEからのバッジ抽出機能の正確性を検証するテストです。
    - **tests/test_repository_processor.py**: リポジトリ情報の取得と加工ロジックの正確性を検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数の引数、戻り値、詳細な機能に関する具体的なコードレベルの情報が含まれていません。そのため、ファイル名とその役割から推測される主要な関数について、その一般的な役割を説明します。

- **src/generate_repo_list/generate_repo_list.py 内の主要関数**:
    - **main()**: プロジェクトのエントリーポイントとなる関数です。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ加工、Markdown生成、そして最終的なファイル出力までの一連のプロセスを統括します。
        - *役割*: プログラム全体の実行フローを制御する。
        - *引数*: プログラム実行時に渡されるコマンドライン引数（例: `--username`, `--output`, `--limit`）
        - *戻り値*: 処理の成功/失敗を示すステータスコード。
- **src/generate_repo_list/repository_processor.py 内の主要関数**:
    - **fetch_repositories(username)**: 指定されたGitHubユーザー名に紐づくリポジトリのリストをGitHub APIを通じて取得します。
        - *役割*: GitHub APIと連携し、リポジトリの生データを取得する。
        - *引数*: `username` (str): GitHubユーザー名。
        - *戻り値*: 取得したリポジトリデータのリスト。
    - **process_repository_data(repo_data)**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（名前、説明、言語など）を抽出し、整形します。
        - *役割*: リポジトリデータを標準化された形式に変換する。
        - *引数*: `repo_data` (dict): 個々のリポジトリの生のAPIレスポンスデータ。
        - *戻り値*: 整形されたリポジトリ情報を含む辞書。
- **src/generate_repo_list/project_overview_fetcher.py 内の主要関数**:
    - **fetch_project_overview(repo_url, config)**: 特定のリポジトリ（通常は対象ユーザーの他のリポジトリ）から、設定されたパス（例: `generated-docs/project-overview.md`）にあるファイルの内容を取得し、そこからプロジェクト概要の3行説明を抽出します。
        - *役割*: 外部リポジトリの特定のファイルから概要を抽出する。
        - *引数*: `repo_url` (str): 対象リポジトリのURL, `config` (dict): プロジェクト概要取得機能の設定。
        - *戻り値*: 抽出された3行のプロジェクト概要（文字列のリスト）。
- **src/generate_repo_list/markdown_generator.py 内の主要関数**:
    - **generate_repo_markdown(repo_info)**: 整形された個々のリポジトリ情報を受け取り、そのリポジトリを表示するためのMarkdown形式のスニペットを生成します。
        - *役割*: 単一リポジトリのMarkdownコンテンツを作成する。
        - *引数*: `repo_info` (dict): 整形されたリポジトリ情報。
        - *戻り値*: 生成されたMarkdown文字列。
    - **generate_index_markdown(all_repo_markdowns)**: 全てのリポジトリから生成されたMarkdownスニペットを結合し、最終的な`index.md`ファイルとして出力するコンテンツを生成します。
        - *役割*: 全リポジトリのMarkdownを結合し、最終出力を作成する。
        - *引数*: `all_repo_markdowns` (list): 各リポジトリのMarkdownスニペットのリスト。
        - *戻り値*: 最終的な`index.md`の内容となるMarkdown文字列。
- **src/generate_repo_list/config_manager.py 内の主要関数**:
    - **load_config(path)**: 指定されたファイルパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - *役割*: 設定ファイルを読み込む。
        - *引数*: `path` (str): 設定ファイルのパス。
        - *戻り値*: 設定内容を含む辞書。
- **src/generate_repo_list/date_formatter.py 内の主要関数**:
    - **format_date(iso_date)**: ISO 8601形式の日付文字列を受け取り、人間が読みやすい特定のフォーマットに変換して返します。
        - *役割*: 日付文字列を整形する。
        - *引数*: `iso_date` (str): ISO 8601形式の日付文字列。
        - *戻り値*: 整形された日付文字列。
- **src/generate_repo_list/url_utils.py 内の主要関数**:
    - **construct_github_api_url(username, endpoint)**: GitHub APIのベースURLと指定されたユーザー名、エンドポイントを組み合わせて、完全なAPIリクエストURLを構築します。
        - *役割*: GitHub APIリクエストURLを生成する。
        - *引数*: `username` (str): GitHubユーザー名, `endpoint` (str): APIエンドポイントパス。
        - *戻り値*: 完全なAPIリクエストURL文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。提供された情報には、具体的な関数の呼び出し関係を特定できるコードが含まれていません。

---
Generated at: 2026-03-16 07:09:02 JST
