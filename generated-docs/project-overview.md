Last updated: 2026-05-12

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧ページを自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdown形式で出力します。
- 検索エンジンによるクロールを促進し、リポジトリ参照におけるLLMの課題緩和に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として使用され、生成されたMarkdownファイルを静的サイトとして公開), Markdown (自動生成されるコンテンツの形式)
- 音楽・オーディオ: なし
- 開発ツール: Git (バージョン管理), GitHub API (リポジトリ情報取得の主要インターフェース)
- テスト: Pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Python (主要なスクリプト実行環境であり、Markdown生成ロジックを内包), Jekyll (GitHub Pagesが利用する静的サイトジェネレータ)
- 言語機能: Python (GitHub APIとの通信、データ処理、ファイルシステム操作、Markdown生成など、システムの中核を担うプログラミング言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリの存在から、自動化されたワークフローで本システムが利用されることが想定されます)
- 開発標準: Ruff (Pythonコードのフォーマットとリントを行うツールで、コード品質の維持に貢献)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリ。
    - **`check_large_files/`**: 大容量ファイルがリポジトリに含まれていないかチェックする自動化スクリプト群。
        - **`README.md`**: `check_large_files` ディレクトリの概要や使用方法を説明するドキュメント。
        - **`check-large-files.toml`**: `check_large_files.py` スクリプトの設定を定義するファイル。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、開発者向けのヒントなどを記述したメインのドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバルな設定を定義するファイル。
- **`assets/`**: ウェブサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズ。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` の機能を独立してテスト・デバッグするためのスクリプト。
- **`generated-docs/`**: 各リポジトリの概要を自動取得する際に参照される、期待されるドキュメント（例: `project-overview.md`）のパスとして設定されるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認で使用される認証ファイル。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイル。
- **`issue-notes/22.md`**: 特定の課題（Issue #22など）に関するメモや詳細を記録したファイル。
- **`manifest.json`**: ウェブアプリケーションのメタデータを提供し、ホーム画面への追加やPWA (Progressive Web App) 機能を実現するためのファイル。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイル。
- **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイル。
- **`requirements.txt`**: プロジェクトの実行環境で必要なPythonパッケージとそのバージョンを列挙したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、または避けるべきかを指示するファイル。
- **`ruff.toml`**: PythonのコードリンタおよびフォーマッタであるRuffの設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`__init__.py`**: Pythonパッケージの初期化ファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成ロジックのコア部分を格納するPythonパッケージ。
        - **`__init__.py`**: Pythonパッケージの初期化ファイル。
        - **`badge_generator.py`**: リポジトリの言語やステータスに応じたバッジ（アイコン）を生成するロジックを実装したファイル。
        - **`config.yml`**: プロジェクト概要取得機能やAPI呼び出しに関する技術的なパラメータを設定するファイル。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのロジック。
        - **`date_formatter.py`**: 日付や時刻の表示形式を統一するためのユーティリティ関数を提供するファイル。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、整形してMarkdownファイルを生成する、本システムのメインスクリプト。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために構造化データを埋め込むJSON-LDテンプレート。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形するロジック。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリから特定のパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要を自動的に取得するロジック。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するロジック。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に加工・整形するロジック。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレート構造を定義する設定ファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するロジック。
        - **`strings.yml`**: プロジェクト内で使用される表示メッセージや文言を一元管理するためのファイル。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイルを読み込み、データを埋め込む処理を行うロジック。
        - **`url_utils.py`**: URLの構築や解析など、URLに関連する共通のユーティリティ関数。
- **`test_project_overview.py`**: `project_overview_fetcher.py` のユニットテストおよび統合テストを記述したファイル。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`conftest.py`**: Pytestのフィクスチャやプラグインを定義し、複数のテストファイルで共通して利用可能にするファイル。
    - **`test_badge_generator_integration.py`**: `badge_generator.py` の機能が他のコンポーネントと正しく連携するかを検証する統合テスト。
    - **`test_check_large_files.py`**: `check_large_files.py` スクリプトの動作を検証するテスト。
    - **`test_config.py`**: 設定ファイルの読み込みや管理ロジックの正確性を検証するテスト。
    - **`test_date_formatter.py`**: `date_formatter.py` の日付整形機能の正確性を検証するテスト。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係の確認を行うテスト。
    - **`test_integration.py`**: システム全体の主要なフローが正しく動作するかを検証する統合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator.py` が正しいMarkdownを生成するかを検証するテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のリポジトリ概要取得機能の正確性を検証するテスト。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のバッジ抽出機能の正確性を検証するテスト。
    - **`test_repository_processor.py`**: `repository_processor.py` のリポジトリデータ処理機能の正確性を検証するテスト。

## 関数詳細説明
提供された情報からは個別の関数の詳細な役割、引数、戻り値は特定できませんが、ファイル名とプロジェクトの機能から推測される主要な処理を担う関数群は以下の通りです。

- **`generate_repo_list.py` 内の主要関数**:
    - `main()`: プログラムのエントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力といったシステム全体のオーケストレーションを行います。
- **`repository_processor.py` 内の主要関数**:
    - `process_repository(repo_data)`: GitHub APIから取得した生のリポジトリデータを入力として受け取り、表示に必要な情報（名前、説明、URL、言語、スター数、最終更新日など）を抽出し、整形されたデータ構造として返します。
- **`project_overview_fetcher.py` 内の主要関数**:
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLと設定情報に基づき、`generated-docs/project-overview.md`ファイルの内容を取得し、その中から所定の形式で記述された3行のプロジェクト概要を抽出して返します。API呼び出しのキャッシュやリトライ機能も内包すると考えられます。
- **`markdown_generator.py` 内の主要関数**:
    - `generate_markdown(processed_repositories, templates, seo_data)`: `repository_processor`によって整形されたリポジトリデータのリスト、テンプレート、SEO関連データを受け取り、Jekyll互換の最終的なMarkdown文字列を生成します。
- **`badge_generator.py` 内の主要関数**:
    - `generate_language_badge(language)`: 指定されたプログラミング言語に対応するバッジのMarkdownまたはHTMLコードを生成します。
    - `generate_status_badge(status)`: リポジトリのアクティブ/アーカイブ/フォークといったステータスに応じたバッジを生成します。
- **`config_manager.py` 内の主要関数**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、設定値を辞書として提供します。
- **`date_formatter.py` 内の主要関数**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形して返します。

これらの関数は、互いに連携しながら、リポジトリ情報の取得から最終的なMarkdown生成までの一連の処理フローを構成しています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
プロジェクトの主要な処理フローは、以下のステップで構成されていると推測されます。
1. `generate_repo_list.py` の `main` 関数が実行を開始。
2. コマンドライン引数を解析し、GitHubユーザー名や出力ファイル名などを取得。
3. GitHub APIから指定されたユーザーのリポジトリ一覧を取得。
4. 取得した各リポジトリデータに対し、`repository_processor.py` の関数でデータを整形・加工。
5. 各リポジトリについて、`project_overview_fetcher.py` の関数を用いて `project-overview.md` から概要を取得。
6. `badge_generator.py` の関数を使って、リポジトリの言語やステータスに応じたバッジを生成。
7. 整形されたリポジトリデータと生成されたバッジ、SEO情報などを基に、`markdown_generator.py` および `template_processor.py` の関数で最終的なMarkdownコンテンツを構築。
8. 構築されたMarkdownコンテンツを指定された出力ファイル（例: `index.md`）に書き込む。

---
Generated at: 2026-05-12 07:26:40 JST
