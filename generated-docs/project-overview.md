Last updated: 2026-11-26

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得・処理します。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンへのインデックスを促進し、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの静的サイトジェネレーター)、**Markdown** (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **pytest** (Pythonテストフレームワーク)、**ruff** (Pythonコードリンター・フォーマッター)
- テスト: **pytest** (テスト実行フレームワーク)
- ビルドツール: **Python** (スクリプト実行環境、リポジトリ一覧生成ロジックの基盤)
- 言語機能: **Python** (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の取得)、GitHub Pages (サイト公開プラットフォーム)
- 開発標準: **ruff** (コードスタイル統一)、**.editorconfig** (IDE設定統一)

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
- **.editorconfig**: 複数のエディタやIDE間で一貫したコーディングスタイル（インデント、文字コードなど）を維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトを格納するディレクトリ。
    - **check_large_files/**: 大規模ファイルを検出するためのスクリプト群。
        - **README.md**: `check_large_files` ディレクトリの目的と使い方を説明。
        - **check-large-files.toml**: 大規模ファイルチェックツールの設定ファイル。
        - **scripts/check_large_files.py**: 指定されたサイズを超えるファイルをチェックするPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの概要、セットアップ方法、使い方、機能などを説明する主要なドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定ファイル。テーマ、プラグイン、変数の定義など。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリ。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 各種サイズのファビコン画像。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグや単体テストを行うためのスクリプト。
- **generated-docs/**: プロジェクトのドキュメント生成や、他のリポジトリから取得した概要ファイル (`project-overview.md`) の参照先となるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどの検索エンジン最適化ツールでサイトの所有権を確認するために使用されるファイル。
- **index.md**: 生成されたリポジトリ一覧が格納されるメインのMarkdownファイル。Jekyllによってウェブページとしてレンダリングされる。
- **issue-notes/22.md**: 特定の課題（Issue #22）に関する詳細なメモや検討事項を記録したファイル。
- **manifest.json**: Webアプリケーションマニフェストファイル。プログレッシブウェブアプリ (PWA) の設定やメタデータを定義。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイル。
- **requirements-dev.txt**: 開発環境やテスト環境で必要となるPythonパッケージの依存関係リスト。
- **requirements.txt**: 本番環境で必要となるPythonパッケージの依存関係リスト。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。コード品質とスタイルを維持するために使用。
- **src/**: プロジェクトのソースコードを格納するルートディレクトリ。
    - **__init__.py**: `src` ディレクトリがPythonパッケージであることを示す。
    - **generate_repo_list/**: リポジトリ一覧を生成するコアロジックを格納するパッケージ。
        - **__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示す。
        - **badge_generator.py**: リポジトリのステータスを示すバッジ（アクティブ、アーカイブなど）をMarkdown形式で生成するロジックを実装。
        - **config.yml**: プロジェクト概要取得機能などの技術的パラメータや設定値を定義するYAMLファイル。
        - **config_manager.py**: `config.yml` や外部のシークレットファイル (`secrets.toml`) を読み込み、設定値を管理するモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付情報を、表示に適した形式に変換するユーティリティ関数を提供。
        - **generate_repo_list.py**: プロジェクトのエントリーポイント。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプト。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレート。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に活用するモジュール。
        - **markdown_generator.py**: 処理されたリポジトリデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得する機能を提供。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理に適した形式に変換する役割を担う。
        - **seo_template.yml**: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリ数や言語分布など、リポジトリに関する統計情報を計算するモジュール。
        - **strings.yml**: UIに表示されるメッセージ、ラベル、文言などを管理するファイル。多言語対応に利用されることも。
        - **template_processor.py**: Markdownテンプレートなどに変数を埋め込んだり、特定のフォーマットで出力したりする処理を行う。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの機能に関する単体テストを記述。
- **tests/**: プロジェクトのテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有可能にする。
    - **test_badge_generator_integration.py**: `badge_generator` モジュールと他のコンポーネントとの連携を検証する結合テスト。
    - **test_check_large_files.py**: `check_large_files` 機能のテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理 (`config_manager`) に関するテスト。
    - **test_date_formatter.py**: 日付フォーマット機能のテスト。
    - **test_environment.py**: テスト実行環境のセットアップや依存関係に関するテスト。
    - **test_integration.py**: プロジェクト全体の主要なフローをカバーする統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要の取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリデータの処理機能のテスト。

## 関数詳細説明
このプロジェクトは複数のモジュールで構成されており、各モジュールが特定の役割を担う関数群を提供します。以下に主要な機能とそれを担う関数の概要を説明します。

- **generate_repo_list.py**
    - `main()`:
        - 役割: スクリプトの実行エントリポイント。コマンドライン引数をパースし、リポジトリ一覧生成の主要処理を呼び出します。
        - 引数: なし (コマンドライン引数は内部で処理)。
        - 戻り値: なし。
    - `generate_repo_list(username: str, output_file: str, limit: Optional[int] = None)`:
        - 役割: 指定されたGitHubユーザーのリポジトリ情報を取得し、整形してMarkdownファイルを生成する主要なフローを管理します。
        - 引数:
            - `username`: GitHubのユーザー名。
            - `output_file`: 生成されるMarkdownファイルのパス。
            - `limit`: (オプション) 処理するリポジトリ数の上限（開発用）。
        - 戻り値: なし。

- **repository_processor.py**
    - `fetch_repositories(username: str, token: str)`:
        - 役割: GitHub APIを利用して指定されたユーザーの全リポジトリ情報を取得します。
        - 引数:
            - `username`: GitHubのユーザー名。
            - `token`: GitHub APIへの認証トークン。
        - 戻り値: GitHub APIから取得したリポジトリデータのリスト。
    - `process_repository_data(repo_data: Dict)`:
        - 役割: 取得した生のリポジトリデータから必要な情報を抽出し、整形された辞書形式で返します。
        - 引数:
            - `repo_data`: 単一リポジトリの生データ辞書。
        - 戻り値: 処理済みのリポジトリ情報辞書。

- **project_overview_fetcher.py**
    - `fetch_project_overview(repo_name: str, owner: str, file_path: str, config: Dict)`:
        - 役割: 指定されたリポジトリ内の特定のファイル (`generated-docs/project-overview.md`) から、プロジェクト概要の3行説明を抽出します。
        - 引数:
            - `repo_name`: リポジトリ名。
            - `owner`: リポジトリのオーナー名。
            - `file_path`: 概要ファイルへのパス。
            - `config`: タイムアウトやリトライ回数などの設定。
        - 戻り値: 抽出されたプロジェクト概要の3行説明（文字列リスト）、または取得できなかった場合は空のリスト。

- **markdown_generator.py**
    - `generate_markdown(repositories: List[Dict], config: Dict)`:
        - 役割: 処理されたリポジトリ情報のリストを受け取り、GitHub Pages向けの整形されたMarkdownコンテンツを生成します。
        - 引数:
            - `repositories`: 処理済みのリポジトリ情報辞書のリスト。
            - `config`: Markdown生成に必要な各種設定。
        - 戻り値: 生成されたMarkdownコンテンツの文字列。

- **badge_generator.py**
    - `generate_badge_markdown(status: str)`:
        - 役割: リポジトリのステータス（例: "active", "archived", "fork"）に基づいて、対応するバッジのMarkdownを生成します。
        - 引数:
            - `status`: リポジトリのステータスを示す文字列。
        - 戻り値: バッジのMarkdown文字列。

- **config_manager.py**
    - `load_config(config_path: str)`:
        - 役割: 指定されたパスのYAML設定ファイルを読み込み、辞書形式で返します。
        - 引数:
            - `config_path`: 設定ファイルへのパス。
        - 戻り値: 設定内容を格納した辞書。
    - `load_secrets(secrets_path: str)`:
        - 役割: 指定されたパスのTOML形式のシークレットファイルを読み込み、辞書形式で返します。
        - 引数:
            - `secrets_path`: シークレットファイルへのパス。
        - 戻り値: シークレット内容を格納した辞書。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-26 07:10:45 JST
