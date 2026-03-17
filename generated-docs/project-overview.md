Last updated: 2026-03-18

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEO課題を解決するため、リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyllベースのサイト向けに最適化されたMarkdownファイルを生成します。
- 各リポジトリの概要自動抽出、バッジ表示、分類機能により、情報の可視性とアクセシビリティを向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesで利用される静的サイトジェネレータ), Markdown (コンテンツ記述), HTML/CSS (Jekyllテンプレートによる描画)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: Python (メインの開発言語), Git (バージョン管理), Ruff (コードフォーマッター), Pytest (テストフレームワーク)
- テスト: Pytest (Pythonコードのユニットテストおよび結合テストに使用)
- ビルドツール: Pythonスクリプト (Markdownファイルの生成), Jekyll (GitHub Pagesによる最終的なサイトビルドは間接的に利用)
- 言語機能: Python (非同期処理、データ構造操作、ファイルI/Oなど一般的な言語機能を使用)
- 自動化・CI/CD: GitHub Actions (特定のCI/CDパイプラインは明示されていないが、`.github_automation`ディレクトリやREADMEの記述から自動化処理との関連が示唆される)
- 開発標準: Ruff (コードスタイルの一貫性を保つためのリンター/フォーマッター), requirements.txt/requirements-dev.txt (依存パッケージ管理)

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

*   **.editorconfig**: エディタの設定ファイル。インデントスタイルや文字コードなど、プロジェクト全体のコーディングスタイルを定義し、開発者間で一貫したコードを維持するために使用されます。
*   **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトを格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルのチェックに関連するスクリプトと設定を格納します。
        *   **README.md**: `check_large_files`機能に関する説明を提供します。
        *   **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        *   **scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
*   **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
*   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
*   **README.md**: プロジェクトの概要、セットアップ方法、使い方、機能などを説明するメインのドキュメントファイルです。
*   **_config.yml**: Jekyllのグローバル設定ファイルです。GitHub Pagesサイトのタイトル、テーマ、プラグインなどの設定を定義します。
*   **assets/**: サイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    *   **favicon-*.png**: サイトのファビコン（ウェブブラウザのタブなどに表示されるアイコン）画像ファイルです。
*   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
*   **generated-docs/**: 各リポジトリから自動生成されたドキュメントや概要ファイルが格納されることが想定されるディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
*   **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧のメインページとなるMarkdownファイルです。
*   **issue-notes/**: 開発中に発生した課題やメモを記録するためのディレクトリです。
    *   **22.md**: 特定の課題（Issue #22）に関するメモや詳細が記述されているMarkdownファイルです。
*   **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブマニフェストファイルです。ホームスクリーンアイコンや表示モードなどを定義します。
*   **pytest.ini**: Pytestのテスト設定ファイルです。テストの発見方法や実行オプションなどを定義します。
*   **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
*   **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
*   **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
*   **ruff.toml**: PythonのコードリンターおよびフォーマッターであるRuffの設定ファイルです。コーディングスタイルルールを定義します。
*   **src/**: ソースコードを格納するメインディレクトリです。
    *   **__init__.py**: Pythonパッケージの初期化ファイルです。
    *   **generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックが格納されているパッケージです。
        *   **__init__.py**: `generate_repo_list`パッケージの初期化ファイルです。
        *   **badge_generator.py**: GitHubリポジトリに表示するバッジ（例: 言語、ライセンスなど）を生成するロジックを扱います。
        *   **config.yml**: リポジトリ一覧生成システムの技術的な設定パラメータを定義するYAMLファイルです。
        *   **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        *   **date_formatter.py**: 日付や時刻のフォーマットを処理するためのユーティリティ関数を提供します。
        *   **generate_repo_list.py**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する全体のプロセスを制御します。
        *   **json_ld_template.json**: 構造化データ（JSON-LD）のテンプレートファイルです。SEOのためにリポジトリ情報を検索エンジンに理解させる目的で使用されます。
        *   **language_info.py**: リポジトリの使用言語情報を取得・解析し、表示形式に変換する機能を提供します。
        *   **markdown_generator.py**: 取得したリポジトリ情報に基づいて、最終的なMarkdownコンテンツを構築するロジックを実装します。
        *   **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出・取得する役割を担います。
        *   **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能を提供します。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形するためのロジックを実装します。
        *   **seo_template.yml**: サイトのSEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        *   **statistics_calculator.py**: リポジトリに関する各種統計情報（例: スター数、フォーク数など）を計算する機能を提供します。
        *   **strings.yml**: UIメッセージ、キャプション、説明文など、表示されるテキストコンテンツを一元的に管理するためのYAMLファイルです。
        *   **template_processor.py**: Markdown生成時に使用されるテンプレートの読み込みや変数置換などを処理するモジュールです。
        *   **url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
*   **test_project_overview.py**: `project_overview_fetcher.py`モジュールのテストスクリプトです。
*   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    *   **test_badge_generator_integration.py**: バッジ生成機能の結合テストです。
    *   **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    *   **test_config.py**: 設定ファイル（`config.yml`など）の読み込みと管理機能のテストです。
    *   **test_date_formatter.py**: 日付フォーマットユーティリティのテストです。
    *   **test_environment.py**: 開発・実行環境に関するテストです。
    *   **test_integration.py**: システム全体の主要な結合テストです。
    *   **test_markdown_generator.py**: Markdown生成機能のテストです。
    *   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    *   **test_readme_badge_extractor.py**: READMEからバッジを抽出する機能のテストです。
    *   **test_repository_processor.py**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
※提供された情報には具体的な関数シグネチャが含まれていないため、ファイル名とプロジェクトの機能から主要な関数とその役割、想定される引数・戻り値を記述します。

*   **src/generate_repo_list/generate_repo_list.py**
    *   `main()`
        *   **役割**: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の全体フローを制御します。
        *   **引数**: なし (内部で`argparse`を使用し、コマンドライン引数を解析)。
        *   **戻り値**: なし。
    *   `generate_repo_list(username: str, output_file: str, limit: Optional[int] = None)`
        *   **役割**: 指定されたGitHubユーザーのリポジトリ情報を取得し、処理してMarkdown形式で指定ファイルに出力します。
        *   **引数**:
            *   `username` (str): GitHubのユーザー名。
            *   `output_file` (str): 生成されたMarkdownコンテンツを出力するファイル名。
            *   `limit` (Optional[int]): 処理するリポジトリ数の上限（デバッグ用）。
        *   **戻り値**: なし。

*   **src/generate_repo_list/project_overview_fetcher.py**
    *   `fetch_project_overview(repo_full_name: str, config: dict, github_token: str)`
        *   **役割**: 指定されたリポジトリ (`owner/repo_name`) から、設定ファイルで指定されたパスとセクションタイトルに基づいてプロジェクト概要（3行説明）を非同期で取得します。GitHub APIを介してファイル内容をフェッチし、解析します。
        *   **引数**:
            *   `repo_full_name` (str): リポジトリのフルネーム (例: "cat2151/my-repo")。
            *   `config` (dict): `config.yml`から読み込まれた設定辞書。プロジェクト概要取得に関する設定を含みます。
            *   `github_token` (str): GitHub API認証用のトークン。
        *   **戻り値**: `str` (抽出されたプロジェクト概要テキスト) または `None` (取得または解析に失敗した場合)。

*   **src/generate_repo_list/markdown_generator.py**
    *   `generate_markdown(repo_data_list: List[dict], config: dict, strings: dict) -> str`
        *   **役割**: 処理済みのリポジトリデータリスト、設定、および表示文字列を使用して、Jekyll形式に準拠した最終的なMarkdownコンテンツを生成します。テンプレートエンジンや文字列置換を活用します。
        *   **引数**:
            *   `repo_data_list` (List[dict]): 処理され、表示準備が整ったリポジトリ情報のリスト。
            *   `config` (dict): グローバル設定。
            *   `strings` (dict): `strings.yml`から読み込まれた表示文字列辞書。
        *   **戻り値**: `str` (生成されたMarkdownコンテンツ)。

*   **src/generate_repo_list/repository_processor.py**
    *   `process_repository_data(repo_raw_data: dict, config: dict, overview_fetcher: ProjectOverviewFetcher) -> dict`
        *   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、整形、計算し、さらにプロジェクト概要などの追加情報を取得して結合します。
        *   **引数**:
            *   `repo_raw_data` (dict): GitHub APIから直接取得したリポジトリの生データ。
            *   `config` (dict): グローバル設定。
            *   `overview_fetcher` (ProjectOverviewFetcher): プロジェクト概要を取得するためのインスタンス。
        *   **戻り値**: `dict` (整形され、追加情報が付与されたリポジトリデータ)。

*   **src/generate_repo_list/config_manager.py**
    *   `load_config(config_path: str) -> dict`
        *   **役割**: 指定されたパスからYAML形式の設定ファイルを読み込み、Python辞書として返します。
        *   **引数**: `config_path` (str): 設定ファイルのパス。
        *   **戻り値**: `dict` (読み込まれた設定データ)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-18 07:13:09 JST
