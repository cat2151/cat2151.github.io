Last updated: 2026-05-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧と詳細ページを自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownを出力します。
- 検索エンジンによるクロールとLLMによる参照を促進し、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll): 静的サイトジェネレーターであるJekyllを利用し、GitHub Pages上でリポジトリ一覧ページを表示します。Markdown: リポジトリ情報をMarkdown形式で出力し、JekyllによってHTMLに変換されます。
- 音楽・オーディオ: (該当なし)
- 開発ツール: `pytest`: Pythonコードの単体テストおよび統合テストフレームワークです。`ruff`: Pythonコードのリンター兼フォーマッターで、コード品質とスタイルを維持します。
- テスト: `pytest`: プロジェクトの各モジュールや機能が意図通りに動作するか検証するために使用されます。
- ビルドツール: Pythonスクリプト: GitHub APIから取得したデータを元に、Jekyllが解釈可能なMarkdownファイルを生成する主要なツールです。
- 言語機能: Python: メインの開発言語であり、GitHub APIとの連携、データ処理、Markdown生成など全てを担います。YAML: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用されます。TOML: 秘密情報 (`secrets.toml`) や設定ファイル (`ruff.toml`, `check-large-files.toml`) の記述に使用されます。`argparse`: コマンドライン引数を解析し、スクリプトの動作を制御するために使用されます。
- 自動化・CI/CD: GitHub Actions (check_large_files): プロジェクト内の大規模ファイルをチェックするためのGitHub Actionsワークフローが含まれます。本システム自体がMarkdown自動生成という自動化機能を提供します。
- 開発標準: `ruff`: Pythonコードのスタイルガイド強制と自動修正を行います。`.editorconfig`: 異なるエディタ間でのコードスタイルの一貫性を保つための設定ファイルです。

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
-   `.editorconfig`: 異なるエディタ間でのコードの整形ルールを定義し、プロジェクト全体でのコードスタイルの一貫性を保ちます。
-   `.github_automation/check_large_files/README.md`: 大容量ファイルチェック用スクリプトの目的と使用方法を説明するドキュメントです。
-   `.github_automation/check_large_files/check-large-files.toml`: 大容量ファイルチェック用スクリプト（`check_large_files.py`）の設定ファイルです。
-   `.github_automation/check_large_files/scripts/check_large_files.py`: GitHub Actionsで実行され、Gitリポジトリ内の大容量ファイルを検出して警告またはエラーを出すPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理システムが無視すべきファイルやディレクトリのパターンを定義します。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載しており、ソフトウェアの利用、配布、変更の条件を定めます。
-   `README.md`: プロジェクト全体の概要、セットアップ方法、実行コマンド、開発者向けのヒントなどを記述したメインのドキュメントです。
-   `_config.yml`: Jekyllサイトのグローバル設定ファイルで、GitHub Pagesの基本的な動作やサイトのメタデータを制御します。
-   `assets/`: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: ウェブサイトのブラウザタブやブックマークなどに表示されるファビコン（アイコン）の各種サイズです。
-   `debug_project_overview.py`: `src/generate_repo_list/project_overview_fetcher.py`モジュールのデバッグや単体テストを支援するためのスクリプトです。
-   `generated-docs/`: リポジトリの`project-overview.md`ファイルのような、他のリポジトリから自動取得されたドキュメントが格納されることを想定したディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleにおけるサイトの所有権を確認するために配置されるHTMLファイルです。このファイル自体には実行可能な関数やインポートはありません。
-   `index.md`: プロジェクトのメインページとして機能し、自動生成されたリポジトリ一覧が表示されるMarkdownファイルです。JekyllによってHTMLに変換され公開されます。
-   `issue-notes/22.md`: 特定のGitHub Issue（Issue #22）に関するメモや詳細な議論を記録したMarkdownファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブサイトがデバイスのホーム画面に追加された際の表示方法や動作を定義します。
-   `pytest.ini`: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイルです。
-   `requirements-dev.txt`: プロジェクトの開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンを定義します。
-   `requirements.txt`: プロジェクトの実行（本番環境）に必要なPythonパッケージとそのバージョンを定義します。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイト内のどのURLをクロールすべきか、またはクロールを避けるべきかを指示するファイルです。
-   `ruff.toml`: Pythonコードの品質とスタイルを維持するための`ruff`リンターおよびフォーマッターの設定ファイルです。
-   `src/__init__.py`: `src`ディレクトリがPythonパッケージであることを示します。
-   `src/generate_repo_list/__init__.py`: `generate_repo_list`ディレクトリがPythonパッケージであることを示します。
-   `src/generate_repo_list/badge_generator.py`: リポジトリの言語、スター数、ステータスなどの情報に基づいて、Markdown形式のバッジを生成するロジックを提供します。
-   `src/generate_repo_list/config.yml`: プロジェクト概要の取得設定やAPIリトライ数などの技術的パラメータを定義するYAML形式の設定ファイルです。
-   `src/generate_repo_list/config_manager.py`: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`など) を読み込み、アプリケーション全体で設定値を管理するためのモジュールです。
-   `src/generate_repo_list/date_formatter.py`: リポジトリの最終更新日時などの日付情報を、人間が読みやすい形式や特定のフォーマットに変換するためのユーティリティ関数を提供します。
-   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのメインスクリプトで、コマンドライン引数を受け取り、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを指定されたパスに出力します。
-   `src/generate_repo_list/json_ld_template.json`: SEO最適化のために、JSON-LD形式の構造化データを生成する際のテンプレートとして使用されるJSONファイルです。
-   `src/generate_repo_list/language_info.py`: リポジトリで使用されているプログラミング言語の統計情報や表示名を処理・整形するための機能を提供します。
-   `src/generate_repo_list/markdown_generator.py`: 取得・整形されたリポジトリ情報とテンプレートに基づいて、リポジトリ一覧や各リポジトリの詳細を含むMarkdownコンテンツを生成するコアロジックを担います。
-   `src/generate_repo_list/project_overview_fetcher.py`: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動的に取得する機能を提供します。
-   `src/generate_repo_list/readme_badge_extractor.py`: GitHubリポジトリのREADMEファイルの内容を解析し、そこに埋め込まれた特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
-   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に変換、フィルタリング、および追加情報（概要、バッジなど）を付与する主要な処理ロジックを含みます。
-   `src/generate_repo_list/seo_template.yml`: ウェブサイトのSEOに関連するメタタグ、キーワード、その他の設定を定義するためのYAMLファイルです。
-   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算し、整形するための機能を提供します。
-   `src/generate_repo_list/strings.yml`: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言の変更が容易になります。
-   `src/generate_repo_list/template_processor.py`: Markdown生成の際に使用されるテンプレート（文字列）を解析し、プレースホルダーを実際のリポジトリデータで置き換える処理を行います。
-   `src/generate_repo_list/url_utils.py`: URLのパース、結合、エンコードなどの操作を行うための汎用的なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールの機能が期待通りに動作するかを検証するための単体テストスクリプトです。
-   `tests/`: プロジェクトのテストスクリプトをまとめて格納するディレクトリです。
    -   `tests/conftest.py`: `pytest`のテスト実行時に共通して使用されるフィクスチャ（テストデータのセットアップなど）や設定を定義するファイルです。
    -   `tests/test_badge_generator_integration.py`: `badge_generator`モジュールの統合テストで、他のモジュールとの連携を含めた動作を検証します。
    -   `tests/test_check_large_files.py`: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストです。
    -   `tests/test_config.py`: 設定ファイル（`config.yml`など）の読み込みや設定管理機能のテストです。
    -   `tests/test_date_formatter.py`: 日付フォーマット機能（`date_formatter.py`）の各種ケースにおける動作を検証するテストです。
    -   `tests/test_environment.py`: 環境変数や依存関係、システム設定など、実行環境に関するテストです。
    -   `tests/test_integration.py`: システム全体の主要な統合テストで、複数のモジュールが連携して最終結果を生成するプロセスを検証します。
    -   `tests/test_markdown_generator.py`: `markdown_generator`モジュールの機能が、正しいMarkdownを生成するかどうかを検証するテストです。
    -   `tests/test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールの機能テストで、リモートリポジトリからの概要取得が正しく行われるか確認します。
    -   `tests/test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールの機能テストで、READMEからのバッジ抽出が正確に行われるか検証します。
    -   `tests/test_repository_processor.py`: `repository_processor`モジュールの機能テストで、リポジトリデータの処理と整形が正しく行われるか確認します。

## 関数詳細説明
プロジェクト情報からは個別の関数の詳細情報は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-17 07:19:40 JST
