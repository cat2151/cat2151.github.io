Last updated: 2026-10-26

# Project Overview

## プロジェクト概要
- このプロジェクトは、GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのGitHub Pagesサイト用にMarkdownファイルを自動生成するシステムです。
- GitHubユーザーページのリポジトリ一覧が検索エンジンにクロールされにくい課題に対し、GitHub Pages側でSEO最適化されたリポジトリ一覧を生成することで解決を試みます。
- これにより、リポジトリが検索結果に表示されやすくなり、ClaudeなどのLLMがリポジトリ情報を参照しやすくなる効果が期待されます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤として使用され、Markdownファイルから静的なWebサイトを生成します。
    - **Markdown**: リポジトリ一覧や個別のリポジトリ概要ページとして自動生成されるファイル形式です。
    - **GitHub Pages**: プロジェクトの成果物（生成されたリポジトリ一覧サイト）を公開するホスティングサービスです。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからのデータ取得、Markdown生成、ファイル操作などに使用されます。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために利用されます。
    - **YAML**: プロジェクトの設定ファイル（`config.yml`、`strings.yml`、`seo_template.yml`）や、プロジェクト概要機能の設定に使用されます。
    - **TOML**: 設定ファイル（`ruff.toml`、`check-large-files.toml`、`secrets.toml`）の記述に利用されます。
- テスト:
    - **pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py` を中心としたPythonスクリプト群が、GitHub APIからのデータ取得とMarkdownファイルの生成（事実上のビルドプロセス）を担います。
- 言語機能:
    - **Python**: 最新の言語機能を利用し、データ処理やファイル操作を効率的に行っています。
- 自動化・CI/CD:
    - **GitHub Pages**: GitHubリポジトリへのプッシュをトリガーにサイトを自動デプロイする機能が利用されます。
    - **GitHub Actions**: （`.github_automation`ディレクトリの存在から推測されるが、明示的なCI/CD設定は示されていない）将来的な自動化や継続的インテグレーション・デリバリーの基盤となり得ます。
- 開発標準:
    - **ruff**: Pythonコードの高速なリンター兼フォーマッターであり、コード品質の維持とスタイルの一貫性を保つために使用されます。
    - **.editorconfig**: 異なるエディタやIDEを使用する開発者間でのコードスタイルの一貫性を保証するための設定ファイルです。

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
- **.editorconfig**: さまざまなエディタ間でのコードスタイルの一貫性を保つための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリです。
    - **.github_automation/check_large_files/**: リポジトリ内の大容量ファイルをチェックするための自動化スクリプト群です。
        - **README.md**: `check_large_files` スクリプトの目的、使い方、設定方法などを説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェック機能の具体的な設定（閾値、対象ファイルなど）を定義するTOML形式のファイルです。
        - **scripts/check_large_files.py**: 実際にリポジトリ内のファイルを走査し、設定された基準を超過する大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイルです。
- **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すファイルです。
- **README.md**: プロジェクト全体の概要、セットアップ方法、主な機能、使用方法などを記述した、プロジェクトの玄関口となるドキュメントです。
- **_config.yml**: Jekyllサイト全体の共通設定（サイト名、テーマ、プラグインなど）を定義するファイルです。
- **assets/**: Webサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（ブラウザのタブなどに表示されるアイコン）のさまざまなサイズバージョンです。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグや単体テストを行うためのスクリプトです。
- **generated-docs/**: 通常、自動生成されたドキュメントや一時ファイルを格納するディレクトリですが、このプロジェクトではリモートリポジトリからの概要を読み取る際のパスとしても指定されています。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成され、GitHub Pagesサイトのトップページ（リポジトリ一覧）となるMarkdownファイルです。
- **issue-notes/**: 開発中の課題や調査結果、一時的なメモなどを格納するディレクトリです。
    - **22.md**: 特定の課題（ID 22）に関する詳細なメモや解決策が記述されたファイルです。
- **manifest.json**: Progressive Web App (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの機能を提供します。
- **pytest.ini**: pytestフレームワークの実行に関する設定（テストの検出パス、プラグインなど）を定義するファイルです。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトが本番環境で実行される際に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか、しないかを指示するためのファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。コードスタイルのルールや自動修正に関する設定を定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを構成するモジュール群です。
        - **__init__.py**: `generate_repo_list` がPythonサブパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（例: `GitHub Actions`、`Python` など）のMarkdownを生成するロジックを扱います。
        - **config.yml**: `generate_repo_list` スクリプトの実行時設定（APIキー、対象ユーザー名、出力パスなど）を定義するYAML形式のファイルです。
        - **config_manager.py**: 設定ファイル（`config.yml`、`secrets.toml`など）の読み込み、解析、アクセスを提供するロジックを管理します。
        - **date_formatter.py**: 日付や時刻の情報を特定のフォーマット（例: `YYYY-MM-DD`）に変換するユーティリティ関数を提供します。
        - **generate_repo_list.py**: プロジェクトのメインエントリーポイントとなるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を生成する際のテンプレートです。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換するロジックを扱います。
        - **markdown_generator.py**: 取得したリポジトリ情報から、Jekyll/GitHub Pagesに対応したMarkdownコンテンツを生成するロジックを担います。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、特定のパターンで記述されたバッジ情報を抽出するロジックを扱います。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整形する主要なロジックを管理します。
        - **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAML形式のファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算するロジックを提供します。
        - **strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を一元的に管理するYAML形式のファイルです。多言語対応や文言変更を容易にします。
        - **template_processor.py**: Jekyllのテンプレートエンジン（Liquidなど）や、Markdown生成時に使用するカスタムテンプレートの処理を担うロジックです。
        - **url_utils.py**: URLの生成、解析、バリデーションなど、URLに関連するさまざまなユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（特にプロジェクト概要の自動取得）をテストするためのスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトが格納されているディレクトリです。
    - **conftest.py**: `pytest` の共通フィクスチャやヘルパー関数を定義し、複数のテストファイルで共有可能にします。
    - **test_badge_generator_integration.py**: `badge_generator` の機能が正しく動作するか、他のモジュールと連携して期待通りの結果を出すかを検証する結合テストです。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトが、正しく大容量ファイルを検出するかどうかをテストします。
    - **test_config.py**: `config_manager` や関連する設定ファイルの読み込み、パース、値の取得が正しく行われるかをテストします。
    - **test_date_formatter.py**: `date_formatter` モジュールの日付整形機能が、さまざまな入力に対して正しい出力を生成するかをテストします。
    - **test_environment.py**: プロジェクトが想定する実行環境（必要な環境変数、依存関係など）が正しく設定されているかを検証するテストです。
    - **test_integration.py**: プロジェクトの主要なフロー（GitHub APIからのデータ取得からMarkdown生成まで）が全体として正しく機能するかを検証する結合テストです。
    - **test_markdown_generator.py**: `markdown_generator` が、与えられたデータから期待通りのMarkdown文字列を生成するかをテストします。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` が、リモートの`project-overview.md`ファイルから正しく概要を抽出できるかをテストします。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor` が、さまざまな形式の`README.md`から正確にバッジ情報を抽出できるかをテストします。
    - **test_repository_processor.py**: `repository_processor` が、GitHub APIから取得したリポジトリ生データを正しく処理・整形できるかをテストします。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**:
    - **`main()`**: プロジェクトのエントリーポイントとなる関数。GitHub APIからリポジトリ情報を取得し、処理してMarkdownファイルとして出力する一連の処理をオーケストレートします。
    - **`_parse_arguments()`**: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、スクリプトの実行に必要なパラメータを準備します。
- **src/generate_repo_list/badge_generator.py**:
    - **`generate_badge_markdown(badge_type: str, label: str, message: str, color: str = 'blue')`**: 指定されたタイプ、ラベル、メッセージ、色に基づいて、GitHub Actionsワークフローなどで使用できる形式のMarkdownバッジ文字列を生成します。
- **src/generate_repo_list/config_manager.py**:
    - **`load_config(config_path: str) -> dict`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書形式で返します。
    - **`load_secrets(secrets_path: str) -> dict`**: 指定されたパスからTOML形式の秘密情報ファイル（例: GitHubトークン）を読み込み、Pythonの辞書形式で返します。
- **src/generate_repo_list/date_formatter.py**:
    - **`format_iso_date(iso_string: str, format_str: str = '%Y-%m-%d') -> str`**: ISO 8601形式の日付文字列を受け取り、指定されたフォーマット文字列に従って整形された日付文字列を返します。
- **src/generate_repo_list/markdown_generator.py**:
    - **`generate_repository_entry(repo_data: dict, project_overview: Optional[str] = None) -> str`**: 処理された単一のリポジトリデータとオプションのプロジェクト概要を受け取り、そのリポジトリ表示用のMarkdownスニペットを生成します。
    - **`generate_index_markdown(repositories_markdown: List[str], username: str) -> str`**: 複数のリポジトリのMarkdownスニペットとユーザー名を受け取り、最終的な`index.md`ファイル全体を構成するMarkdownコンテンツを生成します。
- **src/generate_repo_list/project_overview_fetcher.py**:
    - **`fetch_project_overview(repo_name: str, config: dict) -> Optional[str]`**: 指定されたリポジトリ名と設定情報に基づき、そのリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から3行のプロジェクト概要をHTTPリクエストで取得します。
- **src/generate_repo_list/readme_badge_extractor.py**:
    - **`extract_badges_from_readme(readme_content: str) -> List[str]`**: READMEのコンテンツ文字列から、特定のパターンにマッチするバッジのMarkdown文字列を抽出し、リストとして返します。
- **src/generate_repo_list/repository_processor.py**:
    - **`process_repository_data(raw_repo_list: List[dict], overview_config: dict) -> List[dict]`**: GitHub APIから取得した生のリポジトリデータリストを受け取り、各リポジトリについて必要な情報の抽出、整形、プロジェクト概要の追加などを行い、表示に適した形式のリストを返します。
- **src/generate_repo_list/statistics_calculator.py**:
    - **`calculate_summary_statistics(processed_repo_list: List[dict]) -> dict`**: 処理されたリポジトリのリストを受け取り、総リポジトリ数、言語別の統計などの概要統計情報を計算して返します。
- **src/generate_repo_list/template_processor.py**:
    - **`render_template(template_content: str, data: dict) -> str`**: テンプレート文字列と埋め込むデータを受け取り、データをテンプレートに適用して最終的な文字列を生成します。（JekyllのLiquidテンプレートを模倣した処理を想定）
- **src/generate_repo_list/url_utils.py**:
    - **`construct_github_api_url(username: str) -> str`**: 指定されたGitHubユーザー名に基づき、GitHub APIからリポジトリ情報を取得するためのURLを生成します。
    - **`construct_github_repo_url(username: str, repo_name: str) -> str`**: 指定されたユーザー名とリポジトリ名に基づき、そのリポジトリのGitHub PagesサイトへのURLを生成します。
- **.github_automation/check_large_files/scripts/check_large_files.py**:
    - **`main()`**: 大容量ファイルチェックスクリプトのエントリーポイント。設定ファイルを読み込み、リポジトリ内のファイルを走査して、設定された閾値を超えるファイルを検出してレポートします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-26 07:10:08 JST
