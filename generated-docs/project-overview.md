Last updated: 2026-05-14

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成します。
- 検索エンジンへのクロールを促進し、LLMによるリポジトリ参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤)、Markdown (生成されるリポジトリ一覧コンテンツの形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (主要なスクリプト言語)、Pytest (Python用テストフレームワーク)、Ruff (Pythonコードのリンターおよびフォーマッター)
- テスト: Pytest (ユニットテストおよび統合テストの実行)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得とMarkdown生成ロジックを実装)、YAML/TOML (設定ファイルの記述形式)
- 言語機能: Python (GitHub APIとの連携、ファイル操作、データ処理、文字列操作など)
- 自動化・CI/CD: 本プロジェクトはCI/CDを重視しないローカル開発優先の構成です。
- 開発標準: Ruff (Pythonコードの品質と一貫性を維持するためのルールセット)、.editorconfig (異なるエディタ間でのコーディングスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなど、リポジトリ自動化に関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックするためのツールが含まれています。
        - **`README.md`**: `check_large_files`ツールの説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、機能説明などが記載されたメインドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定ファイルです。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **`assets/`**: ウェブサイトで使用されるファビコン（favicon）などの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが一時的に格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **`index.md`**: `generate_repo_list.py`スクリプトによって生成されたリポジトリ一覧が書き込まれる、GitHub PagesのトップページとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中の課題やメモが格納されるディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてウェブサイトが動作する際のメタデータを定義するファイルです。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの検出ルールやオプションが記述されます。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonライブラリをリストアップするファイルです。
- **`requirements.txt`**: 本番環境で必要となるPythonライブラリをリストアップするファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: PythonコードのスタイルチェックツールRuffの設定ファイルです。コードの整形ルールや警告レベルが定義されます。
- **`src/`**: プロジェクトのソースコードが格納されるルートディレクトリです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを格納するパッケージです。
        - **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリのステータス（例：アクティブ、アーカイブ）に応じたバッジの情報を生成するモジュールです。
        - **`config.yml`**: リポジトリ一覧生成に関する実行時設定（例：プロジェクト概要取得機能のON/OFF、タイムアウト時間など）を定義するファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティモジュールです。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、処理を行い、最終的なMarkdownファイルを生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理するモジュールです。
        - **`markdown_generator.py`**: 処理されたリポジトリデータからMarkdown形式のコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を自動取得するモジュールです。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEからバッジ情報を抽出するモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、表示に適した形式に変換するモジュールです。
        - **`seo_template.yml`**: SEOメタデータに関するテンプレートを定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するモジュールです。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するファイルです。多言語対応や文言の一元管理に利用されます。
        - **`template_processor.py`**: Markdown生成用のテンプレートを処理し、データと結合するモジュールです。
        - **`url_utils.py`**: URLの操作や検証に関するユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能に関するテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: Pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェックツールのテストです。
    - **`test_config.py`**: 設定ファイル読み込み・管理モジュール(`config_manager.py`)のテストです。
    - **`test_date_formatter.py`**: 日付整形モジュールのテストです。
    - **`test_environment.py`**: テスト環境のセットアップや依存関係に関するテストです。
    - **`test_integration.py`**: プロジェクト全体または主要なモジュールの統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成モジュールのテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得モジュールのテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出モジュールのテストです。
    - **`test_repository_processor.py`**: リポジトリ処理モジュールのテストです。

## 関数詳細説明
- **`generate_repo_list.py`**:
    - `main()`: このスクリプトのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力という一連のフローを制御します。
- **`repository_processor.py`**:
    - `process_repository_data(repo_data)`: GitHub APIから取得した単一のリポジトリの生データを整形し、Markdown生成に適した形式に変換します。
        - 引数: `repo_data` (dict) - GitHub APIから取得したリポジトリの辞書形式データ。
        - 戻り値: `dict` - 整形されたリポジトリ情報を含む辞書。
- **`project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_name, owner, config)`: 指定されたGitHubリポジトリ内の`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を非同期で取得します。
        - 引数: `repo_name` (str) - 取得対象のリポジトリ名、`owner` (str) - リポジトリのオーナー名、`config` (ConfigManager) - プロジェクト設定オブジェクト。
        - 戻り値: `list` - 抽出された3行の概要説明文字列のリスト。
- **`markdown_generator.py`**:
    - `generate_markdown(repositories_info)`: 処理済みリポジトリ情報のリストを受け取り、それらを用いて最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
        - 引数: `repositories_info` (list) - `repository_processor.py`によって整形されたリポジトリ情報を含む辞書のリスト。
        - 戻り値: `str` - 生成されたMarkdown形式の文字列。
- **`badge_generator.py`**:
    - `generate_badges(repo_status)`: リポジトリのステータス情報に基づいて、表示用のバッジ（例：アクティブ、アーカイブ）を生成します。
        - 引数: `repo_status` (str) - リポジトリの現在のステータス。
        - 戻り値: `str` - バッジのMarkdownまたはHTML文字列。
- **`config_manager.py`**:
    - `load_config(config_path)`: 指定されたパスからYAML設定ファイルを読み込み、設定オブジェクトを返します。
        - 引数: `config_path` (str) - 設定ファイルのパス。
        - 戻り値: `dict` - 読み込まれた設定値を含む辞書。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-05-14 07:30:43 JST
