Last updated: 2026-06-15

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHubリポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdownで生成します。
- 検索エンジンへのインデックス促進とLLMによるリポジトリ参照精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesを構築するための静的サイトジェネレータ), Markdown (生成されるリポジトリ一覧コンテンツの記述言語)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (主要なスクリプト言語), ruff (Pythonコードのフォーマットとリンティングを行うツール)
- テスト: pytest (Pythonアプリケーションのテストフレームワーク)
- ビルドツール: Jekyll (最終的なウェブサイトのビルドに寄与する静的サイトジェネレータ)
- 言語機能: Python (スクリプト開発言語), TOML (secrets.tomlなど設定ファイルフォーマット), YAML (config.yml, strings.ymlなど設定ファイルフォーマット)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得), プロジェクト自体がリポジトリ一覧の自動生成を行うシステムとして機能します。
- 開発標準: ruff (コードスタイルを統一し、品質を維持するためのツール)

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
-   `.editorconfig`: 異なるエディタやIDE間でコードのフォーマットを統一するための設定ファイル。
-   `.github_automation/`: GitHub Actionsなどで利用する自動化スクリプトや設定を格納するディレクトリ。
    -   `check_large_files/README.md`: 大容量ファイルチェック機能に関する説明。
    -   `check_large_files/check-large-files.toml`: 大容量ファイルチェック機能の設定ファイル。
    -   `check_large_files/scripts/check_large_files.py`: 大容量ファイルを検出するためのPythonスクリプト。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定する設定ファイル。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）。
-   `README.md`: プロジェクトの概要、目的、使用方法などを説明するメインのドキュメント。
-   `_config.yml`: Jekyllサイト全体の挙動を設定するファイル。テーマ、プラグイン、パーマリンクなどを定義。
-   `assets/`: サイトで使用される画像やアイコンなどの静的リソースを格納するディレクトリ。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）ファイル。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグまたはテストに使用されるスクリプト。
-   `generated-docs/`: 生成されたドキュメントや一時ファイルを格納するディレクトリ（例: リポジトリごとの概要ファイル）。
-   `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権確認に使用されるHTMLファイル。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧が記述されたMarkdownファイル。GitHub Pagesのトップページとして機能します。
-   `issue-notes/22.md`: 特定の課題（Issue #22）に関するメモまたは詳細情報。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイル。アプリのメタデータや表示方法を定義。
-   `pytest.ini`: `pytest` テストフレームワークの設定ファイル。
-   `requirements-dev.txt`: 開発環境で必要となるPythonの依存関係を定義したファイル。
-   `requirements.txt`: プロジェクトの実行に必要なPythonの依存関係を定義したファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイル。
-   `ruff.toml`: `ruff` コードリンターおよびフォーマッターの設定ファイル。
-   `src/`: プロジェクトのソースコードを格納するメインディレクトリ。
    -   `src/__init__.py`: Pythonパッケージであることを示すファイル。
    -   `src/generate_repo_list/`: リポジトリ一覧生成機能のコアロジックを格納するパッケージ。
        -   `src/generate_repo_list/__init__.py`: `generate_repo_list` パッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリの各種バッジ（例: ライセンス、言語）を生成するロジックを実装。
        -   `config.yml`: リポジトリ一覧生成スクリプトの動作に関する設定（例: プロジェクト概要取得設定、APIタイムアウト）。
        -   `config_manager.py`: `config.yml` などの設定ファイルを読み込み、管理するクラスや関数を実装。
        -   `date_formatter.py`: 日付や時刻のフォーマット処理を行うユーティリティ関数を実装。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからの情報取得、処理、Markdown生成を統括します。
        -   `json_ld_template.json`: SEO強化のためのJSON-LD形式の構造化データテンプレート。
        -   `language_info.py`: リポジトリの主要言語情報を処理するロジックを実装。
        -   `markdown_generator.py`: 取得したデータに基づいて、最終的なリポジトリ一覧のMarkdown文字列を生成するロジックを実装。
        -   `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出・取得するロジックを実装。
        -   `readme_badge_extractor.py`: READMEファイルから既存のバッジ情報を抽出するロジックを実装。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリ情報を整形し、必要なデータ構造に変換するロジックを実装。
        -   `seo_template.yml`: SEO関連のメタデータや構造化データに関するテンプレート設定。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するロジックを実装。
        -   `strings.yml`: UIに表示される各種メッセージや文言を管理するリソースファイル。
        -   `template_processor.py`: Markdown生成に使用されるテンプレートファイルを読み込み、変数を埋め込む処理を実装。
        -   `url_utils.py`: URLの処理や生成に関するユーティリティ関数を実装。
-   `test_project_overview.py`: プロジェクト概要取得機能に関する単体テストスクリプト。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリ。
    -   `conftest.py`: pytestのフィクスチャやヘルパー関数を定義するファイル。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テスト。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテスト。
    -   `test_config.py`: 設定ファイルの読み込み・管理機能のテスト。
    -   `test_date_formatter.py`: 日付フォーマット機能のテスト。
    -   `test_environment.py`: 実行環境に関するテスト。
    -   `test_integration.py`: プロジェクト全体の主要なフローに関する統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリ情報処理機能のテスト。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、各ファイルにはその役割に応じた関数が実装されています。具体的な引数や戻り値はソースコードを参照する必要がありますが、以下に主要なファイルにおける関数の役割を説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **役割**: プロジェクトの中心となる実行関数。GitHub APIを通じてリポジトリ情報を取得し、他のモジュールの関数を呼び出してデータを処理し、最終的なMarkdownファイルを生成します。
    -   **機能**: コマンドライン引数の解析、GitHub APIクライアントの初期化、リポジトリ情報のフェッチ、各リポジトリの処理、Markdownファイルの出力を行います。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   **役割**: リポジトリのライセンス、言語、スター数などの情報を元に、表示用のバッジURLやMarkdownスニペットを生成する関数を提供します。
    -   **機能**: リポジトリデータを受け取り、指定されたタイプのバッジを表現する文字列を返します。
-   **`src/generate_repo_list/config_manager.py`**:
    -   **役割**: YAML形式の設定ファイル（`config.yml`など）を読み込み、設定値へのアクセスを管理する関数を提供します。
    -   **機能**: 設定ファイルのパスを受け取り、設定値を辞書やオブジェクトとして提供します。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   **役割**: 日付や時刻の情報を特定のフォーマット文字列（例: `YYYY-MM-DD`）に変換するユーティリティ関数を提供します。
    -   **機能**: 日付オブジェクトを受け取り、整形された日付文字列を返します。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **役割**: 処理されたリポジトリ情報とテンプレートを使用して、出力用のMarkdownコンテンツを構築する関数を提供します。
    -   **機能**: 整形済みリポジトリデータのリストを受け取り、リポジトリ一覧を含むMarkdown文字列を生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **役割**: 各リポジトリから指定されたファイル（`generated-docs/project-overview.md`）を読み込み、そこからプロジェクト概要の3行説明を抽出する関数を提供します。
    -   **機能**: リポジトリ名とファイルパスを受け取り、概要テキスト（リスト形式）を返します。GitHub APIを利用してファイルをフェッチします。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、Markdown生成に適した形式に変換・整形する関数を提供します。
    -   **機能**: 生のリポジトリデータを受け取り、必要な情報（名前、説明、URL、スター数、最終更新日など）を抽出・加工して返します。
-   **`src/generate_repo_list/template_processor.py`**:
    -   **役割**: Markdownテンプレートファイル（例: `seo_template.yml`）を読み込み、動的なデータを埋め込む処理を行う関数を提供します。
    -   **機能**: テンプレート文字列とデータ辞書を受け取り、データが埋め込まれた最終的な文字列を返します。
-   **`src/generate_repo_list/url_utils.py`**:
    -   **役割**: URLの生成、解析、エンコードなど、URLに関連するユーティリティ関数を提供します。
    -   **機能**: 例えば、GitHubリポジトリのURLを構築する機能など。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-15 07:29:12 JST
