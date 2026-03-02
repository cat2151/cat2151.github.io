Last updated: 2026-03-03

# Project Overview

## プロジェクト概要
- GitHub API を活用し、指定されたGitHubユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、GitHub Pages サイト向けにSEO最適化されたリポジトリ一覧ページをMarkdown形式で生成します。
- GitHubユーザーページの検索エンジンでの可視性を高め、リポジトリの発見性向上とLLMによる参照失敗の緩和を目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイト生成フレームワーク), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: GitHub (リポジトリホスティング、API提供), Git (バージョン管理システム)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: (直接的なビルドツールは使用されていません。Pythonスクリプトが生成処理を担います。)
- 言語機能: Python (主要なスクリプト開発言語)
- 自動化・CI/CD: (直接的なCI/CDパイプラインは明示されていませんが、Pythonスクリプトによる情報取得・ファイル生成という形で自動化を実現しています)
- 開発標準: ruff (PythonコードのLinterおよびFormatter), .editorconfig (エディタ間の設定統一)

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
- **.editorconfig**: 複数の開発者やエディタ間でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub ActionsなどのGitHub上の自動化処理に関連するスクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルのチェック機能に関するファイル群を格納します。
        - **README.md**: `check_large_files` 機能に関する説明を提供します。
        - **check-large-files.toml**: 大容量ファイルチェックツールの設定ファイルです。
        - **scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの目的、機能、使用方法、開発者向けヒントなどが記載されたメインドキュメントです。
- **_config.yml**: Jekyllサイト全体の挙動を制御する設定ファイルで、GitHub Pagesの表示設定なども含みます。
- **assets/**: サイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: サイトのアイコン（ファビコン）の異なるサイズです。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグやテストに使用されるスクリプトです。
- **generated-docs/**: プロジェクト概要取得機能によって参照される、各リポジトリの概要ファイル (`project-overview.md`) が配置されることが想定されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールで、サイトの所有権を確認するために配置されるファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって自動生成され、リポジトリ一覧が記述されるメインのMarkdownファイルです。JekyllによってGitHub Pagesのトップページとしてレンダリングされます。
- **issue-notes/**: 課題やメモ、検討事項などをMarkdown形式で記録するディレクトリです。
    - **22.md**: 特定の課題番号22に関する詳細なメモや議論が記述されたファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリのホーム画面アイコン、表示モード、起動URLなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **requirements-dev.txt**: プロジェクトの開発およびテストに必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: プロジェクトが本番環境で実行される際に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはクロールすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonコードのスタイルと品質を管理するためのLinterおよびFormatterであるRuffの設定ファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: `src` ディレクトリがPythonパッケージであることを示します。
    - **generate_repo_list/**: リポジトリ一覧を生成するコアロジックを含むPythonパッケージです。
        - **__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        - **badge_generator.py**: リポジトリの各種バッジ（言語、スター数など）を生成するロジックを実装しています。
        - **config.yml**: リポジトリ一覧生成スクリプトの実行に関する技術的パラメータ（例: プロジェクト概要取得機能の設定）を定義する設定ファイルです。
        - **config_manager.py**: `config.yml` や `secrets.toml` などの設定ファイルを読み込み、管理する役割を担います。
        - **date_formatter.py**: 日付情報を読みやすい形式に整形するためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトで、GitHub APIからの情報取得、データの処理、最終的なMarkdownファイルの生成を一連の流れとして実行します。
        - **json_ld_template.json**: 検索エンジンのリッチリザルト表示を強化するためのJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、整形するロジックを含みます。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツ（リポジトリごとの表示ブロックや一覧構造）を生成します。
        - **project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を自動的に取得するロジックを実装しています。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、特定のパターンで記述されたバッジ情報を抽出するロジックです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（整形、フィルタリング、追加データ取得など）を処理・変換する役割を担います。
        - **seo_template.yml**: SEOを意識したメタデータやキーワードなどのテンプレートを定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または抽出するロジックです。
        - **strings.yml**: ユーザーインターフェースに表示されるメッセージや文言、翻訳可能なテキストを管理するためのファイルです。
        - **template_processor.py**: Markdown生成時に使用されるテンプレートファイルの内容を読み込み、データに基づいて埋め込み処理を行うロジックを提供します。
        - **url_utils.py**: GitHub APIエンドポイントやリポジトリURLなど、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher` 機能の単体テストまたは結合テストを記述したスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **test_badge_generator_integration.py**: バッジ生成機能の結合テストを実行します。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストを実行します。
    - **test_config.py**: 設定ファイルの読み込みや管理機能のテストを実行します。
    - **test_date_formatter.py**: 日付整形機能のテストを実行します。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを実行します。
    - **test_integration.py**: プロジェクトの主要な部分が連携して正しく動作するかを確認する結合テストです。
    - **test_markdown_generator.py**: Markdown生成機能のテストを実行します。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストを実行します。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストを実行します。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストを実行します。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main()`: スクリプトのエントリポイント。コマンドライン引数を解析し、リポジトリ一覧の生成プロセスを開始します。
    - `generate_repository_list_markdown(username: str, output_file: str, limit: Optional[int] = None) -> None`: 指定されたGitHubユーザー名に基づきGitHub APIからリポジトリ情報を取得し、整形したMarkdown形式のリポジトリ一覧を指定されたファイルに出力します。`limit`オプションで処理するリポジトリ数を制限できます。
- **badge_generator.py**:
    - `generate_badge(repo_data: dict) -> str`: リポジトリのデータ（言語、スター数など）を受け取り、対応するMarkdown形式のバッジ文字列を生成して返します。
- **config_manager.py**:
    - `load_config(config_path: str) -> dict`: 指定されたパスのYAML形式設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    - `load_secrets(secrets_path: str) -> dict`: 指定されたパスのTOML形式シークレットファイル（例：GitHubトークン）を読み込み、辞書として返します。
- **date_formatter.py**:
    - `format_date(iso_date_string: str) -> str`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式（例：「YYYY年MM月DD日」）に整形して返します。
- **language_info.py**:
    - `get_language_data(repo_data: dict) -> dict`: リポジトリの主要言語やその他の言語に関する情報を抽出し、整理されたデータ構造で返します。
- **markdown_generator.py**:
    - `generate_repo_markdown(repo_info: dict) -> str`: 単一のリポジトリの処理済み情報を受け取り、そのリポジトリを表示するためのMarkdownブロック（タイトル、説明、バッジなど）を生成して返します。
    - `generate_index_markdown(repos_markdown_list: list) -> str`: 複数のリポジトリのMarkdownブロックのリストを受け取り、それらを結合して最終的なリポジトリ一覧ページのMarkdown構造を生成します。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_name: str, config: dict) -> Optional[str]`: 指定されたリポジトリ名と設定に基づき、そのリポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出し、返します。必要に応じてGitHub APIを介してファイル内容を取得します。
- **readme_badge_extractor.py**:
    - `extract_badges_from_readme(readme_content: str) -> list`: リポジトリのREADMEコンテンツ文字列から、特定のパターン（例：Markdown画像リンク）に一致するバッジ情報を解析・抽出してリストで返します。
- **repository_processor.py**:
    - `process_repo_data(raw_repo_data: dict, config: dict) -> dict`: GitHub APIから取得した生のリポジトリデータを受け取り、日付の整形、概要の取得、バッジの追加など、表示に必要な追加処理を施した後に整形されたリポジトリデータを返します。
- **statistics_calculator.py**:
    - `calculate_repo_statistics(repo_data: dict) -> dict`: リポジトリのスター数、フォーク数、ウォッチ数、最終更新日などの統計情報を計算または抽出し、辞書形式で返します。
- **template_processor.py**:
    - `apply_template(template_content: str, data: dict) -> str`: テンプレート文字列と、テンプレート内のプレースホルダーに埋め込むデータを受け取り、最終的な文字列コンテンツを生成して返します。
- **url_utils.py**:
    - `construct_github_api_url(username: str) -> str`: 指定されたGitHubユーザー名に基づき、GitHub APIの特定のエンドポイントURLを構築して返します。
    - `get_github_repo_url(username: str, repo_name: str) -> str`: 指定されたユーザー名とリポジトリ名に基づき、GitHub上のリポジトリURLを構築して返します。
- **.github_automation/check_large_files/scripts/check_large_files.py**:
    - `main()`: 大容量ファイルをチェックするスクリプトのエントリポイント。設定ファイルで定義された基準に基づいて、指定されたリポジトリ内の大容量ファイルを検出・報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-03 07:10:16 JST
