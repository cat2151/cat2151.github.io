Last updated: 2026-10-15

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHub Pagesサイト向けにリポジトリ一覧を自動生成します。
- SEO最適化されたMarkdown形式でリポジトリ情報を出力し、検索エンジンからの可視性を高めます。
- 各リポジトリの概要、バッジ、分類機能を提供し、ポートフォリオサイトとしての利便性を向上させます。

## 技術スタック
- フロントエンド: GitHub Pages, Jekyll, Markdown
  GitHub Pagesは静的サイトホスティングサービスで、本プロジェクトで生成されたMarkdownファイルをJekyllが処理し、公開サイトとして表示します。
- 音楽・オーディオ: (該当なし)
- 開発ツール: Python, GitHub API (requests), YAML, TOML, `argparse`
  Pythonはスクリプトの中心言語であり、`requests`ライブラリを使用してGitHub APIと連携します。設定ファイルはYAMLやTOML形式で管理され、`argparse`でコマンドライン引数を処理します。
- テスト: Pytest
  Pythonで書かれたテストフレームワークで、プロジェクトの各機能の単体テストや統合テストを実行し、品質を保証します。
- ビルドツール: Pythonスクリプト
  専用のビルドツールは使用せず、Pythonスクリプト自体がGitHub APIからの情報取得、データ処理、Markdownファイル生成の一連の「ビルド」プロセスを担います。
- 言語機能: Python
  スクリプトの全機能はPythonで実装されており、GitHub APIとの連携、ファイル操作、文字列処理、データ構造の管理などに利用されます。
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリから推測)
  `.github_automation`ディレクトリの存在から、GitHub Actionsを用いてコードの自動チェックやデプロイなどの継続的インテグレーション/デリバリーが設定されている可能性があります。
- 開発標準: Ruff, EditorConfig
  Ruffは高速なPythonリンターおよびフォーマッターで、コードスタイルの一貫性を保ち、品質を向上させます。EditorConfigは異なるエディタやIDE間でコードスタイルを統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるテキストエディタやIDE間で、インデントスタイル、文字コード、改行コードなどのコードフォーマット設定を統一するためのファイルです。
- **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化処理に関するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルがないかチェックするための設定とスクリプトを含みます。
        - **`README.md`**: `check_large_files`機能に関する説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記載されています。
- **`README.md`**: プロジェクトの概要、目的、設定方法、使用方法などを説明するメインドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定を定義するファイルです。
- **`assets/`**: ウェブサイトで使用される画像、ファビコン、アイコンなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher`モジュールのデバッグや単体動作確認のために使用されるスクリプトです。
- **`generated-docs/`**: プロジェクト内で生成されるドキュメントや一時ファイルを格納するディレクトリです。また、各リポジトリの概要取得元としても利用されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために使用されるHTMLファイルです。
- **`index.md`**: 本プロジェクトによって生成される、リポジトリ一覧のメイン出力ファイルです。GitHub Pagesで公開されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録するMarkdownファイルを格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示情報（名前、アイコン、起動URLなど）を定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために最低限必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイルです。コードスタイルのルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成システムのコアロジックを含むPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや情報を示すバッジのMarkdown文字列を生成する機能を提供します。
        - **`config.yml`**: プロジェクト概要取得機能などの技術的なパラメータや設定を定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: YAMLやTOML形式の設定ファイルを読み込み、設定値にアクセスするための機能を提供します。
        - **`date_formatter.py`**: GitHub APIから取得した日付文字列を、人間が読みやすい形式に整形する機能を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインスクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために利用されるJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・表示する機能を提供します。
        - **`markdown_generator.py`**: 処理されたリポジトリデータとテンプレートを使用して、最終的なMarkdownコンテンツを構築する責任を持つモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        - **`repository_processor.py`**: 個々のGitHubリポジトリの生データを取得し、プロジェクトで利用しやすい形式に整形・加工するロジックをカプセル化しています。
        - **`seo_template.yml`**: SEOメタデータ（タイトル、ディスクリプションなど）を定義するためのYAMLテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: 生成されるMarkdownコンテンツやUIに表示される各種メッセージ、文言、ラベルなどを一元的に管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成に使用するテンプレート（JekyllのLiquidなど）の処理やレンダリングを行う機能を提供します。
        - **`url_utils.py`**: GitHub APIエンドポイントやリポジトリURLなどを構築するためのユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールに関する単体テストを記述したファイルです。
- **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestのフィクスチャやヘルパー関数など、テスト全体で共有される設定を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを行います。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトのテストを行います。
    - **`test_config.py`**: 設定ファイル (`config.yml`, `secrets.toml`など) の読み込みと管理に関するテストを行います。
    - **`test_date_formatter.py`**: `date_formatter`モジュールのテストを行います。
    - **`test_environment.py`**: 開発環境のセットアップや依存関係に関するテストを行います。
    - **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストを行います。
    - **`test_markdown_generator.py`**: `markdown_generator`モジュールのテストを行います。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのテストを行います。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのテストを行います。
    - **`test_repository_processor.py`**: `repository_processor`モジュールのテストを行います。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`:
        - **役割**: コマンドラインスクリプトのエントリポイント。引数を解析し、リポジトリ一覧生成の主要な処理フローを orchestrate します。
        - **引数**: なし (システム引数 `sys.argv` を内部で利用)。
        - **戻り値**: なし。
        - **機能**: `argparse` を用いてユーザー名、出力ファイル名、処理リミットを取得し、`generate_repo_list` 関数を呼び出します。
    - `generate_repo_list(username: str, output_file: str, limit: Optional[int] = None) -> None`:
        - **役割**: 指定されたGitHubユーザーのリポジトリ情報を取得し、Markdown形式で整形されたリポジトリ一覧を生成し、指定されたファイルに出力します。
        - **引数**:
            - `username`: GitHubユーザー名。
            - `output_file`: 生成されたMarkdownを出力するファイルパス。
            - `limit`: (オプション) 処理するリポジトリ数の上限。開発時の高速テストに利用。
        - **戻り値**: なし。
        - **機能**: `config_manager`から設定を読み込み、`repository_processor`でリポジトリ情報を取得・加工し、`markdown_generator`で最終的なMarkdownコンテンツを生成してファイルに書き込みます。
- **`src/generate_repo_list/repository_processor.py`**
    - `fetch_repositories(username: str, token: str, limit: Optional[int] = None) -> list`:
        - **役割**: GitHub APIを介して、指定されたユーザーのリポジトリ情報を取得します。
        - **引数**:
            - `username`: GitHubユーザー名。
            - `token`: GitHub API認証用のパーソナルアクセストークン。
            - `limit`: (オプション) 取得するリポジトリ数の上限。
        - **戻り値**: 取得したリポジトリデータのリスト。
        - **機能**: `url_utils`を使ってAPIエンドポイントを構築し、`requests`ライブラリでAPIリクエストを実行します。
    - `process_repository_data(repo_data: dict, config: dict) -> dict`:
        - **役割**: 生のリポジトリデータ（GitHub APIから取得した辞書）を処理し、表示に必要な情報を抽出・整形します。
        - **引数**:
            - `repo_data`: GitHub APIから取得した単一のリポジトリの生データ。
            - `config`: プロジェクトの設定情報。
        - **戻り値**: 処理済みのリポジトリ情報を含む辞書。
        - **機能**: `project_overview_fetcher`で概要を取得し、`readme_badge_extractor`でバッジを抽出し、`date_formatter`で日付を整形し、`statistics_calculator`で統計情報を計算します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name: str, owner: str, branch: str, config: dict, token: str) -> Optional[str]`:
        - **役割**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出します。
        - **引数**:
            - `repo_name`: リポジトリ名。
            - `owner`: リポジトリの所有者（ユーザー名）。
            - `branch`: 対象となるブランチ名（通常は`main`または`master`）。
            - `config`: プロジェクトの設定情報。
            - `token`: GitHub API認証用のトークン。
        - **戻り値**: 抽出された3行の概要説明、または抽出できなかった場合は`None`。
        - **機能**: GitHub APIを介して指定されたファイルのコンテンツを取得し、正規表現などで「プロジェクト概要」セクションから3行を抽出します。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_markdown(repo_list: list, seo_data: dict, strings: dict, config: dict) -> str`:
        - **役割**: 処理されたリポジトリ情報、SEOデータ、表示文字列、設定情報を用いて、最終的なMarkdownコンテンツを生成します。
        - **引数**:
            - `repo_list`: 処理済みのリポジトリ情報のリスト。
            - `seo_data`: SEOメタデータを含む辞書。
            - `strings`: 表示メッセージや文言を含む辞書。
            - `config`: プロジェクトの設定情報。
        - **戻り値**: 生成されたMarkdownコンテンツの文字列。
        - **機能**: テンプレートファイル (`seo_template.yml`や`json_ld_template.json`など) を`template_processor`で処理し、各リポジトリの情報を組み合わせてMarkdownを構築します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(filepath: str) -> dict`:
        - **役割**: 指定されたパスのYAMLまたはTOML形式の設定ファイルを読み込み、辞書として返します。
        - **引数**:
            - `filepath`: 設定ファイルのパス。
        - **戻り値**: 設定内容を含む辞書。
        - **機能**: ファイルの拡張子に応じて`yaml`または`toml`ライブラリを使用してファイルを解析します。
- **`src/generate_repo_list/date_formatter.py`**
    - `format_date(datetime_str: str) -> str`:
        - **役割**: ISO 8601形式の日付/時刻文字列を、より読みやすい「YYYY年MM月DD日」のような形式に整形します。
        - **引数**:
            - `datetime_str`: ISO 8601形式の日付/時刻文字列 (例: "2023-10-27T10:00:00Z")。
        - **戻り値**: 整形された日付文字列。
        - **機能**: `datetime`モジュールを使用して日付をパースし、指定されたフォーマットで文字列に変換します。
- **`src/generate_repo_list/badge_generator.py`**
    - `create_badge_markdown(label: str, message: str, color: str = 'blue') -> str`:
        - **役割**: Shields.ioのスタイルでMarkdown形式のバッジ文字列を生成します。
        - **引数**:
            - `label`: バッジの左側に表示されるラベル。
            - `message`: バッジの右側に表示されるメッセージ。
            - `color`: (オプション) バッジの色。
        - **戻り値**: 生成されたバッジのMarkdown文字列。
        - **機能**: 提供された情報を使ってShields.ioのURLを構築し、Markdownの画像リンク形式で返します。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
└── generate_repo_list(username, output_file, limit) (src/generate_repo_list/generate_repo_list.py)
    ├── config_manager.load_config(filepath) (src/generate_repo_list/config_manager.py)
    ├── repository_processor.fetch_repositories(username, token, limit) (src/generate_repo_list/repository_processor.py)
    │   └── url_utils.build_github_api_url(endpoint, params) (src/generate_repo_list/url_utils.py)
    ├── repository_processor.process_repository_data(repo_data, config) (src/generate_repo_list/repository_processor.py)
    │   ├── project_overview_fetcher.fetch_project_overview(repo_name, owner, branch, config, token) (src/generate_repo_list/project_overview_fetcher.py)
    │   ├── readme_badge_extractor.extract_badges(readme_content) (src/generate_repo_list/readme_badge_extractor.py)
    │   ├── date_formatter.format_date(datetime_str) (src/generate_repo_list/date_formatter.py)
    │   └── statistics_calculator.calculate_stats(repo_data) (src/generate_repo_list/statistics_calculator.py)
    └── markdown_generator.generate_markdown(repo_list, seo_data, strings, config) (src/generate_repo_list/markdown_generator.py)
        ├── template_processor.apply_template(template_content, context) (src/generate_repo_list/template_processor.py)
        └── badge_generator.create_badge_markdown(label, message, color) (src/generate_repo_list/badge_generator.py)

---
Generated at: 2026-10-15 07:11:32 JST
