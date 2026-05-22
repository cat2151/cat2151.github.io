Last updated: 2026-05-23

# Project Overview

## プロジェクト概要
- GitHub APIを用いてリポジトリ情報を取得し、GitHub Pages用マークダウンを自動生成します。
- 検索エンジン最適化を施し、リポジトリの発見性とLLMからの参照性を向上させます。
- バッジ付き表示、分類、各リポジトリ概要の自動取得などの機能を提供します。

## 技術スタック
- フロントエンド:
  - Jekyll / GitHub Pages: 静的サイトジェネレーターとして、生成されたMarkdownファイルからWebページを構築し、GitHub Pagesで公開します。
  - Markdown: サイトコンテンツやリポジトリ一覧の記述に使用される軽量マークアップ言語です。
- 音楽・オーディオ: 特になし
- 開発ツール:
  - Python: リポジトリ情報の取得、データ処理、Markdown生成を行うメインのスクリプト言語です。
  - pytest: Pythonコードの単体テストや結合テストを実行するためのテストフレームワークです。
  - Ruff: Pythonコードのリンティング（構文チェック）とフォーマット（整形）を自動化し、コード品質とスタイルの一貫性を保ちます。
- テスト:
  - pytest: Pythonアプリケーションの機能検証および品質保証のために使用されるテストフレームワークです。
- ビルドツール:
  - Jekyll: GitHub Pagesによって利用され、生成されたMarkdownファイルやその他のアセットを静的なWebサイトとしてビルドします。
- 言語機能:
  - Python: プロジェクトの主要なプログラミング言語であり、データ処理やAPI通信に利用されます。
  - YAML: `config.yml` や `strings.yml` など、プロジェクトの設定や文字列リソースを記述するために使用されます。
  - TOML: `secrets.toml` のように、機密性の高い設定情報（例: GitHubトークン）を安全に管理するために使用されます。
  - JSON-LD: 検索エンジン最適化 (SEO) のため、構造化されたデータをWebページに埋め込む形式として使用されます。
- 自動化・CI/CD:
  - (Pythonスクリプト自体が自動生成プロセスを担う)
  - .github_automation/check_large_files: 特定の自動化タスク（例: 大容量ファイルのチェック）にPythonスクリプトが使用されていますが、CI/CDパイプライン全体を構築するツールとしての言及はありません。
- 開発標準:
  - Ruff: コードのスタイルを統一し、潜在的なエラーを指摘することで、コード品質を維持するためのルールと自動修正機能を提供します。
  - .editorconfig: 異なる開発環境（エディタ、IDE）間でコーディングスタイル（インデント、改行コードなど）の一貫性を強制するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、文字コードなど）を維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
  - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
  - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
  - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの概要、目的、使用方法、クイックスタートガイドなど、開発者や利用者に向けた主要な説明文書です。
- **`_config.yml`**: Jekyll静的サイトジェネレーターのグローバル設定ファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコン画像やその他の静的アセットを格納するディレクトリです。
  - **`assets/favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像です。
- **`debug_project_overview.py`**: `project_overview` 概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要などのドキュメントが一時的または永続的に格納されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されたHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのメインページ（トップページ）となるMarkdownファイルで、自動生成されたリポジトリ一覧が出力されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや関連情報が記述されたファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータや表示設定を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するためのファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、あるいは避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
  - **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
  - **`src/generate_repo_list/`**: GitHubリポジトリ一覧を生成する機能の中核となるPythonパッケージです。
    - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリの技術スタックなどを視覚的に示すバッジ（例: 使用言語）を生成するモジュールです。
    - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成プロセスや `project_overview` 取得機能などの技術的なパラメータを定義する設定ファイルです。
    - **`src/generate_repo_list/config_manager.py`**: YAML形式の設定ファイル（`config.yml`, `strings.yml`）の読み込み、解析、および管理を行うモジュールです。
    - **`src/generate_repo_list/date_formatter.py`**: 日付情報の表示形式を整形するためのユーティリティモジュールです。
    - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIを通じてリポジトリ情報を取得し、最終的なMarkdownファイル（`index.md`など）を生成するメインスクリプトです。
    - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためにページに埋め込むJSON-LD形式の構造化データテンプレートです。
    - **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの主要言語やその他の言語関連情報を処理・表示するためのモジュールです。
    - **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報に基づいて、最終的なMarkdown形式のコンテンツを組み立てるモジュールです。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を自動的に取得するモジュールです。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス）を抽出するモジュールです。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形するモジュールです。
    - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイルです。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するモジュールです。
    - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや静的な文言を管理するための多言語対応（または単一言語の集約）設定ファイルです。
    - **`src/generate_repo_list/template_processor.py`**: Markdownコンテンツ生成の際に、特定のテンプレートを処理し、データと結合して最終的な出力を生成するモジュールです。
    - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **`tests/conftest.py`**: pytestテストフレームワークのフィクスチャや共通設定を定義するファイルで、複数のテストファイル間で共有されます。
  - **`tests/test_badge_generator_integration.py`**: `badge_generator` モジュールの結合テストを行うスクリプトです。
  - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトのテストを行うスクリプトです。
  - **`tests/test_config.py`**: 設定ファイル（`config.yml`など）の読み込みと解析に関する機能のテストを行うスクリプトです。
  - **`tests/test_date_formatter.py`**: `date_formatter` モジュールの日付整形機能のテストを行うスクリプトです。
  - **`tests/test_environment.py`**: 環境変数や実行環境のセットアップに関するテストを行うスクリプトです。
  - **`tests/test_integration.py`**: プロジェクトの主要なコンポーネント間の連携をテストする結合テストスクリプトです。
  - **`tests/test_markdown_generator.py`**: `markdown_generator` モジュールのMarkdown生成機能のテストを行うスクリプトです。
  - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュール（プロジェクト概要取得）のテストを行うスクリプトです。
  - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールのREADMEからのバッジ抽出機能のテストを行うスクリプトです。
  - **`tests/test_repository_processor.py`**: `repository_processor` モジュール（リポジトリデータ処理）のテストを行うスクリプトです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値、および機能の詳細を特定できませんでした。Pythonスクリプト群には多くの関数が含まれていますが、そのシグネチャと説明はコードの静的解析なしには提供できません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-23 07:25:50 JST
