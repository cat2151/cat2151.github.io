Last updated: 2026-06-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動で取得・処理するシステムです。
- JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- これにより、検索エンジンやLLMによるリポジトリ参照性を向上させ、開発効率の課題解決を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースの静的サイトジェネレーターで、生成されたMarkdownファイルを表示), Markdown (コンテンツ生成形式), HTML (生成されるコンテンツ構造), CSS (Jekyllテーマによるスタイル)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), pytest (テストフレームワーク), ruff (Pythonコードのフォーマッター兼リンター), YAML (設定ファイルの記述), TOML (secrets設定、大規模ファイルチェック設定)
- テスト: pytest (Pythonコードの単体テストおよび結合テストを実行)
- ビルドツール: Pythonスクリプト (リポジトリ情報を取得・処理し、Markdownファイルを「ビルド」), Jekyll (GitHub Pages側でMarkdownファイルをHTMLに「ビルド」)
- 言語機能: Python 3.x (プロジェクトの主要な開発言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリが存在するため、潜在的にGitHub Actionsによる自動化が可能ですが、このプロジェクト自体はローカル実行重視とされています)
- 開発標準: ruff (Pythonコードの品質と一貫性を保つためのリンティングおよびフォーマット)

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

-   **`.editorconfig`**: 異なる開発環境（エディタ、IDE）間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルを一貫させるための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsに関連する自動化スクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/README.md`**: `check_large_files` サブプロジェクトの目的、使用方法、設定などを説明するドキュメント。
    -   **`check_large_files/check-large-files.toml`**: リポジトリ内の大規模ファイルを検出するための設定を記述したTOMLファイル。
    -   **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の指定された閾値を超える大きなファイルを検出し、報告するPythonスクリプト。
-   **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。一時ファイル、ビルド成果物、設定ファイルなどが含まれる。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイル。著作権と利用条件を明示する。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法、インストール手順、設定方法、貢献方法、ライセンスなどを説明するプロジェクトの顔となるドキュメント。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトタイトル、説明、テーマ、パーマリンク構造などのJekyll固有の設定を定義する。
-   **`assets/`**: GitHub Pagesサイトで利用される静的アセット（画像、ファビコン、CSS、JavaScriptなど）を格納するディレクトリ。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズ。
-   **`debug_project_overview.py`**: `project_overview_fetcher` モジュールのデバッグやテスト実行を補助するためのスクリプト。
-   **`generated-docs/`**: GitHub Pagesサイト用に生成されたドキュメントやコンテンツが配置される可能性のあるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどでサイトの所有権を確認するために配置されるHTMLファイル。
-   **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。このプロジェクトによってリポジトリ一覧が自動生成され、ここに書き込まれる。
-   **`issue-notes/22.md`**: 特定のIssue（問題やタスク）に関する詳細なメモや考察を記述したファイル。`22` はIssue番号を指す。
-   **`manifest.json`**: Progressive Web App (PWA) のメタデータファイル。アプリ名、アイコン、起動時の表示設定などを定義する。
-   **`pytest.ini`**: pytestテストフレームワークの設定ファイル。テストの発見ルール、実行オプション、プラグイン設定などを定義する。
-   **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonライブラリとそのバージョンをリストしたファイル。
-   **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonライブラリとそのバージョンをリストしたファイル。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしてはいけないかを指示するファイル。
-   **`ruff.toml`**: `ruff` というPythonの高速リンター/フォーマッターの設定ファイル。コードスタイル、ルール、無視するファイルなどを定義する。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   **`__init__.py`**: Pythonパッケージとして `src` ディレクトリを認識させるためのファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成ロジックを格納するPythonパッケージ。
        -   **`__init__.py`**: `generate_repo_list` パッケージを初期化。
        -   **`badge_generator.py`**: リポジトリのステータス（アクティブ、アーカイブ、フォークなど）に応じたバッジのMarkdownを生成するロジックを定義。
        -   **`config.yml`**: プロジェクトの動作設定（プロジェクト概要の取得方法、キャッシュ設定など）を定義するYAMLファイル。
        -   **`config_manager.py`**: `config.yml` や `strings.yml` など、プロジェクトの設定ファイルを読み込み、管理するユーティリティ。
        -   **`date_formatter.py`**: GitHub APIから取得した日付文字列を、表示に適した形式に変換するためのユーティリティ関数を提供。
        -   **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIからの情報取得、処理、Markdown生成の全体フローを orchestrate する。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、リポジトリ情報からJSON-LD形式の構造化データを生成するためのテンプレート。
        -   **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するロジック。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジック。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要（3行説明）を自動的に取得するロジック。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジック。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示や処理に必要な形式に整形・フィルタリングする主要なロジック。
        -   **`seo_template.yml`**: GitHub PagesサイトのSEOに関連するメタデータや記述を生成するためのテンプレート設定ファイル。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジック。
        -   **`strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するYAMLファイル。多言語対応の基盤にもなりうる。
        -   **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2などのテンプレートエンジンまたはシンプルな文字列置換）を処理する汎用ロジック。
        -   **`url_utils.py`**: GitHub APIのエンドポイントURLの構築や、リポジトリURLの生成など、URL関連のユーティリティ関数を提供。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能に関する単体テストを記述したファイル。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    -   **`conftest.py`**: pytestのテストフィクスチャ（テストのための準備や後処理を行う関数）やフックを定義するファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator` の機能が他のコンポーネントと正しく連携するかを検証する統合テスト。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files.py` スクリプトの機能に関するテスト。
    -   **`test_config.py`**: `config_manager` や関連する設定ファイルの読み込み、パースが正しく行われるかを検証するテスト。
    -   **`test_date_formatter.py`**: `date_formatter` の日付変換機能に関する単体テスト。
    -   **`test_environment.py`**: プロジェクトの実行環境（依存ライブラリのインストール状況など）に関するテスト。
    -   **`test_integration.py`**: プロジェクトの主要なコンポーネント（API取得、データ処理、Markdown生成）がエンドツーエンドで正しく動作するかを検証する包括的な統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator` が正しいMarkdownコンテンツを生成するかを検証するテスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher` が正しくプロジェクト概要をフェッチできるかを検証するテスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor` がREADMEからバッジ情報を正しく抽出できるかを検証するテスト。
    -   **`test_repository_processor.py`**: `repository_processor` がGitHub APIの生データを正しく処理・整形できるかを検証するテスト。

## 関数詳細説明

**`src/generate_repo_list/generate_repo_list.py`**
-   **`main()`**:
    -   **役割**: スクリプトのエントリポイント。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する一連の処理を調整します。
    -   **引数**: なし（`argparse` を使用してコマンドライン引数を内部で処理します）。
    -   **戻り値**: なし（ファイル出力を行います）。
-   **`fetch_repositories(username: str, token: str, limit: int = None) -> List[Dict]`**:
    -   **役割**: 指定されたGitHubユーザー名とアクセストークンを使用して、GitHub APIからリポジトリ情報を取得します。`limit` が指定された場合、取得するリポジトリ数を制限します。
    -   **引数**:
        -   `username` (str): GitHubのユーザー名。
        -   `token` (str): GitHub APIへの認証に使用するパーソナルアクセストークン。
        -   `limit` (int, optional): 取得するリポジトリの最大数。デバッグや開発時に使用されます。
    -   **戻り値**: 取得したリポジトリ情報のリスト（辞書形式）。

**`src/generate_repo_list/repository_processor.py`**
-   **`process_repository_data(raw_repository_list: List[Dict]) -> List[Dict]`**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータ（辞書のリスト）を、プロジェクトで利用しやすい形式に整形・フィルタリングします。必要な情報の抽出、欠損値の処理、基本的な分類などを行います。
    -   **引数**:
        -   `raw_repository_list` (List[Dict]): GitHub APIから直接取得したリポジトリデータのリスト。
    -   **戻り値**: 処理・整形されたリポジトリデータのリスト。

**`src/generate_repo_list/project_overview_fetcher.py`**
-   **`get_project_overview(repo_full_name: str, config: Dict) -> Optional[str]`**:
    -   **役割**: 指定されたリポジトリの `generated-docs/project-overview.md` ファイルから「プロジェクト概要」セクションの3行説明をフェッチします。設定に応じてキャッシュやリトライも行います。
    -   **引数**:
        -   `repo_full_name` (str): リポジトリのフルネーム（例: "cat2151/generate-repo-list"）。
        -   `config` (Dict): `config.yml` から読み込まれた設定情報。
    -   **戻り値**: 取得されたプロジェクト概要の文字列、または見つからなかった場合は `None`。

**`src/generate_repo_list/markdown_generator.py`**
-   **`generate_markdown(processed_repositories: List[Dict], templates: Dict, strings: Dict, config: Dict) -> str`**:
    -   **役割**: 処理済みのリポジトリデータと各種テンプレート、文字列リソースを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   **引数**:
        -   `processed_repositories` (List[Dict]): `repository_processor` によって整形されたリポジトリデータのリスト。
        -   `templates` (Dict): Markdown生成に使用するテンプレート（例: `seo_template.yml`, `json_ld_template.json`）。
        -   `strings` (Dict): `strings.yml` から読み込まれた表示用の文言。
        -   `config` (Dict): `config.yml` から読み込まれた設定情報。
    -   **戻り値**: 生成されたMarkdownコンテンツの文字列。

**`src/generate_repo_list/badge_generator.py`**
-   **`create_badge_markdown(status_type: str) -> str`**:
    -   **役割**: リポジトリのステータス（例: "active", "archived", "fork"）に応じて、対応するMarkdown形式のバッジ文字列を生成します。
    -   **引数**:
        -   `status_type` (str): リポジトリのステータスを示す文字列。
    -   **戻り値**: 生成されたバッジのMarkdown文字列。

**`src/generate_repo_list/config_manager.py`**
-   **`load_config(filepath: str) -> Dict`**:
    -   **役割**: 指定されたYAML設定ファイル（例: `config.yml`, `strings.yml`）を読み込み、Pythonの辞書形式で返します。
    -   **引数**:
        -   `filepath` (str): 読み込む設定ファイルのパス。
    -   **戻り値**: 設定内容を表す辞書。

**`src/generate_repo_list/date_formatter.py`**
-   **`format_date(iso_date_string: str) -> str`**:
    -   **役割**: ISO 8601形式の日付文字列（例: "2023-10-27T10:00:00Z"）を、人間が読みやすい形式（例: "2023年10月27日"）に変換します。
    -   **引数**:
        -   `iso_date_string` (str): フォーマットするISO形式の日付文字列。
    -   **戻り値**: フォーマットされた日付文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-23 07:37:11 JST
