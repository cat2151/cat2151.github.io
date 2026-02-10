Last updated: 2026-02-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・処理するシステムです。
- GitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- 検索エンジンからのクロールを促進し、各リポジトリの認知度向上とLLM連携の改善を目指します。

## 技術スタック
- フロントエンド: JekyllベースのGitHub Pages (生成されたMarkdownを表示), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし（本プロジェクトではオーディオ関連技術は使用していません）
- 開発ツール: Python (主要なスクリプト言語), Pytest (Python用テストフレームワーク), Ruff (Pythonコードの自動フォーマット・リンティングツール), `requirements.txt` (プロジェクトの依存ライブラリを管理), `config.yml` (各種設定パラメータを管理), `strings.yml` (表示メッセージや文言を管理)
- テスト: Pytest (ユニットテストおよび統合テストの実行)
- ビルドツール: Pythonスクリプト (Markdownファイルを生成), Jekyll (GitHub PagesがMarkdownを静的サイトとしてビルド・表示)
- 言語機能: Python (バージョン3.xの標準機能を使用)
- 自動化・CI/CD: Pythonスクリプトによる自動生成 (GitHub APIからの情報取得からMarkdown生成までを自動化。CI/CDパイプラインはプロジェクトの性質上、ローカル開発が重視されており、明示的には組み込まれていません。)
- 開発標準: Ruff (コードの一貫性を保つためのリンティングとフォーマット), .editorconfig (複数の開発環境で一貫したコードスタイルを強制)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
  📖 4.md
  📖 6.md
  📖 8.md
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

*   **.editorconfig**: 各種エディタでコードのインデントや文字コードなどの設定を統一するためのファイルです。
*   **.github_automation/**: GitHub Actionsなど、リポジトリ自動化に関連するスクリプトや設定を格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルがないかをチェックするためのスクリプト群を格納しています。
        *   `README.md`: `check_large_files` 機能の説明ドキュメントです。
        *   `check-large-files.toml`: 大容量ファイルチェックの設定ファイルです。
        *   `scripts/check_large_files.py`: 実際に大容量ファイルをチェックするPythonスクリプトです。
*   **.gitignore**: Gitが追跡しないファイルやディレクトリを指定する設定ファイルです。
*   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
*   **README.md**: プロジェクト全体の概要、セットアップ方法、使用方法などが記述されたメインドキュメントです。
*   `_config.yml`: Jekyllサイト全体の共通設定ファイルです。GitHub Pagesの基本的な動作を制御します。
*   **assets/**: GitHub Pagesサイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
*   `debug_project_overview.py`: `project_overview` 機能のデバッグ用スクリプトです。
*   `generated-docs/`: 他のリポジトリから取得したドキュメントや、生成された一時ファイルなどを格納するディレクトリです。
*   `googled947dc864c270e07.html`: Googleサイト所有権確認用のファイルです。
*   `index.md`: 本プロジェクトによって生成される、GitHub Pagesサイトのリポジトリ一覧が記述されるメインのMarkdownファイルです。
*   **issue-notes/**: 課題や検討事項に関するメモをMarkdown形式で保存しているディレクトリです。
*   `manifest.json`: Webアプリケーションマニフェストファイルで、PWA（Progressive Web App）の設定を定義します。
*   `pytest.ini`: Pytestの設定ファイルです。テスト実行時の挙動をカスタマイズします。
*   `requirements-dev.txt`: 開発およびテストに必要なPythonパッケージの依存関係を記述したファイルです。
*   `requirements.txt`: 本番環境でプロジェクトを実行するために必要なPythonパッケージの依存関係を記述したファイルです。
*   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またクロールすべきでないかを指示するファイルです。
*   `ruff.toml`: Ruff（Pythonリンター/フォーマッター）の設定ファイルです。コードスタイルのルールを定義します。
*   **src/**: プロジェクトのソースコードを格納するメインディレクトリです。
    *   `__init__.py`: Pythonパッケージであることを示すファイルです。
    *   **generate_repo_list/**: リポジトリ一覧生成の主要ロジックを含むサブパッケージです。
        *   `__init__.py`: Pythonサブパッケージであることを示すファイルです。
        *   `badge_generator.py`: リポジトリのバッジ（例: 言語バッジ、ステータスバッジ）のMarkdownを生成するロジックを扱います。
        *   `config.yml`: `generate_repo_list` スクリプト固有の設定（GitHub APIトークンの場所、プロジェクト概要取得機能の有効/無効など）を定義します。
        *   `config_manager.py`: `config.yml` や他の設定ファイルを読み込み、管理するためのモジュールです。
        *   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        *   `generate_repo_list.py`: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体を統括します。
        *   `json_ld_template.json`: SEO強化のためのJSON-LDデータのテンプレートです。
        *   `language_info.py`: リポジトリのプログラミング言語に関する情報を処理し、統計を計算するモジュールです。
        *   `markdown_generator.py`: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを担います。
        *   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するモジュールです。
        *   `readme_badge_extractor.py`: READMEファイルから既存のバッジ情報を抽出する機能を提供します。
        *   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出・加工する役割を担います。
        *   `seo_template.yml`: SEO関連のメタデータやコンテンツのテンプレートを定義します。
        *   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算するモジュールです。
        *   `strings.yml`: UIの表示テキスト、メッセージ、文言などを一元的に管理するためのファイルです。
        *   `template_processor.py`: テンプレートファイル（例: Markdownテンプレート）を読み込み、データに基づいてレンダリングする機能を提供します。
        *   `url_utils.py`: URLの生成や解析など、URL関連のユーティリティ関数を提供します。
*   `test_project_overview.py`: `project_overview_fetcher` 機能に関するテストスクリプトです。
*   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    *   `test_badge_generator_integration.py`: バッジ生成の統合テストです。
    *   `test_check_large_files.py`: 大容量ファイルチェック機能のテストです。
    *   `test_config.py`: 設定ファイル読み込み・管理機能のテストです。
    *   `test_date_formatter.py`: 日付整形機能のテストです。
    *   `test_environment.py`: 実行環境に関するテストです。
    *   `test_integration.py`: 主要機能間の統合テストです。
    *   `test_markdown_generator.py`: Markdown生成機能のテストです。
    *   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストです。
    *   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストです。
    *   `test_repository_processor.py`: リポジトリデータ処理機能のテストです。

## 関数詳細説明

**本プロジェクト情報からは具体的な引数や戻り値の形式を詳細に特定できないため、各関数の役割と機能に焦点を当てて説明します。**

*   **`src/generate_repo_list/generate_repo_list.py`**:
    *   `main()`:
        *   役割: コマンドラインからの実行時に呼ばれるエントリーポイント。
        *   機能: コマンドライン引数を解析し、リポジトリ一覧生成の主要処理をキックします。
    *   `generate_repo_list(username, output_file, limit=None)` (推定):
        *   役割: 指定されたユーザーのリポジトリ情報を取得し、Markdown形式で一覧ファイルを生成する主要な処理を実行します。
        *   機能: GitHub APIからのデータ取得、リポジトリ情報の整形、プロジェクト概要のフェッチ、Markdown生成などの各サブモジュールを連携させ、最終的な出力ファイルを生成します。

*   **`src/generate_repo_list/config_manager.py`**:
    *   `load_config(config_path)` (推定):
        *   役割: 指定されたパスからYAML形式の設定ファイルを読み込みます。
        *   機能: 設定ファイルの内容をPythonのデータ構造（辞書など）として提供します。
    *   `get_setting(key, default=None)` (推定):
        *   役割: 読み込んだ設定から特定のキーに対応する値を取得します。
        *   機能: 設定の取得を抽象化し、デフォルト値も指定できるようにします。

*   **`src/generate_repo_list/project_overview_fetcher.py`**:
    *   `fetch_project_overview(repo_url, target_file, section_title, config)` (推定):
        *   役割: 特定のリポジトリ内にある指定ファイルから、プロジェクト概要の3行説明を抽出します。
        *   機能: HTTPリクエストでファイルを読み込み、指定されたセクションから該当するテキスト行をパースして返します。

*   **`src/generate_repo_list/markdown_generator.py`**:
    *   `generate_markdown(repo_data, template_config)` (推定):
        *   役割: 処理されたリポジトリデータとテンプレート設定に基づき、Markdown形式の文字列を生成します。
        *   機能: リポジトリごとの情報（名前、説明、URL、バッジ、プロジェクト概要など）を構造化し、Markdownシンタックスに変換して出力します。

*   **`src/generate_repo_list/repository_processor.py`**:
    *   `process_repository_data(raw_repo_list, api_client, config)` (推定):
        *   役割: GitHub APIから取得した生のリポジトリデータリストを、アプリケーションで利用しやすい形式に整形・加工します。
        *   機能: 各リポジトリの必要な情報を抽出し、分類（アクティブ、アーカイブ、フォークなど）、追加データ（プロジェクト概要、言語統計など）のフェッチを調整します。

*   **`src/generate_repo_list/badge_generator.py`**:
    *   `generate_badge_markdown(badge_type, value)` (推定):
        *   役割: 指定された種類と値に基づいて、バッジのMarkdown文字列を生成します。
        *   機能: リポジトリの言語やステータスなどを視覚的に表現するバッジをMarkdownとして出力します。

*   **`src/generate_repo_list/date_formatter.py`**:
    *   `format_date(datetime_obj, format_string)` (推定):
        *   役割: 日付/時刻オブジェクトを特定のフォーマット文字列に従って整形します。
        *   機能: リポジトリの最終更新日時などを、人間が読みやすい形式に変換します。

*   **`src/generate_repo_list/language_info.py`**:
    *   `get_language_statistics(repo_name, api_client)` (推定):
        *   役割: 特定のリポジトリで使用されているプログラミング言語とその割合に関する統計情報を取得します。
        *   機能: GitHub APIを利用して言語データを取得し、使用量の多い順に並べるなどの処理を行います。

*   **`src/generate_repo_list/readme_badge_extractor.py`**:
    *   `extract_badges_from_readme(readme_content)` (推定):
        *   役割: READMEファイルのコンテンツから既存のバッジ（画像リンク）を抽出します。
        *   機能: 正規表現などを用いて、READMEに埋め込まれたバッジのURLやタイトルを取得します。

*   **`src/generate_repo_list/statistics_calculator.py`**:
    *   `calculate_repository_statistics(repo_list)` (推定):
        *   役割: リポジトリ一覧全体の統計情報（例: 総リポジトリ数、言語分布）を計算します。
        *   機能: 提供されたリポジトリデータに基づいて集計を行い、概要統計を提供します。

*   **`src/generate_repo_list/template_processor.py`**:
    *   `render_template(template_path, context_data)` (推定):
        *   役割: 指定されたテンプレートファイルにコンテキストデータを適用してレンダリングします。
        *   機能: Jekyllのテンプレートや他の汎用テンプレートにデータを流し込み、最終的な文字列を生成します。

*   **`src/generate_repo_list/url_utils.py`**:
    *   `build_repo_url(username, repo_name)` (推定):
        *   役割: GitHubリポジトリのURLを構築します。
        *   機能: ユーザー名とリポジトリ名から正確なGitHub URLを生成します。

*   **`.github_automation/check_large_files/scripts/check_large_files.py`**:
    *   `main()` (推定):
        *   役割: 大容量ファイルチェックスクリプトのエントリーポイント。
        *   機能: リポジトリ内のファイルを走査し、設定された閾値を超える大容量ファイルがないかをチェックします。

*   その他のファイル（例: `__init__.py`, `googled947dc864c270e07.html`, `config.yml`, `strings.yml`, `json_ld_template.json`, `seo_template.yml`, `pytest.ini`, `ruff.toml` など）には、直接実行される関数は含まれていないか、データ定義が主です。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-02-11 07:17:37 JST
