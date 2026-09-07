Last updated: 2026-09-08

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けのリポジトリ一覧Markdownを自動生成します。
- 検索エンジン最適化されたコンテンツで、リポジトリの可視性を向上させます。
- 各リポジトリの概要、バッジ、分類情報を自動で統合表示します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages) - GitHub Pagesサイトの構築に利用され、生成されたMarkdownファイルを静的サイトとして公開します。
- 音楽・オーディオ: (該当する技術は見当たりません)
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語として、GitHub APIからのデータ取得、処理、Markdown生成スクリプトに利用されています。
    - **pytest**: Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです。
    - **ruff**: Pythonコードのスタイルチェックと自動修正を行う高速なリンター兼フォーマッターです。
- テスト: **pytest** - プロジェクトの各モジュールや統合的な動作を検証するためのテストフレームワークとして利用されています。
- ビルドツール: (専用のビルドツールは使用されていません) - Pythonスクリプト自体がリポジトリ情報からMarkdownファイルを生成する役割を担います。
- 言語機能: **Python** - データ処理、API連携、ファイル操作など、スクリプトの全般的なロジックを記述するために使用されています。
- 自動化・CI/CD: (CI/CDはローカル開発重視のため主要な構成ではありません) - `.github_automation`ディレクトリが存在しますが、プロジェクトの自動化フローとして明示的なCI/CDは含まれません。
- 開発標準: **ruff** - コードの品質を維持し、一貫したコーディングスタイルを強制するために使用されます。

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するためのディレクトリ。
    -   **`check_large_files/`**: 大容量ファイルをチェックするためのスクリプト群。
        -   **`README.md`**: `check_large_files`機能に関する説明ドキュメント。
        -   **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義するファイル。
        -   **`scripts/check_large_files.py`**: 実際に大容量ファイルを検出するPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの目的、セットアップ方法、使い方、機能などを説明する主要なドキュメント。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバル設定ファイル。
-   **`assets/`**: ウェブサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブに表示されるアイコン）画像ファイル。
-   **`debug_project_overview.py`**: `project_overview`機能のデバッグ目的で使用されるスクリプト。
-   **`generated-docs/`**: 生成されたドキュメント（このプロジェクトでは各リポジトリの概要説明など）を格納するディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
-   **`index.md`**: このプロジェクトによってGitHubリポジトリ一覧が自動生成され、出力されるメインのMarkdownファイル。JekyllによってHTMLに変換され、サイトのトップページとなる。
-   **`issue-notes/`**: 開発中のメモや特定の問題に関する記録を格納するディレクトリ。
    -   **`22.md`**: 特定のissueに関するメモを記述したMarkdownファイル。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。Webアプリの表示設定などを定義する。
-   **`pytest.ini`**: `pytest`テストフレームワークの挙動を設定するファイル。
-   **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonパッケージの一覧。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージの一覧。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールし、どのページを無視するかを指示するファイル。
-   **`ruff.toml`**: `ruff`コードリンター/フォーマッターのルールや設定を定義するファイル。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   **`__init__.py`**: Pythonパッケージとして`src`ディレクトリを認識させるための空ファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成機能の主要なモジュール群。
        -   **`__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるための空ファイル。
        -   **`badge_generator.py`**: リポジトリの各種情報（言語、ライセンスなど）からバッジを生成するロジックを扱うモジュール。
        -   **`config.yml`**: `project_overview`機能などの技術的パラメータや設定を定義するYAMLファイル。
        -   **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュール。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティモジュール。
        -   **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからのリポジトリ情報取得、処理、最終的なMarkdown生成までの一連の流れを統括する。
        -   **`json_ld_template.json`**: SEOを強化するためにWebページに埋め込むJSON-LD形式の構造化データテンプレート。
        -   **`language_info.py`**: リポジトリの使用言語情報を取得・解析し、表示に適した形に整形するモジュール。
        -   **`markdown_generator.py`**: 最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを含むモジュール。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するモジュール。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出するモジュール。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整形するモジュール。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化データのテンプレートを定義するYAMLファイル。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・処理するモジュール。
        -   **`strings.yml`**: 表示メッセージ、ラベル、その他の静的なテキスト文字列を一元的に管理するためのYAMLファイル。
        -   **`template_processor.py`**: Markdown生成に使用されるテンプレート（例: Jinja2など）を処理し、データと結合するモジュール。
        -   **`url_utils.py`**: URLの構築、解析、検証など、URL関連の共通ユーティリティ関数を提供するモジュール。
-   **`test_project_overview.py`**: `project_overview`機能の単体テストを記述したファイル。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    -   **`conftest.py`**: `pytest`のテスト設定やフィクスチャを定義するファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    -   **`test_config.py`**: `config_manager`モジュールのテスト。
    -   **`test_date_formatter.py`**: `date_formatter`モジュールのテスト。
    -   **`test_environment.py`**: 実行環境に関するテスト。
    -   **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator`モジュールのテスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのテスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのテスト。
    -   **`test_repository_processor.py`**: `repository_processor`モジュールのテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、各モジュールが特定の役割を持つ関数を提供しています。具体的な関数名は情報にないため、主要なモジュールが提供するであろう一般的な役割について説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**: メインスクリプト
    -   `main()`: スクリプトのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連の流れを orchestrate します。
    -   `_get_repositories(username, limit)`: 指定されたGitHubユーザーのリポジトリをGitHub APIから取得します。`limit`引数がある場合は取得数を制限します。
    -   `_generate_output(repos_data, output_file)`: 処理されたリポジトリデータに基づいて最終的なMarkdownコンテンツを生成し、指定された出力ファイルに書き込みます。
-   **`src/generate_repo_list/repository_processor.py`**: リポジトリデータ処理
    -   `process_repository_data(raw_repo_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出し、整形して、Markdown生成に適した形式に変換します。
-   **`src/generate_repo_list/markdown_generator.py`**: Markdown生成
    -   `generate_full_list_markdown(processed_repos)`: 処理済みの全リポジトリデータを受け取り、完全なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   `_generate_repository_section(repo_info)`: 個々のリポジトリ情報に基づいて、そのリポジトリのMarkdownセクション（タイトル、説明、バッジなど）を生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: プロジェクト概要取得
    -   `fetch_project_overview(repo_url, target_file, section_title)`: 特定のリポジトリ（`repo_url`）内の指定されたファイル（`target_file`）から、特定のセクション（`section_title`）の3行概要を抽出して取得します。
-   **`src/generate_repo_list/config_manager.py`**: 設定管理
    -   `load_config(config_path)`: 指定されたパスにあるYAML設定ファイルを読み込み、設定値をPythonオブジェクトとして返します。
-   **`src/generate_repo_list/date_formatter.py`**: 日付整形
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形して返します。
-   **`src/generate_repo_list/url_utils.py`**: URLユーティリティ
    -   `build_github_api_url(endpoint, username)`: GitHub APIのエンドポイントとユーザー名から完全なAPIリクエストURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-08 07:19:52 JST
