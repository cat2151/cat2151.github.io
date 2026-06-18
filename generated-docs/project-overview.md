Last updated: 2026-06-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・整理するシステムです。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧ページを生成します。
- 検索エンジンやLLMからのプロジェクト参照性を高め、可視性を向上させることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesを動かすための静的サイトジェネレータ)、Markdown (生成されるリポジトリ一覧ページの記述言語)
- 音楽・オーディオ: (該当なし)
- 開発ツール: Python (主要なスクリプト言語)、Git (バージョン管理システム)、Pytest (Python用テストフレームワーク)
- テスト: Pytest (Pythonコードの単体・統合テストに使用)
- ビルドツール: Jekyll (GitHub Pages上でのMarkdownからHTMLへの変換・サイト生成を担当)
- 言語機能: Python (GitHub API連携、ファイル操作、文字列処理、設定ファイル解析などに利用)
- 自動化・CI/CD: GitHub Pages (リポジトリの更新に応じて自動でサイトをデプロイする機能を提供)
- 開発標準: Ruff (Pythonコードのリンティングおよびフォーマットによるコード品質の維持と統一化)

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
-   **README.md**: プロジェクトの目的、背景、主な機能、開発者向けのヒント、クイックテスト方法、設定ファイル、コマンド例などを説明するメインドキュメント。
-   **LICENSE**: 本プロジェクトがMITライセンスで公開されていることを示すファイル。
-   **_config.yml**: Jekyll (GitHub Pagesの基盤) のグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
-   **index.md**: `generate_repo_list.py`スクリプトによって、ユーザーのリポジトリ一覧が自動生成され、出力されるメインのMarkdownファイル。GitHub Pagesのトップページとして機能します。
-   **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認のために配置されるHTMLファイル。
-   **pytest.ini**: PythonのテストフレームワークであるPytestの設定ファイル。テストの実行オプションや探索パスなどを指定します。
-   **requirements.txt**: プロジェクトの実行時に必要なPythonライブラリとそのバージョンを定義するファイル（本番環境用）。
-   **requirements-dev.txt**: プロジェクトの開発・テストに必要なPythonライブラリとそのバージョンを定義するファイル（開発環境用）。
-   **ruff.toml**: Pythonコードのリンティング（構文やスタイルチェック）および自動フォーマットを行うRuffツールの設定ファイル。
-   **src/generate_repo_list/generate_repo_list.py**: プロジェクトの主要な実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を統括します。
-   **src/generate_repo_list/config.yml**: プロジェクト概要の取得機能など、本システム固有の技術的パラメータを設定するためのYAMLファイル。
-   **src/generate_repo_list/strings.yml**: UI表示メッセージや文言を管理するためのYAMLファイル。多言語対応や文言の一元管理に利用されます。
-   **src/generate_repo_list/badge_generator.py**: リポジトリの言語やスター数などの情報を基に、Markdown形式のバッジを生成するロジックを提供します。
-   **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`や`strings.yml`など）の読み込み、解析、管理を行うモジュール。
-   **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付データを、人間が読みやすい形式にフォーマットするためのユーティリティ関数を提供します。
-   **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データであるJSON-LDのテンプレートファイル。
-   **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するモジュール。
-   **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリデータを受け取り、最終的なリポジトリ一覧をMarkdown形式で構築する主要なコンポーネント。
-   **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要（3行説明）を抽出する機能を提供します。
-   **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するロジックを提供します。
-   **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した内部データ構造に変換する役割を担います。
-   **src/generate_repo_list/seo_template.yml**: サイト全体のSEOメタデータ設定や、各リポジトリエントリのSEO情報を定義するためのテンプレートファイル。
-   **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
-   **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレート（文字列フォーマットなど）を処理し、動的なコンテンツを埋め込む機能を提供します。
-   **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URL関連の様々なユーティリティ関数を集めたモジュール。
-   **tests/**: プロジェクトの各モジュールや機能に対するテストコードを格納するディレクトリ。
    -   **tests/conftest.py**: Pytestのフィクスチャ定義など、テスト全体で共通して使用される設定やヘルパー関数を提供します。
    -   **tests/test_*.py**: 各モモジュールの単体テスト、機能テスト、統合テストなどが記述されています。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細を特定できませんでした。各ファイルの主な役割については、「ファイル詳細説明」セクションをご参照ください。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-19 07:42:05 JST
