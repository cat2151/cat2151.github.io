Last updated: 2026-09-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages用のMarkdownファイルを自動生成します。
- 生成されたリポジトリ一覧はSEOに最適化され、検索エンジンからの発見性を高めます。
- 各リポジトリの概要やバッジ、分類を自動表示し、開発プロジェクトの参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll: 生成されたMarkdownファイルをGitHub Pages上で静的サイトとして公開・表示するための静的サイトジェネレーターです。
- 音楽・オーディオ: なし
- 開発ツール:
    - pytest: Pythonで書かれた強力なテストフレームワークで、プロジェクトの機能が期待通りに動作するかを検証します。
    - ruff: 高速なPythonリンターおよびフォーマッターで、コードスタイルの一貫性を保ち、品質を向上させます。
- ビルドツール: Python: スクリプトの実行環境として使用され、GitHub APIからの情報取得やMarkdownファイルの生成処理を担います。
- 言語機能: Python: 主にPython言語の標準機能やライブラリを活用し、リポジトリ情報の処理やファイル操作を行います。
- 自動化・CI/CD: なし (ローカル開発重視の構成)
- 開発標準: ruff: コードのスタイルを統一し、読みやすく保守しやすいPythonコードを維持するためのルールを提供します。

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
- **`.editorconfig`**: 異なる開発者やエディタ間でのコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックするためのスクリプト群を格納しています。
        - **`README.md`**: `check_large_files` ディレクトリに関する説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出し、警告するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明する、主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllを使用するGitHub Pagesサイト全体のグローバル設定を定義するファイルです。
- **`assets/`**: GitHub Pagesサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズ画像ファイルです。
- **`debug_project_overview.py`**: 各リポジトリの `project-overview.md` ファイルの取得機能をデバッグするためのスクリプトです。
- **`generated-docs/`**: `project-overview.md` など、動的に生成されるドキュメントを一時的に格納したり、参照元として機能したりするディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト認証に使用される、特定のコンテンツを持つHTMLファイルです。
- **`index.md`**: メインの実行スクリプトによって、GitHubリポジトリ一覧がMarkdown形式で出力されるファイルです。これがGitHub Pagesで公開されます。
- **`issue-notes/`**: プロジェクトの課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（おそらくIssue #22）に関するメモファイルです。
- **`manifest.json`**: PWA (Progressive Web App) のマニフェストファイルで、ウェブアプリの表示方法や動作を定義します。
- **`pytest.ini`**: `pytest` テストフレームワークの動作設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonライブラリの依存関係を記述したファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働に必要なPythonライブラリの依存関係を記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいは除外すべきかを指示するファイルです。
- **`ruff.toml`**: `ruff` リンターおよびフォーマッターの動作設定を定義するファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要ロジックを格納するPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list` がPythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術を示すバッジ画像を生成または管理するロジックを実装しています。
        - **`config.yml`**: プロジェクト概要取得機能などの技術的パラメータや、リトライ回数、タイムアウト時間といった実行時設定を定義するファイルです。
        - **`config_manager.py`**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdown形式のリポジトリ一覧を生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために使用される、構造化データ（JSON-LD）のテンプレートファイルです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理・整形するロジックを実装しています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得するロジックを担います。
        - **`readme_badge_extractor.py`**: 各リポジトリの `README.md` からバッジ情報を抽出するためのロジックを実装しています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に整形・加工するモジュールです。
        - **`seo_template.yml`**: サイトの検索エンジン最適化（SEO）に関連するメタデータや記述のテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する各種統計情報（スター数、フォーク数など）を計算するロジックを提供します。
        - **`strings.yml`**: プロジェクト内で表示されるメッセージ、ラベル、文言などを一元的に管理するための設定ファイルです。
        - **`template_processor.py`**: Markdown生成時に使用するJinja2などのテンプレートエンジンを介して、コンテンツを組み立てる処理を担います。
        - **`url_utils.py`**: URLの生成、検証、エンコードなど、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能に関するテストを記述したファイルです。
- **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: `pytest` のテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator` モジュールの統合テストを行うファイルです。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトのテストを行うファイルです。
    - **`test_config.py`**: `config_manager` モジュールなど、設定関連のロジックをテストするファイルです。
    - **`test_date_formatter.py`**: `date_formatter` モジュールの機能に関するテストを行うファイルです。
    - **`test_environment.py`**: 実行環境の設定や前提条件に関するテストを行うファイルです。
    - **`test_integration.py`**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テストファイルです。
    - **`test_markdown_generator.py`**: `markdown_generator` モジュールの機能に関するテストを行うファイルです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールの機能に関するテストを行うファイルです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールの機能に関するテストを行うファイルです。
    - **`test_repository_processor.py`**: `repository_processor` モジュールの機能に関するテストを行うファイルです。

## 関数詳細説明
提供された情報からは、各関数の役割、引数、戻り値、機能を詳細に特定できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-19 07:11:10 JST
