Last updated: 2026-06-26

# Project Overview

## プロジェクト概要
- GitHub API を活用し、GitHub Pages サイト向けにリポジトリ一覧を自動生成します。
- 生成されたMarkdownはSEO最適化され、検索エンジンやLLMからの参照性を向上させます。
- 各リポジトリの概要を自動抽出し、アクティブ/アーカイブ/フォーク別に整理して表示します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesでウェブサイトを構築するための静的サイトジェネレータ。本プロジェクトが生成するMarkdownはJekyllによって処理され、HTMLページとして公開されます。
    - Markdown: 生成されるリポジトリ一覧のコンテンツ形式。JekyllがこれをパースしてWebページとして表示します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: メインの開発言語。リポジトリ情報の取得、処理、Markdown生成スクリプトが実装されています。
    - GitHub API: GitHubのリポジトリ情報をプログラムから取得するために利用されます。
    - PyYAML: 設定ファイル (`config.yml`, `strings.yml`など) の読み書きに使用されます。
    - requests: HTTPリクエストを送信し、GitHub APIと通信するために使用されます。
    - toml: シークレットファイル (`secrets.toml`) の読み書きに使用されます。
- テスト:
    - pytest: Pythonアプリケーションのテストフレームワーク。単体テストや統合テストの実行に利用されます。
- ビルドツール:
    - (直接的なビルドツールはありません。Pythonスクリプトがコンテンツ生成の役割を担います。)
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語。
    - YAML: 設定ファイル (`config.yml`, `strings.yml`) やSEOテンプレートの記述に使用されるデータ形式。
    - Markdown: 出力されるリポジトリ一覧コンテンツの記述形式。
    - JSON: GitHub APIからのレスポンスデータ形式、およびJSON-LD構造化データ (`json_ld_template.json`) の記述形式。
- 自動化・CI/CD:
    - GitHub Pages: 生成されたMarkdownファイルをホストし、ウェブサイトとして公開するGitHubのサービス。
- 開発標準:
    - ruff: PythonコードのLinterおよびFormatter。コード品質の維持とスタイルの一貫性を保証します。
    - .editorconfig: 異なるIDEやエディタ間でのコードスタイルの一貫性を維持するための設定ファイル。

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
-   `.editorconfig`: エディタ設定ファイル。インデントスタイルや文字コードなど、プロジェクトのコードスタイルを定義し、開発者間で統一します。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや設定ファイルを格納するディレクトリ。
    -   `check_large_files/README.md`: 大容量ファイルチェックツールの説明。
    -   `check-large-files.toml`: 大容量ファイルチェックツールの設定ファイル。
    -   `scripts/check_large_files.py`: 指定されたサイズを超えるファイルを検出するためのPythonスクリプト。
-   `.gitignore`: Gitによってバージョン管理の対象外とするファイルやディレクトリを指定する設定ファイル。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   `README.md`: プロジェクトの概要、目的、使用方法、設定、開発者向けヒントなどを記述したメインのドキュメントファイル。
-   `_config.yml`: Jekyllサイト全体のグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどが定義されます。
-   `assets/`: サイトで使用される画像、アイコン、スタイルシートなどの静的アセットを格納するディレクトリ。
    -   `favicon-16x16.png`: 16x16ピクセルのファビコン。
    -   `favicon-192x192.png`: 192x192ピクセルのファビコン。
    -   `favicon-32x32.png`: 32x32ピクセルのファビコン。
    -   `favicon-512x512.png`: 512x512ピクセルのファビコン。
-   `debug_project_overview.py`: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグやテストに用いられるスクリプト。
-   `generated-docs/`: 他のリポジトリから自動取得された `project-overview.md` ファイルが格納されることを想定したディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権認証に使用されるHTMLファイル。
-   `index.md`: GitHub Pagesのルートページとして表示されるMarkdownファイル。本プロジェクトで生成されるリポジトリ一覧の出力先となります。
-   `issue-notes/`: 開発中に発生した課題やそのメモを格納するディレクトリ。
    -   `22.md`: 特定の課題に関するメモファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の定義ファイル。アプリの表示設定やアイコンなどを指定します。
-   `pytest.ini`: `pytest`フレームワークの設定ファイル。テストの実行方法や検出パターンなどを定義します。
-   `requirements-dev.txt`: 開発およびテスト時に必要なPythonパッケージのリスト。
-   `requirements.txt`: 本番環境でプロジェクトを実行するのに必要なPythonパッケージのリスト。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイル。
-   `ruff.toml`: `ruff`Linter/Formatterの設定ファイル。Pythonコードの静的解析ルールを定義します。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示すファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成機能のモジュール群を格納するパッケージ。
        -   `__init__.py`: Pythonパッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリのステータスに応じたバッジ画像を生成またはリンクするロジックを実装。
        -   `config.yml`: リポジトリ一覧生成スクリプトの技術的パラメータを設定するファイル。`project_overview`機能の設定などが含まれます。
        -   `config_manager.py`: 設定ファイル (`config.yml`, `strings.yml`など) の読み込みと管理を行うモジュール。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を実装。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIから情報を取得し、Markdownファイルを生成する処理全体を制御します。
        -   `json_ld_template.json`: SEO強化のためのJSON-LD構造化データテンプレート。
        -   `language_info.py`: リポジトリのプログラミング言語情報を処理するためのモジュール。
        -   `markdown_generator.py`: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するコアロジックを実装。
        -   `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` から概要を抽出するロジックを実装。
        -   `readme_badge_extractor.py`: READMEファイルからバッジ情報を抽出するロジックを実装。
        -   `repository_processor.py`: GitHub APIから取得した個々のリポジトリデータを処理し、表示に必要な形式に整形するロジックを実装。
        -   `seo_template.yml`: 検索エンジン最適化(SEO)に関連するメタデータやテンプレートを設定するファイル。
        -   `statistics_calculator.py`: リポジトリの星の数、フォーク数などの統計情報を計算するモジュール。
        -   `strings.yml`: 表示メッセージや文言を管理するためのファイル。
        -   `template_processor.py`: Markdown生成に使用するテンプレートの読み込みや変数置換を行うモジュール。
        -   `url_utils.py`: URLに関連するユーティリティ関数（生成、解析など）を実装。
-   `test_project_overview.py`: `project_overview_fetcher`機能の単体テストスクリプト。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   `conftest.py`: pytestのフィクスチャやヘルパー関数を定義するファイル。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テスト。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテスト。
    -   `test_config.py`: 設定ファイル読み込みのテスト。
    -   `test_date_formatter.py`: 日付フォーマット機能のテスト。
    -   `test_environment.py`: 環境設定に関するテスト。
    -   `test_integration.py`: 主要機能の統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリ情報処理機能のテスト。

## 関数詳細説明
(プロジェクト情報から具体的な関数シグネチャや実装が提供されていないため、主要なモジュールの役割に基づき、想定される代表的な関数の役割を説明します。)

-   `generate_repo_list.py`内の関数:
    -   `main()`: プログラムのエントリポイント。引数解析、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力といった一連の処理を統括します。
-   `repository_processor.py`内の関数:
    -   `process_repository(repo_data)`: GitHub APIから取得した個々のリポジトリデータを受け取り、バッジ情報の追加、プロジェクト概要の取得、統計情報の計算などを行い、出力に適した形式に整形して返します。
-   `project_overview_fetcher.py`内の関数:
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLから `generated-docs/project-overview.md` ファイルの内容を取得し、設定に基づいて「プロジェクト概要」セクションの3行説明を抽出して返します。
-   `markdown_generator.py`内の関数:
    -   `generate_markdown(repo_list_data, template_config)`: 整形されたリポジトリ情報のリストとテンプレート設定を受け取り、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成して返します。
-   `badge_generator.py`内の関数:
    -   `get_badge_url(status)`: リポジトリのステータス（例: "active", "archived"）に応じて、対応するバッジ画像のURLを生成または参照して返します。
-   `config_manager.py`内の関数:
    -   `load_config(config_path)`: 指定されたパスからYAML設定ファイルを読み込み、設定値をディクショナリまたはオブジェクトとして返します。
-   `date_formatter.py`内の関数:
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を、人間が読みやすい形式に変換して返します。
-   `template_processor.py`内の関数:
    -   `render_template(template_content, data)`: テンプレートの文字列コンテンツとデータを受け取り、テンプレート内のプレースホルダーをデータで置換し、レンダリングされた文字列を返します。
-   `url_utils.py`内の関数:
    -   `construct_repo_url(username, repo_name)`: GitHubのユーザー名とリポジトリ名から、完全なリポジトリURLを構築して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-26 07:34:25 JST
