Last updated: 2025-11-12

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、GitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンやLLMからの参照性を高め、プロジェクトの可視性と開発効率向上に貢献します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (Markdownからのサイト生成), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: N/A
- 開発ツール: Python (主要開発言語), GitHub API (リポジトリ情報取得), Ruff (コードリンター/フォーマッター), pytest (テストフレームワーク), .editorconfig (コードスタイル定義)
- テスト: pytest (Pythonコードの単体・統合テスト実行)
- ビルドツール: Pythonスクリプト (Markdownコンテンツ生成), Jekyll (GitHub Pagesによるサイトビルド)
- 言語機能: Python 3.x (オブジェクト指向プログラミング、ファイルI/O、ネットワーク通信、文字列操作など)
- 自動化・CI/CD: GitHub Actions (README内でCI/CD不要と記載されているものの、GitHub API利用自体は自動化フローの一部)
- 開発標準: Ruff (Pythonコードの品質と一貫性を自動チェック・修正), .editorconfig (エディタ間でのコーディングスタイル統一)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイル。生成物、一時ファイル、個人設定などが含まれます。
- **LICENSE**: 本プロジェクトのソフトウェアライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの概要、目的、機能、セットアップ方法、使い方などが記述された主要な説明文書。
- **_config.yml**: GitHub Pages（Jekyll）サイト全体のビルド設定やメタデータを定義するファイル。
- **assets/**: Webサイトで使用する画像、アイコン（ファビコンなど）、スタイルシートなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: 各種デバイス向けに最適化されたファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールの動作をデバッグするための補助スクリプト。
- **generated-docs/**: 各リポジトリから取得した概要や、生成されたドキュメントを一時的に格納する、あるいはキャッシュするためのディレクトリ。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイル。GitHub Pagesのトップページとして表示されます。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを個別のMarkdownファイルとして記録しておくディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名称、アイコン、表示モードなど）を定義するファイル。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定（テスト対象パス、オプションなど）を定義するファイル。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: 本番環境でプロジェクトを動作させるために必要なPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか、どのページを避けるかなどを指示するファイル。
- **ruff.toml**: Pythonの高速リンター/フォーマッターであるRuffの設定ファイル。コードスタイルのルールやチェック項目を定義します。
- **src/**: 本プロジェクトの主要なPythonソースコードを格納するディレクトリ。
    - **src/__init__.py**: Pythonパッケージであることを示すファイル。
    - **src/generate_repo_list/**: リポジトリ一覧生成に関する主要なロジックがモジュールとして格納されているパッケージ。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list` パッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの言語やステータスを示すバッジ（Shields.ioなど）のMarkdownを生成する機能を提供します。
        - **config.yml**: プロジェクト概要取得機能など、本システム固有の技術的パラメータを設定するためのYAMLファイル。
        - **config_manager.py**: `config.yml` や `secrets.toml` などの設定ファイルを読み込み、管理するためのモジュール。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する本プロジェクトのメインスクリプト。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を生成する際のテンプレート。
        - **language_info.py**: GitHubリポジトリの主要言語情報などを処理・整形するロジックを提供します。
        - **markdown_generator.py**: 取得・処理されたリポジトリ情報をもとに、GitHub Pages用のMarkdownコンテンツを生成するモジュール。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータをフィルタリング、整形、追加情報付与などを行うモジュール。
        - **seo_template.yml**: Webサイトの検索エンジン最適化（SEO）関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリ数、言語分布などの統計情報を計算する機能を提供します。
        - **strings.yml**: 生成されるMarkdownやログメッセージなどで使用される固定文字列や表示文言を一元管理するためのYAMLファイル。
        - **template_processor.py**: Markdown生成時に、Jinja2などのテンプレートエンジンを用いて動的にコンテンツをレンダリングする機能を提供します。
        - **url_utils.py**: URLの構築、解析、検証など、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得と解析）を検証するためのテストスクリプト。
- **tests/**: 本プロジェクトの様々なモジュールや機能に対するテストスクリプトを格納するディレクトリ。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを行うスクリプト。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを行うスクリプト。
    - **test_integration.py**: 複数のモジュールが連携して動作する際の統合的なテストを行うスクリプト。
    - **test_markdown_generator.py**: `markdown_generator.py` が正しくMarkdownを生成するかを検証するテストスクリプト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py` の詳細な単体テストを行うスクリプト。
    - **test_repository_processor.py**: `repository_processor.py` がリポジトリデータを正しく処理・整形するかを検証するテストスクリプト。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main()`:
        - **役割**: プログラムのエントリポイント。コマンドライン引数を解析し、設定を読み込み、リポジトリ情報の取得、処理、Markdown生成という一連のフローをオーケストレートします。
        - **引数**: なし（コマンドライン引数として `--username`, `--output`, `--limit` を受け付けます）。
        - **戻り値**: なし（ファイル出力を行います）。
- **repository_processor.py**:
    - `fetch_repositories(username, github_token)`:
        - **役割**: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub API経由で取得します。
        - **引数**: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIへの認証トークン。
        - **戻り値**: リポジトリ情報のリスト (list of dict)。
    - `process_repository_data(repo_data)`:
        - **役割**: 取得した生のリポジトリデータから必要な情報を抽出し、整形、フィルタリングを行います。
        - **引数**: `repo_data` (dict): 単一のリポジトリの生データ。
        - **戻り値**: 処理済みのリポジトリ情報 (dict)。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_name, owner, config)`:
        - **役割**: 特定のリポジトリ（`repo_name`, `owner`）から設定ファイル (`config`) に指定されたパスのMarkdownファイルを取得し、そこから「プロジェクト概要」セクションの3行説明を抽出します。
        - **引数**: `repo_name` (str): リポジトリ名, `owner` (str): リポジトリ所有者のユーザー名, `config` (dict): プロジェクト概要取得に関する設定。
        - **戻り値**: 抽出されたプロジェクト概要の3行説明 (list of str)、または空リスト。
- **markdown_generator.py**:
    - `generate_repo_list_markdown(repositories_info, config)`:
        - **役割**: 処理済みの全リポジトリ情報 (`repositories_info`) を基に、GitHub Pagesに表示するリポジトリ一覧のMarkdown文字列を生成します。
        - **引数**: `repositories_info` (list of dict): 各リポジトリの処理済み情報リスト, `config` (dict): Markdown生成に関する設定。
        - **戻り値**: 生成されたMarkdown文字列 (str)。
- **config_manager.py**:
    - `load_config(config_path)`:
        - **役割**: 指定されたパスのYAML設定ファイル (`config.yml`) を読み込み、Python辞書として返します。
        - **引数**: `config_path` (str): 設定ファイルのパス。
        - **戻り値**: 設定内容を表す辞書 (dict)。
    - `load_secrets(secrets_path)`:
        - **役割**: 指定されたパスの秘密情報ファイル（例: `secrets.toml`）を読み込み、GitHubトークンなどの機密情報を取得します。
        - **引数**: `secrets_path` (str): 秘密情報ファイルのパス。
        - **戻り値**: 秘密情報を含む辞書 (dict)。
- **badge_generator.py**:
    - `generate_badge(label, message, color)`:
        - **役割**: 指定されたラベル、メッセージ、色でMarkdown形式のバッジ（例: Shields.io形式）を生成します。
        - **引数**: `label` (str): バッジの左側のテキスト, `message` (str): バッジの右側のテキスト, `color` (str): バッジの色。
        - **戻り値**: バッジのMarkdown文字列 (str)。
- **statistics_calculator.py**:
    - `calculate_language_stats(repo_data_list)`:
        - **役割**: 複数のリポジトリデータから、使用されているプログラミング言語の統計情報（例: 使用率）を計算します。
        - **引数**: `repo_data_list` (list of dict): 処理済みリポジトリ情報のリスト。
        - **戻り値**: 言語統計情報 (dict)。
- **template_processor.py**:
    - `render_template(template_string, context)`:
        - **役割**: 指定されたテンプレート文字列とコンテキストデータを使用して、最終的なコンテンツをレンダリングします。
        - **引数**: `template_string` (str): テンプレートの内容, `context` (dict): テンプレートに渡すデータ。
        - **戻り値**: レンダリングされた文字列 (str)。
- **url_utils.py**:
    - `build_github_api_url(endpoint, username)`:
        - **役割**: GitHub APIのベースURLと指定されたエンドポイント、ユーザー名から完全なAPI URLを構築します。
        - **引数**: `endpoint` (str): APIのエンドポイント（例: `users/{username}/repos`）, `username` (str): GitHubユーザー名。
        - **戻り値**: 構築されたAPI URL (str)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-12 07:06:32 JST
