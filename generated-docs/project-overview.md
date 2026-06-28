Last updated: 2026-06-29

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成します。
- これにより、プロジェクトの検索エンジンからの可視性を高め、LLMによる参照失敗の問題を緩和します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレータJekyllをベースとしたGitHub Pagesで、生成されたリポジトリ一覧を表示します。
- 音楽・オーディオ: 特になし
- 開発ツール: Python - メインの開発言語としてスクリプトの作成、データ処理、Markdown生成に利用されています。
- テスト: Pytest - Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです。
- ビルドツール: Pythonスクリプト - GitHub APIから取得したデータを処理し、Markdown形式のファイルを生成します。Jekyllは最終的な静的サイトの構築を行います。
- 言語機能: Python 3.x - モダンなPython言語機能（例: 型ヒント、モジュールシステム）を活用しています。
- 自動化・CI/CD: GitHub Actions - リポジトリ内の特定の自動化スクリプト（例: 大容量ファイルチェック）の実行基盤として利用されています。
- 開発標準: Ruff - Pythonコードのフォーマットとリンティングを行い、コード品質と一貫性を保つためのツールです。
- API: GitHub API - リポジトリのメタ情報、説明、言語、星の数などの詳細情報を取得するために利用されます。

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsや自動化スクリプト関連のファイルを格納するディレクトリ。
    -   **`check_large_files/`**: 大容量ファイルチェックに関するスクリプトや設定を格納。
        -   **`README.md`**: 大容量ファイルチェック機能の説明。
        -   **`check-large-files.toml`**: 大容量ファイルチェックの設定。
        -   **`scripts/check_large_files.py`**: 大容量ファイルを検出するPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、および使い方などを説明するメインドキュメント。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイル。
-   **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（アイコン）の様々なサイズ。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプト。
-   **`generated-docs/`**: 自動生成されたドキュメントやデータが一時的に格納される可能性のあるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイル。
-   **`index.md`**: 生成されたリポジトリ一覧のMarkdownコンテンツが出力されるメインページ。Jekyllによって処理され、HTMLページとして公開される。
-   **`issue-notes/`**: 課題やメモを記録するためのディレクトリ。
    -   **`22.md`**: 特定の課題に関する詳細なメモ。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を定義するマニフェストファイル。
-   **`pytest.ini`**: Pytestのテスト実行に関する設定を定義するファイル。
-   **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージの依存関係をリストアップするファイル。
-   **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージの依存関係をリストアップするファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイル。
-   **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成ロジックを格納するパッケージ。
        -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや情報を示すバッジをMarkdown形式で生成する機能。
        -   **`config.yml`**: リポジトリ一覧生成に関する各種設定（例: プロジェクト概要取得機能の設定）。
        -   **`config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`など) の読み込みと管理を行うモジュール。
        -   **`date_formatter.py`**: 日付や時刻のフォーマットを処理するユーティリティ機能。
        -   **`generate_repo_list.py`**: プロジェクトのエントリポイントであり、リポジトリ一覧生成のメインロジックを実行するスクリプト。
        -   **`json_ld_template.json`**: SEOのためのJSON-LD形式の構造化データテンプレート。
        -   **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理するモジュール。
        -   **`markdown_generator.py`**: GitHubリポジトリの情報から、Jekyllに適したMarkdownコンテンツを生成する機能。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得する機能。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報を抽出する機能。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、表示に適した形に処理する機能。
        -   **`seo_template.yml`**: 検索エンジン最適化(SEO)に関連するメタデータや構造のテンプレート。
        -   **`statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するモジュール。
        -   **`strings.yml`**: プロジェクト内で使用される表示テキストや文言を一元管理するファイル。
        -   **`template_processor.py`**: Markdown生成におけるテンプレート処理を担当するモジュール。
        -   **`url_utils.py`**: URLの生成や解析に関連するユーティリティ機能。
-   **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストを記述したファイル。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`conftest.py`**: Pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能のテスト。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテスト。
    -   **`test_environment.py`**: 実行環境に関するテスト。
    -   **`test_integration.py`**: システム全体の主要な統合テスト。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    -   **`test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
-   **`generate_repo_list.py`内の主要関数 (`main`)**:
    -   **役割**: プロジェクトのエントリポイントであり、GitHub APIからリポジトリ情報を取得し、その情報を基にMarkdown形式のリポジトリ一覧ファイルを生成する一連の処理を制御します。
    -   **機能**: コマンドライン引数の解析、設定の読み込み、リポジトリデータの取得、各リポジトリの処理、Markdown生成、ファイル出力までを実行します。
-   **`repository_processor.py`内の主要関数 (`process_repository_data`)**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に整形・加工します。
    -   **機能**: リポジトリのURL、説明、言語、スター数、最終更新日などの情報を抽出し、バッジの有無や概要の取得状況を考慮して、Markdown生成に適したデータ構造を構築します。
-   **`project_overview_fetcher.py`内の主要関数 (`fetch_project_overview`)**:
    -   **役割**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`など）から、そのリポジトリの3行概要を抽出します。
    -   **機能**: GitHub APIを介して指定されたファイルを読み込み、定義されたセクション（「プロジェクト概要」など）から指定行数（通常3行）のテキストをパースして返します。キャッシュ機能も備えています。
-   **`markdown_generator.py`内の主要関数 (`generate_repository_markdown`)**:
    -   **役割**: 処理されたリポジトリデータとテンプレートを使用して、個々のリポジトリのMarkdownコンテンツを生成します。
    -   **機能**: リポジトリ名、説明、リンク、バッジ、概要、言語などの情報を指定されたMarkdownテンプレートに埋め込み、最終的なMarkdown文字列を生成します。
-   **`badge_generator.py`内の主要関数 (`generate_badge_markdown`)**:
    -   **役割**: リポジトリの属性（例: アクティブ、アーカイブ、フォーク）に基づいて、対応するMarkdown形式のバッジを生成します。
    -   **機能**: 渡された情報に応じて、適切なアイコンやテキストを含むバッジのMarkdownスニペットを作成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-06-29 07:25:29 JST
