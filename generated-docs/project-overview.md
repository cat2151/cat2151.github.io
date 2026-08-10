Last updated: 2026-08-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、SEOに最適化されたGitHub Pages用のリポジトリ一覧Markdownファイルを生成します。
- これにより、リポジトリの検索エンジン露出を向上させ、LLMからの参照性も高めることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), GitHub API (リポジトリ情報取得)
- テスト: Pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Pythonスクリプト (Markdownファイル生成), Jekyll (GitHub Pagesサイトのビルドシステム)
- 言語機能: Python (スクリプト開発に利用)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリの存在から、コード品質チェックや自動化タスクに利用されていると推測されます)
- 開発標準: Ruff (Pythonコードのフォーマッター/リンター), EditorConfig (異なるエディタ間でのコーディングスタイル統一)

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

*   **`.editorconfig`**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
*   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリです。
    *   **`check_large_files/`**: 大容量ファイルを検出するためのスクリプト群を格納します。
        *   **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
        *   **`check-large-files.toml`**: 大容量ファイルチェックに関する設定（例: サイズ制限）を定義します。
        *   **`scripts/check_large_files.py`**: 実際に大容量ファイルをチェックするPythonスクリプトです。
*   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義します。
*   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイルです。
*   **`README.md`**: プロジェクトの概要、セットアップ方法、使用方法などを説明するメインのドキュメントです。
*   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
*   **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    *   **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるサイトのアイコンです。
*   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
*   **`generated-docs/`**: `project-overview.md`など、自動生成されたドキュメントの参照元となるファイルを格納するための標準パスです。
*   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するためのHTMLファイルです。
*   **`index.md`**: GitHub Pagesサイトのトップページとして、リポジトリ一覧が自動生成されて出力されるマークダウンファイルです。
*   **`issue-notes/22.md`**: 特定のイシュー（課題）に関するメモや詳細を記録したファイルです。
*   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するファイルで、ウェブサイトをホーム画面に追加する際の表示設定などを指定します。
*   **`pytest.ini`**: Pytestテストフレームワークの設定ファイルです。テストの実行方法やオプションを定義します。
*   **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージの依存関係をリストアップします。
*   **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージの依存関係をリストアップします。
*   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールして良いか、または避けるべきかを指示するファイルです。
*   **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。コーディングスタイルルールを定義します。
*   **`src/`**: プロジェクトのソースコードを格納するディレクトリです。
    *   **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを構成するPythonモジュール群です。
        *   **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
        *   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを含みます。
        *   **`config.yml`**: `generate_repo_list` スクリプトの動作を設定するYAMLファイルです。
        *   **`config_manager.py`**: 設定ファイル（`config.yml`など）の読み込みと管理を行うモジュールです。
        *   **`date_formatter.py`**: 日付や時刻の表示形式を整形する機能を提供します。
        *   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
        *   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートです。
        *   **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理します。
        *   **`markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式の文字列を生成する役割を担います。
        *   **`project_overview_fetcher.py`**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、概要を抽出する機能を提供します。
        *   **`readme_badge_extractor.py`**: リポジトリのREADMEからバッジ情報を抽出する機能を提供します。
        *   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形・加工するモジュールです。
        *   **`seo_template.yml`**: SEOメタデータに関する設定やテンプレートを定義します。
        *   **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算する機能を提供します。
        *   **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するYAMLファイルです。
        *   **`template_processor.py`**: Markdown生成などで使用されるテンプレートの処理を行うモジュールです。
        *   **`url_utils.py`**: URLの操作や検証に関するユーティリティ関数を提供します。
*   **`test_project_overview.py`**: プロジェクト概要取得機能に関する単体テストを記述したファイルです。
*   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    *   **`conftest.py`**: Pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    *   **`test_*.py`**: 各モジュールや機能に対応するテストファイル群です。例えば、`test_badge_generator_integration.py`はバッジ生成機能の統合テスト、`test_config.py`は設定管理モジュールのテストなどです。

## 関数詳細説明
提供された情報からは具体的な関数の引数、戻り値、詳細な機能までを個別に説明することはできません。
しかし、各Pythonファイルはそのファイル名に示される役割を持つ関数群を内部に含んでいます。
例えば、`src/generate_repo_list/generate_repo_list.py` にはリポジトリ一覧の生成フローを制御する主要な関数が含まれ、`markdown_generator.py` にはMarkdown形式の文字列を生成するための関数、`project_overview_fetcher.py` には特定ファイルからプロジェクト概要を抽出する関数などが含まれていると推測されます。

## 関数呼び出し階層ツリー
```
関数の呼び出し階層に関する情報は提供されていないため、ツリーを生成することはできません。

---
Generated at: 2026-08-11 07:14:18 JST
