Last updated: 2026-06-06

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンのクロールを最適化し、LLMがリポジトリを参照しやすくすることで開発効率の向上を目指します。
- 各リポジトリの概要を自動取得し、バッジ付きでアクティブ・アーカイブ・フォーク別に一覧表示します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用), Markdown (自動生成されるコンテンツの形式)
- 音楽・オーディオ: N/A
- 開発ツール: Python (主要なスクリプト言語), Git/GitHub (リポジトリ管理とGitHub API連携), requests (GitHub APIとの通信ライブラリ), PyYAML (YAML設定ファイルの処理), toml (TOML設定ファイルの処理)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: N/A (Pythonスクリプトがコンテンツ生成を直接担うため、特定のビルドツールは使用していません)
- 言語機能: Python (モジュール開発、ファイルI/O、文字列処理などの標準ライブラリ機能)
- 自動化・CI/CD: N/A (プロジェクトのREADMEにCI/CD不要のローカル開発重視と明記されています。`.github_automation` ディレクトリはGitHubと連携するユーティリティスクリプトを含みますが、一般的なCI/CDツールとしては分類されません。)
- 開発標準: ruff (Pythonコードの自動整形およびリンター), .editorconfig (異なるエディタ間でのコーディングスタイル統一設定)

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
-   **`.editorconfig`**: 異なる開発環境やエディタ間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどと連携して自動化を行うためのスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/README.md`**: `check_large_files` ディレクトリ内の機能に関する説明文書です。
    -   **`check_large_files/check-large-files.toml`**: `check_large_files.py` スクリプトの動作を制御する設定ファイルです。
    -   **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大規模なファイルを検出し、管理するのに役立つPythonスクリプトです。
-   **`.gitignore`**: Gitでバージョン管理システムに含めないファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイルです。
-   **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明する主要なドキュメントファイルです。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動や設定を制御するファイルです。
-   **`assets/`**: GitHub Pagesサイトで使用される画像、アイコン、その他の静的ファイルを格納するディレクトリです。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   **`debug_project_overview.py`**: `project_overview_fetcher` などのモジュールのデバッグや単体テストに使用される可能性のあるPythonスクリプトです。
-   **`generated-docs/`**: 本システムによって自動生成されたドキュメントやデータが格納されるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: メインの出力ファイルであり、生成されたリポジトリ一覧がMarkdown形式で記述され、GitHub Pagesのトップページとして表示されます。
-   **`issue-notes/`**: 開発中の特定の課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記述したファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータ（アプリ名、アイコン、表示設定など）を定義するファイルです。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動をカスタマイズするための設定ファイルです。
-   **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンを定義するファイルです。
-   **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを定義するファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、またどの部分を避けるべきかを指示するファイルです。
-   **`ruff.toml`**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **`__init__.py`**: Pythonパッケージとして認識させるための空ファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        -   **`__init__.py`**: `generate_repo_list` パッケージとして認識させるための空ファイルです。
        -   **`badge_generator.py`**: リポジトリのプログラミング言語やライセンスなどの情報を元に、表示用のバッジを生成するロジックを実装しています。
        -   **`config.yml`**: プロジェクト概要取得機能などの技術的なパラメータやスクリプトの動作設定を記述するファイルです。
        -   **`config_manager.py`**: YAMLやTOML形式の設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        -   **`date_formatter.py`**: 日付や時刻の情報を指定されたフォーマットで文字列に整形するユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールを連携させて最終的なMarkdownファイルを生成します。
        -   **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために、JSON-LD形式で構造化データを記述するためのテンプレートファイルです。
        -   **`language_info.py`**: GitHubリポジトリの主要なプログラミング言語に関する情報を処理し、表示に適した形に整形するロジックを実装しています。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報を基に、最終的なGitHub Pages用のMarkdownコンテンツを生成する役割を担います。
        -   **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例：ビルドステータス、カバレッジ）を抽出するロジックを含みます。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、それをアプリケーション内で扱いやすい形に加工・整形する役割を担います。
        -   **`seo_template.yml`**: SEOメタデータやキーワードなど、検索エンジン最適化に関連する情報やテンプレートを定義するファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計するモジュールです。
        -   **`strings.yml`**: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理し、国際化対応を容易にするためのファイルです。
        -   **`template_processor.py`**: Markdown生成時に使用するテンプレート（例：JekyllのLiquidタグ）を処理し、動的なコンテンツを埋め込む機能を提供します。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能に関するテストコードを格納するファイルです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **`conftest.py`**: pytestのフィクスチャやプラグイン、ヘルパー関数などを定義し、複数のテストファイルで共有可能にするためのファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator` モジュールの統合テストを行うファイルです。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files.py` スクリプトのテストコードを格納するファイルです。
    -   **`test_config.py`**: `config_manager` や関連する設定ファイルの読み込み、処理に関するテストを行うファイルです。
    -   **`test_date_formatter.py`**: `date_formatter` モジュールの機能に関するテストを行うファイルです。
    -   **`test_environment.py`**: 開発環境や実行環境のセットアップが正しく行われているかを検証するテストファイルです。
    -   **`test_integration.py`**: システム全体の主要なフローやモジュール間の連携を検証する統合テストを記述したファイルです。
    -   **`test_markdown_generator.py`**: `markdown_generator` モジュールが正しくMarkdownを生成するかどうかを検証するテストファイルです。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）に関するテストを行うファイルです。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールがREADMEから正しくバッジを抽出できるかをテストするファイルです。
    -   **`test_repository_processor.py`**: `repository_processor` モジュールがGitHub APIからのリポジトリデータを正しく処理・整形できるかをテストするファイルです。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数名、引数、戻り値、機能の詳細に関する情報が含まれていないため、個々の関数について詳細な説明を生成することはできません。

各ファイルが担う役割に基づき、以下のような主要な機能を持つ関数群が存在すると考えられますが、具体的なシグネチャは不明です。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: プログラムのエントリーポイント。リポジトリ情報の取得、処理、Markdown生成をオーケストレートする役割。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(...)`: リポジトリの属性に基づいてバッジ画像を生成する役割。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(...)`: 指定されたパスから設定ファイル（YAML/TOML）を読み込み、Pythonオブジェクトとして提供する役割。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(...)`: 指定されたURLまたはファイルパスからプロジェクト概要を抽出し、整形された3行の説明を返す役割。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_markdown(...)`: 処理済みのリポジトリ情報とテンプレートを使用して、最終的なMarkdown文字列を生成する役割。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository_data(...)`: GitHub APIから取得した生のリポジトリデータを受け取り、アプリケーション内部で利用しやすい形式に変換・整形する役割。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**:
    -   `check_files(...)`: 指定された条件に基づいてリポジトリ内のファイルを走査し、大規模なファイルを特定して報告する役割。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-06 07:29:17 JST
