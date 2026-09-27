Last updated: 2026-09-28

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのGitHub Pagesサイト用Markdownを自動生成します。
- 検索エンジン最適化(SEO)とLLMによる参照改善を目的に、バッジ付きのリポジトリ一覧ページを公開します。
- 各リポジトリの概要、分類、統計などを自動取得・表示し、動的かつ最新の情報を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として動作し、Markdownを静的サイトに変換), Markdown (リポジトリ一覧コンテンツの生成形式)
- 音楽・オーディオ: 特になし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), GitHub API (リポジトリ情報取得元), ruff (PythonコードのLinterおよびFormatter), pytest (Pythonコードのテストフレームワーク)
- テスト: pytest (ユニットテストおよび統合テストの実行)
- ビルドツール: Pythonスクリプト (Markdownファイルを生成する実質的なビルドプロセス), YAML (設定ファイルの定義), Jekyll (GitHub Pages側でのMarkdownからHTMLへの変換)
- 言語機能: Python (バージョン3.8以降を想定し、現代的な言語機能を使用)
- 自動化・CI/CD: GitHub Pages (自動デプロイ機能により、コミットされたMarkdownがウェブサイトとして公開されます), .github_automation (GitHub Actionsを用いた自動化の導入を示唆)
- 開発標準: ruff (コードスタイルと品質の自動チェック・修正ツール), .editorconfig (異なるエディタ間でのコーディングスタイルの統一を強制する設定ファイル)

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
- **README.md**: プロジェクトの概要、目的、主な機能、使用方法、設定、ライセンス情報などを記述した、プロジェクトの入口となる主要なドキュメントファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を定義しており、ソフトウェアの利用、改変、配布に関する条件を示します。
- **.editorconfig**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどのコーディングスタイルを統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例：ビルド成果物、一時ファイル、個人設定）を指定するファイルです。
- **_config.yml**: JekyllベースのGitHub Pagesサイトにおけるグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、Markdownパーサーなどを定義します。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認に使用されるファイルです。ウェブサイトのSEO目的で設置されることが多いです。
- **index.md**: プロジェクトのPythonスクリプトによって生成される、リポジトリ一覧が表示されるメインのMarkdownファイルです。GitHub PagesによってHTMLに変換され、公開されます。
- **manifest.json**: ウェブサイトをプログレッシブウェブアプリ（PWA）として動作させるためのマニフェストファイルです。ホーム画面アイコン、表示モード、起動時のURLなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの発見ルール、プラグイン、コマンドラインオプションなどを指定します。
- **requirements.txt**: プロジェクトの実行時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。本番環境での依存関係を管理します。
- **requirements-dev.txt**: 開発時やテスト時にのみ必要となるPythonパッケージとそのバージョンを列挙したファイルです。開発環境のセットアップに使用されます。
- **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリント・フォーマットツールであるruffの設定ファイルです。コーディング規約、自動修正ルール、無視するファイルなどを定義します。
- **debug_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher`）の動作をデバッグしたり、個別にテストしたりするための補助的なスクリプトです。
- **.github_automation/check_large_files/scripts/check_large_files.py**: GitHub ActionsなどのCI/CD環境で、リポジトリ内に大容量ファイルが存在しないかをチェックし、コミットを防止するなどのルールを適用するためのスクリプトです。
- **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/badge_generator.py**: リポジトリのプログラミング言語、ライセンス、ステータスなどの情報を視覚的なバッジとして表現するMarkdown文字列を生成するロジックを提供します。
- **src/generate_repo_list/config.yml**: 本システムが使用する各種技術的パラメータを定義する設定ファイルです。例えば、プロジェクト概要取得機能の有効/無効、対象ファイルのパスなどが含まれます。
- **src/generate_repo_list/config_manager.py**: `config.yml`などのYAML形式の設定ファイルを安全に読み込み、アプリケーション全体で利用可能なPythonオブジェクトとして管理するためのユーティリティモジュールです。
- **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を特定のフォーマット（例：`YYYY-MM-DD`）に整形するためのユーティリティ関数を提供するモジュールです。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、それらを加工してMarkdown形式のリポジトリ一覧ファイルを生成する、プロジェクトの中心的なメインスクリプトです。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジンの構造化データ（JSON-LD）を生成するためのテンプレートファイルです。SEO強化を目的として、リポジトリ情報をリッチスニペットとして表示するのに役立ちます。
- **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、集計、整形、表示に適した形に変換するロジックを提供します。
- **src/generate_repo_list/markdown_generator.py**: 取得・処理されたリポジトリ情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを構築するためのモジュールです。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）から、そのリポジトリの簡潔なプロジェクト概要を自動的に取得する機能を提供します。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADME.mdファイル内から、既存のCI/CDステータスバッジなどの情報を抽出し、再利用するためのロジックです。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータをフィルタリング、整形し、さらに必要な追加情報（例：ライセンス情報）を取得・統合する処理を行うモジュールです。
- **src/generate_repo_list/seo_template.yml**: サイトのSEO（検索エンジン最適化）に関連するメタデータや、検索結果表示の最適化に関する設定を管理するファイルです。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリごとのスター数、フォーク数、最終更新日などの統計情報を計算し、Markdown出力に含めるためのデータ準備を行います。
- **src/generate_repo_list/strings.yml**: UIに表示される各種メッセージや文言（例：見出し、説明文）を一元的に管理するための設定ファイルです。多言語対応や文言変更を容易にします。
- **src/generate_repo_list/template_processor.py**: Markdownコンテンツ生成時に使用するテンプレートファイル（例：リポジトリごとの表示レイアウト）の処理を行う汎用的なロジックを提供します。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`モジュールに特化したテストや動作確認を行うスクリプトです。
- **tests/**: プロジェクトのユニットテストや結合テストが格納されているディレクトリです。
- **tests/conftest.py**: pytestのフィクスチャやヘルパー関数など、テスト実行全体で共有される設定やユーティリティを定義するファイルです。
- **tests/test_badge_generator_integration.py**: `badge_generator`モジュールの統合テストを行い、バッジの生成が意図通りに行われるかを確認します。
- **tests/test_check_large_files.py**: `.github_automation`内の`check_large_files.py`スクリプトのテストを行い、ファイルサイズのチェック機能が正しく動作するか検証します。
- **tests/test_config.py**: `config_manager`モジュールや`config.yml`の設定が正しく読み込まれ、機能するかをテストします。
- **tests/test_date_formatter.py**: `date_formatter`モジュールのテストを行い、日付のフォーマット機能が正確であることを確認します。
- **tests/test_environment.py**: 実行環境のセットアップや依存関係が正しく機能するかを検証する、環境固有のテストファイルです。
- **tests/test_integration.py**: プロジェクト全体の主要な機能が統合された状態で正しく動作するかを検証する、エンドツーエンドに近い統合テストファイルです。
- **tests/test_markdown_generator.py**: `markdown_generator`モジュールのテストを行い、Markdownコンテンツの生成ロジックが期待通りであることを確認します。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテストを行い、リポジトリ概要の取得と抽出が正しく行われるかを確認します。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのテストを行い、READMEからのバッジ抽出機能が正確であることを検証します。
- **tests/test_repository_processor.py**: `repository_processor`モジュールのテストを行い、リポジトリデータの取得、フィルタリング、整形が正しく機能するかを確認します。

## 関数詳細説明
- **generate_repo_list.py::main()**:
    - 役割: プロジェクトのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdown生成、ファイル出力までの一連の処理をオーケストレーションします。
    - 引数: なし (コマンドライン引数から受け取る)
    - 戻り値: なし
    - 機能: スクリプトの実行フローを制御し、必要なモジュールを呼び出して全体処理を実行します。
- **generate_repo_list.py::generate_repo_list(username, output_file, limit)**:
    - 役割: 指定されたGitHubユーザーのリポジトリ情報を取得し、整形されたMarkdown形式のリポジトリ一覧を生成して出力ファイルに書き込みます。
    - 引数: `username` (str): GitHubユーザー名, `output_file` (str): 出力するMarkdownファイル名, `limit` (int, optional): 処理するリポジトリ数の上限 (開発用、デフォルトはNone)
    - 戻り値: なし
    - 機能: GitHub APIを通じてリポジトリデータを収集し、各種サブモジュールと連携して最終的なMarkdownコンテンツを構築します。
- **repository_processor.py::fetch_repositories(username, token)**:
    - 役割: GitHub APIを利用して、指定されたユーザーが所有する公開リポジトリのリストを取得します。
    - 引数: `username` (str): GitHubユーザー名, `token` (str): GitHub APIアクセストークン
    - 戻り値: (list): 取得したリポジトリデータのリスト (辞書のリスト)
    - 機能: GitHub APIへのリクエストを処理し、リポジトリの基本的な情報を取得します。
- **repository_processor.py::process_repository_data(repositories_data, config)**:
    - 役割: 取得した生のリポジトリデータに対して、フィルタリング、追加情報の取得（例: プロジェクト概要）、および整形処理を適用します。
    - 引数: `repositories_data` (list): 生のリポジトリデータリスト, `config` (dict): プロジェクト設定
    - 戻り値: (list): 処理済みのリポジトリデータリスト (辞書のリスト)
    - 機能: リポジトリの表示に必要な詳細情報を準備し、データの品質と一貫性を確保します。
- **project_overview_fetcher.py::fetch_project_overview(repo_full_name, config)**:
    - 役割: 特定のリポジトリ（例: `user/repo_name`）から、設定されたパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要を抽出します。
    - 引数: `repo_full_name` (str): リポジトリのフルネーム (例: "cat2151/my-repo"), `config` (dict): プロジェクト概要取得機能の設定
    - 戻り値: (str, optional): 抽出された3行のプロジェクト概要、またはNone
    - 機能: 各リポジトリのドキュメントから、簡潔な説明文を効率的に取得します。
- **markdown_generator.py::generate_markdown_output(processed_repos, config, strings)**:
    - 役割: 処理済みのリポジトリデータ、設定、および文字列リソースを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    - 引数: `processed_repos` (list): 処理済みのリポジトリデータリスト, `config` (dict): プロジェクト設定, `strings` (dict): 表示メッセージ・文言データ
    - 戻り値: (str): 生成されたMarkdown文字列
    - 機能: 全体のMarkdown構造を構築し、リポジトリごとの詳細やバッジなどを組み込みます。
- **badge_generator.py::generate_language_badge(language)**:
    - 役割: 指定されたプログラミング言語に対応するバッジのMarkdown文字列を生成します。
    - 引数: `language` (str): プログラミング言語名
    - 戻り値: (str): 言語バッジのMarkdown文字列 (例: `![Python](...)`)
    - 機能: リポジトリの主要言語を視覚的に表現するためのバッジを動的に作成します。
- **config_manager.py::load_config(config_path)**:
    - 役割: 指定されたパスにあるYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    - 引数: `config_path` (str): 設定ファイルのパス
    - 戻り値: (dict): 読み込まれた設定データ
    - 機能: 設定データを一元的に管理し、アプリケーション全体で利用可能にします。
- **date_formatter.py::format_date(timestamp, format_string="%Y-%m-%d")**:
    - 役割: Unixタイムスタンプまたは日付文字列を、指定されたフォーマット文字列に従って整形します。
    - 引数: `timestamp` (int or str): 日付/時刻データ, `format_string` (str, optional): 出力フォーマット文字列 (デフォルトは"%Y-%m-%d")
    - 戻り値: (str): フォーマットされた日付文字列
    - 機能: 日付表示の一貫性を保ち、ユーザーフレンドリーな形式を提供します。
- **url_utils.py::build_repo_url(username, repo_name)**:
    - 役割: 指定されたユーザー名とリポジトリ名に基づいて、GitHubリポジトリの完全なURLを構築します。
    - 引数: `username` (str): GitHubユーザー名, `repo_name` (str): リポジトリ名
    - 戻り値: (str): 構築されたリポジトリURL (例: "https://github.com/cat2151/example-repo")
    - 機能: URL生成処理を一元化し、URL構造の変更に柔軟に対応できるようにします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-28 07:11:32 JST
