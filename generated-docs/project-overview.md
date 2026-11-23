Last updated: 2026-11-24

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、JekyllベースのGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジンからのクロールを促進し、LLMがGitHubリポジトリを参照しやすくなることを目的としています。
- 各リポジトリの概要、バッジ、分類などを自動取得・表示し、SEOに最適化されたMarkdownを生成します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレータ。生成されたMarkdownファイルを基にサイトを構築します。
    - **Markdown**: リポジトリ一覧の出力形式であり、Jekyllサイトのコンテンツ記述に利用されます。
- 音楽・オーディオ:
    - （該当する技術はありません）
- 開発ツール:
    - **Pytest**: Pythonコードのテストフレームワーク。単体テストや統合テストの実行に利用されます。
    - **Ruff**: Pythonコードのリンターおよびフォーマッター。コード品質の維持とスタイルの一貫性確保に貢献します。
    - **GitHub API**: リポジトリ情報、プロジェクト概要などを取得するために使用されます。
- テスト:
    - **Pytest**: コードの正しさを検証するためのフレームワーク。
- ビルドツール:
    - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py` がメインのビルドスクリプトとして機能し、GitHub APIからのデータ取得とMarkdownファイルの生成を行います。
    - **YAML/TOML**: 設定ファイル (`config.yml`, `strings.yml`, `ruff.toml`, `pytest.ini` など) の記述に利用されます。
- 言語機能:
    - **Python**: プロジェクトの主要なプログラミング言語。データ取得、処理、ファイル生成のロジックが記述されています。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリ内のスクリプトは、自動化されたワークフロー（例：大規模ファイルチェック）に利用される可能性があります。
- 開発標準:
    - **Ruff**: コードの自動整形と静的解析により、コード品質と可読性を向上させます。
    - **.editorconfig**: 異なるエディタ間でのコーディングスタイル（インデント、改行など）の統一を支援します。

## ファイル階層ツリー
```
📄 .editorconfig
📁 .github_automation/
  📁 check_large_files/
    📖 README.md
    📄 check-large_files.toml
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
- **.editorconfig**: 異なるエディタ間でのコーディングスタイル（インデント、文字コードなど）の統一ルールを定義します。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェック機能に関するファイル群。
        - **README.md**: 大容量ファイルチェック機能の説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックの閾値や対象に関する設定ファイル。
        - **scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: 一時ファイル、ログ、環境固有の設定）を指定します。
- **LICENSE**: 本プロジェクトのライセンス（MITライセンス）情報が記述されています。
- **README.md**: プロジェクトの概要、目的、主な機能、使い方、設定、開発者向けヒントなどを記述した主要なドキュメント。
- **_config.yml**: Jekyllサイト全体の共通設定ファイル。テーマ、プラグイン、変数の定義などを行います。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズで提供されるWebサイトのファビコン（ブラウザタブなどに表示されるアイコン）画像ファイル。
- **debug_project_overview.py**: `project_overview` 機能のデバッグや単独での動作確認に使用されるスクリプトであると推測されます。
- **generated-docs/**: 生成されたドキュメントや一時ファイルを格納するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイトの所有権確認に使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される主要なMarkdownファイル。GitHub Pagesサイトのトップページとして、リポジトリ一覧を表示します。
- **issue-notes/**: 課題やメモを格納するディレクトリ。
    - **22.md**: 特定の課題（おそらくIssue #22に関連する）に関する詳細なメモや考察を記述したMarkdownファイル。
- **manifest.json**: PWA (Progressive Web App) 用のマニフェストファイル。Webアプリの表示方法や動作を設定します。
- **pytest.ini**: Pytestの設定ファイル。テストの実行方法や検出ルールなどを定義します。
- **requirements-dev.txt**: 開発・テスト時に必要なPythonライブラリのリスト。
- **requirements.txt**: 本番環境での実行に必要なPythonライブラリのリスト。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイル。
- **ruff.toml**: Pythonコードリンター・フォーマッターであるRuffの設定ファイル。コードスタイルルールや無視するエラーなどを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: `src` ディレクトリがPythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧の生成に関連するモジュール群を格納するパッケージ。
        - **__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを実装します。
        - **config.yml**: プロジェクト概要取得機能など、スクリプトの技術的なパラメータを設定するYAMLファイル。
        - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するためのロジックを提供します。
        - **date_formatter.py**: 日付や時刻の表示形式を変換・整形するためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインスクリプト。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を取得・処理するロジックを実装します。
        - **markdown_generator.py**: 取得したデータに基づいてMarkdown形式のコンテンツを生成するロジックを実装します。
        - **project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を自動取得するロジックを実装します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するロジックを実装します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理に適した形式に変換するロジックを実装します。
        - **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算するロジックを実装します。
        - **strings.yml**: UIメッセージ、表示文言、説明テキストなどを一元的に管理するYAMLファイル。多言語対応などにも使用されます。
        - **template_processor.py**: MarkdownやHTMLテンプレートを処理し、動的なデータを埋め込むためのロジックを実装します。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` など、プロジェクト概要取得機能の単体テストや統合テストを記述したスクリプトであると推測されます。
- **tests/**: プロジェクトのテストファイルを格納するディレクトリ。
    - **conftest.py**: Pytestのテストフィクスチャやヘルパー関数を定義し、テスト間で共有されるリソースをセットアップします。
    - **test_badge_generator_integration.py**: `badge_generator.py` の機能に関する統合テスト。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py` のテスト。
    - **test_config.py**: 設定ファイルの読み込み・管理 (`config_manager.py`) に関するテスト。
    - **test_date_formatter.py**: `date_formatter.py` の日付整形機能に関するテスト。
    - **test_environment.py**: テスト実行環境や依存関係に関するテスト。
    - **test_integration.py**: プロジェクト全体の主要機能に関する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator.py` のMarkdown生成機能に関するテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py` のプロジェクト概要取得機能に関するテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor.py` のREADMEからのバッジ抽出機能に関するテスト。
    - **test_repository_processor.py**: `repository_processor.py` のリポジトリ情報処理機能に関するテスト。

## 関数詳細説明
提供された情報からは、具体的な関数名、引数、戻り値、詳細な機能について特定できませんでした。
ファイル名から推測される役割としては、以下のモジュールにそれぞれ関連する関数群が含まれていると考えられます。
- `badge_generator.py`: バッジ生成のための関数。
- `config_manager.py`: 設定ファイルの読み込み、設定値の取得・設定のための関数。
- `date_formatter.py`: 日付文字列をフォーマットするための関数。
- `generate_repo_list.py`: メインの処理フローを制御し、各モモジュールの関数を呼び出してリポジトリ一覧を生成する関数。
- `language_info.py`: プログラミング言語情報を処理するための関数。
- `markdown_generator.py`: Markdownコンテンツを生成するための関数。
- `project_overview_fetcher.py`: プロジェクト概要をフェッチするための関数。
- `readme_badge_extractor.py`: READMEからバッジを抽出するための関数。
- `repository_processor.py`: リポジトリデータを処理するための関数。
- `statistics_calculator.py`: 統計情報を計算するための関数。
- `template_processor.py`: テンプレートを処理するための関数。
- `url_utils.py`: URL操作のためのユーティリティ関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-24 07:07:38 JST
