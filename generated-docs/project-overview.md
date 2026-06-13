Last updated: 2026-06-14

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を取得してGitHub Pages向けリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、各リポジトリの概要も自動取得して表示します。
- GitHub Pagesサイトの検索エンジン可視性を向上させ、LLMによるリポジトリ参照の精度改善を目指します。

## 技術スタック
- フロントエンド:
    - **Jekyll/GitHub Pages**: 静的サイトジェネレーターであり、生成されたMarkdownファイルをホストするプラットフォームとして利用されます。
    - **Markdown**: リポジトリ一覧ページや各リポジトリの概要を表示するための出力フォーマットです。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからの情報取得、Markdown生成、ファイル操作などの処理を実行します。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に利用されます。
    - **TOML**: シークレット情報の設定ファイル（`secrets.toml`の例示）や、`.github_automation`内の設定ファイル（`check-large-files.toml`）に利用されます。
- テスト:
    - **Pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報からMarkdownファイルを「生成」する役割を担います。Jekyllは生成されたMarkdownから最終的なWebサイトを構築します。
- 言語機能:
    - **Pythonの標準ライブラリ**: GitHub APIとの連携、ファイルI/O、文字列処理、日付処理などに広く利用されます。
- 自動化・CI/CD:
    - **GitHub API**: リポジトリ情報の自動取得の基盤となり、システムの中核を成す自動化技術です。
    - **`.github_automation`**: リポジトリ管理に関連する補助的な自動化スクリプト（例: 大容量ファイルチェック）が格納されていますが、CI/CD環境での利用は明示されていません。
- 開発標準:
    - **Ruff**: Pythonコードのフォーマットとリンティングを自動的に行い、コード品質と一貫性を保つためのツールです。
    - **.editorconfig**: 異なるエディタやIDE間で基本的なコードスタイル（インデントなど）を統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタ間でのコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: GitHub Actionsやローカルでの大容量ファイルチェックに関するスクリプトと設定を格納するディレクトリです。
    - `README.md`: `check_large_files`機能に関する説明が含まれています。
    - `check-large-files.toml`: 大容量ファイルチェックの設定を定義します。
    - `scripts/check_large_files.py`: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、開発者向けのヒントなどを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定を定義するファイルです。
- **`assets/`**: Jekyllサイトで使用される画像（ファビコン）などの静的アセットを格納するディレクトリです。
    - `favicon-*.png`: ウェブサイトのファビコン画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストに利用される補助スクリプトです。
- **`generated-docs/`**: 各リポジトリから取得されたプロジェクト概要Markdownファイルなどが一時的に格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイト所有権を確認するために利用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このファイルに自動生成されたリポジトリ一覧が出力されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したドキュメントファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するファイルで、ホーム画面への追加やオフライン対応などに利用されます。
- **`pytest.ini`**: Pytestフレームワークの設定ファイルで、テストの挙動やオプションを定義します。
- **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージとそのバージョンを記述したファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールし、どのページを無視するかを指示するファイルです。
- **`ruff.toml`**: Ruffリンターの設定ファイルで、Pythonコードのスタイルガイドや静的解析ルールを定義します。
- **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを認識させるためのファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種ステータス（言語、ライセンスなど）を示すバッジ画像を生成するロジックを扱います。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータや、スクリプト全体の挙動に関する設定を定義するファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットで整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理を orchestrate します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ（JSON-LD）のテンプレートを定義します。
- **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報（例: 人気度、色）を処理するロジックを提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報や概要データをもとに、GitHub Pages用のMarkdownコンテンツを生成する役割を担います。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得するロジックを提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出し、解析するロジックを扱います。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報に整形する主要なビジネスロジックを含みます。
- **`src/generate_repo_list/seo_template.yml`**: SEOメタデータに関するテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する各種統計情報（スター数、フォーク数など）を計算・集計するロジックを提供します。
- **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownやUIで使用される表示メッセージ、文言を管理する多言語対応（または単一言語）のためのファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdownや他の出力形式のテンプレートを読み込み、動的なデータで埋め込んで最終的なコンテンツを生成するロジックを扱います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`機能のテストケースが含まれるファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - `conftest.py`: Pytestのテストフィクスチャやヘルパー関数を定義するファイルです。
    - `test_badge_generator_integration.py`: バッジ生成機能の統合テストを記述します。
    - `test_check_large_files.py`: 大容量ファイルチェック機能のテストケースを記述します。
    - `test_config.py`: 設定ファイルの読み込みや管理機能に関するテストを記述します。
    - `test_date_formatter.py`: 日付整形ユーティリティのテストを記述します。
    - `test_environment.py`: テスト環境のセットアップや依存関係に関するテストを記述します。
    - `test_integration.py`: システム全体の主要な統合テストを記述します。
    - `test_markdown_generator.py`: Markdown生成機能のテストを記述します。
    - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを記述します。
    - `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを記述します。
    - `test_repository_processor.py`: リポジトリ情報処理機能のテストを記述します。

## 関数詳細説明
提供された情報からは、具体的な関数名、引数、戻り値、詳細な機能は分析できませんでした。
しかし、各Pythonファイルはそのファイル名が示す役割を果たす関数群を持っていると推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-14 07:26:41 JST
