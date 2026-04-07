Last updated: 2026-04-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、JekyllベースのGitHub Pages向けリポジトリ一覧を自動生成します。
- SEO最適化とLLM参照性向上を目指し、ユーザーの全リポジトリ情報を可視化します。
- 各リポジトリの`project-overview.md`から概要を自動抽出し、リッチな表示を実現します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤でMarkdownをHTMLに変換し公開), Markdown (生成されるリポジトリ一覧コンテンツの形式)
- 音楽・オーディオ: (情報なし)
- 開発ツール: pytest (Pythonコードのテストフレームワーク), Ruff (Pythonコードの自動フォーマットおよびリンティングツール)
- テスト: pytest (Pythonコードの単体および統合テストフレームワークとして利用)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py` が主要なジェネレーターとして機能し、Markdownファイルを生成)
- 言語機能: Python (主要な開発言語として、GitHub APIとの連携、データ処理、Markdown生成ロジックの実装に使用)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得に利用), Pythonスクリプトによる自動生成 (リポジトリ一覧の作成プロセスを自動化)
- 開発標準: Ruff (コードスタイルの一貫性を保ち、品質を向上させるためのリンターおよびフォーマッター), .editorconfig (異なるエディタ間でのコーディングスタイル統一のための設定)

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
-   **.editorconfig**: エディタのコードスタイル設定（インデント、改行コードなど）を統一し、異なる開発環境間での一貫性を保ちます。
-   **.github_automation/**: GitHub ActionsなどのGitHub上での自動化処理に関連するファイルを格納するディレクトリです。
    -   **check_large_files/**: 大容量ファイルのチェックに関連する機能を含みます。
        -   **README.md**: `check_large_files`機能に関する説明ドキュメントです。
        -   **check-large-files.toml**: 大容量ファイルチェックの設定ファイルです。
        -   **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
-   **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   **README.md**: プロジェクトの概要、利用方法、設定、開発者向けヒントなどを記述したメインのドキュメントです。
-   **_config.yml**: Jekyllサイト全体のグローバル設定を定義するファイルです。
-   **assets/**: Jekyllサイトで使用する静的アセット（例: ファビコン）を格納するディレクトリです。
    -   **favicon-*.png**: ウェブサイトのファビコン画像ファイル群です。
-   **debug_project_overview.py**: `project_overview_fetcher`の機能のデバッグや個別テストに使用されるスクリプトです。
-   **generated-docs/**: 各リポジトリから自動取得・生成されたドキュメントや概要ファイルが格納されるディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleにおけるサイト所有権の確認に使用されるファイルです。
-   **index.md**: `generate_repo_list.py`スクリプトによって生成される、GitHubリポジトリの一覧を表示するメインページ（Markdown形式）です。JekyllによってHTMLに変換されます。
-   **issue-notes/22.md**: 特定のイシュー（ここではイシュー番号22）に関連するメモや草稿が格納されるディレクトリ内のファイルです。
-   **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するマニフェストファイルです。
-   **pytest.ini**: `pytest`テストフレームワークの実行設定を定義するファイルです。
-   **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージの依存関係を記述したファイルです。
-   **requirements.txt**: プロジェクトの本番環境で必要なPythonパッケージの依存関係を記述したファイルです。
-   **robots.txt**: 検索エンジンのクローラーに対して、サイトのどのページをクロールしてよいか、またすべきでないかを指示するファイルです。
-   **ruff.toml**: `ruff` (Pythonリンター/フォーマッター) のコードスタイルに関する設定を定義するファイルです。
-   **src/**: プロジェクトの主要なソースコードが格納されるルートディレクトリです。
    -   **generate_repo_list/**: リポジトリ一覧生成システムの主要ロジックを含むPythonパッケージです。
        -   **__init__.py**: Pythonパッケージの初期化ファイルです。
        -   **badge_generator.py**: リポジトリの技術スタックやステータスを示すバッジを生成するロジックを実装しています。
        -   **config.yml**: リポジトリ情報の取得方法や表示に関する技術的なパラメータを設定するファイルです。
        -   **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体で管理する機能を提供します。
        -   **date_formatter.py**: 日付情報を特定の形式に整形するためのユーティリティ関数を提供します。
        -   **generate_repo_list.py**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を調整します。
        -   **json_ld_template.json**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データ記述のテンプレートです。
        -   **language_info.py**: リポジトリの使用言語情報を処理し、整形する機能を提供します。
        -   **markdown_generator.py**: 取得したリポジトリ情報に基づいてMarkdownコンテンツを生成するコアロジックを担います。
        -   **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を自動で抽出する機能を提供します。
        -   **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、特定のバッジ情報を抽出する機能を提供します。
        -   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、表示に適した形に整形・加工する役割を担います。
        -   **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するファイルです。
        -   **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        -   **strings.yml**: UIメッセージや各種表示文言を一元管理するためのファイルで、文言の変更や多言語対応を容易にします。
        -   **template_processor.py**: Markdown生成に使用するテンプレートファイルの読み込みと処理を行います。
        -   **url_utils.py**: URLに関する共通のユーティリティ関数（例: URLの検証、整形）を提供します。
-   **test_project_overview.py**: `project_overview_fetcher.py`の機能に関する単体テストを定義するファイルです。
-   **tests/**: プロジェクトのテストスクリプトを格納するディレクトリです。
    -   **conftest.py**: `pytest`のテスト実行時に使用される共通のフィクスチャやヘルパー関数を定義するファイルです。
    -   **test_badge_generator_integration.py**: `badge_generator`モジュールの統合テストを定義します。
    -   **test_check_large_files.py**: 大容量ファイルチェック機能のテストを定義します。
    -   **test_config.py**: 設定ファイルの読み込みおよび管理機能のテストを定義します。
    -   **test_date_formatter.py**: 日付フォーマット機能のテストを定義します。
    -   **test_environment.py**: 実行環境に関するテストを定義します。
    -   **test_integration.py**: 主要なコンポーネント間の統合テストを定義します。
    -   **test_markdown_generator.py**: Markdown生成機能のテストを定義します。
    -   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストを定義します。
    -   **test_readme_badge_extractor.py**: `README.md`からのバッジ抽出機能のテストを定義します。
    -   **test_repository_processor.py**: リポジトリ情報処理機能のテストを定義します。

## 関数詳細説明
提供された情報からは具体的な関数の詳細（役割、引数、戻り値、機能）を抽出できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-08 07:15:59 JST
