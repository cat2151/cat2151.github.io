Last updated: 2026-08-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してGitHub Pages用のMarkdownファイルを生成します。
- 検索エンジンでのリポジトリ表示改善とLLMからの参照性向上を目的としたSEO最適化システムです。
- リポジトリ概要の自動取得、バッジ表示、アクティブ/アーカイブ/フォーク分類などの機能を備えています。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として動作し、生成されたMarkdownファイルを静的サイトとしてレンダリングします)、**Markdown** (リポジトリ一覧や個々のリポジトリ情報が記述される出力形式です)。
- 音楽・オーディオ: 該当なし。
- 開発ツール: **pytest** (Pythonコードのテストフレームワークとして利用されています)、**ruff** (Pythonコードのリンター兼フォーマッターとしてコード品質とスタイルを維持します)、**GitHub API** (リポジトリ情報をプログラムから取得するためのインターフェースです)。
- テスト: **pytest** (ユニットテスト、結合テスト、統合テストを実行するために使用されます)。
- ビルドツール: **Python** (スクリプトの実行環境および主要な開発言語として使用されます)。
- 言語機能: **Python** (プロジェクトの主要なプログラミング言語であり、リポジトリ情報の取得、処理、Markdown生成の全てを担います)。
- 自動化・CI/CD: **GitHub Pages** (生成されたコンテンツをデプロイし、公開するためのホスティングサービスです)。
- 開発標準: **ruff** (Pythonコードの自動整形とスタイルチェックにより、一貫性のあるコード品質を保ちます)。

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
-   **.editorconfig**: プロジェクト全体でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
-   **_config.yml**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの構成を定義します。
-   **.gitignore**: Gitバージョン管理システムにおいて、追跡対象から除外するファイルやディレクトリのパターンを定義します。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されており、ソフトウェアの利用、配布、変更に関する条件を明示します。
-   **README.md**: プロジェクトの概要、セットアップ方法、使い方、目的など、主要な情報がまとめられたドキュメントです。
-   **assets/**: サイトで使用される静的アセット（画像ファイル、ファビコンなど）を格納するディレクトリです。
    -   **favicon-*.png**: ウェブサイトのブラウザタブやブックマークアイコンとして表示されるファビコン画像ファイルです。
-   **debug_project_overview.py**: `project_overview` 機能のデバッグや単体動作確認のために使用されるスクリプトです。
-   **generated-docs/**: リポジトリごとの `project-overview.md` など、このシステムによって生成または取得されるドキュメントを格納するためのプレースホルダーディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるHTML検証ファイルです。
-   **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧を含むメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
-   **issue-notes/22.md**: プロジェクトの特定の課題（issue #22）に関するメモや詳細情報を記録するためのファイルです。
-   **manifest.json**: ウェブサイトをプログレッシブウェブアプリ (PWA) として機能させるためのマニフェストファイルで、アプリの表示方法や動作を定義します。
-   **pytest.ini**: Pythonのテストフレームワークである `pytest` の設定ファイルで、テストの挙動やオプションを定義します。
-   **requirements-dev.txt**: 開発環境およびテスト実行時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **requirements.txt**: プロジェクトが本番環境で実行される際に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **robots.txt**: 検索エンジンクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいはアクセスを拒否するかを指示するファイルです。
-   **ruff.toml**: Pythonコードのリンター・フォーマッターである `ruff` の設定ファイルで、コーディングスタイルやルールの詳細を定義します。
-   **src/__init__.py**: Pythonのパッケージとして `src` ディレクトリを認識させるための空のファイルです。
-   **src/generate_repo_list/__init__.py**: Pythonのパッケージとして `generate_repo_list` ディレクトリを認識させるための空のファイルです。
-   **src/generate_repo_list/badge_generator.py**: リポジトリの言語やライセンスなどの情報に基づいて、Markdown形式のバッジを生成するロジックを実装しています。
-   **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプトの実行時設定（GitHub APIの設定、プロジェクト概要取得機能の設定など）を定義するファイルです。
-   **src/generate_repo_list/config_manager.py**: `config.yml` やシークレットファイル (`secrets.toml`) などの設定ファイルを読み込み、管理するためのユーティリティモジュールです。
-   **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
-   **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプトで、コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力の全体フローを制御します。
-   **src/generate_repo_list/json_ld_template.json**: SEO最適化のためにJSON-LD形式で構造化データを埋め込む際のテンプレートファイルです。
-   **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語の情報を処理し、表示に適した形式に変換するロジックを実装しています。
-   **src/generate_repo_list/markdown_generator.py**: 取得・処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成する主要なロジックを担います。
-   **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の特定のパス (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を自動的に取得する機能を提供します。
-   **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するためのロジックを実装しています。
-   **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形し、分類（アクティブ、アーカイブ、フォーク）するロジックを実装しています。
-   **src/generate_repo_list/seo_template.yml**: サイトのSEO関連のメタデータや、検索エンジン向けの追加情報を埋め込むためのテンプレート設定ファイルです。
-   **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのユーティリティを提供します。
-   **src/generate_repo_list/strings.yml**: プロジェクト内で使用される表示メッセージや文言を集中管理するための設定ファイルで、国際化や文言統一に役立ちます。
-   **src/generate_repo_list/template_processor.py**: Markdownテンプレートを読み込み、動的なデータ（リポジトリ情報など）を埋め込んで最終的なMarkdownコンテンツを生成するロジックを担います。
-   **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **test_project_overview.py**: `project_overview_fetcher.py` で実装されているプロジェクト概要取得機能のユニットテストを定義しています。
-   **tests/**: プロジェクトの各種テストスクリプトを格納するディレクトリです。
    -   **conftest.py**: `pytest` のフィクスチャやヘルパー関数など、複数のテストファイルで共有される設定を定義します。
    -   **test_badge_generator_integration.py**: `badge_generator.py` の機能が他のモジュールと連携して正しく動作するかを確認する統合テストです。
    -   **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトの機能をテストします。
    -   **test_config.py**: `config_manager.py` による設定ファイルの読み込みや管理が正しく機能するかをテストします。
    -   **test_date_formatter.py**: `date_formatter.py` の日付フォーマット機能が正しく動作するかをテストします。
    -   **test_environment.py**: プロジェクトの実行環境に関する設定や依存関係が正しく機能するかをテストします。
    -   **test_integration.py**: プロジェクトの主要なエンドツーエンドのフローが正しく動作するかを確認する統合テストです。
    -   **test_markdown_generator.py**: `markdown_generator.py` が正しいMarkdownコンテンツを生成するかをテストします。
    -   **test_project_overview_fetcher.py**: `project_overview_fetcher.py` のプロジェクト概要取得機能のユニットテストです。
    -   **test_readme_badge_extractor.py**: `readme_badge_extractor.py` がREADMEからバッジ情報を正確に抽出できるかをテストします。
    -   **test_repository_processor.py**: `repository_processor.py` がリポジトリデータを正しく処理・整形できるかをテストします。

## 関数詳細説明
-   **main (src/generate_repo_list/generate_repo_list.py)**:
    -   役割: プログラムのエントリーポイント。コマンドライン引数の解析から、リポジトリ情報の取得、処理、Markdown生成、最終的なファイル出力まで、全体の処理フローを統括します。
    -   引数: なし (コマンドライン引数は内部で `parse_arguments` により処理)。
    -   戻り値: なし。
-   **parse_arguments (src/generate_repo_list/generate_repo_list.py)**:
    -   役割: コマンドラインから渡される引数（ユーザー名、出力ファイル名、制限数など）を解析し、プログラムで利用可能な形式で返します。
    -   引数: なし。
    -   戻り値: 解析された引数を含むオブジェクト。
-   **load_config (src/generate_repo_list/config_manager.py)**:
    -   役割: `config.yml` などの設定ファイルを読み込み、Pythonオブジェクトとして提供します。
    -   引数: 設定ファイルのパス。
    -   戻り値: 設定内容を格納した辞書またはオブジェクト。
-   **load_secrets (src/generate_repo_list/config_manager.py)**:
    -   役割: GitHubトークンなどの機密情報を含むシークレットファイル (`secrets.toml`) を安全に読み込みます。
    -   引数: シークレットファイルのパス。
    -   戻り値: シークレット内容を格納した辞書またはオブジェクト。
-   **fetch_repositories (src/generate_repo_list/generate_repo_list.py 内部、または別のモジュール)**:
    -   役割: GitHub APIを介して指定されたユーザーのリポジトリ一覧を取得します。必要に応じて、各リポジトリの詳細情報（`project-overview.md` など）も取得します。
    -   引数: GitHubユーザー名、APIトークン、リポジトリ取得制限数。
    -   戻り値: 取得したリポジトリ情報のリスト。
-   **process_single_repository (src/generate_repo_list/repository_processor.py)**:
    -   役割: 生のリポジトリデータを受け取り、表示に必要な情報（バッジ、概要、統計など）を抽出し、整形します。
    -   引数: GitHub APIから取得した単一のリポジトリデータ、設定オブジェクト。
    -   戻り値: 整形されたリポジトリ情報。
-   **fetch_project_overview (src/generate_repo_list/project_overview_fetcher.py)**:
    -   役割: 指定されたリポジトリ内の特定のパス (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を抽出し、返します。
    -   引数: リポジトリ名、オーナー名、設定オブジェクト。
    -   戻り値: 抽出されたプロジェクト概要の文字列リスト、またはデフォルトの概要。
-   **generate_badge_markup (src/generate_repo_list/badge_generator.py)**:
    -   役割: リポジトリの言語やライセンス情報に基づき、表示用のMarkdownまたはHTML形式のバッジを生成します。
    -   引数: バッジの種類（言語、ライセンスなど）、値。
    -   戻り値: バッジのMarkdown/HTML文字列。
-   **generate_full_markdown (src/generate_repo_list/markdown_generator.py)**:
    -   役割: 処理された全リポジトリのデータとテンプレートを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   引数: 処理済みリポジトリデータのリスト、設定オブジェクト。
    -   戻り値: 生成されたMarkdown文字列。
-   **write_output (src/generate_repo_list/generate_repo_list.py 内部)**:
    -   役割: 生成されたMarkdownコンテンツを指定されたファイルに書き出します。
    -   引数: 出力ファイル名、Markdownコンテンツ。
    -   戻り値: なし。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── parse_arguments()
├── config_manager.load_config()
├── config_manager.load_secrets()
├── fetch_repositories()
│   └── project_overview_fetcher.fetch_project_overview()  (各リポジトリに対して呼び出し)
├── repository_processor.process_repositories()  (ループ内で以下を呼び出し)
│   └── repository_processor.process_single_repository()
│       ├── badge_generator.generate_badge_markup()
│       ├── readme_badge_extractor.extract_readme_badges()
│       ├── statistics_calculator.calculate_statistics()
│       └── date_formatter.format_date()
└── markdown_generator.generate_full_markdown()
    ├── markdown_generator.generate_repo_section()  (各リポジトリのセクションを生成)
    └── template_processor.process_template()
    └── url_utils.construct_url()

---
Generated at: 2026-08-13 07:16:51 JST
