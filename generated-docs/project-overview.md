Last updated: 2026-04-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのGitHub Pagesサイト用のコンテンツを自動生成するシステムです。
- 生成されたリポジトリ一覧や各リポジトリへのリンクをGitHub Pagesで公開し、検索エンジン最適化（SEO）を促進します。
- これにより、リポジトリの可視性を高め、検索エンジンやLLMからの参照を容易にすることを目的としています。

## 技術スタック
- フロントエンド: **Jekyll** - GitHub Pagesサイトの構築に使用される静的サイトジェネレーターです。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python** - システム開発の主要言語として使用されています。
    - **GitHub API** - リポジトリ情報やプロジェクト概要などを取得するために利用されます。
    - **ruff** - Pythonコードのスタイルチェックと自動修正を行う高速なリンター兼フォーマッターです。
    - **pytest** - Pythonのテストフレームワークで、機能テストの記述と実行に使用されます。
- テスト: **pytest** - Pythonコードの単体テスト、統合テスト、およびシステムテストの実行に使用されます。
- ビルドツール: 該当するビルドツールは直接的に記載されていませんが、JekyllがGitHub Pagesによってビルドされます。
- 言語機能:
    - **YAML** - プロジェクトの設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）で使用されます。
    - **TOML** - 設定ファイル（`ruff.toml`, `check-large-files.toml`, `secrets.toml`）で使用されます。
- 自動化・CI/CD: **GitHub Actions** - `.github_automation` ディレクトリの存在から、自動化やCI/CDの連携が想定されます。
- 開発標準: **ruff** - コードの品質を保ち、統一されたスタイルを適用するためのツールです。

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
-   `.editorconfig`: 異なるエディタやIDE間でコードスタイルを統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   `check_large_files/`: リポジトリ内の大容量ファイルを検出するためのツール群です。
        -   `README.md`: `check_large_files`ツールの説明ドキュメントです。
        -   `check-large-files.toml`: 大容量ファイルチェックツールの設定ファイルです。
        -   `scripts/check_large_files.py`: 大容量ファイルを検出するPythonスクリプトです。
-   `.gitignore`: Gitによるバージョン管理から除外するファイルやディレクトリを指定する設定ファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの概要、目的、機能、使用方法などを示すメインのドキュメントです。
-   `_config.yml`: Jekyllサイト全体のグローバル設定ファイルで、サイトのタイトル、テーマなどを定義します。
-   `assets/`: サイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ウェブサイトのアイコン）です。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
-   `generated-docs/`: プロジェクトによって生成されたドキュメントやデータが配置される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有者確認で使用される認証ファイルです。
-   `index.md`: GitHub PagesサイトのトップページとなるMarkdownファイルで、通常は生成されたリポジトリ一覧がここに表示されます。
-   `issue-notes/22.md`: 特定のGitHub Issue（Issue #22）に関するメモや詳細情報が記述されたファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリのホーム画面アイコンや表示モードなどを定義します。
-   `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイルです。
-   `requirements-dev.txt`: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンをリスト化したファイルです。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行するために必要となるPythonパッケージとそのバージョンをリスト化したファイルです。
-   `robots.txt`: 検索エンジンクローラーに対して、ウェブサイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
-   `ruff.toml`: Pythonコードのリンター・フォーマッター`ruff`の設定ファイルです。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: GitHubリポジトリ一覧を生成する機能の中核となるモジュール群です。
        -   `__init__.py`: Pythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリの言語やステータスなどのバッジ画像を生成するロジックを扱います。
        -   `config.yml`: リポジトリ一覧生成機能固有の設定（例：プロジェクト概要取得のON/OFF、対象ファイルなど）を定義するファイルです。
        -   `config_manager.py`: YAML設定ファイル（`config.yml`, `strings.yml`）の読み込みと管理を行うモジュールです。
        -   `date_formatter.py`: 日付や時刻の表示形式を調整するユーティリティ機能を提供します。
        -   `generate_repo_list.py`: リポジトリ情報の取得からMarkdown生成までのメイン処理を実行するスクリプトです。
        -   `json_ld_template.json`: JSON-LD形式の構造化データ（SEOメタデータ）のテンプレートファイルです。
        -   `language_info.py`: リポジトリの使用言語情報を処理・分析する機能を提供します。
        -   `markdown_generator.py`: 取得した情報に基づいてMarkdown形式のコンテンツを生成するモジュールです。
        -   `project_overview_fetcher.py`: 各リポジトリから`project-overview.md`などのファイルを探し、その内容（3行概要）を取得する機能です。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、特定のバッジ情報を抽出する機能です。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形・加工する主要な処理を担います。
        -   `seo_template.yml`: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算する機能です。
        -   `strings.yml`: アプリケーション内で使用される表示メッセージや固定文言を多言語対応なども考慮して一元管理するファイルです。
        -   `template_processor.py`: Markdownテンプレートの変数置換などの処理を行う機能です。
        -   `url_utils.py`: URLのパース、生成、検証など、URL関連のユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`モジュールに関連するテストケースを記述したファイルです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest`の共通フィクスチャやヘルパー関数を定義するファイルです。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テストを記述したファイルです。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストを記述したファイルです。
    -   `test_config.py`: 設定ファイル管理機能のテストを記述したファイルです。
    -   `test_date_formatter.py`: 日付フォーマット機能のテストを記述したファイルです。
    -   `test_environment.py`: 開発・実行環境のセットアップや依存関係に関するテストを記述したファイルです。
    -   `test_integration.py`: 主要なコンポーネント間の連携を検証する統合テストを記述したファイルです。
    -   `test_markdown_generator.py`: Markdown生成機能のテストを記述したファイルです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを記述したファイルです。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを記述したファイルです。
    -   `test_repository_processor.py`: リポジトリ情報処理機能のテストを記述したファイルです。

## 関数詳細説明
提供された情報からは、具体的な関数名、引数、戻り値、機能の詳細を特定できませんでした。
ファイル名から推測される一般的な機能は上記の「ファイル詳細説明」に記載されていますが、個々の関数の詳細なシグネチャはコードベースを参照する必要があります。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-04 07:11:07 JST
