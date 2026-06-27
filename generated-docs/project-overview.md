Last updated: 2026-06-28

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得してGitHub Pages向けMarkdownを生成するシステムです。
- 生成されたリポジトリ一覧はSEO最適化され、検索エンジンやLLMによる参照性を高めます。
- 各リポジトリの概要説明を自動抽出し、アクティブ・アーカイブ・フォーク別に分類して表示します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレータJekyllを利用し、GitHub Pagesでウェブサイトを公開します。
- 音楽・オーディオ: なし
- 開発ツール: GitHub API - GitHubのリポジトリ情報を取得するために利用されます。pytest - Pythonコードのテストフレームワークです。ruff - 高速なPythonリンターおよびフォーマッターです。
- テスト: pytest - Pythonアプリケーションの単体テスト、統合テスト、機能テストを実行するためのフレームワークです。
- ビルドツール: Markdown生成 - Pythonスクリプトにより、Jekyllが解釈できるMarkdown形式のファイルを生成します。
- 言語機能: Python - プロジェクトの主要な開発言語として使用されており、リポジトリ情報の取得とMarkdown生成ロジックを実装しています。
- 自動化・CI/CD: GitHub Pages - 生成された静的サイトのホスティングとデプロイを行います。
- 開発標準: ruff - コードの品質とスタイルを維持するためのリンターおよびフォーマッターとして使用されます。`.editorconfig` - 異なるエディタ間でのコードスタイルの一貫性を保つための設定ファイルです。

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
-   **`.editorconfig`**: 異なる開発環境やエディタ間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリ。
    -   **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書。
    -   **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイル。
    -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを識別し、警告するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトの利用条件を定めるライセンス情報（MITライセンス）。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法などを説明するメインドキュメント。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイル。
-   **`assets/`**: ウェブサイトで使用される静的リソース（ファビコンなどの画像ファイル）を格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを目的としたスクリプト。
-   **`generated-docs/`**: プロジェクトによって自動生成されるドキュメントや、外部リポジトリから取得した概要ファイルなどを配置するためのディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイル。
-   **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。リポジトリ一覧がこのファイルに生成される。
-   **`issue-notes/`**: プロジェクトに関連する特定の課題やメモを記録するためのディレクトリ。
    -   **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや情報。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを提供するマニフェストファイル。ホーム画面への追加やオフライン機能などの設定を含む。
-   **`pytest.ini`**: Pythonのテストフレームワークpytestの動作を設定するファイル。
-   **`requirements-dev.txt`**: プロジェクトの開発時やテスト時に必要なPythonライブラリの一覧。
-   **`requirements.txt`**: プロジェクトの本番環境または実行環境で必要なPythonライブラリの一覧。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか、しないかを指示するファイル。
-   **`ruff.toml`**: PythonのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや潜在的な問題をチェックするルールを定義。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するコアロジックを含むPythonパッケージ。
        -   **`__init__.py`**: Pythonパッケージとして認識させるための初期化ファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや技術を示すバッジ画像を生成または処理するロジック。
        -   **`config.yml`**: `project_overview`機能など、スクリプトの動作を制御する設定パラメータを定義するYAMLファイル。
        -   **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）を読み込み、管理するためのユーティリティ。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するための関数群。
        -   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインスクリプト。
        -   **`json_ld_template.json`**: SEO目的で構造化データ（JSON-LD）を生成するためのテンプレート。
        -   **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理、分析するロジック。
        -   **`markdown_generator.py`**: 取得した情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジック。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得するロジック。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出するロジック。
        -   **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理、整形するためのロジック。
        -   **`seo_template.yml`**: 生成されるMarkdownファイルのSEO関連のメタデータ（タイトル、ディスクリプションなど）を設定するためのテンプレート。
        -   **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（スター数、フォーク数など）を計算するロジック。
        -   **`strings.yml`**: アプリケーション内で表示される各種メッセージやラベル、文言などを一元管理するYAMLファイル。
        -   **`template_processor.py`**: Markdown生成時に使用するテンプレートファイルの読み込みと変数置換を行うロジック。
        -   **`url_utils.py`**: URLの生成、解析、検証などのユーティリティ関数。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`機能の単体テストスクリプト。
-   **`tests/`**: プロジェクトの各種テストコードを格納するディレクトリ。
    -   **`conftest.py`**: pytestのテスト実行前に共通で利用されるフィクスチャやヘルパー関数を定義するファイル。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理に関するテスト。
    -   **`test_date_formatter.py`**: 日付整形関数のテスト。
    -   **`test_environment.py`**: 実行環境の設定や依存関係に関するテスト。
    -   **`test_integration.py`**: プロジェクトの主要なコンポーネント間の連携を検証する統合テスト。
    -   **`test_markdown_generator.py`**: Markdown生成ロジックのテスト。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテスト。
    -   **`test_repository_processor.py`**: リポジトリ情報処理ロジックのテスト。

## 関数詳細説明
提供された情報からは具体的な関数詳細は特定できませんでした。しかし、プロジェクトの性質とファイル名から、以下のような主要な関数が各ファイル内に存在すると推測されます。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: スクリプトの主要なエントリポイント。GitHub APIからリポジトリ情報を取得し、他のモジュールを呼び出してMarkdownを生成する一連の処理を制御します。引数としてGitHubユーザー名、出力ファイル名、処理リポジトリ数上限などを受け取る可能性があります。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(repo_data)`: リポジトリデータに基づいて、表示するバッジ（例: 言語バッジ、ステータスバッジ）の情報を生成または取得します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリURLと設定に基づき、`generated-docs/project-overview.md`ファイルからプロジェクトの概要（3行説明）をフェッチします。

その他のファイルにも、それぞれの役割に応じたヘルパー関数やクラスメソッドが存在しますが、具体的な引数、戻り値、機能の詳細は提供情報からは特定できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は提供された情報からは分析できませんでした。
```

---
Generated at: 2026-06-28 07:25:50 JST
