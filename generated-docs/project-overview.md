Last updated: 2026-10-17

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pagesサイト用のMarkdownファイルを自動生成するシステムです。
- 検索エンジン最適化（SEO）とLLMの参照性向上を目指し、リポジトリ一覧や各リポジトリへのリンクを公開します。
- 各リポジトリの概要自動取得など、GitHub Pagesサイトのリポジトリ情報をリッチにする機能を提供します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースの静的サイトホスティング), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要開発言語), GitHub API (リポジトリ情報取得), Pytest (テストフレームワーク), Ruff (コードフォーマッタ・リンタ), YAML (設定ファイル形式), TOML (秘密情報・設定ファイル形式)
- テスト: Pytest (Python用テストフレームワーク)
- ビルドツール: このプロジェクトはPythonスクリプトでMarkdownファイルを「生成」するため、特定のビルドツールは直接使用しません。Pythonスクリプト自体が生成プロセスを担います。
- 言語機能: Python (データ処理、ファイルI/O、HTTP通信、テキスト生成、引数解析など)
- 自動化・CI/CD: 直接的なCI/CDパイプラインは含まれませんが、生成されたMarkdownはGitHub Pagesで自動デプロイされることを想定しています。
- 開発標準: Ruff (Pythonコードの品質維持、静的解析), .editorconfig (エディタ設定の統一)

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
- `.editorconfig`: エディタのコードスタイル設定をプロジェクト全体で統一するための設定ファイルです。
- `.github_automation/`: GitHub Actionsなどで利用される自動化スクリプトや設定を格納するディレクトリです。
  - `check_large_files/`: リポジトリ内の大容量ファイルをチェックする自動化スクリプト群です。
    - `README.md`: `check_large_files` 機能に関する説明ドキュメントです。
    - `check-large-files.toml`: `check_large_files` スクリプトの設定ファイルです。
    - `scripts/check_large_files.py`: 大容量ファイルを検出するためのPythonスクリプトです。
- `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- `README.md`: プロジェクト全体の概要、セットアップ方法、使用方法、開発者向けのヒントなどを記述したメインドキュメントです。
- `_config.yml`: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどを定義します。
- `assets/`: GitHub Pagesサイトで使用される静的アセット（ファビコンなどの画像ファイル）を格納するディレクトリです。
  - `favicon-*.png`: ウェブサイトのファビコン画像ファイルです。
- `debug_project_overview.py`: `project_overview` 取得機能のデバッグ用途に利用されるスクリプトです。
- `generated-docs/`: プロジェクト概要などを自動取得する際の対象となるファイルが格納されることが想定されるディレクトリです。
- `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- `index.md`: GitHub Pagesサイトのトップページとして機能するMarkdownファイルで、生成されたリポジトリ一覧が出力されます。
- `issue-notes/`: 開発中の課題やメモを記録するためのディレクトリです。
  - `22.md`: 特定の課題（例: Issue #22）に関するメモや詳細を記述したファイルです。
- `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、アプリの表示方法やアイコンなどを定義します。
- `pytest.ini`: `pytest` テストフレームワークの設定ファイルです。
- `requirements-dev.txt`: 開発環境やテスト実行に必要なPythonパッケージの依存関係を定義するファイルです。
- `requirements.txt`: 本番環境で必要なPythonパッケージの依存関係を定義するファイルです。
- `robots.txt`: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてよいか、または除外するかを指示するファイルです。
- `ruff.toml`: Pythonのコードリンタおよびフォーマッタである `ruff` の設定ファイルです。
- `src/`: プロジェクトのPythonソースコードを格納するメインディレクトリです。
  - `__init__.py`: Pythonパッケージであることを示すファイルです。
  - `generate_repo_list/`: GitHubリポジトリ一覧生成機能のコアロジックを格納するPythonパッケージです。
    - `__init__.py`: `generate_repo_list` パッケージであることを示すファイルです。
    - `badge_generator.py`: リポジトリ一覧に表示されるバッジ（例: 言語バッジ、ステータスバッジ）を生成するロジックを含みます。
    - `config.yml`: リポジトリ一覧生成スクリプトの動作を制御するための設定ファイルです（例: プロジェクト概要取得機能の設定）。
    - `config_manager.py`: YAMLやTOML形式の設定ファイルを読み込み、プロジェクト全体で管理するためのユーティリティモジュールです。
    - `date_formatter.py`: 日付や時刻の情報を特定のフォーマットで整形するためのユーティリティ関数を提供します。
    - `generate_repo_list.py`: メインの実行スクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式の出力ファイルを生成します。
    - `json_ld_template.json`: SEO強化のために、構造化データ（JSON-LD）を生成する際のテンプレートファイルです。
    - `language_info.py`: リポジトリごとのプログラミング言語の使用状況や関連情報を処理するロジックを含みます。
    - `markdown_generator.py`: 取得したリポジトリ情報や設定に基づいて、最終的なMarkdownコンテンツを生成するロジックを担います。
    - `project_overview_fetcher.py`: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出するロジックを含みます。
    - `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジックを含みます。
    - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に整形するロジックを担います。
    - `seo_template.yml`: SEO関連のメタデータや、検索エンジン最適化のためのコンテンツ構造に関するテンプレート設定を定義します。
    - `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計するロジックを含みます。
    - `strings.yml`: UIに表示されるメッセージや文言、ラベルなどを一元的に管理するための設定ファイルです。
    - `template_processor.py`: Markdownやその他のテンプレートファイルを処理し、動的なデータを埋め込んで最終的なコンテンツを生成する汎用的なロジックです。
    - `url_utils.py`: URLの構築、解析、検証など、URLに関連するユーティリティ関数を提供します。
- `test_project_overview.py`: `project_overview` 取得機能のユニットテストを記述したスクリプトです。
- `tests/`: プロジェクトのユニットテストや統合テストを格納するディレクトリです。
  - `conftest.py`: `pytest` のテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
  - `test_badge_generator_integration.py`: `badge_generator` モジュールの統合テストを記述したファイルです。
  - `test_check_large_files.py`: `.github_automation/check_large_files.py` スクリプトのテストを記述したファイルです。
  - `test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理に関するテストを記述したファイルです。
  - `test_date_formatter.py`: `date_formatter` モジュールの日付整形機能のテストを記述したファイルです。
  - `test_environment.py`: テスト実行環境の準備や設定に関するテストを記述したファイルです。
  - `test_integration.py`: システム全体の主要なフローに関する統合テストを記述したファイルです。
  - `test_markdown_generator.py`: `markdown_generator` モジュールのMarkdown生成ロジックのテストを記述したファイルです。
  - `test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールのプロジェクト概要取得機能のテストを記述したファイルです。
  - `test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールのREADMEからのバッジ抽出機能のテストを記述したファイルです。
  - `test_repository_processor.py`: `repository_processor` モジュールのリポジトリデータ処理ロジックのテストを記述したファイルです。

## 関数詳細説明
提供された情報から具体的な関数名、引数、戻り値、機能を詳細に説明することはできません。
各ファイルの役割から推測される主要な処理を以下に示します。

- **`generate_repo_list.py` の主要な処理**: GitHub APIと対話し、リポジトリ情報を取得し、整形されたMarkdown形式で出力ファイルを生成するメインの処理を実行します。
- **`badge_generator.py` の主要な処理**: リポジトリの属性（言語、ステータスなど）に基づき、ウェブページに表示するための視覚的なバッジ（アイコンやラベル）を生成します。
- **`config_manager.py` の主要な処理**: プロジェクトで使用されるYAMLやTOML形式の設定ファイルを読み込み、設定値へのアクセスや管理を抽象化します。
- **`date_formatter.py` の主要な処理**: 日付や時刻データを指定された形式の文字列に変換し、人間が読みやすい形式で表示するための処理を提供します。
- **`language_info.py` の主要な処理**: GitHubリポジトリの言語分布情報などを解析し、各言語に関する詳細情報や視覚化のためのデータを提供します。
- **`markdown_generator.py` の主要な処理**: 取得・整形されたリポジトリデータと定義されたテンプレートを用いて、最終的なMarkdown形式のコンテンツを生成します。
- **`project_overview_fetcher.py` の主要な処理**: GitHubリポジトリ内の特定のパスに存在する「プロジェクト概要」ファイルの内容を非同期的に取得し、そのテキストデータを抽出します。
- **`readme_badge_extractor.py` の主要な処理**: リポジトリのREADMEファイルの内容を解析し、そこに埋め込まれたバッジ（例：CI/CDステータス、ライセンス）のURLやテキストを抽出します。
- **`repository_processor.py` の主要な処理**: GitHub APIから直接取得した生のリポジトリデータを、アプリケーションが扱いやすい標準化された内部データ構造に変換・加工します。
- **`statistics_calculator.py` の主要な処理**: リポジトリのスター数、フォーク数、オープンイシュー数、最終コミット日時などの統計情報を計算し、集計結果を提供します。
- **`template_processor.py` の主要な処理**: テンプレートファイル（例：Markdownテンプレート）内のプレースホルダを、実際のデータで置き換えて最終的なコンテンツをレンダリングします。
- **`url_utils.py` の主要な処理**: URLの構築、パスの結合、URLの検証、エンコード・デコードなど、URL操作に関する汎用的なユーティリティ機能を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-17 07:11:24 JST
