Last updated: 2026-09-07

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧ページを自動生成するシステムです。
- 検索エンジンにクロールされにくいGitHubユーザーページの問題を解決し、SEO最適化を促進します。
- 各リポジトリの概要表示、バッジ、分類機能を提供し、GitHub Pagesの利便性を高めます。

## 技術スタック
- フロントエンド:
    - **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルを静的サイトとして公開するための基盤です。
    - **Markdown**: リポジトリ一覧ページおよび各リポジトリの概要がこの形式で生成されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **GitHub API**: リポジトリ情報をプログラムから取得するために使用されます。
    - **YAML**: プロジェクトの設定（`config.yml`）や表示メッセージ（`strings.yml`）、SEOテンプレート（`seo_template.yml`）の記述に利用されます。
    - **TOML**: GitHubトークンなどの機密情報（`secrets.toml`）やコードスタイル設定（`ruff.toml`）、pytest設定（`pytest.ini`）の記述に利用されます。
- テスト:
    - **Pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール: 該当なし（Pythonスクリプトが直接Markdownを生成します）
- 言語機能:
    - **Python**: プロジェクトの主要なロジックを実装するために使用されているプログラミング言語です。
- 自動化・CI/CD:
    - **GitHub Actions (間接的)**: `.github_automation` ディレクトリが存在することから、将来的なCI/CDや自動化スクリプトの連携が考慮されています。（このプロジェクト自体はPythonスクリプトによるMarkdown生成が主な機能です）
- 開発標準:
    - **Ruff**: Pythonコードのフォーマットとリントを自動的に行うためのツールです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクト全体の概要、セットアップ方法、実行コマンド、設定、ライセンスなど、このプロジェクトに関する主要な情報が記載されたメインのドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、URLなどの基本的な情報が含まれます。
- **`assets/` ディレクトリ**: GitHub Pagesサイトで使用される静的アセット（例: ファビコン画像）を格納します。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要の取得機能をデバッグするためのスクリプトです。
- **`generated-docs/` ディレクトリ**: 各リポジトリから自動取得されるプロジェクト概要ファイル（例: `project-overview.md`）などが格納されることを想定しています。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: `generate_repo_list.py` スクリプトによって自動生成される、GitHubリポジトリ一覧のメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 開発中の特定の問題（issue #22）に関するメモや詳細情報が記述されたファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示設定など）を定義するマニフェストファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出ルールやオプションを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリの依存関係が記述されています。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonライブラリの依存関係が記述されています。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか、しないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行うRuffツールの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージとして `src` ディレクトリを認識させるための空ファイルです。
- **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして `generate_repo_list` ディレクトリを認識させるための空ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（アーカイブなど）に応じたバッジのMarkdownを生成するロジックを保持します。
- **`src/generate_repo_list/config.yml`**: リポジトリ情報の取得、キャッシュ、プロジェクト概要の抽出などの技術的パラメータを設定するためのファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するための機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメイン実行スクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する全体プロセスを orchestrate します。
- **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のために、構造化データ（JSON-LD）を生成する際のテンプレートです。
- **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理・表示するためのロジックです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、Markdown形式のコンテンツを生成するコアロジックを担います。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEから特定のバッジ情報を抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理に適した形式に変換する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）関連のメタデータやテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関するスター数、フォーク数などの統計情報を計算する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: サイトに表示される各種メッセージや文言を外部化するためのファイルです。多言語対応や文言の統一に利用されます。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成で使用されるテンプレートファイル（例: Jinja2など）を読み込み、データを埋め込んでレンダリングする機能を提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、正規化などのユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
- **`tests/` ディレクトリ**: プロジェクトの様々なコンポーネントに対するテストスクリプトを格納します。
    - `conftest.py`: pytestのテストフィクスチャやヘルパー関数を定義するためのファイルです。
    - `test_badge_generator_integration.py`: バッジ生成機能の結合テストです。
    - `test_check_large_files.py`: 大容量ファイルチェック機能のテストです。
    - `test_config.py`: 設定ファイルの読み込み・管理機能のテストです。
    - `test_date_formatter.py`: 日付整形機能のテストです。
    - `test_environment.py`: 実行環境のセットアップに関するテストです。
    - `test_integration.py`: 主要なコンポーネント間の連携をテストする結合テストです。
    - `test_markdown_generator.py`: Markdown生成機能のテストです。
    - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストです。
    - `test_readme_badge_extractor.py`: READMEバッジ抽出機能のテストです。
    - `test_repository_processor.py`: リポジトリデータ処理機能のテストです。

## 関数詳細説明
提供された情報から具体的な引数や戻り値の詳細は不明ですが、各ファイルの役割から主要な関数の機能を推測して説明します。

- **`src/generate_repo_list/generate_repo_list.py` 内の `main` 関数**:
    - **役割**: プログラムのエントリポイントであり、GitHubリポジトリ一覧生成の全プロセスを制御します。コマンドライン引数を解析し、設定を読み込み、リポジトリ情報を取得・処理し、最終的なMarkdownファイルを出力します。
    - **機能**: 引数としてGitHubユーザー名、出力ファイル名、処理リポジトリ数制限などを受け取り、各モジュール（リポジトリプロセッサ、概要フェッチャー、Markdownジェネレータなど）を呼び出して連携させ、結果を所定のファイルに書き出します。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の `fetch_project_overview` 関数 (推測)**:
    - **役割**: 指定されたリポジトリパスとファイル名から、プロジェクトの概要説明を抽出します。
    - **機能**: リポジトリの特定パスにあるMarkdownファイル（例: `generated-docs/project-overview.md`）を読み込み、設定されたセクションタイトル（例: "プロジェクト概要"）以下の3行の説明をパースして返します。APIリクエストやファイルI/Oを伴う可能性があります。

- **`src/generate_repo_list/markdown_generator.py` 内の `generate_markdown` 関数 (推測)**:
    - **役割**: 処理済みのリポジトリデータと設定に基づき、GitHub Pages用のMarkdownコンテンツを生成します。
    - **機能**: 入力されたリポジトリオブジェクトのリストを受け取り、テンプレート（`template_processor.py`を利用）と組み合わせて、バッジ情報、プロジェクト概要、統計データなどを埋め込んだ整形済みのMarkdown文字列を生成して返します。

- **`src/generate_repo_list/repository_processor.py` 内の `process_repository_data` 関数 (推測)**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすい統一されたデータ構造に変換します。
    - **機能**: GitHub APIレスポンスとして受け取ったリポジトリごとの辞書データに対し、必要な情報の抽出、欠損値の補完、日付の整形（`date_formatter.py`を利用）、言語情報の処理（`language_info.py`を利用）などを行い、整形済みのリポジトリオブジェクトを返します。

- **`src/generate_repo_list/badge_generator.py` 内の `generate_badge_markdown` 関数 (推測)**:
    - **役割**: リポジトリの状態（アーカイブ、フォークなど）に応じて、対応するバッジのMarkdown文字列を生成します。
    - **機能**: リポジトリのプロパティ（例: `is_archived`, `is_fork`）を受け取り、事前に定義されたバッジのMarkdownスニペットを選択または生成して返します。

## 関数呼び出し階層ツリー
```
main (generate_repo_list.py)
├── config_manager.load_config()
├── repository_processor.process_repository_data()
│   ├── date_formatter.format_date()
│   └── language_info.get_language_details()
├── project_overview_fetcher.fetch_project_overview()
│   └── (GitHub API / ファイル読み込み)
├── markdown_generator.generate_markdown()
│   ├── template_processor.render_template()
│   ├── badge_generator.generate_badge_markdown()
│   └── statistics_calculator.calculate_stats()
└── (出力ファイルへの書き込み)

---
Generated at: 2026-09-07 07:13:59 JST
