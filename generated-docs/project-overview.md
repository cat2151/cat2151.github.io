Last updated: 2026-02-20

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成し、動的なコンテンツを提供します。
- GitHub APIから取得したリポジトリ情報を基に、SEO最適化されたMarkdownファイルを生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照の効率を向上させることを目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースで静的サイトをホスティング)、Markdown (コンテンツ記述形式)
- 音楽・オーディオ: 特になし (本プロジェクトでは音楽・オーディオ関連技術は使用していません)
- 開発ツール: Python (主要なスクリプト言語として利用)、Git (バージョン管理システム)
- テスト: pytest (Pythonコードの単体テストおよび統合テストフレームワーク)
- ビルドツール: 特になし (Jekyllが静的サイトジェネレーターとして機能しますが、本システムはMarkdownファイルを生成するため、直接的なビルドツールは含まれません)
- 言語機能: Python (CLI引数解析、ファイルI/O、HTTPリクエスト処理など)
- 自動化・CI/CD: GitHub Actions (リポジトリ自動生成や大容量ファイルチェックなどの自動化処理)
- 開発標準: ruff (Pythonコードのリンターおよびフォーマッター)、.editorconfig (エディタ間のコードスタイル統一設定)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
  📖 4.md
  📖 6.md
  📖 8.md
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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコードスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプト群を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルがないかチェックするための関連ファイルを含みます。
        - **README.md**: `check_large_files`機能に関する説明です。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイルです。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの概要、目的、使用方法、開発者向けヒントなど、基本的な情報が記載されています。
- **_config.yml**: JekyllベースのGitHub Pagesサイト全体の構成設定を定義するファイルです。
- **assets/**: GitHub Pagesサイトで使用される静的アセット（画像など）を格納するディレクトリです。
    - **favicon-*.png**: 各種デバイス向けに最適化されたファビコン画像ファイルです。
- **debug_project_overview.py**: `project_overview`機能の動作検証やデバッグを目的としたスクリプトです。
- **generated-docs/**: 他のリポジトリから取得した概要などのドキュメントが一時的に生成・保存される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が格納されるメインのMarkdownファイルです。
- **issue-notes/**: 開発過程で発生した課題や検討事項をメモとして記録するためのMarkdownファイル群です。
- **manifest.json**: Progressive Web Apps (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などのメタデータを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonライブラリの依存関係を定義します。
- **requirements.txt**: 本番環境で本システムを実行するために必要なPythonライブラリの依存関係を定義します。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスするかを指示するファイルです。
- **ruff.toml**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **generate_repo_list/**: リポジトリ一覧生成機能の中核をなすPythonパッケージです。
        - **__init__.py**: Pythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリに表示するバッジ（例: スター数、言語）のマークアップを生成するロジックを扱います。
        - **config.yml**: `generate_repo_list`機能固有の設定パラメータ（プロジェクト概要取得の設定など）を定義します。
        - **config_manager.py**: `config.yml`や`secrets.toml`といった各種設定ファイルを読み込み、管理するクラスを提供します。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: プロジェクトの中心となるメインスクリプトで、リポジトリ情報の取得からMarkdown生成までの全体処理をオーケストレートします。
        - **json_ld_template.json**: 検索エンジン最適化のために使用されるJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: プログラミング言語に関する追加情報（色、アイコンなど）を処理するロジックです。
        - **markdown_generator.py**: 取得・処理されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを担います。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得するロジックです。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジ情報などを抽出するロジックです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を整形・処理する主要なロジックを提供します。
        - **seo_template.yml**: 検索エンジン最適化に関連するメタデータやテンプレート設定を定義します。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジックです。
        - **strings.yml**: UIメッセージや各種文言を集中管理し、多言語対応などを容易にするためのファイルです。
        - **template_processor.py**: MarkdownやJSON-LDなどのテンプレートファイルを読み込み、動的なデータで埋め込んで最終出力を生成するロジックです。
        - **url_utils.py**: URLの検証、構築、パースなど、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher`機能の単体テストコードです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストです。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテストです。
    - **test_environment.py**: 実行環境に関する設定や依存関係のテストです。
    - **test_integration.py**: 主要なコンポーネント間の連携を検証する統合テストです。
    - **test_markdown_generator.py**: Markdown生成ロジックのテストです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
    - **test_repository_processor.py**: リポジトリデータ処理ロジックのテストです。

## 関数詳細説明
提供されたプロジェクト情報とファイル構造に基づき、主要なスクリプトファイルとその中に含まれる可能性のある主要な関数について説明します。具体的な引数や戻り値は一般的なパターンとして記述します。

- **`generate_repo_list.py`**
    - **`main()`**:
        - **役割**: プログラムのエントリポイントであり、リポジトリ一覧生成の全プロセスを統括します。コマンドライン引数をパースし、設定をロードし、リポジトリ情報の取得、処理、Markdown生成を順に実行します。
        - **引数**: なし (コマンドライン引数は内部でパース)
        - **戻り値**: なし
        - **機能**: `config_manager`から設定をロードし、`repository_processor`でリポジトリ情報を取得・処理し、`markdown_generator`で最終的な出力ファイルを生成します。
- **`repository_processor.py`**
    - **`fetch_repositories(username: str, token: str, limit: Optional[int] = None)`**:
        - **役割**: GitHub APIを使用して指定されたユーザーのリポジトリ情報を取得します。
        - **引数**: `username` (GitHubユーザー名), `token` (GitHub APIトークン), `limit` (取得するリポジトリ数の上限、オプション)
        - **戻り値**: 取得したリポジトリデータのリスト (辞書形式)
        - **機能**: GitHub APIへのHTTPリクエストを管理し、エラーハンドリングやページネーションを処理してリポジトリデータを収集します。
    - **`process_repository_data(repo_data: Dict, config: Dict)`**:
        - **役割**: GitHub APIから取得した個々のリポジトリデータを整形し、Markdown生成に適した形式に変換します。
        - **引数**: `repo_data` (単一のリポジトリAPIレスポンス), `config` (プロジェクト設定)
        - **戻り値**: 処理済みのリポジトリ情報 (辞書形式)
        - **機能**: リポジトリの言語、スター数、最終更新日などの情報を抽出し、`project_overview_fetcher`で概要を取得したり、`readme_badge_extractor`でバッジ情報を抽出したりします。
- **`project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_name: str, config: Dict)`**:
        - **役割**: 指定されたリポジトリの`generated-docs/project-overview.md`ファイルから3行のプロジェクト概要を抽出します。
        - **引数**: `repo_name` (リポジトリ名), `config` (プロジェクト概要取得機能の設定)
        - **戻り値**: 3行のプロジェクト概要文字列、またはNone
        - **機能**: GitHub APIを介して特定ファイルを読み込み、指定されたセクションから概要をパースします。
- **`markdown_generator.py`**
    - **`generate_markdown_output(repositories: List[Dict], config: Dict)`**:
        - **役割**: 処理済みのリポジトリ情報リストから、GitHub Pages向けの最終的なMarkdownコンテンツを生成します。
        - **引数**: `repositories` (処理済みのリポジトリ情報リスト), `config` (Markdown生成設定)
        - **戻り値**: 生成されたMarkdown文字列
        - **機能**: リポジトリ情報をループし、各リポジトリの表示ブロックを構成し、SEO関連のメタデータやJSON-LD構造化データを組み合わせて完全なMarkdownファイルを構築します。
- **`config_manager.py`**
    - **`load_config(config_path: str)`**:
        - **役割**: YAML形式の設定ファイルを読み込みます。
        - **引数**: `config_path` (設定ファイルへのパス)
        - **戻り値**: 設定内容を表す辞書
        - **機能**: 指定されたパスからYAMLファイルをパースし、アプリケーション全体で使用する設定を提供します。
    - **`load_secrets(secrets_path: str)`**:
        - **役割**: TOML形式の秘密情報ファイル（例: GitHubトークン）を読み込みます。
        - **引数**: `secrets_path` (秘密情報ファイルへのパス)
        - **戻り値**: 秘密情報の内容を表す辞書
        - **機能**: APIトークンなどの機密情報を安全にロードし、設定と分離して管理します。

## 関数呼び出し階層ツリー
```
提供されたプロジェクト情報からは、詳細な関数呼び出し階層ツリーを分析できませんでした。
しかし、主要な処理フローは `src/generate_repo_list/generate_repo_list.py` の `main()` 関数が起点となり、以下のようなモジュール間の連携が想定されます。

main() (src/generate_repo_list/generate_repo_list.py)
├── config_manager.load_config()
├── config_manager.load_secrets()
├── repository_processor.fetch_repositories()
│   └── project_overview_fetcher.fetch_project_overview() (オプション)
└── markdown_generator.generate_markdown_output()
    ├── repository_processor.process_repository_data() (内部でリポジトリごとに呼び出し)
    │   ├── readme_badge_extractor.extract_badges()
    │   ├── statistics_calculator.calculate_statistics()
    │   └── date_formatter.format_date()
    ├── badge_generator.generate_badge_markup()
    └── template_processor.render_template()

---
Generated at: 2026-02-20 07:10:33 JST
