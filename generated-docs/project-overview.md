Last updated: 2026-07-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得します。
- GitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdownで生成します。
- 検索エンジンのクロールとLLMによるリポジトリ参照性を向上させ、情報発見を支援します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として静的サイトを構築), **Markdown** (リポジトリ一覧のコンテンツ生成形式), **HTML/CSS** (Jekyllによって生成されるウェブページの構造とスタイル)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: **Python** (主要なスクリプト言語), **GitHub API** (リポジトリ情報の取得), **Git** (バージョン管理システム)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストフレームワーク)
- ビルドツール: **Jekyll** (GitHub Pagesサイトのビルドプロセスを担う)
- 言語機能: **Python** (アプリケーションのロジックを実装), **YAML** (設定ファイル `config.yml`, `strings.yml`, `seo_template.yml` で使用), **TOML** (設定ファイル `secrets.toml`, `check-large-files.toml` で使用), **JSON** (JSON-LDテンプレートなどで使用)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリ内のスクリプトや設定から推測される継続的インテグレーション/デリバリーの自動化機能), **GitHub API** (各種自動化プロセスでリポジトリ情報にアクセス)
- 開発標準: **ruff** (Pythonコードの高速リンターおよびフォーマッター), **EditorConfig** (`.editorconfig` により異なるエディタ間でのコードスタイル統一を支援)

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
- **`.editorconfig`**: 異なるIDEやエディタ間で、インデントスタイルや文字コードなどのコード整形ルールを統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理しないファイルやディレクトリを指定するファイルです。一時ファイルやログファイルなどをリポジトリから除外します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。プロジェクトの使用、配布、変更条件を定めます。
- **`README.md`**: プロジェクトの概要、目的、主な機能、開発者向けヒント、クイックテスト方法、設定ファイル、コマンド例などを説明する、リポジトリの顔となるファイルです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどの基本設定が含まれます。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` のデバッグやテストに特化したスクリプトであると推測されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。本システムによってリポジトリ一覧がこのファイルに自動生成されます。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルです。アプリの表示情報（名前、アイコン、表示モードなど）や動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonの依存パッケージをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行する際に必要となるPythonの依存パッケージをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイト内でクロールを許可または禁止する範囲を伝えるファイルです。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターである `ruff` の設定ファイルです。コードのスタイルや品質に関するルールを定義します。
- **`test_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテストコードです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明です。
    - **`check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像ファイル群です。
- **`generated-docs/`**: `project-overview.md` など、このシステムが自動生成したドキュメントを格納するためのプレースホルダー的なディレクトリです。
- **`issue-notes/`**: 開発中に検討された課題や決定事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（Issue #22）に関するメモです。
- **`src/`**: プロジェクトの主要なPythonソースコードが格納されるルートディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` がPythonパッケージであることを示すファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示する言語バッジやステータスバッジなどを生成する機能を提供します。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成システムの動作に関する詳細な設定（例：プロジェクト概要取得機能のON/OFF、対象ファイルパス、タイムアウト設定など）を定義します。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml` や `secrets.toml` など、プロジェクトで使用される各種設定ファイルを読み込み、管理するためのユーティリティ機能を提供します。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式に整形する機能を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、その情報を元にMarkdown形式のリポジトリ一覧を生成する一連の処理を統括します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用される、JSON-LD形式の構造化データテンプレートを定義します。
        - **`src/generate_repo_list/language_info.py`**: GitHub APIから取得した各リポジトリの言語情報を処理し、表示に適した形式に整形する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、GitHub Pages向けのMarkdownコンテンツを生成する主要な機能を提供します。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動で抽出し、取得する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、特定のパターンに合致するバッジ情報（例：ビルドステータス、カバレッジなど）を抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、このプロジェクトで利用しやすい内部データ構造に変換し、必要な情報を抽出・加工する機能を提供します。
        - **`src/generate_repo_list/seo_template.yml`**: リポジトリ一覧ページに適用されるSEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリの統計情報（例：スター数の合計、言語ごとの分布など）を計算する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言を集中管理するYAMLファイルです。多言語対応や文言の一貫性維持に貢献します。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用される各種テンプレートファイルを読み込み、動的なデータ（リポジトリ情報など）を埋め込んで最終的なコンテンツをレンダリングする機能を提供します。
        - **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリのURL構築や、その他のURL関連のユーティリティ関数を提供します。
- **`tests/`**: プロジェクトのテストコードを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest` のテスト実行におけるフィクスチャ（テストデータを準備する関数）や共通設定を定義するファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator.py` の統合テストです。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`tests/test_config.py`**: 設定ファイルの読み込み・管理機能 (`config_manager.py`) のテストです。
    - **`tests/test_date_formatter.py`**: 日付整形機能 (`date_formatter.py`) のテストです。
    - **`tests/test_environment.py`**: テスト実行環境に関するテストです。
    - **`tests/test_integration.py`**: システム全体の主要なフローに関する統合テストです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能 (`markdown_generator.py`) のテストです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテストです。
    - **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能 (`readme_badge_extractor.py`) のテストです。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能 (`repository_processor.py`) のテストです。

## 関数詳細説明
このプロジェクトの情報からは、各関数の引数、戻り値、具体的な内部実装を詳細に分析することはできませんでした。
しかし、各ファイルの役割から、以下の主要な機能を持つ関数群が存在すると推測されます。

- **`src/generate_repo_list/badge_generator.py`**: リポジトリの状態や言語を示すバッジ（例: `generate_language_badge`, `generate_status_badge` など）を生成する関数。
- **`src/generate_repo_list/config_manager.py`**: YAMLやTOML形式の設定ファイルを読み込み、設定値を取得する関数（例: `load_config`, `get_secret` など）。
- **`src/generate_repo_list/date_formatter.py`**: 日付オブジェクトを指定されたフォーマットの文字列に変換したり、相対時間を計算したりする関数（例: `format_date`, `format_time_ago` など）。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの全体的なフローを制御し、GitHub APIからのデータ取得、処理、Markdown生成までの一連のタスクを実行するメイン関数（例: `main`, `generate_repository_list` など）。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報を取得し、表示用に処理する関数（例: `get_repository_languages` など）。
- **`src/generate_repo_list/markdown_generator.py`**: リポジトリ情報をもとに、タイトル、説明、バッジ、リンクなどを含むMarkdown形式の文字列を構築する関数（例: `generate_repo_markdown`, `generate_index_page` など）。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 特定のファイルパスから「プロジェクト概要」セクションのテキストを抽出・取得する関数（例: `fetch_project_overview` など）。
- **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルの内容から、特定の正規表現パターンに合致するバッジURLやテキストを抽出する関数（例: `extract_badges` など）。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON）を解析し、必要な情報を抽出・加工して内部モデルにマッピングする関数（例: `process_repository_data`, `get_repo_details` など）。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリ群の合計スター数、言語使用率などの統計情報を計算する関数（例: `calculate_overall_statistics` など）。
- **`src/generate_repo_list/template_processor.py`**: テンプレートファイル（MarkdownやHTMLなど）を読み込み、プレースホルダーを実際のデータで置き換えて最終的な出力テキストを生成する関数（例: `render_template` など）。
- **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリやプロフィールへのURLを生成するユーティリティ関数（例: `build_github_repo_url`, `build_user_profile_url` など）。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: 設定ファイルに基づき、リポジトリ内の指定されたしきい値を超えるサイズのファイルを検出する関数（例: `check_files_for_size` など）。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-19 07:20:02 JST
