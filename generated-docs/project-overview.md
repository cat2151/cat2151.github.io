Last updated: 2025-11-30

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・処理します。
- 取得した情報からGitHub Pages向けにSEO最適化されたリポジトリ一覧をMarkdownで生成します。
- 検索エンジンからのクロールを促進し、リポジトリの可視性とLLMによる参照性を向上させます。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング基盤), Jekyll (GitHub Pagesが利用する静的サイトジェネレーター), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: (該当する技術がプロジェクト情報にないため、記載しません)
- 開発ツール: GitHub API (リポジトリ情報取得元), Python (主要な開発言語およびスクリプト実行環境), VS Code (.editorconfigを通じてコードスタイルを統一)
- テスト: pytest (Pythonコードの単体テストおよび統合テストフレームワーク)
- ビルドツール: Python (スクリプトとしてMarkdownファイルを生成), YAML (設定ファイルやテンプレートの記述に利用)
- 言語機能: Python (汎用プログラミング言語として、リポジトリ情報の取得、加工、Markdown生成のロジックを実装)
- 自動化・CI/CD: (ローカル開発重視のため、特定のCI/CDツールは使用していません。依存関係管理として`requirements.txt`を使用します)
- 開発標準: ruff (Pythonコードのリンティングと自動フォーマットツール), EditorConfig (異なるエディタ間でのコードスタイル統一設定)

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
- **.editorconfig**: さまざまなエディタ間でコードの書式設定（インデント、改行コードなど）を統一するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **LICENSE**: 本プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、使い方、設定方法などが記載された主要なドキュメントファイルです。
- **_config.yml**: GitHub Pagesで利用されるJekyllのサイト全体の設定ファイルです。
- **assets/**: GitHub Pagesサイトで使用される静的アセット（画像ファイルなど）を格納するディレクトリです。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのタブやブックマークなどに表示されるファビコンの各サイズ画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグや単体動作確認のために使用される補助スクリプトです。
- **generated-docs/**: プロジェクトによって自動生成される、各リポジトリの概要説明Markdownファイルなどが格納されることが想定されるディレクトリです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイルです。GitHub Pagesサイトのトップページとして機能します。
- **issue-notes/**: 開発過程で発生した課題や検討事項に関するメモがMarkdown形式で個別のファイルとして記録されているディレクトリです。
    - `10.md`, `12.md`, `14.md`, `2.md`, `4.md`, `6.md`, `8.md`: 各課題の詳細な情報や議論が記述されたメモファイルです。
- **manifest.json**: Progressive Web App (PWA) マニフェストファイルです。ウェブサイトをモバイルデバイスにアプリのようにインストールするための情報（アイコン、表示モードなど）を提供します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の挙動を制御するための設定ファイルです。
- **requirements-dev.txt**: 開発環境やテスト実行時に必要となるPythonパッケージとそのバージョンをリスト化したファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージとそのバージョンをリスト化したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールして良いか、または避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンターおよびフォーマッターである`ruff`の設定ファイルです。コードの品質と一貫性を保ちます。
- **src/__init__.py**: `src`ディレクトリをPythonパッケージとして認識させるための初期化ファイルです。
- **src/generate_repo_list/**: リポジトリ一覧自動生成システムの主要なPythonロジックを格納するパッケージです。
    - `__init__.py`: `generate_repo_list`パッケージの初期化ファイルです。
    - `badge_generator.py`: リポジトリのステータスや使用技術を示すバッジのMarkdown文字列を生成するロジックを含みます。
    - `config.yml`: プロジェクト固有の各種設定（例: プロジェクト概要機能の有効/無効、タイムアウト時間など）を定義するYAML形式の設定ファイルです。
    - `config_manager.py`: `config.yml`やシークレット情報（`secrets.toml`など）を読み込み、管理する役割を担います。
    - `generate_repo_list.py`: このプロジェクトのメインスクリプトであり、GitHub APIからの情報取得、データの処理、Markdownファイルの生成という一連の処理を実行します。
    - `json_ld_template.json`: SEO強化のため、検索エンジンがリポジトリ情報をより良く理解できるよう構造化データ（JSON-LD）を生成するためのテンプレートファイルです。
    - `language_info.py`: 各リポジトリで使用されているプログラミング言語の情報を取得し、その割合などを分析するロジックを提供します。
    - `markdown_generator.py`: 処理済みのリポジトリ情報から、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックを実装しています。
    - `project_overview_fetcher.py`: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出し取得する機能を提供します。
    - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
    - `seo_template.yml`: SEO関連のメタデータやコンテンツ構造に関するテンプレート設定を定義するファイルです。
    - `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックを提供します。
    - `strings.yml`: UIに表示される各種メッセージやラベル、文言などを一元的に管理するためのYAML形式のファイルです。国際化対応にも役立ちます。
    - `template_processor.py`: Jekyllテンプレートやその他のテキストテンプレートを処理し、動的なコンテンツを生成するための汎用的なユーティリティロジックを含みます。
    - `url_utils.py`: GitHub APIのエンドポイントURLの構築や、その他のURL関連の処理を行うユーティリティ関数を集めたファイルです。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールのプロジェクト概要取得機能を検証するための単体テストファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - `test_config.py`: 設定ファイル（`config.yml`など）の読み込みやパース処理に関するテストを行います。
    - `test_environment.py`: プログラムが実行される環境設定や依存関係の整合性を確認するためのテストです。
    - `test_integration.py`: プロジェクトの複数のコンポーネントが連携して正しく動作するかを確認する統合テストファイルです。
    - `test_markdown_generator.py`: `markdown_generator.py`が期待通りのMarkdownコンテンツを生成するかをテストします。
    - `test_project_overview_fetcher.py`: `project_overview_fetcher.py`の機能、特にリモートファイルからのプロジェクト概要抽出ロジックをテストします。
    - `test_repository_processor.py`: `repository_processor.py`がGitHub APIから取得したリポジトリデータを正しく処理・整形するかをテストします。

## 関数詳細説明
- **`generate_repo_list.py`**
    - `main()`: スクリプトの主要な実行エントリポイントです。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連の流れをオーケストレーションします。
        - 引数: なし (コマンドライン引数は `parse_arguments` で処理されます)
        - 戻り値: なし (主な副作用はMarkdownファイルの出力です)
    - `parse_arguments()`: コマンドラインから渡される引数 (`--username`, `--output`, `--limit` など) を解析し、プログラムが利用できる形式に変換します。
        - 引数: なし
        - 戻り値: `argparse.Namespace` オブジェクト (解析された引数とその値)
- **`config_manager.py`**
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイル (`config.yml` など) を読み込み、Pythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (str): 設定ファイルのパス
        - 戻り値: `dict`: 設定ファイルの内容
    - `load_secrets(secrets_path)`: 指定されたパスからTOML形式の秘密情報ファイル (`secrets.toml` など) を読み込み、GitHubトークンなどの機密情報を安全に提供します。
        - 引数: `secrets_path` (str): 秘密情報ファイルのパス
        - 戻り値: `dict`: 秘密情報の内容
- **`repository_processor.py`**
    - `fetch_repositories(username, token, limit=None)`: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。プライベートリポジトリやフォークの除外、取得数の制限が可能です。
        - 引数: `username` (str): GitHubユーザー名, `token` (str): GitHub認証トークン, `limit` (int, optional): 取得するリポジトリ数の上限 (デフォルト: `None`)
        - 戻り値: `list`: 取得したリポジトリ情報のリスト (それぞれが辞書形式)
    - `process_repository_data(repo_data, config, fetcher)`: GitHub APIから取得した単一の生リポジトリデータを受け取り、設定ファイルやプロジェクト概要フェッチャーを使って、Markdown生成に適した形に整形・加工します。
        - 引数: `repo_data` (dict): 単一リポジトリの生データ, `config` (dict): 全体設定, `fetcher` (ProjectOverviewFetcher): プロジェクト概要取得オブジェクト
        - 戻り値: `dict`: 処理済みのリポジトリ情報
- **`project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name, default_branch, config, github_token)`: 指定されたリポジトリのデフォルトブランチから、設定されたパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要テキストを非同期で取得します。
        - 引数: `repo_name` (str): リポジトリ名, `default_branch` (str): デフォルトブランチ名, `config` (dict): 設定情報, `github_token` (str): GitHub認証トークン
        - 戻り値: `str` または `None`: 抽出されたプロジェクト概要の3行説明、または取得できなかった場合は`None`
- **`markdown_generator.py`**
    - `generate_markdown(processed_repos, strings_data, seo_template, json_ld_template)`: 処理済みのリポジトリ情報リスト、表示文言、SEOテンプレート、JSON-LDテンプレートなどを用いて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
        - 引数: `processed_repos` (list): 処理済みのリポジトリ情報リスト, `strings_data` (dict): 表示文言, `seo_template` (dict): SEOテンプレート, `json_ld_template` (dict): JSON-LDテンプレート
        - 戻り値: `str`: 生成されたMarkdownコンテンツ
- **`badge_generator.py`**
    - `generate_badge_markdown(label, message, color)`: 指定されたラベル、メッセージ、色を使って、Shields.io形式のMarkdownバッジ文字列を生成します。
        - 引数: `label` (str): バッジの左側のテキスト, `message` (str): バッジの右側のテキスト, `color` (str): バッジの色
        - 戻り値: `str`: Markdown形式のバッジ文字列
- **`template_processor.py`**
    - `render_template(template_content, data)`: 指定されたテンプレートコンテンツと辞書形式のデータを用いて、テンプレートをレンダリング（データで穴埋め）します。Jinja2などのテンプレートエンジンを内部で使用している可能性があります。
        - 引数: `template_content` (str): テンプレート文字列, `data` (dict): テンプレートに埋め込むデータ
        - 戻り値: `str`: レンダリングされた文字列

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-30 07:05:57 JST
