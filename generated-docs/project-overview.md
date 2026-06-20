Last updated: 2026-06-21

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けのリポジトリ一覧を自動生成するシステムです。
- 各リポジトリの情報を取得し、検索エンジン最適化されたMarkdown形式で出力します。
- 検索エンジンからの参照性を向上させ、LLMがリポジトリ情報を参照しやすくなることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として利用), Markdown (生成されるリポジトリ一覧コンテンツの形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: GitHub API (リポジトリ情報の取得に使用), YAML (設定ファイル管理 `config.yml`, `strings.yml`), TOML (設定ファイル管理 `pytest.ini`, `ruff.toml`, `secrets.toml`)
- テスト: pytest (Pythonコードの単体・統合テストフレームワーク)
- ビルドツール: Python (主要なスクリプト言語として、リポジトリ情報の取得・処理・Markdown生成を実行)
- 言語機能: Python (プロジェクトの中心となるスクリプト言語)
- 自動化・CI/CD: GitHub Pages (生成されたコンテンツを公開するためのプラットフォーム。本プロジェクト自体はCI/CDの仕組みを含まない)
- 開発標準: ruff (Pythonコードのスタイルチェックとフォーマットを自動化するリンター/フォーマッター)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリ。
    - **`check_large_files/`**: 大規模なファイルをチェックするためのスクリプト群。
        - **`README.md`**: `check_large_files`機能に関する説明。
        - **`check-large-files.toml`**: `check_large_files`スクリプトの設定ファイル。
        - **`scripts/check_large_files.py`**: 大規模ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定する設定ファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、使用方法、クイックスタートガイドなどを記述したメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイル。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン画像ファイル（様々なサイズ）。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用途のスクリプト。
- **`generated-docs/`**: `project-overview.md`のような、自動生成されたドキュメントを一時的に配置したり、参照したりする目的のディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認に使用されるHTMLファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして表示されるMarkdownファイル。本プロジェクトによってリポジトリ一覧がここに生成される。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリ。
    - **`22.md`**: 特定のissueに関する詳細メモ。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。アプリの表示方法や動作を定義する。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの実行方法やオプションを定義する。
- **`requirements-dev.txt`**: 開発環境で必要となるPythonライブラリのリスト（例: テストツール、リンターなど）。
- **`requirements.txt`**: プロジェクトの実行に最低限必要なPythonライブラリのリスト。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである `ruff` の設定ファイル。コードスタイルルールを定義する。
- **`src/`**: プロジェクトのソースコードを格納するメインディレクトリ。
    - **`__init__.py`**: Pythonパッケージの初期化ファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックが格納されるPythonパッケージ。
        - **`__init__.py`**: `generate_repo_list`パッケージの初期化ファイル。
        - **`badge_generator.py`**: リポジトリの言語やステータスを示すバッジ画像を生成するロジックを含む。
        - **`config.yml`**: `generate_repo_list`スクリプトの実行時設定を記述するファイル（例: プロジェクト概要取得機能の有効/無効、ターゲットファイルパスなど）。
        - **`config_manager.py`**: 設定ファイル(`config.yml`など)の読み込みと管理を行うモジュール。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティモジュール。
        - **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成する処理を orchestrate する。
        - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のためのJSON-LD形式のデータテンプレート。
        - **`language_info.py`**: リポジトリの使用言語に関する情報を処理・整形するモジュール。
        - **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、最終的なMarkdown形式のコンテンツを生成するロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するモジュール。
        - **`readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報などを抽出するモジュール。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報に変換する中心的な処理ロジック。
        - **`seo_template.yml`**: 検索エンジン最適化(SEO)関連のメタデータやテンプレート設定を記述するYAMLファイル。
        - **`statistics_calculator.py`**: リポジトリの星の数、フォーク数などの統計情報を計算するモジュール。
        - **`strings.yml`**: UIメッセージ、説明文、タイトルなどの表示文言を一元管理するYAMLファイル。
        - **`template_processor.py`**: Markdown生成などで使用するテンプレートを処理するモジュール。
        - **`url_utils.py`**: URLの処理や生成に関するユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関するテストスクリプト。
- **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリ。
    - **`conftest.py`**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`test_check_large_files.py`**: 大規模ファイルチェック機能のテスト。
    - **`test_config.py`**: 設定ファイル(`config.yml`など)の読み込み・管理機能のテスト。
    - **`test_date_formatter.py`**: 日付整形ユーティリティのテスト。
    - **`test_environment.py`**: テスト環境のセットアップや依存関係に関するテスト。
    - **`test_integration.py`**: システム全体の統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
提供された情報からは具体的な関数の詳細（引数、戻り値、内部ロジック）を直接抽出することはできませんでした。
しかし、本プロジェクトのPythonスクリプト群（例: `src/generate_repo_list/generate_repo_list.py`, `src/generate_repo_list/project_overview_fetcher.py`, `src/generate_repo_list/markdown_generator.py`など）には、以下のような役割を持つ関数が含まれていると推測されます。

- **GitHub APIとの通信関数**: リポジトリ情報やファイル内容を非同期で取得する役割。HTTPリクエストを送信し、JSON形式のレスポンスを解析する。
- **データ処理・整形関数**: 取得した生データを、表示に適した形式に変換する役割。日付のフォーマット、文字列のクリーンアップ、カテゴリ分類などを行う。
- **Markdown生成関数**: 整形されたデータから、Jekyll/GitHub Pagesに適したMarkdownテキストを組み立てる役割。テンプレート処理や条件分岐を含む。
- **設定管理関数**: YAML/TOMLファイルから設定値を読み込み、アプリケーション全体で利用可能な形式で提供する役割。
- **ユーティリティ関数**: バッジ生成、URLの処理、統計計算など、特定の補助的なタスクを実行する役割。
- **エラーハンドリング関数**: API呼び出しの失敗、ファイル読み込みエラーなど、予期せぬ問題が発生した際に適切に処理する役割。

これらの関数は通常、特定のタスクを実行するために設計され、必要なデータ（引数）を受け取り、処理結果（戻り値）を返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-21 07:29:15 JST
