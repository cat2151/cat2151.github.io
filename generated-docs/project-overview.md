Last updated: 2026-09-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、JekyllベースのGitHub Pages向けにリポジトリ一覧を自動生成します。
- SEO最適化、バッジ表示、分類機能により、リポジトリ情報の発見性を高めます。
- 各リポジトリの概要を自動取得し、動的で魅力的な一覧ページを提供します。

## 技術スタック
- フロントエンド: **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトはJekyllサイト用のMarkdownファイルを生成します。
- 開発言語: **Python**: リポジトリ情報の取得、処理、Markdown生成の主要なスクリプト言語として使用されています。
- API連携: **GitHub API**: GitHubリポジトリの情報をプログラムで取得するために利用されます。
- 設定・データフォーマット:
    - **YAML**: プロジェクトの各種設定（`config.yml`、`seo_template.yml`）や表示メッセージ（`strings.yml`）の記述に用いられます。
    - **TOML**: GitHubトークンなどの秘密情報や、`ruff`の設定（`ruff.toml`）に利用されます。
    - **Markdown**: GitHub Pagesサイトのコンテンツ（リポジトリ一覧など）を生成するための出力フォーマットです。
    - **JSON-LD**: SEOメタデータの一部として利用される構造化データフォーマットです。
- テスト: **pytest**: Pythonコードの単体テストおよび統合テストフレームワークとして利用され、コードの品質と信頼性を保証します。
- コード品質: **ruff**: Pythonコードのリンターおよびフォーマッターとして使用され、コードスタイルの一貫性と品質を自動的に維持します。

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
-   **`.editorconfig`**: 異なるエディタ間でのコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルのチェックに関する自動化スクリプトを格納します。
        -   **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
        -   **`check-large-files.toml`**: 大容量ファイルチェック機能の設定（例: サイズ上限、除外パターン）を定義します。
        -   **`scripts/check_large_files.py`**: 指定されたリポジトリ内の大容量ファイルを検出し、報告するPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、設定方法、実行コマンド、開発者向けのヒントなど、プロジェクトに関する最も重要な情報を提供するメインドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の共通設定ファイル。GitHub Pagesの基本的な挙動やテーマ設定などを定義します。
-   **`assets/`**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: 異なるサイズで提供されるファビコン（サイトアイコン）の画像ファイルです。
-   **`debug_project_overview.py`**: `project_overview` 機能（各リポジトリから概要を自動取得する機能）のデバッグや単体テストに使用されるスクリプトです。
-   **`generated-docs/`**: 本プロジェクトによって生成されたドキュメントや、他リポジトリから取得されたドキュメントを一時的に格納するためのディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイルです。
-   **`index.md`**: GitHub Pagesサイトのメインページ（トップページ）となるMarkdownファイルです。本プロジェクトで生成されるリポジトリ一覧のコンテンツが出力されることが想定されます。
-   **`issue-notes/`**: 課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモや検討内容を記述したMarkdownファイルです。
-   **`manifest.json`**: Web App Manifestファイル。プログレッシブウェブアプリ（PWA）のインストール情報や表示設定（アプリ名、アイコンなど）を定義します。
-   **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テスト実行時のオプションやパスなどを指定します。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンターおよびフォーマッターである `ruff` の設定ファイルです。コードスタイルのルールなどを定義します。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
    -   **`generate_repo_list/`**: リポジトリ一覧生成機能の主要モジュールを格納するパッケージです。
        -   **`__init__.py`**: Pythonパッケージであることを示すファイル。
        -   **`badge_generator.py`**: リポジトリのステータス（例: アクティブ、アーカイブ）や技術スタックを示すバッジの生成に関連するロジックを扱います。
        -   **`config.yml`**: `generate_repo_list` スクリプトの実行時設定（例: GitHub APIのタイムアウト、キャッシュ設定、プロジェクト概要取得設定）を定義するファイルです。
        -   **`config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、管理するためのユーティリティ関数を提供します。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数（例: `YYYY-MM-DD` 形式への変換）を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプトです。GitHub APIからリポジトリ情報を取得し、加工・整形してMarkdownファイルを生成する一連の処理を統括します。
        -   **`json_ld_template.json`**: JSON-LD形式のSEOメタデータテンプレート。構造化データとしてリポジトリ情報を記述する際に使用されます。
        -   **`language_info.py`**: リポジトリの主要言語情報を取得・処理するためのロジックを扱います。
        -   **`markdown_generator.py`**: 取得・加工されたリポジトリ情報から、SEOを意識したMarkdown形式のコンテンツを生成するモジュールです。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要（3行説明）を自動取得する機能を担当します。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出するロジックを扱います。
        -   **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを受け取り、表示に必要な情報（整形された日付、バッジ情報、概要など）に加工・整形するモジュールです。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータテンプレートや設定を定義するYAMLファイルです。
        -   **`statistics_calculator.py`**: リポジトリに関連する統計情報（スター数、フォーク数、最終更新日など）を計算または集計するモジュールです。
        -   **`strings.yml`**: UIに表示される各種メッセージ、ラベル、文言などを管理するYAMLファイルです。多言語対応や文言の一元管理に利用されます。
        -   **`template_processor.py`**: Markdown生成時に利用されるテンプレート処理ロジック（プレースホルダーの置換など）を扱います。
        -   **`url_utils.py`**: URLの操作や生成に関するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テスト用スクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義するファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator` モジュールの統合テストです。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    -   **`test_config.py`**: 設定ファイルの読み込み・管理機能のテストです。
    -   **`test_date_formatter.py`**: 日付整形機能のテストです。
    -   **`test_environment.py`**: 実行環境に関するテストです。
    -   **`test_integration.py`**: プロジェクト全体の主要な統合テストです。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    -   **`test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能のテストです。
    -   **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
（提供されたプロジェクト情報から、具体的な関数シグネチャやコードが特定できないため、主要なファイルから推測される中心的な関数の役割と機能を説明します。）

-   **`main` (in `src/generate_repo_list/generate_repo_list.py`)**:
    -   **役割**: プロジェクト全体の処理フローを制御するメインエントリーポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、各リポジトリの加工、Markdownコンテンツ生成、および最終的なファイル出力の一連のプロセスを統括します。
    -   **引数**: `username` (str): GitHubユーザー名, `output_file` (str): 出力ファイルパス, `limit` (int, optional): 処理するリポジトリ数の上限（開発用）。
    -   **戻り値**: なし（ファイルの書き出しが主な副作用）。
    -   **機能**: 設定の読み込み、GitHub APIクライアントの初期化、リポジトリデータの取得、各リポジトリ情報の処理と整形、Markdown形式でのコンテンツ生成、指定されたファイルへの書き出し。

-   **`get_repositories_from_github` (in `src/generate_repo_list/repository_processor.py` または関連モジュール)**:
    -   **役割**: 指定されたGitHubユーザーのリポジトリ一覧をGitHub APIを介して取得します。
    -   **引数**: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIアクセストークン。
    -   **戻り値**: GitHubから取得したリポジトリ情報（辞書のリスト）。
    -   **機能**: GitHub APIへのHTTPリクエストの構築と送信、レスポンスデータのJSONパース、エラーハンドリング。

-   **`process_single_repository` (in `src/generate_repo_list/repository_processor.py`)**:
    -   **役割**: 個々のリポジトリの生データを受け取り、出力に必要な情報（整形された日付、言語、バッジ、概要など）に加工・整形します。
    -   **引数**: `repo_data` (dict): 単一リポジトリの生のAPIデータ, `config` (dict): プロジェクト設定。
    -   **戻り値**: 表示用に整形されたリポジトリ情報（辞書）。
    -   **機能**: 日付フォーマットの適用、プロジェクト概要の取得、言語情報の抽出、バッジデータの生成または抽出。

-   **`generate_markdown_content` (in `src/generate_repo_list/markdown_generator.py`)**:
    -   **役割**: 処理され整形されたリポジトリ情報のリストを受け取り、GitHub Pagesサイト用のSEO最適化されたMarkdown形式のコンテンツを生成します。
    -   **引数**: `repositories` (list of dict): 整形済みリポジトリ情報のリスト, `strings` (dict): 表示に用いる文言データ。
    -   **戻り値**: 生成されたMarkdownコンテンツの文字列。
    -   **機能**: テンプレートへのデータの適用、各リポジトリの情報のループ処理と整形、SEOメタデータ（JSON-LDなど）の埋め込み。

-   **`fetch_project_overview_from_repo` (in `src/generate_repo_list/project_overview_fetcher.py`)**:
    -   **役割**: 各リポジトリ内の指定されたファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要（通常3行の説明）を抽出します。
    -   **引数**: `repo_full_name` (str): リポジトリのフルネーム (例: `user/repo`), `config` (dict): プロジェクト設定, `github_token` (str): GitHub APIアクセストークン。
    -   **戻り値**: 抽出されたプロジェクト概要の文字列、または概要が見つからない場合はNone。
    -   **機能**: GitHub APIを介したファイルコンテンツの取得、Markdownコンテンツのパース、指定されたセクションからの情報抽出、キャッシュ処理。

-   **`load_configuration` (in `src/generate_repo_list/config_manager.py`)**:
    -   **役割**: 指定されたYAMLファイルから設定情報を読み込み、Pythonの辞書形式で提供します。
    -   **引数**: `file_path` (str): 設定ファイルのパス。
    -   **戻り値**: 読み込まれた設定データ（辞書）。
    -   **機能**: YAMLファイルのオープンとパース、設定のバリデーション（オプション）。

-   **`format_iso_date` (in `src/generate_repo_list/date_formatter.py`)**:
    -   **役割**: ISO 8601形式などの日付文字列を受け取り、指定されたユーザーフレンドリーな形式に整形します。
    -   **引数**: `iso_date_string` (str): ISO 8601形式の日付文字列, `output_format` (str): 整形後の日付フォーマット文字列。
    -   **戻り値**: 整形された日付文字列。
    -   **機能**: 日付文字列のパース、日付オブジェクトへの変換、指定フォーマットでの出力。

## 関数呼び出し階層ツリー
```
（提供された情報では関数呼び出し階層の分析ができませんでした。）

---
Generated at: 2026-09-04 07:21:00 JST
