Last updated: 2026-03-09

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- リポジトリ情報をGitHub APIから取得し、SEO最適化されたMarkdownファイルを生成します。
- 検索エンジンやLLMからのリポジトリ参照性を向上させ、開発効率の課題解決を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesで利用される静的サイトジェネレータの基盤)、Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語)、Pytest (テストフレームワーク)、Ruff (Pythonコードのフォーマッタおよびリンター)
- テスト: Pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: 該当なし (コンテンツ生成が主であり、一般的なビルドツールは使用していません)
- 言語機能: Python (スクリプトの記述に用いられるプログラミング言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリが存在するため、潜在的な自動化環境として利用されています)
- 開発標準: Ruff (コードの品質と一貫性を保つための静的解析ツール)

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
- **`.editorconfig`**: さまざまなエディタとIDEで一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック自動化スクリプトの説明。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックの設定ファイル。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: GitHub Actions等で利用される、リポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法などを説明するメインのドキュメントファイル。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。テーマ、プラグイン、変数の定義など。
- **`assets/`**: Jekyllサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグ用途で使用されるスクリプト。
- **`generated-docs/`**: `project-overview.md`などの生成されたドキュメントや一時ファイルを格納するディレクトリ（GitHub APIからの取得元）。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のためのHTMLファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧コンテンツが出力されるMarkdownファイル。
- **`issue-notes/22.md`**: 特定のIssueに関連するメモや詳細情報を記述したファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するマニフェストファイル。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイル。
- **`requirements-dev.txt`**: 開発環境およびテスト環境で必要なPythonパッケージのリスト。
- **`requirements.txt`**: 本番環境でこのプロジェクトが動作するために必要なPythonパッケージのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか指示するファイル。
- **`ruff.toml`**: PythonのLinterおよびフォーマッタであるRuffの設定ファイル。
- **`src/generate_repo_list/__init__.py`**: Pythonパッケージの初期化ファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やスター数などのバッジを生成するロジックを実装。
- **`src/generate_repo_list/config.yml`**: リポジトリ情報取得やMarkdown生成の各種設定を定義するYAMLファイル。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するモジュール。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のフォーマットを行うユーティリティ関数を提供。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからの情報取得からMarkdown生成までの一連の流れを実行。
- **`src/generate_repo_list/json_ld_template.json`**: SEO強化のために構造化データを埋め込むためのJSON-LDテンプレート。
- **`src/generate_repo_list/language_info.py`**: リポジトリの言語に関する情報を処理し、集計する機能を提供。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリ情報から最終的なMarkdownコンテンツを生成するロジック。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` から概要説明を抽出する機能。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルからバッジ情報を解析・抽出する。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを整形し、必要な情報を抽出する処理。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレートを定義するファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュール。
- **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージや文言を国際化・一元管理するためのYAMLファイル。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成におけるテンプレートエンジンの処理を担当。
- **`src/generate_repo_list/url_utils.py`**: URL関連の操作や解析を行うユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview`機能の単体テストスクリプト。
- **`tests/`**: プロジェクトの各種モジュールや機能に対するテストスクリプトを格納するディレクトリ。

## 関数詳細説明
- **`generate_repo_list.py` 内の `main()`**:
    - **役割**: プロジェクトのエントリポイント。GitHub APIからリポジトリ情報を取得し、取得したデータを処理、最終的にMarkdownファイルを生成する一連のプロセスを管理・実行します。
    - **引数**: 通常はコマンドライン引数（`--username`, `--output`, `--limit`など）を受け取ります。
    - **戻り値**: なし（ファイル出力が主な目的）。
    - **機能**: 設定の読み込み、GitHub APIクライアントの初期化、リポジトリデータのフェッチ、各リポジトリの処理、Markdown生成、ファイルへの書き出し。

- **`repository_processor.py` 内の `process_repository(repo_data)`**:
    - **役割**: 個々のGitHubリポジトリの生データを受け取り、表示に必要な形式に整形・加工します。
    - **引数**: `repo_data` (辞書型): GitHub APIから取得した単一リポジトリのデータ。
    - **戻り値**: 整形されたリポジトリデータ (辞書型)。
    - **機能**: リポジトリ名の抽出、説明の取得、言語情報の処理、最終更新日のフォーマット、スター数などの統計計算、プロジェクト概要の取得呼び出し。

- **`project_overview_fetcher.py` 内の `fetch_project_overview(repo_url, config)`**:
    - **役割**: 指定されたリポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を非同期で取得します。
    - **引数**: `repo_url` (文字列): リポジトリのURL、`config` (辞書型): 概要取得に関する設定（ファイルパス、セクションタイトルなど）。
    - **戻り値**: 抽出された3行の概要説明 (リスト型または文字列)、または取得に失敗した場合は空の文字列。
    - **機能**: HTTPリクエストによるファイル内容の取得、Markdown解析による指定セクションからのテキスト抽出、キャッシュ処理、リトライメカニズム。

- **`markdown_generator.py` 内の `generate_markdown(repo_list, config)`**:
    - **役割**: 処理済みのリポジトリデータリストと設定情報に基づき、GitHub Pages用の最終的なMarkdownコンテンツを生成します。
    - **引数**: `repo_list` (リスト型): 整形されたリポジトリデータのリスト、`config` (辞書型): Markdown生成に関する設定。
    - **戻り値**: 生成されたMarkdown文字列。
    - **機能**: テンプレート処理、リポジトリごとの情報の埋め込み、SEOメタデータの追加、バッジの生成呼び出し。

- **`config_manager.py` 内の `load_config(config_path)`**:
    - **役割**: 指定されたパスのYAMLファイルから設定情報を読み込み、Pythonの辞書形式で提供します。
    - **引数**: `config_path` (文字列): YAML設定ファイルのパス。
    - **戻り値**: 読み込まれた設定データ (辞書型)。
    - **機能**: YAMLファイルのオープンとパース、設定値のバリデーション（オプション）。

- **`badge_generator.py` 内の `generate_badge(badge_type, value)`**:
    - **役割**: 指定されたタイプと値に基づいて、リポジトリ表示用のバッジ（例: 言語バッジ、スター数バッジ）のMarkdownまたはHTMLスニペットを生成します。
    - **引数**: `badge_type` (文字列): バッジの種類、`value` (文字列または数値): バッジに表示する値。
    - **戻り値**: バッジを表すMarkdownまたはHTML文字列。
    - **機能**: バッジのテンプレート選択、値の整形、色付け（オプション）。

## 関数呼び出し階層ツリー
```
提供された情報では関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-09 07:06:49 JST
