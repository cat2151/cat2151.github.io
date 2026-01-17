Last updated: 2026-01-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定されたユーザーの全リポジトリ情報を自動で取得します。
- 取得した情報に基づき、GitHub Pages向けのSEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- これにより、リポジトリの検索エンジンへの露出を高め、LLMなどからの参照成功率を向上させることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages): 静的サイトジェネレーターであるJekyllを利用し、生成されたMarkdownファイルをGitHub Pagesサイトとして公開します。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python: プロジェクトの主要なロジックがPythonで記述されており、GitHub APIとの連携やMarkdown生成を行います。
- テスト: pytest: Pythonコードの単体テストおよび結合テストを行うためのフレームワークです。
- ビルドツール: Pythonスクリプト: GitHub APIからデータを取得し、Jekyllで利用可能なMarkdown形式のファイルを生成する中心的な役割を担います。
- 言語機能: Python: プロジェクトのロジック実装に使用される主要なプログラミング言語です。
- 自動化・CI/CD: GitHub API: リポジトリ情報の自動取得に利用され、このシステムの主要な自動化機能を支えています。
- 開発標準: ruff: Pythonコードのスタイルチェックとフォーマットを自動で行い、コード品質と一貫性を保つためのツールです。また、`.editorconfig`ファイルでコードスタイルの統一ルールを定義しています。

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  18.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_badge_generator_integration.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
-   **README.md**: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、プロジェクト全体の概要と開発者向けヒントをまとめた主要なドキュメントファイルです。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を強制するための設定ファイルです。
-   **.gitignore**: Gitが追跡すべきでないファイルやディレクトリ（一時ファイル、ビルド成果物など）を指定するファイルです。
-   **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの挙動に影響を与えます。
-   **assets/**: GitHub Pagesサイトで使用されるファビコンなどの静的アセットファイルを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
-   **debug_project_overview.py**: `project_overview`機能のデバッグやテストに使用されるスクリプトです。
-   **generated-docs/**: 各リポジトリから取得された `project-overview.md` のようなドキュメントを一時的に格納、または参照する場所として想定されます。
-   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認に使用されるファイルです。
-   **index.md**: `generate_repo_list.py`スクリプトによって生成される主要なMarkdownファイルで、GitHub Pagesサイトのリポジトリ一覧ページの内容となります。
-   **issue-notes/**: プロジェクト開発中に発生した課題やそのメモを記録するMarkdownファイルを格納するディレクトリです。
-   **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（アイコン、表示モードなど）を定義するファイルです。
-   **pytest.ini**: `pytest`テストフレームワークの動作設定を定義するファイルです。
-   **requirements.txt**: プロジェクトが本番環境で実行するために必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
-   **requirements-dev.txt**: 開発時やテスト実行時に必要な追加のPythonパッケージをリストアップしたファイルです。
-   **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
-   **ruff.toml**: Pythonコードのリント（静的解析）とフォーマットを行う`ruff`ツールの設定ファイルです。
-   **src/**: プロジェクトのソースコードを格納する主要なディレクトリです。
    -   `generate_repo_list/`: リポジトリ一覧生成システムのコアロジックを格納するパッケージです。
        -   `__init__.py`: Pythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリに表示するバッジ（例：言語、ステータス）を生成するロジックを実装しています。
        -   `config.yml`: `project_overview`機能などの技術的パラメータを定義する設定ファイルです。
        -   `config_manager.py`: YAML形式の設定ファイルを読み込み、管理するためのモジュールです。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
        -   `json_ld_template.json`: SEO強化のため、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        -   `language_info.py`: リポジトリの使用言語に関する情報を処理、整形するモジュールです。
        -   `markdown_generator.py`: 取得・処理されたリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを実装しています。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEからバッジ情報を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した個々のリポジトリデータを整形し、必要な情報を抽出するためのロジックを実装しています。
        -   `seo_template.yml`: SEO関連のメタデータや設定を定義するテンプレートファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算するモジュールです。
        -   `strings.yml`: UIに表示されるメッセージや文言（多言語対応の可能性も含む）を管理する設定ファイルです。
        -   `template_processor.py`: Markdown生成の際にテンプレートを処理するためのモジュールです。
        -   `url_utils.py`: URLの構築や解析に関するユーティリティ関数を提供します。
-   **test_project_overview.py**: `project_overview_fetcher`機能のテストを行うスクリプトです。
-   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。

## 関数詳細説明
-   **`generate_repo_list.py` 内の `main()` 関数**:
    -   役割: プロジェクトのエントリポイント。GitHub APIからリポジトリ情報を取得し、各リポジトリを処理し、最終的なMarkdownファイルを生成する一連の処理を調整します。
    -   引数: `username` (str): GitHubユーザー名, `output` (str): 出力ファイル名, `limit` (int, オプション): 処理するリポジトリ数の上限。
    -   戻り値: なし (サイドエフェクトとしてファイルを出力します)。
-   **`config_manager.py` 内の `load_config(filepath)` 関数**:
    -   役割: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
    -   引数: `filepath` (str): 読み込む設定ファイルのパス。
    -   戻り値: `dict`: 設定ファイルの内容を辞書形式で返します。
-   **`project_overview_fetcher.py` 内の `fetch_project_overview(repo_url, config)` 関数**:
    -   役割: 指定されたリポジトリのURLから、`config.yml`で定義されたパスにある `project-overview.md` ファイルを読み込み、指定されたセクション（例: "プロジェクト概要"）から3行の要約を抽出します。
    -   引数: `repo_url` (str): 対象リポジトリのGitHub URL, `config` (dict): プロジェクト概要取得機能に関する設定。
    -   戻り値: `list[str]` または `None`: 抽出された3行の概要のリスト、または取得できなかった場合は `None`。
-   **`repository_processor.py` 内の `process_repository(repo_info, config, github_token)` 関数**:
    -   役割: GitHub APIから取得した個々のリポジトリの生データを整形し、表示に必要な情報（名前、説明、言語、スター数、プロジェクト概要など）を抽出・加工します。
    -   引数: `repo_info` (dict): GitHub APIから取得した単一リポジトリの生データ, `config` (dict): 全体設定, `github_token` (str): GitHub API認証トークン。
    -   戻り値: `dict`: 整形され、表示可能な形式に変換されたリポジトリ情報。
-   **`markdown_generator.py` 内の `generate_markdown(repos_data, strings_config, seo_template)` 関数**:
    -   役割: 複数の処理済みリポジトリデータと、表示用の文字列設定、SEOテンプレートを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   引数: `repos_data` (list[dict]): 処理済みリポジトリデータのリスト, `strings_config` (dict): 表示メッセージ設定, `seo_template` (dict): SEOテンプレート設定。
    -   戻り値: `str`: 生成されたMarkdown形式の文字列。
-   **`badge_generator.py` 内の `generate_badge(badge_text, badge_color)` 関数**:
    -   役割: 指定されたテキストと色でMarkdown形式のバッジ文字列を生成します。
    -   引数: `badge_text` (str): バッジに表示するテキスト, `badge_color` (str): バッジの色（例: "blue", "green"）。
    -   戻り値: `str`: 生成されたMarkdown形式のバッジ文字列。
-   **`url_utils.py` 内の `build_github_api_url(username)` 関数**:
    -   役割: 指定されたGitHubユーザー名に基づき、GitHub APIのエンドポイントURLを構築します。
    -   引数: `username` (str): GitHubユーザー名。
    -   戻り値: `str`: 構築されたGitHub APIのURL。
-   **`date_formatter.py` 内の `format_date(iso_date_string)` 関数**:
    -   役割: ISO 8601形式の日付文字列を、人間が読みやすい形式に変換します。
    -   引数: `iso_date_string` (str): ISO 8601形式の日付文字列。
    -   戻り値: `str`: 整形された日付文字列。

## 関数呼び出し階層ツリー
```
提供された情報から関数呼び出し階層ツリーを分析できませんでした。

---
Generated at: 2026-01-18 07:06:09 JST
