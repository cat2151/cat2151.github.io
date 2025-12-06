Last updated: 2025-12-07

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、リポジトリ情報からSEO最適化されたMarkdownファイルを自動生成します。
- これにより、GitHub Pagesを通じてリポジトリの検索エンジンからの発見性とLLMによる参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として、生成されたMarkdownファイルをレンダリングするために間接的に利用されます), Markdown (生成されるリポジトリ一覧の出力形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: GitHub API (リポジトリ情報取得のデータソース), Pytest (テストフレームワーク), Ruff (コードリンターおよびフォーマッター), Python (主要な開発言語およびスクリプト実行環境)
- テスト: Pytest (Pythonコードの単体テストおよび統合テストに使用されるテストフレームワーク)
- ビルドツール: Python (スクリプトの実行環境として機能), YAML (設定ファイルの定義に使用)
- 言語機能: Python (プロジェクトの主要な開発言語)
- 自動化・CI/CD: GitHub Actions (生成されたMarkdownファイルをGitHub Pagesにデプロイする際のワークフローを想定していますが、本システム自体はCI/CDツールではありません)
- 開発標準: Ruff (コードの品質と一貫性を保つための自動修正およびリンティングツール)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を一貫させるための設定ファイル。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などを説明するメインのドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: サイトで使用されるファビコン（`favicon-*.png`）などの静的アセットを格納するディレクトリ。
- **`debug_project_overview.py`**: `project_overview` 機能のデバッグに使用されるスクリプト。
- **`generated-docs/`**: 他のリポジトリから取得した `project-overview.md` など、自動生成されたドキュメントを一時的に格納する可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるファイル。
- **`index.md`**: プロジェクトによって生成されるメインのリポジトリ一覧Markdownファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項をMarkdown形式で記録したファイル群。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示モードなど）を定義するファイル。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境でのみ必要となるPythonパッケージのリスト。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonパッケージのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールして良いか、またはクロールしてはいけないかを指示するファイル。
- **`ruff.toml`**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルルールを定義します。
- **`src/`**: プロジェクトのソースコードを格納するメインディレクトリ。
    - **`__init__.py`**: Pythonパッケージを示すためのファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成に関するコアロジックを格納するパッケージ。
        - **`__init__.py`**: Pythonサブパッケージを示すためのファイル。
        - **`badge_generator.py`**: リポジトリのステータスに応じたバッジを生成するロジックを扱うファイル。
        - **`config.yml`**: `project_overview` 機能など、プロジェクトの技術的パラメータを設定するファイル。
        - **`config_manager.py`**: 設定ファイル（`config.yml`, `strings.yml` など）の読み込みと管理を行うモジュール。
        - **`generate_repo_list.py`**: このプロジェクトの主要なエントリーポイント。リポジトリ情報の取得、処理、Markdown生成をオーケストレーションします。
        - **`json_ld_template.json`**: SEO強化のためにウェブページに構造化データとして埋め込むJSON-LDのテンプレートファイル。
        - **`language_info.py`**: GitHubリポジトリの言語情報を取得・処理するロジックを扱うファイル。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを実装したファイル。
        - **`project_overview_fetcher.py`**: 各リポジトリから `generated-docs/project-overview.md` を読み込み、プロジェクト概要を抽出するロジックを扱うファイル。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を整形し、必要なデータに加工するロジックを実装したファイル。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するファイル。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数など）を計算するロジックを扱うファイル。
        - **`strings.yml`**: UIに表示されるメッセージや文言を一元的に管理するためのファイル。
        - **`template_processor.py`**: Markdown生成に使用されるテンプレートファイルの読み込みと処理を行うモジュール。
        - **`url_utils.py`**: URLの構築や解析など、URLに関連するユーティリティ関数を集めたファイル。
- **`test_project_overview.py`**: `project_overview` 機能に関するテストスクリプト。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテスト。
    - **`test_environment.py`**: 実行環境に関するテスト。
    - **`test_integration.py`**: 複数のモジュール間の連携を検証する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能の正確性を検証するテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能の正確性を検証するテスト。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能の正確性を検証するテスト。

## 関数詳細説明
このプロジェクトではPythonスクリプトが中核をなしており、各ファイルに以下のような主要な関数が含まれると想定されます（具体的な引数・戻り値はコードベースに依存します）。

- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`:
        - **役割**: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力という一連のプロセスをオーケストレーションします。
        - **引数**: なし (通常は `sys.argv` を介してコマンドライン引数を内部で処理)。
        - **戻り値**: なし。
- **`src/generate_repo_list/repository_processor.py`**
    - `fetch_and_process_repositories(username, github_token, limit=None)`:
        - **役割**: 指定されたGitHubユーザー名のリポジトリをGitHub APIから取得し、必要な情報（名前、説明、URL、スター数など）を抽出・整形します。オプションで取得リポジトリ数を制限できます。
        - **引数**: `username` (str): GitHubユーザー名, `github_token` (str): GitHub API認証トークン, `limit` (int, optional): 処理するリポジトリ数の上限。
        - **戻り値**: 整形されたリポジトリ情報のリスト (list of dict)。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `get_project_overview(repo_name, owner, target_file, section_title, max_retries, timeout_seconds, enable_cache)`:
        - **役割**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、指定されたセクション（例: "プロジェクト概要"）の3行説明を抽出します。API失敗時のリトライやキャッシュ機能も備えます。
        - **引数**: `repo_name` (str): リポジトリ名, `owner` (str): リポジトリの所有者, `target_file` (str): 概要が記載されているファイルパス, `section_title` (str): 抽出対象のセクションタイトル, `max_retries` (int): API呼び出しのリトライ回数, `timeout_seconds` (int): API呼び出しのタイムアウト時間, `enable_cache` (bool): キャッシュの有効/無効。
        - **戻り値**: 抽出されたプロジェクト概要の文字列 (str) または None。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_repo_markdown(repo_data_list, strings_data, seo_template_data, json_ld_template_data)`:
        - **役割**: 処理済みのリポジトリデータのリストを受け取り、それらを用いて最終的なリポジトリ一覧のMarkdownコンテンツを生成します。表示メッセージ、SEOテンプレート、JSON-LDテンプレートなどを適用します。
        - **引数**: `repo_data_list` (list of dict): 整形されたリポジトリ情報のリスト, `strings_data` (dict): 表示メッセージデータ, `seo_template_data` (dict): SEOテンプレートデータ, `json_ld_template_data` (dict): JSON-LDテンプレートデータ。
        - **戻り値**: 生成されたMarkdownコンテンツの文字列 (str)。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path)`:
        - **役割**: YAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - **引数**: `config_path` (str): 設定ファイルのパス。
        - **戻り値**: 設定内容を格納した辞書 (dict)。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge_markdown(status_type, label, message)`:
        - **役割**: リポジトリのステータス（例: "アクティブ", "アーカイブ"）に応じたバッジのMarkdown構文を生成します。
        - **引数**: `status_type` (str): バッジのタイプ, `label` (str): バッジに表示するラベル, `message` (str): バッジに表示するメッセージ。
        - **戻り値**: バッジのMarkdown文字列 (str)。
- **`src/generate_repo_list/url_utils.py`**
    - `build_github_api_url(username)`:
        - **役割**: 指定されたGitHubユーザー名に基づき、GitHub APIのエンドポイントURLを構築します。
        - **引数**: `username` (str): GitHubユーザー名。
        - **戻り値**: 構築されたAPI URL (str)。

## 関数呼び出し階層ツリー
```
提供された情報では、具体的な関数呼び出し階層ツリーを分析できませんでした。
```

---
Generated at: 2025-12-07 07:05:47 JST
