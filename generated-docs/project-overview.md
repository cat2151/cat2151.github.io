Last updated: 2026-09-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けに最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、GitHub PagesサイトのSEOを向上させ、LLMによるリポジトリ参照の精度改善を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を利用し、自動生成されたMarkdownファイルを静的サイトとして公開します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Pytest: Pythonコードのテストフレームワークとして利用されています。
    - Ruff: コードの整形とリントを行い、コードスタイルと品質を統一します。
    - Git: ソースコードのバージョン管理システムとして使用されます。
- テスト: Pytest を用いて、各機能の単体テストおよび結合テストが実施されます。
- ビルドツール: 該当なし（PythonスクリプトがMarkdown生成の役割を果たします）
- 言語機能:
    - Python: メインのスクリプト言語として、GitHub APIとの連携、データ処理、Markdown生成に利用されています。
    - YAML: プロジェクトの設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用されています。
    - Markdown: GitHub Pagesへの出力形式として、リポジトリ一覧やプロジェクト概要の記述に利用されています。
    - TOML: 設定ファイル (`secrets.toml`, `ruff.toml`, `check-large-files.toml`) の記述に使用されています。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation` ディレクトリ内のスクリプトは、GitHub Actionsと連携して特定の自動化タスク（例: 大容量ファイルチェック）を実行するために設計されています。
- 開発標準:
    - Ruff: コードの整形とリントを自動化し、Pythonコードの品質と統一性を保ちます。
    - .editorconfig: 異なるエディタ間でのコーディングスタイルの一貫性を維持するための設定ファイルです。

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
- **`.editorconfig`**: コードエディタの設定（インデントスタイル、文字コードなど）を統一し、開発者間で一貫したコーディングスタイルを維持します。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローで使用されるスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックする自動化スクリプト群です。
        - **`README.md`**: `check_large_files` ディレクトリの目的と使い方を説明するドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するTOMLファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリ（例: 一時ファイル、ビルド成果物）を指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの概要、目的、機能、インストール方法、使い方、設定、ライセンスなど、プロジェクトに関する包括的な情報を提供します。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
- **`assets/`**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズです。
- **`debug_project_overview.py`**: リポジトリのプロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要ファイルなどが一時的に配置される、またはその基準となるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: メインのMarkdownファイルで、このスクリプトによってGitHubリポジトリの一覧が生成・出力されます。これがGitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: 課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（ID 22）に関する詳細なメモや議論が記述されています。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの表示方法や動作を定義します。
- **`pytest.ini`**: Pytestのテスト実行に関する設定（テスト検出パターン、プラグインなど）を定義するファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの依存関係を記述したファイルです。
- **`requirements.txt`**: プロジェクトの本番環境で実行するために必要なPythonライブラリの依存関係を記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールするか、しないかを指示するファイルです。
- **`ruff.toml`**: RuffによるPythonコードの整形およびリントに関するルールや設定を定義するファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要ロジックが含まれるPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリの技術スタックや状態を示すバッジ（Markdown形式）を生成するロジックを含みます。
        - **`config.yml`**: `generate_repo_list` スクリプトの動作設定（プロジェクト概要取得機能のON/OFF、対象ファイルパスなど）を定義するYAMLファイルです。
        - **`config_manager.py`**: YAML設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供します。
        - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式でリポジトリ一覧を生成します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を取得・処理するロジックを提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報や設定に基づき、最終的なMarkdownコンテンツを生成するコアロジックを含みます。
        - **`project_overview_fetcher.py`**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクト概要のテキストを抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に加工・整形するロジックを含みます。
        - **`seo_template.yml`**: SEO関連のメタデータ（タイトル、説明など）を定義するテンプレートYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言（多言語対応の可能性も含む）を一元管理するYAMLファイルです。
        - **`template_processor.py`**: Markdownテンプレートに変数を埋め込んだり、条件分岐を処理したりして、最終的な出力コンテンツを生成する機能を提供します。
        - **`url_utils.py`**: URLの操作や検証、生成に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能、特にプロジェクト概要の取得ロジックに関するテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: Pytestのテスト設定やフィクスチャを定義するファイルで、テスト間で共有される共通設定を提供します。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストコードです。
    - **`test_check_large_files.py`**: 大容量ファイルチェックスクリプトのテストコードです。
    - **`test_config.py`**: 設定ファイル (`config.yml`など) の読み込みや管理機能に関するテストコードです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストコードです。
    - **`test_environment.py`**: テスト環境のセットアップや依存関係に関するテストコードです。
    - **`test_integration.py`**: プロジェクトの主要機能間の統合テストコードです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストコードです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストコードです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストコードです。

## 関数詳細説明
提供された情報からは具体的な関数の引数や戻り値の詳細な分析ができませんでしたが、ファイル名とプロジェクトの機能から主要な関数の役割を推測して説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   **`main()`**: プロジェクトのエントリーポイントとなる関数。GitHub APIからのリポジトリ取得、データの加工、Markdown生成の各ステップをオーケストレーションします。引数としてGitHubユーザー名、出力ファイルパス、リポジトリ数制限などを受け取る可能性があります。
-   **`src/generate_repo_list/badge_generator.py`**
    -   **`generate_badge_markdown(badge_data)` (推定)**: 与えられたバッジデータ（例: テキスト、色、リンク）に基づいて、Markdown形式のバッジ文字列を生成します。
-   **`src/generate_repo_list/config_manager.py`**
    -   **`load_config(config_path)` (推定)**: 指定されたパスからYAML設定ファイルを読み込み、Pythonオブジェクトとして返します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   **`format_date(date_string)` (推定)**: GitHub APIから取得した日付文字列を、指定された読みやすい形式（例: "YYYY年MM月DD日"）に変換します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   **`generate_markdown_output(repositories_data, config)` (推定)**: 処理されたリポジトリデータと設定情報に基づき、最終的なリポジトリ一覧のMarkdownコンテンツ全体を生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **`fetch_project_overview(repo_owner, repo_name, config)` (推定)**: 指定されたリポジトリ（オーナー名とリポジトリ名）から、設定で指定されたパス（例: `generated-docs/project-overview.md`）にあるファイルの内容を取得し、プロジェクト概要の3行説明を抽出します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   **`process_repositories(github_client, username, limit)` (推定)**: GitHub APIクライアントとユーザー名を受け取り、GitHub APIを通じてユーザーのリポジトリ情報を取得し、必要な情報に加工してリストとして返します。
-   **`src/generate_repo_list/template_processor.py`**
    -   **`apply_template(template_string, data)` (推定)**: テンプレート文字列と埋め込むべきデータを受け取り、データをテンプレートに適用して最終的な文字列（Markdownの一部）を生成します。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**
    -   **`main()` (推定)**: 大容量ファイルチェックスクリプトのエントリーポイント。リポジトリ内のファイルを走査し、設定された閾値を超えるファイルを検出して報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-09-23 07:12:44 JST
