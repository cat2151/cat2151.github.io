Last updated: 2026-03-11

# Project Overview

## プロジェクト概要
- GitHub API を活用し、GitHub Pages サイト用のリポジトリ一覧を自動生成するシステムです。
- 生成されたコンテンツはSEOに最適化され、検索エンジンやLLMによるリポジトリ参照を促進します。
- 各リポジトリの概要、バッジ、分類などを自動で表示し、GitHub Pagesでのポートフォリオ公開を効率化します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として、生成されたMarkdownファイルを静的サイトに変換), Markdown (リポジトリ一覧の出力形式), HTML (最終的なWebページの構成要素)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), YAML (設定ファイル管理), TOML (設定ファイル管理), JSON (データ形式、特にSEO構造化データ用)
- テスト: pytest (Pythonコードの単体テストおよび統合テストフレームワーク)
- ビルドツール: なし (専用のビルドツールは使用せず、Pythonスクリプトがコンテンツ生成の役割を担います)
- 言語機能: Python (プロジェクト全体の開発基盤となるプログラミング言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得), Pythonスクリプトによるコンテンツ生成の自動化 (継続的なコンテンツデプロイをサポート)
- 開発標準: ruff (Pythonコードのフォーマッター兼リンター), .editorconfig (エディタ設定を統一し、異なる開発環境間でのコードスタイルの一貫性を保つ)

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどのコードフォーマットを統一するための設定ファイル。
- **.github_automation/check_large_files/**: GitHub Actionsなどで、リポジトリ内の大規模なファイルをチェックし、管理するための自動化スクリプトおよび設定ファイル群。
  - **README.md**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメント。
  - **check-large-files.toml**: 大規模ファイルチェックツールの設定ファイル。チェック対象のファイルサイズや除外パスなどを定義。
  - **scripts/check_large_files.py**: 実際に大規模ファイルを検出・報告するPythonスクリプト。
- **.gitignore**: Gitによってバージョン管理されるべきではないファイルやディレクトリ（例: ビルド成果物、一時ファイル、個人設定ファイル）を指定する設定ファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクト全体の概要、目的、使い方、インストール方法などを説明するメインのドキュメント。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義。
- **assets/**: GitHub Pagesサイトで利用される静的アセット（画像、ファビコンなど）を格納するディレクトリ。
  - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: 異なるサイズのファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher.py` モジュールのデバッグやテスト実行のために用意されたスクリプト。
- **generated-docs/**: 他のリポジトリから取得された `project-overview.md` ファイルのキャッシュや、生成されたドキュメントを一時的に格納するためのディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールによるサイトの所有権確認に使用されるHTMLファイル。
- **index.md**: GitHub Pagesサイトのトップページを構成するMarkdownファイル。このプロジェクトによって自動生成されたリポジトリ一覧がここに出力される。
- **issue-notes/22.md**: 開発中に特定された課題や検討事項に関するメモを記録したMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。アプリの名称、アイコン、表示モードなどを定義し、ユーザーがWebサイトをデバイスのホーム画面に追加できるようにする。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テストの実行方法、検出パス、プラグインなどを設定。
- **requirements-dev.txt**: 開発・テスト環境でのみ必要となるPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: 本番環境（スクリプト実行時）で必要となるPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや潜在的なバグの検出ルールを定義。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックが格納されたPythonパッケージ。
  - **__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
  - **badge_generator.py**: リポジトリのステータス（アーカイブ、フォークなど）に応じたバッジを生成するロジックを実装。
  - **config.yml**: プロジェクト概要取得機能など、リポジトリ一覧生成システムの動作に関する技術的パラメータを設定するYAMLファイル。
  - **config_manager.py**: YAML形式の設定ファイルを読み込み、プログラムから設定値にアクセスするためのユーティリティを提供。
  - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供。
  - **generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからのリポジトリ情報取得、情報の加工、Markdown形式での出力までの一連の処理を統括。
  - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を生成する際のテンプレート。
  - **language_info.py**: リポジトリで使用されているプログラミング言語の統計情報（割合など）を処理・表示するためのロジック。
  - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdown形式のコンテンツを生成するロジックを実装。
  - **project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を自動で取得するモジュール。
  - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、shields.ioなどのサービスで生成されたバッジの情報を抽出するモジュール。
  - **repository_processor.py**: GitHub APIから取得した個々のリポジトリオブジェクトを、システムが利用しやすい形式に整形・加工する役割を担う。
  - **seo_template.yml**: SEO関連のメタデータや、JSON-LD生成のための構造化データに関する設定テンプレート。
  - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュール。
  - **strings.yml**: 生成されるMarkdownコンテンツやUIメッセージなどで使用される固定文言を一元的に管理するYAMLファイル。多言語対応の基盤にもなりうる。
  - **template_processor.py**: Markdown生成時に、テンプレートエンジン（例: Jinja2）を使用してプレースホルダーを実際のデータで置き換える処理を担う。
  - **url_utils.py**: URLの構築、解析、検証など、URL操作に関するユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得と抽出）を検証するためのテストスクリプト。
- **tests/**: プロジェクト全体のテストファイルを格納するディレクトリ。
  - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
  - **test_check_large_files.py**: `.github_automation/check_large_files/` のスクリプトのテスト。
  - **test_config.py**: 設定ファイルの読み込みや管理機能のテスト。
  - **test_date_formatter.py**: 日付整形ユーティリティのテスト。
  - **test_environment.py**: 開発・実行環境のセットアップや依存関係に関するテスト。
  - **test_integration.py**: 主要な機能間の連携を検証する統合テスト。
  - **test_markdown_generator.py**: Markdown生成ロジックのテスト。
  - **test_project_overview_fetcher.py**: プロジェクト概要抽出機能のテスト。
  - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
  - **test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細なリストを抽出できませんでしたが、各Pythonファイルの役割に基づき、想定される主要な関数の機能について説明します。

- **badge_generator.py**
  - **generate_status_badge(status: str) -> str**: リポジトリのステータス（例: "Archived", "Fork"）を表すMarkdown形式のバッジ文字列を生成します。特定の引数を受け取り、対応するバッジの文字列を返します。
- **config_manager.py**
  - **load_config(file_path: str) -> dict**: 指定されたYAML設定ファイルを読み込み、その内容をPythonの辞書形式で返します。ファイルパスを引数として受け取ります。
  - **get_value(config_dict: dict, key_path: str, default=None)**: 設定辞書から指定されたキーパス（例: "project_overview.enabled"）の値を取得します。キーが見つからない場合はデフォルト値を返します。
- **date_formatter.py**
  - **format_date(datetime_obj: datetime) -> str**: `datetime` オブジェクトを受け取り、指定されたフォーマット（例: "YYYY-MM-DD"）で日付文字列に整形して返します。
- **generate_repo_list.py**
  - **main()**: プログラムの主要なエントリポイント。GitHub APIからリポジトリ情報を取得し、各リポジトリを処理し、最終的なMarkdownコンテンツを生成して指定されたファイルに出力する一連のプロセスを制御します。コマンドライン引数を解析して動作を調整します。
- **language_info.py**
  - **get_language_stats(repo_data: dict) -> dict**: リポジトリの言語情報（例: 使用言語とそのバイト数）を解析し、各言語の割合などの統計情報を計算して返します。
- **markdown_generator.py**
  - **generate_repo_list_markdown(repositories: list, config: dict) -> str**: 処理済みのリポジトリ情報のリストと設定情報を受け取り、それらを基にGitHub Pages用のリポジトリ一覧のMarkdownコンテンツ全体を生成して返します。
- **project_overview_fetcher.py**
  - **fetch_overview(username: str, repo_name: str, config: dict) -> str**: 指定されたユーザー名とリポジトリ名から、対象リポジトリの `generated-docs/project-overview.md` ファイルの内容を取得し、設定に従って3行のプロジェクト概要を抽出します。
- **readme_badge_extractor.py**
  - **extract_badges(readme_content: str) -> list**: READMEのMarkdownコンテンツを受け取り、その中からShiel.ioなどのサービスで生成されたバッジのURLやテキスト情報を抽出してリスト形式で返します。
- **repository_processor.py**
  - **process_repository(repo_data: dict, config: dict) -> dict**: GitHub APIから取得した生のリポジトリデータと設定を受け取り、表示に必要な情報（プロジェクト概要、バッジ、整形された日付など）を追加・加工して、整形されたリポジトリ情報を辞書形式で返します。
- **statistics_calculator.py**
  - **calculate_repo_stats(repo_data: dict) -> dict**: リポジトリのスター数、フォーク数、ウォッチャー数、最終更新日などの統計情報を計算し、整理して返します。
- **template_processor.py**
  - **render_template(template_path: str, data: dict) -> str**: 指定されたテンプレートファイル（例: Markdownテンプレート）とデータ辞書を受け取り、テンプレート内のプレースホルダーをデータで置き換えて、最終的な文字列を生成します。
- **url_utils.py**
  - **build_github_repo_url(username: str, repo_name: str) -> str**: GitHubユーザー名とリポジトリ名から、対応するGitHubリポジトリのURLを構築して返します。

## 関数呼び出し階層ツリー
```
提供された情報からは関数間の具体的な呼び出し階層を分析できませんでした。
しかし、主要な実行フローは `src/generate_repo_list/generate_repo_list.py` の `main` 関数から開始され、
以下のモジュール群が順次、または連携して呼び出されることが推測されます。

- `config_manager.py`: 設定ファイルの読み込み
- `repository_processor.py`: 個々のリポジトリ情報の処理
- `project_overview_fetcher.py`: 各リポジトリの概要取得
- `readme_badge_extractor.py`: READMEからのバッジ抽出
- `badge_generator.py`: バッジの生成
- `date_formatter.py`: 日付の整形
- `language_info.py`: 言語統計の処理
- `statistics_calculator.py`: リポジトリ統計の計算
- `markdown_generator.py`: 最終的なMarkdownコンテンツの生成
- `template_processor.py`: テンプレートのレンダリング
- `url_utils.py`: URLの構築

---
Generated at: 2026-03-11 07:08:58 JST
