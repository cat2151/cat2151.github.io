Last updated: 2026-10-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownを自動生成します。
- 生成されたリポジトリ一覧ページは、検索エンジン最適化（SEO）とLLMの参照性向上に貢献します。
- 各リポジトリの概要表示、バッジ、分類機能などを備え、Jekyll環境に最適化されています。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll), Markdown (生成されるコンテンツ)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: YAML (設定ファイルフォーマット), Pythonスクリプト (Markdown生成のビルド機能)
- 言語機能: Python
- 自動化・CI/CD: GitHub Actions (スクリプトの実行環境として想定), _config.yml (Jekyllのサイト設定)
- 開発標準: ruff (Pythonコードフォーマッター/リンター), EditorConfig (エディタ設定統一)

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
- **`.editorconfig`**: 異なる開発環境間でのコードスタイル（インデント、改行など）を統一するための設定ファイル。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイル。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方などが記載されたプロジェクトのメインドキュメント。
- **`_config.yml`**: GitHub PagesがJekyllでサイトを生成する際に使用する設定ファイル。サイトのタイトル、テーマ、プラグインなどが定義されます。
- **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の各サイズ画像。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを行うための補助スクリプト（推測）。
- **`generated-docs/`**: 各リポジトリの `project-overview.md` など、生成されたドキュメントを一時的に格納、または参照するためのディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどの検索エンジンツールでサイトの所有権を確認するために配置されるファイル。
- **`index.md`**: メインスクリプトによって生成される、GitHubリポジトリ一覧を含むMarkdownファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定のIssue（問題やタスク）に関する詳細なメモや解決策を記述したドキュメント。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイル。アプリのアイコン、表示名、起動URLなどを指定します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイル。テストの検出ルールやオプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージのリスト。
- **`requirements.txt`**: プロジェクトが実行される本番環境で必要となるPythonパッケージのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンター兼フォーマッターであるRuffの設定ファイル。コードスタイルや静的解析ルールを定義します。
- **`src/__init__.py`**: Pythonのパッケージであることを示すファイル。`src` ディレクトリがPythonパッケージとして扱われることを意味します。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや情報を視覚的なバッジとして生成するロジックを実装したスクリプト。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプト自体の設定を定義するファイル（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）。
- **`src/generate_repo_list/config_manager.py`**: YAML設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのユーティリティスクリプト。
- **`src/generate_repo_list/date_formatter.py`**: GitHub APIから取得した日付情報を、読みやすい形式に整形するロジックを実装したスクリプト。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、加工、最終的なMarkdownファイルを生成するプロジェクトのメインスクリプト。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD形式）のテンプレートファイル。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報などを処理・表示するためのロジック（推測）。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なMarkdownコンテンツの文字列を生成するロジックを実装したスクリプト。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` からプロジェクトの3行概要を自動的に取得するロジック。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADME.mdファイルから既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジック。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出し、整形する主要な処理ロジック。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジック（推測）。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示文字列、文言、メッセージなどを一元的に管理するファイル。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレートファイル（もしあれば）を読み込み、動的なデータで埋め込む処理を行うスクリプト。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を集めたスクリプト。
- **`test_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) の単体テストスクリプト。
- **`tests/conftest.py`**: pytestのテスト実行時に共通で利用されるフィクスチャやヘルパー関数を定義するファイル。
- **`tests/test_badge_generator_integration.py`**: `badge_generator.py` の統合テストを行うスクリプト。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストスクリプト。
- **`tests/test_config.py`**: `config_manager.py` や `config.yml` などの設定関連機能のテストスクリプト。
- **`tests/test_date_formatter.py`**: `date_formatter.py` の日付整形機能のテストスクリプト。
- **`tests/test_environment.py`**: 実行環境の設定や依存関係が正しく動作するかを確認するテスト。
- **`tests/test_integration.py`**: プロジェクト全体の主要な機能が連携して正しく動作するかを確認する統合テスト。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py` のMarkdown生成機能のテストスクリプト。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のテストスクリプト。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のテストスクリプト。
- **`tests/test_repository_processor.py`**: `repository_processor.py` のテストスクリプト。

## 関数詳細説明
具体的な引数、戻り値の情報が提供されていないため、主要なスクリプトファイル名から推測される主要な関数の役割を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main()`**:
        - 役割: スクリプトの実行エントリーポイント。コマンドライン引数をパースし、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力までの一連のフローを制御します。
        - 引数: なし（またはコマンドライン引数が内部で処理される）。
        - 戻り値: なし（またはプログラムの終了ステータス）。
    - **`parse_arguments()`**:
        - 役割: コマンドラインから `--username`, `--output`, `--limit` などの引数を解析し、設定オブジェクトとして返します。
        - 引数: なし。
        - 戻り値: 解析された引数を含むオブジェクト。
- **`src/generate_repo_list/repository_processor.py`**:
    - **`process_repositories(username, token, limit=None)`**:
        - 役割: 指定されたユーザーのリポジトリ情報をGitHub APIから取得し、必要な情報（説明、言語、スター数など）を抽出し、整形されたデータ構造のリストとして返します。
        - 引数: `username` (str), `token` (str), `limit` (int, オプション)。
        - 戻り値: 処理されたリポジトリ情報のリスト。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **`generate_markdown(processed_repositories)`**:
        - 役割: 処理されたリポジトリデータのリストを受け取り、Jekyllの要件に合わせたMarkdown形式の文字列を生成します。
        - 引数: `processed_repositories` (list of dict)。
        - 戻り値: 生成されたMarkdownコンテンツの文字列。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_name, github_token, config)`**:
        - 役割: 指定されたリポジトリの特定のパス（例: `generated-docs/project-overview.md`）からファイル内容を読み込み、設定されたセクション（例: "プロジェクト概要"）から3行の要約を抽出して返します。
        - 引数: `repo_name` (str), `github_token` (str), `config` (dict)。
        - 戻り値: 抽出されたプロジェクト概要のリスト (list of str) または None。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-13 07:12:55 JST
