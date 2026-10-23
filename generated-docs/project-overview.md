Last updated: 2026-10-24

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- 取得した情報をもとにGitHub Pages向けのSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照精度を向上させることを目的としています。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub PagesでMarkdownファイルを元にWebサイトを構築する静的サイトジェネレーター), **Markdown** (リポジトリ一覧の表示フォーマット)
- 音楽・オーディオ: 該当なし
- 開発ツール: **ruff** (PythonコードのフォーマットとLintingを自動化), **pytest** (Pythonアプリケーションのテストフレームワーク)
- テスト: **pytest** (単体テスト、結合テストの実行)
- ビルドツール: **Pythonスクリプト** (`generate_repo_list.py` を中心とした一連のスクリプトがMarkdownファイルを生成する役割を担う)
- 言語機能: **Python** (プロジェクトの主要な開発言語。GitHub API連携、ファイル操作、文字列処理などに利用)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から、リポジトリ一覧の自動更新やデプロイに利用されていると推測)
- 開発標準: **ruff** (コードのフォーマットとスタイルチェックの統一)

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。特に `check_large_files` は大規模ファイルの検出に利用されます。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを記述するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、設定、クイックテスト手順などを記述した、プロジェクトの入り口となるドキュメント。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の共通設定ファイル。サイトのタイトル、テーマ、プラグインなどの情報を保持します。
-   **`assets/`**: ウェブサイトで使用されるファビコン、画像、CSSなどの静的アセットを格納するディレクトリ。
-   **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグを目的とした補助スクリプト。
-   **`generated-docs/`**: 他のリポジトリから自動的に取得された `project-overview.md` ファイルなどが一時的に格納される可能性のあるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイル。
-   **`index.md`**: `src/generate_repo_list/generate_repo_list.py` スクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧メインページとなるMarkdownファイル。
-   **`issue-notes/`**: 開発中の課題やメモなどを記録しておくためのディレクトリ。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイル。ウェブサイトをユーザーのデバイスにインストール可能なアプリのように見せるための設定を含みます。
-   **`pytest.ini`**: pytestテストフレームワークの共通設定を記述するファイル。テスト実行時のオプションなどを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージの依存関係をリストアップしたファイル。
-   **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージの依存関係をリストアップしたファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、あるいはクロールしてはならないかを指示するファイル。
-   **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるruffの設定ファイル。コードスタイルや静的解析のルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   **`src/__init__.py`**: Pythonパッケージとして認識させるためのファイル。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成機能の中核となるPythonモジュール群を格納するディレクトリ。
        -   **`src/generate_repo_list/__init__.py`**: Pythonサブパッケージを示すファイル。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するためのロジック。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能やその他技術的パラメータに関する設定ファイル。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル (`config.yml`, `strings.yml` など) を読み込み、管理するためのモジュール。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を整形し、表示に適した形式に変換するユーティリティ。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリスクリプト。GitHub APIからの情報取得、リポジトリ処理、Markdown生成、ファイル出力までの一連のプロセスを制御します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 構造化データの一種であるJSON-LD形式のテンプレート。検索エンジン最適化 (SEO) のためにリポジトリ情報をリッチスニペットとして表示させるのに役立ちます。
        -   **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの主要言語情報などを処理・表示するためのロジック。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成するモジュール。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を自動的に取得するロジック。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報などを抽出するロジック。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に処理するモジュール。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するファイル。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算するモジュール。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するための設定ファイル。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用するテンプレートファイルの読み込みやレンダリングを処理するモジュール。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュールのテストケースの一部を含むファイル。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`tests/conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義し、テスト間で共有するためのファイル。
    -   **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    -   **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能に関するテスト。
    -   **`tests/test_config.py`**: 設定ファイル (`config.yml` など) の読み込みや解釈に関するテスト。
    -   **`tests/test_date_formatter.py`**: 日付フォーマット機能のテスト。
    -   **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテスト。
    -   **`tests/test_integration.py`**: 主要なコンポーネントが連携して正しく機能するかを確認する統合テスト。
    -   **`tests/test_markdown_generator.py`**: Markdown生成ロジックのテスト。
    -   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    -   **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    -   **`tests/test_repository_processor.py`**: GitHubリポジトリ情報の処理に関するテスト。

## 関数詳細説明
-   **`generate_repo_list.py` 内の主要関数**:
    -   `main()`: (エントリポイント) コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、最終的なファイル出力までの一連の処理をオーケストレーションします。
    -   `_get_github_token()`: GitHub APIにアクセスするために必要なトークンを安全に取得します。
    -   `_fetch_repositories(username, token, limit)`: 指定されたユーザー名とトークンを使用し、GitHub APIを介してリポジトリ情報を取得します。`limit` パラメータで取得数を制限できます。
-   **`repository_processor.py` 内の主要関数**:
    -   `process_repository_data(repo_data, config, token)`: GitHub APIから取得した生のリポジトリデータ（辞書形式）を受け取り、プロジェクトで利用しやすいように整形し、追加情報（例: プロジェクト概要）を付与して返します。
-   **`project_overview_fetcher.py` 内の主要関数**:
    -   `fetch_project_overview(repo_name, target_file, config, token)`: 指定されたリポジトリ名から `config` で定義された `target_file` (例: `generated-docs/project-overview.md`) を取得し、その中から指定された `section_title` の下の3行の概要を抽出して返します。
-   **`markdown_generator.py` 内の主要関数**:
    -   `generate_repository_list_markdown(processed_repos, strings_config, seo_template_config)`: 処理済みリポジトリ情報のリスト、表示文言設定、SEOテンプレート設定を受け取り、それらを組み合わせて最終的なリポジトリ一覧のMarkdown文字列を生成します。
-   **`badge_generator.py` 内の主要関数**:
    -   `generate_badge_markdown(badge_info)`: バッジに関する情報（テキスト、色、リンクなど）を受け取り、それに対応するMarkdown形式のバッジ文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-24 07:11:19 JST
