Last updated: 2026-11-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト向けのリポジトリ一覧を自動生成するシステムです。
- SEOに最適化されたMarkdownファイルを生成することで、リポジトリ情報を検索エンジンに認識させやすくします。
- これにより、LLMがGitHubリポジトリを参照できない課題を緩和し、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトのレンダリングエンジン)、Markdown (リポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール:
    - Ruff: Pythonコードのフォーマットとリンティングを行うツール。
    - Pytest: Python製のテストフレームワーク。
    - YAML: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用。
    - TOML: 秘密情報 (`secrets.toml`) や設定ファイル (`ruff.toml`, `check-large-files.toml`) の記述に使用。
- テスト: Pytest (ユニットテストおよび結合テストフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIからのデータ取得とMarkdown生成の中心)
- 言語機能: Python (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得)、ローカルスクリプト (リポジトリ一覧の自動生成)。`.github_automation` ディレクトリが存在しますが、本プロジェクトはCI/CDよりもローカル開発が重視されています。
- 開発標準: Ruff (コードスタイル統一)、.editorconfig (エディタ間の設定統一)

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者が、プロジェクト全体で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定ファイルを格納するためのディレクトリ。
    -   **`check_large_files/`**: 大容量ファイルを検出・管理するための自動化スクリプト群。
        -   **`README.md`**: `check_large_files` ディレクトリの目的や使い方を説明するファイル。
        -   **`check-large-files.toml`**: `check_large_files.py` スクリプトの動作を設定するためのTOML形式の設定ファイル。
        -   **`scripts/check_large_files.py`**: Gitリポジトリ内の指定されたサイズを超えるファイルをチェックするためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトはMITライセンス）。
-   **`README.md`**: プロジェクトの概要、目的、使い方、設定、クイックスタートガイドなどを記述する主要なドキュメントファイル。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動を制御する設定ファイル。サイトのタイトル、テーマ、プラグインなどが定義されます。
-   **`assets/`**: ウェブサイトで使用される静的リソース（画像、ファビコンなど）を格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像。異なるサイズが用意されています。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py` の機能) をデバッグするための補助スクリプト。
-   **`generated-docs/`**: 自動生成されたドキュメントや一時的なファイルを格納するためのディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどでサイトの所有権を確認するために使用されるHTMLファイル。
-   **`index.md`**: GitHub Pagesサイトのトップページとして表示されるMarkdownファイル。`generate_repo_list.py` の実行結果がここに出力されます。
-   **`issue-notes/`**: プロジェクトの課題や検討事項に関するメモを格納するディレクトリ。
    -   **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモや考察を記述したMarkdownファイル。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの名称、アイコン、表示モードなどを定義します。
-   **`pytest.ini`**: Pytestフレームワークの実行オプションや設定を記述するファイル。
-   **`requirements-dev.txt`**: 開発環境でのみ必要なPythonパッケージとそのバージョンを記述するファイル。
-   **`requirements.txt`**: プロジェクトの本番環境（実行時）で必要なPythonパッケージとそのバージョンを記述するファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイル。
-   **`ruff.toml`**: PythonコードのリンティングとフォーマットツールであるRuffの設定ファイル。コード品質とスタイルを維持します。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   **`__init__.py`**: Pythonパッケージであることを示す空ファイル。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧生成システムの主要なモジュール群。
        -   **`__init__.py`**: Pythonパッケージであることを示す空ファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ画像を生成または処理する機能を提供します。
        -   **`config.yml`**: プロジェクト概要の取得機能など、リポジトリ一覧生成に関する技術的なパラメータを設定するYAMLファイル。
        -   **`config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、アプリケーション全体で利用可能にするための設定管理モジュール。
        -   **`date_formatter.py`**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成します。
        -   **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、リポジトリ情報に構造化データ (JSON-LD) を追加する際のテンプレートファイル。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語の情報を処理・分析するためのモジュール。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成するモジュール。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル (`generated-docs/project-overview.md`) からプロジェクト概要の3行説明を自動的に抽出するモジュール。
        -   **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するためのモジュール。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に加工・整形する主要なビジネスロジックを担うモジュール。
        -   **`seo_template.yml`**: リポジトリ一覧のSEOメタデータや構造化データに関する設定を定義するYAMLテンプレートファイル。
        -   **`statistics_calculator.py`**: 各リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するモジュール。
        -   **`strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイル。多言語対応（i18n）の基盤となります。
        -   **`template_processor.py`**: Markdown生成において、特定のテンプレート構文を処理し、動的なデータを埋め込むためのモジュール。
        -   **`url_utils.py`**: GitHub APIのエンドポイントURLの構築や、その他のURL関連の処理を行うユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得）をテストするためのユニットテストファイル。
-   **`tests/`**: プロジェクトのすべてのテストファイルを格納するディレクトリ。
    -   **`conftest.py`**: Pytestのフィクスチャやテストヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator.py` モジュールの結合テスト。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトの機能をテストするためのファイル。
    -   **`test_config.py`**: `config_manager.py` や各種設定ファイル (`config.yml` など) の読み込み・処理が正しく行われるかをテストするファイル。
    -   **`test_date_formatter.py`**: `date_formatter.py` モジュールの機能（日付フォーマット）をテストするファイル。
    -   **`test_environment.py`**: プロジェクトの実行環境が正しく設定されているか、必要な依存関係が利用可能かなどをチェックするテスト。
    -   **`test_integration.py`**: プロジェクト全体または主要なコンポーネント間の連携をテストする結合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator.py` モジュールの機能（Markdownコンテンツ生成）をテストするファイル。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の抽出）をテストするファイル。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py` モジュールの機能（READMEからのバッジ情報抽出）をテストするファイル。
    -   **`test_repository_processor.py`**: `repository_processor.py` モジュールの機能（リポジトリデータの処理）をテストするファイル。

## 関数詳細説明
このプロジェクトはPythonで書かれており、主にスクリプトとモジュールに分かれています。以下に主要なモジュールに含まれると考えられる主要な関数の役割を説明します。具体的な引数や戻り値はソースコードを参照する必要がありますが、ここではその機能に焦点を当てます。

-   **`generate_repo_list.py`**:
    -   `main()`: スクリプトのエントリポイント。コマンドライン引数をパースし、リポジトリ一覧生成の処理フローをオーケストレートします。
    -   `generate_repository_list(username, output_file, limit)`: 指定されたGitHubユーザーのリポジトリ情報を取得し、Markdown形式で一覧ファイルを生成するメインのロジックを担います。
-   **`repository_processor.py`**:
    -   `fetch_repositories(username, token, limit)`: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。認証のためにトークンを使用します。
    -   `process_repository_data(repo_data, config)`: GitHub APIから取得した個々のリポジトリデータを受け取り、表示に必要な情報を抽出・整形します。
-   **`project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_name, owner, target_file, section_title, config)`: 指定されたリポジトリ内の`target_file`から、`section_title`で指定されたセクションの3行概要を抽出して返します。
-   **`markdown_generator.py`**:
    -   `generate_markdown_output(repositories_info, config, strings)`: 処理されたリポジトリ情報と設定、文字列データを受け取り、最終的なMarkdown形式の文字列を生成します。
-   **`badge_generator.py`**:
    -   `generate_status_badges(repo_status)`: リポジトリのステータス（アーカイブ、フォークなど）に基づいて、対応するMarkdown形式のバッジ文字列を生成します。
-   **`config_manager.py`**:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
-   **`date_formatter.py`**:
    -   `format_date_for_display(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、ユーザーフレンドリーな形式（例: "YYYY年MM月DD日"）に整形して返します。
-   **`url_utils.py`**:
    -   `build_github_api_url(endpoint, username=None, repo_name=None)`: GitHub APIの特定のエンドポイントに対するURLを構築します。
-   **`check_large_files.py`** (`.github_automation/check_large_files/scripts/`):
    -   `check_files_for_size(path, max_size_bytes)`: 指定されたパス以下のファイルで、`max_size_bytes`を超えるファイルを検出し、リストとして返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-23 07:07:19 JST
