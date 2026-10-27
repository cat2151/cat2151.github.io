Last updated: 2026-10-28

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成します。
- 検索エンジンやLLMからの参照性を向上させ、リポジトリ情報を効率的に公開します。
- 各リポジトリの概要、技術バッジ、分類などを自動でマークダウンに出力します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として静的サイトを生成)、**Markdown** (生成されるリポジトリ一覧のフォーマット)、**HTML/CSS/JavaScript** (Jekyllテーマによるページ表示)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なスクリプト言語)、**Git** (バージョン管理)、**GitHub API** (リポジトリ情報取得)、**VS Code** (推奨開発環境、`.editorconfig`で設定連携)、**pytest** (テストフレームワーク)、**ruff** (コードリンター・フォーマッター)
- テスト: **Pytest** (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: **Python** (スクリプト実行によるMarkdown生成)、**Jekyll** (GitHub Pagesでのサイトビルド)
- 言語機能: **Python** (スクリプト全体の記述言語)、**YAML** (設定ファイル`config.yml`, `strings.yml`などで使用)、**TOML** (秘密情報`secrets.toml`や設定ファイル`ruff.toml`などで使用)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリに自動化スクリプトを格納、大型ファイルチェックなどに使用)、**Pythonスクリプト** (リポジトリ一覧生成の自動化本体)
- 開発標準: **Ruff** (Pythonコードのスタイルチェックと自動修正)、**.editorconfig** (IDEやエディタ間でのコーディングスタイル統一)

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
-   **`.github_automation/`**: GitHub Actionsなどを用いた自動化スクリプトや設定ファイルを格納するディレクトリ。
    -   **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    -   **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義するTOML形式の設定ファイル。
    -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、警告するためのPythonスクリプト。
-   **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）が記述されたファイル。
-   **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方、開発者向けのヒントなどが記されたプロジェクトの主要な説明書。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグイン、ビルドオプションなどを定義する。
-   **`assets/`**: Jekyllサイトで使用される画像、アイコン、CSS、JavaScriptファイルなどの静的アセットを格納するディレクトリ。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズ。
-   **`debug_project_overview.py`**: リポジトリ概要取得機能のデバッグや単体テストを行うための補助スクリプト。
-   **`generated-docs/`**: 生成されたドキュメントや一時ファイルを格納するためのディレクトリ。
-   **`googled947dc864c270e07.html`**: Googleサイト認証用のHTMLファイル。ウェブマスターツールのサイト所有権確認に使用される。
-   **`index.md`**: GitHub Pagesサイトのトップページとして表示されるメインのMarkdownファイル。`generate_repo_list.py`スクリプトによってリポジトリ一覧がここに生成される。
-   **`issue-notes/22.md`**: 開発中の課題やメモ、特定のイシューに関する詳細を記録するためのドキュメント。
-   **`manifest.json`**: ウェブアプリケーションマニフェストファイル。プログレッシブウェブアプリ（PWA）の構成情報（アプリ名、アイコン、表示設定など）を定義する。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの実行方法や検出ルールなどをカスタマイズする。
-   **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンをリストアップしたファイル。
-   **`requirements.txt`**: プロジェクトの本番環境で実行するために最低限必要なPythonパッケージとそのバージョンをリストアップしたファイル。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしてはいけないかを指示するファイル。
-   **`ruff.toml`**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイル。コードスタイルルールや無視するファイルなどを定義する。
-   **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空のファイル。
-   **`src/generate_repo_list/`**: リポジトリ一覧自動生成システムの主要なPythonモジュール群を格納するパッケージ。
    -   **`__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空のファイル。
    -   **`badge_generator.py`**: リポジトリの技術スタックなどを示すバッジ画像を生成またはリンクを処理するロジックを含む。
    -   **`config.yml`**: プロジェクト概要取得機能やAPIタイムアウトなど、システム固有の技術的パラメータを設定するYAMLファイル。
    -   **`config_manager.py`**: YAMLやTOML形式の設定ファイルを読み込み、プロジェクト全体で設定を管理する機能を提供する。
    -   **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形するユーティリティ関数を提供する。
    -   **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力する。
    -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式のメタデータテンプレート。
    -   **`language_info.py`**: GitHubリポジトリから取得した言語情報を解析し、表示に適した形に処理する機能を提供する。
    -   **`markdown_generator.py`**: 取得および整形されたリポジトリ情報から、Jekyllに対応したMarkdownコンテンツを生成する。
    -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動的に抽出し、整形する。
    -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから技術バッジの情報を抽出するロジックを含む。
    -   **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報（概要、バッジ、分類など）を抽出・整形する。
    -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化データを定義するテンプレートファイル。
    -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算する機能を提供する。
    -   **`strings.yml`**: ユーザーインターフェースに表示される各種メッセージや文言を一元的に管理するためのYAMLファイル。
    -   **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2などのテンプレートエンジン）の処理を担う。
    -   **`url_utils.py`**: URLの生成、解析、検証などの汎用的なURL関連ユーティリティ関数を提供する。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプト。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`conftest.py`**: pytestのテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義するファイル。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    -   **`test_config.py`**: 設定ファイルの読み込みや解析に関するテスト。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテスト。
    -   **`test_environment.py`**: 実行環境（依存関係、OSなど）に関するテスト。
    -   **`test_integration.py`**: システム全体の主要なフロー（APIアクセスからMarkdown生成まで）の統合テスト。
    -   **`test_markdown_generator.py`**: Markdown生成ロジックのテスト。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテスト。
    -   **`test_repository_processor.py`**: リポジトリデータ処理ロジックのテスト。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャや詳細な説明は得られませんが、ファイル名から推測される主要な関数とその役割を説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **`main()`**: プロジェクトの主要なエントリーポイント。GitHub APIからリポジトリ情報を取得し、整形し、Markdownファイルとして出力する一連の処理を統括します。引数としてGitHubユーザー名、出力ファイルパス、リポジトリ処理制限数などを受け取ります。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **`fetch_project_overview(repo_url, config)`**: 指定されたリポジトリのURLと設定情報に基づいて、リモートの`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出し、返却します。ネットワークアクセスやファイル解析を行います。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **`generate_markdown(repo_data_list, template_path)`**: 処理済みのリポジトリデータリストとMarkdownテンプレートのパスを受け取り、Jekyll形式のリポジトリ一覧Markdownコンテンツを生成します。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   **`process_repository(repo_info, config)`**: GitHub APIから取得した個々のリポジトリ情報を受け取り、プロジェクト概要の取得、バッジ情報の抽出、言語情報の解析などを行い、表示に適した形にデータを整形して返します。
-   **`src/.github_automation/check_large_files/scripts/check_large_files.py`**:
    -   **`main()`**: リポジトリ内のファイルを走査し、設定ファイルで定義された閾値を超える大容量ファイルを検出してレポートします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-10-28 07:08:46 JST
