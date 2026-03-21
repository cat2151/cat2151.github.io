Last updated: 2026-03-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、自動でMarkdown形式のリポジトリ一覧を生成します。
- GitHub PagesサイトのSEOを最適化し、リポジトリの発見性を向上させることを目的としています。
- 各リポジトリの概要表示やバッジ、分類機能を提供し、情報 rich な一覧ページを作成します。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレータでGitHub Pagesを構築), GitHub Pages (サイトホスティング)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (スクリプト言語として主要な処理を担当), Git (バージョン管理), GitHub API (リポジトリ情報取得), Ruff (コードフォーマッタ/リンター)
- テスト: Pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Pythonスクリプト (本プロジェクトではPythonスクリプト自体がMarkdownファイルの生成・「ビルド」の役割を担う)
- 言語機能: Python (汎用プログラミング言語としての標準機能を利用)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリで関連スクリプトを管理するが、本プロジェクト自体はCI/CD不要のローカル開発重視)
- 開発標準: Ruff (コードスタイルの一貫性を保つためのリンター/フォーマッタ)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードの整形ルール（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: GitHub Actionsを用いて、リポジトリ内の大きなファイルをチェックする自動化スクリプト群を格納するディレクトリです。
    - **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    - **`check-large-files.toml`**: `check_large_files.py` スクリプトの設定を定義するファイルです。
    - **`scripts/check_large_files.py`**: リポジトリ内の特定の基準を超える大きなファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記載されたファイルです。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使用方法、開発者向けヒントなど、主要な情報を提供するドキュメントです。
- **`_config.yml`**: Jekyllサイトの設定ファイルで、サイトのタイトル、テーマ、プラグインなどの全体設定を定義します。
- **`assets/`**: Jekyllサイトで使用される静的アセット（ファビコン画像など）を格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` の機能をデバッグするために使用される補助スクリプトです。
- **`generated-docs/`**: 各リポジトリの概要ファイル（`project-overview.md`）など、生成されたドキュメントや参照されるドキュメントを格納するプレースホルダーとして機能する可能性があります。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイトの所有権を証明するために使用される認証ファイルです。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧ページのメイン出力ファイルです。
- **`issue-notes/22.md`**: プロジェクト開発中の特定の課題やメモを記録するためのファイルです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、プログレッシブウェブアプリ（PWA）のインストール情報やホーム画面アイコンなどを定義します。
- **`pytest.ini`**: Pytestテストフレームワークの設定ファイルです。テストの発見方法や実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの依存関係をリストアップするファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行するために必要なPythonライブラリの依存関係をリストアップするファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットに使用されるRuffツールの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージの初期化ファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` パッケージの初期化ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種状態（言語、アクティブ/アーカイブなど）を示すバッジのMarkdownを生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、本システム固有の技術的パラメータを設定するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）の読み込みと管理を行うモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を調整します。
- **`src/generate_repo_list/json_ld_template.json`**: JSON-LD形式の構造化データテンプレートで、SEO最適化のためにメタデータを埋め込む際に使用されます。
- **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理・表示するための機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 取得および整形されたリポジトリ情報から、最終的なMarkdown形式の出力文字列を生成する役割を担います。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: 言語バッジ、ステータスバッジ）を抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIからリポジトリデータを取得し、それを必要な形式に加工・フィルタリングする主要なロジックを実装しています。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや構造化データを生成するためのテンプレート設定を定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリの各種統計情報（スター数、フォーク数など）を計算・集計するための機能を提供します。
- **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージや文言を一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（Jekyll構文など）を処理し、動的なコンテンツを挿入する役割を担います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、整形など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` のユニットテストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストケースを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py` の統合テストを記述したファイルです。
    - **`test_check_large_files.py`**: `_github_automation/check_large_files/scripts/check_large_files.py` のテストを記述したファイルです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    - **`test_date_formatter.py`**: 日付整形ユーティリティのテストを記述したファイルです。
    - **`test_environment.py`**: プロジェクトの実行環境に関するテストを記述したファイルです。
    - **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストを記述したファイルです。
    - **`test_markdown_generator.py`**: `markdown_generator.py` のユニットテストを記述したファイルです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のユニットテストを記述したファイルです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のユニットテストを記述したファイルです。
    - **`test_repository_processor.py`**: `repository_processor.py` のユニットテストを記述したファイルです。

## 関数詳細説明
このプロジェクトではPythonスクリプトが多岐にわたる処理を実行しており、各ファイルに複数の関数が存在しますが、主な機能を提供する関数を以下に説明します。

- **`generate_repo_list.py`**
    - `main()`:
        - 役割: スクリプトの主要な実行フローを制御します。GitHub APIからのリポジトリ情報取得、情報の加工、Markdown生成、ファイル出力までの一連の処理をオーケストレートします。
        - 引数: なし (内部でコマンドライン引数をパース)
        - 戻り値: なし
    - `parse_args()`:
        - 役割: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、プログラムが利用できる形式で返します。
        - 引数: なし
        - 戻り値: 解析された引数を含むオブジェクト

- **`repository_processor.py`**
    - `fetch_repositories(username, token, limit=None)`:
        - 役割: 指定されたGitHubユーザー名とトークンを使用して、GitHub APIからリポジトリ情報（公開リポジトリのみ）を取得します。オプションで取得するリポジトリ数を制限できます。
        - 引数: `username` (str): GitHubユーザー名, `token` (str): GitHubパーソナルアクセストークン, `limit` (int, optional): 取得するリポジトリ数の上限。
        - 戻り値: GitHub APIから取得したリポジトリデータのリスト。
    - `process_repository_data(repo_data, config)`:
        - 役割: 取得した生のリポジトリデータを受け取り、プロジェクトの要件に合わせて整形、フィルタリング、追加情報の付与（例: プロジェクト概要の取得）を行います。
        - 引数: `repo_data` (list): 生のリポジトリデータ, `config` (dict): 設定情報。
        - 戻り値: 処理済みのリポジトリデータのリスト。

- **`markdown_generator.py`**
    - `generate_markdown_output(processed_repos, strings)`:
        - 役割: `repository_processor`によって整形されたリポジトリデータを受け取り、最終的なMarkdown形式のリポジトリ一覧文字列を生成します。JekyllのLiquidテンプレート構文なども考慮して生成されます。
        - 引数: `processed_repos` (list): 処理済みのリポジトリデータのリスト, `strings` (dict): 表示に使う文言集。
        - 戻り値: 生成されたMarkdown文字列。

- **`project_overview_fetcher.py`**
    - `get_project_overview(repo_full_name, config, token)`:
        - 役割: 特定のリポジトリ（`repo_full_name`）内の指定されたパス（`config['target_file']`）から、プロジェクト概要の3行説明を抽出し、返します。
        - 引数: `repo_full_name` (str): `owner/repo`形式のリポジトリ名, `config` (dict): 設定情報, `token` (str): GitHubパーソナルアクセストークン。
        - 戻り値: 抽出されたプロジェクト概要の文字列、またはNone。

- **`badge_generator.py`**
    - `generate_badge_markdown(badge_type, value)`:
        - 役割: 指定されたタイプと値に基づいて、リポジトリ情報を視覚的に示すバッジのMarkdown形式（例: Shields.ioのバッジ）を生成します。
        - 引数: `badge_type` (str): バッジの種類 (例: 'language', 'status'), `value` (str): バッジに表示する値。
        - 戻り値: バッジのMarkdown文字列。

- **`config_manager.py`**
    - `load_config(config_path)`:
        - 役割: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (str): 設定ファイルのパス。
        - 戻り値: 設定内容を表す辞書オブジェクト。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-22 07:06:53 JST
