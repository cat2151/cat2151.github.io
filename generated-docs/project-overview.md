Last updated: 2026-03-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、GitHub Pagesサイト向けのリポジトリ一覧Markdownを自動生成するシステムです。
- 検索エンジン最適化された表示により、プロジェクトのリポジトリ情報を効果的に公開・発見可能にします。
- 各リポジトリのプロジェクト概要を自動取得し、動的で魅力的な一覧ページを構築します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースのサイト生成環境), Markdown (生成されるコンテンツのフォーマット)
- 開発ツール: Python (主要な開発言語), GitHub API (リポジトリ情報の取得), PyYAML (設定ファイルの読み書き), argparse (コマンドライン引数解析), requests (HTTPリクエスト処理)
- テスト: pytest (Pythonコードの単体および統合テストフレームワーク)
- ビルドツール: (このプロジェクト自体はMarkdownファイルを生成するものであり、最終的なサイトのビルドはJekyllが担当します)
- 言語機能: Python 3.x (オブジェクト指向プログラミング、標準ライブラリ、データ処理機能)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリにより、自動化ワークフローの存在を示唆)
- 開発標準: ruff (Pythonコードのフォーマットとリンティング), .editorconfig (エディタ設定の統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で、コーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `.github_automation` ディレクトリ内の大規模ファイルチェック機能に関する説明ドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大規模ファイルチェックのルールや設定を定義するTOML形式の設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大規模ファイルを検出し、管理するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定するファイルです（例: ログファイル、ビルド成果物、一時ファイル）。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、使い方、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を保持します。
- **`assets/`**: サイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - `favicon-*.png`: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズを格納します。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや単体テストに利用される可能性のあるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトによってリポジトリ一覧が生成されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したドキュメントです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの挙動をカスタマイズします。
- **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境で必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのリンティングおよびフォーマットツールRuffの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージの初期化ファイル。`src` ディレクトリをPythonパッケージとして扱います。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして扱います。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの状態や情報に基づいて、SVG形式のバッジ画像を生成するロジックを実装しています。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、システム全体の技術的パラメータを設定するためのYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` などの設定ファイルを読み込み、設定値へのアクセスを管理するモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールを協調させて最終的なMarkdownファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: SEOのために構造化データ（JSON-LD）を生成する際のテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、集計するためのロジックを実装しています。
- **`src/generate_repo_list/markdown_generator.py`**: 整形されたリポジトリ情報を受け取り、GitHub Pagesサイト用のMarkdownコンテンツ（リポジトリ一覧）を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出・取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、特定のパターンに一致するバッジ情報（URLやaltテキストなど）を抽出するロジックです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形に整形・加工する主要なロジックを管理します。
- **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータ（タイトル、ディスクリプションなど）のテンプレートを定義します。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する様々な統計情報（スター数、フォーク数など）を計算・集計するためのモジュールです。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元的に管理するためのYAMLファイルです。
- **`src/generate_repo_list/template_processor.py`**: Jekyllのテンプレートエンジンに渡すデータ構造を準備したり、Markdownテンプレートを処理するためのユーティリティを提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールに関連するテストコードを含むファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - `test_badge_generator_integration.py`: バッジ生成機能の統合テストです。
    - `test_check_large_files.py`: 大規模ファイルチェック機能のテストです。
    - `test_config.py`: 設定ファイルの読み込みや管理機能のテストです。
    - `test_date_formatter.py`: 日付フォーマットユーティリティのテストです。
    - `test_environment.py`: テスト環境のセットアップや依存関係に関するテストです。
    - `test_integration.py`: システム全体の機能が意図通りに連携して動作するかを確認するための統合テストを含みます。
    - `test_markdown_generator.py`: Markdown生成機能のテストです。
    - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストです。
    - `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストです。
    - `test_repository_processor.py`: リポジトリ情報処理機能のテストです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py` 内の `main` 関数**:
    - 役割: プログラムのエントリポイント。コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成までの一連のワークフローを調整・実行します。
    - 引数: 内部で `argparse` によりコマンドライン引数を処理します。
    - 戻り値: なし（指定されたファイルパスにMarkdownコンテンツを出力します）。
- **`src/generate_repo_list/repository_processor.py` 内の `process_repositories` 関数 (想定)**:
    - 役割: GitHub APIから取得した生のリポジトリデータリストを受け取り、フィルタリング、並べ替え、必要な情報の抽出などを行い、表示に適した形式に加工します。各リポジトリに対して `project_overview_fetcher` や `readme_badge_extractor` などを呼び出して詳細情報を付加します。
    - 引数: GitHubユーザー名、生のリポジトリデータリスト、GitHubトークン、設定オブジェクト（想定）。
    - 戻り値: 処理済みのリポジトリ情報を含むリスト（想定）。
- **`src/generate_repo_list/project_overview_fetcher.py` 内の `fetch_project_overview` 関数 (想定)**:
    - 役割: 特定のリポジトリ内の指定されたパス（例: `generated-docs/project-overview.md`）からコンテンツを取得し、設定されたセクションタイトルに基づいてプロジェクト概要の3行説明を抽出します。
    - 引数: GitHubユーザー名、リポジトリ名、ターゲットファイルパス、セクションタイトル、GitHubトークン（想定）。
    - 戻り値: 抽出されたプロジェクト概要の文字列リスト、または取得・抽出失敗時には空リストやデフォルト値（想定）。
- **`src/generate_repo_list/markdown_generator.py` 内の `generate_markdown_content` 関数 (想定)**:
    - 役割: 処理済みのリポジトリ情報を受け取り、Jekyllの要件に合わせたフロントマターや、SEO最適化された構造、バッジ、各リポジトリの詳細を含むMarkdown形式の文字列を生成します。
    - 引数: 処理済みのリポジトリ情報リスト、SEOテンプレート、文字列リソース、設定オブジェクト（想定）。
    - 戻り値: 生成されたMarkdownコンテンツの文字列（想定）。
- **`src/generate_repo_list/badge_generator.py` 内の `create_badge_svg` 関数 (想定)**:
    - 役割: 指定されたテキスト、スタイル、色などの情報に基づき、バッジのSVG画像を生成します。
    - 引数: ラベルテキスト、メッセージテキスト、色、スタイルなど（想定）。
    - 戻り値: SVG形式の画像データ文字列（想定）。

## 関数呼び出し階層ツリー
```
generate_repo_list.py (main関数)
├── config_manager.py (設定ファイルを読み込み、設定オブジェクトを初期化)
├── repository_processor.py (リポジトリ情報を取得・処理するコアロジック)
│   ├── project_overview_fetcher.py (各リポジトリの概要ファイルをフェッチし、概要を抽出)
│   ├── readme_badge_extractor.py (リポジトリのREADMEからバッジ情報を抽出)
│   └── statistics_calculator.py (リポジトリの統計情報を計算)
├── markdown_generator.py (整形されたリポジトリ情報からMarkdownコンテンツを生成)
│   ├── template_processor.py (Jekyllテンプレートとデータを結合)
│   ├── badge_generator.py (必要に応じてバッジのSVGを生成)
│   ├── date_formatter.py (日付の表示形式を変換)
│   └── url_utils.py (URLの構築や操作を行うユーティリティ)
└── url_utils.py (グローバルなURL関連のユーティリティ)

---
Generated at: 2026-03-13 07:08:02 JST
