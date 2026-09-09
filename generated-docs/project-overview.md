Last updated: 2026-09-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、指定されたユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、GitHub Pages向けにSEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- 検索エンジンでの視認性を高め、LLMによるリポジトリ参照の精度向上を目的としたシステムです。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyll)**: 生成されたMarkdownファイルを表示するための静的サイトホスティングサービスと、そのフレームワーク。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **GitHub API**: リポジトリ情報の取得に利用されるGitHubが提供するプログラマブルインターフェース。
    - **pytest**: Pythonコードのテストを効率的に行うためのフレームワーク。
    - **ruff**: Pythonコードの高速なリンター兼フォーマッター。
- テスト:
    - **pytest**: プロジェクトのコード品質と機能の正確性を検証するためのテストフレームワーク。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報の取得からMarkdown生成までの一連の処理を自動化するためのメインスクリプト。
- 言語機能:
    - **Python**: プロジェクトの主要な開発言語。データ処理、API連携、ファイル生成などに用いられます。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用。
    - **TOML**: シークレット情報 (`secrets.toml`) や一部の設定ファイル (`check-large-files.toml`) の記述に使用。
    - **JSON**: SEOメタデータテンプレート (`json_ld_template.json`) やPWAマニフェスト (`manifest.json`) に使用。
    - **Markdown**: 生成されるリポジトリ一覧ページのフォーマット。
- 自動化・CI/CD:
    - **GitHub Actions (示唆)**: プロジェクト概要自動取得機能の文脈で言及されており、GitHubプラットフォーム上でのワークフロー自動化に利用される可能性があります。
    - **Pythonスクリプト**: `_github_automation` ディレクトリ内のスクリプトなど、特定の自動化タスクに使用されます。
- 開発標準:
    - **ruff**: Pythonコードのスタイルガイド遵守と品質維持のために使用されるリンターおよびフォーマッター。
    - **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。

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
- **.editorconfig**: コードエディタ間でインデントスタイルや文字コードなど、基本的なコーディングルールを統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化処理で利用されるスクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するファイル群です。
        - **README.md**: このディレクトリの目的や使用方法を説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェックの設定（しきい値など）を定義するファイルです。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド生成物、ログファイル、一時ファイルなど）を指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。利用条件が示されています。
- **README.md**: プロジェクトの概要、目的、主な機能、使用方法、開発者向けヒントなどがまとめられた、プロジェクトの顔となるドキュメントです。
- **_config.yml**: Jekyll（GitHub Pagesの基盤）サイト全体の構成を設定するファイルです。
- **assets/**: GitHub Pagesサイトで利用される画像、アイコン、CSSなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: Webブラウザのタブやブックマークに表示されるサイトアイコンの様々なサイズ画像です。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグやテスト実行時に使用される補助スクリプトです。
- **generated-docs/**: 各リポジトリから自動取得されたプロジェクト概要ファイルなどが格納される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が格納されるMarkdownファイルです。
- **issue-notes/22.md**: 課題や検討事項に関するメモが記述されたファイルです。
- **manifest.json**: PWA (Progressive Web App) 用のマニフェストファイルで、アプリの表示設定などを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を行うファイルです。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記載したファイルです。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールして良いか、またどのページを避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonのリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: Pythonパッケージとして認識させるためのファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックを格納するパッケージです。
        - **__init__.py**: Pythonパッケージとして認識させるためのファイルです。
        - **badge_generator.py**: リポジトリに関連するバッジ（例: 言語、ライセンス）の生成や処理を行うスクリプトです。
        - **config.yml**: リポジトリ一覧生成システムの動作に関する主要な設定を定義するファイルです。
        - **config_manager.py**: `config.yml` やシークレットファイルなどの設定情報を読み込み、管理するモジュールです。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するモジュールです。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化(SEO)のためのJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立てるモジュールです。
        - **markdown_generator.py**: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するモジュールです。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `project-overview.md`）から、プロジェクトの概要説明を自動で抽出するモジュールです。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出するためのモジュールです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形するモジュールです。
        - **seo_template.yml**: SEO関連のメタ情報やページ構造に関するテンプレート設定を定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュールです。
        - **strings.yml**: UIメッセージ、キャプション、説明文など、アプリケーション内で使用されるテキスト文字列を管理するファイルです。
        - **template_processor.py**: MarkdownやHTMLなどのテンプレートファイルにデータを埋め込み、最終的なコンテンツを生成するモジュールです。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連の共通ユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: プロジェクト概要取得機能が正しく動作するかを検証するテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **conftest.py**: pytestのフィクスチャ（テストの前処理・後処理）や共通設定を定義するファイルです。
    - **test_badge_generator_integration.py**: バッジ生成機能の結合テストを行うスクリプトです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストを行うスクリプトです。
    - **test_config.py**: 設定ファイルの読み込みや解析が正しく行われるかをテストするスクリプトです。
    - **test_date_formatter.py**: 日付整形機能が期待通りに動作するかをテストするスクリプトです。
    - **test_environment.py**: プロジェクトの実行環境が適切に設定されているかを検証するテストスクリプトです。
    - **test_integration.py**: プロジェクトの主要なコンポーネント間の連携を検証する結合テストスクリプトです。
    - **test_markdown_generator.py**: Markdown生成機能が正しい形式のMarkdownを出力するかをテストするスクリプトです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能の正確性を検証するスクリプトです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能のテストを行うスクリプトです。
    - **test_repository_processor.py**: リポジトリデータ処理機能の正確性を検証するスクリプトです。

## 関数詳細説明
このプロジェクトの主要な関数とその役割は以下の通りです。
- `src/generate_repo_list/generate_repo_list.py` 内の関数:
    - **`main()`**: プログラムのエントリポイント。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力までの一連のワークフローを制御します。
- `src/generate_repo_list/repository_processor.py` 内の関数:
    - **`fetch_repositories(username, token, limit=None)`**: 指定されたGitHubユーザー名とアクセストークンを使用し、GitHub APIからユーザーのリポジトリ情報を取得します。`limit`オプションで取得数を制限できます。
    - **`process_repository_data(repo_data)`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（名前、説明、URL、言語、スター数など）に整形して返します。
- `src/generate_repo_list/markdown_generator.py` 内の関数:
    - **`generate_markdown(repo_list, template_content, seo_data, strings_data)`**: 整形されたリポジトリ情報のリスト、Markdownテンプレート、SEOデータ、表示文字列データを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- `src/generate_repo_list/project_overview_fetcher.py` 内の関数:
    - **`fetch_project_overview(username, repo_name, config, token=None, cache=None)`**: 指定されたリポジトリから設定ファイルで定義されたパスにある `project-overview.md` を読み込み、プロジェクトの3行概要を抽出します。キャッシュ機能も利用可能です。
- `src/generate_repo_list/config_manager.py` 内の関数:
    - **`load_config(config_path)`**: YAML形式のプロジェクト設定ファイル (`config.yml`) を読み込み、Pythonの辞書形式で返します。
    - **`load_secrets(secrets_path)`**: TOML形式のシークレットファイル (`secrets.toml`) を読み込み、GitHubトークンなどの機密情報を取得します。
- `src/generate_repo_list/date_formatter.py` 内の関数:
    - **`format_date(iso_date)`**: ISO 8601形式の日付文字列を、より人間が読みやすい形式に変換します。
- `src/generate_repo_list/badge_generator.py` 内の関数:
    - **`generate_shields_io_badge_markdown(label, message, color)`**: Shields.ioサービスを利用して、指定されたラベル、メッセージ、色のバッジのMarkdownコードを生成します。
- `src/generate_repo_list/url_utils.py` 内の関数:
    - **`build_github_repo_url(username, repo_name)`**: 指定されたGitHubユーザー名とリポジトリ名から、GitHubリポジトリのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-10 07:11:44 JST
