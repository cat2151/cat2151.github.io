Last updated: 2025-11-15

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してGitHub Pages向けに最適化されたマークダウンを生成します。
- 生成されたリポジトリ一覧は検索エンジンからの参照性を高め、LLMがリポジトリ情報を取得しやすくします。
- 各リポジトリの「プロジェクト概要」を自動取得・表示することで、一覧性を向上させ開発効率に貢献します。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages** (マークダウンから静的サイトを生成し公開するプラットフォーム), **Markdown** (生成されるリポジトリ一覧の記述形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (スクリプトの実行環境および主要言語), **pytest** (テストフレームワーク), **ruff** (Pythonコードのリンター兼フォーマッター)
- テスト: **pytest** (Pythonコードの単体・結合テストを実行するためのフレームワーク)
- ビルドツール: **Python** (スクリプト自体がマークダウンファイルの生成を行う役割)
- 言語機能: **Python** (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の取得元として、自動化された情報収集に利用)
- 開発標準: **ruff** (コードの品質と一貫性を保つための自動コードスタイルチェックおよび整形ツール)

## ファイル階層ツリー
```
📄 .editorconfig
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
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 2.md
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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.gitignore**: Gitがバージョン管理しないファイルやディレクトリを指定するファイル。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの概要、目的、使用方法、設定などを示す主要なドキュメント。
- **_config.yml**: Jekyllがサイトを構築する際に使用する設定ファイル。
- **assets/**: Webサイトで使用される画像（ファビコン）などの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのブラウザタブやブックマークに表示されるアイコンファイル。様々なサイズに対応。
- **debug_project_overview.py**: `project_overview_fetcher`の機能や動作をデバッグするためのスクリプト。
- **generated-docs/**: 生成されたマークダウンファイルなどのドキュメントを一時的または最終的に出力するディレクトリ。
- **index.md**: 生成されたリポジトリ一覧が記述される、GitHub Pagesサイトのメインページとなるマークダウンファイル。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを個別のマークダウンファイルとして記録するディレクトリ。
- **manifest.json**: PWA (Progressive Web App) がWebアプリのメタデータを提供するマニフェストファイル。アイコンや表示モードなどを定義。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイル。テスト検出ルールなどを指定。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを記述したファイル。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonコードのリンター兼フォーマッターであるRuffの設定ファイル。コーディング規約や自動修正ルールを定義。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成に関連するモジュール群を格納するパッケージディレクトリ。
        - **__init__.py**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを実装。
        - **config.yml**: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイル。
        - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するクラスや関数を提供。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIから情報を取得し、マークダウンを生成する一連の処理を制御。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データを生成するためのテンプレート。
        - **language_info.py**: GitHubリポジトリの主要言語や使用されている言語に関する情報を処理・分析する機能。
        - **markdown_generator.py**: 取得したリポジトリ情報や統計データ、概要などを用いて、最終的なマークダウンコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に取得する機能。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形、フィルタリング、必要な情報の抽出などの前処理を行うロジック。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するマークダウンやメタデータのテンプレート設定。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能。
        - **strings.yml**: 生成されるマークダウン内で使用される様々な表示メッセージや固定文言を一元管理するファイル。多言語対応の基盤にもなりうる。
        - **template_processor.py**: マークダウン生成時に使用されるテンプレートエンジン（例: Jinja2など）を介して、データとテンプレートを結合し最終的な文字列を生成する処理。
        - **url_utils.py**: URLの検証、構築、パースなど、URL関連のユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher`モジュールに関連する単体テストを定義したファイル。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **test_config.py**: `config_manager`など、設定関連のモジュールのテスト。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテスト。
    - **test_integration.py**: 複数のモジュールが連携して動作する際の統合テスト。
    - **test_markdown_generator.py**: `markdown_generator`モジュールのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor`モジュールのテスト。

## 関数詳細説明
このプロジェクトではPythonスクリプトが主体となって動作するため、主要な機能は各モジュール内の関数として実装されています。具体的な関数のシグネチャは提供されていませんが、ファイル名とプロジェクトの説明から役割を推測し、一般的な引数と戻り値を記述します。

- **`src/generate_repo_list/generate_repo_list.py`内の主要関数**
    - **`main()`**
        - **役割**: スクリプトの実行エントリポイント。引数解析、設定読み込み、リポジトリ情報の取得・処理、マークダウン生成の一連の流れをオーケストレートします。
        - **引数**: `username` (str): GitHubユーザー名, `output_file` (str): 出力マークダウンファイルパス, `limit` (int, Optional): 処理するリポジトリ数の上限（デバッグ用）。
        - **戻り値**: None (処理成功時にファイル出力)

- **`src/generate_repo_list/config_manager.py`内の主要関数**
    - **`load_config(file_path)`**
        - **役割**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - **引数**: `file_path` (str): 設定ファイルのパス。
        - **戻り値**: dict: 設定内容を格納した辞書。
    - **`load_strings(file_path)`**
        - **役割**: 指定されたパスからYAML形式の文字列定義ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - **引数**: `file_path` (str): 文字列定義ファイルのパス。
        - **戻り値**: dict: 文字列定義を格納した辞書。

- **`src/generate_repo_list/repository_processor.py`内の主要関数**
    - **`fetch_all_repositories(username, github_token)`**
        - **役割**: GitHub APIを使用して、指定されたユーザーのリポジトリ情報をすべて取得します。認証にはGitHubトークンを使用します。
        - **引数**: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIアクセス用の認証トークン。
        - **戻り値**: list[dict]: 取得したリポジトリ情報のリスト。
    - **`process_repository_data(raw_repos)`**
        - **役割**: GitHub APIから取得した生のリポジトリデータ（辞書リスト）を、後続処理に適した形式に整形・フィルタリングします。
        - **引数**: `raw_repos` (list[dict]): GitHub APIから取得した生のリポジトリデータのリスト。
        - **戻り値**: list[dict]: 処理済みのリポジトリデータのリスト。

- **`src/generate_repo_list/project_overview_fetcher.py`内の主要関数**
    - **`fetch_project_overview(repo_name, owner, config)`**
        - **役割**: 指定されたリポジトリから、設定ファイルに定義されたパスとセクションタイトルに基づき、3行のプロジェクト概要を抽出します。
        - **引数**: `repo_name` (str): リポジトリ名, `owner` (str): リポジトリの所有者名, `config` (dict): プロジェクト概要取得機能の設定。
        - **戻り値**: str: 抽出された3行のプロジェクト概要文字列、またはNone。

- **`src/generate_repo_list/markdown_generator.py`内の主要関数**
    - **`generate_repository_list_markdown(repositories_data, strings_config)`**
        - **役割**: 処理済みリポジトリデータのリストと文字列設定を使用して、GitHub Pages用のリポジトリ一覧マークダウンコンテンツを生成します。
        - **引数**: `repositories_data` (list[dict]): 処理済みのリポジトリデータのリスト, `strings_config` (dict): 表示文言設定。
        - **戻り値**: str: 生成されたマークダウン文字列。

- **`src/generate_repo_list/badge_generator.py`内の主要関数**
    - **`generate_badges(repository_info)`**
        - **役割**: 特定のリポジトリ情報に基づき、関連する技術スタックやステータスを示すマークダウン形式のバッジ文字列を生成します。
        - **引数**: `repository_info` (dict): 単一リポジトリの情報。
        - **戻り値**: str: 生成されたバッジのマークダウン文字列。

## 関数呼び出し階層ツリー
詳細な関数呼び出し階層は提供されていませんが、プロジェクトの主要な処理フローに基づき、大まかな呼び出し関係を以下に示します。

```
main() (src/generate_repo_list/generate_repo_list.py)
├─── config_manager.load_config()
├─── config_manager.load_strings()
├─── repository_processor.fetch_all_repositories()
│    └─── (GitHub APIへのHTTPリクエスト)
├─── repository_processor.process_repository_data()
│    ├─── project_overview_fetcher.fetch_project_overview()
│    │    └─── (各リポジトリのgenerated-docs/project-overview.mdを読み込み)
│    ├─── badge_generator.generate_badges()
│    └─── statistics_calculator.calculate_statistics()
└─── markdown_generator.generate_repository_list_markdown()
     └─── template_processor.render_template()

---
Generated at: 2025-11-15 07:06:00 JST
