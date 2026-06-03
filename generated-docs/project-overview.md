Last updated: 2026-06-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得してMarkdown形式のリポジトリ一覧を生成します。
- 生成された一覧はJekyllベースのGitHub Pagesサイトに最適化され、検索エンジンやLLMからの参照性を高めます。
- 各リポジトリの概要、バッジ、言語、アクティビティを魅力的に表示し、訪問者がプロジェクトを容易に発見・理解できるよう支援します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesサイトの静的コンテンツを生成・表示するためのエンジンです。本プロジェクトが生成するMarkdownファイルをHTMLに変換し、Webサイトとして公開します。
- 音楽・オーディオ: 該当なし。
- 開発ツール:
    - Pytest: Pythonアプリケーションの機能が意図通りに動作するかを検証するためのテストフレームワークです。
    - Ruff: 高速なPythonリンターおよびフォーマッターで、コードの品質と一貫性を自動的に保つために使用されます。
    - requests: PythonからHTTPリクエストを行うためのライブラリで、GitHub APIとの通信に使用されます。
    - PyYAML, toml: 設定ファイル（YAML形式やTOML形式）の読み込みと管理に利用されます。
- テスト:
    - Pytest: ユニットテスト、統合テストなど、コードの信頼性を確保するためのテストを実行します。
- ビルドツール:
    - Pythonスクリプト群: GitHub APIからの情報取得、データの処理、最終的なMarkdownファイルの生成といった、コンテンツ生成の中核を担うスクリプト群です。
- 言語機能:
    - Python: プロジェクトの主要な開発言語であり、API連携、データ処理、ファイルI/Oなど、多岐にわたる処理に利用されています。
- 自動化・CI/CD:
    - .github_automation/scripts/check_large_files.py: GitHub Actionsなどで利用され得る、リポジトリ内の大容量ファイルをチェックする自動化スクリプトです。
- 開発標準:
    - Ruff: コードの整形と静的解析により、コード規約の強制と品質向上を支援します。
    - .editorconfig: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。

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
- **.editorconfig**: 開発環境における統一されたコーディングスタイル（インデント、改行コードなど）を定義する設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **check_large_files/README.md**: 大容量ファイルチェックツール`check_large_files.py`に関する説明ドキュメントです。
    - **check-large-files.toml**: 大容量ファイルチェックツールの設定ファイルで、チェック対象や閾値などを定義します。
    - **scripts/check_large_files.py**: リポジトリ内の大容量ファイルを特定し、レポートするためのPythonスクリプトです。
- **.gitignore**: Gitのバージョン管理システムが追跡しないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトの利用条件を定めるライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの概要、目的、主な機能、使い方、設定方法などを説明する主要なドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成や挙動を定義する設定ファイルです。
- **assets/**: Webサイトで使用される画像、ファビコン、その他の静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのブラウザタブやブックマークなどに表示される様々なサイズのファビコン画像です。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグやテストを目的としたスクリプトです。
- **generated-docs/**: プロジェクトによって生成されたドキュメントや、参照元となるドキュメント（例: 各リポジトリの`project-overview.md`）が格納される可能性があるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。本プロジェクトによってリポジトリ一覧のコンテンツがこのファイルに生成・出力されます。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを格納するためのディレクトリです。
    - **22.md**: 特定の課題（Issue #22など）に関する詳細なメモや考察が記述されたファイルです。
- **manifest.json**: Webアプリケーションマニフェストファイルで、プログレッシブウェブアプリ（PWA）としての設定（アプリ名、アイコン、表示モードなど）を定義します。
- **pytest.ini**: Pytestテストフレームワークの構成設定ファイルで、テストの実行オプションやパスなどを指定します。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **requirements.txt**: このスクリプトを本番環境で実行する際に必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしても良いか、またはクロールしてはいけないかを指示するファイルです。
- **ruff.toml**: `ruff`リンターおよびフォーマッターの設定ファイルで、Pythonコードの静的解析ルールや整形ルールを定義します。
- **src/**: プロジェクトの主要なPythonソースコードを格納するルートディレクトリです。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成に関連するPythonモジュールやスクリプトを格納するパッケージです。
        - **__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリの言語やステータスなどを示すバッジ画像を生成するためのロジックを含みます。
        - **config.yml**: リポジトリ一覧生成スクリプトの技術的な動作パラメータや設定を定義するYAML形式のファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プロジェクト内で利用可能な形式で管理するためのモジュールです。
        - **date_formatter.py**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するための機能を提供します。
        - **generate_repo_list.py**: プロジェクトの中核となるスクリプトで、GitHub APIから情報を取得し、Markdownファイルを生成するメインの処理ロジックを実行します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD）を生成する際のテンプレートファイルです。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に利用するための機能を提供します。
        - **markdown_generator.py**: 取得および処理されたリポジトリ情報から、最終的なMarkdown形式のコンテンツを生成するモジュールです。
        - **project_overview_fetcher.py**: 各リポジトリに存在する`generated-docs/project-overview.md`ファイルから、プロジェクトの3行概要を自動的に抽出・取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、ライセンス）を抽出する機能です。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換する主要な処理を行います。
        - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやページ固有の設定を定義するテンプレートファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIに表示される各種メッセージや文言を一元的に管理するためのYAML形式のファイルです。
        - **template_processor.py**: Markdown生成の際に利用するテンプレートファイルの内容を読み込み、データに基づいてレンダリングする機能を提供します。
        - **url_utils.py**: GitHub APIのエンドポイントURLの構築や、その他のURL関連の処理を行うためのユーティリティ関数を集めたモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのユニットテストファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **conftest.py**: Pytestのテストフィクスチャ（テスト環境の準備・後処理）や共通ヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールが他のコンポーネントと連携して正しく動作するかを検証する統合テストです。
    - **test_check_large_files.py**: 大容量ファイルチェックスクリプト`check_large_files.py`の機能が正しく動作するかを検証するテストです。
    - **test_config.py**: 設定ファイル（`config.yml`など）の読み込み、解析、および管理機能のテストです。
    - **test_date_formatter.py**: 日付整形機能`date_formatter.py`の各種フォーマットが正しく適用されるかを検証するテストです。
    - **test_environment.py**: プロジェクトの実行環境や依存関係が正しく設定されているかを検証するテストです。
    - **test_integration.py**: プロジェクトの主要なエンドツーエンドのフローが正しく動作するかを検証する統合テストです。
    - **test_markdown_generator.py**: Markdown生成機能`markdown_generator.py`が正しくMarkdownコンテンツを生成するかを検証するテストです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが`project-overview.md`から正確に概要を抽出できるかを検証するテストです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正しく抽出できるかを検証するテストです。
    - **test_repository_processor.py**: リポジトリデータ処理機能`repository_processor.py`がGitHub APIからのデータを正しく整形できるかを検証するテストです。

## 関数詳細説明
提供された情報から具体的な関数リストは得られませんでしたが、主要なファイルに基づいて予想される重要な関数の役割を説明します。

- **generate_repo_list.py 内の主要関数**:
    - `main()`: このスクリプトのエントリーポイントです。コマンドライン引数の解析、GitHub APIからのデータ取得、リポジトリ情報の処理、Markdownコンテンツの生成、そしてファイルへの書き出しといった一連のプロセスをオーケストレートします。引数はありません。
- **config_manager.py 内の主要関数**:
    - `load_config(filepath: str) -> dict`: 指定されたパスにあるYAML形式の設定ファイルを読み込み、辞書としてその内容を返します。
- **project_overview_fetcher.py 内の主要関数**:
    - `fetch_project_overview(owner: str, repo_name: str, config: dict) -> str`: 特定のリポジトリ（`owner`/`repo_name`）から`generated-docs/project-overview.md`ファイルを取得し、設定（`config`）に基づきその中からプロジェクトの3行概要を抽出して文字列として返します。
- **markdown_generator.py 内の主要関数**:
    - `generate_markdown(repo_data: list, template: str) -> str`: 処理済みのリポジトリデータ（`repo_data`）とMarkdownテンプレート（`template`）を使用して、最終的なリポジトリ一覧のMarkdownコンテンツ文字列を生成します。
- **repository_processor.py 内の主要関数**:
    - `process_repository_data(raw_repos: list, config: dict) -> list`: GitHub APIから取得した生のリポジトリデータ（`raw_repos`）を、設定（`config`）に従って整形し、表示に適した構造化されたリポジトリデータリストとして返します。
- **badge_generator.py 内の主要関数**:
    - `create_language_badge(language: str) -> str`: 指定されたプログラミング言語（`language`）に対応する、リポジトリ表示用のバッジのMarkdownまたはHTML文字列を生成します。
- **date_formatter.py 内の主要関数**:
    - `format_date(datetime_obj: datetime, format_string: str) -> str`: Pythonの`datetime`オブジェクト（`datetime_obj`）を指定されたフォーマット文字列（`format_string`）で整形し、人間が読みやすい日付文字列を返します。
- **url_utils.py 内の主要関数**:
    - `build_github_api_url(username: str, endpoint: str = "") -> str`: 指定されたGitHubユーザー名（`username`）とAPIエンドポイント（`endpoint`）に基づいて、GitHub APIにアクセスするための完全なURL文字列を構築して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は提供された情報からは分析できませんでした。

---
Generated at: 2026-06-04 07:45:54 JST
