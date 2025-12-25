Last updated: 2025-12-26

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧ページを自動生成するシステムです。
- GitHub APIを活用し、SEO最適化されたMarkdown形式でリポジトリ情報を出力します。
- 検索エンジンからの発見性を高め、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyllベース)**: 生成されたMarkdownファイルを静的サイトとして公開するための基盤。**Markdown**: リポジトリ一覧や各リポジトリの概要を表示するためのコンテンツ形式。
- 音楽・オーディオ: 該当なし
- 開発ツール: **pytest**: Pythonコードのテストフレームワーク。**ruff**: Pythonコードのリンターおよびフォーマッター。
- テスト: **pytest**: ユニットテスト、結合テストを実行するためのフレームワーク。
- ビルドツール: **Python**: リポジトリ情報の取得、処理、Markdown生成を行うスクリプト言語。**GitHub Pages (Jekyll)**: 最終的なウェブサイトを構築・デプロイするサービス。
- 言語機能: **Python**: プロジェクトの主要な開発言語。
- 自動化・CI/CD: **GitHub Actions**: (暗黙的に) リポジトリ一覧の自動生成スクリプトを実行するためのCI/CDプラットフォームとして利用される可能性がありますが、プロジェクト自体はローカル開発重視と明記されています。
- 開発標準: **ruff**: コードの品質と一貫性を保つためのフォーマッターおよびリンター。

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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を一貫させるための設定ファイル。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報 (MITライセンス) を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方、主な機能などを説明するメインドキュメント。
- **`_config.yml`**: Jekyllによって構築されるGitHub Pagesサイト全体の共通設定ファイル。テーマやプラグイン、サイト変数などを定義します。
- **`assets/`**: サイトの画像やファビコンなどの静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイル。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプト。
- **`generated-docs/`**: 各リポジトリのプロジェクト概要などが格納される可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
- **`index.md`**: 自動生成されたリポジトリ一覧コンテンツが出力されるメインのMarkdownファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 過去の課題や検討事項に関するメモがMarkdown形式で格納されているディレクトリ。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークpytestの設定ファイル。テストの実行方法やカバレッジレポートなどを指定します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージの依存関係を定義するファイル。
- **`requirements.txt`**: 本番環境でこのシステムを実行するために必要なPythonパッケージの依存関係を定義するファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    - **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを認識させるための空ファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成に関するコアロジックを格納するサブパッケージ。
        - **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして`generate_repo_list`ディレクトリを認識させるための空ファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの状態（アクティブ、アーカイブ、フォークなど）に応じたバッジのMarkdownを生成するロジックを記述。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的な動作パラメータを設定するYAMLファイル。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`) の読み込みと管理を行うモジュール。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのエントリーポイントとなるメインスクリプト。GitHub APIからの情報取得、処理、Markdown生成、ファイル出力の一連の流れを統括します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、JSON-LD形式の構造化データを生成するためのテンプレート。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するロジック。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジック。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得するロジック。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータをフィルタリング、ソート、整形するロジック。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算するロジック。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するYAMLファイル。多言語対応などにも利用可能です。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2など）の処理を担うモジュール。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関するテストケースを記述したファイル。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテスト。
    - **`test_environment.py`**: 実行環境や依存関係に関するテスト。
    - **`test_integration.py`**: システムの主要なコンポーネントが連携して正しく動作するかを確認する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成ロジックが期待通りに動作するかを確認するテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要を正確に取得できるかを確認するテスト。
    - **`test_repository_processor.py`**: リポジトリデータの処理や整形ロジックの正確性を検証するテスト。

## 関数詳細説明
- **`generate_repo_list.py`内の主要関数 (例: `main()`, `run_generator()`)**
    - 役割: プログラムのエントリーポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、最終的なファイル出力までの一連のワークフローをオーケストレートします。
    - 引数: `username` (GitHubユーザー名), `output` (出力ファイル名), `limit` (処理するリポジトリ数の上限、開発用) など。
    - 戻り値: なし（直接ファイルに書き込むため）。
- **`repository_processor.py`内の主要関数 (例: `fetch_repositories()`, `process_repository_data()`)**
    - 役割: 指定されたGitHubユーザーのリポジトリ情報をGitHub API経由で取得し、必要に応じてフィルタリング、ソート、整形を行います。
    - 引数: `username`, `github_token` (API認証用), フィルター条件など。
    - 戻り値: 処理済みリポジトリ情報のリスト。
- **`project_overview_fetcher.py`内の主要関数 (例: `get_project_overview_from_repo()`)**
    - 役割: 各リポジトリ内の指定されたパス（例: `generated-docs/project-overview.md`）から「プロジェクト概要」セクションの3行説明を自動的に抽出し取得します。
    - 引数: `repo_full_name` (リポジトリ名), `file_path` (概要ファイルのパス), `section_title` (概要セクションのタイトル) など。
    - 戻り値: 抽出された3行のプロジェクト概要テキスト（リストまたは単一文字列）。
- **`markdown_generator.py`内の主要関数 (例: `generate_repository_list_markdown()`)**
    - 役割: 処理済みのリポジトリ情報リストを受け取り、これらを基にGitHub Pages用のSEO最適化されたMarkdown形式のコンテンツを生成します。
    - 引数: `repository_data_list` (処理済みリポジトリ情報のリスト), テンプレートデータなど。
    - 戻り値: 生成されたMarkdown文字列。
- **`badge_generator.py`内の主要関数 (例: `create_status_badge()`)**
    - 役割: リポジトリの状態（例: active, archived, forked）を示すバッジのMarkdown文字列を生成します。
    - 引数: `repository_status` (リポジトリのステータス情報)。
    - 戻り値: バッジのMarkdown文字列。
- **`config_manager.py`内の主要関数 (例: `load_config()`, `get_string()`)**
    - 役割: `config.yml`や`strings.yml`などの設定ファイルを読み込み、設定値や表示メッセージをアプリケーションの他の部分に提供します。
    - 引数: `file_path` (設定ファイルのパス), `key` (取得したい設定項目のキー) など。
    - 戻り値: 設定値または文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-26 07:06:01 JST
