Last updated: 2026-11-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をマークダウンで自動生成します。
- これにより、リポジトリの検索エンジンへのインデックスを促進し、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll / GitHub Pages** (生成されたMarkdownを表示する静的サイトジェネレータ)、**Markdown** (コンテンツの記述形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **GitHub API** (リポジトリ情報の取得に使用)、**Git** (バージョン管理)、**GitHub CLI** (ローカルからのGitHub操作に利用される可能性)
- テスト: **pytest** (Pythonコードのテストフレームワーク)
- ビルドツール: **Python** (スクリプト自体が生成プロセスを担う)、**PyYAML** (設定ファイルや文言管理ファイル `config.yml`, `strings.yml` のパースに使用)
- 言語機能: **Python** (プロジェクトの主要な実装言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリが存在するため、自動化ワークフローで使用される可能性が高い)
- 開発標準: **ruff** (Pythonコードの高速なLinterおよびFormatter)、**.editorconfig** (IDEやエディタ間でのコーディングスタイル統一)

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
-   **.editorconfig**: プロジェクト全体でコードのインデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関連するファイルを格納するディレクトリです。
    -   **check_large_files/**: 大容量ファイルのチェックに関連するスクリプトや設定を格納します。
        -   **README.md**: `check_large_files` 機能の説明文書です。
        -   **check-large-files.toml**: 大容量ファイルチェックの設定を記述します。
        -   **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
-   **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **README.md**: プロジェクトの概要、目的、使い方など、プロジェクトに関する包括的な情報を提供するメインの説明文書です。
-   **_config.yml**: Jekyllのサイト設定ファイルです。GitHub Pagesの振る舞いを定義します。
-   **assets/**: サイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    -   **favicon-*.png**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）ファイルです。
-   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
-   **generated-docs/**: 各リポジトリから取得した概要などのドキュメントが、自動生成されて格納されることを想定したディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権を確認するための認証ファイルです。
-   **index.md**: 生成されたリポジトリ一覧が書き込まれるデフォルトの出力ファイル、またはGitHub PagesのトップページとなるMarkdownファイルです。
-   **issue-notes/**: 開発中の課題やメモを記録するためのディレクトリです。
    -   **22.md**: 特定の課題（例: Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
-   **manifest.json**: Progressive Web App (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの機能を提供します。
-   **pytest.ini**: pytestの実行設定を定義するファイルです。テストの発見方法やプラグインなどが設定されます。
-   **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を記述するファイルです。
-   **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係を記述するファイルです。
-   **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスするかを指示するファイルです。
-   **ruff.toml**: PythonコードのLinterおよびFormatterであるRuffの設定ファイルです。コード規約や自動修正ルールを定義します。
-   **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   **__init__.py**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    -   **generate_repo_list/**: リポジトリ一覧生成のメインロジックを格納するPythonパッケージです。
        -   **__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
        -   **badge_generator.py**: リポジトリに表示するバッジ（例: 言語、ライセンスなど）のMarkdownを生成するロジックを含みます。
        -   **config.yml**: プロジェクト概要取得機能などの技術的な設定パラメータを定義するYAMLファイルです。
        -   **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するクラスや関数を提供します。
        -   **date_formatter.py**: 日付情報を整形して表示するためのユーティリティ関数を提供します。
        -   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインのエントリーポイントスクリプトです。
        -   **json_ld_template.json**: 検索エンジン最適化(SEO)のためのJSON-LD形式の構造化データテンプレートです。
        -   **language_info.py**: リポジトリの主要言語情報などを処理・整形するロジックを提供します。
        -   **markdown_generator.py**: 取得したリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを含みます。
        -   **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得するロジックを提供します。
        -   **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するロジックを含みます。
        -   **repository_processor.py**: GitHub APIを介してリポジトリ情報を取得し、後続の処理のためにデータを加工・整形する主要なロジックを提供します。
        -   **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **statistics_calculator.py**: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するロジックを提供します。
        -   **strings.yml**: プロジェクト内で使用される表示メッセージや文言を管理するためのYAMLファイルです。多言語対応や文言変更の際に利用されます。
        -   **template_processor.py**: Markdown生成に使用されるテンプレート（Jinja2など）の処理を担うロジックを提供します。
        -   **url_utils.py**: GitHubリポジトリのURLやGitHub PagesのURLなどを生成・処理するユーティリティ関数を提供します。
-   **test_project_overview.py**: `project_overview_fetcher.py` の機能に関する単体テストまたは結合テストを行うスクリプトです。
-   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **conftest.py**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    -   **test_badge_generator_integration.py**: `badge_generator.py` の統合テストを行うスクリプトです。
    -   **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py` のテストを行うスクリプトです。
    -   **test_config.py**: 設定ファイルの読み込みや管理に関するテストを行うスクリプトです。
    -   **test_date_formatter.py**: `date_formatter.py` の日付整形機能に関するテストを行うスクリプトです。
    -   **test_environment.py**: 実行環境に関する設定や依存関係のテストを行うスクリプトです。
    -   **test_integration.py**: プロジェクトの主要な複数のコンポーネントが連携して正しく動作するかを確認する統合テストを行うスクリプトです。
    -   **test_markdown_generator.py**: `markdown_generator.py` のMarkdown生成機能に関するテストを行うスクリプトです。
    -   **test_project_overview_fetcher.py**: `project_overview_fetcher.py` の機能に関するテストを行うスクリプトです。
    -   **test_readme_badge_extractor.py**: `readme_badge_extractor.py` のREADMEからのバッジ抽出機能に関するテストを行うスクリプトです。
    -   **test_repository_processor.py**: `repository_processor.py` のリポジトリ情報処理機能に関するテストを行うスクリプトです。

## 関数詳細説明
-   **generate_repo_list.py**:
    -   `main()`: エントリーポイント関数。コマンドライン引数をパースし、リポジトリ情報の取得、加工、Markdown生成のプロセス全体を調整します。
        -   引数: なし (コマンドライン引数は内部で処理)
        -   戻り値: None
        -   機能: プログラムの実行フローを制御し、必要なモジュールを呼び出してリポジトリ一覧を生成します。
    -   `parse_arguments()`: コマンドライン引数をパースするための関数。
        -   引数: なし
        -   戻り値: `argparse.Namespace`オブジェクト（パースされた引数）
        -   機能: `--username`, `--output`, `--limit`などの引数を定義し、ユーザーからの入力を受け取ります。
-   **config_manager.py**:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込みます。
        -   引数: `config_path` (str) - 設定ファイルのパス。
        -   戻り値: dict (設定内容)
        -   機能: プロジェクトの動的な設定（例: プロジェクト概要取得機能の有効/無効、タイムアウト値）を提供します。
    -   `load_strings(strings_path)`: 指定されたパスからYAML形式の文言ファイルを読み込みます。
        -   引数: `strings_path` (str) - 文言ファイルのパス。
        -   戻り値: dict (文言内容)
        -   機能: サイトに表示されるテキストメッセージやラベルを集中管理します。
-   **repository_processor.py**:
    -   `fetch_repositories(username, token, limit=None)`: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。
        -   引数: `username` (str), `token` (str), `limit` (int, optional)
        -   戻り値: list[dict] (取得したリポジトリデータのリスト)
        -   機能: GitHub APIとの認証と通信を行い、リポジトリの詳細情報を取得します。
    -   `process_repository_data(repo_data, config)`: 取得した個々のリポジトリデータを処理し、表示に必要な形に整形します。
        -   引数: `repo_data` (dict), `config` (dict)
        -   戻り値: dict (整形されたリポジトリデータ)
        -   機能: プロジェクト概要の取得、バッジの抽出、言語情報の加工など、各リポジトリに特有の処理を実行します。
-   **project_overview_fetcher.py**:
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリの特定のパスからプロジェクト概要のMarkdownを抽出し、3行の要約を返します。
        -   引数: `repo_url` (str), `config` (dict)
        -   戻り値: list[str] (3行の概要説明) または None
        -   機能: リポジトリ内の特定のファイルコンテンツを解析し、指定されたセクションからプロジェクトの簡潔な説明を抽出します。
-   **readme_badge_extractor.py**:
    -   `extract_badges(readme_content)`: READMEの内容からバッジのURLやAltテキストを抽出します。
        -   引数: `readme_content` (str)
        -   戻り値: list[dict] (抽出されたバッジ情報のリスト)
        -   機能: 正規表現などを用いて、Markdown形式のバッジ記述を識別し、その情報を構造化します。
-   **markdown_generator.py**:
    -   `generate_markdown(processed_repos, strings, config)`: 処理済みのリポジトリデータと文言、設定情報を用いて最終的なMarkdownコンテンツを生成します。
        -   引数: `processed_repos` (list[dict]), `strings` (dict), `config` (dict)
        -   戻り値: str (生成されたMarkdownテキスト)
        -   機能: テンプレートエンジンやユーティリティ関数を呼び出し、リポジトリ一覧ページのHTML構造をMarkdownで構築します。
-   **badge_generator.py**:
    -   `generate_badge_markdown(badge_data)`: バッジデータに基づいてMarkdown形式のバッジ画像を生成します。
        -   引数: `badge_data` (dict)
        -   戻り値: str (バッジのMarkdown文字列)
        -   機能: 各リポジトリの言語やステータスを示すバッジをHTML/Markdown形式でレンダリングします。
-   **date_formatter.py**:
    -   `format_date(iso_date_string)`: ISO形式の日付文字列を人間が読みやすい形式に整形します。
        -   引数: `iso_date_string` (str)
        -   戻り値: str (整形された日付文字列)
        -   機能: GitHub APIから取得される日付データを、ユーザーフレンドリーな形式（例: "2023年10月27日"）に変換します。
-   **statistics_calculator.py**:
    -   `calculate_statistics(repo_list)`: リポジトリのリストからスター数の合計などの統計情報を計算します。
        -   引数: `repo_list` (list[dict])
        -   戻り値: dict (計算された統計情報)
        -   機能: サイトフッターなどに表示する、全リポジトリの累積的な情報を集計します。
-   **template_processor.py**:
    -   `render_template(template_name, context)`: 指定されたテンプレートファイルにコンテキストデータを適用し、レンダリング結果を返します。
        -   引数: `template_name` (str), `context` (dict)
        -   戻り値: str (レンダリングされた文字列)
        -   機能: Markdown生成時に、Jinja2などのテンプレートエンジンを利用して動的なコンテンツを埋め込みます。
-   **url_utils.py**:
    -   `construct_repo_url(username, repo_name)`: GitHubリポジトリのURLを構築します。
        -   引数: `username` (str), `repo_name` (str)
        -   戻り値: str (リポジトリのURL)
        -   機能: `https://github.com/<username>/<repo_name>`形式のURLを生成します。

## 関数呼び出し階層ツリー
```
main (generate_repo_list.py)
├── parse_arguments()
├── load_config (config_manager.py)
├── load_strings (config_manager.py)
├── fetch_repositories (repository_processor.py)
│   └── (GitHub APIへのHTTPリクエスト)
├── process_repository_data (repository_processor.py)
│   ├── fetch_project_overview (project_overview_fetcher.py)
│   │   └── (リポジトリコンテンツ取得APIまたはHTTPリクエスト)
│   ├── extract_badges (readme_badge_extractor.py)
│   ├── (language_info.py の関数 - 推測)
│   └── (statistics_calculator.py の関数 - 推測、個別の統計計算)
├── calculate_statistics (statistics_calculator.py)
├── generate_markdown (markdown_generator.py)
│   ├── render_template (template_processor.py)
│   ├── generate_badge_markdown (badge_generator.py)
│   ├── format_date (date_formatter.py)
│   └── construct_repo_url (url_utils.py)
└── (出力ファイルへの書き込み)

---
Generated at: 2026-11-13 07:07:38 JST
