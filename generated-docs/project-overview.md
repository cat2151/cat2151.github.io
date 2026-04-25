Last updated: 2026-04-26

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を取得してGitHub Pagesサイト向けにMarkdownを自動生成するシステムです。
- SEOを最適化し、リポジトリ一覧や各リポジトリへのリンクを含むページを作成することで検索エンジンによるインデックスを促進します。
- これにより、GitHubユーザーページのSEO課題や、LLMがリポジトリ参照に失敗する問題を緩和することを目指します。

## 技術スタック
- フロントエンド: **Jekyll / GitHub Pages** (生成されたMarkdownファイルを静的サイトとして公開するための基盤)
- 音楽・オーディオ: (該当なし)
- 開発ツール: **Ruff** (Pythonコードのフォーマットとリントを高速に行うツール)、**pytest** (Python向けのテストフレームワーク)
- テスト: **pytest** (ユニットテストおよび統合テストの実行に利用)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報の取得、Markdownの生成、各種処理のオーケストレーションを行うカスタムビルドロジック)
- 言語機能: **Python** (プロジェクトの主要な開発言語)
- 自動化・CI/CD: (このプロジェクト自体が「自動生成」を行うシステムであり、明示的なCI/CDツールは記述されていません。ただし、GitHub Actionsからの呼び出しが想定されます)
- 開発標準: **Ruff** (コードスタイルの一貫性を保ち、品質を向上させるためのツール)

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
-   `.editorconfig`: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）の一貫性を定義するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   `check_large_files/README.md`: 大容量ファイルチェック自動化機能の説明ドキュメントです。
    -   `check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルです。
    -   `scripts/check_large_files.py`: 指定されたリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitによるバージョン管理から除外するファイルやディレクトリを指定する設定ファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けヒントなどをまとめた主要なドキュメントファイルです。
-   `_config.yml`: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesの挙動を制御します。
-   `assets/`: ウェブサイトのファビコンやその他の静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン画像ファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher` 機能のデバッグを目的としたPythonスクリプトです。
-   `generated-docs/`: 他のリポジトリから取得した `project-overview.md` など、自動生成または参照されるドキュメントを一時的に格納する、あるいは参照元となるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
-   `index.md`: メインの生成物であり、GitHub Pagesのトップページとして機能するリポジトリ一覧のMarkdownファイルです。
-   `issue-notes/`: 開発中の課題、メモ、検討事項などを管理するためのMarkdownファイル群を格納するディレクトリです。
    -   `22.md`: 特定の課題またはメモの内容を記述したMarkdownファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）としてサイトを定義するためのメタデータファイルです。アプリ名、アイコン、表示モードなどを指定します。
-   `pytest.ini`: `pytest` テストフレームワークの設定ファイルです。テスト実行オプションやプラグインなどを定義します。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonの依存パッケージとそのバージョンを記載したファイルです。
-   `requirements.txt`: 本番運用（またはスクリプト実行）に必要なPythonの依存パッケージとそのバージョンを記載したファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロール・インデックスすべきか、または避けるべきかを指示するファイルです。
-   `ruff.toml`: Ruffリンターの設定ファイルです。コードスタイルのルール、無視するファイル、検出する問題などを定義します。
-   `src/`: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
    -   `__init__.py`: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリ一覧生成ロジックを構成するモジュール群を格納するパッケージです。
        -   `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ画像を生成または処理する機能を提供します。
        -   `config.yml`: プロジェクト概要取得機能など、本システム固有の設定パラメータを定義するYAMLファイルです。
        -   `config_manager.py`: `config.yml` やその他の設定ファイルを読み込み、設定値を管理するためのモジュールです。
        -   `date_formatter.py`: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: リポジトリ一覧を生成するメインのエントリスクリプトです。GitHub APIからのデータ取得、処理、Markdown生成までの一連の流れを統括します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために構造化データを埋め込むJSON-LDのテンプレートファイルです。
        -   `language_info.py`: GitHubリポジトリの言語情報を解析し、表示に適した形式に処理する機能を提供します。
        -   `markdown_generator.py`: 取得したリポジトリ情報や処理結果に基づいて、Markdown形式のコンテンツを生成する機能を提供します。
        -   `project_overview_fetcher.py`: 各リポジトリから `generated-docs/project-overview.md` ファイルの内容を自動取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、必要な形式に加工・処理するロジックをカプセル化します。
        -   `seo_template.yml`: Markdown生成時に利用されるSEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        -   `strings.yml`: UIに表示されるメッセージや文言、定数などを一元管理するためのYAMLファイルです。国際化・ローカライズ対応に利用されます。
        -   `template_processor.py`: Markdownなどのテンプレートファイルを読み込み、動的なデータを差し込んで最終的なコンテンツを生成する機能を提供します。
        -   `url_utils.py`: URLの操作、解析、生成に関するユーティリティ関数をまとめたモジュールです。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールの機能（特にプロジェクト概要の取得）をテストするためのスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest` のフィクスチャ（テストヘルパー）や設定を定義するためのファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator` モジュールの統合テストを行うスクリプトです。
    -   `test_check_large_files.py`: `.github_automation/check_large_files/scripts/check_large_files.py` のテストスクリプトです。
    -   `test_config.py`: 設定ファイル読み込み・管理機能 (`config_manager.py` など) のテストスクリプトです。
    -   `test_date_formatter.py`: `date_formatter` モジュールの機能（日付整形）をテストするスクリプトです。
    -   `test_environment.py`: テスト環境の設定や依存関係が正しく機能するかを確認するスクリプトです。
    -   `test_integration.py`: プロジェクトの主要なコンポーネントが連携して正しく動作するかを確認する統合テストスクリプトです。
    -   `test_markdown_generator.py`: `markdown_generator` モジュールの機能（Markdown生成）をテストするスクリプトです。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールの機能（プロジェクト概要取得）をテストするスクリプトです。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールの機能（READMEからのバッジ抽出）をテストするスクリプトです。
    -   `test_repository_processor.py`: `repository_processor` モジュールの機能（リポジトリデータ処理）をテストするスクリプトです。

## 関数詳細説明
このプロジェクトでは、主要なPythonスクリプトファイル (`.py` 拡張子を持つファイル) 内に多数の関数が存在します。具体的な引数や戻り値はコードの解析が必要ですが、ファイル名とその役割から推測される主な関数の機能は以下の通りです。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: プログラムのエントリポイントとなる関数で、コマンドライン引数を解析し、リポジトリ情報の取得からMarkdown生成までの一連の処理をオーケストレーションします。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(...)`: 指定された情報（例：言語、ステータス）に基づいて、リポジトリ用のバッジ文字列（または画像パス）を生成する関数群です。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(config_path)`: 指定されたパスから設定ファイル（例：`config.yml`）を読み込み、設定オブジェクトを返す関数です。
    -   `get_setting(key)`: 読み込まれた設定から特定のキーに対応する値を取得する関数です。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_date(datetime_obj, format_str)`: 日付/時刻オブジェクトを指定された文字列形式に整形する関数です。
    -   `get_human_readable_time_ago(datetime_obj)`: 特定の日付が「X日前」のような人間が読みやすい形式に変換する関数です。
-   **`src/generate_repo_list/language_info.py`**:
    -   `get_language_data(repo_data)`: リポジトリの言語情報（使用割合など）を抽出し、整理する関数です。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repo_markdown(repo_data)`: 単一のリポジトリ情報から、そのリポジトリ表示用のMarkdownスニペットを生成する関数です。
    -   `generate_index_markdown(repo_list)`: 複数のリポジトリデータから、リポジトリ一覧全体のMarkdownファイルコンテンツを生成する関数です。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリURLから、`generated-docs/project-overview.md` ファイルの内容をフェッチし、概要部分を抽出する関数です。
-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   `extract_badges_from_readme(readme_content)`: READMEのテキストコンテンツから、バッジ（例：Shields.io形式）のURLや情報を抽出する関数です。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository(repo_raw_data, github_token)`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出し、整形する関数です。これには、概要取得やバッジ抽出などのサブルーチン呼び出しが含まれます。
    -   `get_user_repositories(username, github_token)`: 指定されたユーザー名でGitHub APIを呼び出し、リポジトリのリストを取得する関数です。
-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   `calculate_repo_statistics(repo_data)`: リポジトリのスター数、フォーク数などの統計情報を計算または集計する関数です。
-   **`src/generate_repo_list/template_processor.py`**:
    -   `render_template(template_path, data)`: 指定されたテンプレートファイル（例：Markdownテンプレート）にデータ（変数）を埋め込んで最終的な文字列を生成する関数です。
-   **`src/generate_repo_list/url_utils.py`**:
    -   `build_github_api_url(username, repo_name)`: GitHub APIのエンドポイントURLを構築するユーティリティ関数です。
    -   `parse_github_url(url)`: GitHubのリポジトリURLを解析し、ユーザー名やリポジトリ名などのコンポーネントを抽出する関数です。
-   **`_automation/check_large_files/scripts/check_large_files.py`**:
    -   `main()`: 大容量ファイルチェックスクリプトのエントリポイントで、設定に基づいてリポジトリ内のファイルをチェックし、閾値を超えるファイルを報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-26 07:12:57 JST
