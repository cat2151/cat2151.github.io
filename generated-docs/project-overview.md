Last updated: 2026-03-21

# Project Overview

## プロジェクト概要
- GitHub Pages向けリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Markdownを生成します。
- SEOを意識した出力で、リポジトリの検索エンジンからの発見性を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的コンテンツ生成と表示に利用)
- 音楽・オーディオ: (該当なし)
- 開発ツール:
    - Python: メインのスクリプト言語として、リポジトリ情報の取得とMarkdown生成に利用。
    - Ruff: Pythonコードのスタイルチェックと自動整形ツール。
    - pytest: Pythonプロジェクトの単体テストおよび結合テストフレームワーク。
- テスト:
    - pytest: テストコードの実行と結果検証に利用。
- ビルドツール:
    - Pythonスクリプト: GitHub APIからのデータ取得、加工、Markdownファイルへの出力というビルドプロセスを実行。
    - Jekyll: GitHub PagesサイトとしてMarkdownファイルを静的サイトに変換・表示。
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語。
- 自動化・CI/CD:
    - GitHub Automation: `.github_automation` ディレクトリ配下に自動化スクリプトを配置。
- 開発標準:
    - Ruff: コード品質の維持と統一されたコーディングスタイルを強制するために利用。
    - .editorconfig: 複数のエディタで一貫したコーディングスタイルを維持するための設定ファイル。

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
-   `.editorconfig`: 異なるエディタやIDE間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリです。
    -   `check_large_files/README.md`: 大容量ファイルチェック機能に関する説明文書です。
    -   `check_large_files/check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルです。
    -   `check_large_files/scripts/check_large_files.py`: 指定された閾値を超える大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理システムで、特定のファイルやディレクトリを追跡対象から除外するための設定ファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイルです。
-   `README.md`: プロジェクトの概要、目的、主な機能、クイックスタートガイド、開発者向けヒントなどを記述したメインのドキュメントです。
-   `_config.yml`: Jekyllサイト全体の設定を定義するファイルで、サイトのタイトル、テーマ、プラグインなどの情報を保持します。
-   `assets/`: GitHub Pagesサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher`機能のデバッグや単体テストを目的としたスクリプトです。
-   `generated-docs/`: プロジェクトによって自動生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのウェブマスターツールでサイトの所有権を証明するために使用される認証ファイルです。
-   `index.md`: GitHub Pagesサイトのルートページとして機能するMarkdownファイルで、自動生成されたリポジトリ一覧が出力されます。
-   `issue-notes/`: 課題や検討事項に関するノートを整理して格納するディレクトリです。
    -   `issue-notes/22.md`: 特定の課題（例：Issue #22）に関する詳細なメモや考察を記述したファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリの名前、アイコン、表示設定などを定義するJSONファイルです。
-   `pytest.ini`: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイルです。
-   `requirements-dev.txt`: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `requirements.txt`: プロジェクトが本番稼働するために最低限必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイルです。
-   `ruff.toml`: `Ruff` linterのルールや設定を定義するTOML形式の設定ファイルです。
-   `src/__init__.py`: `src`ディレクトリがPythonパッケージであることを示すファイルです。
-   `src/generate_repo_list/__init__.py`: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
-   `src/generate_repo_list/badge_generator.py`: リポジトリの各種情報（言語、ライセンスなど）に基づいて、視覚的なバッジ画像を生成するロジックを実装しています。
-   `src/generate_repo_list/config.yml`: リポジトリ一覧生成機能に関連する各種技術的パラメータ（例：プロジェクト概要取得機能の有効/無効、対象ファイルなど）を設定するYAMLファイルです。
-   `src/generate_repo_list/config_manager.py`: `config.yml`や`strings.yml`などの設定ファイルを読み込み、アプリケーション全体でアクセス可能な形で管理する機能を提供します。
-   `src/generate_repo_list/date_formatter.py`: GitHub APIから取得した日付や時刻データを、読みやすい形式に整形するユーティリティ関数を提供します。
-   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのメイン実行スクリプト。GitHub APIを介してリポジトリ情報を取得し、他のモジュールと連携してMarkdownファイルを生成します。
-   `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化（SEO）のために、構造化データをJSON-LD形式で記述するためのテンプレートファイルです。
-   `src/generate_repo_list/language_info.py`: リポジトリの主要言語や言語の使用状況に関する情報を処理し、Markdown出力に適した形式に変換する機能を提供します。
-   `src/generate_repo_list/markdown_generator.py`: 処理されたリポジトリデータに基づいて、JekyllのMarkdown形式に準拠したコンテンツを生成するロジックを実装しています。
-   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出・取得する機能を提供します。
-   `src/generate_repo_list/readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジ情報（例：ビルドステータス、ライセンスバッジなど）を解析し抽出する機能を提供します。
-   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、アプリケーション内で扱いやすい形式に整形、フィルタリング、および追加情報（プロジェクト概要など）を付与する機能を提供します。
-   `src/generate_repo_list/seo_template.yml`: SEO関連のメタデータやキーワードなどを定義するためのテンプレート設定ファイルです。
-   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
-   `src/generate_repo_list/strings.yml`: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
-   `src/generate_repo_list/template_processor.py`: Markdown生成時に使用されるテキストテンプレートを読み込み、プレースホルダーを実際のデータで置き換える（レンダリングする）機能を提供します。
-   `src/generate_repo_list/url_utils.py`: URLの構築、検証、エンコード・デコードなど、URL操作に関連する汎用的なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールの機能が正しく動作するか検証するためのテストスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `tests/test_badge_generator_integration.py`: バッジ生成機能の統合的な動作を検証するテストです。
    -   `tests/test_check_large_files.py`: `check_large_files.py`スクリプトの機能を検証するテストです。
    -   `tests/test_config.py`: 設定ファイルの読み込みや管理機能が正しく動作するかを検証するテストです。
    -   `tests/test_date_formatter.py`: 日付整形機能の正確性を検証するテストです。
    -   `tests/test_environment.py`: プロジェクトの実行環境が正しく設定されているかを検証するテストです。
    -   `tests/test_integration.py`: プロジェクト全体の主要なフロー（GitHub API連携からMarkdown生成まで）が正しく連携して動作するかを検証する統合テストです。
    -   `tests/test_markdown_generator.py`: Markdown生成ロジックが期待通りの出力を生成するかを検証するテストです。
    -   `tests/test_project_overview_fetcher.py`: プロジェクト概要の取得機能が正しく動作するかを検証するテストです。
    -   `tests/test_readme_badge_extractor.py`: `README`からバッジ情報を正確に抽出できるかを検証するテストです。
    -   `tests/test_repository_processor.py`: リポジトリ情報の処理と整形機能が正しく動作するかを検証するテストです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細は分析できませんでした。しかし、各ファイルはその役割から以下のような種類の関数を提供していると推測できます。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(type, value, style)`: 指定されたタイプ（言語、ライセンスなど）と値に基づいて、shields.io形式のバッジURLを生成する関数。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(config_path)`: 指定されたパスからYAML設定ファイルを読み込み、ディクショナリとして返す関数。
    -   `get_setting(key_path)`: ドット区切りのキーパスを使用して、読み込んだ設定から特定の値を安全に取得する関数。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_date(iso_date_string, format_string)`: ISO 8601形式の日付文字列を指定されたフォーマット文字列に変換する関数。
-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: スクリプトのエントリーポイント。コマンドライン引数をパースし、リポジトリ情報の取得、処理、Markdown生成、ファイル出力の全体フローをオーケストレートする関数。
    -   `fetch_and_process_repos(username, limit, github_token)`: GitHub APIからリポジトリ情報を取得し、各リポジトリを処理する関数。
    -   `generate_output_markdown(processed_repos)`: 処理済みのリポジトリ情報から最終的なMarkdown文字列を生成する関数。
-   **`src/generate_repo_list/language_info.py`**:
    -   `get_primary_language(languages_data)`: GitHub APIから取得した言語データから、主要な言語を特定する関数。
    -   `format_language_stats(languages_data)`: 言語使用統計を整形し、表示用の文字列を生成する関数。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repository_entry(repo_data)`: 単一のリポジトリ情報から、Markdown形式のリポジトリエントリ（タイトル、説明、バッジなど）を生成する関数。
    -   `generate_full_markdown(repo_list, seo_data, json_ld_data)`: 複数のリポジトリエントリを統合し、SEO情報やJSON-LDを含んだ最終的なMarkdownドキュメントを生成する関数。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_name, owner, github_token, config)`: 指定されたリポジトリから`project-overview.md`ファイルを読み込み、その中からプロジェクト概要の3行説明を抽出する関数。
-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   `extract_badges(readme_content)`: `README.md`のテキストコンテンツから、バッジのMarkdownまたはHTMLスニペットを解析・抽出する関数。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repo_data(raw_repo_data, github_token, config)`: GitHub APIから取得した個々のリポジトリの生データを、必要な情報（概要、言語、バッジなど）を含む整形された辞書形式に変換する関数。
-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   `calculate_star_fork_stats(repo_data)`: リポジトリのスター数とフォーク数を集計し、統計情報として提供する関数。
-   **`src/generate_repo_list/template_processor.py`**:
    -   `render_template(template_string, data)`: テンプレート文字列内のプレースホルダーを、提供されたデータで置き換えて最終的な文字列を生成する関数。
-   **`src/generate_repo_list/url_utils.py`**:
    -   `build_github_api_url(endpoint, username, repo_name)`: GitHub APIのエンドポイントとパラメータから、完全なAPIリクエストURLを構築する関数。
    -   `slugify(text)`: テキストをURLフレンドリーなスラッグ形式に変換する関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-21 07:09:04 JST
