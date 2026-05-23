Last updated: 2026-05-24

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、自動で一覧を生成します。
- GitHub Pagesサイト用にSEOに配慮したMarkdown形式で出力を最適化します。
- 検索エンジンからの可視性を高め、リポジトリ情報を効率的に共有するシステムです。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータとして機能し、生成されたMarkdownファイルをHTMLに変換して公開します。)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は利用していません。
- 開発ツール: Python (主要な開発言語)、GitHub API (リポジトリ情報の取得)、pip (Pythonパッケージ管理)。
- テスト: Pytest (Pythonコードの単体テストおよび結合テストフレームワーク)。
- ビルドツール: Jekyll (最終的なウェブサイトの「ビルド」と見なせる静的サイト生成の役割を担います)。
- 言語機能: Python (スクリプトの記述と実行に利用されるプログラミング言語です)。
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリが存在し、自動化されたタスク（例: 大容量ファイルチェック）の実行を示唆していますが、CI/CDパイプラインの具体的な設定はプロジェクト情報に明記されていません。広義の自動化として利用されます)。
- 開発標準: Ruff (Pythonコードのフォーマッター兼リンター)、.editorconfig (エディタ全体でコードスタイルを統一するための設定ファイル)。

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
- **.editorconfig**: エディタのコードスタイル設定（インデント、エンコーディングなど）を定義し、プロジェクト全体で一貫性を保つためのファイル。
- **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定ファイルを格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルを検出し、リポジトリの健全性を保つための自動化スクリプト群。
        - **README.md**: `check_large_files` 機能の目的と使用方法を説明するドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイル。ファイルサイズ制限などを定義。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内で設定された上限を超える大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）が記載されたファイル。
- **README.md**: プロジェクトの概要、目的、機能、利用方法、設定手順などを詳細に説明するメインドキュメント。
- **_config.yml**: Jekyll (GitHub Pages) サイトの全体設定ファイル。サイトタイトル、テーマ、プラグインなどを定義。
- **assets/**: Webサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイル群。
- **debug_project_overview.py**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグやテストに用いられるスクリプト。
- **generated-docs/**: 自動生成されたドキュメント（例: 各リポジトリの概要ファイル `project-overview.md` など）が配置されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認のために配置される認証用HTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイル。Jekyllによってウェブページとして公開される。
- **issue-notes/**: 開発中に発見された課題や検討事項、メモなどを格納するディレクトリ。
    - **22.md**: 特定の課題（例: Issue番号22）に関する詳細なメモや考察が記述されたMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。Webアプリの表示方法や動作を定義。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テストの発見ルール、オプション、フィクスチャなどを定義。
- **requirements-dev.txt**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonコードのリンター兼フォーマッターであるRuffの設定ファイル。コードスタイルや静的解析ルールを定義。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: GitHubリポジトリ一覧を生成するロジックの中核をなすPythonパッケージ。
        - **__init__.py**: `generate_repo_list` パッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成または処理するロジック。
        - **config.yml**: `generate_repo_list` パッケージ固有の設定パラメータを定義するYAMLファイル。
        - **config_manager.py**: YAMLファイルなどの設定ファイルを読み込み、管理するためのモジュール。
        - **date_formatter.py**: 日付や時刻の表示形式を変換・整形するためのユーティリティモジュール。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式で一覧を生成する。
        - **json_ld_template.json**: SEO最適化のため、JSON-LD形式の構造化データを生成するためのテンプレートファイル。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理するモジュール。
        - **markdown_generator.py**: 取得したリポジトリ情報から、SEO最適化されたMarkdownコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から概要の3行説明を抽出するモジュール。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、プロジェクトの状態や利用技術を示すバッジ情報を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整理するモジュール。
        - **seo_template.yml**: SEO（検索エンジン最適化）に関連するテンプレートやメタデータを定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュール。
        - **strings.yml**: アプリケーション内で使用される表示テキストやメッセージを一元管理するためのYAMLファイル（多言語対応や文言修正を容易にする）。
        - **template_processor.py**: Markdown生成時に使用されるテンプレート（Jekyll形式など）を処理し、最終出力を生成するモジュール。
        - **url_utils.py**: URLの検証、構築、パースなど、URLに関連するユーティリティ関数を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得と抽出）を検証するためのテストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: pytestフレームワーク用の設定や共通フィクスチャを定義するファイル。テスト環境のセットアップなどに利用。
    - **test_badge_generator_integration.py**: `badge_generator` モジュールの機能が他のモジュールと連携して正しく動作するかを検証する統合テスト。
    - **test_check_large_files.py**: 大容量ファイルチェック機能が正しく動作するかを検証するテスト。
    - **test_config.py**: 設定管理モジュール（`config_manager.py`など）が正しく設定を読み込み、提供するかを検証するテスト。
    - **test_date_formatter.py**: 日付整形ユーティリティが正しく日付をフォーマットするかを検証するテスト。
    - **test_environment.py**: 実行環境（依存ライブラリ、設定ファイルなど）が正しくセットアップされているかを検証するテスト。
    - **test_integration.py**: プロジェクト全体の主要なフロー（GitHub APIからのデータ取得からMarkdown生成まで）が正しく連携するかを検証する統合テスト。
    - **test_markdown_generator.py**: Markdown生成ロジックが期待通りのMarkdownコンテンツを生成するかを検証するテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールが正しくプロジェクト概要を抽出するかを検証するテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor` モジュールがREADMEから正しくバッジ情報を抽出するかを検証するテスト。
    - **test_repository_processor.py**: リポジトリデータ処理モジュールがGitHub APIレスポンスを正しくパースし、処理するかを検証するテスト。

## 関数詳細説明
提供された情報では個別の関数シグネチャ（引数、戻り値）までは特定できませんでしたが、プロジェクトの機能とファイル構成から主要な関数の役割を以下に推測します。

- **`generate_repo_list.py` 内の主要な関数**:
    - `main()`: このスクリプトのエントリーポイントです。コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、リポジトリ情報の取得、処理、および最終的なMarkdownファイルの生成という一連のプロセスを制御します。
- **`repository_processor.py` 内の主要な関数**:
    - `fetch_repositories(username, token)`: 指定されたGitHubユーザー名とアクセストークンを使用して、GitHub APIから公開リポジトリのリストとその詳細情報を取得します。
    - `process_repository_data(repo_data_list)`: GitHub APIから取得した生のJSON形式のリポジトリデータを受け取り、必要な情報（名前、説明、言語、スター数など）を抽出し、内部で扱いやすい統一されたデータ構造に変換します。
- **`project_overview_fetcher.py` 内の主要な関数**:
    - `fetch_project_overview(repo_name, file_path)`: 特定のリポジトリ（`repo_name`）の指定されたファイルパス（`file_path`、例: `generated-docs/project-overview.md`）から、「プロジェクト概要」セクションに記述された3行の説明文を抽出し、返します。
- **`markdown_generator.py` 内の主要な関数**:
    - `generate_markdown(processed_repo_data, template_config)`: 処理済みのリポジトリデータとMarkdown生成用のテンプレート設定を受け取り、それらを使用してGitHub Pagesサイトに表示されるSEO最適化されたリポジトリ一覧のMarkdownコンテンツを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-05-24 07:20:47 JST
