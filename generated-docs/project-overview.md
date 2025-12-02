Last updated: 2025-12-03

# Project Overview

## プロジェクト概要
- GitHub Pagesサイトのために、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- 各リポジトリの概要表示、バッジ付き分類、Jekyll/GitHub Pages対応などの機能を提供します。

## 技術スタック
- フロントエンド:
    - **GitHub Pages / Jekyll**: 生成されたMarkdownファイルが公開されるプラットフォームであり、JekyllはMarkdownをHTMLに変換する静的サイトジェネレータです。
    - **Markdown**: 生成されるコンテンツのフォーマットです。
- 音楽・オーディオ:
    - (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの主要なプログラミング言語であり、リポジトリ情報取得およびMarkdown生成スクリプトが実装されています。
    - **GitHub API**: リポジトリ情報（名前、説明、言語、星の数など）を取得するためのインターフェースです。
    - **Pytest**: Pythonアプリケーションのテストフレームワークであり、機能の正確性を検証するために使用されます。
    - **Ruff**: 高速なPythonリンターおよびフォーマッターで、コードの一貫性を保ち品質を向上させます。
- テスト:
    - **Pytest**: Pythonコードの単体テスト、結合テスト、およびインテグレーションテストを実行するためのフレームワークです。
- ビルドツール:
    - **Jekyll**: GitHub Pagesの基盤技術であり、生成されたMarkdownファイルを静的サイトとしてビルド・公開するために利用されます。
- 言語機能:
    - **Python言語機能**: ファイル操作、APIリクエスト、データ処理、文字列操作など、Pythonの標準的な機能が幅広く利用されています。
- 自動化・CI/CD:
    - **スクリプト実行**: `generate_repo_list.py`スクリプト自体がリポジトリ一覧生成プロセスを自動化します。
    - **依存関係管理**: `requirements.txt`と`requirements-dev.txt`により、プロジェクトの実行および開発に必要なPythonパッケージのバージョンを管理します。
- 開発標準:
    - **Ruff (.toml)**: コードスタイルの一貫性を強制し、潜在的な問題を検出するためのリンティングルールとフォーマット設定が記述されています。

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
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのインデント、行末文字、文字コードなどの基本設定を統一するためのファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。一時ファイルやログ、生成物などが含まれます。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法、開発者向け情報などを記述したメインのドキュメントファイルです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動や設定（テーマ、プラグイン、変数など）を制御するファイルです。
- **`assets/`**: GitHub Pagesサイトで利用される静的アセット（画像、アイコン、CSS、JavaScriptなど）を格納するディレクトリです。`favicon`ファイルが含まれます。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグやテストに特化したスクリプトであると推測されます。
- **`generated-docs/`**: 各リポジトリの概要が記述された`project-overview.md`ファイルなどが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: このシステムによって自動生成される、GitHubリポジトリ一覧のメインMarkdownファイルです。GitHub Pagesサイトのトップページとして表示されます。
- **`issue-notes/`**: プロジェクト開発中の課題やメモなどをMarkdown形式で記録しているディレクトリであると推測されます。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名称、アイコン、表示設定など）を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの検出方法や実行オプションなどが記述されます。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはクロールしてはならないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンターおよびフォーマッターである`ruff`の設定ファイルです。コードスタイルのルールや自動修正の設定などが記述されます。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージを示すためのファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能の実装を含むPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージを示すためのファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの状態（アーカイブ、アクティブなど）や言語に応じたバッジを生成するためのロジックを実装したモジュールです。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`といった各種設定ファイルを読み込み、管理するためのロジックを実装したモジュールです。
        - **`src/generate_repo_list/generate_repo_list.py`**: このシステムのメインスクリプトであり、GitHub APIからの情報取得、処理、Markdown生成、出力までの一連の処理を制御します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理、整形するためのロジックを実装したモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報から、GitHub Pages向けのMarkdown形式のコンテンツ（リポジトリ一覧など）を生成するロジックを実装したモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動的に取得・抽出するロジックを実装したモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を、表示に適した形に整形・分類・フィルタリングするなどの処理を行うロジックを実装したモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータや記述のテンプレートを定義するファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリ数や言語分布などの統計情報を計算するロジックを実装したモジュールです。
        - **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownやUI表示で使用される各種メッセージや文言を一元管理するための設定ファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成において、特定のテンプレート（例えばJekyllのレイアウト）を処理したり、プレースホルダーを実際のデータで置き換えたりするロジックを実装したモジュールです。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、バリデーションなど、URLに関連するユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`機能に特化したテストスクリプトであると推測されます。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストを行うモジュールです。
    - **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテストを行うモジュールです。
    - **`tests/test_integration.py`**: システムの異なるコンポーネント間、または外部APIとの連携を含む統合テストを行うモジュールです。
    - **`tests/test_markdown_generator.py`**: Markdown生成ロジックが期待通りに動作するかを検証するテストを行うモジュールです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの機能が正確に動作するかを検証するテストを行うモジュールです。
    - **`tests/test_repository_processor.py`**: リポジトリ情報の処理ロジックが正しく機能するかを検証するテストを行うモジュールです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細は分析できませんでしたが、各ファイルが持つ役割から、以下の様な関数群が含まれていると推測されます。

- **`badge_generator.py`**:
    - **役割**: リポジトリの属性（アーカイブ状態、使用言語など）に基づいて、視覚的なバッジ（例: アーカイブ済み、Python）の情報を生成または取得する関数群。
    - **機能**: 入力されたリポジトリデータから適切なバッジの種類を判断し、そのバッジのURLやマークアップを返す。
- **`config_manager.py`**:
    - **役割**: プロジェクトの設定ファイル（`config.yml`, `secrets.toml`など）の読み込み、解析、および値の取得を行う関数群。
    - **機能**: 指定されたパスから設定ファイルを読み込み、設定値をディクショナリやオブジェクトとして提供する。
- **`generate_repo_list.py`**:
    - **役割**: プロジェクトのエントリーポイントであり、リポジトリ一覧生成の全体フローを orchestrate するメイン関数。
    - **機能**: コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、情報の処理、Markdown生成モジュールの呼び出し、結果のファイル出力など、一連のタスクを実行する。
- **`language_info.py`**:
    - **役割**: プログラミング言語に関する情報を処理し、表示に適した形式に整形する関数群。
    - **機能**: GitHub APIから取得した言語情報を基に、言語名やその使用比率などを計算し、Markdown出力に利用可能な形式に変換する。
- **`markdown_generator.py`**:
    - **役割**: 処理されたリポジトリデータを受け取り、GitHub Pagesサイトで表示されるMarkdown形式のコンテンツを生成する関数群。
    - **機能**: リポジトリ一覧の構造を構築し、各リポジトリの詳細（名前、説明、リンク、バッジ、概要など）を埋め込んで最終的なMarkdown文字列を生成する。
- **`project_overview_fetcher.py`**:
    - **役割**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出する関数群。
    - **機能**: GitHub APIを通じてファイルの内容を取得し、指定されたセクション（例: `## プロジェクト概要`）から3行の要約テキストをパースして返す。
- **`repository_processor.py`**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーションのロジックで扱いやすい形式に変換し、必要なフィルタリングや分類を行う関数群。
    - **機能**: リポジトリのアーカイブ状態、フォークの有無、アクティブ/非アクティブの状態を判定し、表示順序を決定するための処理などを行う。
- **`statistics_calculator.py`**:
    - **役割**: リポジトリのリストに基づいて、合計リポジトリ数、使用言語の統計、スター数の合計などの集計データを計算する関数群。
    - **機能**: リポジトリ一覧のサマリーセクションなどに表示するための統計値を算出する。
- **`template_processor.py`**:
    - **役割**: MarkdownやHTMLのテンプレートに、実際のデータ（リポジトリ情報など）を挿入して最終的なコンテンツを生成する関数群。
    - **機能**: プレースホルダーを含むテンプレート文字列を受け取り、指定されたデータでそれらのプレースホルダーを置き換える。
- **`url_utils.py`**:
    - **役割**: URLの生成、検証、エンコード/デコードなど、URLに関連する汎用的なユーティリティ関数群。
    - **機能**: GitHubリポジトリのURL、GitHub PagesのURLなどを適切に構築する。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-03 07:06:07 JST
