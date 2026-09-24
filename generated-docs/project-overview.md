Last updated: 2026-09-25

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のリポジトリ情報を自動取得します。
- GitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- これにより、リポジトリが検索エンジンにインデックスされやすくなり、情報の可視性を高めます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本システムで生成されたMarkdownファイルを読み込み、Webサイトとして公開するために使用されます。
    - **Markdown**: リポジトリ一覧ページを記述するための軽量マークアップ言語。システムはこの形式でコンテンツを生成します。
    - **HTML/CSS**: Jekyllによって最終的に生成されるウェブページの構造とスタイルを定義します。
- 音楽・オーディオ: 該当なし。
- 開発ツール:
    - **Python**: プロジェクトの主要なプログラミング言語。リポジトリ情報の取得、処理、Markdown生成のコアロジックを実装しています。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラムから取得するために使用されます。
    - **pytest**: Pythonコードのテストを記述・実行するためのフレームワーク。
    - **ruff**: Pythonコードの高速なリンター兼フォーマッター。コード品質とスタイルの一貫性を保ちます。
    - **Git**: プロジェクトのバージョン管理システム。
- テスト:
    - **pytest**: Pythonアプリケーションの単体テスト、結合テスト、機能テストを実行するためのフレームワーク。
- ビルドツール:
    - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py` がGitHub APIから情報を取得し、Markdownファイルを生成する実質的なビルドプロセスを担います。
    - **Jekyll**: (間接的に) 生成されたMarkdownを静的サイトに変換するビルドツール。
- 言語機能:
    - **Python標準ライブラリ**: ファイルI/O、文字列処理、HTTPリクエストなど、基本的なプログラミングタスクに利用されます。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリ内のスクリプトや、プロジェクト概要での言及から、自動化されたワークフローや継続的インテグレーション/デリバリーに利用される可能性があります。
- 開発標準:
    - **ruff**: コードのスタイルガイドラインを強制し、潜在的なエラーを検出するためのリンター/フォーマッター。
    - **.editorconfig**: 異なるエディタやIDE間でコードの整形ルール（インデントスタイル、文字コードなど）を統一するための設定ファイル。

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
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
googled947dc864c270e07.html
index.md
issue-notes/
  22.md
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
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: コードエディタ全体で一貫したコーディングスタイル（インデントサイズ、改行コードなど）を定義する設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化されたタスクやスクリプトを格納するためのディレクトリです。
    - **`check_large_files/`**: プロジェクト内の大容量ファイルをチェックし、管理するためのツールです。
        - **`README.md`**: `check_large_files`ツールの使用方法や目的を説明するドキュメントです。
        - **`check-large-files.toml`**: `check_large_files`ツールの設定パラメータ（例: サイズ上限、無視するファイル）を定義するファイルです。
        - **`scripts/`**: `check_large_files`ツールに関連する実行可能なスクリプトを格納します。
            - **`check_large_files.py`**: プロジェクト内のファイルサイズを検査し、設定された基準を超えるファイルを報告するPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。著作権、利用条件、免責事項などが含まれます。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、目的、開発者向け情報などを説明する、リポジトリの主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などの設定を定義します。
- **`assets/`**: ウェブサイトで使用されるファビコン、画像、CSS、JavaScriptなどの静的リソースを格納するディレクトリです。
    - **`favicon-16x16.png`**: 16x16ピクセルのファビコン画像ファイルです。
    - **`favicon-192x192.png`**: 192x192ピクセルのファビコン（またはPWAアイコン）画像ファイルです。
    - **`favicon-32x32.png`**: 32x32ピクセルのファビコン画像ファイルです。
    - **`favicon-512x512.png`**: 512x512ピクセルのファビコン（またはPWAアイコン）画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや個別テストのために使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや、他のリポジトリから取得された概要ファイルなどを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するためにGoogleが要求する特定のHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このファイルにリポジトリ一覧が自動生成されます。
- **`issue-notes/`**: 開発中の課題、検討事項、または一時的なメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルです。ウェブアプリの表示方法、アイコン、テーマカラーなどを定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルです。テストの実行オプション、検出パターンなどを指定します。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、または除外するかを指示するファイルです。
- **`ruff.toml`**: `ruff`リンター/フォーマッターの設定ファイルです。コードの整形ルール、警告レベル、無視するファイルなどを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるルートディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すための空ファイル、またはパッケージ初期化コードを含みます。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するロジックをカプセル化したPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`サブパッケージを示すためのファイルです。
        - **`badge_generator.py`**: リポジトリの技術スタック、ライセンスなどの情報を視覚的なバッジとして生成するロジックを含みます。
        - **`config.yml`**: プロジェクトの動作に関する技術的な設定パラメータ（例: プロジェクト概要取得の有効/無効、タイムアウト）を定義するYAMLファイルです。
        - **`config_manager.py`**: YAML形式の設定ファイル (`config.yml`, `strings.yml` など) を読み込み、管理するためのユーティリティスクリプトです。
        - **`date_formatter.py`**: 日付や時刻の文字列を特定のフォーマットに整形するための関数を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIを呼び出し、リポジトリ情報を取得し、Markdownファイルを生成する処理をオーケストレートします。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、整形するための関数を提供します。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートを基に、最終的なMarkdownコンテンツを生成するロジックを含みます。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要を抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整形する主要な処理ロジックを含みます。
        - **`seo_template.yml`**: SEO関連のメタデータや構造化データに関する追加設定やテンプレートを定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するための関数を提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレートを読み込み、変数置換などを行う汎用的な処理を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能のテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのフィクスチャやテストのヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストを行うファイルです。
    - **`test_check_large_files.py`**: 大容量ファイルチェックツールのテストを行うファイルです。
    - **`test_config.py`**: 設定ファイル読み込み・管理機能のテストを行うファイルです。
    - **`test_date_formatter.py`**: 日付整形機能のテストを行うファイルです。
    - **`test_environment.py`**: 実行環境に関するテスト（依存関係、パスなど）を行うファイルです。
    - **`test_integration.py`**: 主要なコンポーネント間の連携を検証する結合テストを行うファイルです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを行うファイルです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うファイルです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを行うファイルです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うファイルです。

## 関数詳細説明
与えられた情報からは具体的な関数シグネチャを特定できませんが、ファイル名から推測される主要な関数の役割は以下の通りです。

- **`generate_repo_list.py`**:
    - `main()`: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力という一連の流れを制御します。
        - *役割*: プログラム全体の実行フローを管理。
        - *引数*: なし（コマンドライン引数を内部で解析）。
        - *戻り値*: なし。
    - `generate_list(username: str, output_file: str, limit: Optional[int] = None)`: 指定されたGitHubユーザーのリポジトリ情報を取得し、整形して指定された出力ファイルにMarkdown形式で書き出します。
        - *役割*: リポジトリ一覧生成の主要なロジックを実行。
        - *引数*: `username` (GitHubユーザー名), `output_file` (出力ファイル名), `limit` (処理するリポジトリ数の上限、オプション)。
        - *戻り値*: なし。

- **`repository_processor.py`**:
    - `fetch_repositories(username: str, token: str) -> List[Dict]`: GitHub APIを通じて、指定されたユーザー名の全公開リポジトリを取得します。
        - *役割*: GitHub APIとの通信を担当し、生のリポジトリデータを取得。
        - *引数*: `username` (GitHubユーザー名), `token` (GitHub個人アクセストークン)。
        - *戻り値*: リポジトリ情報の辞書リスト。
    - `process_repository_data(repo_data: Dict, config: Dict, strings: Dict) -> Dict`: 取得した生のリポジトリデータから必要な情報を抽出し、整形し、Markdown生成に適した形式に変換します。この中で、概要の取得やバッジの生成なども呼び出します。
        - *役割*: 取得データの解析と整形。
        - *引数*: `repo_data` (個々のリポジトリの生データ), `config` (設定辞書), `strings` (文言辞書)。
        - *戻り値*: 整形されたリポジトリ情報辞書。

- **`project_overview_fetcher.py`**:
    - `get_project_overview(repo_url: str, config: Dict) -> Optional[str]`: 指定されたリポジトリの`generated-docs/project-overview.md`ファイルから、定義されたセクションの3行概要をフェッチして返します。
        - *役割*: 各リポジトリの概要ファイルを読み込み、指定部分を抽出。
        - *引数*: `repo_url` (リポジトリのURL), `config` (プロジェクト概要機能の設定)。
        - *戻り値*: 抽出された概要文字列、またはNone。

- **`markdown_generator.py`**:
    - `generate_markdown(processed_repos: List[Dict], strings: Dict) -> str`: 処理済みのリポジトリデータと文言データを使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
        - *役割*: 整形されたデータからMarkdownテキストを構築。
        - *引数*: `processed_repos` (整形済みリポジトリ情報のリスト), `strings` (文言辞書)。
        - *戻り値*: 生成されたMarkdown文字列。

- **`config_manager.py`**:
    - `load_config(config_path: str) -> Dict`: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
        - *役割*: 設定ファイルの読み込み。
        *引数*: `config_path` (設定ファイルへのパス)。
        *戻り値*: 設定内容の辞書。
    - `load_strings(strings_path: str) -> Dict`: 指定されたパスからYAML形式の文言ファイルを読み込み、辞書として返します。
        - *役割*: 文言定義ファイルの読み込み。
        *引数*: `strings_path` (文言ファイルへのパス)。
        *戻り値*: 文言内容の辞書。

- **`date_formatter.py`**:
    - `format_date(iso_date_string: str) -> str`: ISO 8601形式の日付文字列を、人間が読みやすい形式に整形します。
        - *役割*: 日付の表示形式を調整。
        *引数*: `iso_date_string` (ISO 8601形式の日付文字列)。
        *戻り値*: 整形された日付文字列。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── load_config() (config_manager.py)
├── load_strings() (config_manager.py)
└── generate_list(username, output_file, limit)
    ├── fetch_repositories(username, token) (repository_processor.py)
    ├── process_repository_data(repo_data, config, strings) (repository_processor.py)
    │   ├── get_project_overview(repo_url, config) (project_overview_fetcher.py)
    │   ├── generate_badges(repo_info) (badge_generator.py)
    │   ├── format_date(iso_date_string) (date_formatter.py)
    │   ├── (readme_badge_extractor.py 内の関数)
    │   ├── (language_info.py 内の関数)
    │   └── (statistics_calculator.py 内の関数)
    └── generate_markdown(processed_repos, strings) (markdown_generator.py)
        ├── (template_processor.py 内の関数)
        └── (url_utils.py 内の関数)

---
Generated at: 2026-09-25 07:12:32 JST
