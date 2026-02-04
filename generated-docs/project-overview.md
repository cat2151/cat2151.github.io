Last updated: 2026-02-05

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、自身のGitHubリポジトリ情報を自動で収集・整理するシステムです。
- 収集した情報に基づき、SEOに最適化されたJekyll/GitHub Pages用のMarkdownファイルを自動生成します。
- これにより、公開リポジトリ一覧や各リポジトリの概要が検索エンジンに適切にインデックスされ、参照性を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータ)、Markdown (リポジトリ一覧のコンテンツ形式)、HTML/CSS (Jekyllテーマによる描画)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用していません。
- 開発ツール: Python (主要なスクリプト言語)、GitHub API (リポジトリ情報取得)、Ruff (コードリンター・フォーマッター)、Pytest (単体・統合テストフレームワーク)
- テスト: Pytest (Pythonコードのテスト自動化)
- ビルドツール: Pythonスクリプト (Markdownコンテンツの生成ロジック)、Jekyll (GitHub Pagesサイトのビルドプロセス)
- 言語機能: Python (スクリプトの実行環境および標準ライブラリ)
- 自動化・CI/CD: GitHub Pages (生成されたコンテンツの自動デプロイプラットフォーム)、ローカルスクリプト実行によるコンテンツ自動生成 (CI/CDパイプラインは意図的にシンプル化)
- 開発標準: Ruff (Pythonコードの品質と一貫性を保つためのルールセット)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載しています。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向け情報などを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体のグローバル設定（サイトタイトル、テーマ、プラグインなど）を定義するファイルです。
- **`assets/`**: Jekyllサイトで利用される画像、アイコンなどの静的ファイルを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示される小さなアイコン）画像ファイル群です。
- **`debug_project_overview.py`**: プロジェクト概要取得機能の動作確認やデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した`project-overview.md`などのドキュメントを一時的に格納したり、生成された中間ファイルを配置するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるファイルです。
- **`index.md`**: GitHubリポジトリ一覧が自動生成され、最終的に出力されるMarkdownファイルです。Jekyllによって処理され、GitHub Pagesサイトのトップページとして表示されます。
- **`issue-notes/`**: 開発中の課題、検討事項、メモなどをMarkdown形式で記録したファイル群を格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、ウェブアプリのメタデータ（名称、アイコン、表示モードなど）を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonライブラリの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働時に必要となるPythonライブラリの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内でクロールを許可または禁止するパスを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンターおよびフォーマッターである`ruff`の挙動を定義する設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージを初期化するためのファイルです。
        - **`badge_generator.py`**: リポジトリの技術スタックやライセンスなどのバッジ（アイコン）をMarkdown形式で生成するロジックを含みます。
        - **`config.yml`**: `project_overview`機能など、スクリプトの動作に関する技術的パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: YAML形式の設定ファイルを読み込み、プログラム内で利用可能な形式で管理する機能を提供します。
        - **`date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式に整形するユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このシステムのメインスクリプト。GitHub APIからリポジトリ情報を取得し、各コンポーネントを連携させて最終的なMarkdownファイルを生成する処理を統括します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために利用されるJSON-LD形式のデータテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報（アイコン、色など）を処理し、表示に役立てる機能を提供します。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報から、SEOに最適化されたMarkdownコンテンツを生成する主要なロジックを担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリの`README.md`ファイルから、特定の形式で埋め込まれたバッジ情報を解析・抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適したデータ構造に変換する役割を担います。
        - **`seo_template.yml`**: SEO関連のメタデータやコンテンツ構造を定義するためのYAMLテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数といった統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: プロジェクト内で使用される表示テキスト、メッセージ、文言などを一元的に管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に、Jinja2などのテンプレートエンジンを用いて動的にコンテンツを組み立てる処理を担います。
        - **`url_utils.py`**: GitHub関連のURL構築や、URLの検証などのユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能に関する単体テストを定義するスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_config.py`**: 設定ファイルの読み込みおよび`config_manager`の機能に関するテストです。
    - **`test_date_formatter.py`**: 日付整形機能`date_formatter`に関するテストです。
    - **`test_environment.py`**: 実行環境の設定や依存関係に関するテストです。
    - **`test_integration.py`**: システム全体の主要なフローに関する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能`markdown_generator`に関するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの詳細なテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能`readme_badge_extractor`に関するテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能`repository_processor`に関するテストです。

## 関数詳細説明
このプロジェクトはPythonで実装されており、各モジュールに複数の関数が含まれています。ここでは主要なモジュールの代表的な機能について説明します。具体的な引数や戻り値の型はコードベースに依存するため、ここでは汎用的な役割を記述します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`: スクリプトのエントリポイントとなる関数です。GitHub APIからリポジトリ情報を取得し、各処理モジュールを呼び出してMarkdownコンテンツを生成し、指定された出力ファイルに書き出す一連のフローをオーケストレートします。
-   **`src/generate_repo_list/repository_processor.py`**
    -   `process_repository(repository_data)`: GitHub APIから取得した単一のリポジトリデータを受け取り、生成されるMarkdownで利用しやすいように必要な情報を抽出し、整形されたデータ構造として返します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLと設定情報に基づき、リモートの`project-overview.md`ファイルを読み込み、設定で指定されたセクション（例: "プロジェクト概要"）から3行の概要テキストを抽出して返します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_repository_markdown(processed_repo_data)`: `repository_processor`によって整形された単一のリポジトリデータを受け取り、そのリポジトリに関するMarkdown形式のスニペットを生成して返します。これにはバッジ、概要、リンクなどが含まれます。
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badge_markdown(badge_type, value)`: 指定されたバッジの種類（例: 言語、ライセンス）と値に基づいて、対応するMarkdown形式のバッジ文字列を生成して返します。
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(config_path)`: 指定されたパスにあるYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(datetime_obj)`: 日時オブジェクトを受け取り、指定されたフォーマットで日付文字列を整形して返します。
-   **`src/generate_repo_list/url_utils.py`**
    -   `build_github_url(username, repo_name, path=None)`: GitHubのユーザー名、リポジトリ名、およびオプションのパスから、完全なGitHub URLを構築して返します。
-   **`src/generate_repo_list/template_processor.py`**
    -   `render_template(template_content, data)`: テンプレート文字列とデータを入力として受け取り、テンプレートエンジン（例: Jinja2）を使用してレンダリングされたテキスト（Markdown）を返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-05 07:08:01 JST
