Last updated: 2026-05-28

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEOとLLMによるリポジトリ参照問題を解決するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のMarkdownファイルを自動生成します。
- リポジトリ一覧、バッジ、各プロジェクトの概要など豊富な情報を自動で公開サイトに反映します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイト構築の基盤), Markdown (生成されるWebコンテンツの形式), JSON-LD (検索エンジン最適化のための構造化データ記述形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: Git (バージョン管理システム), GitHub API (リポジトリ情報の取得インターフェース)
- テスト: pytest (Pythonコードの単体・統合テストフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIとの連携および動的なMarkdown生成のコアロジック), YAML/JSON (設定ファイルやテンプレートの記述形式)
- 言語機能: Python (プロジェクトの主要開発言語)
- 自動化・CI/CD: GitHub Actions (本システムを継続的に実行し、GitHub Pagesを更新するためのCI/CD環境として利用可能)
- 開発標準: ruff (Pythonコードの品質向上とスタイル統一のためのリンター・フォーマッター), EditorConfig (異なる開発環境間でのコードスタイルの一貫性を保つための設定ファイル)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコードスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いた自動化処理に関連するスクリプトや設定を格納するディレクトリです。
  - **.github_automation/check_large_files/**: 大容量ファイルのチェックを行う自動化スクリプト群です。
    - **README.md**: `check_large_files` 機能の説明ドキュメントです。
    - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
    - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitでバージョン管理しないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの概要、目的、使い方、開発者向け情報などをまとめた主要ドキュメントです。
- **_config.yml**: Jekyllサイト全体の基本的な設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
  - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグや単体テストに利用されるスクリプトです。
- **generated-docs/**: 生成されたドキュメントや、他リポジトリから取得した概要ファイルが一時的に格納される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでのサイト所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって自動生成される、リポジトリ一覧のメインMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: プロジェクトの課題、検討事項、開発メモなどを個別に記録したファイル群です。
  - **22.md**: 特定の課題やメモに関するMarkdownファイルです。
- **manifest.json**: WebサイトをProgressive Web App (PWA) として機能させるためのマニフェストファイルです。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonライブラリの依存関係を定義したファイルです。
- **requirements.txt**: プロジェクトの本番運用環境で必要となるPythonライブラリの依存関係を定義したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またどのページを避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのスタイルチェックとフォーマットを行う`ruff`ツールの設定ファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
  - **__init__.py**: `src`ディレクトリをPythonパッケージとして認識させるための初期化ファイルです。
  - **src/generate_repo_list/**: リポジトリ一覧生成ロジックをまとめたPythonパッケージです。
    - **__init__.py**: `generate_repo_list`ディレクトリをPythonサブパッケージとして認識させるための初期化ファイルです。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジのMarkdownを生成するロジックが含まれています。
    - **config.yml**: プロジェクト概要取得機能など、主要な技術的パラメータを設定するファイルです。
    - **config_manager.py**: 設定ファイル（`config.yml`など）の読み込み、解析、管理を行うロジックが含まれています。
    - **date_formatter.py**: GitHub APIから取得した日付データを整形し、表示に適した形式にするロジックが含まれています。
    - **generate_repo_list.py**: プロジェクトのメインエントリポイントとなるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する全体の処理フローを制御します。
    - **json_ld_template.json**: 検索エンジン最適化のためのJSON-LD形式の構造化データテンプレートです。
    - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に利用するロジックが含まれています。
    - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックが含まれています。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要説明を自動的に取得するロジックが含まれています。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出し、再利用または加工するロジックが含まれています。
    - **repository_processor.py**: 個々のGitHubリポジトリから取得した生データを解析し、必要な情報を抽出・整理するロジックが含まれています。
    - **seo_template.yml**: 検索エンジン最適化に関連するテンプレートや設定を定義するファイルです。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックが含まれています。
    - **strings.yml**: UIに表示されるメッセージ、文言、キャプションなどを一元的に管理する設定ファイルです。
    - **template_processor.py**: マークダウン生成などで利用される各種テンプレートファイルの読み込みと、データを用いたレンダリングを行うロジックが含まれています。
    - **url_utils.py**: URLの操作、バリデーション、整形など、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能の単体テストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **conftest.py**: `pytest`のテスト実行時に共通で利用されるフィクスチャやヘルパー関数を定義するファイルです。
  - **test_badge_generator_integration.py**: バッジ生成機能の統合的な動作を確認するテストです。
  - **test_check_large_files.py**: 大容量ファイルチェック機能のテストスクリプトです。
  - **test_config.py**: 設定ファイルの読み込みや管理機能に関するテストです。
  - **test_date_formatter.py**: 日付フォーマット機能のテストです。
  - **test_environment.py**: 実行環境の設定や依存関係に関するテストです。
  - **test_integration.py**: プロジェクト全体の主要な機能が連携して正しく動作するかを確認する統合テストです。
  - **test_markdown_generator.py**: Markdown生成機能のテストです。
  - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
  - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
  - **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
提供されたプロジェクト情報からは、`googled947dc864c270e07.html`を除くファイルについては具体的な関数名の詳細が明示されていませんが、各Pythonファイルはその役割に応じた主要な関数群を持つことが想定されます。以下に、主要なファイルの機能から推測される関数の役割を説明します。

- **src/generate_repo_list/generate_repo_list.py**:
  - `main()`: プロジェクトのエントリポイントとなる関数で、コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得から最終的なMarkdownファイルの生成まで、全体の処理フローを調整します。
- **src/generate_repo_list/badge_generator.py**:
  - `generate_badge_markup(repository_data)`: リポジトリのデータを受け取り、そのリポジトリに関連するバッジ（例: 言語、ライセンス、ステータスなど）のMarkdown形式のマークアップを生成します。
- **src/generate_repo_list/config_manager.py**:
  - `load_config(config_path)`: 指定されたパスからYAML設定ファイルを読み込み、設定データを辞書形式で返します。
- **src/generate_repo_list/date_formatter.py**:
  - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形して返します。
- **src/generate_repo_list/project_overview_fetcher.py**:
  - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリURLと設定に基づき、対象リポジトリ内の特定のファイルからプロジェクトの概要（3行説明など）をHTTPリクエストを通じて取得します。キャッシュ機能やリトライ処理も内包する可能性があります。
- **src/generate_repo_list/markdown_generator.py**:
  - `generate_repo_list_markdown(repositories_data, strings_config)`: 複数のリポジトリデータと文言設定を受け取り、それらを基にリポジトリ一覧のMarkdownコンテンツ全体を生成します。
  - `generate_repository_section(repo_data)`: 個々のリポジトリデータを受け取り、そのリポジトリの情報を表示するためのMarkdownセクションを生成します。
- **src/generate_repo_list/repository_processor.py**:
  - `process_repository(api_data, overview_fetcher)`: GitHub APIから取得した生のリポジトリデータと、プロジェクト概要フェッチャーなどを利用して、表示に必要な情報を整形・加工した単一のリポジトリデータオブジェクトを生成します。
- **src/generate_repo_list/readme_badge_extractor.py**:
  - `extract_badges(readme_content)`: リポジトリのREADMEコンテンツから、既に埋め込まれているバッジのURLやテキスト情報を抽出します。
- **src/generate_repo_list/statistics_calculator.py**:
  - `calculate_language_stats(repositories_data)`: 複数のリポジトリデータから、使用されているプログラミング言語の分布や統計情報を計算します。
- **src/generate_repo_list/template_processor.py**:
  - `render_template(template_path, context)`: 指定されたテンプレートファイル（例: Markdownテンプレート）とコンテキストデータを受け取り、データを埋め込んだ最終的な文字列をレンダリングします。
- **src/generate_repo_list/url_utils.py**:
  - `construct_github_api_url(username)`: 指定されたユーザー名に基づいて、GitHub APIのエンドポイントURLを構築します。
  - `validate_url(url_string)`: 与えられた文字列が有効なURLであるか検証します。
- **.github_automation/check_large_files/scripts/check_large_files.py**:
  - `check_files(config_path)`: 設定ファイルに基づいて、プロジェクト内のファイルサイズをチェックし、閾値を超えるファイルを報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-28 07:35:34 JST
