Last updated: 2026-09-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けのMarkdownファイルを自動生成するシステムです。
- 生成されるリポジトリ一覧ページはSEOを最適化し、検索エンジンやLLMからの参照性向上を目指します。
- 各リポジトリの概要、バッジ、分類表示にも対応し、JekyllベースのGitHub Pagesサイトに統合可能です。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの構築基盤)、Markdown (自動生成されるコンテンツの形式)
- 音楽・オーディオ: N/A
- 開発ツール: Python (主要なスクリプト言語)、Git (バージョン管理システム)、pytest (Python用テストフレームワーク)、ruff (Pythonコードフォーマッタ・リンター)、EditorConfig (IDE間のコードスタイル統一)
- テスト: pytest (Pythonコードの単体・統合テスト実行)
- ビルドツール: Pythonスクリプト (Markdownコンテンツの生成処理)、Jekyll (GitHub Pagesサイトの静的サイトジェネレータ)
- 言語機能: Python (スクリプトの記述および実行)
- 自動化・CI/CD: GitHub API (リポジトリ情報取得の主要インターフェース)、`check_large_files.py` (GitHub Actionsなどで利用される可能性のあるファイルサイズチェック自動化スクリプト)
- 開発標準: ruff (Pythonコードのスタイルガイド強制および自動修正)、EditorConfig (プロジェクト全体のコーディングスタイル定義)
- その他: YAML (設定ファイル形式)、TOML (設定ファイル形式)、JSON (データ構造定義)

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
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
  22.md
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
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリ。
  - **check_large_files/**: ファイルサイズチェックの自動化機能に関連するファイル群。
    - **README.md**: `check_large_files`機能の説明。
    - **check-large-files.toml**: `check_large_files`スクリプトの設定ファイル。
    - **scripts/check_large_files.py**: 指定されたファイルが大きすぎないかをチェックするPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）。
- **README.md**: プロジェクトの概要、目的、機能、使用方法などを説明するメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の挙動を設定するファイル。テーマ、プラグイン、変数などを定義。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
  - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグやテストに特化したスクリプト。
- **generated-docs/**: リポジトリの特定のパスに配置され、プロジェクト概要などの情報を格納する可能性のあるディレクトリ（参照元）。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のためのHTMLファイル。
- **index.md**: このシステムによって生成される、リポジトリ一覧を含むメインのMarkdownファイル。GitHub Pagesのトップページとして機能する。
- **issue-notes/**: 課題やメモを記録するためのディレクトリ。
  - **22.md**: 特定の課題に関するメモファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの表示、アイコンなどを定義。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テスト検出ルールやプラグイン設定などを定義。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを列挙。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを列挙。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか/しないかを指示するファイル。
- **ruff.toml**: ruffコードフォーマッタおよびリンターの設定ファイル。コードスタイルルールを定義し、自動修正や警告を行う。
- **src/__init__.py**: Pythonパッケージの初期化ファイル。
- **src/generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージ。
  - **__init__.py**: Pythonパッケージの初期化ファイル。
  - **badge_generator.py**: リポジトリのステータスや特性を示すバッジ（例: アクティブ、アーカイブ、フォークなど）の生成ロジックを含む。
  - **config.yml**: プロジェクト固有の技術的パラメータ（例: プロジェクト概要取得機能の設定、キャッシュ設定など）を定義するファイル。
  - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するクラスや関数。
  - **date_formatter.py**: 日付や時刻の表示形式を整形するユーティリティ関数を提供する。
  - **generate_repo_list.py**: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力する処理を制御する。
  - **json_ld_template.json**: SEO最適化のため、JSON-LD形式の構造化データテンプレートを定義する。
  - **language_info.py**: リポジトリで使用されている言語に関する情報を処理、表示する機能を含む。
  - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成する。
  - **project_overview_fetcher.py**: 各リポジトリの特定のファイルから「プロジェクト概要」を自動取得する機能を担当する。
  - **readme_badge_extractor.py**: README.mdなどから特定のバッジ情報を抽出する機能を持つ。
  - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換するロジックを含む。
  - **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するファイル。
  - **statistics_calculator.py**: リポジトリに関連する統計情報（スター数、フォーク数など）を計算・集計する。
  - **strings.yml**: プロジェクトで表示される各種メッセージや文言を一元管理するファイル。多言語化にも対応可能。
  - **template_processor.py**: Markdown生成において、特定のテンプレートを処理し、データと結合する機能。
  - **url_utils.py**: URLの生成や解析、検証など、URL関連のユーティリティ関数を提供する。
- **test_project_overview.py**: プロジェクト概要取得機能のテストコード。
- **tests/**: プロジェクトのテストコードを格納するディレクトリ。
  - **conftest.py**: pytestのフィクスチャやヘルパー関数を定義するファイル。
  - `test_badge_generator_integration.py`, `test_check_large_files.py`, `test_config.py`, `test_date_formatter.py`, `test_environment.py`, `test_integration.py`, `test_markdown_generator.py`, `test_project_overview_fetcher.py`, `test_readme_badge_extractor.py`, `test_repository_processor.py`: 各機能の単体テストや統合テストコード。

## 関数詳細説明
プロジェクト情報には具体的な関数一覧や詳細説明が提供されていません。しかし、各ファイル名から、そのファイルがどのような機能を持つ関数群を提供しているかを推測できます。

- `generate_repo_list.py`: GitHub APIとの連携、リポジトリ情報の取得、取得したデータの処理、最終的なMarkdown出力の調整を行うメイン処理の関数群。
- `project_overview_fetcher.py`: GitHubリポジトリ内の特定のファイルからプロジェクト概要を非同期でフェッチし、解析する関数群。
- `markdown_generator.py`: リポジトリデータを受け取り、定義されたテンプレートに基づいてSEO最適化されたMarkdown文字列を生成する関数群。
- `repository_processor.py`: GitHub APIから取得したリポジトリの生データを整形し、フィルタリング、分類（アクティブ、アーカイブ、フォークなど）を行う関数群。
- `badge_generator.py`: リポジトリの状態（例：アーカイブ、フォーク）や言語などの情報から、対応するHTMLまたはMarkdown形式のバッジを生成する関数群。
- `date_formatter.py`: 日付オブジェクトやタイムスタンプを入力として受け取り、指定された形式で日付文字列を生成するユーティリティ関数群。
- `language_info.py`: リポジトリの言語情報を解析し、表示に適した形式に変換する関数群。
- `readme_badge_extractor.py`: リポジトリのREADME.mdファイルの内容を解析し、含まれるバッジ情報（例：shields.ioバッジ）を抽出する関数群。
- `statistics_calculator.py`: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算または集計する関数群。
- `template_processor.py`: 特定のテンプレートファイルとデータを受け取り、プレースホルダーを置き換えることで最終的なテキストコンテンツを生成する関数群。
- `url_utils.py`: URLの構築、検証、エンコード/デコードなど、URLに関連する様々なユーティリティ関数群。
- `.github_automation/check_large_files/scripts/check_large_files.py`: 指定されたディレクトリ内のファイルのサイズをチェックし、閾値を超えるファイルを報告する関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層はプロジェクト情報からは分析できませんでした。

---
Generated at: 2026-09-18 07:11:46 JST
