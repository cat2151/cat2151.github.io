Last updated: 2026-05-18

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのGitHubリポジトリ一覧を自動で生成します。
- 生成されたリポジトリ情報はJekyllベースのGitHub Pagesサイトに最適化されます。
- SEO向上とLLMの参照性改善を通じ、プロジェクトの可視性向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (生成されたMarkdownファイルがGitHub Pagesによって表示されるため、静的サイトジェネレーターとして間接的に関連します)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの中核となるスクリプト言語です。
    - **requests**: GitHub APIとのHTTP通信を行うためのライブラリです。
    - **PyYAML**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）の読み込みに使用します。
    - **toml**: TOML形式の秘密情報ファイル（`secrets.toml`）の読み込みに使用します。
    - **GitHub API**: リポジトリ情報の取得における主要なインターフェースです。
- テスト: **pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール: (厳密な意味でのビルドツールは使用していませんが、PythonスクリプトがMarkdown生成を担います)
- 言語機能: **Python**: データ処理、ファイル操作、API連携など汎用的なプログラミング機能を提供します。
- 自動化・CI/CD: **GitHub Actions**: 将来的なCI/CDや自動化のために設計された`.github_automation`ディレクトリが存在します。
- 開発標準: **ruff**: Pythonコードのリンティングおよび自動フォーマットを行うためのツールです。

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
- **`.editorconfig`**: 異なるエディタ間でのコーディングスタイルの一貫性を保つための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなど、自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイル検出に関連する自動化処理の格納ディレクトリです。
        - **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイル検出スクリプトの設定ファイルです。
        - **`scripts/check_large_files.py`**: 指定された閾値を超える大容量ファイルを検出するPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、開発者向けヒントなどを記述したメインのドキュメントです。
- **`_config.yml`**: GitHub Pages (Jekyll) の設定ファイルです。
- **`assets/`**: サイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: 異なるサイズで提供されるファビコン画像です。
- **`debug_project_overview.py`**: `project_overview` 機能のデバッグ用スクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得された `project-overview.md` など、生成されたドキュメントを一時的に格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト認証のために配置されるHTMLファイルです。
- **`index.md`**: 生成されたリポジトリ一覧が書き込まれるメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: 課題や議論のメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題に関するメモまたは詳細を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブマニフェストファイルです。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージのリストです。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールするか/しないかを指示するファイルです。
- **`ruff.toml`**: ruffリンターの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能のモジュールを格納するパッケージです。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのバッジ（例：言語、ステータス）を生成する機能を持つモジュールです。
        - **`config.yml`**: `generate_repo_list` スクリプトの技術的なパラメータ（API設定、キャッシュ設定など）を定義する設定ファイルです。
        - **`config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`) の読み込みと管理を行うモジュールです。
        - **`date_formatter.py`**: 日付の表示形式を整形する機能を持つモジュールです。
        - **`generate_repo_list.py`**: リポジトリ一覧を生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: SEO強化のためのJSON-LD形式のテンプレートファイルです。
        - **`language_info.py`**: リポジトリの言語情報を処理・表示するモジュールです。
        - **`markdown_generator.py`**: リポジトリ情報からMarkdownコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの `project-overview.md` から概要を抽出するモジュールです。
        - **`readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報を抽出するモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得したリポジトリ情報を処理、整形するモジュールです。
        - **`seo_template.yml`**: SEO関連のテンプレートや設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数など）を計算するモジュールです。
        - **`strings.yml`**: UIに表示されるメッセージや文言を管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成のテンプレート処理を行うモジュールです。
        - **`url_utils.py`**: URLに関連するユーティリティ関数（生成、解析など）を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのフィクスチャや設定を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイル検出スクリプトのテストです。
    - **`test_config.py`**: 設定ファイルの読み込みと処理のテストです。
    - **`test_date_formatter.py`**: 日付整形機能のテストです。
    - **`test_environment.py`**: 環境設定や依存関係のテストです。
    - **`test_integration.py`**: 主要機能の統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
提供された情報からは具体的な関数名やその詳細な説明を特定できませんでした。ハルシネーションを避けるため、このセクションは空白とします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-18 07:21:12 JST
