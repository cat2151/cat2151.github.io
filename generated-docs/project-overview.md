Last updated: 2026-01-21

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにGitHub APIを使用してリポジトリ一覧を自動生成します。
- リポジトリ情報を元に、SEOに最適化されたMarkdownファイルを動的に作成します。
- 各リポジトリの概要や分類機能を付与し、検索エンジンからのサイトの可視性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータとしての利用), Markdown (生成されるコンテンツの記述形式)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール: Python (主要なスクリプト言語としてデータの取得、処理、Markdown生成に使用), pytest (テストコードの実行フレームワーク), ruff (PythonコードのLinterおよびFormatter)
- テスト: pytest (Pythonコードの単体テストおよび統合テストに使用されます)
- ビルドツール: (直接的なビルドツールは使用されていません。Pythonスクリプトがコンテンツ生成の役割を担います)
- 言語機能: Python (スクリプトの記述に利用されるプログラミング言語です)
- 自動化・CI/CD: (CI/CDパイプラインは明示されていませんが、GitHub APIによるリポジトリ情報の自動取得とMarkdown生成という形で自動化を実現しています)
- 開発標準: ruff (コードのスタイルチェックと自動修正により、コード品質と統一性を保ちます), .editorconfig (異なるエディタ間でのコードスタイルの一貫性を維持します)

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコードスタイル（インデント、改行コードなど）を強制するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
-   **`README.md`**: プロジェクトの概要、設定方法、使用方法、開発者向けのヒントなどを記述したメインのドキュメントファイルです。
-   **`_config.yml`**: Jekyllによって生成されるGitHub Pagesサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの情報を含みます。
-   **`assets/`**: Jekyllサイトで利用される静的なアセット（画像、ファビコンなど）を格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像です。
-   **`debug_project_overview.py`**: `project_overview_fetcher`機能のテストやデバッグを目的とした補助スクリプトです。
-   **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要などのドキュメントを一時的または恒久的に格納するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleによるサイトの所有権確認に使用されるHTMLファイルです。このファイルには関数は含まれていません。
-   **`index.md`**: 生成されたリポジトリ一覧が書き込まれる、GitHub PagesサイトのトップページとなるMarkdownファイルです。
-   **`issue-notes/`**: プロジェクト開発中の課題や検討事項をMarkdown形式で記録したファイル群が格納されています。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を記述するファイルです。アプリ名、アイコン、表示モードなどを定義します。
-   **`pytest.ini`**: `pytest` テストフレームワークの設定ファイルです。テストの検出ルールや実行オプションなどが定義されています。
-   **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを一覧化したファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境向けPythonパッケージとそのバージョンを一覧化したファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: `ruff` Linter/Formatterの設定ファイルです。Pythonコードの静的解析ルールや自動フォーマットに関するオプションが定義されています。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧を生成するためのロジックを含むPythonパッケージです。
        -   `__init__.py`: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
        -   `badge_generator.py`: リポジトリのステータスや特性を示すバッジ（アイコン）を生成するためのロジックを実装しています。
        -   `config.yml`: プロジェクト概要取得機能など、スクリプトの動作を制御する技術的なパラメータを定義する設定ファイルです。
        -   `config_manager.py`: `config.yml` や `strings.yml` など、プロジェクトで使用される設定ファイルを読み込み、管理する役割を担います。
        -   `date_formatter.py`: 日付や時刻を特定の形式で整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: このプロジェクトのメインスクリプトであり、GitHub APIからのリポジトリ情報取得、処理、最終的なMarkdownファイル生成の全体フローを制御します。
        -   `json_ld_template.json`: SEO（検索エンジン最適化）を強化するために、JSON-LD形式の構造化データテンプレートを定義するファイルです。
        -   `language_info.py`: リポジトリの使用言語情報を解析し、表示に適した形式に処理する機能を提供します。
        -   `markdown_generator.py`: 処理されたリポジトリ情報に基づいて、Jekyll互換のMarkdown形式のコンテンツを生成するコアロジックを実装しています。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動的に抽出する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから既存のバッジ（例: ビルドステータス、ライセンスなど）を解析し、抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出し、追加処理を適用する中心的なデータ処理ロジックを担います。
        -   `seo_template.yml`: 検索エンジン最適化のためのメタデータやその他のSEO関連のテンプレート設定を定義するファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、整形する機能を提供します。
        -   `strings.yml`: アプリケーション内で使用される表示メッセージや文言を一元的に管理するための設定ファイルです。多言語化の基盤としても利用可能です。
        -   `template_processor.py`: Jekyll/Markdownのテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成する機能を提供します。
        -   `url_utils.py`: GitHub APIエンドポイントURLの構築や、その他のURL関連のユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストケースを含むスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `test_badge_generator_integration.py`: `badge_generator.py`の統合テストを実行します。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理に関するテストを実行します。
    -   `test_date_formatter.py`: `date_formatter.py`内の日付整形関数のテストを実行します。
    -   `test_environment.py`: テスト実行環境のセットアップや依存関係に関するテストを実行します。
    -   `test_integration.py`: プロジェクトの主要な処理フロー全体をカバーする統合テストを実行します。
    -   `test_markdown_generator.py`: `markdown_generator.py`内のMarkdown生成機能のテストを実行します。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher.py`内のプロジェクト概要取得機能のテストを実行します。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor.py`内のREADMEからのバッジ抽出機能のテストを実行します。
    -   `test_repository_processor.py`: `repository_processor.py`内のリポジトリデータ処理機能のテストを実行します。

## 関数詳細説明
-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`:
        -   役割: スクリプトの主要なエントリポイント。コマンドライン引数を解析し、設定ファイルの読み込み、リポジトリ情報の取得と処理、Markdown生成、そして結果のファイル出力までの一連の流れをオーケストレートします。
        -   引数: なし (コマンドライン引数を内部で処理)
        -   戻り値: なし
-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_and_process_repositories(username, token, limit=None)`:
        -   役割: 指定されたGitHubユーザー名のリポジトリ情報をGitHub APIから取得し、整形処理を適用します。プロジェクト概要の取得、言語情報の解析などもこの処理内で呼び出されます。
        -   引数: `username` (str): GitHubユーザー名, `token` (str): GitHub APIアクセストークン, `limit` (int, オプション): 処理するリポジトリ数の上限
        -   戻り値: 処理され、整形されたリポジトリ情報のリスト (list[dict])
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_repository_list_markdown(repositories, config, strings)`:
        -   役割: 処理済みのリポジトリ情報のリストに基づいて、Jekyllと互換性のあるリポジトリ一覧のMarkdown文字列を生成します。バッジや日付のフォーマット、SEOテンプレートの適用なども含まれます。
        -   引数: `repositories` (list[dict]): 処理済みリポジトリ情報のリスト, `config` (dict): 設定情報, `strings` (dict): 表示文字列情報
        -   戻り値: 生成されたMarkdown文字列 (str)
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url, config)`:
        -   役割: 指定されたリポジトリのURLから、`config`で指定されたパスにあるプロジェクト概要ファイルを読み込み、特定のセクションから3行の説明を抽出します。
        -   引数: `repo_url` (str): リポジトリのクローンURL, `config` (dict): プロジェクト概要取得に関する設定
        -   戻り値: プロジェクト概要の3行説明のリスト (list[str]) または空のリスト
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badge_markdown(status_type, repo_name)`:
        -   役割: リポジトリのステータス（例: アクティブ、アーカイブ）やその他の情報に基づいて、表示用のバッジ（アイコン）のMarkdownコードを生成します。
        -   引数: `status_type` (str): バッジのタイプ, `repo_name` (str): リポジトリ名
        -   戻り値: バッジを表すMarkdown文字列 (str)
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(config_path)`:
        -   役割: 指定されたYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        -   引数: `config_path` (str): 設定ファイルのパス
        -   戻り値: 設定情報 (dict)
-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(datetime_obj)`:
        -   役割: 日付/時刻オブジェクトを受け取り、人間が読みやすい形式の文字列にフォーマットします。
        -   引数: `datetime_obj` (datetime.datetime): フォーマットする日付/時刻オブジェクト
        -   戻り値: フォーマットされた日付文字列 (str)
-   **`src/generate_repo_list/language_info.py`**
    -   `get_repository_languages(repo_data)`:
        -   役割: GitHub APIから取得したリポジトリデータの中から、使用されているプログラミング言語に関する情報を抽出し、整理します。
        -   引数: `repo_data` (dict): リポジトリの生データ
        -   戻り値: 主要な言語情報 (list[str] または dict)
-   **`src/generate_repo_list/readme_badge_extractor.py`**
    -   `extract_badges_from_readme(readme_content)`:
        -   役割: リポジトリのREADMEファイルの内容を解析し、Markdown形式で埋め込まれているバッジ（例：shields.ioバッジ）の情報を抽出します。
        -   引数: `readme_content` (str): READMEファイルの全文
        -   戻り値: 抽出されたバッジ情報のリスト (list[dict])
-   **`src/generate_repo_list/statistics_calculator.py`**
    -   `calculate_repo_statistics(repo_data)`:
        -   役割: リポジトリの生データからスター数、フォーク数、issue数、最終更新日などの統計情報を抽出し、必要に応じて計算または整形します。
        -   引数: `repo_data` (dict): リポジトリの生データ
        -   戻り値: 統計情報を含む辞書 (dict)
-   **`src/generate_repo_list/template_processor.py`**
    -   `process_template(template_path, data)`:
        -   役割: 指定されたテンプレートファイル（例: Markdownテンプレート）を読み込み、提供されたデータでプレースホルダーを置き換えることで、最終的なコンテンツを生成します。
        -   引数: `template_path` (str): テンプレートファイルのパス, `data` (dict): テンプレートに埋め込むデータ
        -   戻り値: 処理済みのコンテンツ文字列 (str)
-   **`src/generate_repo_list/url_utils.py`**
    -   `build_github_api_url(username)`:
        -   役割: 指定されたGitHubユーザー名に基づき、GitHub REST APIのリポジトリ一覧エンドポイントURLを構築します。
        -   引数: `username` (str): GitHubユーザー名
        -   戻り値: 構築されたAPI URL (str)

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── config_manager.load_config(config.yml)
├── config_manager.load_config(strings.yml)
├── repository_processor.fetch_and_process_repositories()
│   ├── url_utils.build_github_api_url()
│   ├── (GitHub API呼び出し)
│   ├── project_overview_fetcher.fetch_project_overview()
│   ├── language_info.get_repository_languages()
│   ├── readme_badge_extractor.extract_badges_from_readme()
│   └── statistics_calculator.calculate_repo_statistics()
└── markdown_generator.generate_repository_list_markdown()
    ├── date_formatter.format_date()
    ├── badge_generator.generate_badge_markdown()
    └── template_processor.process_template()
        └── (ファイル出力)

---
Generated at: 2026-01-21 07:08:04 JST
