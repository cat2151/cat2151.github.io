Last updated: 2026-04-20

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成し、検索エンジン最適化（SEO）を強化します。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のマークダウン形式で出力します。
- 各リポジトリの概要表示、バッジ、分類機能を提供し、サイトの可視性と情報伝達力を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesベースの静的サイトジェネレータで、生成されたMarkdownファイルを表示するために使用されます。), Markdown (GitHub Pagesサイトに表示されるリポジトリ一覧ページのコンテンツ形式です。)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用されていません。
- 開発ツール: Git (バージョン管理システム), GitHub (リポジトリホスティングおよびAPI利用), Ruff (Pythonコードのフォーマッター兼リンター)
- テスト: Pytest (Python製のテストフレームワークで、プロジェクトの単体・結合テストに使用されます。)
- ビルドツール: Python (メインのスクリプト言語であり、リポジトリ情報の取得・処理・Markdown生成を実行する環境です。)
- 言語機能: Python (プロジェクトの主要な開発言語であり、GitHub APIとの連携、データ処理、ファイル生成など全てのロジックを実装しています。)
- 自動化・CI/CD: GitHub API (GitHubリポジトリから情報をプログラムで取得するために使用されます。)
- 開発標準: Ruff (Pythonコードの品質を統一し、可読性と保守性を高めるための静的解析ツールです。)

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどのコードフォーマットを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するためのディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトに関する説明が記述されたMarkdownファイルです。
    - **`.github_automation/check_large_files/check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイルで、大きなファイルの検出ルールなどを定義します。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: GitHubリポジトリ内の大きなファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド生成物、ログ、一時ファイルなど）を指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記載されたファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定、ライセンスなど、ユーザーがプロジェクトを理解し始めるための主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定を定義するファイルです。サイトタイトル、テーマ、プラグインなどが含まれます。
- **`assets/`**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`assets/favicon-16x16.png`**, **`assets/favicon-192x192.png`**, **`assets/favicon-32x32.png`**, **`assets/favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグやテストに使用される可能性のあるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが格納されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: メインスクリプトによって生成される、リポジトリ一覧を含むGitHub PagesのトップページとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中の課題やメモなどを格納するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細情報が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルで、アプリの表示方法、アイコン、スタートURLなどをブラウザに伝えます。
- **`pytest.ini`**: Pytestの実行設定を定義するファイルです。テストの検出パターン、プラグイン、レポートオプションなどが含まれます。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの依存関係を記述したファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonライブラリの依存関係を記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: Ruffリンターの設定ファイルで、コードスタイルルール、無視するエラー、フォーマットオプションなどを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能のコアロジックを格納するパッケージです。
        - **`src/generate_repo_list/__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスなどを表示するバッジを生成するロジックが含まれます。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの技術的パラメータ（例: プロジェクト概要取得設定）を定義するYAML形式の設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するロジックが含まれます。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: メインのリポジトリ一覧生成スクリプトです。GitHub APIから情報を取得し、Markdownファイルを生成します。
        - **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD形式）のテンプレートファイルで、SEO強化のために使用されます。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報を処理するロジックが含まれます。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックが含まれます。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリから特定のMarkdownファイル（`generated-docs/project-overview.md`）を読み込み、プロジェクト概要を抽出するロジックが含まれます。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEからバッジ情報を抽出するロジックが含まれます。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換するロジックが含まれます。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するロジックが含まれます。
        - **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージや文言を一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレート処理を行うロジックが含まれます。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築や解析に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`機能の単体テストまたは統合テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: Pytestのテストフィクスチャやヘルパー関数を定義するファイルで、複数のテストファイルで共通して利用されます。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    - **`tests/test_check_large_files.py`**: `.github_automation`内の`check_large_files.py`スクリプトのテストを記述したファイルです。
    - **`tests/test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや解析に関するテストを記述したファイルです。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストを記述したファイルです。
    - **`tests/test_environment.py`**: テスト環境のセットアップや依存関係に関するテストを記述したファイルです。
    - **`tests/test_integration.py`**: プロジェクトの主要コンポーネント間の統合テストを記述したファイルです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
    - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストを記述したファイルです。

## 関数詳細説明
プロジェクト情報から具体的な関数名は検出されていませんが、ファイル名から推測される主要な関数とその役割は以下の通りです。

- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: プログラムのエントリーポイント。GitHub APIからリポジトリ情報を取得し、取得したデータを処理して、最終的なMarkdownファイルを生成します。

- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge(status: str) -> str`: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）を表すバッジのMarkdownまたはHTMLスニペットを生成します。

- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path: str) -> dict`: 指定されたパスからYAML形式の設定ファイルを読み込み、Python辞書として返します。
    - `get_setting(key: str, default=None)`: 設定ファイルから特定のキーの値を安全に取得します。

- **`src/generate_repo_list/date_formatter.py`**
    - `format_date(date_string: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> str`: ISO 8601形式などの日付文字列を受け取り、指定されたフォーマット文字列に従って整形された日付文字列を返します。

- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview(repo_api_url: str, config: dict) -> list[str]`: 指定されたリポジトリのURLと設定に基づき、`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出し、文字列のリストとして返します。

- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_markdown(repo_data: dict, template_content: str) -> str`: 処理されたリポジトリデータとMarkdownテンプレートを使用して、個々のリポジトリや全体のリポジトリ一覧のMarkdownコンテンツを生成します。

- **`src/generate_repo_list/repository_processor.py`**
    - `process_repository_data(raw_repo_list: list[dict], username: str) -> list[dict]`: GitHub APIから取得した生のリポジトリデータ（リスト）を受け取り、必要な情報の抽出、整形、分類などの処理を行い、表示に適した構造化されたリポジトリデータのリストとして返します。

- **`src/generate_repo_list/readme_badge_extractor.py`**
    - `extract_badges_from_readme(readme_content: str) -> list[dict]`: リポジトリのREADMEの内容から、画像やリンクの形式で埋め込まれたバッジ情報を抽出し、URLやaltテキストを含む辞書のリストとして返します。

- **`src/generate_repo_list/statistics_calculator.py`**
    - `calculate_stats(repo_list: list[dict]) -> dict`: リポジトリのリスト全体から、合計スター数、フォーク数、言語分布などの統計情報を計算して返します。

- **`src/generate_repo_list/template_processor.py`**
    - `render_template(template_path: str, context: dict) -> str`: 指定されたテンプレートファイルとコンテキストデータを使用して、最終的な出力文字列を生成します。

- **`src/generate_repo_list/url_utils.py`**
    - `build_github_api_url(username: str, endpoint: str = "repos") -> str`: 指定されたGitHubユーザー名とAPIエンドポイントに基づいて、GitHub APIへのリクエストURLを構築します。
    - `build_github_repo_url(username: str, repo_name: str) -> str`: 指定されたユーザー名とリポジトリ名から、GitHubリポジトリのURLを構築します。

- **`.github_automation/check_large_files/scripts/check_large_files.py`**
    - `check_files(repo_path: str, config: dict) -> bool`: 指定されたリポジトリパスと設定（例: 最大ファイルサイズ）に基づき、リポジトリ内のファイルを走査し、サイズ制限を超えるファイルがないかチェックします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-20 07:12:15 JST
