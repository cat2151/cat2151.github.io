Last updated: 2026-07-06

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEOを改善し、リポジトリ情報を効率的に公開するシステムです。
- GitHub APIからリポジトリ情報を取得し、Jekyll対応のMarkdownファイルを自動生成します。
- プロジェクト概要の自動抽出や分類表示により、検索エンジンとLLMの参照性を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤とし、静的なHTMLコンテンツを生成します。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語です。
    - Pytest: テストフレームワークとして使用され、コードの品質と信頼性を保証します。
    - Ruff: Pythonコードのスタイルチェックとフォーマットを自動化し、コードの一貫性を保ちます。
- テスト:
    - Pytest: ユニットテスト、統合テスト、および機能テストを実行します。
- ビルドツール:
    - Pythonスクリプト: GitHub APIからのデータ取得、Markdownファイルの生成、およびその他コンテンツ変換処理の実行を担います。
- 言語機能:
    - Python: メインのプログラミング言語。
    - YAML: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用されます。
    - Markdown: 生成されるリポジトリ一覧の出力形式です。
    - JSON: SEOのための構造化データ (JSON-LD) テンプレート (`json_ld_template.json`) に使用されます。
- 自動化・CI/CD:
    - GitHub API: リポジトリ情報の取得に使用されます。
    - GitHub Actions (設定ファイルにより言及): プロジェクト概要の自動取得など、特定機能の設定でCI/CD環境での利用を想定しています。
- 開発標準:
    - Ruff: Pythonコードのスタイルガイド強制、整形、およびリンティングを自動化します。

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
- **.editorconfig**: 異なるエディタ間でのコーディングスタイル (インデント、改行コードなど) を統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsを用いた自動化スクリプト群を格納するディレクトリ。
    - **check_large_files/**: 大規模ファイルをチェックするための自動化機能。
        - **README.md**: `check_large_files`機能に関する説明ドキュメント。
        - **check-large-files.toml**: 大規模ファイルチェックの設定パラメータを定義するファイル。
        - **scripts/check_large_files.py**: GitHubリポジトリ内の大規模ファイルを検出し、レポートするPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを記述したファイル。
- **LICENSE**: プロジェクトのライセンス情報 (MIT License) を記述したファイル。
- **README.md**: プロジェクトの目的、機能、使い方、設定方法などを説明する主要なドキュメントファイル。
- **_config.yml**: Jekyllサイト全体の共通設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどを指定します。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズのファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールのデバッグやテスト実行に使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得された `project-overview.md` ファイルが一時的に配置されることを想定したディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでのサイト所有権確認のために使用されるHTMLファイル。
- **index.md**: 生成されたリポジトリ一覧が書き込まれる、GitHub PagesのメインページとなるMarkdownファイル。
- **issue-notes/22.md**: 特定の課題（Issue #22）に関するメモや詳細情報が記述されたファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、Webアプリの表示方法、アイコン、スタートURLなどを定義します。
- **pytest.ini**: `pytest` テストフレームワークの動作設定を定義するファイル。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリをリストアップしたファイル。
- **requirements.txt**: プロジェクトの実行に必要なPythonライブラリをリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールするか、しないかを示す指示を記述したファイル。
- **ruff.toml**: Pythonコードリンター `ruff` の設定ファイル。コードスタイルルールや無視する項目などを定義します。
- **src/**: プロジェクトのソースコードを格納するメインディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        - **__init__.py**: `generate_repo_list`パッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの各種バッジ（例: ビルドステータス、ライセンス）を生成または処理するモジュール。
        - **config.yml**: `generate_repo_list`スクリプトの技術的パラメータや動作設定を定義するファイル。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、設定値を提供するモジュール。
        - **date_formatter.py**: 日付や時刻のフォーマットを処理するユーティリティ関数を提供するモジュール。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力するメインスクリプト。
        - **json_ld_template.json**: 構造化データ（JSON-LD）を生成するためのテンプレートファイル。SEO対策に利用されます。
        - **language_info.py**: リポジトリの使用言語に関する情報を処理し、表示に適した形式に変換するモジュール。
        - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するモジュール。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するモジュール。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ情報を解析・抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、表示に必要な形に整形するモジュール。
        - **seo_template.yml**: SEO関連のメタデータ（タイトル、ディスクリプションなど）を生成するためのテンプレート設定ファイル。
        - **statistics_calculator.py**: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するモジュール。
        - **strings.yml**: 表示メッセージ、カテゴリ名、文言などを国際化対応のために管理する設定ファイル。
        - **template_processor.py**: Markdownテンプレートに変数を埋め込み、最終的なコンテンツを生成するモジュール。
        - **url_utils.py**: URLの検証、構築、パースなど、URL関連のユーティリティ関数を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能に関するテストスクリプト。
- **tests/**: プロジェクトのテストスクリプトを格納するディレクトリ。
    - **conftest.py**: `pytest`の共通フィクスチャや設定を定義するファイル。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **test_check_large_files.py**: 大規模ファイルチェック機能のテスト。
    - **test_config.py**: 設定ファイルの読み込みおよび管理機能のテスト。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテスト。
    - **test_environment.py**: 開発・実行環境のセットアップに関するテスト。
    - **test_integration.py**: 主要な機能群の連携を検証する統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからバッジを抽出する機能のテスト。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**:
    - `main()`: プログラムのエントリポイント。コマンドライン引数をパースし、リポジトリ情報の取得、処理、Markdown生成の一連のフローを制御します。
- **src/generate_repo_list/repository_processor.py**:
    - `fetch_repositories(username, limit=None)`: GitHub APIを使用して、指定されたユーザー名のリポジトリ一覧を取得します。`limit`引数で取得するリポジトリ数を制限できます。
    - `process_repository(repo_data)`: GitHub APIから取得した個々のリポジトリデータ（JSON形式）を受け取り、必要な情報を抽出し、内部で扱いやすい形式に整形して返します。
- **src/generate_repo_list/markdown_generator.py**:
    - `generate_markdown(repo_list)`: 処理済みのリポジトリ情報リストを受け取り、Jekyllの要件に合わせたMarkdown形式の文字列を生成します。
- **src/generate_repo_list/project_overview_fetcher.py**:
    - `get_project_overview(repo_full_name, config_params)`: 指定されたリポジトリ (`repo_full_name`) から、設定ファイル (`config_params`) に定義されたパスとセクションタイトルに基づいてプロジェクト概要（3行説明）を抽出して返します。
- **src/generate_repo_list/config_manager.py**:
    - `load_config(file_path)`: 指定されたYAMLファイルパスから設定を読み込み、Pythonの辞書オブジェクトとして返します。
    - `get_secret(key)`: `secrets/secrets.toml`ファイルから、指定されたキーに対応するシークレット値を取得します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-07-06 07:22:53 JST
