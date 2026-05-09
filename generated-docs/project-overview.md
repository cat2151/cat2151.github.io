Last updated: 2026-05-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得します。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧をMarkdownで生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照精度向上を目指します。

## 技術スタック
- フロントエンド:
  - Jekyll: GitHub Pagesの静的サイトジェネレーターとして、生成されたMarkdownファイルをHTMLに変換し表示するために利用されます。
  - Markdown: プロジェクトが自動生成するコンテンツの形式であり、JekyllによってGitHub Pages上でレンダリングされます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
  - Python: プロジェクトの主要な開発言語であり、GitHub APIからの情報取得、データの加工、Markdownファイルの生成など、システムの中核を担っています。
  - GitHub API: リポジトリ情報（名前、説明、言語、スター数など）を取得するための主要な外部インターフェースです。
- テスト:
  - Pytest: Pythonで書かれたテストコードを実行するためのフレームワークです。プロジェクトの機能が期待通りに動作するかを検証します。
- ビルドツール:
  - Pythonスクリプト: `generate_repo_list.py` を中心とするPythonスクリプト群が、GitHub APIから取得した情報に基づき、最終的なMarkdownファイルを生成（ビルド）します。
- 言語機能:
  - Python: 高レベルなプログラミング言語であり、データ処理、API通信、ファイル操作など、本システムの多様なロジックを実装するために使用されています。
- 自動化・CI/CD:
  - (本プロジェクト自体はCI/CD不要のローカル開発重視とされていますが、GitHub APIを利用した自動生成システムとして、以下の技術が自動化に寄与します。)
  - GitHub API: リポジトリ情報の自動取得によるコンテンツ自動生成の基盤です。
- 開発標準:
  - Ruff: Pythonコードのリンティングとフォーマットを自動的に実行し、コード品質と一貫性を保つためのツールです。
  - EditorConfig: 異なるIDEやエディタ間でコードの書式設定（インデント、改行コードなど）を統一するための設定ファイルです。

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
- **.editorconfig**: 異なる開発環境（IDEやテキストエディタ）間で、インデントスタイル、文字コード、改行コードなどのコードフォーマット設定を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや、それに関連する設定ファイルを格納するためのディレクトリです。
  - **.github_automation/check_large_files/README.md**: `check_large_files` 機能に関する説明や使用方法が記述されているドキュメントファイルです。
  - **.github_automation/check_large_files/check-large-files.toml**: リポジトリ内の大容量ファイルをチェックするための設定ファイルです。チェック対象や閾値などを定義します。
  - **.github_automation/check_large_files/scripts/check_large_files.py**: GitHubリポジトリ内の指定されたサイズを超えるファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitのバージョン管理から除外すべきファイルやディレクトリのパターンを記述する設定ファイルです。一時ファイルやビルド成果物などが指定されます。
- **LICENSE**: プロジェクトのライセンス情報（本プロジェクトではMITライセンス）が記述されているファイルです。著作権表示や利用条件が記載されます。
- **README.md**: プロジェクトの概要、目的、主な機能、インストール方法、使用方法、貢献方法など、プロジェクトに関する最も基本的な情報を提供するメインドキュメントファイルです。
- **_config.yml**: Jekyllサイト全体の挙動を設定するためのYAML形式の設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットファイルを格納するディレクトリです。
  - **assets/favicon-16x16.png**, **assets/favicon-192x192.png**, **assets/favicon-32x32.png**, **assets/favicon-512x512.png**: Webサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）として使用される、様々な解像度の画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグや、プロジェクト概要取得機能の単体テストを補助するために使用される可能性のあるPythonスクリプトです。
- **generated-docs/**: プロジェクトの実行によって自動的に生成されるドキュメントやコンテンツファイルを格納するためのディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールで、サイトの所有権を確認するために配置されるHTMLファイルです。特定のユニークな文字列を含みます。
- **index.md**: GitHub Pagesサイトのルートに配置されるMarkdownファイルであり、本システムによって生成されたリポジトリ一覧のコンテンツが書き込まれ、サイトのトップページとして機能します。
- **issue-notes/**: プロジェクトの課題、バグ、機能要望などに関するメモや詳細情報を格納するディレクトリです。
  - **issue-notes/22.md**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモ、調査結果、解決策などが記述されているMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を記述するJSONファイルです。アプリ名、アイコン、表示モード、起動URLなど、PWAのメタデータを定義します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイルです。テストファイルの発見パターン、プラグイン、マーカーなどの実行オプションを定義します。
- **requirements-dev.txt**: 開発環境やテスト環境でのみ必要となるPythonパッケージの依存関係を記述するファイルです。`pytest`や`ruff`などが含まれます。
- **requirements.txt**: 本番環境でプロジェクトを実行するために最低限必要となるPythonパッケージの依存関係を記述するファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、ウェブサイトのどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンティングとフォーマットツールである`ruff`の設定ファイルです。コードスタイルガイド、検出するエラー、自動修正ルールなどを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
  - **src/__init__.py**: Pythonのパッケージとして`src`ディレクトリを認識させるための空ファイルです。
  - **src/generate_repo_list/**: GitHubリポジトリ一覧生成機能に関連するすべてのモジュールを格納するPythonパッケージです。
    - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるための空ファイルです。
    - **src/generate_repo_list/badge_generator.py**: リポジトリの使用言語やステータスを示すSVG形式のバッジを生成するためのロジックを提供するPythonモジュールです。
    - **src/generate_repo_list/config.yml**: `generate_repo_list`機能固有の実行時設定（例: プロジェクト概要機能の有効/無効、対象ファイルパス、タイムアウト設定）を定義するYAMLファイルです。
    - **src/generate_repo_list/config_manager.py**: 複数の設定ファイル（例: `config.yml`, `secrets.toml`）を読み込み、アプリケーション全体で利用可能な設定オブジェクトとして管理するPythonモジュールです。
    - **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付や時刻の情報を、人間が読みやすい形式（例: "YYYY年MM月DD日"）に整形するユーティリティ関数を提供するPythonモジュールです。
    - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインエントリスクリプトであり、GitHub APIからリポジトリ情報を取得し、加工、Markdown生成までの一連の処理をオーケストレーションします。
    - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のために、リポジトリ情報からJSON-LD形式の構造化データを生成するためのテンプレートを定義するJSONファイルです。
    - **src/generate_repo_list/language_info.py**: リポジトリの使用言語に関する詳細情報（例: 言語名、色コード、関連URL）を管理し、取得するPythonモジュールです。
    - **src/generate_repo_list/markdown_generator.py**: 処理済みのリポジトリデータを受け取り、GitHub Pages向けの整形されたMarkdownコンテンツを生成するロジックを提供するPythonモジュールです。
    - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明テキストを抽出する機能を提供するPythonモジュールです。
    - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、特定の形式で記述されたバッジ情報（例: ビルドステータス、カバレッジ）を抽出するPythonモジュールです。
    - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、整形、フィルタリング、追加情報の付与などを行い、Markdown生成に適したデータ構造に変換するPythonモジュールです。
    - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化 (SEO) に関するメタデータやキーワード、説明文などのテンプレートを定義するYAMLファイルです。
    - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するためのPythonモジュールです。
    - **src/generate_repo_list/strings.yml**: UI表示メッセージ、ラベル、案内文など、アプリケーション内で使用される各種テキスト文字列を一元的に管理するためのYAMLファイルです。多言語対応にも利用されます。
    - **src/generate_repo_list/template_processor.py**: Markdown生成のために、Jinja2などのテンプレートエンジンを用いて、リポジトリデータとテンプレートファイルを結合し、最終的な出力テキストを生成するPythonモジュールです。
    - **src/generate_repo_list/url_utils.py**: GitHubリポジトリのURL、APIエンドポイント、各リポジトリのGitHub Pagesへのリンクなど、URLに関連するユーティリティ関数（生成、解析、検証など）を提供するPythonモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`モジュールなど、プロジェクト概要取得機能のテストコードを記述したファイルです。
- **tests/**: プロジェクト全体の単体テスト、統合テスト、E2Eテストなどのテストコードを格納するためのディレクトリです。
  - **tests/conftest.py**: `pytest`フレームワークでテスト実行時に自動的に検出される共通のフィクスチャ、フック、ヘルパー関数などを定義するファイルです。
  - **tests/test_badge_generator_integration.py**: `badge_generator`モジュールが他のコンポーネントと正しく連携するかどうかを検証する統合テストコードです。
  - **tests/test_check_large_files.py**: `.github_automation/check_large_files.py`スクリプトの機能を検証するためのテストコードです。
  - **tests/test_config.py**: `config_manager`モジュールや設定ファイルの読み込み、パースが正しく行われるかを検証するテストコードです。
  - **tests/test_date_formatter.py**: `date_formatter`モジュールが正しく日付の整形を行うかを検証するテストコードです。
  - **tests/test_environment.py**: プロジェクトの実行環境（依存関係、設定など）が正しくセットアップされているかを検証するテストコードです。
  - **tests/test_integration.py**: `generate_repo_list`スクリプトの主要な処理フロー全体が期待通りに動作するかを検証する統合テストコードです。
  - **tests/test_markdown_generator.py**: `markdown_generator`モジュールがリポジトリデータから正しくMarkdownを生成するかを検証するテストコードです。
  - **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが正しくプロジェクト概要を抽出できるかを検証するテストコードです。
  - **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEファイルからバッジ情報を正しく抽出できるかを検証するテストコードです。
  - **tests/test_repository_processor.py**: `repository_processor`モジュールがGitHub APIから取得したリポジトリデータを正しく処理・整形するかを検証するテストコードです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細は特定できません。以下は各モジュールが提供すると想定される主要な機能の例です。

- **src/generate_repo_list/badge_generator.py**:
  - `generate_repo_badge()`: リポジトリの属性（例: 言語、スター数、最終更新日など）に基づいて、Markdown形式で表示されるバッジ文字列を生成します。
    - 役割: リポジトリ情報を視覚的に表現するバッジを作成。
    - 引数: (詳細不明、リポジトリデータの一部や特定の属性が想定されます)
    - 戻り値: (詳細不明、Markdown形式のバッジ文字列が想定されます)

- **src/generate_repo_list/config_manager.py**:
  - `load_config(config_path: str) -> dict`: 指定されたパスから設定ファイル（例: YAML, TOML）を読み込み、辞書形式で設定値を提供します。
    - 役割: アプリケーションの設定を一元的に管理し、アクセス可能にする。
    - 引数: `config_path` (string): 設定ファイルのパス。
    - 戻り値: (dict) 読み込まれた設定データ。

- **src/generate_repo_list/date_formatter.py**:
  - `format_date_human_readable(date_str: str) -> str`: GitHub APIから取得した日付文字列を、人間が読みやすい形式（例: "YYYY年MM月DD日"）に整形します。
    - 役割: 日付情報をユーザーフレンドリーな形式に変換。
    - 引数: `date_str` (string): APIから取得した日付の文字列。
    - 戻り値: (string) 整形された日付文字列。

- **src/generate_repo_list/generate_repo_list.py**:
  - `main()`: プロジェクトの主要なエントリポイントであり、コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データ処理、最終的なMarkdownファイルへの出力という一連の処理をオーケストレーションします。
    - 役割: アプリケーション全体の実行フローを管理。
    - 引数: (詳細不明、コマンドライン引数が想定されます)
    - 戻り値: (詳細不明、通常はNone)

- **src/generate_repo_list/markdown_generator.py**:
  - `generate_repository_markdown(repo_data: dict, config: dict) -> str`: 処理済みのリポジトリデータと設定に基づき、個々のリポジトリの情報を表すMarkdownコンテンツを生成します。
    - 役割: リポジトリデータをWebページ表示用のMarkdown形式に変換。
    - 引数: `repo_data` (dict): 処理済みのリポジトリ情報, `config` (dict): アプリケーション設定。
    - 戻り値: (string) 生成されたMarkdownコンテンツ。

- **src/generate_repo_list/project_overview_fetcher.py**:
  - `fetch_project_overview(owner: str, repo_name: str, config: dict) -> str`: 指定されたGitHubリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要説明を抽出します。
    - 役割: 各リポジトリの概要情報を取得。
    - 引数: `owner` (string): リポジトリの所有者名, `repo_name` (string): リポジトリ名, `config` (dict): アプリケーション設定。
    - 戻り値: (string) 抽出されたプロジェクト概要テキスト、または空文字列。

- **src/generate_repo_list/repository_processor.py**:
  - `process_repository_data(raw_repo_data: dict, config: dict) -> dict`: GitHub APIから取得した生のリポジトリデータを受け取り、整形、フィルタリング、必要な追加情報の付与などを行い、後のMarkdown生成に適した形式に加工します。
    - 役割: リポジトリの生データを整理・加工。
    - 引数: `raw_repo_data` (dict): GitHub APIからの生データ, `config` (dict): アプリケーション設定。
    - 戻り値: (dict) 処理済みのリポジトリデータ。

## 関数呼び出し階層ツリー
```
関数間の呼び出し階層は、提供された情報からは分析できませんでした。

---
Generated at: 2026-05-10 07:18:38 JST
