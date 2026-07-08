Last updated: 2026-07-09

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHub APIでリポジトリ情報を取得しMarkdownを自動生成します。
- 検索エンジンへの露出を高め、LLMによるリポジトリ参照失敗を緩和するSEO最適化システムです。
- バッジ表示、分類、各リポジトリの概要自動取得など、豊富な機能で情報可視化と開発効率を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) は、生成されたMarkdownファイルを静的ウェブサイトとして公開するための静的サイトジェネレータです。最終的なWebページの表示を担います。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連の技術は使用していません。
- 開発ツール:
    - Python: プロジェクトの主要な開発言語として、データ処理、API連携、ファイル生成などに利用されます。
    - Ruff: Pythonコードの品質を保証するためのリンターおよびフォーマッター。コードスタイルの統一とバグの早期発見を支援します。
    - Pytest: Pythonで書かれたコードのテストを実行するためのフレームワーク。コードの信頼性を確保します。
- テスト:
    - Pytest: プロジェクト内の各モジュールや機能が意図通りに動作するかを検証するためのテストフレームワークです。
- ビルドツール:
    - Pythonスクリプト (`generate_repo_list.py`): GitHub APIから取得した情報を元に、GitHub Pages用のMarkdownファイルを生成する中心的なロジックを実装しています。
    - Jekyll (概念的): 生成されたMarkdownファイルを実際のHTMLページに変換し、GitHub Pagesサイトとして公開する役割を担います。
- 言語機能:
    - Python: プロジェクトの全ロジックがPythonで実装されており、GitHub APIとの連携、データ処理、ファイルI/Oなどを行います。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation` ディレクトリの存在から、コードの品質チェック（例: 大容量ファイルチェック）などの自動化処理にGitHub Actionsが利用されていることが示唆されます。
- 開発標準:
    - Ruff: Pythonコードのスタイルガイド強制、整形、および品質チェックを自動化し、一貫したコードベースを維持します。
    - .editorconfig: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタ間でのコーディングスタイル（インデントサイズ、文字コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定ファイルを格納するディレクトリです。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルのチェック機能に関する説明が記述されたREADMEファイルです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定を定義するTOML形式のファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するためのファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイルです。
- **`README.md`**: このプロジェクト全体の目的、機能、使い方、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどを定義します。
- **`assets/`**: サイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
- **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグやテスト実行に使用される可能性のあるスクリプトです。
- **`generated-docs/`**: 各リポジトリの `project-overview.md` ファイルが存在するパスの例や、生成されたドキュメントの一時的な格納場所として使用されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: 生成されたリポジトリ一覧のマークダウンコンテンツが出力されるメインファイルです。Jekyllによってウェブページとして表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項に関するメモを格納するディレクトリです。
- **`issue-notes/22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや議論を含むマークダウンファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、アプリの名称、アイコン、表示モードなどを定義します。
- **`pytest.ini`**: `pytest` テストフレームワークの設定ファイルで、テスト検出パターン、オプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境でのみ必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行するために必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: `ruff` リンター・フォーマッターの設定ファイルで、コーディングスタイルルールなどを定義します。
- **`src/`**: プロジェクトのソースコードを格納する主要なディレクトリです。
- **`src/__init__.py`**: Pythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧生成機能のコアロジックを格納するPythonパッケージです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` がPythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを含むスクリプトです。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの技術的パラメータ（例：プロジェクト概要取得機能の設定、タイムアウトなど）を定義する設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` やその他の設定ファイルを読み込み、管理するロジックを含むスクリプトです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのロジックを含むスクリプトです。
- **`src/generate_repo_list/generate_repo_list.py`**: リポジトリ一覧生成プロセスのメインエントリポイントとなるスクリプトです。GitHub API呼び出し、データ処理、Markdown生成をオーケストレートします。
- **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のためのJSON-LD形式の構造化データテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理するロジックを含むスクリプトです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを含むスクリプトです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得するロジックを含むスクリプトです。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するロジックを含むスクリプトです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報（説明、言語、最終更新日など）を抽出・整形するロジックを含むスクリプトです。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやキーワードなどのテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・整形するロジックを含むスクリプトです。
- **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージや文言を管理するための設定ファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（文字列フォーマットなど）を処理するロジックを含むスクリプトです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、整形などのユーティリティ関数をまとめたスクリプトです。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能のテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
- **`tests/conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義するファイルです。
- **`tests/test_badge_generator_integration.py`**: `badge_generator` 機能の統合テストを行うスクリプトです。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストを行うスクリプトです。
- **`tests/test_config.py`**: 設定ファイルの読み込み・管理機能のテストを行うスクリプトです。
- **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストを行うスクリプトです。
- **`tests/test_environment.py`**: テスト環境のセットアップや依存関係の確認に関するテストを行うスクリプトです。
- **`tests/test_integration.py`**: プロジェクトの主要コンポーネント間の統合テストを行うスクリプトです。
- **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを行うスクリプトです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher` 機能のテストを行うスクリプトです。
- **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを行うスクリプトです。
- **`tests/test_repository_processor.py`**: リポジトリ処理機能のテストを行うスクリプトです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main()`**: プロジェクト全体の実行エントリポイント。GitHub APIからリポジトリ情報を取得し、各リポジトリの処理、Markdownコンテンツの生成、そして結果のファイル出力までの一連のワークフローを調整します。
        - 役割: プログラムの起動、コマンドライン引数の解析、主要な処理フローのオーケストレーション。
        - 想定される引数: `--username` (str), `--output` (str), `--limit` (int) など、コマンドラインで指定される各種オプション。
        - 想定される戻り値: なし（直接ファイルに結果を出力するため）。
- **`src/generate_repo_list/repository_processor.py`**:
    - **`process_repository(repo_raw_data, config)`**: GitHub APIから取得した個々の生のリポジトリデータを受け取り、表示に必要な情報（説明、言語、最終更新日など）を抽出し、整形された辞書形式のデータとして返します。
        - 役割: 生のAPIレスポンスデータを扱いやすい形式に変換し、後続の処理で利用できるように準備します。
        - 想定される引数: `repo_raw_data` (dict): GitHub APIからのリポジトリデータ, `config` (dict): プロジェクトの設定情報。
        - 想定される戻り値: `dict`: 処理済みリポジトリデータ。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(username, repo_name, config)`**: 指定されたリポジトリの `generated-docs/project-overview.md` ファイルから「プロジェクト概要」セクションの3行説明を抽出し、リスト形式で返します。APIリクエストのタイムアウトやリトライも管理します。
        - 役割: 各リポジトリ固有の概要情報をリモートファイルから取得し、解析します。
        - 想定される引数: `username` (str): GitHubユーザー名, `repo_name` (str): リポジトリ名, `config` (dict): `project_overview` 機能の設定。
        - 想定される戻り値: `list` of `str` (抽出された概要の各行) または `None`。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **`generate_markdown(repos_data, seo_data)`**: 処理された複数のリポジトリデータとSEO情報を基に、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。タイトル、各リポジトリの詳細、SEOメタデータなどを組み込みます。
        - 役割: 全リポジトリの情報を統合し、出力フォーマット（Markdown）に沿って整形します。
        - 想定される引数: `repos_data` (list of dict): 処理済みリポジトリデータのリスト, `seo_data` (dict): SEO関連データ。
        - 想定される戻り値: `str` (生成された全Markdownコンテンツ)。
- **`src/generate_repo_list/badge_generator.py`**:
    - **`generate_badge(status, type)`**: リポジトリのステータス（例: アクティブ、アーカイブ）やタイプ（例: フォーク）に基づいて、表示用のバッジのマークダウン文字列を生成します。
        - 役割: リポジトリの状態を視覚的に表現するバッジを作成します。
        - 想定される引数: `status` (str): リポジトリのステータス, `type` (str): リポジトリのタイプ。
        - 想定される戻り値: `str` (生成されたバッジのMarkdown文字列)。
- **`src/generate_repo_list/config_manager.py`**:
    - **`load_config(filepath)`**: 指定されたYAMLファイルパスから設定情報を読み込み、Python辞書として返します。
        - 役割: プロジェクト全体で使用される設定値をファイルからロードし、アプリケーションで利用できるようにします。
        - 想定される引数: `filepath` (str): 設定ファイルのパス。
        - 想定される戻り値: `dict` (設定内容を格納した辞書)。
- **`src/generate_repo_list/date_formatter.py`**:
    - **`format_date(datetime_obj, format_string="%Y-%m-%d")`**: 日付時刻オブジェクトを受け取り、指定されたフォーマット文字列に従って整形された日付文字列を返します。
        - 役割: 日付情報の表示形式を標準化し、人間が読みやすい形式にします。
        - 想定される引数: `datetime_obj` (datetime.datetime): フォーマットする日付時刻オブジェクト, `format_string` (str): フォーマット文字列。
        - 想定される戻り値: `str` (整形された日付文字列)。
- **`src/generate_repo_list/language_info.py`**:
    - **`get_main_language(repo_data)`**: リポジトリの言語情報から、主要なプログラミング言語を特定して返します。
        - 役割: リポジトリの技術スタックの概要を提供します。
        - 想定される引数: `repo_data` (dict): リポジトリのデータ。
        - 想定される戻り値: `str` (主要な言語名) または `None`。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
    - **`extract_badges(readme_content)`**: リポジトリのREADMEコンテンツから、特定のパターンに合致するバッジ情報を抽出します。
        - 役割: README内に埋め込まれたステータスや技術スタックを示すバッジを解析します。
        - 想定される引数: `readme_content` (str): READMEファイルのテキストコンテンツ。
        - 想定される戻り値: `list` of `str` (抽出されたバッジのURLやマークダウン断片)。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - **`calculate_stats(repo_data)`**: リポジトリのスター数、フォーク数などの統計情報を計算し、整形された形式で提供します。
        - 役割: リポジトリの人気度や活動状況を示す数値データを準備します。
        - 想定される引数: `repo_data` (dict): リポジトリのデータ。
        - 想定される戻り値: `dict` (統計情報の辞書)。
- **`src/generate_repo_list/template_processor.py`**:
    - **`render_template(template_string, data)`**: 指定されたテンプレート文字列とデータを使用して、最終的な文字列をレンダリングします。
        - 役割: Markdown生成などで使用される動的なコンテンツを生成します。
        - 想定される引数: `template_string` (str): テンプレート文字列, `data` (dict): テンプレートに埋め込むデータ。
        - 想定される戻り値: `str` (レンダリングされた文字列)。
- **`src/generate_repo_list/url_utils.py`**:
    - **`build_repo_url(username, repo_name)`**: GitHubユーザー名とリポジトリ名から、リポジトリのURLを構築します。
        - 役割: 各種リソースへの正確なURLを生成します。
        - 想定される引数: `username` (str): GitHubユーザー名, `repo_name` (str): リポジトリ名。
        - 想定される戻り値: `str` (構築されたURL)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-09 07:24:24 JST
