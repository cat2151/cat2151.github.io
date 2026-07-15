Last updated: 2026-07-16

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを自動作成します。
- これにより、サイトの検索エンジン可視性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages** (静的サイトジェネレータJekyllをベースとしたGitHub Pagesでコンテンツを表示)、**Markdown** (生成されるリポジトリ一覧のフォーマット)、**HTML/CSS** (Jekyllのテンプレートを通じて利用)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Ruff** (Pythonコードのフォーマットとリント)、**pytest** (Pythonコードの単体・結合テストフレームワーク)、**GitHub API** (リポジトリ情報取得のためのデータソース)
- テスト: **pytest** (Pythonコードのテスト実行フレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報取得からMarkdown生成までの一連の処理を実行)
- 言語機能: **Python** (プロジェクトの主要開発言語)
- 自動化・CI/CD: **GitHub Actions** (プロジェクト情報の記述から、リポジトリ一覧の自動生成とデプロイに使用されることが示唆される)
- 開発標準: **Ruff** (Pythonのコードスタイルと品質を維持するためのツール)

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
- **`.editorconfig`**: さまざまなエディタやIDEでコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連ファイルを格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルのチェックに関する自動化スクリプト群です。
        - **`README.md`**: `check_large_files` ディレクトリの目的や使い方を説明するファイルです。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明するメインのドキュメントです。
- **`_config.yml`**: GitHub Pagesが使用するJekyllの設定ファイルです。サイトのメタデータやテーマなどを定義します。
- **`assets/`**: サイトで利用される画像などの静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: サイトのファビコン（ブラウザタブなどに表示されるアイコン）のさまざまなサイズです。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグやテストに特化したスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得される`project-overview.md`などのドキュメントを一時的に格納したり、生成されたドキュメントの出力先として使用されることが想定されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧を表示するメインのMarkdownファイルです。
- **`issue-notes/`**: 課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（Issue #22など）に関するメモファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルで、ホーム画面への追加やオフライン対応などの設定が含まれます。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの実行方法や検出ルールなどを定義します。
- **`requirements-dev.txt`**: 開発環境で必要となるPythonライブラリ（テストツール、リンターなど）をリストしたファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要となる本番環境のPythonライブラリをリストしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは避けるべきかを指示するファイルです。
- **`ruff.toml`**: PythonのLinter/Formatterである`ruff`の設定ファイルです。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトのソースコードのルートディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示す空ファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の主要なロジックを格納するパッケージです。
        - **`__init__.py`**: Pythonパッケージを示す空ファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ画像を生成するロジックを扱います。
        - **`config.yml`**: `generate_repo_list`機能固有の設定（プロジェクト概要取得の設定など）を定義するYAMLファイルです。
        - **`config_manager.py`**: YAML設定ファイル（`config.yml`など）の読み込み、解析、および管理を担当するモジュールです。
        - **`date_formatter.py`**: リポジトリの作成日や更新日などを、Jekyllに適した形式や人間が読みやすい形式に整形する機能を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式のリポジトリ一覧を生成するメインスクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データであるJSON-LDのテンプレートファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語の情報を取得し、処理する機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報や設定に基づいて、最終的なMarkdownコンテンツを生成するロジックを扱います。
        - **`project_overview_fetcher.py`**: 各リポジトリから`project-overview.md`ファイルを読み込み、3行の概要を抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、特定のパターンで記述されたバッジ情報を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIからリポジトリ情報を取得し、フィルタリング、ソート、追加情報の付与などの前処理を行うロジックを扱います。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元的に管理するYAMLファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: 汎用的なテンプレート処理（例: MarkdownやHTMLテンプレートの変数置換）を行う機能を提供します。
        - **`url_utils.py`**: URLの構築、解析、検証など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストまたは結合テストを行うスクリプトです。
- **`tests/`**: プロジェクト全体のテストケースを格納するディレクトリです。
    - **`conftest.py`**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みと解析に関するテストです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストです。
    - **`test_environment.py`**: 環境設定や依存関係のテストです。
    - **`test_integration.py`**: プロジェクト全体の主要機能の統合的なテストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main()`**: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdownファイルの生成までの一連の処理を調整します。
        - **引数**: コマンドライン引数（例: `--username`, `--output`, `--limit`）
        - **戻り値**: なし
        - **機能**: 引数解析、設定読み込み、リポジトリ処理の開始、結果のファイル出力。
- **`src/generate_repo_list/repository_processor.py`**:
    - **`fetch_repositories(username: str, token: str, limit: Optional[int] = None) -> List[Dict]`**: 指定されたGitHubユーザーのリポジトリ情報をGitHub APIから取得します。
        - **引数**: `username` (GitHubユーザー名), `token` (GitHub個人アクセストークン), `limit` (取得するリポジトリ数の上限、任意)
        - **戻り値**: リポジトリ情報の辞書リスト
        - **機能**: GitHub APIへのリクエスト送信、リポジトリデータの取得と基本的なフィルタリング。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_url: str, config: Dict) -> Optional[str]`**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの3行概要を抽出します。
        - **引数**: `repo_url` (リポジトリのGitHub URL), `config` (プロジェクト概要取得に関する設定)
        - **戻り値**: 抽出された3行概要の文字列、または`None`
        - **機能**: リポジトリのURLから対象ファイルを読み込み、指定されたセクションから概要テキストをパースして抽出。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **`generate_markdown(repo_data: List[Dict], strings: Dict, config: Dict) -> str`**: 処理されたリポジトリ情報とテンプレート、設定に基づいて最終的なMarkdownコンテンツを生成します。
        - **引数**: `repo_data` (処理済みリポジトリ情報のリスト), `strings` (表示用文言), `config` (Markdown生成に関する設定)
        - **戻り値**: 生成されたMarkdown文字列
        - **機能**: リポジトリデータを整形し、Markdownの構造（ヘッダー、リストアイテム、バッジなど）を組み合わせて出力。
- **`src/generate_repo_list/config_manager.py`**:
    - **`load_config(config_path: str) -> Dict`**: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
        - **引数**: `config_path` (設定ファイルへのパス)
        - **戻り値**: 設定内容を表す辞書
        - **機能**: YAMLファイルのオープン、パース、データ構造としての提供。
- **`src/generate_repo_list/date_formatter.py`**:
    - **`format_date(iso_date: str, format_str: str = "%Y-%m-%d") -> str`**: ISO 8601形式の日付文字列を指定されたフォーマットで整形します。
        - **引数**: `iso_date` (ISO 8601形式の日付文字列), `format_str` (出力フォーマット文字列)
        - **戻り値**: フォーマットされた日付文字列
        - **機能**: 日付文字列の解析と再フォーマット。
- **`src/generate_repo_list/badge_generator.py`**:
    - **`create_badge_markdown(label: str, message: str, color: str = "blue") -> str`**: Shields.io形式のバッジMarkdown文字列を生成します。
        - **引数**: `label` (バッジの左側のテキスト), `message` (バッジの右側のテキスト), `color` (バッジの色)
        - **戻り値**: バッジのMarkdown形式の文字列
        - **機能**: 引数からバッジのURLを構築し、それを含むMarkdownリンクを生成。
- 他にも多数のユーティリティ関数が各モジュールに存在し、それぞれ特定のデータ処理、整形、抽出、計算などの役割を担っています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
しかし、一般的な構成として、`src/generate_repo_list/generate_repo_list.py`の`main()`関数が、`repository_processor.py`、`project_overview_fetcher.py`、`markdown_generator.py`などの各モジュール内の主要な関数を順次呼び出して処理を進めると推測されます。

---
Generated at: 2026-07-16 07:22:42 JST
