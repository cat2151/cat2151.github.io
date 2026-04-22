Last updated: 2026-04-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けに自動でMarkdownファイルを生成します。
- 生成されたリポジトリ一覧はSEOを最適化し、検索エンジンでのクロール性と視認性を高めます。
- LLMがGitHubリポジトリを参照できない問題を緩和し、開発効率の向上を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースで静的サイトを構築), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Git (バージョン管理), GitHub API (リポジトリ情報取得), pytest (テストフレームワーク), ruff (コードリンター)
- テスト: pytest (Pythonコードの単体・統合テストを実行)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得とMarkdownの動的な生成), Jekyll (GitHub Pages側でMarkdownをHTMLにビルド)
- 言語機能: Python (主要なスクリプト言語)
- 自動化・CI/CD: Pythonスクリプトによる自動生成 (GitHub Actionsでの定期実行を想定), `.github_automation` ディレクトリによる自動化のサポート
- 開発標準: ruff (Pythonコードの静的解析とフォーマット)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックのルールや閾値を定義する設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報 (MIT License) を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などを説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、GitHub Pagesの挙動に影響します。
- **`assets/`**: Jekyllサイトで利用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`assets/favicon-16x16.png`**, **`assets/favicon-192x192.png`**, **`assets/favicon-32x32.png`**, **`assets/favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズです。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや個別テストのために使用されるスクリプトです。
- **`generated-docs/`**: このスクリプトによって生成されるドキュメントや一時ファイルを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: このスクリプトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイルです。GitHub Pagesで公開されます。
- **`issue-notes/`**: 課題や検討事項に関するメモを格納するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（Issue #22など）に関連する詳細メモやドキュメントです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルです。ウェブアプリの名前、アイコン、表示モードなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境で必要となるPythonパッケージの依存関係をリストアップするファイルです。
- **`requirements.txt`**: このプロジェクトの実行に必要となる本番環境のPythonパッケージ依存関係をリストアップするファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、または避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである `ruff` の設定ファイルです。コードスタイルや静的解析ルールを定義します。
- **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やライセンスなどのバッジ画像を生成するロジックを格納するモジュールです。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行に関する技術的パラメータ（APIリトライ、キャッシュ設定など）を定義する設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` などの設定ファイルを読み込み、プログラム内で利用できるように管理するモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の形式に整形するためのユーティリティモジュールです。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を統括します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のため、JSON-LD形式の構造化データを生成するためのテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリのプログラミング言語に関する情報を取得、処理、整形するモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出し取得するモジュールです。
- **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリの `README.md` ファイルから、既に存在するバッジの情報を抽出するモジュールです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownファイルに組み込むSEO関連のメタデータやテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するモジュールです。
- **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや固定文言を一元管理するリソースファイルです。
- **`src/generate_repo_list/template_processor.py`**: Jekyllのテンプレートエンジンやその他のMarkdownテンプレートの処理を担うモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ機能を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールに特化した単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest` のテスト実行に必要な共通のフィクスチャやヘルパー関数を定義するファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator` の機能が正しく連携するかを確認する統合テストです。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストスクリプトです。
    - **`tests/test_config.py`**: 設定管理機能が正しく動作するかを検証するテストです。
    - **`tests/test_date_formatter.py`**: 日付整形ユーティリティのテストです。
    - **`tests/test_environment.py`**: 実行環境の依存関係や設定が適切であるかを確認するテストです。
    - **`tests/test_integration.py`**: 主要なコンポーネントが連携して全体として正しく機能するかを検証する統合テストです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`tests/test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能のテストです。
    - **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、それぞれ特定の役割を持つ関数群を内包しています。提供された情報には個々の関数の詳細（具体的な関数名、引数、戻り値）は含まれていませんが、各ファイルの役割から以下の機能を持つ関数群が存在すると推測されます:

- **リポジトリ情報取得・処理**: GitHub APIと連携し、リポジトリの基本情報、言語、スター数などを取得・整形する関数群。
- **Markdown生成**: 取得した情報を基に、SEO最適化されたリポジトリ一覧のMarkdownコンテンツを構築する関数群。
- **設定管理**: プロジェクトの設定ファイル（`config.yml`など）を読み込み、プログラム内で利用できるように管理する関数群。
- **日付・文字列処理**: 日付のフォーマット変換や、表示メッセージの管理を行う関数群。
- **バッジ・概要抽出**: `README.md`からバッジ情報を抽出したり、各リポジトリの `project-overview.md` から概要をフェッチする関数群。
- **URLユーティリティ**: URLの構築や解析など、URLに関連する様々な操作を行う関数群。
これらの関数は、`src/generate_repo_list/generate_repo_list.py` を中心に相互に連携し、リポジトリ一覧の自動生成という目的を達成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-04-23 07:19:33 JST
