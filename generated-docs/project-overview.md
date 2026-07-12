Last updated: 2026-07-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得するシステムです。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- 検索エンジンや大規模言語モデルからの参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesをベースとした静的サイトジェネレータ), Markdown (ページコンテンツ記述形式)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), Git (バージョン管理システム)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: 該当する特定のビルドツールはありません（PythonスクリプトがMarkdown生成を担います）。
- 言語機能: Python (標準ライブラリおよび`requests`, `PyYAML`などの外部ライブラリを含む)
- 自動化・CI/CD: GitHub Actions (`.github_automation`内の自動化スクリプトの実行環境として想定)
- 開発標準: ruff (Pythonコードのフォーマッター兼リンター), EditorConfig (コーディングスタイル統一のための設定ファイル)

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
- **`.editorconfig`**: 開発環境間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **`.github_automation/`**: GitHub上での自動化処理に関するスクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、使い方などを説明する主要なドキュメント。
- **`_config.yml`**: Jekyllサイト全体の共通設定ファイル。サイトタイトルやテーマなどの設定を定義。
- **`assets/`**: サイトのロゴ、ファビコンなどの静的アセット（画像ファイル）を格納するディレクトリ。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用途で使用されるスクリプト。
- **`generated-docs/`**: 生成されたドキュメントや一時ファイルが置かれるディレクトリ（通常は空か、プレースホルダーを保持）。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権認証のために配置されるファイル。
- **`index.md`**: メインスクリプトによって生成されるリポジトリ一覧が出力されるMarkdownファイル。GitHub Pagesのトップページとして機能します。
- **`issue-notes/22.md`**: 開発中に記録された特定課題（Issue #22）に関するメモファイル。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発時およびテスト実行時に必要となるPythonパッケージとそのバージョンを記述したファイル。
- **`requirements.txt`**: プロジェクトが本番環境で動作するために必要となるPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイル。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行う `ruff` ツールの設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`src/__init__.py`**: Pythonパッケージとして認識させるための初期化ファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能の主要なモジュール群。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種ステータスを示すバッジ画像を生成または管理するロジックを実装。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを設定するためのYAMLファイル。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`) の読み込みと管理を行うモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻データを特定のフォーマットに整形するためのユーティリティ関数を提供。
        - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプト。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式のデータテンプレート。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語情報を処理するロジック。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報に基づいてMarkdown形式のコンテンツを生成するロジック。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイルからプロジェクト概要を抽出し取得する機能。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルからバッジ情報を抽出する機能。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示用に整形するロジック。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するテンプレート設定を記述したYAMLファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するロジック。
        - **`src/generate_repo_list/strings.yml`**: サイトに表示されるメッセージや文言を管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        - **`src/generate_repo_list/template_processor.py`**: MarkdownやJekyllのテンプレートを処理し、動的なコンテンツを埋め込むためのユーティリティ。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証などのユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview`機能の単体テストを含むスクリプト。
- **`tests/`**: プロジェクトの各種テストコードが格納されるディレクトリ。
    - **`tests/conftest.py`**: `pytest`で使用される共通のフィクスチャやヘルパー関数を定義するファイル。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`tests/test_config.py`**: 設定ファイルの読み込みと処理に関するテスト。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`tests/test_environment.py`**: 実行環境に関するテスト。
    - **`tests/test_integration.py`**: プロジェクト全体の主要機能の統合テスト。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテスト。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
現在、このプロジェクトの関数詳細情報は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-13 07:19:20 JST
