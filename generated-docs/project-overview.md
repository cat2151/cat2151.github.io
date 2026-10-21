Last updated: 2026-10-22

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成し、検索エンジン最適化（SEO）を強化します。
- GitHub APIを活用してリポジトリ情報を取得し、Jekyllに対応したMarkdownファイルとして出力します。
- 各リポジトリの概要を自動抽出し、訪問者にとって分かりやすく、魅力的な情報提供を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータで、MarkdownファイルをHTMLに変換), **Markdown** (コンテンツ記述言語), **HTML/CSS/JavaScript** (Jekyllテーマや生成コンテンツの一部として使用), **PWA (Progressive Web App)** 関連ファイル (manifest.json, faviconなど)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (主要なプログラミング言語), **Git** (バージョン管理システム), **pytest** (テストフレームワーク), **ruff** (Pythonコードのリンター・フォーマッター)。
- テスト: **pytest** (Pythonのテストコード実行フレームワーク)。
- ビルドツール: **Jekyll** (GitHub Pagesが利用する静的サイトジェネレータで、サイトをビルドする), **Pythonスクリプト** (リポジトリ情報を取得しMarkdownファイルを生成するプロセス自体がビルドの役割を果たす)。
- 言語機能: **Python** (スクリプト開発言語), **Markdown** (生成コンテンツおよびドキュメント記述言語), **YAML** (設定ファイル形式), **JSON** (データ交換形式、特にJSON-LDテンプレートに使用)。
- 自動化・CI/CD: **GitHub Actions** (GitHubリポジトリの自動化をサポートするプラットフォーム。明示的なワークフローはないものの、システムは自動生成を前提とする), **Pythonスクリプト** (リポジトリ一覧生成の自動化本体)。
- 開発標準: **ruff** (Pythonコードの品質と一貫性を保つためのリンターおよびフォーマッター), **.editorconfig** (異なるエディタやIDE間でコーディングスタイルを統一するための設定)。

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
- **`.editorconfig`**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどのリポジトリ自動化に関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files`機能に関する説明ドキュメントです。
    - **`check-large-files.toml`**: リポジトリ内の大容量ファイルをチェックする際のしきい値やルールを設定するファイルです。
    - **`scripts/check_large_files.py`**: GitHubリポジトリ内の指定されたサイズを超えるファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリ（例: ビルド生成物、環境固有の設定）を指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）が記述されたファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、クイックスタートガイド、設定方法、ライセンスなどの概要を説明する主要なドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが記述されます。
- **`assets/`**: ウェブサイトで利用される画像、アイコンなどの静的リソースを格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブやブックマークなどに表示されるウェブサイトのアイコンファイル群です。
- **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) の動作確認やデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: GitHub Pagesサイト用に生成されたドキュメントや一時ファイルを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために利用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページ（トップページ）として機能するMarkdownファイルです。リポジトリ一覧の生成結果がここに書き込まれます。
- **`issue-notes/`**: 開発中の特定の課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定のIssue（課題）番号22に関連する詳細なメモや考察が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）として機能させるためのメタデータ（アプリ名、アイコン、表示設定など）を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出方法や実行オプションが記述されます。
- **`requirements-dev.txt`**: 開発環境やテスト環境でのみ必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またどのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードの品質チェック（リンティング）と自動フォーマットを行うツールRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成システムの主要ロジックを格納するPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージとして認識させるための初期化ファイルです。
        - **`badge_generator.py`**: リポジトリのステータス（例: 使用言語、ライセンス）を示すバッジのMarkdownを生成するロジックを含みます。
        - **`config.yml`**: リポジトリ一覧生成処理に関する技術的パラメータ（例: APIタイムアウト、キャッシュ設定、プロジェクト概要取得設定）を定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、プログラムから利用しやすい形式で提供・管理するモジュールです。
        - **`date_formatter.py`**: 日付や時刻の情報を指定された形式に整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このシステムのメインスクリプトです。GitHub APIからの情報取得、データの加工、Markdown生成までの一連の処理を orchestrate します。
        - **`json_ld_template.json`**: SEO最適化のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`language_info.py`**: リポジトリの使用言語情報を取得し、表示に適した形式に処理するためのロジックを含みます。
        - **`markdown_generator.py`**: 取得・加工されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツ（リポジトリ一覧など）を生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリに存在する`generated-docs/project-overview.md`ファイルから、プロジェクトの3行概要を抽出するロジックを含みます。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジックです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、プログラム内で扱いやすい形式に加工する役割を担います。
        - **`seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータや構造化データのテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのロジックを提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するためのYAML形式の設定ファイルです。
        - **`template_processor.py`**: Markdownなどのテンプレートファイルとデータを使って、最終的な出力テキストを生成する処理を担います。
        - **`url_utils.py`**: GitHub APIのエンドポイントURLの構築や、リポジトリURLの解析など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュール（プロジェクト概要取得機能）の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト実行時に共通で利用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを記述したファイルです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
    - **`test_config.py`**: 設定ファイルの読み込みや解析に関するテストを記述したファイルです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストを記述したファイルです。
    - **`test_environment.py`**: 実行環境や依存関係に関するテストを記述したファイルです。
    - **`test_integration.py`**: システム全体の連携動作を確認する統合テストを記述したファイルです。
    - **`test_markdown_generator.py`**: `markdown_generator`モジュールのテストを記述したファイルです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのテストを記述したファイルです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - **`test_repository_processor.py`**: リポジトリデータ処理モジュールのテストを記述したファイルです。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャや実装詳細を特定できませんが、各ファイルの役割から以下の主要な関数群が存在すると推測できます。

- **`badge_generator.py`**:
    - `generate_badge(repo_data)`: リポジトリ情報 `repo_data` を基に、言語やライセンスなどのバッジを示すMarkdown文字列を生成します。
- **`config_manager.py`**:
    - `load_config(config_path)`: 指定されたパスから設定ファイル（YAMLなど）を読み込み、Pythonオブジェクトとして返します。
    - `get_setting(key_path)`: 設定オブジェクトから特定のキーパスに対応する設定値を取得します。
- **`date_formatter.py`**:
    - `format_date(datetime_obj, format_string)`: 日時オブジェクトを特定の `format_string` に従って整形した文字列を返します。
- **`generate_repo_list.py`**:
    - `main()`: プログラムのエントリポイントで、コマンドライン引数の解析、GitHub APIからの情報取得、リポジトリ処理、Markdown生成、ファイル出力までの一連の処理を統括します。
    - `run_generation(username, output_file, limit)`: リポジトリ一覧生成の主要なロジックを実行します。
- **`language_info.py`**:
    - `get_top_languages(repo_data)`: リポジトリの主要言語情報を抽出し、整形します。
    - `format_language_display(languages)`: 言語情報を表示に適した文字列形式に変換します。
- **`markdown_generator.py`**:
    - `generate_repository_section(repo_data, overview_text)`: 個々のリポジトリの情報を基に、そのリポジトリのMarkdownセクション（タイトル、説明、バッジなど）を生成します。
    - `generate_index_page(repositories_markdown)`: 複数のリポジトリセクションを組み合わせて、最終的な `index.md` ページ全体のMarkdownコンテンツを生成します。
- **`project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリから `project-overview.md` ファイルの内容をフェッチします。
    - `extract_overview_text(markdown_content, config)`: フェッチしたMarkdownコンテンツから、設定に基づきプロジェクトの3行概要テキストを抽出します。
- **`repository_processor.py`**:
    - `fetch_repositories_from_github_api(username, github_token, limit)`: 指定されたGitHubユーザーのリポジトリ情報をGitHub API経由で取得します。
    - `process_repository_data(raw_repo_list)`: APIから取得した生のリポジトリデータ（JSON形式など）を、プログラムで扱いやすいPythonオブジェクトのリストに整形・加工します。
- **`statistics_calculator.py`**:
    - `calculate_stars(repo_data)`: リポジトリのスター数を計算または抽出します。
    - `get_fork_status(repo_data)`: リポジトリがフォークであるかどうかを判定し、その状態を返します。
- **`template_processor.py`**:
    - `render_template(template_string, data)`: テンプレート文字列とデータ辞書を受け取り、データをテンプレートに埋め込んで最終的なテキストを生成します。
- **`url_utils.py`**:
    - `build_github_api_url(username)`: 指定されたユーザー名に基づいてGitHub APIのリポジトリ一覧URLを構築します。
    - `build_github_repo_url(username, repo_name)`: 指定されたユーザー名とリポジトリ名に基づいてGitHubリポジトリのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-22 07:11:21 JST
