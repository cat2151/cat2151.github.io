Last updated: 2026-08-01

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、GitHub Pages向けのリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、リポジトリの検索エンジン可視性を向上させます。
- 検索エンジンやLLMによるリポジトリ参照を促進し、開発効率の向上に貢献します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレータ。生成されたMarkdownファイルを処理し、Webサイトを構築します。
    - **Markdown**: リポジトリ一覧や個別のリポジトリ概要を記述するための軽量マークアップ言語。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **GitHub API**: GitHubリポジトリの情報（メタデータ、プロジェクト概要など）をプログラム的に取得するためのインターフェース。
    - **PyYAML**: `.yml` 形式の設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`など）をPythonから読み書きするために使用されます。
    - **TOML**: `secrets.toml` など、設定ファイルや秘密情報を扱うために使用される可能性のある形式です。
- テスト:
    - **pytest**: Pythonプロジェクトのテストフレームワーク。単体テストや統合テストの実行、テストの自動化に使用されます。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報を取得し、Markdownファイルを生成する主要なロジックを実装しています。
- 言語機能:
    - **Python**: プロジェクトの主要な開発言語であり、すべてのスクリプトがPythonで記述されています。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリの存在から、コード品質チェック（例: 大容量ファイルチェック）などの自動化されたワークフローが設定されていると推測されます。
- 開発標準:
    - **ruff**: Pythonコードのリンティングとフォーマットを統合的に行うツール。コード品質の維持と統一されたコーディングスタイルを強制します。
    - **EditorConfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を定義し、維持するための設定ファイル形式です。

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
- **`.editorconfig`**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなど、基本的なコーディングスタイルの一貫性を維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsを使った自動化スクリプトを格納するディレクトリ。
    - **`check_large_files/`**: 大容量ファイルをチェックするためのスクリプトと設定が含まれる。
        - **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明する。
        - **`check-large-files.toml`**: 大容量ファイルチェックのルールや閾値を定義する設定ファイル。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されているファイル。
- **`README.md`**: プロジェクト全体の概要、目的、機能、セットアップ方法、使用方法、ライセンスなどの主要情報を提供する、ユーザーが最初に読むドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を含む。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供。
- **`debug_project_overview.py`**: `project_overview` 機能のデバッグやテストを目的としたスクリプト。
- **`generated-docs/`**: 各リポジトリから取得・生成されたドキュメント（例: project-overview.md）が一時的に、または最終的に格納される可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイル。
- **`index.md`**: プロジェクトのメイン出力ファイル。生成されたリポジトリ一覧がMarkdown形式でこのファイルに書き込まれ、GitHub Pagesのトップページとして表示される。
- **`issue-notes/`**: 開発中の課題やメモが保存されている可能性のあるディレクトリ。
    - **`22.md`**: 特定の課題（例: Issue #22）に関するメモや詳細情報が記載されたMarkdownファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータ定義ファイル。アプリの表示方法や動作を設定する。
- **`pytest.ini`**: `pytest` テストフレームワークの設定ファイル。テスト検出ルール、プラグイン、テストオプションなどを定義。
- **`requirements-dev.txt`**: 開発およびテスト環境でこのプロジェクトに必要なPythonライブラリの依存関係リスト。`requirements.txt` の内容に加え、開発・テスト専用のライブラリを含む。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために最低限必要なPythonライブラリの依存関係リスト。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしてはいけないかを指示するファイル。
- **`ruff.toml`**: `ruff` リンター・フォーマッターの設定ファイル。Pythonコードの静的解析ルール、自動修正設定、無視するファイルパターンなどを定義。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **`src/__init__.py`**: Pythonパッケージとして認識させるための空ファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        - **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして認識させるための空ファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスに応じたバッジのURLやMarkdownを生成するロジックを担う。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの、システム固有の技術的パラメータを設定するためのファイル。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml` や他の設定ファイルを読み込み、設定値にアクセスするためのユーティリティ関数を提供する。
        - **`src/generate_repo_list/date_formatter.py`**: リポジトリの作成日時や最終更新日時などの日付情報を、人間が読みやすい形式に整形する機能。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成する全体の処理をオーケストレーションする。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO強化のため、JSON-LD形式の構造化データテンプレートを定義するファイル。検索エンジンにコンテンツの情報をより正確に伝えるために使用される。
        - **`src/generate_repo_list/language_info.py`**: 各リポジトリのプログラミング言語に関する情報を処理し、集計や表示に役立つ機能を提供する。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報に基づいて、Jekyllが解釈できるMarkdown形式の文字列を生成するコアロジック。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの概要テキストを自動で取得・抽出する機能。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータスバッジ）を解析・抽出する機能。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した内部データ構造に変換する役割を担う。
        - **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownのSEO関連のメタデータやテンプレート設定を定義するファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算または集計する機能。
        - **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownファイル内で使用される、表示メッセージや文言を管理するための設定ファイル。多言語対応や文言変更を容易にする。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成の際に使用するテンプレートファイル（例: Jinja2テンプレート）を読み込み、取得したデータで埋め込んで最終的なコンテンツを生成する。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、エンコーディングなど、URLに関連する様々なユーティリティ関数を提供する。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストまたは結合テストを含むファイル。
- **`tests/`**: プロジェクトの自動テストコードを格納するディレクトリ。
    - **`conftest.py`**: `pytest` のフィクスチャ（テストヘルパー）やテスト関連の設定を定義するファイル。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能のテスト。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`test_environment.py`**: テスト環境のセットアップや依存関係に関するテスト。
    - **`test_integration.py`**: システム全体の主要なフローに関する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
    - `main(username: str, output_file: str, limit: int = None)`: プログラムのエントリポイント。指定されたGitHubユーザーのリポジトリ情報をGitHub APIから取得し、処理後、指定された出力ファイルパスにMarkdown形式のリポジトリ一覧を生成します。`limit` オプションで処理するリポジトリ数を制限できます。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge_markdown(status: str, label: str)`: 指定されたステータスとラベルに基づいて、Markdown形式のバッジ文字列を生成します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path: str)`: 指定されたYAML設定ファイルのパスから設定を読み込み、Pythonオブジェクトとして返します。
- **`src/generate_repo_list/date_formatter.py`**
    - `format_date_for_display(iso_date_string: str)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式（例: "YYYY年MM月DD日"）に変換して返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_repo_list_markdown(repos_data: list, config: dict, strings: dict)`: 処理されたリポジトリデータのリスト、設定、表示文字列を受け取り、全体のリポジトリ一覧を構成するMarkdown文字列を生成します。
    - `_generate_single_repo_section(repo_data: dict, config: dict, strings: dict)`: 単一のリポジトリデータから、そのリポジトリの表示セクションをMarkdown形式で生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_and_parse_project_overview(repo_full_name: str, config: dict)`: 指定されたリポジトリの完全名と設定情報に基づいて、リポジトリ内の `project-overview.md` ファイルからプロジェクト概要の3行説明を取得し、返します。GitHub APIを介してファイルを読み込みます。
- **`src/generate_repo_list/repository_processor.py`**
    - `process_raw_repository_data(raw_repo_data: dict, config: dict)`: GitHub APIから取得した生のリポジトリデータ（辞書形式）を受け取り、整形・加工して、Markdown生成に適したクリーンなデータ構造に変換して返します。これには、関連情報の取得や計算も含まれます。
- **`src/generate_repo_list/template_processor.py`**
    - `render_markdown_template(template_content: str, data: dict)`: テンプレート文字列とデータを入力として受け取り、データをテンプレートに埋め込んで最終的なMarkdown文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**
    - `get_github_repo_content_url(username: str, repo_name: str, path: str)`: 指定されたユーザー名、リポジトリ名、ファイルパスから、GitHubリポジトリ内の特定のファイルコンテンツにアクセスするための生のURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層に関する具体的な情報は提供されていないため、詳細なツリーは生成できません。
しかし、一般的なフローとして以下の主要な呼び出し関係が推測されます。

main (generate_repo_list.py)
├── load_config (config_manager.py)
├── process_raw_repository_data (repository_processor.py)
│   └── fetch_and_parse_project_overview (project_overview_fetcher.py)
├── generate_repo_list_markdown (markdown_generator.py)
│   ├── _generate_single_repo_section (markdown_generator.py)
│   │   ├── generate_badge_markdown (badge_generator.py)
│   │   ├── format_date_for_display (date_formatter.py)
│   │   └── render_markdown_template (template_processor.py)
│   └── render_markdown_template (template_processor.py)

---
Generated at: 2026-08-01 07:23:26 JST
