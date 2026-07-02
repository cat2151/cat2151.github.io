Last updated: 2026-07-03

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成します。
- 検索エンジンにインデックスされにくいGitHubユーザーページのリポジトリ一覧を最適化します。
- GitHub Pagesを通じてリポジトリ情報を公開し、LLMによる参照失敗の緩和とSEO向上を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティングサービス、Jekyllと連携してウェブサイトを公開)、Jekyll (Ruby製の静的サイトジェネレータ、MarkdownファイルをHTMLに変換)、Markdown (GitHub Pagesのコンテンツ記述言語)。
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール: Python (プロジェクトの主要なスクリプト言語、GitHub APIからの情報取得とMarkdown生成に使用)、GitHub API (GitHubのリポジトリ情報をプログラムから取得するためのインターフェース)、YAML (設定ファイル形式、`config.yml`などに使用)、TOML (設定ファイル形式、`secrets.toml`などに使用)。
- テスト: pytest (Pythonアプリケーションのテストフレームワーク)。
- ビルドツール: (このプロジェクト自体は特定のビルドツールを使用せず、Pythonスクリプトがコンテンツ生成と変換を行います)
- 言語機能: Python (動的なスクリプト言語)。
- 自動化・CI/CD: (ローカル開発重視の構成であり、明示的なCI/CDパイプラインは提供情報に含まれません)
- 開発標準: ruff (Pythonの高速なリンター/フォーマッター、コードスタイルの自動修正に利用)。

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードスタイル（インデント、文字コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックのルールや閾値を定義する設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、設定されたルールに基づいて警告またはエラーを出すPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、機能、ライセンスなどを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の挙動を設定するためのファイルで、GitHub Pagesのサイト設定も含まれます。
- **`assets/favicon-16x16.png`**, **`assets/favicon-192x192.png`**, **`assets/favicon-32x32.png`**, **`assets/favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` の機能を独立してテスト・デバッグするための補助スクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルで、生成されたリポジトリ一覧がこのファイルに出力されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22など）に関するメモや詳細を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてウェブサイトを機能させるためのメタデータを提供するファイルです。
- **`pytest.ini`**: `pytest` テストフレームワークの設定ファイルで、テストの実行オプションや発見ルールを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境で必要となるPythonパッケージとその依存関係をリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonパッケージとその依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしても良いか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンターおよびフォーマッターである`ruff`の設定ファイルで、コードスタイルや静的解析のルールを定義します。
- **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるための空ファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` サブディレクトリをPythonサブパッケージとして認識させるための空ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: GitHubリポジトリの状態や技術スタックを示すバッジ（例: Shields.io）を生成するロジックを実装しています。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行に関する各種設定（例: プロジェクト概要取得の有効化、ターゲットファイルパスなど）を定義するファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` や `strings.yml` など、プロジェクトで使用される設定ファイルを読み込み、管理するためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻データを特定のフォーマット（例: `YYYY-MM-DD`）に変換するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトの中核となるスクリプトで、GitHub APIからリポジトリ情報を取得し、その情報を元にMarkdown形式のリポジトリ一覧ファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用されるJSON-LD（構造化データ）のテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要なプログラミング言語情報（使用割合など）を処理・整形するためのモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なMarkdown形式のリポジトリ一覧コンテンツを組み立てるロジックを実装しています。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定の形式のバッジ情報を抽出するスクリプトです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に整形・加工する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) のためのメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのモジュールです。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するためのファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdownテンプレートに変数を埋め込んだり、条件に基づいてコンテンツを生成したりする処理を管理するモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの構築、検証、整形など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能を検証するためのテストスクリプトです。
- **`tests/conftest.py`**: `pytest` テストフレームワークの共通フィクスチャやフックを定義し、テスト間の共通処理を提供します。
- **`tests/test_badge_generator_integration.py`**: `badge_generator.py` モジュールの統合テストを実行し、バッジ生成機能が正しく動作するかを検証します。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能 (`check_large_files.py`) のテストを行うスクリプトです。
- **`tests/test_config.py`**: `config_manager.py` モジュールによる設定ファイルの読み込みと管理が正しく行われるかをテストします。
- **`tests/test_date_formatter.py`**: `date_formatter.py` モジュールの日付フォーマット機能が意図通りに動作するかをテストします。
- **`tests/test_environment.py`**: プロジェクトの実行環境（依存ライブラリの有無など）に関する基本的なチェックを行うテストです。
- **`tests/test_integration.py`**: プロジェクト全体の主要な機能が連携して正しく動作するかを検証する統合テストです。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py` モジュールによるMarkdown生成機能が期待通りの出力をするかをテストします。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールがプロジェクト概要を正しく抽出できるかをテストします。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` モジュールがREADMEファイルからバッジ情報を正確に抽出できるかをテストします。
- **`tests/test_repository_processor.py`**: `repository_processor.py` モジュールがGitHub APIから取得したリポジトリデータを適切に処理・整形できるかをテストします。

## 関数詳細説明
このプロジェクトでは多くのPythonスクリプトファイルが存在し、それぞれが特定のタスクを担っています。主要な処理フローに関わる関数の概要を以下に示します。具体的な引数や戻り値はコードに依存しますが、一般的な役割を記述します。

- **`src/generate_repo_list/generate_repo_list.py` 内の `main()` 関数**
    - 役割: プロジェクト全体の実行エントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力までの一連のフローを制御します。
    - 引数: なし (コマンドライン引数は内部で解析されます)。
    - 戻り値: なし (ファイルのサイドエフェクトとして動作します)。
    - 機能: 設定ファイルの読み込み、GitHub APIクライアントの初期化、指定ユーザーのリポジトリ取得、各リポジトリのデータ整形処理、整形されたデータに基づいたMarkdownコンテンツ生成、指定されたファイルへの書き込みを行います。

- **`src/generate_repo_list/repository_processor.py` 内の `process_repository_data()` 関数**
    - 役割: GitHub APIから取得した単一のリポジトリ生データを受け取り、表示に必要な形式に整形・加工します。他の補助モジュールと連携して詳細情報を収集します。
    - 引数: `repo_data` (dict): GitHub APIから取得した生のリポジトリ情報。
    - 戻り値: `processed_repo` (dict): 整形され、必要な追加情報（例: プロジェクト概要、バッジ）が付加されたリポジトリ情報。
    - 機能: リポジトリの基本的な情報（名前、説明、URL、スター数、言語など）の抽出、`project_overview_fetcher` を使用した概要の取得、`readme_badge_extractor` を使用したバッジ情報の抽出、言語統計やその他のメタデータの集計を行います。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の `fetch_project_overview()` 関数**
    - 役割: 特定のリポジトリ（`repo_name`, `owner`）の指定されたパス（`generated-docs/project-overview.md`など）にあるファイルから、「プロジェクト概要」セクションの3行説明を抽出し、返します。
    - 引数: `repo_name` (str): リポジトリ名。 `owner` (str): リポジトリの所有者名。 `config` (dict): プロジェクト概要取得に関する設定（有効/無効、ファイルパス、セクションタイトルなど）。
    - 戻り値: `overview_text` (str): 抽出された3行のプロジェクト概要説明。見つからない場合は空文字列。
    - 機能: GitHubのRawコンテンツAPIなどを利用して対象ファイルの内容をフェッチし、正規表現や文字列操作を用いて指定されたセクションから該当する行を抽出します。キャッシュ機能も備えています。

- **`src/generate_repo_list/markdown_generator.py` 内の `generate_repo_markdown()` 関数**
    - 役割: `repository_processor` によって整形された複数のリポジトリデータリストと、各種設定（テンプレート、表示文言など）を基に、GitHub Pages用の最終的なMarkdownコンテンツ全体を生成します。
    - 引数: `processed_repos` (list): `process_repository_data` で整形されたリポジトリ情報のリスト。 `template_config` (dict): Markdown生成に使用するテンプレート関連の設定。 `strings_config` (dict): 表示メッセージや文言の設定。
    - 戻り値: `markdown_content` (str): 生成されたリポジトリ一覧のMarkdown形式の文字列。
    - 機能: テンプレートファイルにリポジトリ情報を埋め込み、アクティブ、アーカイブ、フォークなどのカテゴリで分類して表示、バッジの追加、日付のフォーマット、JSON-LDやSEOメタデータの組み込みなどを行います。

- **`src/generate_repo_list/badge_generator.py` 内の `generate_badge_markdown()` 関数**
    - 役割: リポジトリの言語やステータスを示すためのMarkdown形式のバッジ文字列（例: `![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)`）を生成します。
    - 引数: `badge_info` (dict): バッジのテキスト、色、ロゴ、リンクなどの情報を含む辞書。
    - 戻り値: `badge_markdown` (str): 生成されたMarkdown形式のバッジ文字列。
    - 機能: Shields.ioなどのバッジサービスへのURLを構築し、Markdownの画像リンク構文に変換して返します。

## 関数呼び出し階層ツリー
```
main (src/generate_repo_list/generate_repo_list.py)
├───parse_arguments()
├───ConfigManager.load_configs()
│   ├───_load_yaml_config()
│   └───_load_toml_config()
├───GitHubAPIClient.fetch_repositories()
│   └───_make_api_request()
├───for each repository in fetched_repositories:
│   ├───RepositoryProcessor.process_repository_data()
│   │   ├───ProjectOverviewFetcher.fetch_project_overview()
│   │   │   └───_get_github_file_content()  (内部でHTTPリクエストを伴う)
│   │   ├───ReadmeBadgeExtractor.extract_badges()
│   │   ├───LanguageInfo.get_language_breakdown()
│   │   └───StatisticsCalculator.calculate_stats()
│   ├───BadgeGenerator.generate_badge_markdown()
├───MarkdownGenerator.generate_repo_markdown()
│   ├───TemplateProcessor.apply_template()
│   ├───DateFormatter.format_date()
│   ├───UrlUtils.build_repo_url()
│   └───(various string/list manipulations for classification and formatting)
└───write_output_file()

---
Generated at: 2026-07-03 07:25:42 JST
