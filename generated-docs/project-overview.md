Last updated: 2026-10-19

# Project Overview

## プロジェクト概要
- GitHub API を活用し、リポジトリ情報を自動で取得・整形するシステムです。
- Jekyll ベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルを静的サイトとしてホスティングし、公開するために使用されます。最終的な出力はMarkdown形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: **Python**: プロジェクトの主要なロジックを実装するためのスクリプト言語です。**pytest**: テストコードの実行と管理を行うためのPythonのテスティングフレームワークです。**ruff**: Pythonコードのスタイルチェックと自動フォーマットを行うための高速なリンター兼フォーマッターです。
- テスト: **pytest**: ユニットテスト、結合テスト、および機能テストを実行し、コードの品質と信頼性を保証するために使用されます。
- ビルドツール: **Pythonスクリプト (`generate_repo_list.py`)**: GitHub APIから取得したデータを基に、最終的なMarkdownファイルを生成する役割を担います。
- 言語機能: **Python**: HTTPリクエストによるAPI通信、ファイルI/O、文字列処理、データ構造の操作など、多岐にわたる言語機能が活用されています。
- 自動化・CI/CD: **GitHub Actions**: (`.github_automation/` ディレクトリに示唆がありますが、本プロジェクトはローカル開発重視と明記されています)。プロジェクト内では、主にユーティリティースクリプト (`check-large-files.py`) に関連する自動化の仕組みが考えられます。
- 開発標準: **ruff (`ruff.toml`)**: コードの構文やスタイルに関する統一ルールを強制し、コード品質を維持します。**.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタ間でコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイル。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック自動化スクリプトに関する説明ドキュメント。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックのルール設定ファイル。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリを指定する設定ファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などを説明するメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイル。GitHub Pagesの基本的な設定を定義します。
- **`assets/`**: ウェブサイトで使用される静的アセット（ファビコン画像など）を格納するディレクトリ。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイル。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを行うためのスクリプト。
- **`generated-docs/`**: 各リポジトリから取得した `project-overview.md` ファイルが配置されることを想定したディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。`generate_repo_list.py`によってリポジトリ一覧が生成され、このファイルに出力されます。
- **`issue-notes/22.md`**: 開発中の特定の課題や検討事項に関するメモ。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるWebアプリマニフェストファイル。
- **`pytest.ini`**: `pytest`の挙動をカスタマイズするための設定ファイル。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージのリスト。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行する際に必要なPythonパッケージのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: `ruff` linterおよびフォーマッターのルール設定ファイル。
- **`src/__init__.py`**: Pythonパッケージであることを示す空ファイル。
- **`src/generate_repo_list/__init__.py`**: Pythonパッケージであることを示す空ファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やライセンスなどの情報を元に、Markdown形式のバッジを生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得機能やAPIタイムアウトなど、プログラムの技術的パラメータを設定するためのYAMLファイル。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml` など) を読み込み、アプリケーション全体で利用可能な形で管理するモジュール。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプト。GitHub APIを呼び出し、リポジトリ情報を取得・処理し、最終的なMarkdownファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレート。SEO強化のため、検索エンジンにコンテンツの意味を正確に伝えるのに役立ちます。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリから取得した言語関連の情報を処理・整形する機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 処理済みのリポジトリデータを受け取り、指定されたフォーマットでMarkdownコンテンツを生成するコアモジュール。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` から3行のプロジェクト概要を抽出・取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報（例：CI/CDステータス、バージョン）を抽出する機能。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを詳細に処理し、必要な情報（説明、言語、星の数など）を抽出・整形するモジュール。
- **`src/generate_repo_list/seo_template.yml`**: サイト全体のSEO設定やメタデータを定義するためのテンプレートファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: 生成されるMarkdown内の各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイル。
- **`src/generate_repo_list/template_processor.py`**: 取得したデータと定義されたテンプレート（Markdown、HTMLなど）を組み合わせて最終的な出力を生成する汎用的なテンプレート処理モジュール。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能（`project_overview_fetcher.py`）に関するテストスクリプト。
- **`tests/conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義するための設定ファイル。
- **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
- **`tests/test_config.py`**: 設定ファイル (`config.yml`, `strings.yml`) の読み込みや管理機能のテスト。
- **`tests/test_date_formatter.py`**: 日付フォーマット機能のテスト。
- **`tests/test_environment.py`**: 実行環境（依存パッケージなど）のセットアップに関するテスト。
- **`tests/test_integration.py`**: プロジェクト全体の主要な処理フローに関する統合テスト。
- **`tests/test_markdown_generator.py`**: Markdown生成機能のテスト。
- **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
- **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテスト。
- **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供されたプロジェクト情報からは、具体的な関数シグネチャ（引数、戻り値）を詳細に特定できません。しかし、各ファイルの役割から以下の主要な関数の存在とその機能が推測されます。

- **`src/generate_repo_list/generate_repo_list.py` 内の `main` 関数**
    - **役割**: スクリプトのエントリポイントとして、GitHub APIからのリポジトリ情報取得、データ処理、Markdownファイル生成の一連の流れを制御します。
    - **引数**: 不明 (コマンドライン引数（ユーザー名、出力ファイル、リミットなど）を受け取る可能性があります)
    - **戻り値**: 不明 (スクリプトの成功/失敗を示す値など)
    - **機能**: ユーザー名と出力ファイルを指定してリポジトリリストを生成する主要なロジックを実行します。

- **`src/generate_repo_list/repository_processor.py` 内の `process_repository` 関数**
    - **役割**: 単一のGitHubリポジトリから取得した生データを解析し、Markdown生成に適した形式に整形します。
    - **引数**: 不明 (GitHub APIから取得した単一リポジトリの生データ)
    - **戻り値**: 不明 (整形され、Markdown生成に必要な情報が抽出されたリポジトリデータ)
    - **機能**: リポジトリ名、説明、言語、最終更新日などの情報を抽出し、必要に応じて他のヘルパー関数（例: `fetch_project_overview`）を呼び出して追加情報を取得します。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の `fetch_project_overview` 関数**
    - **役割**: 特定のリポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を非同期で取得します。
    - **引数**: 不明 (対象リポジトリのURL、設定情報オブジェクトなど)
    - **戻り値**: 不明 (抽出されたプロジェクト概要のテキスト、または取得失敗時のデフォルト値)
    - **機能**: GitHub APIを通じて指定されたファイルを読み込み、設定されたセクションタイトルに基づいて概要部分をパースし、指定された行数分の説明を抽出します。

- **`src/generate_repo_list/markdown_generator.py` 内の `generate_markdown_content` 関数**
    - **役割**: 処理済みのリポジトリ情報リストを受け取り、最終的なMarkdownコンテンツを生成します。
    - **引数**: 不明 (整形されたリポジトリデータリスト、文言データ、設定データなど)
    - **戻り値**: 不明 (生成されたMarkdown形式の文字列)
    - **機能**: 各リポジトリの情報をループ処理し、定義されたテンプレートやバッジ情報、SEO関連のメタデータなどを組み合わせて、整形されたMarkdown文字列を組み立てます。

- **`src/generate_repo_list/badge_generator.py` 内の `generate_badge` 関数**
    - **役割**: 特定のデータ（例: 言語、ライセンス）に基づいて、対応するMarkdown形式のバッジ文字列を生成します。
    - **引数**: 不明 (バッジ生成に必要なデータ、例: 言語名、ライセンスタイプ)
    - **戻り値**: 不明 (生成されたMarkdown形式のバッジ文字列)
    - **機能**: 入力データに応じたアイコン、テキスト、リンクなどを組み合わせ、視覚的に分かりやすいバッジを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-19 07:10:41 JST
