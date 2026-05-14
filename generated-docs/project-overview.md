Last updated: 2026-05-15

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、自動でリポジトリ一覧を生成するシステムです。
- JekyllベースのGitHub Pagesサイト向けにSEO最適化されたMarkdownファイルを生成します。
- これにより、検索エンジンでの発見性を高め、LLMによるリポジトリ参照の問題を緩和します。

## 技術スタック
- フロントエンド:
  - **Jekyll**: 静的サイトジェネレーターで、GitHub Pagesサイトの基盤として利用されます。
  - **Markdown**: 生成されるリポジトリ一覧コンテンツの形式であり、Jekyllでレンダリングされます。
- 音楽・オーディオ:
  - 該当する技術は使用されていません。
- 開発ツール:
  - **Python**: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得、処理、Markdown生成の中核を担います。
  - **Git**: ソースコードのバージョン管理システム（GitHubとの連携を前提）。
  - **GitHub API**: リポジトリ情報をプログラムで取得するためのインターフェースです。
- テスト:
  - **Pytest**: Pythonプロジェクトで広く使われるテストフレームワークで、コードの品質と信頼性を保証するために使用されます。
- ビルドツール:
  - 明示的なビルドツールはありませんが、Pythonスクリプトがコンテンツ生成の「ビルド」を担います。
- 言語機能:
  - **Python**: データ処理、API通信、ファイル操作、文字列処理など、多様なスクリプト機能を活用しています。
- 自動化・CI/CD:
  - 本プロジェクトはCI/CDを重視せず、ローカル開発での迅速なテスト・実行に焦点を当てています。
- 開発標準:
  - **Ruff**: Pythonコードの整形と静的解析を行うツールで、コードスタイルの一貫性と品質を保ちます。
  - **.editorconfig**: 複数の開発者やエディタ間で、インデントスタイルなどのコーディングスタイルを統一するための設定ファイルです。

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
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
  - **`check_large_files/`**: 大容量ファイルを検出する機能に関連するファイル群です。
    - **`README.md`**: `check_large_files` 機能についての説明文書です。
    - **`check-large-files.toml`**: `check_large_files` スクリプトの設定ファイルです。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定などを説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトルやテーマなどが定義されます。
- **`assets/`**: Jekyllサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能（`project_overview`）のデバッグやテストに使用されるPythonスクリプトです。
- **`generated-docs/`**: 生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: 生成されたリポジトリ一覧のMarkdownコンテンツが出力されるメインファイルです。Jekyllによってウェブページとして表示されます。
- **`issue-notes/`**: 開発中の特定の課題やメモを格納するディレクトリです。
  - **`22.md`**: 特定の課題（Issue #22）に関する詳細なメモファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示設定（名前、アイコンなど）を定義します。
- **`pytest.ini`**: Pytestフレームワークのテスト設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージのリストです。
- **`requirements.txt`**: プロジェクトの実行に最低限必要となるPythonパッケージのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのスタイルチェックツールRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
  - **`__init__.py`**: Pythonパッケージとして認識させるための空ファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成のロジックを格納するPythonパッケージです。
    - **`__init__.py`**: `generate_repo_list` パッケージとして認識させるための空ファイルです。
    - **`badge_generator.py`**: リポジトリのステータスを示すバッジ（例：アクティブ、アーカイブ）を生成するロジックを含みます。
    - **`config.yml`**: プロジェクトの主要な設定パラメータ（例：プロジェクト概要機能のON/OFF）を定義するYAMLファイルです。
    - **`config_manager.py`**: `config.yml` などの設定ファイルを読み込み、管理するロジックを提供します。
    - **`date_formatter.py`**: 日付や時刻をユーザーフレンドリーな形式に整形するロジックを含みます。
    - **`generate_repo_list.py`**: プロジェクトのエントリーポイント。GitHub APIから情報を取得し、Markdownを生成するメインスクリプトです。
    - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理するロジックです。
    - **`markdown_generator.py`**: 取得したリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを含みます。
    - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要（3行説明）を抽出するロジックです。
    - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルからバッジ情報を抽出するロジックです。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報のみを抽出・加工するロジックです。
    - **`seo_template.yml`**: 検索エンジン最適化（SEO）関連のテンプレート設定を定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するロジックを含みます。
    - **`strings.yml`**: ユーザーインターフェースに表示される各種メッセージや文言を一元管理するためのYAMLファイルです。
    - **`template_processor.py`**: Markdown生成の際に、テンプレートファイルとデータを組み合わせてコンテンツをレンダリングするロジックです。
    - **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview` 機能のユニットテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **`conftest.py`**: Pytestのテストフィクスチャや共通設定を定義するファイルです。
  - **`test_badge_generator_integration.py`**: `badge_generator` モジュールの結合テストです。
  - **`test_check_large_files.py`**: `check_large_files` スクリプトのテストです。
  - **`test_config.py`**: 設定ファイル読み込み・管理ロジックのテストです。
  - **`test_date_formatter.py`**: 日付整形ロジックのテストです。
  - **`test_environment.py`**: 実行環境のセットアップに関するテストです。
  - **`test_integration.py`**: 主要なコンポーネント間の結合テストです。
  - **`test_markdown_generator.py`**: Markdown生成ロジックのテストです。
  - **`test_project_overview_fetcher.py`**: `project_overview_fetcher` ロジックのテストです。
  - **`test_readme_badge_extractor.py`**: `readme_badge_extractor` ロジックのテストです。
  - **`test_repository_processor.py`**: リポジトリデータ処理ロジックのテストです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
  - **`main()`**: プロジェクトの主たる実行フローを定義します。コマンドライン引数を解析し、リポジトリ情報の取得、処理、そして最終的なMarkdownファイルの生成という一連の処理を調整します。
- **`src/generate_repo_list/repository_processor.py`**:
  - **`fetch_repositories(username, limit=None)`**: GitHub APIを通じて、指定されたユーザーのリポジトリ一覧を取得します。必要に応じて取得するリポジトリ数を制限できます。
  - **`process_repository_data(repo_data)`**: GitHub APIから取得した生のリポジトリデータ（辞書形式）を受け取り、システムで扱いやすい形に整形・加工します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
  - **`get_project_overview(repo_url, config)`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、設定に基づいてプロジェクトの3行概要説明を抽出します。
- **`src/generate_repo_list/markdown_generator.py`**:
  - **`generate_markdown(repositories, seo_data, strings)`**: 処理済みのリポジトリ情報とSEO関連データ、表示用文字列を基に、GitHub Pagesサイト用の最終的なMarkdownコンテンツ全体を生成します。
- **`src/generate_repo_list/badge_generator.py`**:
  - **`generate_badge_markdown(status)`**: リポジトリの現在のステータス（例: "active", "archived", "fork"）に応じて、Markdown形式の視覚的なバッジコードを生成します。
- **`src/generate_repo_list/config_manager.py`**:
  - **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
  - **`load_strings(strings_path)`**: 指定されたパスからYAML形式の文字列定義ファイルを読み込み、表示メッセージなどを辞書として提供します。
- **`src/generate_repo_list/date_formatter.py`**:
  - **`format_date(date_string)`**: ISO 8601形式などの日付文字列を受け取り、人間が読みやすい形式に整形して返します。
- **`src/generate_repo_list/language_info.py`**:
  - **`get_language_details(languages_url)`**: GitHub APIの言語情報エンドポイントURLから、リポジトリで使用されているプログラミング言語とその使用割合に関する詳細な情報を取得します。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
  - **`extract_badges(readme_content)`**: リポジトリのREADMEファイルのコンテンツから、埋め込まれたバッジ（例: Build Status）のURLやテキスト情報を解析して抽出します。
- **`src/generate_repo_list/statistics_calculator.py`**:
  - **`calculate_repo_statistics(repo_list)`**: 処理されたリポジトリのリストを受け取り、総スター数、言語分布などの集計統計情報を計算します。
- **`src/generate_repo_list/template_processor.py`**:
  - **`render_template(template_path, data)`**: 指定されたテンプレートファイルと、テンプレートに埋め込むべきデータを使用して、最終的なコンテンツ（例: HTMLスニペット）をレンダリングします。
- **`src/generate_repo_list/url_utils.py`**:
  - **`build_github_api_url(endpoint, username)`**: GitHub APIのエンドポイントパスとユーザー名から、完全なGitHub APIリクエストURLを構築します。
  - **`parse_github_url(repo_url)`**: GitHubリポジトリの公開URLから、リポジトリ所有者やリポジトリ名などの構成要素を解析して抽出します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-15 07:27:23 JST
