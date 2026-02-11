Last updated: 2026-02-12

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- SEOを最適化し、各リポジトリの検索エンジンへのインデックス登録を促進します。
- リポジトリごとのプロジェクト概要やバッジ表示をサポートし、LLMによる参照を容易にします。

## 技術スタック
- フロントエンド: Jekyll (生成されたMarkdownファイルがGitHub Pages上で静的サイトとしてレンダリングされるプラットフォーム)
- 音楽・オーディオ: 該当なし
- 開発ツール: Git (バージョン管理システム。プロジェクトのソースコード管理に利用), GitHub API (リポジトリ情報の取得に利用されるAPI)
- テスト: pytest (Pythonで書かれたテストコードを実行するためのフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIからのデータ取得、Markdownファイルの生成など、本システムのコア処理を担うカスタムスクリプト群)
- 言語機能: Python (プロジェクトの主要な開発言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得によるプロセス自動化), カスタムスクリプト (リポジトリ一覧の自動生成という形で自動化を実現)
- 開発標準: ruff (Pythonコードのリンターおよびフォーマッター。コードスタイルと品質を自動的に統一・維持する)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
    - **`check_large_files/`**: 大容量ファイルチェックに関する自動化機能のディレクトリ。
        - **`README.md`**: `check_large_files` 機能の説明。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイル。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを指定する設定ファイル。
- **`LICENSE`**: プロジェクトのライセンス情報 (MITライセンス) を示すファイル。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法、開発者向けのヒントなどを記述した主要なドキュメント。
- **`_config.yml`**: Jekyllサイト全体の共通設定ファイル。GitHub Pagesのビルド設定やテーマ設定などを含む。
- **`assets/`**: Jekyllサイトで使用される画像やアイコンなどの静的リソースを格納するディレクトリ。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: サイトのファビコン画像。異なるサイズに対応。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能の動作確認やデバッグを目的とした補助スクリプト。
- **`generated-docs/`**: 他のリポジトリから自動的に取得されたプロジェクト概要などのドキュメントを一時的または恒久的に格納するためのディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるファイル。
- **`index.md`**: メインの出力ファイル。GitHub APIから取得したリポジトリ情報に基づいて生成されたリポジトリ一覧がMarkdown形式で書き込まれ、JekyllによってGitHub Pagesのトップページとして表示される。
- **`issue-notes/`**: 開発中に発生した課題や検討事項をMarkdown形式で記録するメモ群を格納するディレクトリ。
- **`manifest.json`**: Webアプリマニフェストファイル。プログレッシブウェブアプリ (PWA) の設定や、ホーム画面への追加に関する情報を提供する。
- **`pytest.ini`**: pytestテストフレームワークの共通設定ファイル。テストの実行方法やプラグイン設定などを定義する。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **`requirements.txt`**: 本番環境でこのシステムを実行するために必要なPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや静的解析ルールを定義する。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **`__init__.py`**: Pythonがこのディレクトリをパッケージとして認識するためのファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の中核となるPythonパッケージ。
        - **`__init__.py`**: Pythonがこのディレクトリをパッケージとして認識するためのファイル。
        - **`badge_generator.py`**: リポジトリの言語やスター数などの情報を元に、表示用のバッジを生成するロジックを扱う。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの動作を制御する技術的パラメータ（例: プロジェクト概要取得機能のON/OFF、タイムアウト設定など）を定義するファイル。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのユーティリティを提供する。
        - **`date_formatter.py`**: 日付や時刻の情報を特定の形式に整形するための関数を提供する。
        - **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理の全体を統括する。
        - **`json_ld_template.json`**: SEO強化のためにWebページに埋め込む構造化データ (JSON-LD) のテンプレート。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形する。
        - **`markdown_generator.py`**: 処理されたリポジトリデータやSEO情報を基に、出力されるMarkdownコンテンツの構造を構築する。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル (例: `generated-docs/project-overview.md`) からプロジェクト概要の3行説明を自動的に取得する。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能を提供する。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形する。
        - **`seo_template.yml`**: 検索エンジン最適化 (SEO) のためのメタデータやテンプレート設定を定義するファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算する。
        - **`strings.yml`**: 生成されるMarkdownファイルやログメッセージで使用される表示文言や文字列を集中管理するファイル。
        - **`template_processor.py`**: Markdownテンプレートの読み込み、変数置換、条件分岐処理などを行い、動的なコンテンツ生成をサポートする。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供する。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（特にプロジェクト概要の抽出ロジック）を検証するためのテストスクリプト。
- **`tests/`**: プロジェクト全体の単体テスト、統合テストなどを格納するディレクトリ。
    - **`test_badge_generator_integration.py`**: `badge_generator` の統合テスト。
    - **`test_check_large_files.py`**: `check_large_files.py` スクリプトのテスト。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能 (`config_manager.py` など) のテスト。
    - **`test_date_formatter.py`**: 日付フォーマット機能 (`date_formatter.py`) のテスト。
    - **`test_environment.py`**: 環境変数や依存関係など、実行環境に関するテスト。
    - **`test_integration.py`**: 主要な機能間の連携を検証する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能 (`markdown_generator.py`) のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテスト。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能 (`readme_badge_extractor.py`) のテスト。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能 (`repository_processor.py`) のテスト。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py` 内の関数**
    - `main()`: コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といった一連の処理を調整し実行する、スクリプトのエントリポイント。
- **`src/generate_repo_list/repository_processor.py` 内の関数**
    - `fetch_repositories(username: str, github_token: str) -> list`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIから取得し、生データとして返します。
        - 引数: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIアクセストークン。
        - 戻り値: リポジトリ情報のリスト。
    - `process_repository_data(repo_data: dict, config: dict) -> dict`: 個々のリポジトリの生データを整形し、Markdown生成に適した形式に変換します。プロジェクト概要の取得やバッジ情報の加工なども含まれます。
        - 引数: `repo_data` (dict): GitHub APIから取得した単一リポジトリのデータ, `config` (dict): プロジェクトの設定情報。
        - 戻り値: 処理済みのリポジトリデータ辞書。
- **`src/generate_repo_list/project_overview_fetcher.py` 内の関数**
    - `fetch_project_overview(repo_name: str, config: dict, github_token: str) -> str`: 指定されたリポジトリの特定のファイル (例: `generated-docs/project-overview.md`) から、設定に基づいてプロジェクト概要の3行説明を抽出して返します。APIリクエストやファイル内容のパースが含まれます。
        - 引数: `repo_name` (str): リポジトリ名, `config` (dict): プロジェクトの設定情報, `github_token` (str): GitHub APIアクセストークン。
        - 戻り値: 抽出されたプロジェクト概要 (str)、または空文字列。
- **`src/generate_repo_list/markdown_generator.py` 内の関数**
    - `generate_markdown(processed_repos: list, seo_config: dict, strings: dict) -> str`: 処理済みのリポジトリデータとSEO設定、表示文言を基に、最終的なリポジトリ一覧のMarkdownコンテンツ全体を構築して返します。
        - 引数: `processed_repos` (list): 処理済みのリポジトリデータリスト, `seo_config` (dict): SEO関連の設定, `strings` (dict): 表示文言の辞書。
        - 戻り値: 生成されたMarkdown文字列。
- **`src/generate_repo_list/badge_generator.py` 内の関数**
    - `generate_badge(badge_type: str, value: Any) -> str`: 指定された種類と値に基づいて、表示用のバッジを表すMarkdownスニペットを生成します。
        - 引数: `badge_type` (str): バッジの種類 (例: 'language', 'stars'), `value` (Any): バッジに表示する値。
        - 戻り値: バッジのMarkdown文字列。
- **`src/generate_repo_list/config_manager.py` 内の関数**
    - `load_config(config_path: str) -> dict`: 指定されたパスのYAML設定ファイルを読み込み、辞書として返します。
        - 引数: `config_path` (str): 設定ファイルのパス。
        - 戻り値: 設定内容を格納した辞書。
- **`src/generate_repo_list/date_formatter.py` 内の関数**
    - `format_date(iso_date_str: str) -> str`: ISO 8601形式の日付文字列を、人間が読みやすい形式に整形して返します。
        - 引数: `iso_date_str` (str): ISO 8601形式の日付文字列。
        - 戻り値: フォーマットされた日付文字列。
- **`src/generate_repo_list/readme_badge_extractor.py` 内の関数**
    - `extract_badges_from_readme(readme_content: str) -> list`: READMEの内容から、特定のパターンに合致するバッジ情報を抽出します。
        - 引数: `readme_content` (str): READMEファイルのテキスト内容。
        - 戻り値: 抽出されたバッジ情報のリスト。
- **`src/generate_repo_list/statistics_calculator.py` 内の関数**
    - `calculate_statistics(repo_data: dict) -> dict`: リポジトリデータに基づいて、スター数、フォーク数などの統計情報を計算し、辞書として返します。
        - 引数: `repo_data` (dict): リポジトリのデータ。
        - 戻り値: 計算された統計情報辞書。
- **`src/generate_repo_list/template_processor.py` 内の関数**
    - `apply_template(template_str: str, data: dict) -> str`: テンプレート文字列内のプレースホルダーを、提供されたデータで置換し、最終的な文字列を生成します。
        - 引数: `template_str` (str): テンプレート文字列, `data` (dict): プレースホルダーに適用するデータ。
        - 戻り値: データが適用された文字列。
- **`.github_automation/check_large_files/scripts/check_large_files.py` 内の関数**
    - `main()`: スクリプトのエントリポイント。設定ファイルを読み込み、Gitリポジトリを走査して大容量ファイルを検出し、報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。
しかし、`src/generate_repo_list/generate_repo_list.py` の `main()` 関数がエントリポイントとして、他のモジュール（`config_manager`, `repository_processor`, `project_overview_fetcher`, `markdown_generator` など）の主要な関数を呼び出して全体の処理フローを制御していると推測されます。

---
Generated at: 2026-02-12 07:10:51 JST
