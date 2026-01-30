Last updated: 2026-01-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動的に取得・整理するシステムです。
- 取得した情報からJekyllベースのGitHub Pagesサイト向けにMarkdownファイル群を生成します。
- GitHub Pagesを通じてリポジトリ一覧や個別のリポジトリページを公開し、SEOとLLMの参照性を向上させることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として、生成されたMarkdownファイルをレンダリングするために使用されます。本プロジェクトはMarkdownを生成する側です。), Markdown (自動生成されるコンテンツの形式であり、静的サイトの記述に用いられます。)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成に利用されます。), Git (バージョン管理システム。GitHub APIを通じてリポジトリ情報の取得に間接的に利用されます。), GitHub API (GitHubリポジトリの情報をプログラム的に取得するために使用されます。)
- テスト: pytest (Pythonコードのユニットテストおよび統合テストフレームワークとして利用され、コードの品質と信頼性を確保します。)
- ビルドツール: 該当なし (GitHub PagesのJekyllがこれに相当しますが、本プロジェクト自体は直接ビルドを行いません。)
- 言語機能: Python (汎用プログラミング言語。データ処理、API通信、ファイル操作など、システムの中核的なロジックを実装するために使用されます。)
- 自動化・CI/CD: GitHub Actions (README内で共通化されたワークフローに言及があり、このシステムが生成するMarkdownは、GitHub ActionsによってデプロイされるGitHub Pages上で利用されることを想定しています。)
- 開発標準: ruff (Pythonコードのリンターおよびフォーマッターとして利用され、コードスタイルの一貫性を保ち、品質を向上させます。)

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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   `.gitignore`: Gitによってバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
-   `LICENSE`: プロジェクトのソフトウェアライセンス（MITライセンス）情報が記載されたファイル。
-   `README.md`: プロジェクトの概要、目的、機能、利用方法、設定手順などを説明するメインのドキュメント。
-   `_config.yml`: Jekyllサイト全体の設定を定義するファイル。GitHub Pagesの振る舞いやサイトのメタデータを制御します。
-   `assets/`: GitHub Pagesサイトで使用される静的リソース（例: ファビコン画像）を格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ウェブサイトのアイコン）の各サイズ。
-   `debug_project_overview.py`: `project_overview` 機能の動作確認やデバッグを目的としたPythonスクリプト。
-   `generated-docs/`: 他のリポジトリからプロジェクト概要を読み込む際に、その概要ファイルが存在すると想定されるディレクトリ名。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置されるファイル。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される主要なMarkdownファイル。GitHub Pagesのトップページとしてリポジトリ一覧が表示されます。
-   `issue-notes/`: 開発中の課題や検討事項に関するメモがMarkdown形式で格納されているディレクトリ。
-   `manifest.json`: Webアプリマニフェストファイル。PWA（プログレッシブウェブアプリ）機能のためのメタデータを提供し、ホーム画面への追加やオフライン利用などの機能に貢献します。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの設定ファイル。テストの実行オプションや検出ルールなどを定義します。
-   `requirements-dev.txt`: 開発環境およびテスト環境で必要となるPythonライブラリとそのバージョンをリストアップしたファイル。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行するために必要となるPythonライブラリとそのバージョンをリストアップしたファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
-   `ruff.toml`: Pythonのコードリンター/フォーマッターであるRuffの設定ファイル。コードスタイルや静的解析のルールを定義します。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   `__init__.py`: `src` ディレクトリがPythonパッケージであることを示す空ファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        -   `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示す空ファイル。
        -   `badge_generator.py`: リポジトリの言語やステータスなどを示すバッジのHTML/Markdownを生成するロジックが含まれます。
        -   `config.yml`: プロジェクト概要の取得設定など、システム固有の技術的パラメータを定義するYAML形式の設定ファイル。
        -   `config_manager.py`: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        -   `date_formatter.py`: リポジトリの更新日時などを人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成する一連の処理を実行します。
        -   `json_ld_template.json`: 検索エンジン最適化(SEO)のために構造化データを埋め込むためのJSON-LDテンプレート。
        -   `language_info.py`: リポジトリのプログラミング言語情報を処理し、表示に適した形式に変換するロジック。
        -   `markdown_generator.py`: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するコアロジック。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから既存のバッジ情報を抽出するロジック。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形するためのロジック。
        -   `seo_template.yml`: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算する機能。
        -   `strings.yml`: UIの表示メッセージや各種文言を一元管理するためのYAML形式の設定ファイル。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレート（Jinja2など）を処理し、データと結合して最終出力を生成する機能。
        -   `url_utils.py`: URLの構築や解析など、URL関連のユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py` モジュールに関連する機能のテストスクリプト。
-   `tests/`: プロジェクトのテストスクリプトを格納するディレクトリ。
    -   `test_badge_generator_integration.py`: `badge_generator` の統合テスト。
    -   `test_config.py`: 設定ファイルや設定マネージャーのロジックに関するテスト。
    -   `test_date_formatter.py`: 日付整形ユーティリティのテスト。
    -   `test_environment.py`: 開発環境のセットアップや依存関係に関するテスト。
    -   `test_integration.py`: システム全体の主要なフローに関する統合テスト。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテスト。
    -   `test_project_overview_fetcher.py`: `project_overview` 取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリ情報処理ロジックのテスト。

## 関数詳細説明
このプロジェクトはPythonモジュールとして構成されており、各ファイルに複数の関数が含まれる可能性があります。主な機能を持つ関数とその役割を以下に示します。

-   **`generate_repo_list.py`**:
    -   `main()`: プログラムのエントリポイント。GitHub APIからリポジトリ情報を取得し、整形、Markdown生成、ファイル出力までの一連の処理をオーケストレーションします。引数としてユーザー名や出力ファイル名、処理リポジトリ数の上限などを受け取ります。
-   **`badge_generator.py`**:
    -   `generate_badge(label, message, color)`: 指定されたラベル、メッセージ、色に基づいてSVGバッジのMarkdown/HTMLスニペットを生成します。
-   **`config_manager.py`**:
    -   `load_config(file_path)`: 指定されたYAML設定ファイルから設定を読み込み、Python辞書として返します。
-   **`date_formatter.py`**:
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を人間が読みやすい形式に変換します。
-   **`markdown_generator.py`**:
    -   `generate_repository_markdown(repository_data, template_config)`: 整形されたリポジトリデータとテンプレート設定を使用して、個々のリポジトリのMarkdownコンテンツを生成します。
    -   `generate_full_list_markdown(all_repositories_data, site_config)`: 処理された全リポジトリデータとサイト設定を基に、最終的なリポジトリ一覧のMarkdownファイルを生成します。
-   **`project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_name, github_token, config)`: 指定されたリポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を非同期で取得します。
-   **`repository_processor.py`**:
    -   `process_repository_data(raw_data, github_token, config)`: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出し、整形された辞書形式で返します。これには言語情報、スター数、フォーク数、プロジェクト概要の取得などが含まれます。
-   **`url_utils.py`**:
    -   `build_github_api_url(username, endpoint)`: GitHub APIのエンドポイントURLを構築します。

## 関数呼び出し階層ツリー
```
現在、関数呼び出し階層は分析されていません。

---
Generated at: 2026-01-31 07:07:35 JST
