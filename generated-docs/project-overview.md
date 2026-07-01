Last updated: 2026-07-02

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得・整理するシステムです。
- 取得した情報から、検索エンジンに最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、GitHub PagesサイトのSEOとリポジトリの可視性を向上させ、情報アクセシビリティを改善します。

## 技術スタック
- フロントエンド: **Jekyll** - GitHub Pagesで使用される静的サイトジェネレーターで、生成されたMarkdownファイルを美しいWebサイトとして表示します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: プロジェクトの主要なロジックを実装するために使用されるプログラミング言語です。
    - **GitHub API**: リポジトリ情報（名前、説明、言語など）をプログラムから取得するために利用されます。
- テスト:
    - **pytest**: Pythonアプリケーションのテストを効率的に記述・実行するためのフレームワークです。
- ビルドツール:
    - **Python実行環境**: リポジトリ情報の取得、処理、Markdown生成といった一連の「ビルド」プロセスを実行します。
- 言語機能:
    - **Python**: オブジェクト指向プログラミング、強力な標準ライブラリ、読みやすい構文により、システムの開発効率を高めます。
- 自動化・CI/CD:
    - **Pythonスクリプトによる自動生成**: ローカル環境でのスクリプト実行により、リポジトリ一覧の自動生成を実現します。
- 開発標準:
    - **ruff**: Pythonコードのフォーマットとリンティングを自動的に行い、コードの一貫性と品質を保ちます。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/check_large_files/`**: GitHub Actionsで実行される可能性のある、大規模ファイルをチェックするための自動化スクリプト群。
    - **`README.md`**: この自動化スクリプトに関する説明ドキュメント。
    - **`check-large-files.toml`**: 大容量ファイルチェックの構成設定ファイル。
    - **`scripts/check_large_files.py`**: 実際に大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などを説明するメインのドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどを定義します。
- **`assets/`**: ウェブサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン画像ファイル。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグやテストを目的としたスクリプト。
- **`generated-docs/`**: `generated-docs/project-overview.md`など、自動生成されたドキュメントを格納するためのプレースホルダーディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイル。
- **`index.md`**: `generate_repo_list.py`によってリポジトリ一覧が生成・出力されるメインのMarkdownファイル。Jekyllによってウェブページとして変換されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記録したMarkdownファイル。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイル。プログレッシブウェブアプリ（PWA）として動作するための情報（アイコン、表示モードなど）を提供します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイル。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリをリストアップしたファイル。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonライブラリをリストアップしたファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: `ruff`コードリンター/フォーマッターの設定ファイル。Pythonコードのスタイルガイドやルールを定義します。
- **`src/__init__.py`**: Pythonパッケージであることを示す空ファイル。
- **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックが格納されているPythonパッケージ。
    - **`__init__.py`**: Pythonサブパッケージであることを示す空ファイル。
    - **`badge_generator.py`**: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）に応じたバッジのMarkdownを生成するロジックを扱います。
    - **`config.yml`**: プロジェクト概要取得機能やGitHub API関連の技術的なパラメータを設定するファイル。
    - **`config_manager.py`**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのモジュール。
    - **`date_formatter.py`**: リポジトリの更新日時などの日付情報を整形するためのユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからの情報取得、処理、Markdown生成までの一連のワークフローを制御します。
    - **`json_ld_template.json`**: 検索エンジン最適化のために、JSON-LD形式の構造化データを出力するためのテンプレートファイル。
    - **`language_info.py`**: リポジトリの主要なプログラミング言語に関する情報を処理・表示するためのロジックを扱います。
    - **`markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なMarkdown形式のリポジトリ一覧文字列を生成します。
    - **`project_overview_fetcher.py`**: 各リポジトリ内の`generated-docs/project-overview.md`から3行のプロジェクト概要を抽出する機能を提供します。
    - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するモジュール。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを担います。
    - **`seo_template.yml`**: SEO関連のメタデータや、ウェブページのヘッダーに埋め込むためのテンプレート設定を定義します。
    - **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算するためのモジュール。
    - **`strings.yml`**: ウェブページや生成されるMarkdown内で使用される各種表示メッセージや文言を一元管理するファイル。
    - **`template_processor.py`**: マークダウンやHTMLテンプレートの変数を実際のデータで置き換えるなど、テンプレート処理全般を担います。
    - **`url_utils.py`**: URLの生成、検証、整形など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストや統合テストを含むファイル。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`test_config.py`**: 設定ファイルの読み込み・管理に関するテスト。
    - **`test_date_formatter.py`**: 日付整形機能のテスト。
    - **`test_environment.py`**: 実行環境に関するテスト。
    - **`test_integration.py`**: プロジェクト全体の主要な統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテスト。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: メイン処理のエントリーポイント。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、加工し、Markdownファイルを生成する一連のプロセスをオーケストレートします。
- **`src/generate_repo_list/repository_processor.py`**:
    - `fetch_repositories(username, limit=None, token=None)`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIから取得します。`limit`で取得数を制限し、`token`で認証を行います。
    - `process_repository(repo_data, config, strings, project_overview_fetcher)`: GitHub APIから取得した単一のリポジトリデータを受け取り、表示に必要な情報（概要、バッジ、言語など）を抽出し、整形された辞書形式で返します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_markdown(processed_repos, strings, config)`: 処理済みのリポジトリ情報のリストを受け取り、これらを整形して最終的なMarkdown文字列として生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `get_project_overview(repo_name, owner, target_file, section_title, config)`: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、特定のセクション（例: "プロジェクト概要"）の3行の説明をフェッチします。
- **`src/generate_repo_list/badge_generator.py`**:
    - `create_badge_markdown(status, badge_type='status')`: リポジトリのステータス（例: "アクティブ"、"アーカイブ"）に応じたバッジのMarkdown構文を生成します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(config_path)`: 指定されたパスにあるYAML形式の設定ファイルを読み込み、辞書オブジェクトとして返します。
    - `load_strings(strings_path)`: 指定されたパスにあるYAML形式の文字列定義ファイルを読み込み、辞書オブジェクトとして返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-02 07:32:33 JST
