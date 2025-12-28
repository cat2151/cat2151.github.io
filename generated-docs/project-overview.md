Last updated: 2025-12-29

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（`<username>.github.io`）用に、リポジトリ一覧ページを自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを自動出力します。
- 検索エンジンによるクロールを促進し、LLMがリポジトリを参照しやすくなることを目指します。

## 技術スタック
- フロントエンド: Jekyll, Markdown (GitHub Pagesサイトのコンテンツ記述とレンダリングに使用)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語), pytest (テストフレームワーク), Ruff (コードフォーマッター/リンター)
- テスト: pytest (ユニットテストおよび統合テストに使用)
- ビルドツール: なし (Pythonスクリプトによる生成が主な処理のため)
- 言語機能: Python (GitHub APIとの連携、ファイル操作、文字列処理などに使用)
- 自動化・CI/CD: GitHub Actions (リポジトリ情報の取得とMarkdown生成の自動化を想定)
- 開発標準: Ruff (コードスタイルの一貫性を保つためのルール), .editorconfig (エディタの設定統一)

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
- **README.md**: プロジェクトの目的、背景、機能、使い方、設定方法、開発者向けのヒント、ライセンス情報などを記述したメインドキュメント。
- **LICENSE**: プロジェクトのライセンス（MITライセンス）を定義するファイル。
- **_config.yml**: Jekyllサイトの全体設定ファイル。GitHub Pagesのレンダリングに使用される。
- **assets/**: Webサイトで使用される画像アセット（ファビコンなど）を格納するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧のMarkdownファイル。これがGitHub Pagesのトップページとして表示される。
- **issue-notes/**: 開発中の課題やメモをMarkdown形式で記録したファイル群を格納するディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を記述するJSONファイル。Webアプリとしてサイトをインストールする際の挙動を定義。
- **pytest.ini**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの実行オプションなどを指定。
- **requirements.txt**: プロジェクトの本番環境で必要なPythonパッケージをリストアップしたファイル。
- **requirements-dev.txt**: プロジェクトの開発・テスト環境で必要なPythonパッケージをリストアップしたファイル。
- **robots.txt**: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイル。
- **ruff.toml**: Pythonのコードリンター/フォーマッター `Ruff` の設定ファイル。コードスタイルや品質ルールを定義。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインスクリプト。
- **src/generate_repo_list/config.yml**: プロジェクトの実行時設定（例: `project_overview` 機能の有効/無効、対象ファイルパス、タイムアウトなど）を定義するYAMLファイル。
- **src/generate_repo_list/strings.yml**: UI表示メッセージ、ラベル、その他の静的テキストコンテンツを国際化対応できるように管理するYAMLファイル。
- **src/generate_repo_list/badge_generator.py**: リポジトリのステータス（例: アクティブ、アーカイブ）に応じたバッジのMarkdownを生成するロジックを含むファイル。
- **src/generate_repo_list/config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのユーティリティクラス/関数を提供するファイル。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジンのリッチリザルト表示を強化するためのJSON-LD形式の構造化データテンプレート。
- **src/generate_repo_list/language_info.py**: GitHubリポジトリの言語情報（使用言語、割合など）を処理・整形するロジックを含むファイル。
- **src/generate_repo_list/markdown_generator.py**: 取得・処理されたリポジトリ情報から、最終的なMarkdownコンテンツ（リポジトリ一覧のエントリや全体構造）を生成するロジックを含むファイル。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得する機能を提供するファイル。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを含むファイル。
- **src/generate_repo_list/seo_template.yml**: サイトのSEO（検索エンジン最適化）関連のメタデータや設定を定義するYAMLテンプレート。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリに関する各種統計情報（スター数、フォーク数など）を計算するロジックを含むファイル。
- **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレート（例: リポジトリごとの表示形式）の処理を管理するファイル。
- **src/generate_repo_list/url_utils.py**: GitHub APIのエンドポイントURLやリポジトリのWeb URLなどを構築するためのユーティリティ関数を提供するファイル。
- **tests/**: プロジェクトのテストスクリプトを格納するディレクトリ。各モジュールの単体テストや統合テストが含まれる。

## 関数詳細説明
- **generate_repo_list.py::main()**:
    - **役割**: スクリプトのエントリーポイント。コマンドライン引数をパースし、リポジトリ情報の取得、処理、Markdown生成、ファイル出力という一連のフローを orchestrate する。
    - **引数**: なし (内部で `argparse` を使用してコマンドライン引数を処理)。
    - **戻り値**: なし。
    - **機能**: GitHubユーザー名や出力ファイル名、処理リポジトリ数上限などのパラメータを解析し、それに基づいてリポジトリ一覧生成プロセスを開始します。
- **badge_generator.py::generate_badge(repo_status: str) -> str**:
    - **役割**: リポジトリのステータスに応じたバッジのMarkdown文字列を生成する。
    - **引数**: `repo_status` (str) - リポジトリの現在のステータス（例: 'active', 'archived', 'fork'）。
    - **戻り値**: バッジのMarkdown文字列。
    - **機能**: 特定のステータスを表すアイコンやテキストを含むMarkdown形式のバッジを作成します。
- **config_manager.py::load_config(file_path: str) -> dict**:
    - **役割**: YAML形式の設定ファイルを読み込み、辞書として返す。
    - **引数**: `file_path` (str) - 読み込む設定ファイルのパス。
    - **戻り値**: 設定内容を表す辞書。
    - **機能**: プロジェクトの設定（例: `config.yml`, `strings.yml`）をファイルからメモリにロードします。
- **markdown_generator.py::create_repository_entry(repo_data: dict, project_overview: str) -> str**:
    - **役割**: 個々のリポジトリデータとプロジェクト概要から、そのリポジトリのMarkdown表示用エントリを生成する。
    - **引数**: `repo_data` (dict) - 処理済みのリポジトリ情報。`project_overview` (str) - 取得したプロジェクト概要の3行説明。
    - **戻り値**: 特定のリポジトリに対応するMarkdown文字列。
    - **機能**: リポジトリ名、説明、言語、バッジ、プロジェクト概要などを組み合わせて、一覧表示用のMarkdownブロックを作成します。
- **markdown_generator.py::create_full_markdown(repo_entries: list[str]) -> str**:
    - **役割**: 個々のリポジトリエントリのリストを結合し、最終的なリポジトリ一覧ページのMarkdownコンテンツを生成する。
    - **引数**: `repo_entries` (list[str]) - 各リポジトリのMarkdownエントリ文字列のリスト。
    - **戻り値**: 完全なMarkdownページの文字列。
    - **機能**: すべてのリポジトリのエントリをヘッダーやフッターとともに連結し、GitHub Pagesで表示される最終的なMarkdownファイルを構築します。
- **project_overview_fetcher.py::fetch_project_overview(repo_name: str, config: dict) -> str**:
    - **役割**: 指定されたリポジトリ内の `project-overview.md` からプロジェクト概要の3行説明を抽出する。
    - **引数**: `repo_name` (str) - 対象となるリポジトリ名。`config` (dict) - `project_overview`機能に関する設定情報。
    - **戻り値**: 抽出されたプロジェクト概要の3行説明文字列、または空文字列。
    - **機能**: GitHub APIを使ってリポジトリ内の特定のファイルの内容を取得し、設定されたセクションタイトルに基づいて概要部分を解析します。
- **repository_processor.py::process_repository_data(raw_repo: dict, config: dict) -> dict**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に整形・加工する。
    - **引数**: `raw_repo` (dict) - GitHub APIから直接取得したリポジトリ情報。`config` (dict) - 処理設定。
    - **戻り値**: 整形されたリポジトリ情報辞書。
    - **機能**: 必要なフィールドの抽出、URLの生成、ステータスの決定、言語情報の解析などを行い、後続のMarkdown生成で使いやすいデータ構造に変換します。
- **url_utils.py::build_github_api_url(username: str, endpoint: str) -> str**:
    - **役割**: GitHub APIのエンドポイントURLを構築する。
    - **引数**: `username` (str) - GitHubユーザー名。`endpoint` (str) - APIの特定のエンドポイントパス。
    - **戻り値**: 完全なGitHub APIのURL文字列。
    - **機能**: ベースURLとユーザー名、エンドポイントを組み合わせて、APIリクエスト用のURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
```

---
Generated at: 2025-12-29 07:06:08 JST
