Last updated: 2026-07-29

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を自動で取得し、GitHub Pages用のMarkdownファイルを生成するシステムです。
- ユーザーページでは検索されにくいリポジトリ情報を、SEOに最適化された形で公開し、検索エンジンやLLMからの参照を改善します。
- これにより、プロジェクトの認知度向上と、開発者・利用者の情報アクセス効率の向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤、生成されたMarkdownをWebサイトとして公開), **Markdown** (リポジトリ一覧や詳細ページとして自動生成されるコンテンツ形式)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール: **pytest** (Pythonコードのテストフレームワーク), **ruff** (Pythonの高速なリンター兼フォーマッター), **toml** (設定ファイル形式), **YAML** (設定ファイルやメッセージ管理に利用)
- テスト: **pytest** (コードの品質と動作の正確性を保証するためのテスト実行)
- ビルドツール: **Python** (リポジトリ情報からMarkdownファイルを生成する主要なスクリプト言語), **Jekyll** (GitHub Pages側でMarkdownファイルを静的Webサイトとしてビルド)
- 言語機能: **Python** (プロジェクトの主要な開発言語)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の自動取得に使用。システムが自動で情報を収集・生成する基盤となります)
- 開発標準: **ruff** (コードスタイルの一貫性を保ち、品質を向上させるための静的解析ツール)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリ（例: ビルド成果物、一時ファイル）を指定するファイル。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明するメインのドキュメント。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定（サイトタイトル、URL、テーマなど）を定義するファイル。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや単体テストを行うための補助スクリプト。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために利用されるファイル。
- **`index.md`**: メインの出力ファイル。`generate_repo_list.py` によって生成されたリポジトリ一覧のMarkdownコンテンツが格納されます。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を定義するファイル。ホーム画面アイコンや表示モードなどを指定します。
- **`pytest.ini`**: pytest テストフレームワークの設定ファイル。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージのリスト。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージのリスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイル。
- **`ruff.toml`**: ruff リンター/フォーマッターの設定ファイル。コードのスタイルや品質に関するルールを定義します。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能の自動テストコード。
- **`.github_automation/check_large_files/`**: GitHub Actionsと連携し、リポジトリ内の大きなファイルをチェックするための自動化スクリプトと設定。
  - `check-large-files.toml`: 大きなファイルチェック機能の設定ファイル。
  - `scripts/check_large_files.py`: 実際に大きなファイルを検出するPythonスクリプト。
- **`assets/`**: ウェブサイトで使用される静的アセット（例: ファビコン画像）を格納するディレクトリ。
- **`generated-docs/`**: 各リポジトリから取得された `project-overview.md` など、動的に生成されるドキュメントを一時的に格納する、または参照される場所。
- **`issue-notes/22.md`**: プロジェクトの課題や検討事項に関するメモファイル。
- **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なPythonモジュール群。
  - `__init__.py`: Pythonパッケージであることを示すファイル。
  - `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成する機能を提供します。
  - `config.yml`: プロジェクト概要取得機能など、本システム固有の設定パラメータを定義するファイル。
  - `config_manager.py`: `config.yml` やその他の設定ファイルを読み込み、管理する機能を提供します。
  - `date_formatter.py`: 日付や時刻の情報を特定のフォーマットに整形する機能を提供します。
  - `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプト。
  - `json_ld_template.json`: SEO強化のため、構造化データ（JSON-LD）のテンプレートを定義するファイル。
  - `language_info.py`: 各リポジトリの使用言語情報を処理・分析する機能を提供します。
  - `markdown_generator.py`: 取得したリポジトリ情報から、指定されたフォーマットでMarkdownコンテンツを生成する機能を提供します。
  - `project_overview_fetcher.py`: 各GitHubリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から概要情報を取得する機能を提供します。
  - `readme_badge_extractor.py`: 各リポジトリのREADMEからバッジ情報を抽出する機能を提供します。
  - `repository_processor.py`: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に変換する機能を提供します。
  - `seo_template.yml`: SEO（検索エンジン最適化）に特化したメタデータやテンプレート設定を定義するファイル。
  - `statistics_calculator.py`: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算する機能を提供します。
  - `strings.yml`: UIに表示されるメッセージや文言、テンプレートのテキストなどを一元管理するファイル。
  - `template_processor.py`: Markdown生成に使用するテンプレートの読み込みや、データとの結合を行う機能を提供します。
  - `url_utils.py`: URLの構築や解析など、URL関連のユーティリティ機能を提供します。
- **`tests/`**: プロジェクトの機能が正しく動作することを確認するための自動テストコードを格納するディレクトリ。
  - `conftest.py`: pytestのフィクスチャやヘルパー関数を定義し、テスト全体で共有する設定ファイル。
  - `test_badge_generator_integration.py`: `badge_generator.py` の統合テスト。
  - `test_check_large_files.py`: `.github_automation/check_large_files.py` のテスト。
  - `test_config.py`: 設定ファイルの読み込みや管理機能のテスト。
  - `test_date_formatter.py`: 日付フォーマット機能のテスト。
  - `test_environment.py`: 実行環境のセットアップに関するテスト。
  - `test_integration.py`: システム全体の主要な連携部分の統合テスト。
  - `test_markdown_generator.py`: Markdown生成機能のテスト。
  - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
  - `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテスト。
  - `test_repository_processor.py`: リポジトリ情報処理機能のテスト。

## 関数詳細説明
このプロジェクトは、複数のPythonスクリプトとモジュールで構成されており、各ファイルが特定の役割を担う関数群を提供しています。以下に主要なモジュールに含まれると推測される関数の役割を説明します。具体的な引数や戻り値は提供されていませんが、モジュールの機能に基づいた一般的な役割です。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: スクリプトのエントリーポイント。コマンドライン引数をパースし、リポジトリ情報の取得とMarkdown生成のプロセス全体を調整します。
    - `generate_repo_list()`: 指定されたユーザーのリポジトリ情報を取得し、処理して、最終的なMarkdownコンテンツを生成します。
- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge()`: リポジトリのプロパティ（例: 言語、ステータス）に基づいて、表示用のバッジ（例: Markdown形式の画像リンク）を生成します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config()`: 指定された設定ファイル（例: `config.yml`, `secrets.toml`）を読み込み、Pythonオブジェクトとして提供します。
- **`src/generate_repo_list/date_formatter.py`**:
    - `format_date()`: 日付オブジェクトを指定された文字列フォーマットに変換します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_markdown_content()`: 処理されたリポジトリデータとテンプレートを使用して、最終的なMarkdown形式の文字列を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview()`: 指定されたリポジトリの特定のパスにある概要ファイルから、プロジェクトの3行説明などを取得します。
    - `get_file_content_from_github()`: GitHub APIを使用して、特定のリポジトリのファイル内容を取得します。
- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repository()`: GitHub APIから取得した単一のリポジトリデータを受け取り、表示に必要な形式に整形・変換する処理を行います。
    - `get_repo_languages()`: 特定のリポジトリの使用言語情報を取得します。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - `calculate_statistics()`: リポジトリのスター数、フォーク数などの統計情報を計算または集計します。
- **`src/generate_repo_list/template_processor.py`**:
    - `render_template()`: テンプレートファイルに動的なデータを差し込み、最終的な出力を生成します。
- **`src/generate_repo_list/url_utils.py`**:
    - `build_github_api_url()`: GitHub APIエンドポイントのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-07-29 07:24:03 JST
