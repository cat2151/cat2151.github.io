Last updated: 2026-09-12

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧ページを自動生成するシステムです。
- 検索エンジンでのクロール促進と、LLMによるリポジトリ参照精度の向上を目的としています。
- 各リポジトリの概要、バッジ、分類を含むSEO最適化されたMarkdownコンテンツを出力します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyllベース)** - 静的サイトホスティングサービスと、その基盤となる静的サイトジェネレータ。生成されたMarkdownをWebサイトとして表示するために使用されます。**Markdown** - 出力されるコンテンツ形式。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** - メインのスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成を行います。**GitHub API** - GitHubからリポジトリ情報をプログラム的に取得するために使用されます。**Pytest** - Pythonアプリケーションのテストフレームワーク。
- テスト: **Pytest** - テストコードの記述と実行に利用されます。`conftest.py`や`tests/`ディレクトリ内の各`test_*.py`ファイルでテストが管理されています。
- ビルドツール: **Pythonスクリプト** - `src/generate_repo_list/generate_repo_list.py` を中心としたPythonスクリプト群が、リポジトリ情報を加工し、最終的なMarkdownファイルを生成する役割を担います。
- 言語機能: **Python** - プロジェクトの大部分はPythonで実装されており、GitHub APIとの連携やファイル操作、文字列処理などに利用されます。**YAML/TOML** - 設定ファイル（`config.yml`, `strings.yml`, `ruff.toml`, `pytest.ini` など）の記述に使用されます。
- 自動化・CI/CD: **Pythonスクリプトによる自動化** - `generate_repo_list.py` がリポジトリ一覧生成の自動化を実行します。`.github_automation/` ディレクトリは将来的なGitHub Actionsやその他の自動化スクリプトの格納を想定しています。
- 開発標準: **Ruff** - Pythonコードのリンティングとフォーマットを自動化し、コードスタイルの一貫性を保つためのツール。`ruff.toml`で設定されます。**.editorconfig** - 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するためのディレクトリです。
    -   **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトの目的と使用方法を説明するドキュメントです。
    -   **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック用スクリプト`check_large_files.py`の設定ファイルです。チェック対象や閾値などを定義します。
    -   **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、警告するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。一時ファイルやログ、ビルド成果物などが含まれます。
-   **`LICENSE`**: プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
-   **`README.md`**: プロジェクトの主要なドキュメントです。プロジェクトの概要、背景、機能、セットアップ方法、実行コマンド、設定、開発者向けのヒントなどが記載されています。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などのJekyllに関連する設定を定義します。
-   **`assets/`**: Jekyllサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    -   **`assets/favicon-16x16.png`**, **`assets/favicon-192x192.png`**, **`assets/favicon-32x32.png`**, **`assets/favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   **`debug_project_overview.py`**: `project_overview`機能（他のリポジトリから概要を自動取得する機能）を単独でデバッグ・テストするためのスクリプトです。
-   **`generated-docs/`**: 他のリポジトリから取得された`project-overview.md`ファイルのような、自動生成されたドキュメントや一時ファイルを格納する、または参照されるパスの例を示唆するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールで、サイトの所有権を確認するためにGoogleから提供される検証用HTMLファイルです。
-   **`index.md`**: このプロジェクトのスクリプトによって生成される主要なMarkdownファイルです。GitHub Pagesサイトのトップページとして、リポジトリの一覧が表示されます。
-   **`issue-notes/`**: 開発中の課題、検討事項、または特定のイシューに関するメモを格納するためのディレクトリです。
    -   **`issue-notes/22.md`**: 特定のイシュー番号（例: 22）に関連するメモや詳細が記述されたファイルです。
-   **`manifest.json`**: ウェブアプリケーションマニフェストファイルです。プログレッシブウェブアプリ（PWA）として動作させるためのアプリ名、アイコン、表示モードなどの設定を定義します。
-   **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルです。テストファイルの検出パターン、テスト実行オプション、カバレッジ設定などを定義します。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。`pytest`や`ruff`などが含まれます。
-   **`requirements.txt`**: プロジェクトを本番環境で実行する際に必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。GitHub APIクライアントなどが含まれます。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内でクロールを許可するページと禁止するページを指示するためのファイルです。
-   **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツール`Ruff`の設定ファイルです。コードスタイルルール、無視するファイル、エラーコードなどを定義します。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **`src/__init__.py`**: Pythonパッケージであることを示す空のファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージであることを示す空のファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語、ライセンスなどの情報を元に、Markdown形式のバッジを生成するロジックを管理します。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイル、タイムアウト時間など）を定義するYAMLファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、ユーザーが読みやすい形式に整形するためのユーティリティ関数を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインエントリスクリプトです。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力までの一連のワークフローをオーケストレーションします。
        -   **`src/generate_repo_list/json_ld_template.json`**: JSON-LD形式の構造化データテンプレートです。SEOのためにリポジトリ情報を検索エンジンに理解しやすい形式で記述する際に利用されます。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するモジュールです。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを実装しています。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、ビルドステータスやカバレッジなどの特定のバッジ情報を抽出するロジックを管理します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを詳細に処理し、表示に必要な情報（概要、バッジ、分類など）に整形する役割を担います。
        -   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するモジュールです。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成において、テンプレートエンジン（例: Jinja2）を用いて動的にコンテンツを生成・レンダリングする機能を提供します。
        -   **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URL操作に関するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを確認するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`tests/conftest.py`**: `pytest`のテストフィクスチャや共通のヘルパー関数を定義するファイルで、複数のテストファイルで再利用可能なリソースを提供します。
    -   **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールが他のコンポーネントと正しく連携するかを検証する統合テストです。
    -   **`tests/test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトのテストです。
    -   **`tests/test_config.py`**: `config_manager`モジュールによる設定ファイルの読み込みと解析が正しく行われるかをテストします。
    -   **`tests/test_date_formatter.py`**: `date_formatter`モジュールの日付整形機能が正しく動作するかをテストします。
    -   **`tests/test_environment.py`**: プロジェクトの実行環境や依存関係が正しく設定されているかを確認するテストです。
    -   **`tests/test_integration.py`**: システム全体の主要な機能がエンドツーエンドで正しく動作するかを確認する統合テストです。
    -   **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールが期待通りにMarkdownコンテンツを生成するかをテストします。
    -   **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールがリモートの`project-overview.md`ファイルを正しく取得・解析できるかをテストします。
    -   **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正しく抽出できるかをテストします。
    -   **`tests/test_repository_processor.py`**: `repository_processor`モジュールがGitHub APIからの生のリポジトリデータを適切に処理・整形できるかをテストします。

## 関数詳細説明
このプロジェクトでは、Pythonモジュールが特定の役割を担っており、各モジュール内にその役割を実行するための主要な関数群が含まれています。以下に主要なモジュールと、その中で中心的な役割を果たすと推測される関数について説明します。具体的な引数や戻り値は提供されていませんが、一般的なPythonプロジェクトの慣習に基づき記述します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main(username: str, output_file: str, limit: Optional[int] = None)`: スクリプトのエントリポイントです。GitHub APIから指定されたユーザーのリポジトリ情報を取得し、各リポジトリを処理し、最終的にMarkdown形式のリポジトリ一覧を指定されたファイルに出力する一連の処理を調整します。
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badges(repo_data: Dict) -> str`: リポジトリの言語、ライセンス、その他のメタデータを含む辞書を受け取り、対応するMarkdown形式のバッジ文字列を生成して返します。
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config() -> ConfigObject`: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、設定値を構造化されたオブジェクトとして提供します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(iso_date_string: str) -> str`: ISO 8601形式の日付文字列を受け取り、指定された人間が読みやすい形式（例: "YYYY年MM月DD日"）に整形して返します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown(repositories_data: List[Dict], config: ConfigObject) -> str`: 処理済みのリポジトリデータ（各リポジトリの詳細情報を含む辞書のリスト）と設定オブジェクトを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成して返します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url: str, config: ConfigObject) -> Optional[str]`: 指定されたリポジトリURLから`config`で指定されたファイル（例: `generated-docs/project-overview.md`）を取得し、「プロジェクト概要」セクションから3行の説明を抽出し、文字列として返します。取得に失敗した場合はNoneを返します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   `process_repository(repo_json: Dict, config: ConfigObject) -> Dict`: GitHub APIから取得した単一のリポジトリの生データ（JSON形式の辞書）を受け取り、表示に必要な情報（整形された説明、バッジ情報、分類、概要など）を抽出し、加工された辞書として返します。
-   **`src/generate_repo_list/statistics_calculator.py`**
    -   `calculate_repo_statistics(repo_data: Dict) -> Dict`: リポジトリデータを受け取り、スター数、フォーク数、最終更新日などの統計情報を計算し、辞書形式で返します。
-   **`src/generate_repo_list/template_processor.py`**
    -   `render_template(template_name: str, context: Dict) -> str`: 指定されたテンプレートファイル名と、テンプレート内で使用するコンテキストデータ（辞書）を受け取り、テンプレートをレンダリングして最終的な文字列コンテンツ（Markdownなど）を返します。
-   **`src/generate_repo_list/url_utils.py`**
    -   `construct_github_api_url(username: str) -> str`: GitHubユーザー名を受け取り、そのユーザーのリポジトリ一覧を取得するためのGitHub APIエンドポイントのURLを構築して返します。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**
    -   `check_files(config: Dict)`: 設定ファイル（`check-large-files.toml`）に基づいて、リポジトリ内のファイルを走査し、設定された閾値を超える大容量ファイルを検出して報告します。
-   **`googled947dc864c270e07.html`**: このファイルは静的なHTMLであり、関数は含まれていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層ツリーは提供された情報からは分析できませんでした。
```

---
Generated at: 2026-09-12 07:12:59 JST
