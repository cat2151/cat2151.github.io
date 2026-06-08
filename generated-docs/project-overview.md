Last updated: 2026-06-09

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で収集・整理するシステムです。
- GitHub Pagesサイト向けに最適化されたMarkdown形式のリポジトリ一覧を自動生成します。
- 検索エンジンからのアクセス向上とLLMの参照効率改善を目的としたSEOフレンドリーな設計です。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesのベース)、Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Python: プロジェクトの主要なプログラミング言語。
    - GitHub API: リポジトリ情報を取得するためのインターフェース。
    - pytest: Pythonアプリケーションのテストフレームワーク。
    - ruff: Pythonコードのリンティングとフォーマットツール。
- テスト:
    - pytest: ユニットテスト、統合テストの実行に利用。
- ビルドツール:
    - (直接的なビルドツールはなし): PythonスクリプトがMarkdownファイルを生成する。
- 言語機能:
    - Pythonの標準ライブラリ: ファイル操作、HTTPリクエスト、データ構造操作などに利用。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation` ディレクトリの存在と説明から、CI/CDや自動化処理（例: 大容量ファイルチェック）に利用されていると推測されます。
- 開発標準:
    - .editorconfig: エディタ設定を統一するためのファイル。
    - ruff: コードスタイルガイドラインの強制と自動修正。

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
- **.editorconfig**: 複数の開発者間で異なるエディタやIDEを使用しても、一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなど、リポジトリの自動化ワークフローに関連するファイル群を格納するディレクトリ。
    - **.github_automation/check_large_files/**: 大容量ファイル検出のための設定とスクリプトを格納。
        - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明。
        - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の設定ファイル。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定する設定ファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの目的、機能、使い方、設定方法などを記述したメインドキュメント。
- **_config.yml**: GitHub Pages（Jekyll）のサイト全体の設定ファイル。
- **assets/**: Webサイトで使用する静的アセット（画像ファイルなど）を格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのファビコン画像ファイル。異なるサイズが用意されている。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグまたはテストに使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得されたプロジェクト概要ファイル `project-overview.md` が存在すると仮定されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。本プロジェクトで生成されるリポジトリ一覧の出力先。
- **issue-notes/**: Issueに関するメモなどを格納するディレクトリ。
    - **issue-notes/22.md**: 特定のIssueに関連するメモファイル。
- **manifest.json**: Progressive Web Apps (PWA) の設定ファイル。ウェブアプリケーションのマニフェストを定義。
- **pytest.ini**: pytestの実行設定を定義するファイル。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を記述したファイル。
- **requirements.txt**: 本番環境で必要なPythonパッケージの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどこをクロールしてよいか、どこを避けるべきかを指示するファイル。
- **ruff.toml**: PythonコードのリンティングおよびフォーマットツールRuffの設定ファイル。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **src/__init__.py**: Pythonパッケージを示すためのファイル。
    - **src/generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list` パッケージを示すためのファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリのバッジ（例: 言語、ライセンス）を生成または処理するロジックを格納。
        - **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプトの設定ファイル。プロジェクト概要取得機能のON/OFFなどが定義される。
        - **src/generate_repo_list/config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するロジック。
        - **src/generate_repo_list/date_formatter.py**: 日付フォーマットに関するユーティリティ関数を格納。
        - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownを生成するメインスクリプト。
        - **src/generate_repo_list/json_ld_template.json**: 構造化データ（JSON-LD）のテンプレートファイル。SEO強化に利用。
        - **src/generate_repo_list/language_info.py**: リポジトリの使用言語に関する情報を処理するロジック。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報から最終的なMarkdownコンテンツを生成するロジック。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの `project-overview.md` から概要をフェッチするロジック。
        - **src/generate_repo_list/readme_badge_extractor.py**: READMEファイルからバッジ情報を抽出するロジック。
        - **src/generate_repo_list/repository_processor.py**: 個々のリポジトリデータを整形し、表示可能な形式に処理するロジック。
        - **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータやコンテンツ構造に関するテンプレート設定。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリ関連の統計情報（スター数、フォーク数など）を計算するロジック。
        - **src/generate_repo_list/strings.yml**: UI表示メッセージや文言を管理するための設定ファイル。
        - **src/generate_repo_list/template_processor.py**: Markdown生成に使用するテンプレートの処理ロジック。
        - **src/generate_repo_list/url_utils.py**: URL関連のユーティリティ関数を格納。
- **test_project_overview.py**: `project_overview_fetcher` 機能のテストスクリプト。
- **tests/**: プロジェクトのテストスクリプトを格納するディレクトリ。
    - **tests/conftest.py**: pytestのフィクスチャやヘルパー関数を定義するファイル。
    - **tests/test_badge_generator_integration.py**: `badge_generator` の統合テスト。
    - **tests/test_check_large_files.py**: `check_large_files` スクリプトのテスト。
    - **tests/test_config.py**: 設定ファイル（`config.yml` など）の読み込みと処理に関するテスト。
    - **tests/test_date_formatter.py**: 日付フォーマットユーティリティ関数のテスト。
    - **tests/test_environment.py**: 環境設定や依存関係に関するテスト。
    - **tests/test_integration.py**: プロジェクト全体の主要な統合テスト。
    - **tests/test_markdown_generator.py**: Markdown生成ロジックのテスト。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **tests/test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **tests/test_repository_processor.py**: リポジトリ情報処理ロジックのテスト。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数名、引数、戻り値、詳細な機能に関する記述が不足しています。ハルシネーションを避けるため、各Pythonファイルの役割に基づき、そのファイル内で主要な処理を担うであろう関数群の概要を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - **主要な関数群**: GitHub APIを介してリポジトリ情報を取得し、取得したデータを処理し、最終的にMarkdown形式のリポジトリ一覧ファイルを生成する一連のメイン処理を調整・実行する関数群。コマンドライン引数の解析も含まれます。
- **`src/generate_repo_list/badge_generator.py`**:
    - **主要な関数群**: リポジトリのプログラミング言語、ライセンス、その他の属性に応じた視覚的なバッジ（アイコンなど）を生成または管理する関数群。
- **`src/generate_repo_list/config_manager.py`**:
    - **主要な関数群**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）を読み込み、パースし、アプリケーション全体で利用可能な形式で管理する関数群。
- **`src/generate_repo_list/date_formatter.py`**:
    - **主要な関数群**: 日付や時刻の情報を特定のフォーマット文字列（例: "YYYY-MM-DD"）に従って整形するユーティリティ関数群。
- **`src/generate_repo_list/language_info.py`**:
    - **主要な関数群**: リポジトリの使用言語に関する詳細情報（例: トップ言語、割合）を取得・解析し、表示に適した形に処理する関数群。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **主要な関数群**: 処理されたリポジトリデータを受け取り、Jekyllの要件に合致するSEO最適化されたMarkdown文字列として出力する関数群。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **主要な関数群**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）に存在するプロジェクト概要ファイルを非同期でフェッチし、その中から指定されたセクション（例: 3行の要約）を抽出する関数群。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
    - **主要な関数群**: リポジトリのREADMEファイルの内容を解析し、そこに埋め込まれたバッジのURLやテキスト情報を抽出する関数群。
- **`src/generate_repo_list/repository_processor.py`**:
    - **主要な関数群**: GitHub APIから取得した生のリポジトリデータを受け取り、それをプロジェクトの表示要件に合わせてフィルタリング、分類（アクティブ、アーカイブ、フォークなど）、および必要な統計情報を付加して整形する関数群。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - **主要な関数群**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、Markdown生成時に利用可能な形式で提供する関数群。
- **`src/generate_repo_list/template_processor.py`**:
    - **主要な関数群**: Markdown生成時に使用されるテンプレートファイル（例: `json_ld_template.json`, `seo_template.yml`）を読み込み、動的なデータでプレースホルダーを置き換える関数群。
- **`src/generate_repo_list/url_utils.py`**:
    - **主要な関数群**: URLの構築、解析、エンコーディングなど、URLに関連する一般的なユーティリティ機能を提供する関数群。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**:
    - **主要な関数群**: リポジトリ内のファイルサイズをチェックし、設定された閾値を超えるファイルがあれば警告またはエラーを報告する関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層の分析は提供された情報からは生成できませんでした。

---
Generated at: 2026-06-09 07:37:57 JST
