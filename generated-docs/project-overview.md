Last updated: 2026-11-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成します。
- GitHubユーザーページのリポジトリが検索エンジンにクロールされにくい問題を解決し、LLMによる参照失敗も緩和します。
- SEO最適化されたリポジトリ一覧、各リポジトリの概要表示、アクティブ/アーカイブ/フォークによる分類機能を提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータ), **Markdown** (コンテンツ記述言語), **GitHub Pages** (静的サイトホスティングサービス)
- 音楽・オーディオ: 該当なし
- 開発ツール: **GitHub API** (リポジトリ情報取得), **Python** (スクリプト実行環境), **pytest** (テストフレームワーク), **ruff** (Pythonリンター/フォーマッター)
- テスト: **pytest** (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: **Python** (スクリプト言語としてコンテンツ生成を実行), **YAML** (設定ファイルのパース)
- 言語機能: **Python** (コマンドライン引数パーシング、ファイルI/O、HTTPリクエストなど一般的なスクリプト機能)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリにより、リポジトリの特定の自動化タスクが示唆されますが、本プロジェクト自体はCI/CDツールではありません), **_config.yml**, **robots.txt**, **manifest.json** (Jekyll/GitHub Pagesのサイト設定や最適化関連ファイル)
- 開発標準: **ruff** (コードスタイル自動修正・チェック), **.editorconfig** (エディタのコードスタイル統一設定)

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
- **.editorconfig**: 複数の開発者が異なるエディタを使用しても、インデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプト群を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルがないかをチェックする自動化スクリプト群。
        - **README.md**: `check_large_files`スクリプトの説明。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルチェックを実行するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **README.md**: プロジェクトの概要、目的、主な機能、使い方などを説明するメインのドキュメントファイルです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **assets/**: サイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
- **debug_project_overview.py**: `project_overview`機能のデバッグ用途で使用される補助スクリプトです。
- **generated-docs/**: プロジェクト概要取得機能によって、各リポジトリから取得されたドキュメントや、生成されるMarkdownファイルが一時的に格納される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認で使用される認証ファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧のメインのMarkdownファイルです。Jekyllサイトのトップページとして表示されます。
- **issue-notes/**: 開発中に発生した課題やそのメモを記録するディレクトリです。
    - **22.md**: 特定の課題（Issue #22など）に関する詳細なメモや議論が記述されたMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、ウェブアプリのマニフェストファイルです。ホーム画面への追加、アプリのテーマカラーなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法や検出ルールなどを定義します。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要なPythonパッケージを列挙したファイルです。
- **requirements.txt**: 本番環境でこのスクリプトを実行するために必要なPythonパッケージを列挙したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonのリンター兼フォーマッターであるruffの設定ファイルです。コードのスタイルや品質に関するルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成の主要なロジックを格納するパッケージです。
        - **__init__.py**: Pythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（例：Python, JavaScriptなど）を生成するロジックを提供します。
        - **config.yml**: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイルです。
        - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するモジュールです。
        - **date_formatter.py**: GitHub APIから取得した日付データを整形して表示するためのロジックを提供します。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        - **json_ld_template.json**: SEOを目的としたJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: リポジトリの使用言語情報を処理し、表示に役立つ形式に変換するモジュールです。
        - **markdown_generator.py**: 取得したリポジトリ情報や統計データに基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックを提供します。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要を自動取得するロジックを担います。
        - **readme_badge_extractor.py**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例：CI/CDステータス、ライセンスなど）を抽出し解析するロジックを提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報を抽出し、整形する主要なモジュールです。
        - **seo_template.yml**: SEO関連のメタデータや構造化データのテンプレート設定を定義します。
        - **statistics_calculator.py**: リポジトリ群に関する統計情報（例：言語の割合、更新頻度など）を計算するモジュールです。
        - **strings.yml**: UIに表示されるメッセージや文言を管理する設定ファイルです。多言語対応や文言の一元管理に利用されます。
        - **template_processor.py**: Markdown生成時に特定のテンプレート（JekyllのLiquidタグなど）を処理し、最終的な出力形式を整えるモジュールです。
        - **url_utils.py**: GitHubリポジトリへのURLやGitHub PagesサイトへのURLなど、各種URLの生成と管理を行うユーティリティモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`機能の単体テストを記述したファイルです。
- **tests/**: プロジェクトの自動テストコードを格納するディレクトリです。
    - **conftest.py**: pytestのテスト実行時に使用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの結合テストを記述したファイルです。
    - **test_check_large_files.py**: `.github_automation/check_large_files`スクリプトのテストを記述したファイルです。
    - **test_config.py**: `config_manager`モジュールや設定ファイルの読み込みに関するテストを記述したファイルです。
    - **test_date_formatter.py**: `date_formatter`モジュールのテストを記述したファイルです。
    - **test_environment.py**: テスト実行環境に関する設定や依存関係のテストを記述したファイルです。
    - **test_integration.py**: プロジェクト全体の主要な機能に関する結合テストを記述したファイルです。
    - **test_markdown_generator.py**: `markdown_generator`モジュールのテストを記述したファイルです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールの詳細なテストを記述したファイルです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのテストを記述したファイルです。
    - **test_repository_processor.py**: `repository_processor`モジュールのテストを記述したファイルです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルが特定の機能を担当するモジュールとして設計されています。具体的な関数名や引数、戻り値の詳細は提供されていませんが、各モジュールの役割に基づいて主要な関数の役割を説明します。

- **generate_repo_list.py**:
    - `main()`: スクリプトのエントリポイント。コマンドライン引数の解析、設定の読み込み、リポジトリデータの取得と処理、Markdown生成、ファイル出力までの一連のフローを制御します。
    - `parse_arguments()`: コマンドライン引数（例: `--username`, `--output`, `--limit`）を解析し、スクリプト実行に必要なパラメータを取得します。
    - `generate_list(username, output_file, limit)`: 指定されたユーザー名のリポジトリ一覧を生成し、指定されたファイルに出力する主要なロジックをカプセル化します。
- **config_manager.py**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    - `get_setting(key_path, default=None)`: 設定ファイルから特定のキーパスに存在する設定値を取得します。
- **repository_processor.py**:
    - `fetch_repositories(username, github_token)`: GitHub APIを使用して、指定されたユーザーのリポジトリ情報を取得します。
    - `process_repository_data(repo_data, config, strings_data)`: 取得したリポジトリの生データを整形し、Markdown生成に適した形式に変換します。この中で、プロジェクト概要の取得やバッジの抽出、言語情報の処理などを呼び出します。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_name, owner, target_file, section_title, config)`: 指定されたリポジトリの特定ファイルから「プロジェクト概要」セクションの3行説明を抽出し、返します。
- **markdown_generator.py**:
    - `generate_markdown(processed_repos, config, strings_data, seo_data)`: 処理済みのリポジトリデータ、設定、文言データ、SEOデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- **badge_generator.py**:
    - `generate_badge_markdown(badge_type, value)`: 特定のバッジタイプと値に基づいて、Markdown形式のバッジ文字列を生成します。
- **date_formatter.py**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を、人間が読みやすい形式に整形します。
- **template_processor.py**:
    - `apply_template(content, data)`: Liquid構文などを含むテンプレート文字列にデータを適用し、レンダリングされたコンテンツを返します。
- **url_utils.py**:
    - `build_github_repo_url(owner, repo_name)`: GitHubリポジトリへのURLを構築します。
    - `build_github_pages_url(owner, repo_name)`: そのリポジトリに対応するGitHub PagesサイトへのURLを構築します。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── parse_arguments()
├── config_manager.load_config(config.yml)
├── config_manager.load_config(strings.yml)
├── repository_processor.fetch_repositories(username, github_token)
│   └── (GitHub API呼び出し)
└── generate_list(username, output_file, limit)
    ├── repository_processor.process_repository_data()
    │   ├── project_overview_fetcher.fetch_project_overview()
    │   │   └── (GitHub API呼び出し for specific file)
    │   ├── readme_badge_extractor.extract_badges()
    │   └── language_info.get_language_language_details()
    ├── statistics_calculator.calculate_statistics()
    ├── markdown_generator.generate_markdown()
    │   ├── template_processor.apply_template()
    │   ├── badge_generator.generate_badge_markdown()
    │   ├── date_formatter.format_date()
    │   └── url_utils.build_github_pages_url()
    └── (ファイル出力: output_file)

---
Generated at: 2026-11-18 07:07:38 JST
