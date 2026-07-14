Last updated: 2026-07-15

# Project Overview

## プロジェクト概要
- GitHub APIでリポジトリ情報を取得し、GitHub Pages向けMarkdownを自動生成するシステムです。
- Jekyllベースの個人サイトにリポジトリ一覧を公開し、検索エンジンからの発見性を高めます。
- SEO最適化されたコンテンツ生成により、LLMによる参照失敗の緩和も目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータで、MarkdownをHTMLに変換), **Markdown** (リポジトリ一覧のコンテンツ記述形式)
- 音楽・オーディオ: なし
- 開発ツール: **pytest** (Python用テストフレームワーク), **ruff** (Pythonコードの高速リンターおよびフォーマッタ), **Git** (バージョン管理システム), **GitHub** (リポジトリホスティングおよびAPI提供プラットフォーム)
- テスト: **pytest** (Pythonコードの単体テストおよび結合テストフレームワーク)
- ビルドツール: **Jekyll** (GitHub Pages環境で、生成されたMarkdownファイルを静的ウェブサイトとしてビルドする役割を間接的に担います)
- 言語機能: **Python** (メインの開発言語), **YAML** (設定ファイルや文字列定義に使用), **TOML** (シークレット情報の設定ファイルに使用)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の取得に利用), **GitHub Actions** (プロジェクトの性質上、GitHub Pagesへの自動デプロイや更新に利用されることが想定されます)
- 開発標準: **ruff** (コードスタイルの一貫性を保ち、品質を向上させるためのリンティングおよびフォーマットツール)

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsなどの自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/README.md`**: `check_large_files`ツールの使用方法や説明が記述されたドキュメント。
    -   **`check_large_files/check-large-files.toml`**: `check_large_files.py`スクリプトの設定を定義するTOML形式のファイル。
    -   **`check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
-   **`README.md`**: プロジェクトの概要、機能、セットアップ方法、使用例などを記述した主要なドキュメント。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの動作を制御します。
-   **`assets/`**: GitHub Pagesサイトで利用される静的なアセット（アイコン画像など）を格納するディレクトリ。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズ画像。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) の動作確認やデバッグを目的とした補助スクリプト。
-   **`generated-docs/`**: 生成されたドキュメントや、参照元となる特定のドキュメントを格納するためのディレクトリ（例: 各リポジトリの概要ファイル）。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイル。
-   **`index.md`**: 生成されたリポジトリ一覧の最終的な出力先となるMarkdownファイル。GitHub Pagesのトップページとして表示されます。
-   **`issue-notes/`**: 開発中の課題やノートをまとめたディレクトリ。
    -   **`22.md`**: 特定の課題（おそらくIssue #22）に関する詳細なメモや考察を記述したMarkdownファイル。
-   **`manifest.json`**: ウェブサイトをプログレッシブウェブアプリ（PWA）として動作させるための設定を記述したファイル。
-   **`pytest.ini`**: `pytest`フレームワークの実行設定やオプションを定義するファイル。
-   **`requirements-dev.txt`**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンをリストしたファイル。
-   **`requirements.txt`**: 本番環境で必要となるPythonパッケージとそのバージョンをリストしたファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、どのページを避けるべきかを指示するファイル。
-   **`ruff.toml`**: Pythonコードのリンティングとフォーマットを行う`ruff`ツールの設定ファイル。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   **`src/__init__.py`**: Pythonのパッケージであることを示すファイル。
    -   **`src/generate_repo_list/`**: リポジトリ一覧を生成するコアロジックを含むPythonパッケージ。
        -   **`src/generate_repo_list/__init__.py`**: サブパッケージであることを示すファイル。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジ画像を生成または整形する機能を提供するPythonモジュール。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを定義するYAML形式の設定ファイル。
        -   **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で設定値を管理するためのPythonモジュール。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するPythonモジュール。
        -   **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、それを加工して最終的なMarkdownファイルを生成する、このシステムのメイン実行スクリプト。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためにJSON-LD形式の構造化データを生成するためのテンプレートファイル。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するPythonモジュール。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するPythonモジュール。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`など）からプロジェクトの概要文を自動的に取得するPythonモジュール。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するPythonモジュール。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形・フィルタリングするPythonモジュール。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや、検索エンジン向けのコンテンツ生成に関する設定を定義するYAMLファイル。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するPythonモジュール。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーションで表示される各種メッセージや文言を国際化・一元管理するためのYAMLファイル。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートの読み込み、変数置換などの処理を行うPythonモジュール。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証などの汎用的なユーティリティ関数を提供するPythonモジュール。
-   **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が期待通りに動作するかを検証するためのテストスクリプト。
-   **`tests/`**: プロジェクト全体のテストスクリプトが格納されているディレクトリ。
    -   **`conftest.py`**: `pytest`のテスト実行時に共有されるフィクスチャや共通設定を定義するファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを行うスクリプト。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files`スクリプトの単体テストを行うスクリプト。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能 (`config_manager.py`) のテストを行うスクリプト。
    -   **`test_date_formatter.py`**: 日付フォーマット機能 (`date_formatter.py`) のテストを行うスクリプト。
    -   **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストを行うスクリプト。
    -   **`test_integration.py`**: システム全体または主要なコンポーネント間の連携を検証する統合テストスクリプト。
    -   **`test_markdown_generator.py`**: `markdown_generator`モジュールのテストを行うスクリプト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのテストを行うスクリプト（`test_project_overview.py`と役割が重複している可能性あり、またはより広範なテスト）。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのテストを行うスクリプト。
    -   **`test_repository_processor.py`**: `repository_processor`モジュールのテストを行うスクリプト。

## 関数詳細説明
このプロジェクトでは、特定の関数の引数、戻り値、詳細な機能についての情報が直接提供されていません。しかし、各Pythonモジュールの役割から、そこにどのような関数が存在するかを推測し、その概要を説明します。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   リポジトリの言語やステータスを示すバッジ（例：Python、JavaScript、アーカイブなど）を生成・取得・整形するための関数群。
    -   主に、入力されたリポジトリ情報に基づいて、表示すべきバッジのURLやテキストを返す機能を提供します。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `config.yml`や`strings.yml`などのYAML形式の設定ファイルを読み込み、その内容をアプリケーション全体で利用可能な形式で管理するための関数群。
    -   設定値の取得、デフォルト値の提供、設定のバリデーションなどの機能を含みます。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   リポジトリの作成日や最終更新日などの日付データを、人間が読みやすい形式や特定のロケールに合わせた形式に整形するための関数群。
    -   例えば、ISOフォーマットの日付文字列を受け取り、「YYYY年MM月DD日」形式に変換する機能などが考えられます。
-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   このプロジェクトのメインとなる実行ファイルであり、GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdownコンテンツを生成する主要な関数群。
    -   コマンドライン引数の解析、GitHub APIへのリクエスト送信、取得データの処理、Markdownコンテンツの組み立て、ファイルへの書き込みなど、一連のワークフローをオーケストレートする機能を提供します。
-   **`src/generate_repo_list/language_info.py`**:
    -   リポジトリの主要言語情報（GitHub APIから取得されるもの）を解析し、表示に適した形式（例：言語名とパーセンテージ、色情報など）に変換するための関数群。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   整形されたリポジトリデータやその他の情報を基に、最終的なリポジトリ一覧のMarkdown形式の文字列を生成するための関数群。
    -   テンプレート処理モジュールと連携し、データとテンプレートを組み合わせて出力コンテンツを作成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出・取得するための関数群。
    -   HTTPリクエスト（GitHubのrawファイル取得など）を実行し、指定されたセクションからテキストをパースして抽出する機能が含まれます。
-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   リポジトリの`README.md`ファイルの内容を解析し、そこに埋め込まれた特定のバッジ情報（例: CI/CDステータスバッジ）を抽出するための関数群。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   GitHub APIから取得した個々のリポジトリオブジェクトを受け取り、そこから必要な情報を抽出し、整形・フィルタリングして、Markdown生成に適したデータ構造に変換するための関数群。
    -   アクティブ/アーカイブ/フォークの分類、スター数、フォーク数などのメタデータの処理を行います。
-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   リポジトリのスター数、フォーク数、issue数など、様々な統計情報を計算・集計するための関数群。
-   **`src/generate_repo_list/template_processor.py`**:
    -   Markdownコンテンツ生成に使用されるテンプレートファイル（文字列、またはファイルパス）を読み込み、プレースホルダーを実際のデータで置き換えるための関数群。
    -   シンプルな文字列置換から、Jinja2のようなより高度なテンプレートエンジンを利用する機能までが考えられます。
-   **`src/generate_repo_list/url_utils.py`**:
    -   GitHubリポジトリのURL、APIエンドポイントのURLなど、URLに関連する操作（生成、検証、エンコードなど）を行うための汎用ユーティリティ関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-15 07:22:40 JST
