Last updated: 2026-03-06

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEOを強化し、リポジトリ情報を検索エンジンに最適化して公開します。
- GitHub APIを利用してリポジトリ情報を自動取得し、Jekyll対応のMarkdownファイルを生成。
- 各リポジトリの概要表示やバッジ、分類機能で、訪問者へ魅力的にプロジェクトを紹介します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレーターで、生成されたMarkdownをHTMLに変換), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), pytest (テストフレームワーク), Ruff (コードリンターおよびフォーマッター)
- テスト: pytest (Pythonコードのテストを実行するためのフレームワーク)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py` が自動生成プロセスを管理), Jekyll (最終的なサイトを構築するGitHub Pagesの基盤)
- 言語機能: Python (GitHub APIとの連携、データ処理、ファイルI/Oに利用)
- 自動化・CI/CD: GitHub API (リポジトリ情報の取得), Pythonスクリプト (自動生成およびユーティリティ処理), GitHub Actions (将来的なCI/CD実装の可能性を示唆するファイル構造)
- 開発標準: Ruff (コードスタイルの一貫性を保つための設定ファイル `ruff.toml`), EditorConfig (異なるエディター間でのコードスタイル統一設定ファイル `.editorconfig`)

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
-   `.editorconfig`: 異なる開発環境でもコードのスタイル（インデント、改行など）を統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    -   `check_large_files/`: プロジェクト内の大容量ファイルをチェックする自動化機能に関連するファイル群です。
        -   `README.md`: `check_large_files` 機能の概要を説明するドキュメントです。
        -   `check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルです。
        -   `scripts/check_large_files.py`: 大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitでバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
-   `LICENSE`: 本プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの目的、機能、使用方法など、プロジェクト全体の概要を説明するメインドキュメントです。
-   `_config.yml`: Jekyllサイト（GitHub Pages）の全体設定を定義するファイルです。
-   `assets/`: サイトで使用する画像やアイコンなどの静的ファイルを格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブに表示されるアイコン）画像ファイル群です。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
-   `generated-docs/`: プロジェクトによって自動生成されたドキュメントやファイルを格納するためのディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleでのサイト所有権確認に使用されるHTML認証ファイルです。
-   `index.md`: メインのGitHubリポジトリ一覧が自動生成されるMarkdownファイルです。GitHub Pagesで公開されます。
-   `issue-notes/`: 開発中の課題やメモを管理するためのディレクトリです。
    -   `22.md`: 特定の課題（例: Issue #22）に関する詳細なメモや考察が記述されたファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）としてサイトを定義するための設定ファイルです。
-   `pytest.ini`: Pythonのテストフレームワーク `pytest` の設定ファイルです。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonライブラリのリストです。
-   `requirements.txt`: 本番環境（このスクリプトの実行環境）で必要となるPythonライブラリのリストです。
-   `robots.txt`: 検索エンジンクローラーに対して、ウェブサイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
-   `ruff.toml`: Pythonコードのリンティングおよびフォーマットツール `Ruff` の設定ファイルです。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリ一覧を生成する主要なロジックが格納されているサブディレクトリです。
        -   `__init__.py`: `generate_repo_list` がPythonサブパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのステータスバッジ（例: ビルド成功、ライセンス情報）を生成または管理するロジックを提供します。
        -   `config.yml`: リポジトリ一覧生成スクリプトの実行パラメータや機能を設定するファイルです。
        -   `config_manager.py`: `config.yml` や外部の秘密情報ファイル（例: `secrets.toml`）を読み込み、管理するモジュールです。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownを生成します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のためのJSON-LD形式のメタデータテンプレートです。
        -   `language_info.py`: リポジトリの主要言語情報やその割合などを処理するロジックを提供します。
        -   `markdown_generator.py`: 取得・処理されたリポジトリ情報をもとに、GitHub Pages用のMarkdownコンテンツを生成するモジュールです。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `project-overview.md`）から、プロジェクトの3行概要を抽出する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、プロジェクトに設定されているバッジ情報を抽出するモジュールです。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報に加工するモジュールです。
        -   `seo_template.yml`: 検索エンジン最適化（SEO）に関連するテンプレートやメタデータの定義を格納するファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        -   `strings.yml`: UIに表示される各種メッセージや文言を一元管理するための設定ファイルです。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレートファイルの内容を読み込み、データに基づいてレンダリングする機能を提供します。
        -   `url_utils.py`: GitHub APIエンドポイントやリポジトリURLの構築など、URLに関連するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールのテストケースを記述したスクリプトです。
-   `tests/`: プロジェクト全体のテストコードが格納されているディレクトリです。
    -   `test_badge_generator_integration.py`: `badge_generator` モジュールの統合テストを行うスクリプトです。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストを行うスクリプトです。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みと解析に関するテストを行うスクリプトです。
    -   `test_date_formatter.py`: 日付フォーマットユーティリティのテストを行うスクリプトです。
    -   `test_environment.py`: 実行環境のセットアップや依存関係に関するテストを行うスクリプトです。
    -   `test_integration.py`: システム全体の主要機能に関する統合テストを行うスクリプトです。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテストを行うスクリプトです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを行うスクリプトです。
    -   `test_readme_badge_extractor.py`: `README.md`からのバッジ抽出機能のテストを行うスクリプトです。
    -   `test_repository_processor.py`: リポジトリデータ処理ロジックのテストを行うスクリプトです。

## 関数詳細説明
このプロジェクトは複数のPythonスクリプトから構成されており、それぞれが特定の役割を担っています。主要な関数とその役割は以下の通りです。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`: スクリプトの実行開始点。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データの処理、Markdownファイルの生成、そして結果の出力を行います。
    -   `parse_arguments()`: コマンドラインから渡される引数（ユーザー名、出力ファイル名、リポジトリ数制限など）を解析し、スクリプトが利用できる形式に変換します。

-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_repositories(username)`: 指定されたGitHubユーザー名に基づき、GitHub APIを通じてそのユーザーが所有するすべてのリポジトリの情報を取得します。
    -   `process_repository_data(repo_list)`: 取得した生のリポジトリデータを受け取り、表示に必要な情報（アクティブ/アーカイブ/フォークの分類、スター数、最終更新日など）に整形およびフィルタリングを行います。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown(processed_repos)`: 処理済みのリポジトリ情報リストを基に、最終的にGitHub Pagesに表示されるMarkdown形式のコンテンツを生成します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `get_project_overview(repo_name, owner, config)`: 特定のリポジトリ（`repo_name`と`owner`で指定）から、設定ファイルで指定されたパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要を読み込み、3行の要約を抽出します。

-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(path)`: 指定されたパスにある設定ファイル（例: `config.yml`）を読み込み、プログラム内で利用可能なデータ構造に変換します。
    -   `load_secrets(path)`: 指定されたパスにある機密情報ファイル（例: GitHubトークンを含む`secrets.toml`）を安全に読み込みます。

-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badge(data)`: リポジトリの言語やライセンスなどの情報に基づき、表示用のバッジ（例: Shields.io形式のSVG画像URL）を生成します。

-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(date_string)`: 日付文字列を受け取り、ユーザーフレンドリーな形式（例: "YYYY年MM月DD日"）に整形します。

-   **`src/generate_repo_list/url_utils.py`**
    -   `build_github_api_url(endpoint)`: GitHub APIのベースURLと指定されたエンドポイントを組み合わせて、APIリクエスト用の完全なURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-06 07:10:12 JST
