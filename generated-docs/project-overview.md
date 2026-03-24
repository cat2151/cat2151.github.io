Last updated: 2026-03-25

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- 取得した情報に基づき、SEOに最適化されたGitHub Pages向けリポジトリ一覧をMarkdownで生成します。
- これにより、GitHub Pagesサイトの検索エンジン可視性を高め、リポジトリ参照を改善することを目指します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyllベース)** - GitHubが提供する静的サイトホスティングサービスで、MarkdownファイルをHTMLに変換してウェブサイトを構築します。本プロジェクトはこれに対応したMarkdownファイルを生成します。
- 音楽・オーディオ: 該当なし - このプロジェクトでは音楽やオーディオに関連する技術は使用されていません。
- 開発ツール: **Python** - リポジトリ情報の取得、解析、Markdown生成の中核ロジックを実装するために使用されるスクリプト言語です。
- テスト: **pytest** - Pythonで書かれた強力なテストフレームワークで、プロジェクトのコードの機能と品質を検証するために使用されます。
- ビルドツール: **Jekyll (GitHub Pages)** - 生成されたMarkdownファイルをHTMLとして公開するためにGitHub Pages内部で使用される静的サイトジェネレータです。本プロジェクトが直接実行するビルドツールではありません。
- 言語機能: **Python** - 高度なデータ構造、ファイルI/O、ネットワーク通信（GitHub API呼び出し）、テキスト処理などの豊富な機能が活用されています。
- 自動化・CI/CD: **`_github_automation` ディレクトリ** - GitHub Actionsなどの自動化スクリプトや設定を格納する可能性のあるディレクトリですが、プロジェクト全体としての継続的インテグレーション/デリバリーの具体的なパイプラインは明示されていません。
- 開発標準: **Ruff** - Pythonコードの高速なLinterおよびフォーマッターとして、コードスタイルの一貫性と品質を自動的に維持するために使用されます。**`.editorconfig`** - 異なるIDEやエディタ間でのコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタ間での一貫したコーディングスタイル（インデント、改行コードなど）を定義するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルがリポジトリに含まれていないかチェックする機能に関連するファイル群です。
        - **`README.md`**: `check_large_files` 機能に関する説明が記載されています。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定（しきい値など）を定義するファイルです。
        - **`scripts/check_large_files.py`**: 実際に大容量ファイルを検出するPythonスクリプトです。
- **`.gitignore`**: Gitによってバージョン管理されるべきでないファイルやディレクトリ（例: 実行時に生成されるファイル、一時ファイル、依存関係のディレクトリなど）を指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定、開発者向けヒントなどが記述されたメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の設定ファイルです。GitHub Pagesの振る舞いやサイトのメタ情報などを定義します。
- **`assets/`**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストに使用されるPythonスクリプトであると推測されます。
- **`generated-docs/`**: プロジェクトによって自動生成されたドキュメントを格納するためのプレースホルダーディレクトリ、または特定のドキュメントを期待する場所として機能します。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されたファイルです。内容はGoogleが指定した短いHTMLコードのみです。
- **`index.md`**: 生成されたリポジトリ一覧のメイン出力ファイルとなるMarkdownファイルです。このファイルがGitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: 課題やノート（メモ）を保存するためのディレクトリです。
    - **`22.md`**: 特定の課題またはメモをMarkdown形式で記述したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの表示方法や動作に関するメタデータを定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。テストの実行方法や検出ルールなどを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonの依存パッケージとそのバージョンを記述したファイルです。
- **`requirements.txt`**: 本番環境で必要となるPythonの依存パッケージとそのバージョンを記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Ruff linter/formatterの設定ファイルです。コードスタイルのルールや自動修正のオプションなどを定義します。
- **`src/`**: プロジェクトのソースコードを格納するメインディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の中核をなすPythonモジュール群を格納するディレクトリです。
        - **`__init__.py`**: `generate_repo_list`がPythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの各種ステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを含むファイルです。
        - **`config.yml`**: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを含むファイルです。
        - **`date_formatter.py`**: 日付や時刻のフォーマットを処理するためのユーティリティ関数を含むファイルです。
        - **`generate_repo_list.py`**: メインの実行スクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールを呼び出して最終的なMarkdownを生成します。
        - **`json_ld_template.json`**: JSON-LD形式の構造化データテンプレートです。SEOのためにリポジトリ情報にメタデータを付与する際に使用されます。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理・整形するためのロジックを含むファイルです。
        - **`markdown_generator.py`**: 取得したリポジトリ情報から、最終的なMarkdownコンテンツを生成する主要なロジックを含むファイルです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得するロジックを含むファイルです。
        - **`readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報などを抽出するロジックを含むファイルです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形・加工するロジックを含むファイルです。
        - **`seo_template.yml`**: SEO関連のメタデータや構造化データに関する設定、またはテンプレートを定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計するロジックを含むファイルです。
        - **`strings.yml`**: UIに表示されるメッセージや文言、ラベルなどを一元管理するための設定ファイルです。
        - **`template_processor.py`**: Markdown生成に使用されるテンプレートファイルの読み込みや変数置換などを処理するロジックを含むファイルです。
        - **`url_utils.py`**: URLの操作や検証、生成に関するユーティリティ関数を含むファイルです。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関するテストケースを記述したPythonスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
    - **`test_config.py`**: 設定ファイル読み込み・管理に関するテストを記述したファイルです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストを記述したファイルです。
    - **`test_environment.py`**: 実行環境に関するテストを記述したファイルです。
    - **`test_integration.py`**: システム全体の統合テストを記述したファイルです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを記述したファイルです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストを記述したファイルです。

## 関数詳細説明
- **`generate_repo_list.py` 内の主要関数**:
    - `main()`: このスクリプトのエントリーポイントとして機能し、コマンドライン引数の解析、GitHub APIからのリポジトリ情報の取得、取得したデータの処理、および最終的なMarkdownファイルの生成という一連のプロセスを調整します。
- **`config_manager.py` 内の主要関数**:
    - `load_config(filepath)`: 指定されたファイルパスからYAML形式の設定ファイルを読み込み、その内容をプログラムが利用できる形式（例: 辞書）で返します。
- **`project_overview_fetcher.py` 内の主要関数**:
    - `fetch_project_overview(repo_url, target_file, section_title)`: 特定のリポジトリ（`repo_url`）内の指定されたファイル（`target_file`）から、特定のセクションタイトル（`section_title`）に続くプロジェクト概要の3行説明を抽出し、文字列として返します。
- **`markdown_generator.py` 内の主要関数**:
    - `generate_repository_list_markdown(repositories_data)`: 処理済みのリポジトリデータのリストを受け取り、それらの情報をもとに、GitHub Pagesで表示するのに適したMarkdown形式のリポジトリ一覧文字列を生成します。
- **`repository_processor.py` 内の主要関数**:
    - `process_repository_data(raw_repo_data)`: GitHub APIから取得した生のリポジトリデータを入力として受け取り、表示に必要な情報を抽出、変換、整形して、後続の処理に適した構造化されたデータ形式で返します。
- **`badge_generator.py` 内の主要関数**:
    - `generate_badge(badge_type, value)`: 指定されたバッジの種類（例: 言語、ステータス）と対応する値に基づいて、GitHub Pagesに表示可能なバッジのMarkdownまたはURL文字列を生成します。
- **`date_formatter.py` 内の主要関数**:
    - `format_date(datetime_obj)`: 日付と時刻を表すオブジェクトを受け取り、指定された書式（例: `YYYY-MM-DD`）で人間が読みやすい日付文字列に変換して返します。
- **`statistics_calculator.py` 内の主要関数**:
    - `calculate_repository_stats(repo_data)`: リポジトリのデータを受け取り、スター数、フォーク数、最終更新日などの関連する統計情報を計算または集計して返します。
- **`template_processor.py` 内の主要関数**:
    - `render_template(template_path, context)`: 指定されたテンプレートファイル（`template_path`）と、テンプレート内で置き換えられるデータ（`context`）を使用して、最終的な出力文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-25 07:11:40 JST
