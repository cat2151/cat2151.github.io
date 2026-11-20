Last updated: 2026-11-21

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・処理するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧Markdownを自動生成します。
- 各リポジトリの概要を自動取得し表示することで、検索エンジンやLLMによる参照性を向上させます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesでサイトを構築するための静的サイトジェネレーター。本プロジェクトで生成されたMarkdownファイルをHTMLに変換します。
    - **Markdown**: リポジトリ一覧の出力形式であり、Jekyllが処理するコンテンツ形式です。
- 音楽・オーディオ: なし
- 開発ツール:
    - **Python**: リポジトリ情報の取得、処理、Markdown生成を行うメインのスクリプト言語です。
    - **Git**: ソースコードのバージョン管理に使用されています。
    - **GitHub**: リポジトリ情報取得元のプラットフォームであり、GitHub Pagesのホスティング環境です。
- テスト:
    - **pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py`がリポジトリ情報を元にMarkdownファイルを「生成」する役割を担います。
    - **Jekyll**: GitHub Pages上でMarkdownファイルをHTMLに「ビルド」し、ウェブサイトとして公開します。
- 言語機能:
    - **Python**: プロジェクトの主要なプログラミング言語です。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用されています。
    - **JSON**: SEO最適化のためのJSON-LDテンプレート (`json_ld_template.json`) で使用されています。
- 自動化・CI/CD:
    - **GitHub Actions**: プロジェクトの自動テスト、コード品質チェック、そしてリポジトリ一覧の定期的な自動生成など、継続的な統合・デリバリーの自動化に利用されることが想定されます（`.github_automation`ディレクトリや自動生成システムであることから）。
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックとフォーマットを自動化するためのリンター・フォーマッターです。
    - **.editorconfig**: 異なるエディタやIDE間でコードのフォーマットを統一するための設定ファイルです。

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
- **.editorconfig**: 開発環境全体でコードスタイルの一貫性を維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するコンポーネントを格納します。
        - **README.md**: `check_large_files`機能の目的と使用方法を説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェックのルールや閾値を定義する設定ファイルです。
        - **scripts/**: 大容量ファイルチェックの実行スクリプトを格納します。
            - **check_large_files.py**: 指定されたリポジトリ内で大きなファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義するファイルです。
- **LICENSE**: 本プロジェクトのライセンス（MITライセンス）情報が記載されています。
- **README.md**: プロジェクトの概要、機能、使い方、開発ヒントなどを説明する主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリです。
    - **favicon-*.png**: 各種デバイスやブラウザで表示されるファビコン画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher`機能の動作検証やデバッグを目的としたスクリプトです。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメント（例: プロジェクト概要ファイル）を一時的に保存したり、参照したりするパスとして使用されます。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認に使用されるファイルです。
- **index.md**: `generate_repo_list.py`によって生成されるリポジトリ一覧のメインコンテンツが出力されるMarkdownファイルです。
- **issue-notes/**: 開発中に発生した課題やその調査結果、メモなどを記録するためのディレクトリです。
    - **22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや解決策が記述されたファイルです。
- **manifest.json**: ウェブアプリケーションマニフェストファイルで、PWA（プログレッシブウェブアプリ）の動作や表示方法を設定します。
- **pytest.ini**: `pytest`フレームワークの実行設定（テストの発見方法、プラグインなど）を定義するファイルです。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: `ruff`リンター・フォーマッターの設定ファイルで、Pythonコードの品質とスタイルを維持するためのルールが定義されています。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧自動生成システムのコアロジックを含むPythonパッケージです。
        - **__init__.py**: `generate_repo_list`がPythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリの言語やステータスなどに基づいて表示されるバッジを生成するスクリプトです。
        - **config.yml**: リポジトリ一覧生成機能に関する技術的なパラメータ（例: プロジェクト概要取得設定）を定義する設定ファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、設定値にアクセスするためのユーティリティスクリプトです。
        - **date_formatter.py**: 日付情報を読みやすい形式に整形するためのユーティリティスクリプトです。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイル（`index.md`など）を生成するメインの実行スクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のためにページに埋め込む構造化データ（JSON-LD形式）のテンプレートファイルです。
        - **language_info.py**: リポジトリの主要言語情報などを処理し、表示に利用するためのスクリプトです。
        - **markdown_generator.py**: 処理されたリポジトリデータから、最終的なMarkdownコンテンツ（リストや詳細）を生成するスクリプトです。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出するスクリプトです。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するためのスクリプトです。
        - **repository_processor.py**: GitHub APIから取得した生のJSONデータを、表示に適したオブジェクトや構造に変換・整形するスクリプトです。
        - **seo_template.yml**: SEO関連のメタデータや設定を定義するためのテンプレートファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのスクリプトです。
        - **strings.yml**: UIメッセージや各種表示文言を一元的に管理するためのファイルです（多言語化対応や文言変更の容易化のため）。
        - **template_processor.py**: Markdown生成時に使用されるテンプレート（例: リストアイテムのフォーマット）を処理し、データと結合するスクリプトです。
        - **url_utils.py**: URLの生成、解析、検証など、URL操作に関連するユーティリティ関数を提供するスクリプトです。
- **test_project_overview.py**: `project_overview_fetcher`機能のテストケースを定義したスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **conftest.py**: `pytest`の共通フィクスチャやヘルパー関数を定義し、複数のテストファイルで共有可能にします。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストを行うスクリプトです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストスクリプトです。
    - **test_config.py**: 設定ファイルの読み込みや管理機能のテストスクリプトです。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテストスクリプトです。
    - **test_environment.py**: 実行環境に関する設定や依存関係のテストスクリプトです。
    - **test_integration.py**: 主要な機能モジュール間の連携を検証する統合テストスクリプトです。
    - **test_markdown_generator.py**: Markdownコンテンツ生成機能のテストスクリプトです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストスクリプトです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストスクリプトです。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテストスクリプトです。

## 関数詳細説明
提供された情報からは具体的な関数名や詳細なシグネチャを抽出できませんでした。しかし、プロジェクトのファイル構成と機能説明に基づき、以下の主要な処理を担う関数群が含まれていると推測されます。

- **`generate_repo_list.py`内の関数群**:
    - GitHub APIを呼び出してリポジトリ情報を取得し、全体的な処理フローを調整するメインの関数。
    - 各サブモジュールの関数を呼び出し、データの流れを制御します。
- **`repository_processor.py`内の関数群**:
    - GitHub APIから返された生のリポジトリデータ（JSON形式）を解析し、アプリケーション内で扱いやすいデータ構造に整形する関数。
    - リポジトリの属性（名前、説明、URL、言語、スター数など）を抽出し、標準化します。
- **`markdown_generator.py`内の関数群**:
    - 処理済みのリポジトリデータを受け取り、リポジトリ一覧のMarkdownテキストを生成する関数。
    - 各リポジトリの情報をテンプレートに沿って整形し、リンクやバッジを含んだ形式で出力します。
- **`project_overview_fetcher.py`内の関数群**:
    - 特定のリポジトリ（またはそのURL）を指定して、そのリポジトリ内の`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出・取得する関数。
    - ネットワークリクエストを管理し、タイムアウトやリトライ処理を含みます。
- **`badge_generator.py`内の関数群**:
    - リポジトリの属性（アクティブ、アーカイブ、フォークなど）や言語に基づいて、対応するMarkdown形式のバッジ文字列を生成する関数。
- **`config_manager.py`内の関数群**:
    - YAML形式の設定ファイル（例: `config.yml`）を読み込み、設定値をキーで取得できるインターフェースを提供する関数。
- **`date_formatter.py`内の関数群**:
    - 日付やタイムスタンプのデータを、指定されたフォーマット（例: `YYYY-MM-DD`）の文字列に変換する関数。
- **`url_utils.py`内の関数群**:
    - URLの生成、解析、正規化、検証など、URLに関連するさまざまなユーティリティ操作を提供する関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-21 07:07:27 JST
