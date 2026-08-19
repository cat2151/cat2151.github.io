Last updated: 2026-08-20

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で収集・整理します。
- 取得した情報からJekyllベースのGitHub Pages向けにSEO最適化されたMarkdownファイルを生成します。
- これにより、プロジェクトのリポジトリ一覧が検索エンジンにクロールされやすくなり、情報の可視性を向上させます。

## 技術スタック
- フロントエンド: Jekyll: GitHub Pagesサイトの構築に使用される静的サイトジェネレーターで、生成されたMarkdownファイルを美しいWebページに変換します。
- 音楽・オーディオ: (特になし)
- 開発ツール:
    - GitHub API: リポジトリのメタデータ、READMEの内容、コミット履歴などをプログラム的に取得するために使用されます。
    - pytest: Pythonで書かれたテストコードを効率的に実行するためのフレームワークです。
    - ruff: Pythonコードの品質と一貫性を保つための高速なリンター兼フォーマッターです。
    - Git: プロジェクトのバージョン管理システムとして使用され、コードの変更履歴を管理します。
- テスト: pytest: コードの正確性を検証するための単体テストおよび結合テストの実行に利用されます。
- ビルドツール: (直接的なビルドツールは明示されていませんが、Jekyllがサイト生成の役割を担います)
- 言語機能: Python: プロジェクトの主要な開発言語であり、GitHub APIとの連携やMarkdown生成ロジックの実装に用いられます。
- 自動化・CI/CD: GitHub Pages: 静的サイトをホスティングし、Webサイトを公開するためのプラットフォームです。
- 開発標準: ruff: Pythonコードのスタイルガイド強制、エラー検出、自動修正に使用され、コードの一貫性と保守性を高めます。

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
- **.editorconfig**: 複数のエディタやIDEでコードのスタイル（インデント、改行コードなど）を統一するための設定ファイル。
- **.github_automation/check_large_files/README.md**: 大容量ファイル検出自動化スクリプトに関する説明ドキュメント。
- **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイル検出スクリプトの設定ファイル。
- **.github_automation/check_large_files/scripts/check_large_files.py**: 指定された条件に基づいてリポジトリ内の大容量ファイルをチェックするPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイル。
- **README.md**: プロジェクトの目的、機能、使用方法、設定、ライセンスなどを説明する主要なドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。テーマ、プラグイン、変数の設定など。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグやテストを目的としたスクリプト。
- **generated-docs/**: スクリプトによって生成されたドキュメントやデータが保存されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでのサイト所有権確認に使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py` によって生成される、リポジトリ一覧のメインMarkdownファイル。Jekyllがこれを処理してHTMLページにする。
- **issue-notes/22.md**: 特定のIssue（問題）に関する詳細なメモや解決策が記述されたファイル。
- **manifest.json**: ウェブアプリマニフェスト。プログレッシブウェブアプリ (PWA) の設定を提供し、ホーム画面への追加やオフライン機能などを可能にする。
- **pytest.ini**: pytestの実行設定（テストファイルの発見方法、プラグイン、マーカーなど）を定義するファイル。
- **requirements-dev.txt**: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンを記述したファイル。
- **requirements.txt**: プロジェクトの実行時に必要となる基本的なPythonパッケージとそのバージョンを記述したファイル。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイル。
- **ruff.toml**: Pythonコードリンター・フォーマッターであるRuffの設定ファイル。コードスタイルやチェックルールを定義する。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/badge_generator.py**: リポジトリの言語やステータスなどの情報を視覚的なバッジとして生成するロジックを実装。
- **src/generate_repo_list/config.yml**: プロジェクト概要の取得機能やAPIのリトライ設定など、プロジェクトの技術的パラメータを定義する設定ファイル。
- **src/generate_repo_list/config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するためのユーティリティ関数やクラスを提供。
- **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を指定された形式にフォーマットするためのユーティリティ関数を提供。
- **src/generate_repo_list/generate_repo_list.py**: このプロジェクトの主要な実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を統括。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレート。
- **src/generate_repo_list/language_info.py**: リポジトリの使用言語情報を取得し、処理するためのロジックを実装。
- **src/generate_repo_list/markdown_generator.py**: 取得・整形されたリポジトリ情報に基づいて、最終的なMarkdown形式のコンテンツを生成するロジックを実装。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動的に取得する機能を提供。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリの `README.md` ファイルから、外部サービスへのリンクを示すバッジの情報を抽出するロジック。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Webページ表示に適した形式に加工するロジック。
- **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化 (SEO) に関連するメタデータや記述のテンプレート設定ファイル。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのロジック。
- **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、文言、ラベルなどを一元的に管理するためのファイル。多言語対応の基盤にもなりうる。
- **src/generate_repo_list/template_processor.py**: MarkdownやHTMLのテンプレートを用いて、動的なコンテンツを生成するロジック。
- **src/generate_repo_list/url_utils.py**: URLの構築、解析、エンコードなど、URL操作に関連するユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能が正しく動作するかを検証するためのテストスクリプト。
- **tests/conftest.py**: pytestのテスト実行時に共通して使用されるフィクスチャや設定を定義するファイル。
- **tests/test_badge_generator_integration.py**: `badge_generator.py` の機能が他のコンポーネントと連携して正しく動作するかを検証する結合テスト。
- **tests/test_check_large_files.py**: `check_large_files.py` スクリプトの機能が期待通りに動作するかを検証するテスト。
- **tests/test_config.py**: `config_manager.py` や `config.yml` などの設定関連機能が正しく動作するかを検証するテスト。
- **tests/test_date_formatter.py**: `date_formatter.py` の日付フォーマット機能が正しく動作するかを検証するテスト。
- **tests/test_environment.py**: テスト実行環境や依存関係が正しく設定されているかを検証するテスト。
- **tests/test_integration.py**: プロジェクトの主要なフロー全体が正しく連携し、期待通りの結果を出すかを検証する総合的な結合テスト。
- **tests/test_markdown_generator.py**: `markdown_generator.py` が正しいMarkdownコンテンツを生成するかを検証するテスト。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher.py` が期待通りにプロジェクト概要を取得できるかを検証するテスト。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor.py` がREADMEから正確にバッジ情報を抽出できるかを検証するテスト。
- **tests/test_repository_processor.py**: `repository_processor.py` がリポジトリ情報を正しく整形できるかを検証するテスト。

## 関数詳細説明
- **generate_repo_list.pyのmain()**:
    - 役割: プログラムのエントリーポイント。リポジトリ情報の取得からMarkdownファイルの生成までの一連の処理を調整します。
    - 引数: コマンドライン引数（ユーザー名、出力ファイル名、制限数など）を受け取ります。
    - 戻り値: なし。指定されたパスにMarkdownファイルを出力します。
    - 機能: 設定を読み込み、GitHub APIからリポジトリを取得し、各リポジトリを処理して、最終的なMarkdownコンテンツを生成しファイルに書き出します。
- **project_overview_fetcher.pyのfetch_project_overview(repo_url, owner, repo_name)**:
    - 役割: 指定されたリポジトリの特定のファイル (`project-overview.md`) からプロジェクト概要の3行説明を抽出します。
    - 引数: `repo_url` (リポジトリのURL), `owner` (リポジトリの所有者), `repo_name` (リポジトリ名)。
    - 戻り値: 抽出されたプロジェクト概要のリスト（通常は3行）を返します。取得に失敗した場合は空のリストを返します。
    - 機能: GitHubのコンテンツAPIを介して指定ファイルを読み込み、マークダウンのセクションを解析して概要を抽出します。
- **markdown_generator.pyのgenerate_markdown(repo_data_list)**:
    - 役割: 処理されたリポジトリデータのリストを受け取り、Jekyll形式に整形されたMarkdownコンテンツを生成します。
    - 引数: `repo_data_list` (処理済みのリポジトリ情報を含む辞書のリスト)。
    - 戻り値: 生成されたMarkdown文字列を返します。
    - 機能: テンプレートエンジンと組み合わせて、各リポジトリの詳細（名前、説明、バッジ、概要など）を含むMarkdownセクションを作成し、全体を統合します。
- **repository_processor.pyのprocess_repository(repo_info, github_token, config)**:
    - 役割: GitHub APIから取得した生のリポジトリ情報を受け取り、表示に適した形式に加工・整形します。
    - 引数: `repo_info` (GitHub APIから得られた単一リポジトリの生のデータ), `github_token` (GitHub API認証トークン), `config` (設定オブジェクト)。
    - 戻り値: 整形され、追加情報（プロジェクト概要、バッジなど）が付与されたリポジトリ情報の辞書を返します。
    - 機能: リポジトリの言語情報、スター数、最終更新日などを抽出し、`project_overview_fetcher` を呼び出して概要を取得するなど、追加処理を行います。
- **config_manager.pyのload_config(config_path)**:
    - 役割: 指定されたパスにあるYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    - 引数: `config_path` (設定ファイルへのパス)。
    - 戻り値: 設定内容を表す辞書オブジェクトを返します。
    - 機能: ファイルIOとYAMLパーサーを使用して設定を読み込み、プログラム全体で利用できるようにします。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── load_config() (src/generate_repo_list/config_manager.py)
├── [GitHub API呼び出し] (リポジトリ情報取得)
└── repository_processor.process_repository() (src/generate_repo_list/repository_processor.py) (各リポジトリに対して実行)
    ├── project_overview_fetcher.fetch_project_overview() (src/generate_repo_list/project_overview_fetcher.py)
    ├── readme_badge_extractor.extract_badges_from_url() (src/generate_repo_list/readme_badge_extractor.py)
    ├── badge_generator.generate_badge_data() (src/generate_repo_list/badge_generator.py)
    ├── date_formatter.format_date() (src/generate_repo_list/date_formatter.py)
    └── statistics_calculator.calculate_statistics() (src/generate_repo_list/statistics_calculator.py)
└── markdown_generator.generate_markdown() (src/generate_repo_list/markdown_generator.py)
    └── template_processor.process_template() (src/generate_repo_list/template_processor.py)
└── [ファイル出力]

---
Generated at: 2026-08-20 07:07:08 JST
