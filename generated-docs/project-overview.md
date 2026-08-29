Last updated: 2026-08-30

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を取得・整理します。
- JekyllベースのGitHub Pagesサイト向けに、検索エンジン最適化されたリポジトリ一覧Markdownを自動生成します。
- 生成されたページは、検索エンジンやLLMによるリポジトリ情報の参照性を向上させることを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレーターの基盤), Markdown (自動生成されるコンテンツのフォーマット)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), Ruff (Pythonコードのフォーマッター/リンター), pytest (Pythonのテストフレームワーク), YAML (設定ファイルのフォーマット)
- テスト: pytest (Pythonプロジェクトのテスト実行に利用)
- ビルドツール: Pythonスクリプト (リポジトリ情報取得からMarkdown生成までの一連のプロセスを実行)
- 言語機能: Python (スクリプトの記述に用いられるプログラミング言語)
- 自動化・CI/CD: GitHub Actions (README内で共通化されたワークフロー管理に言及されており、自動化に利用される可能性が高い)
- 開発標準: Ruff (コードスタイルの自動修正と統一), .editorconfig (異なるエディタ間でのコーディングスタイル統一)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェックに関するスクリプト群。
        - **README.md**: 大容量ファイルチェック機能に関する説明。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの目的、機能、使用方法、設定など、全体的な概要を説明する主要なドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（アイコン）。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ用途に使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得したプロジェクト概要などが格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイル。
- **index.md**: 生成されたリポジトリ一覧が書き込まれるメインのMarkdownファイル。GitHub Pagesのトップページとなる。
- **issue-notes/**: 課題や検討事項に関するメモを格納するディレクトリ。
    - **22.md**: 特定の課題に関するメモ。
- **manifest.json**: Webアプリマニフェストファイルで、PWA (Progressive Web App) としてのサイト情報を提供する。
- **pytest.ini**: Pythonのテストフレームワークpytestの設定ファイル。
- **requirements-dev.txt**: 開発環境やテスト環境で必要となるPythonの依存ライブラリをリストアップしたファイル。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonの依存ライブラリをリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに、Webサイトのどの部分をクロールしてよいか、またはクロールしてはならないかを指示するファイル。
- **ruff.toml**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイル。
- **src/**: プロジェクトのソースコードを格納する主要ディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成機能のコアロジックを格納するパッケージ。
        - **__init__.py**: Pythonパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの言語やライセンスなどのバッジ画像を生成するロジックを管理するスクリプト。
        - **config.yml**: リポジトリ情報取得やプロジェクト概要取得機能などの技術的パラメータを定義する設定ファイル。
        - **config_manager.py**: `config.yml`からの設定値の読み込みと管理を行うスクリプト。
        - **date_formatter.py**: 日付データのフォーマットに関するユーティリティ関数を提供するスクリプト。
        - **generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する。
        - **json_ld_template.json**: SEOのためのJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリの言語情報に関する処理を行うスクリプト。
        - **markdown_generator.py**: 取得した情報からMarkdown形式のコンテンツを生成するロジックを管理するスクリプト。
        - **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`からプロジェクト概要を自動取得するスクリプト。
        - **readme_badge_extractor.py**: READMEファイルからバッジ情報を抽出するスクリプト。
        - **repository_processor.py**: GitHubから取得した個々のリポジトリデータを処理・整形するスクリプト。
        - **seo_template.yml**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するファイル。
        - **statistics_calculator.py**: リポジトリの統計情報（例: スター数、フォーク数）を計算するスクリプト。
        - **strings.yml**: UIメッセージや表示文言を一元管理するための設定ファイル。
        - **template_processor.py**: Markdown生成に使用するテンプレートの処理を行うスクリプト。
        - **url_utils.py**: URL操作に関するユーティリティ関数を提供するスクリプト。
- **test_project_overview.py**: プロジェクト概要取得機能の単体テストを記述したスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
    - **test_config.py**: 設定ファイルの読み込みと処理に関するテスト。
    - **test_date_formatter.py**: 日付フォーマット機能のテスト。
    - **test_environment.py**: 実行環境に関するテスト。
    - **test_integration.py**: 主要機能の統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
提供されたプロジェクト情報からは具体的な関数の詳細（引数、戻り値、機能）を特定できませんでした。コードが提供されていないため、ハルシネーションを避けるため、ここでは詳細な説明を割愛します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-30 07:10:16 JST
