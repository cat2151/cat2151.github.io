Last updated: 2026-01-19

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ情報を自動収集し一覧を生成するシステムです。
- GitHub APIを利用してSEOに最適化されたMarkdown形式のページを自動生成します。
- 検索エンジンでの発見性向上とLLMによるリポジトリ参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll) - 最終的なウェブサイトのホスティング環境と静的サイトジェネレータとして利用されます。
- 音楽・オーディオ: なし
- 開発ツール:
    - Ruff: Pythonコードの静的解析とフォーマットを自動で行い、コード品質と一貫性を保ちます。
    - Pytest: Pythonアプリケーションのテストフレームワークで、効率的な単体テストおよび結合テストの実行を支援します。
- テスト: Pytest - Pythonコードの機能検証と品質保証のために使用されます。
- ビルドツール: Python - スクリプト実行によりMarkdownファイルの生成を行います。
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語として、リポジトリ情報の取得からMarkdown生成までを制御します。
    - YAML: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に使用されます。
    - Markdown: 生成されるリポジトリ一覧の出力フォーマット、および各リポジトリの概要ファイル（`project-overview.md`）の入力フォーマットとして使用されます。
    - JSON: SEOメタデータ（JSON-LD）のテンプレート記述に使用されます。
    - TOML: 秘密情報（例: GitHubトークン）の安全な管理に利用されます。
- 自動化・CI/CD: GitHub API - GitHubリポジトリの情報を自動的に取得するために使用されます。
- 開発標準: Ruff - コードスタイルの一貫性と品質を強制するために導入されています。

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
  📄 test_badge_generator_integration.py
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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、文字コードなど）を維持するための設定ファイルです。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義します。
-   `LICENSE`: プロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイルです。
-   `README.md`: プロジェクトの概要、目的、設定方法、使用方法、ライセンスなどの包括的な情報を提供します。
-   `_config.yml`: Jekyllサイト全体の動作を制御する設定ファイルで、サイトのタイトルやテーマなどを定義します。
-   `assets/`: GitHub Pagesサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: ウェブサイトのファビコンや、異なるデバイス・プラットフォームでのアプリアイコンとして使用される画像ファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher` モジュールのデバッグや単体テストを支援するためのスクリプトです。
-   `generated-docs/`: このプロジェクトによって生成されるドキュメントやデータが格納される予定のディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
-   `index.md`: GitHub Pagesサイトのルートページとして機能するMarkdownファイルです。生成されたリポジトリ一覧がここに表示されます。
-   `issue-notes/`: 開発中の課題、検討事項、または過去の課題に関するメモをMarkdown形式で格納するディレクトリです。
    -   `10.md`, `12.md`, `14.md`, `16.md`, `18.md`, `2.md`, `4.md`, `6.md`, `8.md`: それぞれ特定の課題や議論に関する詳細なメモが記述されています。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面にウェブサイトを追加する際のアイコンや表示モードなどを定義します。
-   `pytest.ini`: Pythonのテストフレームワークである`pytest`の設定ファイルです。テストの発見ルールやプラグインなどを定義します。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを記述したファイルです。
-   `requirements.txt`: 本番環境（スクリプト実行時）で必要となるPythonパッケージとそのバージョンを記述したファイルです。
-   `robots.txt`: 検索エンジンクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、また避けるべきかを指示するファイルです。
-   `ruff.toml`: コードスタイルチェッカーおよびフォーマッタである`ruff`の設定ファイルです。コードの整形ルールやlintingルールを定義します。
-   `src/`: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    -   `__init__.py`: `src` ディレクトリがPythonパッケージであることを示します。
    -   `generate_repo_list/`: リポジトリ一覧生成システムの核となるPythonモジュール群をまとめたパッケージです。
        -   `__init__.py`: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示します。
        -   `badge_generator.py`: リポジトリの言語バッジやステータスバッジなどの情報を生成するロジックが含まれます。
        -   `config.yml`: プロジェクト概要取得機能などの技術的なパラメータを定義する設定ファイルです。
        -   `config_manager.py`: `config.yml` や `secrets.toml` などの設定ファイルや秘密情報を読み込み、管理する役割を持つモジュールです。
        -   `date_formatter.py`: 日付や時刻のフォーマット変換に関するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのメインエントリスクリプトです。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdown生成までの一連の処理を調整します。
        -   `json_ld_template.json`: 検索エンジン最適化 (SEO) のための構造化データ（JSON-LD）のテンプレートです。
        -   `language_info.py`: GitHub APIから取得したリポジトリの言語利用状況を解析し、整形する機能を持つモジュールです。
        -   `markdown_generator.py`: 処理されたリポジトリ情報に基づいて、GitHub Pages用のMarkdownコンテンツを生成する主要なモジュールです。
        -   `project_overview_fetcher.py`: 各GitHubリポジトリの `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を抽出・取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジ情報を抽出する機能を持つモジュールです。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
        -   `seo_template.yml`: 生成されるMarkdownのSEO関連メタデータを記述するためのテンプレート設定ファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計する機能を提供します。
        -   `strings.yml`: UIに表示されるメッセージや文言を外部化し、国際化や文言の一元管理を容易にするための設定ファイルです。
        -   `template_processor.py`: Markdown生成の際に使用されるテンプレートエンジンや、プレースホルダー置換などの処理を管理するモジュールです。
        -   `url_utils.py`: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールが正しく動作するかを確認するためのテストスクリプトです。
-   `tests/`: プロジェクトのテストコードを格納するディレクトリです。
    -   `test_badge_generator_integration.py`: バッジ生成機能の複数のコンポーネントを結合したテストを行います。
    -   `test_config.py`: `config_manager` モジュールなど、設定ファイルの読み込みと管理に関するテストを行います。
    -   `test_date_formatter.py`: `date_formatter` モジュール内の日付フォーマット機能のテストを行います。
    -   `test_environment.py`: プロジェクトの実行環境や依存関係が正しく設定されているかを確認するテストです。
    -   `test_integration.py`: システム全体または主要なサブシステム間の連携を確認する結合テストです。
    -   `test_markdown_generator.py`: `markdown_generator` モジュールが期待通りのMarkdownを生成するかをテストします。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールがリポジトリ概要を正しく取得・解析するかをテストします。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールがREADMEからバッジを正確に抽出するかをテストします。
    -   `test_repository_processor.py`: `repository_processor` モジュールがリポジトリデータを正しく処理・整形するかをテストします。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャ（引数、戻り値）を直接抽出できませんでしたが、各ファイルで想定される主要な関数の役割と機能について説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: スクリプトのエントリーポイント。コマンドライン引数をパースし、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といった一連のワークフローをオーケストレートします。
    -   `_parse_args()`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、処理リミットなどのオプションを `argparse` を用いて取得します。

-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(config_path)`: 指定されたYAMLファイルパスから設定情報を読み込み、辞書またはオブジェクトとして返します。
    -   `load_secrets(secrets_path)`: 指定されたTOMLファイルパスから秘密情報（例: GitHubトークン）を安全に読み込みます。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_language_badge(language_data)`: リポジトリの主要言語情報に基づいて、視覚的な言語バッジ（SVG文字列など）を生成します。
    -   `generate_status_badge(repo_status)`: リポジトリのステータス（例: Active, Archived, Fork）を示すバッジを生成します。

-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_datetime(datetime_obj, format_string)`: `datetime` オブジェクトを指定された書式文字列に従って整形した文字列として返します。

-   **`src/generate_repo_list/language_info.py`**:
    -   `get_main_language(languages_data)`: GitHub APIから取得した言語情報から、リポジトリの最も主要な言語を特定します。
    -   `get_language_breakdown(languages_data)`: リポジトリの使用言語とその割合を計算し、整形された形式で提供します。

-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repo_markdown(repo_data, config)`: 処理済みの単一リポジトリデータと設定情報を受け取り、そのリポジトリに関するMarkdownスニペットを生成します。
    -   `generate_full_markdown(repo_list, config)`: 複数のリポジトリデータを受け取り、完全なリポジトリ一覧ページを構成するMarkdownファイルを生成します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_name, owner, target_file, config)`: 指定されたGitHubリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）の内容を取得し、設定されたセクションから3行のプロジェクト概要を抽出します。
    -   `_parse_overview_markdown(markdown_content, section_title)`: 取得したMarkdownコンテンツから、特定のセクションタイトルを見つけ、その下の箇条書きを抽出してプロジェクト概要として返します。

-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   `extract_badges_from_readme(readme_content)`: リポジトリのREADMEコンテンツを解析し、Markdown形式で埋め込まれたバッジのURLやALTテキストなどの情報を抽出します。

-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository_data(raw_repo_data, config)`: GitHub APIから直接取得したリポジトリの生データを受け取り、プロジェクトのニーズに合わせて必要な情報を抽出し、整形・強化（例: 概要の追加、統計計算など）します。

-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   `calculate_star_count(repo_data)`: リポジトリのスター数を取得します。
    -   `calculate_fork_count(repo_data)`: リポジトリのフォーク数を取得します。

-   **`src/generate_repo_list/template_processor.py`**:
    -   `render_template(template_string, data)`: 指定されたテンプレート文字列とデータを使用して、プレースホルダーを置換し、最終的なコンテンツを生成します。

-   **`src/generate_repo_list/url_utils.py`**:
    -   `build_github_api_url(username, endpoint)`: GitHub APIのエンドポイントURLを構築します。
    -   `is_valid_url(url)`: 与えられた文字列が有効なURLであるかを検証します。

## 関数呼び出し階層ツリー
```
利用可能な情報からは関数呼び出し階層を生成できませんでした。

---
Generated at: 2026-01-19 07:06:17 JST
