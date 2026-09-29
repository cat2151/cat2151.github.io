Last updated: 2026-09-30

# Project Overview

## プロジェクト概要
- GitHub API を活用し、JekyllベースのGitHub Pagesサイト向けにリポジトリ一覧のMarkdownファイルを自動生成するシステムです。
- GitHubユーザーページのリポジトリ一覧が抱えるSEO上の課題を解決し、検索エンジンやLLMからの参照性を向上させます。
- リポジトリの概要、バッジ、分類、SEOメタデータを自動で表示し、情報の可読性とアクセス性を高めます。

## 技術スタック
- フロントエンド:
    - GitHub Pages: 生成されたMarkdownファイルをホスティングし、公開する静的サイトサービス。
    - Jekyll: GitHub Pagesの静的サイトジェネレーター（このプロジェクトが生成するMarkdownはJekyll互換）。
    - Markdown: リポジトリ一覧のコンテンツ記述に使用される軽量マークアップ言語。
- 音楽・オーディオ: なし
- 開発ツール:
    - Python: プロジェクトの主要な開発言語。
    - argparse: コマンドライン引数をパースし、スクリプトの実行オプションを定義するために使用。
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の読み込みと書き出しに使用。
    - requests: GitHub APIへのHTTPリクエストを送信し、リポジトリ情報を取得するために使用。
    - beautifulsoup4: HTML/XMLパーシングライブラリ。READMEからバッジ情報を抽出する際に使用される可能性があります。
    - toml: TOML形式の設定ファイル (`secrets.toml`) の読み込みに使用。
- テスト:
    - pytest: Pythonでテストを記述・実行するためのフレームワーク。
- ビルドツール:
    - 特になし: プロジェクトの主要な機能はMarkdownファイルの生成であり、複雑なビルドプロセスは含まれません。
- 言語機能:
    - Python: ファイル操作、文字列処理、データ構造（リスト、辞書）、HTTP通信、エラーハンドリングなど、豊富な言語機能を利用。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation` ディレクトリが存在することから、関連する自動化スクリプトの実行環境としてGitHub Actionsが利用されることを想定しています。
- 開発標準:
    - ruff: Pythonコードのリンティングとフォーマットを自動化し、コードスタイルの一貫性を保つツール。
    - .editorconfig: 異なるIDEやエディタを使用する開発者間でコードの書式設定（インデント、改行など）を統一するためのファイル。

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
- **`.editorconfig`**: コードエディタの設定を統一し、異なる開発者間でのコードスタイルの一貫性を保証します。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定を定義するファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの概要、目的、使用方法、開発者向けのヒントなどが記述されたメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。
- **`assets/`**: faviconなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグを目的としたスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや、リポジトリのプロジェクト概要（`project-overview.md`）が配置される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のためのHTMLファイルです。
- **`index.md`**: メインスクリプトによって生成される、リポジトリ一覧のコンテンツを含むMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **`issue-notes/22.md`**: 特定のイシューに関するメモや詳細情報が記述されたファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルで、アプリのメタデータや表示設定を定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイルです。
- **`requirements-dev.txt`**: 開発やテスト、ビルド時にのみ必要なPythonライブラリのリストです。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonライブラリのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットツール`ruff`の設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの特性（言語、ステータスなど）を示すバッジを生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成システムの動作に関する主要な設定パラメータ（例: プロジェクト概要取得の有効化、タイムアウトなど）を定義します。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）を読み込み、アプリケーション全体で利用できるように管理するモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式や特定のロケールに合わせた形式に変換する機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリスクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdownファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジンにリポジトリ情報をより適切に理解させるためのJSON-LD形式の構造化データテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語に関する情報を処理し、集計や表示に適した形式に変換する機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートに基づいて、Jekyll互換のMarkdown形式のリポジトリ一覧コンテンツを生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクト概要のテキストを抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、既に記述されているバッジ情報を解析し抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータに対して、フィルタリング、必要な情報の抽出、整形などの前処理を行うモジュールです。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化データに関するテンプレート定義を格納します。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新からの経過時間などの統計情報を計算・集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言を管理し、国際化/ローカライズに対応するためのファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用するテンプレートファイルの読み込み、変数置換、条件分岐処理など、テンプレートエンジンの役割を担います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、エンコード・デコードなど、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関する単体テストを記述したファイルです。
- **`tests/conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共通利用可能にします。
- **`tests/test_badge_generator_integration.py`**: バッジ生成機能の動作を確認するための統合テストです。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
- **`tests/test_config.py`**: 設定ファイルの読み込みや解析に関するテストを記述したファイルです。
- **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストを記述したファイルです。
- **`tests/test_environment.py`**: 開発環境のセットアップや依存関係に関する基本的なテストを記述したファイルです。
- **`tests/test_integration.py`**: プロジェクトの主要なコンポーネント間の連携を確認するための統合テストです。
- **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
- **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
- **`tests/test_readme_badge_extractor.py`**: `README.md`からのバッジ抽出機能のテストを記述したファイルです。
- **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテストを記述したファイルです。

## 関数詳細説明
提供された情報からは具体的な関数の引数や戻り値の詳細を特定できませんでした。しかし、各ファイルが提供する機能に基づいて、以下に主要な機能グループとそれに関連する関数の役割を説明します。

- **`generate_repo_list.py`**:
    - メインの実行フローを制御する関数群を提供します。GitHub APIからのデータ取得、データの処理、そして最終的なMarkdownファイルへの出力を調整します。
- **`badge_generator.py`**:
    - 指定されたリポジトリ情報（言語、ステータスなど）に基づいて、Markdown形式のバッジ文字列を生成する関数群を提供します。
- **`config_manager.py`**:
    - 設定ファイル（例: `config.yml`）を読み込み、その内容をアプリケーション全体でアクセス可能なオブジェクトとして提供する関数群を提供します。
- **`date_formatter.py`**:
    - 日付や時刻のオブジェクトを、指定されたフォーマット（例: "YYYY/MM/DD"）の文字列に変換する関数群を提供します。
- **`language_info.py`**:
    - リポジトリのプログラミング言語に関する情報を解析し、主要言語の特定や、言語ごとの統計情報を提供する関数群を提供します。
- **`markdown_generator.py`**:
    - 処理済みのリポジトリデータとテンプレートを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成する関数群を提供します。
- **`project_overview_fetcher.py`**:
    - 指定されたリポジトリの特定のパス（例: `generated-docs/project-overview.md`）からテキストコンテンツを読み込み、プロジェクト概要の3行説明を抽出する関数群を提供します。
- **`readme_badge_extractor.py`**:
    - リポジトリの`README.md`ファイルの内容を解析し、その中に含まれる既存のバッジ（例: Shields.io形式）のURLやテキストを抽出する関数群を提供します。
- **`repository_processor.py`**:
    - GitHub APIから取得した生のリポジトリデータを入力として受け取り、表示に必要な情報（名前、説明、URL、スター数、言語など）を抽出し、整形する関数群を提供します。
- **`statistics_calculator.py`**:
    - リポジトリのスター数、フォーク数、最終コミットからの経過時間など、各種統計情報を計算する関数群を提供します。
- **`template_processor.py`**:
    - テンプレートファイル（MarkdownやJSON-LD）を読み込み、変数置換や条件に応じたコンテンツ挿入などを行う関数群を提供します。
- **`url_utils.py`**:
    - URLの構築、検証、エンコーディング、デコーディングなど、URL操作に関連する共通ユーティリティ関数群を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-30 07:12:56 JST
