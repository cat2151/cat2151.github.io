Last updated: 2026-04-05

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・整形するシステムです。
- ユーザーのGitHub Pagesサイト向けに、検索エンジン最適化(SEO)されたMarkdown形式のリポジトリ一覧ページを自動生成します。
- 各リポジトリの概要、バッジ、分類などを表示し、LLMによる参照性の向上と訪問者への情報提供を目的としています。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルをホスティングし、静的サイトとして公開するフレームワーク。**Markdown**: 生成されるリポジトリ一覧のコンテンツ形式。
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python**: プロジェクトの主要なプログラミング言語。**ruff**: Pythonコードのリンティングとフォーマットを自動化するツール。
- テスト: **pytest**: Pythonプロジェクトのテストフレームワーク。単体テストや統合テストの実行に利用。
- ビルドツール: **Pythonスクリプト**: GitHub APIからのデータ取得とMarkdown生成を行うカスタムビルドロジック。**Jekyll**: GitHub Pagesのビルドエンジン。
- 言語機能: **Python**: 豊富な標準ライブラリと表現力を持ち、スクリプト開発に適しています。
- 自動化・CI/CD: **GitHub Actions (部分的に)**: `.github_automation`ディレクトリが存在し、大容量ファイルチェックなどの自動化スクリプトを含みます。プロジェクトの主要な生成プロセスはローカル実行を重視しています。
- 開発標準: **ruff**: コードスタイルの一貫性を保ち、品質を向上させるための自動修正ツール。**.editorconfig**: 異なるエディタ間でコードの整形ルールを統一するための設定ファイル。

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
- **`.editorconfig`**: 開発環境全体でインデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsや関連する自動化スクリプトを格納するディレクトリです。
  - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
  - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
  - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使い方、開発者向けの情報などを記述したメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の挙動を設定するファイルです。テーマ、プラグイン、パーマリンク構造などを定義します。
- **`assets/`**: ウェブサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的ファイルを格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリからプロジェクト概要 (`project-overview.md`) が取得されるターゲットディレクトリ、または関連ドキュメントを一時的に格納する場所として想定されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有者確認のために使用される、空または特定の文字列を含むHTMLファイルです。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、GitHub Pagesのリポジトリ一覧ページのメインコンテンツとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録するためのファイル群を格納するディレクトリです。
  - **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモや議論が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルです。ウェブアプリの名前、アイコン、表示モードなどを定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルです。テスト検出パスやマーカー、追加の引数などを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境でのみ必要なPythonライブラリをリストアップしたファイルです。本番環境には不要なツールなどが含まれます。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのURLをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットに関する設定ファイルです。`ruff`ツールがこの設定に従ってコードスタイルを自動修正します。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
  - **`__init__.py`**: Pythonパッケージを示すための空のファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成機能の中核となるPythonモジュール群を格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すための空のファイルです。
    - **`badge_generator.py`**: リポジトリの各種状態（言語、ライセンス、スター数など）に応じたMarkdownバッジを生成する機能を提供します。
    - **`config.yml`**: `generate_repo_list`モジュール固有の設定、特にプロジェクト概要取得機能などの技術的パラメータを定義します。
    - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体の動作パラメータを管理するユーティリティです。
    - **`date_formatter.py`**: 日付情報を特定のフォーマット文字列に変換するユーティリティ関数群です。
    - **`generate_repo_list.py`**: コマンドラインから実行され、GitHub APIを呼び出し、リポジトリ情報を取得し、Markdown形式で一覧ファイルを生成するメインスクリプトです。
    - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のためのJSON-LD形式のテンプレートファイルです。生成されるページに構造化データを組み込むために使用されます。
    - **`language_info.py`**: リポジトリの主要言語情報を取得・処理し、Markdown表示用に整形する機能を提供します。
    - **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートを基に、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックです。
    - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し取得する機能です。
    - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能です。
    - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを整形し、Markdown生成に適した形式に変換する役割を担います。
    - **`seo_template.yml`**: 検索エンジン最適化(SEO)のためのメタデータや設定を定義するテンプレートファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算する機能を提供します。
    - **`strings.yml`**: UI表示や生成されるMarkdown内の固定文言、メッセージを管理するための設定ファイルです。多言語対応や文言変更の容易化を目的とします。
    - **`template_processor.py`**: MarkdownテンプレートやSEO用テンプレートを処理し、動的なコンテンツを埋め込む汎用的なテンプレート処理機能です。
    - **`url_utils.py`**: URLの生成、検証、整形など、URLに関するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`の機能をテストするためのスクリプトです。
- **`tests/`**: プロジェクトの各モジュールや機能に対する単体テスト、統合テストのスクリプトを格納するディレクトリです。
  - **`conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義するファイルです。テスト間で共通のセットアップなどを提供します。
  - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
  - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
  - **`test_config.py`**: 設定管理機能 (`config_manager.py`) のテストです。
  - **`test_date_formatter.py`**: 日付フォーマット機能のテストです。
  - **`test_environment.py`**: 開発環境や依存関係に関するテストです。
  - **`test_integration.py`**: システム全体の主要機能が連携して正しく動作するかを確認する統合テストです。
  - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
  - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
  - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
    - 関数名: `main()`
    - 役割: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、Markdownを生成して指定されたファイルに出力する一連の処理を統括します。プロジェクトの主要なエントリーポイントです。
    - 引数: なし (コマンドライン引数は内部で解析されます)
    - 戻り値: なし (処理の成功/失敗はシステム終了コードで示されます)
- **`src/generate_repo_list/badge_generator.py`**:
    - 関数名: `generate_badge_markdown(repo_data, badge_type)` (推測)
    - 役割: リポジトリのデータと指定されたバッジタイプ（例: 言語、ライセンス、スター数）に基づいて、表示用のMarkdownバッジ文字列を生成します。
    - 引数: `repo_data` (リポジトリ情報を格納した辞書やオブジェクト)、`badge_type` (生成するバッジの種類を示す文字列)
    - 戻り値: 生成されたバッジのMarkdown文字列 (例: `![Python](https://img.shields.io/badge/language-python-blue)` )
- **`src/generate_repo_list/config_manager.py`**:
    - 関数名: `load_config(config_path)` (推測)
    - 役割: 指定されたパスのYAML設定ファイルを読み込み、設定値をPythonの辞書やオブジェクトとして提供します。
    - 引数: `config_path` (設定ファイルへのパスを示す文字列)
    - 戻り値: 設定内容を格納した辞書またはオブジェクト
- **`src/generate_repo_list/date_formatter.py`**:
    - 関数名: `format_date(date_string, format_specifier)` (推測)
    - 役割: 日付/時刻を表す文字列を指定されたフォーマットで整形し、人間が読みやすい形式に変換します。
    - 引数: `date_string` (日付/時刻を表すISO 8601形式などの文字列)、`format_specifier` (出力フォーマットを示す文字列、例: `%Y-%m-%d`)
    - 戻り値: フォーマットされた日付文字列
- **`src/generate_repo_list/markdown_generator.py`**:
    - 関数名: `generate_repo_list_markdown(repositories_data, config)` (推測)
    - 役割: 処理されたリポジトリデータのリストと設定情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツ全体を生成します。
    - 引数: `repositories_data` (整形されたリポジトリ情報のリスト)、`config` (プロジェクトの設定)
    - 戻り値: 生成されたMarkdownコンテンツの文字列
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - 関数名: `fetch_overview_from_repo(repo_owner, repo_name, config)` (推測)
    - 役割: 指定されたリポジトリ内の `generated-docs/project-overview.md` ファイルから、設定で指定されたセクション（例: 「プロジェクト概要」）の3行説明を抽出し、取得します。GitHub APIを介してファイル内容にアクセスします。
    - 引数: `repo_owner` (リポジトリの所有者名)、`repo_name` (リポジトリ名)、`config` (プロジェクト概要取得に関する設定)
    - 戻り値: 抽出された3行の概要リスト、または取得失敗時は空のリストやNone
- **`src/generate_repo_list/repository_processor.py`**:
    - 関数名: `process_repository_data(raw_repo_data, config)` (推測)
    - 役割: GitHub APIから直接取得した生のリポジトリデータを受け取り、表示に必要な情報（クリーンな説明、適切なURL、言語情報など）に加工・整形します。
    - 引数: `raw_repo_data` (GitHub APIから取得したリポジトリデータの辞書)、`config` (処理に関する設定)
    - 戻り値: 整形され、Markdown生成に適した形式のリポジトリデータ辞書
- **`src/generate_repo_list/template_processor.py`**:
    - 関数名: `apply_template(template_content, data)` (推測)
    - 役割: プレースホルダーを含むテンプレートコンテンツに、提供されたデータ（辞書など）を埋め込み、最終的な文字列コンテンツを生成します。
    - 引数: `template_content` (テンプレート文字列)、`data` (テンプレートに埋め込むデータ辞書)
    - 戻り値: データが埋め込まれた最終コンテンツ文字列
- **`src/generate_repo_list/url_utils.py`**:
    - 関数名: `generate_github_repo_url(username, repo_name)` (推測)
    - 役割: GitHubのユーザー名とリポジトリ名から、該当リポジトリへの正確なURLを生成します。
    - 引数: `username` (GitHubユーザー名)、`repo_name` (リポジトリ名)
    - 戻り値: 生成されたリポジトリURL文字列

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-05 07:08:54 JST
