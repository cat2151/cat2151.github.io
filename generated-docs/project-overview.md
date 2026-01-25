Last updated: 2026-01-26

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得するPythonシステムです。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照の改善を支援します。

## 技術スタック
- フロントエンド: なし（生成されるのはMarkdownコンテンツであり、レンダリングはJekyllとブラウザに依存）
- 音楽・オーディオ: なし
- 開発ツール:
    - Python: 主要なスクリプト言語として、リポジトリ情報取得とMarkdown生成ロジックに使用されています。
    - GitHub API: GitHubのリポジトリ情報（説明、言語、星の数など）をプログラムから取得するために利用されます。
    - ruff: Pythonコードのフォーマットとリント（静的解析）を行うためのツールで、コード品質の維持に貢献します。
- テスト:
    - pytest: Pythonプロジェクトのテストフレームワークとして、コードの機能が期待通りに動作するかを検証するために使用されます。
- ビルドツール: なし（直接的なビルドプロセスはありません。生成されたMarkdownはJekyllによってサイトとして構築されます）
- 言語機能:
    - Python: 最新の言語機能を活用し、効率的なスクリプト処理を実現しています。
- 自動化・CI/CD:
    - ruff, pytest: ローカルでの開発品質確保のため、コードスタイルチェックとテスト実行が自動化されています。
- 開発標準:
    - ruff: コードスタイルの一貫性を保ち、可読性と保守性を向上させるための標準ツールとして設定されています。

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
-   `.editorconfig`: 異なるエディタやIDEを使用する開発者間で、コードのスタイル（インデント、改行コードなど）を一貫させるための設定ファイルです。
-   `.gitignore`: Gitによるバージョン管理から除外すべきファイルやディレクトリ（例: ビルド生成物、ログ、個人設定など）を指定します。
-   `LICENSE`: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載しており、ソフトウェアの利用、配布、変更に関する条件を定めます。
-   `README.md`: プロジェクトの概要、目的、主な機能、セットアップ方法、使用方法などが記述された主要なドキュメントファイルです。
-   `_config.yml`: Jekyllサイト全体の構成設定を定義するファイルで、サイトのタイトル、テーマ、プラグインなどの情報を保持します。
-   `assets/`: サイトで使用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリです。`favicon-*.png` ファイルはサイトのファビコン（ブラウザタブなどに表示されるアイコン）を提供します。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグやテストに特化したPythonスクリプトと考えられます。
-   `generated-docs/`: 他のリポジトリから自動取得された `project-overview.md` ファイルが格納されることを想定したディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのウェブマスターツールによるサイトの所有権確認に使用されるHTMLファイルです。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される主要なMarkdownファイルで、GitHubリポジトリの一覧が含まれます。
-   `issue-notes/`: 課題や議論のメモをMarkdown形式で整理して保存するためのディレクトリです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルで、アプリのホーム画面アイコン、表示モード、起動URLなどをブラウザに指示します。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの設定ファイルで、テスト実行時のオプションやプラグインの設定を定義します。
-   `requirements-dev.txt`: 開発環境やテスト環境で必要となるPythonライブラリの依存関係を記述したファイルです。
-   `requirements.txt`: プロジェクトの実行に最低限必要なPythonライブラリの依存関係を記述したファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはならないかを指示するファイルです。
-   `ruff.toml`: Pythonコードのリンター・フォーマッターであるruffの設定ファイルで、コーディングスタイルや品質に関するルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `src/__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `src/generate_repo_list/`: リポジトリ一覧生成に関するメインのロジックを保持するパッケージです。
        -   `src/generate_repo_list/__init__.py`: Pythonサブパッケージであることを示すファイルです。
        -   `src/generate_repo_list/badge_generator.py`: GitHubリポジトリの言語やステータスに応じたバッジ画像を生成するロジックを担当します。
        -   `src/generate_repo_list/config.yml`: プロジェクトの動作に関する技術的パラメータ（例: APIタイムアウト、キャッシュ設定）を設定するYAMLファイルです。
        -   `src/generate_repo_list/config_manager.py`: `config.yml` などの設定ファイルを読み込み、管理するためのロジックを提供します。
        -   `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を整形し、人間が読みやすい形式に変換する機能を提供します。
        -   `src/generate_repo_list/generate_repo_list.py`: このプロジェクトのメインスクリプトであり、リポジトリ情報の取得からMarkdownファイル生成までの一連の処理をオーケストレートします。
        -   `src/generate_repo_list/json_ld_template.json`: SEO強化のため、構造化データ（JSON-LD形式）のテンプレートを定義します。
        -   `src/generate_repo_list/language_info.py`: リポジトリの主要言語に関する情報（例: 色分け、統計）を処理します。
        -   `src/generate_repo_list/markdown_generator.py`: 取得したリポジトリ情報をもとに、Jekyll互換のMarkdownコンテンツを生成するロジックを担当します。
        -   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得する機能を提供します。
        -   `src/generate_repo_list/readme_badge_extractor.py`: READMEファイルなどから特定のバッジ情報（例: ビルドステータス、ライセンス）を抽出するロジックを提供します。
        -   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換する機能を提供します。
        -   `src/generate_repo_list/seo_template.yml`: 検索エンジン最適化（SEO）関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        -   `src/generate_repo_list/statistics_calculator.py`: リポジトリに関する統計情報（例: スター数、フォーク数、最終更新日）を計算または集計します。
        -   `src/generate_repo_list/strings.yml`: 表示メッセージや文言（例: ヘッダー、フッター、分類ラベル）を一元管理するためのYAMLファイルです。
        -   `src/generate_repo_list/template_processor.py`: Markdown生成時に使用するテンプレートファイルの読み込みと、データの埋め込みを行う機能を提供します。
        -   `src/generate_repo_list/url_utils.py`: URLの構築、解析、検証など、URLに関連するユーティリティ機能を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py` の機能に特化したテストスクリプトです。
-   `tests/`: プロジェクト全体のテストケースを格納するディレクトリです。
    -   `tests/test_badge_generator_integration.py`: バッジ生成機能の統合テストを扱います。
    -   `tests/test_config.py`: 設定ファイル読み込みや管理機能のテストを行います。
    -   `tests/test_date_formatter.py`: 日付整形機能のテストを行います。
    -   `tests/test_environment.py`: 実行環境のセットアップや依存関係に関するテストを行います。
    -   `tests/test_integration.py`: プロジェクト全体の主要なフローに関する統合テストを扱います。
    -   `tests/test_markdown_generator.py`: Markdown生成機能のテストを行います。
    -   `tests/test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを行います。
    -   `tests/test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを行います。
    -   `tests/test_repository_processor.py`: リポジトリ情報処理機能のテストを行います。

## 関数詳細説明
プロジェクト情報から具体的な関数名、引数、戻り値に関する詳細な情報は特定できませんでした。しかし、上記ファイル群の役割から、それぞれが以下の目的を持つ関数群を含んでいると考えられます。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: プログラムのエントリーポイント。コマンドライン引数の解析、設定の読み込み、リポジトリ情報の取得、処理、Markdown生成までの一連のフローを制御する。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(repo_info)`: リポジトリ情報に基づいて、特定の特性（言語、ライセンスなど）を示すバッジのURLやMarkdownを生成する。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(file_path)`: 指定されたパスからYAMLまたはTOML形式の設定ファイルを読み込み、設定オブジェクトを返す。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_date(datetime_obj, format_string)`: 日付オブジェクトを指定されたフォーマット文字列に従って整形する。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repo_list_markdown(repositories_data)`: 複数のリポジトリデータを受け取り、完全なリポジトリ一覧のMarkdown文字列を生成する。
    -   `generate_repository_entry(repo_data)`: 個々のリポジトリデータから、そのリポジトリに対応するMarkdown形式のエントリ（タイトル、説明、バッジなど）を生成する。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(github_api_client, repo_name, config)`: 指定されたリポジトリから `generated-docs/project-overview.md` を取得し、設定に基づいて概要テキストを抽出する。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository_data(raw_repo_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、整形、フィルタリング、追加情報の計算などを行い、構造化されたデータとして返す。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-26 07:06:21 JST
