Last updated: 2025-12-01

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEOに最適化されたMarkdown形式のページを生成します。
- これにより、リポジトリの検索エンジンでの発見性を高め、LLMからの参照性改善に貢献します。

## 技術スタック
- フロントエンド: Jekyll (生成されるMarkdownが出力されるGitHub Pagesのプラットフォーム)
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - `pytest`: Pythonコードのテストを実行するためのフレームワーク。
    - `ruff`: Pythonコードの静的解析と自動フォーマットを行うツール。
- テスト:
    - `pytest`: 単体テスト、結合テスト、機能テストなど、様々なレベルのテストを実行します。
- ビルドツール:
    - `Python`: 主要なスクリプト言語であり、リポジトリ情報の取得からMarkdown生成までの処理を実行します。
- 言語機能:
    - `Python`: プロジェクト全体で利用される主要なプログラミング言語です。
- 自動化・CI/CD:
    - `GitHub Pages`: 自動生成されたリポジトリ一覧や各リポジトリのページを公開するホスティングサービスです。
- 開発標準:
    - `ruff`: コードの品質を維持し、一貫性のあるコードスタイルを強制するためのリンターおよびフォーマッターです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: GitHub Pagesの静的サイトジェネレーターであるJekyllの設定ファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのアイコンとして使用される画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されたドキュメントやファイルを格納するためのディレクトリです。
- **`index.md`**: メインの出力ファイルであり、GitHubリポジトリ一覧がMarkdown形式で生成されます。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモを記録したMarkdownファイル群です。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの表示や動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリの依存関係を定義します。
- **`requirements.txt`**: 本番環境で必要となるPythonライブラリの依存関係を定義します。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: Pythonコードの静的解析ツール`ruff`の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの状態（アクティブ、アーカイブなど）に応じたバッジを生成するロジックが含まれます。
        - **`config.yml`**: プロジェクト固有の設定（例：プロジェクト概要取得機能のON/OFF、ターゲットファイルパスなど）を定義するYAMLファイルです。
        - **`config_manager.py`**: 設定ファイル（`config.yml`など）を読み込み、管理するためのロジックを提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインのスクリプトです。
        - **`json_ld_template.json`**: SEOのために構造化データ（JSON-LD形式）を生成する際のテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理するためのロジックが含まれます。
        - **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートをもとに、最終的なMarkdownコンテンツを生成するロジックが含まれます。
        - **`project_overview_fetcher.py`**: 各リポジトリから`project-overview.md`ファイルを読み込み、プロジェクト概要の3行説明を抽出するロジックが含まれます。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形・加工し、表示に適した形式に変換するロジックが含まれます。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリの統計情報（スター数、フォーク数など）を計算するためのロジックが含まれます。
        - **`strings.yml`**: 生成されるMarkdownページ内で使用される表示メッセージや固定文言を一元管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に、テンプレートファイルに変数を埋め込むなどの処理を行うロジックが含まれます。
        - **`url_utils.py`**: URLの構築や解析など、URLに関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストコードです。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストコードです。
    - **`test_environment.py`**: プロジェクトの実行環境に関するテストコードです。
    - **`test_integration.py`**: 複数のコンポーネントを結合した際の動作を検証する結合テストコードです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックに関するテストコードです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能に関するテストコードです。
    - **`test_repository_processor.py`**: リポジトリデータ処理ロジックに関するテストコードです。

## 関数詳細説明
このプロジェクトはPythonスクリプトとして動作し、主に以下の処理を担う関数群で構成されています。具体的な関数名が提示されていないため、主要な機能に対応する概念的な関数とその役割を説明します。

- **`main()` (generate_repo_list.py内)**:
    - **役割**: プロジェクトのエントリポイントであり、全体処理の流れを制御します。
    - **機能**: コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ情報取得、取得した情報の処理と整形、Markdownコンテンツの生成、そして最終的なファイルへの出力を行います。

- **`load_configuration(path)` (config_manager.py内)**:
    - **役割**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）を読み込みます。
    - **引数**: `path` (str): 設定ファイルのパス。
    - **戻り値**: `dict`: 読み込まれた設定情報。
    - **機能**: YAML形式の設定ファイルを解析し、Pythonの辞書形式で設定値を提供します。

- **`fetch_repositories_from_github(username, token)` (repository_processor.py内)**:
    - **役割**: GitHub APIを介して、指定されたユーザーのリポジトリ情報を取得します。
    - **引数**: `username` (str): GitHubユーザー名、`token` (str): GitHub APIアクセストークン。
    - **戻り値**: `list`: 取得したリポジトリデータのリスト。
    - **機能**: GitHub APIのエンドポイントにHTTPリクエストを送信し、リポジトリの詳細情報をJSON形式で受け取ります。

- **`process_repository_data(repo_data, config)` (repository_processor.py内)**:
    - **役割**: 個々のリポジトリデータを整形し、Markdown生成に適した形式に変換します。
    - **引数**: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ、`config` (dict): プロジェクトの設定。
    - **戻り値**: `dict`: 処理され、整形されたリポジトリ情報。
    - **機能**: リポジトリの基本情報（名前、説明、URL）、言語情報、統計情報などを抽出し、必要に応じて追加処理（例：プロジェクト概要の取得）を実行します。

- **`get_project_overview_description(repo_url, config)` (project_overview_fetcher.py内)**:
    - **役割**: 指定されたリポジトリの`generated-docs/project-overview.md`から3行のプロジェクト概要を抽出します。
    - **引数**: `repo_url` (str): リポジトリのURL、`config` (dict): プロジェクトの設定（ターゲットファイル名、セクションタイトルなど）。
    - **戻り値**: `str`: 抽出されたプロジェクト概要。
    - **機能**: GitHubのコンテンツAPIなどを利用して指定ファイルの内容を取得し、Markdownを解析して特定のセクションから説明文を抽出します。

- **`generate_markdown_content(processed_repo_list, seo_data, strings, templates)` (markdown_generator.py内)**:
    - **役割**: 処理済みのリポジトリ情報から、GitHub Pages用のMarkdownコンテンツを生成します。
    - **引数**: `processed_repo_list` (list): 処理済みのリポジトリ情報リスト、`seo_data` (dict): SEO関連データ、`strings` (dict): 表示文言、`templates` (dict): Markdownテンプレート。
    - **戻り値**: `str`: 生成されたMarkdownコンテンツ。
    - **機能**: テンプレートエンジンや文字列フォーマットを利用して、リポジトリ情報を組み込んだ最終的なMarkdownドキュメントを作成します。

- **`create_repository_badge(status)` (badge_generator.py内)**:
    - **役割**: リポジトリの状態（例：アーカイブ、フォーク）に応じた表示バッジの情報を生成します。
    - **引数**: `status` (str): リポジトリの状態を示す文字列。
    - **戻り値**: `str`: バッジのMarkdownまたはHTML形式。
    - **機能**: 指定されたステータスに基づいて、適切なバッジのマークアップを返します。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── load_configuration() (config_manager.py)
├── fetch_repositories_from_github() (repository_processor.py)
│   └── (GitHub APIへのHTTPリクエスト)
├── for each repository_data in fetched_repositories:
│   └── process_repository_data() (repository_processor.py)
│       ├── get_project_overview_description() (project_overview_fetcher.py)
│       │   └── (GitHubコンテンツAPIへのHTTPリクエスト)
│       ├── create_repository_badge() (badge_generator.py)
│       └── (統計計算、言語情報処理など)
└── generate_markdown_content() (markdown_generator.py)
    └── (テンプレート処理、文字列置換など)

---
Generated at: 2025-12-01 07:05:51 JST
