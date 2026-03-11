Last updated: 2026-03-12

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得するシステムです。
- 取得した情報から、GitHub Pages向けのSEO最適化されたMarkdownファイルを自動生成します。
- 検索エンジンからの発見性を高め、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: **GitHub Pages** (Jekyllベースの静的サイトホスティング), **Jekyll** (Markdownファイルを静的サイトに変換するジェネレーター), **Markdown** (リポジトリ一覧のコンテンツ生成形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: **Python** (主要なスクリプト言語), **GitHub API** (リポジトリ情報取得のためのインターフェース), **Git** (バージョン管理システム), **VS Code** (一般的な統合開発環境として想定)
- テスト: **pytest** (Pythonプロジェクトのテストフレームワーク)
- ビルドツール: **Python** (スクリプト実行によりMarkdownファイルを生成)
- 言語機能: **Python** (オブジェクト指向プログラミング、標準ライブラリ、データ構造など一般的な言語機能)
- 自動化・CI/CD: 本プロジェクトの目的自体が自動生成ですが、CI/CDパイプラインは「CI/CD不要のローカル開発重視」とされており、特に導入されていません。Pythonスクリプトの実行による**自動化**が主な要素です。
- 開発標準: **ruff** (Pythonコードの高速リンター/フォーマッター), **.editorconfig** (各種エディタでコードスタイルを統一するための設定)

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルを検知・管理するためのツール群を格納します。
        -   **`README.md`**: `check_large_files`ツールの説明ドキュメントです。
        -   **`check-large-files.toml`**: `check_large_files`ツールの設定ファイルです。
        -   **`scripts/check_large_files.py`**: 大容量ファイルをチェックするPythonスクリプト本体です。
-   **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリ（例: ビルド成果物、ログ、一時ファイルなど）を指定する設定ファイルです。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
-   **`README.md`**: プロジェクトの目的、機能、使い方、開発者向けのヒントなどが記述された主要なドキュメントファイルです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン設定などが含まれます。
-   **`assets/`**: Jekyllサイトで使用される画像やファビコンなどの静的アセットを格納するディレクトリです。
    -   **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズが格納されています。
-   **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグや単体テスト実行のために使用されるスクリプトです。
-   **`generated-docs/`**: 生成されたドキュメントや、特定の機能（例: プロジェクト概要取得）の対象となるドキュメントが置かれることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルで、このプロジェクトによって自動生成されたリポジトリ一覧が格納されます。
-   **`issue-notes/`**: 課題や特定のイシューに関するメモや詳細情報を格納するディレクトリです。
    -   **`22.md`**: 特定のイシュー（恐らくイシュー番号22）に関するメモのMarkdownファイルです。
-   **`manifest.json`**: Progressive Web App (PWA) の設定ファイルで、ウェブアプリの名称、アイコン、表示モードなどを定義します。
-   **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。テストの検出方法やプラグイン設定などが含まれます。
-   **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージとそのバージョンを記述したファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境用のPythonパッケージとそのバージョンを記述したファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイルです。
-   **`ruff.toml`**: PythonコードのリンターであるRuffの設定ファイルです。コードスタイルや潜在的なバグの検出ルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   **`__init__.py`**: Pythonパッケージを示すための空ファイル、またはパッケージ初期化コードを含むファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧生成のメインロジックを含むPythonパッケージです。
        -   **`__init__.py`**: このディレクトリがPythonパッケージであることを示します。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを実装します。
        -   **`config.yml`**: プロジェクト概要取得機能などの、スクリプト実行時の各種技術的パラメータを設定するYAMLファイルです。
        -   **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        -   **`date_formatter.py`**: GitHub APIから取得した日付情報を指定された形式にフォーマットする機能を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        -   **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために構造化データを埋め込むJSON-LDのテンプレートファイルです。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語の情報を処理・整形する機能を提供します。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、最終的なMarkdownコンテンツを生成するロジックを実装します。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、整形する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出する機能を提供します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報に加工する主要な処理を担います。
        -   **`seo_template.yml`**: 検索エンジン最適化に関連するテンプレート設定を定義するYAMLファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        -   **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元的に管理するためのYAMLファイルです。
        -   **`template_processor.py`**: Markdown生成などで使用されるテンプレートエンジンを処理する機能を提供します。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を集めたモジュールです。
-   **`test_project_overview.py`**: `project_overview_fetcher`モジュールに関連するテストケースを記述したスクリプトです。
-   **`tests/`**: プロジェクトの自動テストコードを格納するディレクトリです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストを行うスクリプトです。
    -   **`test_check_large_files.py`**: `check_large_files`ツールのテストを行うスクリプトです。
    -   **`test_config.py`**: 設定管理モジュール（`config_manager.py`）のテストを行うスクリプトです。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテストを行うスクリプトです。
    -   **`test_environment.py`**: 実行環境の設定や依存関係に関するテストを行うスクリプトです。
    -   **`test_integration.py`**: プロジェクト全体の主要なフローに関する総合的な結合テストを行うスクリプトです。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテストを行うスクリプトです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うスクリプトです。
    -   **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを行うスクリプトです。
    -   **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うスクリプトです。

## 関数詳細説明
このプロジェクトでは、以下の主要な機能領域にわたって関数が提供されていると想定されます。具体的な引数や戻り値は提供されていませんが、各関数の役割はファイル名やプロジェクトの目的から推測できます。

-   **メイン実行関数 (`generate_repo_list.py`内)**
    -   **役割**: プログラムのエントリーポイントであり、リポジトリ一覧生成の全体フローを管理します。
    -   **機能**: コマンドライン引数の解析、GitHubトークンの読み込み、リポジトリデータの取得、各リポジトリの処理、Markdown生成、ファイル出力といった一連のプロセスをオーケストレーションします。

-   **リポジトリデータ取得・処理関数 (`repository_processor.py`内)**
    -   **役割**: GitHub APIからリポジトリ情報を取得し、後続の処理に適した形に整形します。
    -   **機能**: GitHub APIへのリクエスト送信、APIレスポンスのパース、不要なデータのフィルタリング、必要な情報の抽出とデータ構造への格納を行います。

-   **プロジェクト概要取得関数 (`project_overview_fetcher.py`内)**
    -   **役割**: 各リポジトリの特定ファイルからプロジェクト概要のテキストを抽出します。
    -   **機能**: GitHub APIを介してリポジトリ内の指定ファイルを読み込み、特定のセクション（例: "プロジェクト概要"）から指定行数のテキストを抽出し、キャッシュ管理も行います。

-   **Markdown生成関数 (`markdown_generator.py`, `template_processor.py`内)**
    -   **役割**: 取得・整形されたリポジトリ情報と抽出されたプロジェクト概要を元に、GitHub Pages用のMarkdownコンテンツを作成します。
    -   **機能**: テンプレートとデータを結合し、リポジトリ名、説明、言語、バッジ、概要、リンクなどを含む整形されたMarkdown文字列を生成します。

-   **バッジ生成関数 (`badge_generator.py`内)**
    -   **役割**: リポジトリの特定の属性（言語、ステータスなど）に対応するバッジのマークダウンコードを生成します。
    -   **機能**: 指定された情報に基づき、Shields.ioなどのサービスを利用してバッジのURLと表示名を組み立て、Markdown形式で出力します。

-   **設定管理関数 (`config_manager.py`内)**
    -   **役割**: プログラムの設定ファイル（例: `config.yml`）の読み込みとアクセスを提供します。
    -   **機能**: YAMLファイルなどをパースし、設定値をプログラム内で簡単に参照できるようにオブジェクトとして提供します。

-   **ユーティリティ関数 (`date_formatter.py`, `url_utils.py`, `statistics_calculator.py`, `language_info.py`など)**
    -   **役割**: 日付のフォーマット、URLの操作、統計情報の計算、言語情報の解析といった特定の補助的な処理を行います。
    -   **機能**: それぞれのドメインに特化した処理（例: 日付文字列の変換、URLのエンコード/デコード、星数の合計計算など）を提供し、メインロジックの可読性を高めます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-12 07:09:08 JST
