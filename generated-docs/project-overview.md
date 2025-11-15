Last updated: 2025-11-16

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト (`.github.io`ドメイン) 向けに、ユーザーのリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdown形式で出力します。
- 生成された一覧は、検索エンジンやLLMによるリポジトリ参照性を向上させることを目的としています。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースで動作する静的サイトホスティング), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語), Requests (GitHub APIとのHTTP通信), PyYAML (設定ファイル `config.yml`, `strings.yml` の読み込み), Argparse (コマンドライン引数処理), TOML (シークレットファイル `secrets.toml` の管理)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: 該当するビルドツールは直接使用されていません。Pythonスクリプトがコンテンツ生成の役割を担います。
- 言語機能: Python 3.x (標準ライブラリおよび現代的な言語機能)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得に使用), GitHub Actions (GitHub Pagesのデプロイなど、広義の自動化の基盤として利用される可能性はありますが、このプロジェクト自体はローカルでの実行を重視しています。)
- 開発標準: Ruff (PythonコードのLinterおよびFormatter), .editorconfig (エディタの設定統一)

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
index.md
issue-notes/
  10.md
  12.md
  14.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字エンコーディング、行末文字などのコードスタイルを統一するための設定ファイル。
- **.gitignore**: Gitが追跡すべきでないファイルやディレクトリ（例: ビルド成果物、一時ファイル、環境固有の設定ファイルなど）を指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されたファイル。利用者がプロジェクトのコードをどのように使用、配布、変更できるかを定義します。
- **README.md**: プロジェクトの概要、セットアップ方法、使い方、設定、ライセンスなど、プロジェクトに関する基本的な情報を提供するマークダウンファイル。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **assets/**: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **favicon-*.png**: サイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
- **debug_project_overview.py**: `project_overview` 機能のデバッグやテストに特化したスクリプト。
- **generated-docs/**: 各リポジトリから取得したプロジェクト概要など、自動生成されたドキュメントを一時的に格納、または参照されることを想定したディレクトリ。
- **index.md**: 生成されたリポジトリ一覧が書き込まれるメインのマークダウンファイル。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: 開発中の課題やメモを管理するためのマークダウンファイル群を格納するディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリ名、アイコン、開始URLなどを定義するマニフェストファイル。
- **pytest.ini**: pytestフレームワークの設定ファイル。テストの実行オプションやデフォルトの引数などを定義します。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を記述したファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイル。
- **ruff.toml**: PythonコードのLinterおよびFormatterであるRuffの設定ファイル。コードスタイルや静的解析ルールを定義します。
- **src/**: プロジェクトのソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成システムのメインパッケージ。
        - **__init__.py**: Pythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを実装したファイル。
        - **config.yml**: プロジェクト概要取得機能など、システム全体の技術的パラメータを設定するYAMLファイル。
        - **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理する機能を提供するファイル。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、マークダウンファイルを生成する主要なスクリプトのエントリポイント。
        - **json_ld_template.json**: SEO最適化のため、JSON-LD形式の構造化データを生成するためのテンプレートファイル。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形する機能を提供するファイル。
        - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、最終的なマークダウンコンテンツを生成するロジックを実装したファイル。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル (`generated-docs/project-overview.md` など) からプロジェクト概要を自動取得する機能を提供するファイル。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを加工し、必要な情報のみを抽出・整形する機能を提供するファイル。
        - **seo_template.yml**: SEO関連のメタデータやコンテンツ構造に関するテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算・処理する機能を提供するファイル。
        - **strings.yml**: UIメッセージや文言など、表示に関する文字列を一元管理するためのYAMLファイル。多言語対応や文言変更の際に使用されます。
        - **template_processor.py**: マークダウン生成時に使用するテンプレートファイルの処理や、データとの結合を行う機能を提供するファイル。
        - **url_utils.py**: URLの生成、解析、整形など、URL関連のユーティリティ関数を提供するファイル。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能に特化したテストファイル。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを行うファイル。
    - **test_environment.py**: 実行環境や依存関係に関するテストを行うファイル。
    - **test_integration.py**: プロジェクトの複数のコンポーネントが連携して正しく動作するかを確認する統合テストを行うファイル。
    - **test_markdown_generator.py**: マークダウン生成機能の正確性を検証するテストを行うファイル。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールの機能に関するテストを行うファイル。
    - **test_repository_processor.py**: リポジトリデータの処理機能に関するテストを行うファイル。

## 関数詳細説明
具体的な関数名、引数、戻り値の情報は提供されていないため、ファイル名とプロジェクトの機能から推測される主要な関数の役割について、一般的な説明をします。

- **generate_repo_list.py 内の主要関数**:
    - **役割**: プログラムのエントリポイントとして、コマンドライン引数をパースし、設定を読み込み、リポジトリ情報を取得し、最終的なマークダウンファイルを生成する一連の処理をオーケストレーションします。
    - **機能**: 引数解析 (username, output, limit)、設定読み込み、リポジトリデータの取得と処理、マークダウン生成モジュールへのデータ渡し、ファイル書き込み。
    - **引数**: (想定) `username` (str): GitHubユーザー名, `output_file` (str): 出力ファイルパス, `limit` (int, Optional): 処理するリポジトリ数の上限。
    - **戻り値**: (想定) `None` (副作用としてファイル出力) または処理成否を示すブール値。

- **repository_processor.py 内の主要関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、マークダウン生成に適した形式に加工・整形します。
    - **機能**: リポジトリデータのフィルタリング（アーカイブ、フォークなど）、主要なプロパティ（名前、説明、言語、スター数など）の抽出、URLの生成。
    - **引数**: (想定) `raw_repo_data` (dict or list[dict]): GitHub APIレスポンス、`config` (dict): 設定データ。
    - **戻り値**: (想定) `list[dict]` の整形されたリポジトリ情報。

- **project_overview_fetcher.py 内の主要関数**:
    - **役割**: 各リポジトリ内の特定のファイル (`generated-docs/project-overview.md`) から、プロジェクトの概要説明を自動的に抽出します。
    - **機能**: 対象ファイルのコンテンツ取得（GitHub API経由）、マークダウンパーシングによる特定セクションの抽出、複数行の説明の結合。
    - **引数**: (想定) `repo_name` (str): リポジトリ名, `config` (dict): 設定データ (対象ファイル名、セクションタイトルなど)。
    - **戻り値**: (想定) `str` (抽出されたプロジェクト概要) または `None` (見つからない場合)。

- **markdown_generator.py 内の主要関数**:
    - **役割**: 整形されたリポジトリ情報を受け取り、最終的なGitHub Pages向けのマークダウンコンテンツを生成します。
    - **機能**: リポジトリごとのカード/エントリの生成、分類（アクティブ、アーカイブ、フォーク）、JSON-LDなどのSEO要素の組み込み、全体のレイアウト構築。
    - **引数**: (想定) `processed_repo_data` (list[dict]): 整形されたリポジトリ情報, `strings` (dict): 表示文言, `config` (dict): 設定データ。
    - **戻り値**: (想定) `str` (生成されたマークダウンコンテンツ)。

- **badge_generator.py 内の主要関数**:
    - **役割**: リポジトリの言語やステータス（アーカイブなど）に基づいて、マークダウン形式のバッジ文字列を生成します。
    - **機能**: 言語検出と対応するバッジURLの取得、アーカイブ状態を示すバッジの生成、それらをマークダウン形式で整形。
    - **引数**: (想定) `language` (str), `is_archived` (bool)。
    - **戻り値**: (想定) `str` (マークダウン形式のバッジ文字列)。

- **config_manager.py 内の主要関数**:
    - **役割**: YAML形式の設定ファイル (`config.yml`, `strings.yml`) を読み込み、プログラム全体で利用可能な形式で提供します。
    - **機能**: YAMLファイルのパス解決、ファイル内容のパース、辞書形式での設定データ提供。
    - **引数**: (想定) `file_path` (str): 設定ファイルのパス。
    - **戻り値**: (想定) `dict` (読み込まれた設定データ)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-16 07:05:09 JST
