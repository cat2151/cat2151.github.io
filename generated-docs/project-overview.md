Last updated: 2026-05-29

# Project Overview

## プロジェクト概要
- GitHub APIを用いてリポジトリ情報を取得し、GitHub Pages向けに自動生成するシステムです。
- リポジトリ一覧や各リポジトリのページをSEO最適化されたMarkdown形式で出力します。
- これにより検索エンジンからのクロールを促進し、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages** (生成されたMarkdownファイルを静的サイトとして公開), **Markdown** (リポジトリ一覧や各リポジトリの概要を記述するフォーマット)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール: **Python** (主要なスクリプト言語), **ruff** (Pythonコードのリンティングとフォーマット), **pytest** (Pythonコードのテストフレームワーク), **Git** (バージョン管理)
- テスト: **pytest** (単体テストおよび統合テストの実行)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報の取得、処理、Markdown生成の自動化), **YAML** (設定ファイルの記述)
- 言語機能: **Python** (スクリプト開発全般に使用)
- 自動化・CI/CD: (このプロジェクト自体はローカル開発重視とされていますが、GitHub APIを利用して情報を取得し、Markdownを生成する過程に自動化の概念が含まれます。)
- 開発標準: **ruff** (コードスタイルと品質の統一), **.editorconfig** (IDEやエディタ間でのコーディングスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデントサイズ、文字コードなど）を定義する設定ファイル。
- **`.github_automation/check_large_files/`**: プロジェクト内の大容量ファイルをチェックするための自動化スクリプト群。
  - **`check-large-files.toml`**: `check_large_files.py`の動作設定ファイル。
  - **`scripts/check_large_files.py`**: 大容量ファイルを検出し、潜在的な問題を特定するPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）。
- **`README.md`**: プロジェクト全体の目的、機能、使用方法などについて記述された主要なドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。GitHub Pagesの振る舞いを定義します。
- **`assets/`**: ウェブサイトで使用されるファビコン（favicon）などの静的アセットを格納するディレクトリ。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグ目的で使用されるスクリプト。
- **`generated-docs/`**: 他のリポジトリから取得した `project-overview.md` ファイルが一時的に格納される可能性のあるディレクトリ、または生成物の出力先の一部。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために使用される認証ファイル。
- **`index.md`**: メインスクリプトによって生成される最終的なリポジトリ一覧のMarkdownファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定のイシュー（課題）に関するメモや詳細が記述されたファイル。
- **`manifest.json`**: ウェブアプリケーションマニフェスト。プログレッシブウェブアプリ（PWA）の機能を提供するメタデータ（アプリ名、アイコン、表示モードなど）を定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイル。テストの発見ルールやプラグインなどを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストするファイル。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージの依存関係をリストするファイル。
- **`robots.txt`**: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: `ruff`リンターおよびフォーマッターの設定ファイル。Pythonコードの品質とスタイルを維持するためのルールを定義します。
- **`src/`**: プロジェクトのソースコードを格納するメインディレクトリ。
  - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むパッケージ。
    - **`badge_generator.py`**: リポジトリの言語やライセンスなどの情報に基づいて、表示用のバッジデータを生成するモジュール。
    - **`config.yml`**: リポジトリ一覧生成処理に関する技術的なパラメータ（例: project overview機能の有効/無効、APIタイムアウト設定など）を定義する設定ファイル。
    - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュール。
    - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形するためのユーティリティモジュール。
    - **`generate_repo_list.py`**: このシステムのメインエントリスクリプト。GitHub APIからの情報取得、処理、Markdown生成までの一連のワークフローを調整します。
    - **`json_ld_template.json`**: SEO最適化のために、構造化データ（JSON-LD）のテンプレートを定義するファイル。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形するモジュール。
    - **`markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを実装したモジュール。
    - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出する機能を提供するモジュール。
    - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するモジュール。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に加工するモジュール。
    - **`seo_template.yml`**: 検索エンジン最適化（SEO）関連のメタデータやテンプレート設定を定義するファイル。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するモジュール。
    - **`strings.yml`**: 表示メッセージや文言を管理するためのファイル。多言語対応や文言の変更を容易にします。
    - **`template_processor.py`**: MarkdownやJekyllのテンプレートファイルを読み込み、データを埋め込んで最終的なコンテンツを生成するモジュール。
    - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールに関する単体テストまたは結合テスト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
  - **`conftest.py`**: `pytest`の共通フィクスチャや設定を定義するファイル。
  - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
  - **`test_check_large_files.py`**: 大容量ファイルチェックスクリプトのテスト。
  - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテスト。
  - **`test_date_formatter.py`**: 日付フォーマットモジュールのテスト。
  - **`test_environment.py`**: 実行環境に関するテスト。
  - **`test_integration.py`**: プロジェクト全体の主要な機能の統合テスト。
  - **`test_markdown_generator.py`**: Markdown生成モジュールのテスト。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得モジュールのテスト。
  - **`test_readme_badge_extractor.py`**: READMEバッジ抽出モジュールのテスト。
  - **`test_repository_processor.py`**: リポジトリデータ処理モジュールのテスト。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
  - **`main()`**: プログラムのエントリポイント。コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成の一連の流れをオーケストレートします。
    - 役割: システム全体の実行フローを制御。
    - 引数: コマンドライン引数（`--username`, `--output`, `--limit`など）。
    - 戻り値: なし。
- **`src/generate_repo_list/repository_processor.py`**
  - **`fetch_repositories(username, token=None, limit=None)`**: 指定されたGitHubユーザー名のリポジトリ情報をGitHub APIから取得します。
    - 役割: GitHub APIとの通信を担当し、生のリポジトリデータを取得。
    - 引数: `username` (str): GitHubユーザー名, `token` (str, optional): GitHub認証トークン, `limit` (int, optional): 取得するリポジトリ数の上限。
    - 戻り値: リポジトリデータのリスト (List[dict])。
  - **`process_repository_data(repo_data)`**: 取得した生のリポジトリデータを、Markdown生成に適した形式に整形・加工します。
    - 役割: リポジトリデータのクリーンアップ、必要な情報の抽出と変換。
    - 引数: `repo_data` (dict): GitHub APIから取得した単一のリポジトリの生データ。
    - 戻り値: 整形されたリポジトリ情報 (dict)。
- **`src/generate_repo_list/markdown_generator.py`**
  - **`generate_markdown(repo_list, output_file, config, strings)`**: 処理済みのリポジトリ情報リストを受け取り、最終的なMarkdownファイルを生成して指定されたパスに保存します。
    - 役割: 整形済みデータに基づいてMarkdownコンテンツを構築し、ファイルとして出力。
    - 引数: `repo_list` (List[dict]): 処理されたリポジトリ情報のリスト, `output_file` (str): 出力ファイル名, `config` (dict): 設定情報, `strings` (dict): 文言情報。
    - 戻り値: なし。
- **`src/generate_repo_list/project_overview_fetcher.py`**
  - **`get_project_overview(owner, repo_name, config)`**: 特定のリポジトリ（`owner`/`repo_name`）から、設定で指定されたファイル（例: `generated-docs/project-overview.md`）の内容を読み込み、3行のプロジェクト概要を抽出します。
    - 役割: 各リポジトリの概要情報を外部ファイルから取得・解析。
    - 引数: `owner` (str): リポジトリのオーナー名, `repo_name` (str): リポジトリ名, `config` (dict): 設定情報。
    - 戻り値: 3行のプロジェクト概要テキスト (str) または空文字列。
- **`src/generate_repo_list/config_manager.py`**
  - **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込みます。
    - 役割: 設定ファイルの読み込みと辞書形式での提供。
    - 引数: `config_path` (str): 設定ファイルへのパス。
    - 戻り値: 設定内容を保持する辞書 (dict)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-29 07:36:25 JST
