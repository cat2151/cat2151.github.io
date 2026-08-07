Last updated: 2026-08-08

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- 検索エンジン最適化(SEO)を意識し、リポジトリ一覧や各リポジトリへのリンクを公開します。
- 各リポジトリの「プロジェクト概要」を自動取得・表示し、バッジや分類機能も提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub PagesでMarkdownコンテンツから静的サイトを生成)、**Markdown** (リポジトリ一覧のコンテンツ記述)、**HTML/CSS** (Jekyllによる最終出力)
- 音楽・オーディオ: 該当なし
- 開発ツール: **pytest** (Pythonコードのテストフレームワーク)、**ruff** (Pythonコードのリンター・フォーマッター)、**Git** (バージョン管理システム)
- テスト: **pytest** (ユニットテストおよび統合テストの実行)
- ビルドツール: **Python** (リポジトリ情報の取得・加工およびMarkdownファイルの生成スクリプト実行環境)
- 言語機能: **Python** (スクリプト開発に使用されるプログラミング言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から、特定タスクの自動化に使用される可能性を示唆。プロジェクトの主要機能自体が「自動生成」であり、GitHub Pagesへのデプロイも自動化の範疇)
- 開発標準: **ruff** (コードスタイルの一貫性維持)、**.editorconfig** (異なるエディタ間でのコードスタイル統一)

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
- **`.editorconfig`**: 異なる開発環境間でのコードスタイル（インデント、改行など）の統一を定義するファイル。
- **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイル。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリのパターンを定義するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方などを説明するメインのドキュメント。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体のビルド設定や変数定義を行うファイル。
- **`assets/`**: ウェブサイトで使用される画像、アイコン（favicon）などの静的アセットを格納するディレクトリ。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや単体テストを行うための補助スクリプト。
- **`generated-docs/`**: 各リポジトリから取得した「プロジェクト概要」ファイル（例: `project-overview.md`）が想定されるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでのサイト所有権確認に使用されるファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。生成されたリポジトリ一覧がここに書き込まれる。
- **`issue-notes/22.md`**: プロジェクトの特定の課題（Issue #22）に関する詳細なメモや調査結果を記録したファイル。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。ホーム画面アイコンや表示モードなどを定義。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイル。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンを記述したファイル。
- **`requirements.txt`**: プロジェクトの本番実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどのパスをクロール・インデックスすべきかを指示するファイル。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。コードの品質と一貫性を保つために使用。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成に関するメインのロジックをカプセル化したPythonパッケージ。
        - **`badge_generator.py`**: リポジトリの状態（アクティブ、アーカイブなど）に応じたバッジのMarkdownコードを生成する役割を担う。
        - **`config.yml`**: プロジェクト概要取得機能やGitHub APIに関する技術的パラメータを設定するYAMLファイル。
        - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのユーティリティ。
        - **`date_formatter.py`**: GitHub APIから取得した日付文字列を、ユーザーにとって読みやすい形式に整形するための関数を提供する。
        - **`generate_repo_list.py`**: プロジェクトのエントリーポイントとなるメインスクリプト。GitHub APIからの情報取得、処理、Markdown生成までの一連の流れを orchestrate する。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために構造化データを記述するJSON-LDのテンプレートファイル。
        - **`language_info.py`**: リポジトリの使用言語に関する情報を処理し、表示に役立つ形式に変換する。
        - **`markdown_generator.py`**: 最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックを実装。
        - **`project_overview_fetcher.py`**: 各リポジトリから特定のパスにある`project-overview.md`ファイルを読み込み、プロジェクト概要の3行説明を抽出する。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから既存のバッジ情報を抽出し、解析する。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、アプリケーションが扱いやすい形式に整形・フィルタリングする。
        - **`seo_template.yml`**: サイトのSEOメタデータや記述に関するテンプレート設定を管理するファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する。
        - **`strings.yml`**: アプリケーション内で表示される様々なメッセージや文言を国際化・一元管理するためのYAMLファイル。
        - **`template_processor.py`**: Markdown生成時などに使用するテンプレート（Jinja2など）の処理を抽象化する。
        - **`url_utils.py`**: URLの生成、解析、クリーンアップなど、URL操作に関するユーティリティ関数を提供する。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能に関する単体テストを記述したファイル。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **`conftest.py`**: pytestのテストフィクスチャ（テストデータや共通設定）を定義するファイル。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の統合テスト。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/`内のスクリプトのテスト。
    - **`test_config.py`**: 設定読み込み・管理(`config_manager.py`)機能に関するテスト。
    - **`test_date_formatter.py`**: 日付整形(`date_formatter.py`)機能に関するテスト。
    - **`test_environment.py`**: 実行環境に関する基本的なテスト。
    - **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator.py`の機能に関するテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`の機能に関するテスト。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`の機能に関するテスト。
    - **`test_repository_processor.py`**: `repository_processor.py`の機能に関するテスト。

## 関数詳細説明
提供された情報では個々の関数の詳細なシグネチャは不明ですが、ファイル名から推測される主要な関数とその役割を説明します。

-   **`generate_repo_list.py`内の主要関数 (例: `main()`)**
    -   **役割**: プログラムのエントリーポイント。GitHub APIからのリポジトリ情報取得、データの処理、Markdownコンテンツの生成、およびファイルへの出力という一連の処理フローを統括します。
    -   **引数**: コマンドライン引数（ユーザー名、出力ファイル名、制限数など）をパースして使用します。
    -   **戻り値**: 処理の成功/失敗を示すステータスコードなど。
-   **`repository_processor.py`内の主要関数 (例: `process_repositories(username, token)`)**
    -   **役割**: 指定されたGitHubユーザーのリポジトリ情報をGitHub API経由で取得し、アプリケーションが扱いやすい形式に整形・フィルタリングします。
    -   **引数**: `username` (GitHubユーザー名)、`token` (GitHubアクセストークン) など。
    -   **戻り値**: 処理済みのリポジトリデータのリスト。
-   **`project_overview_fetcher.py`内の主要関数 (例: `fetch_project_overview(repo_url, config)`)**
    -   **役割**: 指定されたリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出し取得します。
    -   **引数**: `repo_url` (リポジトリのURL)、`config` (設定情報)。
    -   **戻り値**: 抽出された3行のプロジェクト概要、または空のリスト。
-   **`markdown_generator.py`内の主要関数 (例: `generate_markdown(repos_data, config, strings)`)**
    -   **役割**: 処理されたリポジトリデータ、設定情報、表示用の文字列テンプレートなどを用いて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   **引数**: `repos_data` (処理済みリポジトリデータのリスト)、`config` (設定情報)、`strings` (表示用文字列)。
    -   **戻り値**: 生成されたMarkdown形式の文字列。
-   **`config_manager.py`内の主要関数 (例: `load_config(path)`)**
    -   **役割**: YAML形式の設定ファイル（`config.yml`や`strings.yml`）を読み込み、Pythonの辞書オブジェクトとして提供します。
    -   **引数**: `path` (設定ファイルのパス)。
    -   **戻り値**: 読み込まれた設定データ。
-   **`badge_generator.py`内の主要関数 (例: `generate_badge(status)`)**
    -   **役割**: リポジトリのステータス（例: "active", "archived", "forked"）に基づいて、対応するMarkdown形式のバッジ文字列を生成します。
    -   **引数**: `status` (リポジトリのステータス)。
    -   **戻り値**: バッジのMarkdown文字列。
-   **`date_formatter.py`内の主要関数 (例: `format_date(iso_date_string)`)**
    -   **役割**: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形して返します。
    -   **引数**: `iso_date_string` (ISO形式の日付文字列)。
    -   **戻り値**: 整形された日付文字列。

## 関数呼び出し階層ツリー
```
main (src/generate_repo_list/generate_repo_list.py)
  ├── load_config (src/generate_repo_list/config_manager.py)
  ├── load_strings (src/generate_repo_list/config_manager.py)
  ├── process_repositories (src/generate_repo_list/repository_processor.py)
  │     ├── fetch_project_overview (src/generate_repo_list/project_overview_fetcher.py)
  │     │     └── (外部HTTPリクエストなど)
  │     └── generate_badge (src/generate_repo_list/badge_generator.py)
  │     └── format_date (src/generate_repo_list/date_formatter.py)
  │     └── calculate_statistics (src/generate_repo_list/statistics_calculator.py)
  │     └── extract_readme_badges (src/generate_repo_list/readme_badge_extractor.py)
  │     └── get_language_info (src/generate_repo_list/language_info.py)
  ├── generate_markdown (src/generate_repo_list/markdown_generator.py)
  │     └── process_template (src/generate_repo_list/template_processor.py)
  │     └── build_repo_url (src/generate_repo_list/url_utils.py)
  └── (ファイル書き込み処理)
```
*補足：提供情報から具体的な関数呼び出し階層を自動生成することはできませんでしたが、プロジェクトの目的と各ファイルの役割から一般的な処理フローと呼び出し関係を推測して図示しました。`main`関数が全体を制御し、他のモジュールの主要関数を呼び出す構造です。*

---
Generated at: 2026-08-08 07:13:39 JST
