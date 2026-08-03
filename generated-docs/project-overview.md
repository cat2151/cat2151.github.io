Last updated: 2026-08-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得・分析するシステムです。
- 取得した情報から、SEO最適化されたMarkdown形式のリポジトリ一覧ページをGitHub Pages向けに生成します。
- これにより、リポジトリの検索エンジンへの露出を高め、LLMによる参照失敗などの課題を緩和します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesのベースとなる静的サイトジェネレーターで、生成されたMarkdownファイルをレンダリングします), **Markdown** (リポジトリ一覧ページの記述形式), **GitHub Pages** (静的サイトのホスティングサービス)
- 音楽・オーディオ: 特になし
- 開発ツール: **Python** (メインのスクリプト言語), **GitHub API** (リポジトリ情報の取得に使用), **YAML** (プロジェクト設定ファイル `config.yml`, `strings.yml`, `seo_template.yml` などに利用), **TOML** (pytest設定 `pytest.ini`, コードスタイル設定 `ruff.toml`, シークレット管理 `secrets.toml` などに利用), **JSON** (SEO用のJSON-LDテンプレート `json_ld_template.json`)
- テスト: **pytest** (Pythonコードの単体テストおよび結合テストフレームワーク)
- ビルドツール: プロジェクトのPythonスクリプト自体が、GitHub APIから取得したデータを基にMarkdownファイルを生成するため、**Pythonスクリプト**がビルドツールとしての役割を果たします。
- 言語機能: **Python** (オブジェクト指向プログラミング、モジュールによる機能分割、非同期処理など、柔軟なスクリプト記述とデータ処理能力)
- 自動化・CI/CD: **Pythonスクリプト** (リポジトリ情報の取得とMarkdown生成の自動化), **GitHub Actions** (`.github_automation`ディレクトリに関連ファイルがあり、自動化処理に利用される可能性があります)
- 開発標準: **ruff** (PythonコードのLinterおよびFormatterで、コード品質の維持とスタイルの統一を自動化)

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
-   **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/`**: 大容量ファイルをチェックする自動化スクリプト群。
        -   **`README.md`**: `check_large_files`機能に関する説明。
        -   **`check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイル。
        -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などを説明するメインドキュメント。
-   **`_config.yml`**: Jekyllサイト全体の構成設定ファイル。GitHub Pagesの振る舞いを制御します。
-   **`assets/`**: ウェブサイトで使用される画像（ファビコンなど）やその他の静的アセットを格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのファビコン画像ファイル。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテスト実行に用いられる可能性のあるスクリプト。
-   **`generated-docs/`**: 自動生成されたドキュメントを一時的、あるいは最終的に格納するディレクトリ、または`project-overview.md`のような参照元ファイルを置く場所。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどの所有権確認に使用されるHTMLファイル。関数やインポートは含まれません。
-   **`index.md`**: `generate_repo_list.py`によってリポジトリ一覧が生成され、GitHub Pagesのトップページとして表示されるMarkdownファイル。
-   **`issue-notes/`**: プロジェクトの課題やメモを記録するためのディレクトリ。
    -   **`22.md`**: 特定の課題に関する詳細なメモや議論が記述されたMarkdownファイル。
-   **`manifest.json`**: ウェブアプリケーションマニフェストファイル。PWA（Progressive Web App）機能を提供するために、アプリのメタデータ（アイコン、表示モードなど）を定義します。
-   **`pytest.ini`**: pytestテストフレームワークのグローバル設定ファイル。
-   **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンをリストするファイル。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストするファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
-   **`ruff.toml`**: PythonコードのLinter/Formatterであるruffの設定ファイル。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   **`__init__.py`**: Pythonパッケージの初期化ファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むPythonパッケージ。
        -   **`__init__.py`**: `generate_repo_list`パッケージの初期化ファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ画像を生成または管理するスクリプト。
        -   **`config.yml`**: プロジェクト概要取得機能など、`generate_repo_list`モジュール固有の設定を定義するファイル。
        -   **`config_manager.py`**: 設定ファイル（YAML, TOMLなど）を読み込み、アプリケーション全体で利用可能な形で管理するモジュール。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するモジュール。
        -   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
        -   **`json_ld_template.json`**: SEO対策のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイル。
        -   **`language_info.py`**: GitHubリポジトリから取得した言語情報を処理し、表示に適した形に整形するモジュール。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装したモジュール。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するモジュール。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、プロジェクトの状態や特徴を示すバッジ情報を抽出するモジュール。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、生成システムで扱いやすい形式に加工・処理するモジュール。
        -   **`seo_template.yml`**: SEO関連のメタデータやキーワードなどのテンプレート設定を定義するファイル。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュール。
        -   **`strings.yml`**: UIに表示される各種メッセージや固定文言を一元管理するための設定ファイル。
        -   **`template_processor.py`**: Markdown生成などで利用される汎用的なテンプレート処理ロジックを提供するモジュール。
        -   **`url_utils.py`**: URLの生成、解析、バリデーションなど、URLに関連するユーティリティ関数を提供するモジュール。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールに対するテストスクリプト。
-   **`tests/`**: プロジェクト全体のテストコードが格納されるディレクトリ。
    -   **`conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator.py`モジュールの統合テスト。
    -   **`test_check_large_files.py`**: `check_large_files.py`スクリプトのテスト。
    -   **`test_config.py`**: 設定ファイルや設定管理モジュールに関するテスト。
    -   **`test_date_formatter.py`**: `date_formatter.py`モジュールのテスト。
    -   **`test_environment.py`**: 開発・実行環境の設定や依存関係に関するテスト。
    -   **`test_integration.py`**: システム全体の主要なフローに関する統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator.py`モジュールのテスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールのテスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールのテスト。
    -   **`test_repository_processor.py`**: `repository_processor.py`モジュールのテスト。

## 関数詳細説明
プロジェクト情報からは、個別の関数の詳細（引数、戻り値、具体的な内部ロジックなど）は提供されていません。そのため、具体的な関数の説明は省略します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-08-04 07:24:26 JST
