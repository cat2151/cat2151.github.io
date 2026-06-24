Last updated: 2026-06-25

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEOを強化し、自身のリポジトリ一覧と各プロジェクト概要を自動生成するシステムです。
- GitHub APIから情報を取得し、Jekyll互換のMarkdown形式で出力。LLMによるリポジトリ参照失敗の緩和も目指します。
- バッジ、アクティブ/アーカイブ分類、各リポジトリの3行概要自動取得表示など、豊富な機能を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - GitHub Pagesサイトのコンテンツ生成とホスティングに利用される静的サイトジェネレータ。
- 音楽・オーディオ: 該当なし - このプロジェクトでは音楽やオーディオ関連の技術は使用していません。
- 開発ツール: Python - プロジェクトの主要なロジックを実装するために使用されるプログラミング言語。
- テスト: pytest - Pythonアプリケーションの単体テストや統合テストを実行するためのフレームワーク。
- ビルドツール: Pythonスクリプト - リポジトリ情報からMarkdownファイルを生成する処理自体が、このプロジェクトにおけるコンテンツの「ビルド」を担当します。
- 言語機能: Python言語機能 (例: f-string, データ構造など) - Pythonの標準的な機能と構文。 YAML - 設定ファイルの記述に利用される人間が読みやすいデータシリアライゼーション形式。 TOML - 秘密情報の管理（GitHubトークンなど）に使用される設定ファイル形式。
- 自動化・CI/CD: GitHub Actions (部分的に利用) - `.github_automation` ディレクトリに存在するスクリプト（例: 大容量ファイルチェック）は、自動化の可能性を示唆しますが、CI/CDはローカル開発重視とされています。
- 開発標準: ruff - Pythonコードのフォーマットとリンティングを自動で行い、コード品質と一貫性を保つためのツール。

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

*   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
*   **`.github_automation/`**: GitHub Actionsに関連する自動化スクリプトや設定を格納するディレクトリです。
    *   **`.github_automation/check_large_files/`**: 大容量ファイルをチェックするためのスクリプト群です。
        *   `README.md`: `check_large_files` 機能の説明ドキュメントです。
        *   `check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルです。
        *   `scripts/check_large_files.py`: 実際の大容量ファイルチェックロジックを実装したPythonスクリプトです。
*   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
*   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
*   **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを記述した、プロジェクトの顔となるドキュメントです。
*   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を定義します。
*   **`assets/`**: Jekyllサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
    *   `favicon-*.png`: サイトのファビコン（ブラウザのタブに表示されるアイコン）の異なるサイズを提供します。
*   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
*   **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するディレクトリです。
*   **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト認証に使用される可能性のある検証ファイルです。
*   **`index.md`**: 自動生成されるリポジトリ一覧のメインページとなるMarkdownファイルです。JekyllによってHTMLに変換され、GitHub Pagesで表示されます。
*   **`issue-notes/`**: 開発中の課題やメモを管理するためのディレクトリです。
    *   `22.md`: 特定の課題に関する詳細なメモや情報が記載されたMarkdownファイルです。
*   **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、PWA（Progressive Web App）の設定やアイコン情報などを定義します。
*   **`pytest.ini`**: `pytest`フレームワークの設定ファイルで、テストの挙動やオプションを定義します。
*   **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリをリストアップしたファイルです。
*   **`requirements.txt`**: プロジェクトの本番稼働に必要なPythonライブラリをリストアップしたファイルです。
*   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイルです。
*   **`ruff.toml`**: Pythonコードのリンティング（構文やスタイルチェック）とフォーマットを行う`ruff`ツールの設定ファイルです。
*   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    *   **`src/generate_repo_list/`**: GitHubリポジトリ一覧を生成するシステムの主要モジュールを格納するディレクトリです。
        *   `__init__.py`: Pythonパッケージであることを示すファイルです。
        *   `badge_generator.py`: リポジトリのステータスに応じたバッジのMarkdownを生成するロジックを含みます。
        *   `config.yml`: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイルです。
        *   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するロジックを提供します。
        *   `date_formatter.py`: 日付を特定のフォーマットで整形するためのユーティリティ関数を提供します。
        *   `generate_repo_list.py`: プロジェクトのメインエントリスクリプト。リポジトリ情報の取得、処理、Markdown生成をオーケストレートします。
        *   `json_ld_template.json`: SEO強化のため、構造化データ（JSON-LD）のテンプレートを定義します。
        *   `language_info.py`: リポジトリの主要言語情報に関する処理や表示を担当します。
        *   `markdown_generator.py`: 処理されたリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを含みます。
        *   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得する機能を提供します。
        *   `readme_badge_extractor.py`: リポジトリのREADMEファイルからバッジ情報を抽出するロジックを含みます。
        *   `repository_processor.py`: GitHub APIからリポジトリ情報を取得し、必要な形式に整形・フィルタリングする主要な処理を担当します。
        *   `seo_template.yml`: SEO関連のメタデータや設定のテンプレートを定義します。
        *   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        *   `strings.yml`: UIに表示されるメッセージや文言を一元的に管理するための設定ファイルです。
        *   `template_processor.py`: Markdown生成の際に使用されるテンプレートを処理し、データで埋める機能を提供します。
        *   `url_utils.py`: URLの生成や検証など、URL関連のユーティリティ関数を提供します。
*   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
*   **`tests/`**: プロジェクトの自動テストコードを格納するディレクトリです。
    *   `conftest.py`: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    *   `test_*.py`: 各モジュールや機能に対応する単体テストや統合テストのスクリプトです。

## 関数詳細説明
このプロジェクトでは、主に`src/generate_repo_list/`ディレクトリ内のPythonファイルにロジックが実装されています。具体的な関数の引数や戻り値の詳細はプロジェクト情報に記載がないため、ここでは各ファイルの主要な役割から推測される主要関数の役割を説明します。

*   **`src/generate_repo_list/generate_repo_list.py`**
    *   **`main()`**: プログラムのエントリポイント。GitHub APIからリポジトリ情報を取得し、設定に基づいて処理を行い、最終的なMarkdownコンテンツを出力ファイルに生成する一連の流れをオーケストレートします。
*   **`src/generate_repo_list/config_manager.py`**
    *   **`load_config(config_path: str) -> dict`**: 指定されたパスからYAML設定ファイルを読み込み、辞書形式で設定値を提供します。
    *   **`load_secrets(secrets_path: str) -> dict`**: 指定されたパスからTOML形式の秘密情報ファイルを読み込み、GitHubトークンなどの機密データを提供します。
*   **`src/generate_repo_list/repository_processor.py`**
    *   **`fetch_and_process_repositories(username: str, token: str, limit: int = None) -> list`**: 指定されたGitHubユーザー名のリポジトリをGitHub API経由で取得し、必要な情報（説明、言語、更新日時など）を抽出・整形してリスト形式で返します。
*   **`src/generate_repo_list/project_overview_fetcher.py`**
    *   **`fetch_project_overview(repo_name: str, config: dict) -> str`**: 指定されたリポジトリ名と設定に基づき、そのリポジトリ内の特定のファイルからプロジェクトの3行概要を取得して文字列で返します。
*   **`src/generate_repo_list/markdown_generator.py`**
    *   **`generate_repo_list_markdown(repositories: list, config: dict, strings: dict) -> str`**: 処理されたリポジトリ情報のリストと設定、表示文言を受け取り、それらを基にリポジトリ一覧のMarkdownコンテンツを生成して文字列で返します。
    *   **`generate_seo_metadata(repo_info: dict, template: dict) -> str`**: リポジトリ情報とSEOテンプレートを使って、検索エンジン最適化のためのメタデータ（JSON-LDなど）を生成します。
*   **`src/generate_repo_list/badge_generator.py`**
    *   **`generate_repo_status_badge(repo_status: str) -> str`**: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）に応じて、適切な表示のMarkdown形式のバッジ文字列を生成します。
*   **`src/generate_repo_list/date_formatter.py`**
    *   **`format_datetime(datetime_str: str) -> str`**: ISO形式などの日付文字列を受け取り、人間が読みやすい形式に整形して返します。
*   **`src/generate_repo_list/statistics_calculator.py`**
    *   **`calculate_language_percentages(languages_data: dict) -> dict`**: リポジトリの言語使用率データを受け取り、各言語のパーセンテージを計算して返します。
*   **`src/generate_repo_list/readme_badge_extractor.py`**
    *   **`extract_badges_from_readme(readme_content: str) -> list`**: READMEファイルのコンテンツから、Markdown形式のバッジ情報（例: shields.io）を検出してリストで返します。
*   **`src/generate_repo_list/template_processor.py`**
    *   **`render_template(template_content: str, data: dict) -> str`**: テンプレート文字列とデータ辞書を受け取り、データをテンプレートに埋め込んで最終的な文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
プロジェクト情報に具体的な関数の呼び出し関係が提供されていないため、詳細なツリーを生成することはできません。

---
Generated at: 2026-06-25 07:31:19 JST
