Last updated: 2025-11-11

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成し、検索エンジン最適化(SEO)を促進します。
- GitHub APIからリポジトリ情報を取得し、Markdown形式で整形されたリストを出力します。
- 各リポジトリの概要を自動取得・表示することで、可視性と検索性を高めることを目的とします。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレーターとして利用され、生成されるMarkdownがJekyllによってHTMLに変換されます), Markdown (最終的な出力形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), ruff (コードスタイルリンター、フォーマッター), pytest (テストフレームワーク)
- テスト: pytest (Pythonコードの単体・結合テストを実行するためのフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得・加工、Markdown生成を行う実質的なビルドプロセス), Jekyll (GitHub Pagesによるデプロイ時に静的サイトを構築)
- 言語機能: Python (バージョン3.8以降を想定、コマンドライン引数処理、API通信、ファイル操作など)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得), Pythonスクリプト (リポジトリ一覧生成プロセスの自動化)
- 開発標準: ruff (Pythonコードの品質と一貫性を保つためのリンティングおよびフォーマットツール)

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
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、ライセンスなど、プロジェクトに関する包括的な情報が記述されています。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバル設定を定義するファイルです。
- **`assets/`**: ウェブサイトで利用される静的アセット（例: ファビコン画像）が格納されるディレクトリです。
    - **`favicon-*.png`**: 各種サイズのファビコン画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得された `project-overview.md` ファイルが一時的に配置される、または参照されるディレクトリです。
- **`index.md`**: 生成されたリポジトリ一覧が最終的に書き込まれる主要なMarkdownファイルで、GitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: プロジェクト開発中の課題や検討事項、メモなどが個別のMarkdownファイルとして整理されています。
    - **`*.md`**: 個別の課題やメモの内容が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてGitHub Pagesサイトを設定するためのWeb App Manifestファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの検出方法や実行オプションなどを定義します。
- **`requirements-dev.txt`**: プロジェクトの開発・テスト時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンター/フォーマッターである `ruff` の設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成ロジックが実装されているPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list` ディレクトリをPythonサブパッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや属性（例: アクティブ、アーカイブ）を示すバッジのMarkdownを生成するロジックを扱います。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの実行時パラメータや挙動を制御する設定ファイルです（例: プロジェクト概要取得機能のON/OFF、タイムアウト設定）。
        - **`config_manager.py`**: 設定ファイル (`config.yml` や `secrets.toml` など) の読み込み、解析、管理を行うモジュールです。
        - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプトです。GitHub APIからリポジトリ情報を取得し、加工してMarkdownファイルを生成する一連の処理を統括します。
        - **`json_ld_template.json`**: 検索エンジン最適化のために、Webページに構造化データを埋め込むためのJSON-LD形式のテンプレートファイルです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、表示可能な形式に変換するロジックを実装しています。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報やプロジェクト概要情報に基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクト概要の3行説明を抽出するロジックを扱います。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に加工するモジュールです。
        - **`seo_template.yml`**: サイト全体のSEO設定やメタデータに関するテンプレートを定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計するロジックを扱います。
        - **`strings.yml`**: スクリプトが出力するメッセージや表示される文言、翻訳テキストなどを一元的に管理するファイルです。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（例: Jinja2テンプレート）のレンダリングを処理するモジュールです。
        - **`url_utils.py`**: URLの構築、解析、検証など、URLに関連するユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能に関するテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストコードです。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストコードです。
    - **`test_integration.py`**: 複数のモジュールが連携して動作する際の結合テストコードです。
    - **`test_markdown_generator.py`**: `markdown_generator.py` モジュールの機能に関するテストコードです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールが正しく動作するかを検証するテストコードです。
    - **`test_repository_processor.py`**: `repository_processor.py` モジュールがリポジトリデータを正しく処理するかを検証するテストコードです。

## 関数詳細説明
プロジェクト情報からは具体的な関数シグネチャが提供されていないため、ファイル名と役割から主要な関数とその機能を推測して説明します。

-   **`generate_repo_list.py` 内の関数:**
    -   **`main()`**:
        -   **役割**: コマンドライン引数を解析し、リポジトリ一覧生成の全体フローをオーケストレートします。
        -   **引数**: コマンドラインからの引数（`--username`, `--output`, `--limit`など）。
        -   **戻り値**: なし（直接ファイルを生成します）。
        -   **機能**: `config_manager`から設定を読み込み、`repository_processor`を呼び出してリポジトリ情報を取得・処理し、`project_overview_fetcher`で各リポジトリの概要を取得後、`markdown_generator`で最終的なMarkdownを生成し、指定されたファイルに出力します。

-   **`config_manager.py` 内の関数:**
    -   **`load_config(config_path: str) -> dict`**:
        -   **役割**: 指定されたパスから設定ファイルを読み込み、辞書形式で返します。
        -   **引数**: `config_path` (str): 設定ファイルのパス。
        -   **戻り値**: `dict`: 読み込まれた設定内容。
        -   **機能**: YAML形式やTOML形式の設定ファイルを解析し、スクリプトが使用する設定パラメータを提供します。

-   **`repository_processor.py` 内の関数:**
    -   **`fetch_and_process_repositories(username: str, github_token: str, limit: int = None) -> list[dict]`**:
        -   **役割**: GitHub APIを介して指定されたユーザーのリポジトリ情報を取得し、整形して返します。
        -   **引数**: `username` (str): GitHubユーザー名, `github_token` (str): GitHub認証トークン, `limit` (int, optional): 取得するリポジトリ数の上限。
        -   **戻り値**: `list[dict]`: 処理されたリポジトリ情報のリスト。
        -   **機能**: GitHub APIへのリクエストを構築し、リポジトリデータを取得後、必要な情報（名前、説明、URL、スター数、言語など）を抽出し、フィルタリングやソートを行います。

-   **`project_overview_fetcher.py` 内の関数:**
    -   **`fetch_project_overview(repo_full_name: str, config: dict) -> str`**:
        -   **役割**: 特定のリポジトリから、設定ファイルで指定されたパスのMarkdownファイルを読み込み、プロジェクト概要の3行説明を抽出します。
        -   **引数**: `repo_full_name` (str): リポジトリのフルネーム（例: `cat2151/my-repo`), `config` (dict): プロジェクト概要取得に関する設定（ファイルパス、セクションタイトルなど）。
        -   **戻り値**: `str`: 抽出された3行のプロジェクト概要、または空文字列。
        -   **機能**: GitHub APIを通じてリポジトリ内のファイルコンテンツを取得し、特定のセクション (`## プロジェクト概要`) から箇条書きの最初の3行をパースして抽出します。

-   **`markdown_generator.py` 内の関数:**
    -   **`generate_markdown(repositories: list[dict], project_overview_map: dict, config: dict, strings: dict) -> str`**:
        -   **役割**: 処理されたリポジトリ情報と取得されたプロジェクト概要をもとに、Jekyll互換のMarkdownコンテンツを生成します。
        -   **引数**: `repositories` (list[dict]): 処理済みのリポジトリ情報リスト, `project_overview_map` (dict): リポジトリごとのプロジェクト概要マップ, `config` (dict): 全体設定, `strings` (dict): 表示文言。
        -   **戻り値**: `str`: 生成されたMarkdown文字列。
        -   **機能**: JekyllのFront Matterや、各リポジトリのタイトル、説明、バッジ、リンクなどを整形して、最終的なMarkdownファイルの内容を組み立てます。

-   **`badge_generator.py` 内の関数:**
    -   **`generate_badge_markdown(repo_status: str) -> str`**:
        -   **役割**: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）に応じたMarkdown形式のバッジを生成します。
        -   **引数**: `repo_status` (str): リポジトリの現在のステータス。
        -   **戻り値**: `str`: バッジのMarkdown文字列。
        -   **機能**: 指定されたステータスに基づき、対応するSVGバッジのMarkdownまたはテキストを返します。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── load_config() (src/generate_repo_list/config_manager.py)
├── fetch_and_process_repositories() (src/generate_repo_list/repository_processor.py)
│   ├── (GitHub API呼び出し)
│   └── (リポジトリデータのフィルタリング・整形)
├── for each repository:
│   └── fetch_project_overview() (src/generate_repo_list/project_overview_fetcher.py)
│       └── (GitHub APIによるファイルコンテンツ取得)
│       └── (Markdownパースによる概要抽出)
├── generate_markdown() (src/generate_repo_list/markdown_generator.py)
│   ├── (Jekyll Front Matterの生成)
│   ├── for each repository:
│   │   ├── generate_badge_markdown() (src/generate_repo_list/badge_generator.py)
│   │   ├── (リポジトリ情報の整形)
│   │   └── (プロジェクト概要の埋め込み)
│   └── (テンプレート処理による最終Markdownの組み立て)
└── (Markdownコンテンツのファイル出力)

---
Generated at: 2025-11-11 07:06:49 JST
