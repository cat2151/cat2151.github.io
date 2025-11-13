Last updated: 2025-11-14

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、SEOに最適化されたコンテンツを効率的に作成します。
- 生成されたリポジトリ一覧を通じて、検索エンジンやAIからの情報発見を促進します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: 静的サイトジェネレーターとしてGitHub Pagesで使用され、生成されたMarkdownファイルを美しいウェブサイトとして公開します。
    - **Markdown**: リポジトリ一覧や各リポジトリ概要の記述に利用される軽量マークアップ言語です。
- 音楽・オーディオ: (このプロジェクトでは該当する技術はありません)
- 開発ツール:
    - **Python**: リポジトリ情報の取得、処理、Markdown生成の主要なスクリプト言語です。
    - **Pytest**: プロジェクトの機能が正しく動作するかを確認するためのテストフレームワークです。
    - **ruff**: Pythonコードのスタイルと品質を自動的にチェックし、修正するためのリンターおよびフォーマッターです。
- テスト:
    - **Pytest**: Pythonアプリケーションの単体テスト、統合テストを行うためのフレームワークです。
- ビルドツール:
    - (直接的なビルドツールは使用されていません。PythonスクリプトがMarkdownファイルを「生成」し、Jekyllがそれを静的サイトとしてビルドします。)
- 言語機能:
    - **Python**: スクリプトによる自動化とデータ処理の豊富なライブラリと機能を使用しています。
- 自動化・CI/CD:
    - **GitHub Actions**: (直接的なCI/CDは行われていませんが、生成されたGitHub PagesはGitHub Actionsによってデプロイされることが一般的です。)
- 開発標準:
    - **ruff**: コードベース全体で一貫したコーディングスタイルと品質を維持するために使用されます。
    - **.editorconfig**: 異なるエディタやIDEを使用する開発者間でのコードフォーマットを統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なる開発環境間でのコードスタイル（インデント、改行コードなど）を統一するための設定ファイル。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの概要、目的、機能、使い方、設定方法などを詳細に説明する主要なドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成や振る舞いを定義する設定ファイルで、GitHub Pagesの動作に影響します。
- **`assets/`**: ウェブサイトで使用されるファビコン、ロゴ、画像などの静的リソースを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのアイコン画像で、ブラウザのタブなどに表示されます。
- **`debug_project_overview.py`**: `project_overview_fetcher` モジュールのデバッグや単体テストを目的としたスクリプト。
- **`generated-docs/`**: 他のリポジトリから取得した「プロジェクト概要」などの生成済みドキュメントを一時的または恒久的に格納するためのディレクトリ。
- **`index.md`**: メインの出力ファイル。GitHub APIから取得・処理されたリポジトリ情報が整形されて格納され、GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを個別のMarkdownファイルとして記録するディレクトリです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイル。PWA (Progressive Web App) としてブラウザにインストールされる際の設定情報（アイコン、表示モードなど）を定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの動作に関する設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを記述したファイル。
- **`requirements.txt`**: 本番環境（このスクリプトが実行される環境）で必要となるPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのパスをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: `ruff`というPythonコードリンター・フォーマッターの設定ファイルで、コードスタイルのルールを定義します。
- **`src/`**: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空のファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成に関するモジュール群をまとめたPythonパッケージ。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`がPythonパッケージであることを示すファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例：アクティブ、アーカイブ）や言語を示すバッジのMarkdownを生成するロジックを扱います。
        - **`src/generate_repo_list/config.yml`**: プロジェクトの各種設定（プロジェクト概要取得機能のON/OFF、対象ファイルパスなど）を定義するYAML形式の設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml` や `secrets.toml` など、各種設定ファイルやシークレットを読み込み、管理する役割を担います。
        - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を統括します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEOのために利用されるJSON-LD形式の構造化データ（例：`WebPage`スキーマ）のテンプレートを定義します。
        - **`src/generate_repo_list/language_info.py`**: GitHub APIから取得したリポジトリの言語情報を処理し、表示に適した形式に整形する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理済みのリポジトリデータを受け取り、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成するコアモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 他のリポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）から、プロジェクト概要のテキストを自動的に取得・抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出し、整形する前処理を行うモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownファイルのSEOメタデータや、検索エンジン向けの追加情報に関するテンプレート設定を定義します。
        - **`src/generate_repo_list/statistics_calculator.py`**: 各リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、見出し、ボタンの文言などを一元的に管理するYAMLファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成で使用されるさまざまなテンプレート（例：リポジトリごとの表示形式）に変数を適用し、動的なコンテンツを生成します。
        - **`src/generate_repo_list/url_utils.py`**: GitHub APIのエンドポイントURLやリポジトリのURLなど、URLに関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能をテストするためのスクリプト。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`tests/test_config.py`**: 設定ファイル (`config.yml`, `secrets.toml` など) の読み込みや解析が正しく行われるかをテストします。
    - **`tests/test_environment.py`**: プロジェクトの実行環境が適切に設定されているか（例：必要な環境変数や依存関係）をテストします。
    - **`tests/test_integration.py`**: 複数のモジュールが連携して正しく機能するかを確認する統合テストが記述されています。
    - **`tests/test_markdown_generator.py`**: `markdown_generator.py` が期待通りのMarkdownコンテンツを生成するかをテストします。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` が正しくプロジェクト概要を抽出できるかをテストします。
    - **`tests/test_repository_processor.py`**: `repository_processor.py` がGitHub APIから取得したデータを適切に処理・整形できるかをテストします。

## 関数詳細説明
- **`generate_repo_list.py` 内の主要な関数**:
    - `main()`: このスクリプトのエントリーポイント。コマンドライン引数の解析、設定の読み込み、リポジトリ情報の取得、Markdownの生成、ファイルへの書き出しといった一連の処理フローを管理します。
    - `parse_arguments()`: コマンドラインから渡される引数（ユーザー名、出力ファイル名、制限数など）を解析し、プログラムで利用できる形式に変換します。
- **`repository_processor.py` 内の主要な関数**:
    - `fetch_repositories(username, token, limit)`: 指定されたGitHubユーザーのリポジトリ情報をGitHub API経由で取得します。オプションで取得するリポジトリ数を制限できます。
    - `process_repository_data(repo_data)`: GitHub APIから取得した個々のリポジトリの生データを受け取り、必要な情報（名前、説明、URL、言語など）を抽出・整形して返します。
- **`project_overview_fetcher.py` 内の主要な関数**:
    - `get_project_overview(repo_url, config)`: 指定されたリポジトリの特定パスにあるMarkdownファイルから「プロジェクト概要」セクションを読み込み、3行の要約を抽出して返します。API呼び出しのキャッシュやリトライ機能も内包します。
- **`markdown_generator.py` 内の主要な関数**:
    - `generate_markdown(repositories_info, config, strings)`: 処理済みのリポジトリ情報、設定、表示文言データを用いて、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成します。
- **`config_manager.py` 内の主要な関数**:
    - `load_config(config_path)`: 指定されたパスにあるYAML形式の設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書オブジェクトとして返します。
    - `load_secrets(secrets_path)`: 機密情報（例: GitHubトークン）を安全に管理するための`secrets.toml`ファイルを読み込みます。
- **`badge_generator.py` 内の主要な関数**:
    - `create_badge_markdown(status, language)`: リポジトリの状態（アクティブ、アーカイブなど）や使用されているプログラミング言語に基づいて、表示用のMarkdown形式のバッジ文字列を生成します。
- **`language_info.py` 内の主要な関数**:
    - `get_language_breakdown(repo_languages)`: リポジトリが使用しているプログラミング言語とその割合（GitHub APIから取得されるデータ）を分析し、人間が読みやすい形式に整形して返します。
- **`statistics_calculator.py` 内の主要な関数**:
    - `calculate_repo_statistics(repo_data)`: リポジトリのスター数、フォーク数、最終更新日などの各種統計データを計算し、集計します。
- **`template_processor.py` 内の主要な関数**:
    - `apply_template(template_content, data)`: Markdownテンプレートのプレースホルダーに実際のリポジトリデータなどを差し込み、動的なMarkdownコンテンツを生成します。
- **`url_utils.py` 内の主要な関数**:
    - `build_github_api_url(username)`: 特定のGitHubユーザーのリポジトリ情報を取得するためのGitHub APIのエンドポイントURLを構築します。
    - `build_repo_url(username, repo_name)`: 指定されたユーザーとリポジトリ名から、GitHub上のリポジトリへのURLを構築します。

## 関数呼び出し階層ツリー
```
（関数呼び出し階層の情報は提供されていませんでした。）

---
Generated at: 2025-11-14 07:06:37 JST
