Last updated: 2026-06-07

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を取得・整理します。
- JekyllベースのGitHub Pages向けに、SEOを意識したリポジトリ一覧を自動生成します。
- 検索エンジンからのアクセス性とLLMによる参照性を向上させ、プロジェクト公開を支援します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesの静的サイトジェネレーター。本システムが生成するMarkdownファイルはJekyllによって処理され、ウェブサイトとして公開されます。
    - Markdown: GitHub Pagesサイトのコンテンツを記述するために、本システムが生成する軽量マークアップ言語です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語であり、リポジトリ情報取得、データ処理、Markdown生成のコアロジックを実装しています。
    - GitHub API: GitHubのリポジトリ情報（説明、言語、スター数など）をプログラムから取得するためのREST APIです。
- テスト:
    - pytest: Pythonアプリケーションのテストフレームワーク。コードの品質と信頼性を確保するための単体テストおよび結合テストに使用されます。
- ビルドツール:
    - Python: スクリプトの実行環境として利用されます。
    - YAML: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`など）の記述形式として使用され、柔軟な設定管理を実現します。
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語であり、その豊富なライブラリと表現力豊かな構文を活用してシステムが構築されています。
- 自動化・CI/CD:
    - GitHub API: リポジトリ情報の自動取得機能により、手動でのリスト更新作業を不要にしています。
    - GitHub Pages: 自動生成されたMarkdownファイルを静的サイトとして自動デプロイするGitHubのホスティングサービスです。
- 開発標準:
    - ruff: Pythonコードの品質を維持するための高速なリンター兼フォーマッター。コードの一貫性と可読性を確保します。

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
- **`.editorconfig`**: 複数のエディタやIDE間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub ActionsなどのCI/CDや自動化プロセスに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックする自動化ワークフローに関連するファイル群です。
        - **`README.md`**: `check_large_files`機能の目的や使い方を説明するドキュメントです。
        - **`check-large-files.toml`**: `check_large_files.py`スクリプトのための設定を定義するファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、警告を発するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス条文ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法など、全体概要を説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。テーマ、プラグイン、パーマリンク構造などが含まれます。
- **`assets/`**: GitHub Pagesサイトで利用される画像、アイコン、CSSなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像です。様々なサイズが提供されています。
- **`debug_project_overview.py`**: `project_overview`機能が正しく動作するかをデバッグするための補助スクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されるプロジェクト概要などのドキュメントが格納される、または参照されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでウェブサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: メインの実行スクリプトによって生成されるリポジトリ一覧が書き出されるMarkdownファイルです。GitHub Pagesサイトのトップページとして機能します。
- **`issue-notes/`**: 開発中に発生した課題や検討事項を記録するためのメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（例: Issue番号22）に関する詳細なメモや考察を記述したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示名、アイコン、起動時の動作などを定義します。
- **`pytest.ini`**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境用のPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター/フォーマッターであるRuffの設定を定義するファイルです。コードスタイルの一貫性を保ちます。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして認識させるための空のファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するシステムの主要なロジックを格納するPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリの言語やスター数などを表示するためのバッジ（マークダウン形式）を生成するロジックを管理します。
        - **`config.yml`**: プロジェクト概要取得機能などの、システムの技術的なパラメータや動作設定を定義するファイルです。
        - **`config_manager.py`**: YAMLファイルや環境変数から設定情報を読み込み、管理する役割を担います。
        - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマット（例: "YYYY-MM-DD"）に整形するユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このシステムのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、整形し、最終的なMarkdownファイルを生成する一連の処理を orchestrateします。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`language_info.py`**: GitHubリポジトリの主要言語情報などを処理し、表示に適した形に整形するロジックを含みます。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動的に抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジの情報を抽出するロジックを扱います。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（説明、トピック、最終更新日など）を抽出・整形する役割を担います。
        - **`seo_template.yml`**: SEO関連のメタデータや、検索エンジン向けのコンテンツ生成に関するテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（例: 全リポジトリの合計スター数、言語ごとの分布など）を計算する機能を提供します。
        - **`strings.yml`**: 生成されるMarkdownや表示メッセージにおける、各種文言やフレーズを一元的に管理するためのファイルです。
        - **`template_processor.py`**: Markdown生成時に、定義されたテンプレートに変数を埋め込むなどのテンプレート処理を行う機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を含みます。
- **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストまたは統合テストを記述したスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestにおいて、テスト実行前に共通で利用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合的な動作を検証するテストスクリプトです。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトの正確な動作を検証するテストです。
    - **`test_config.py`**: `config_manager`モジュールにおける設定の読み込みや管理機能のテストです。
    - **`test_date_formatter.py`**: `date_formatter`モジュールの日付整形機能の正確性を検証するテストです。
    - **`test_environment.py`**: テスト実行環境の設定や依存関係が正しく準備されているかを検証するテストです。
    - **`test_integration.py`**: システム全体、または主要なコンポーネンス間の連携を検証する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator`モジュールが正しいMarkdownコンテンツを生成するかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの概要抽出機能のテストです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールがREADMEから正しくバッジを抽出できるかを検証するテストです。
    - **`test_repository_processor.py`**: `repository_processor`モジュールがGitHub APIからのデータを適切に処理・整形できるかを検証するテストです。

## 関数詳細説明
（提供された情報では個別の関数の引数、戻り値、呼び出し関係の分析が困難なため、ファイル名から推測される主要な関数の役割について説明します。）

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main()`**: プロジェクトのエントリポイントとなる主要関数です。GitHub APIからリポジトリ情報を取得し、整形処理を経て、最終的なMarkdown形式のリポジトリ一覧を生成する一連の流れを制御します。
    - **`parse_arguments()`**: コマンドライン引数（例: `--username`, `--output`, `--limit`）を解析し、スクリプトで利用可能な形式に変換します。
- **`src/generate_repo_list/badge_generator.py`**
    - **`generate_badge_markdown(language: str, stars: int) -> str`**: 指定されたプログラミング言語とスター数を基に、リポジトリ表示用のバッジのMarkdown形式文字列を生成します。
- **`src/generate_repo_list/config_manager.py`**
    - **`load_config(config_path: str) -> dict`**: 指定されたYAMLファイルパスから設定情報を読み込み、辞書形式で返します。
    - **`get_secret(key: str) -> str`**: `secrets.toml`ファイルや環境変数から、GitHubトークンなどの機密情報を安全に取得します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_url: str, config: dict) -> list[str]`**: 指定されたGitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出し、文字列のリストとして返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_repository_list_markdown(repos: list[dict], config: dict) -> str`**: 処理済みのリポジトリ情報（辞書のリスト）と設定情報を受け取り、それらを整形してHTML/Markdown形式のリポジトリ一覧文字列を生成します。
- **`src/generate_repo_list/repository_processor.py`**
    - **`process_repository_data(raw_repo_data: dict) -> dict`**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を受け取り、表示に必要な情報（説明、言語、最終更新日、トピックなど）を抽出し、整理された辞書形式で返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-07 07:26:36 JST
