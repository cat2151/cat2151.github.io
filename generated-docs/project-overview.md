Last updated: 2026-05-20

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、GitHub Pages向けリポジトリ一覧Markdownを自動生成するシステムです。
- 検索エンジンにクロールされにくいGitHubユーザーページの問題を解決し、SEOを最適化します。
- 各リポジトリの概要を自動抽出し、LLMによる参照失敗の緩和にも貢献します。

## 技術スタック
- フロントエンド: **GitHub Pages** (Jekyllベースの静的サイトホスティングプラットフォーム。本システムが生成したMarkdownを元に最終的なWebサイトを構築します。)、**Markdown** (本システムが生成する主要な出力フォーマットで、JekyllによってHTMLに変換されます。)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要な開発言語および実行環境。GitHub APIとの連携、ファイルの生成ロジックを実装しています。)、**GitHub API** (リポジトリ情報の取得元となるAPI。ユーザーのリポジトリデータや各リポジトリのファイル内容にアクセスします。)、**Git** (バージョン管理システム。リポジトリのクローンやファイルアクセスに使用されます。)
- テスト: **pytest** (Python製のテストフレームワーク。プロジェクトの各モジュールの単体テストや統合テストを実行し、品質を保証します。)
- ビルドツール: **Jekyll** (静的サイトジェネレーター。本システムが生成したMarkdownファイルとテンプレートを組み合わせて、最終的なHTMLサイトをビルドします。)
- 言語機能: **Python** (プロジェクト全体のロジックを記述するために使用されています。)、**YAML** (設定ファイルやテンプレートファイルの記述に使用されます。)、**TOML** (Secretsファイルやコードスタイル設定ファイルに使用されます。)、**JSON** (構造化データテンプレートに使用されます。)
- 自動化・CI/CD: **GitHub Pages** (生成されたサイトコンテンツを自動的にデプロイ・公開するプラットフォームとして利用されます。)、**GitHub Actions** (`.github_automation` ディレクトリが存在し、大規模ファイルチェックなどの自動化処理が想定されます。)
- 開発標準: **Ruff** (Pythonの高速なリンター兼フォーマッター。コードスタイルの一貫性を保ち、品質を向上させるために使用されます。)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。インデントのサイズや文字コードなどを定義します。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するファイル群。
        - **README.md**: `check_large_files` 機能の説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイルの検出ルールや閾値などを設定するTOMLファイル。
        - **scripts/**: 実際のチェック処理を行うスクリプトを格納。
            - **check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。一時ファイル、ログ、環境固有の設定などが含まれます。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイル。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、使用方法、開発者向けのヒントなどを記述したメインドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定ファイル。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
- **assets/**: Webサイトで使用される画像、ファビコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: さまざまなサイズで表示されるサイトのファビコン画像。
- **debug_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher.py`）の動作をデバッグするための補助スクリプト。
- **generated-docs/**: 他のリポジトリから自動取得されたドキュメント（例: `project-overview.md`）が一時的に格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのWebマスターツールによるサイト所有権確認のために配置されるファイル。
- **index.md**: `generate_repo_list.py` によって生成される、GitHub Pagesサイトのリポジトリ一覧を含むメインのMarkdownファイル。
- **issue-notes/**: 開発中の課題や調査結果、アイデアなどをメモとして記録するディレクトリ。
    - **22.md**: 特定の課題（Issue #22など）に関する詳細なノートや検討事項が記述されたMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるWebアプリマニフェストファイル。ホーム画面アイコンや表示モードなどを定義します。
- **pytest.ini**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの実行オプション、プラグイン、マーカーなどを定義します。
- **requirements-dev.txt**: 開発時およびテスト時にのみ必要なPythonライブラリの依存関係をリストアップしたファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonライブラリの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはクロールすべきでないかを指示するファイル。
- **ruff.toml**: Pythonのリンター/フォーマッター `Ruff` の設定ファイル。コードスタイルルール、エラー検出規則などを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージとして認識させるためのファイル。
    - **generate_repo_list/**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージ。
        - **__init__.py**: `generate_repo_list` パッケージとして認識させるためのファイル。
        - **badge_generator.py**: リポジトリの各種バッジ（例: スター数、言語など）をMarkdown形式で生成するロジックを実装。
        - **config.yml**: `generate_repo_list` パッケージ固有の設定（例: プロジェクト概要機能の有効/無効、ターゲットファイル名、キャッシュ設定など）を定義するYAMLファイル。
        - **config_manager.py**: `config.yml` や `strings.yml` など、プロジェクトの設定ファイルを読み込み、管理するためのモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付情報を、表示に適した形式にフォーマットするためのユーティリティ関数を提供。
        - **generate_repo_list.py**: **このプロジェクトのメインスクリプト。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、情報の整形、Markdown生成、ファイル出力までの一連の流れを統括します。**
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリの使用言語情報を処理し、表示可能な形式に変換するロジックを実装。
        - **markdown_generator.py**: 取得・整形されたリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックを実装。
        - **project_overview_fetcher.py**: 他のリポジトリに存在する `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を自動的に取得・抽出する機能を提供。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報（例: 状態バッジ）を抽出するロジック。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報のフィルタリング、整形、追加処理（例: 概要の取得、統計計算）を行うモジュール。
        - **seo_template.yml**: サイトのSEOメタデータやページタイトルなどのテンプレートを定義するYAMLファイル。
        - **statistics_calculator.py**: 各リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジックを実装。
        - **strings.yml**: UIに表示される各種メッセージ、ラベル、文言などを管理するYAMLファイル。多言語対応や文言変更を容易にします。
        - **template_processor.py**: MarkdownやJSON-LDのテンプレートを読み込み、リポジトリデータを適用して最終的な文字列を生成する汎用的なテンプレート処理モジュール。
        - **url_utils.py**: URLの生成、検証、エンコードなどのユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（特にプロジェクト概要の自動取得）に対するテストスクリプト。
- **tests/**: pytestによるテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャ、フック、補助関数などを定義し、複数のテストファイルで共有するための設定ファイル。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **test_check_large_files.py**: `_github_automation/check_large_files.py` の機能に対するテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理を行う `config_manager.py` の機能に対するテスト。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテスト。
    - **test_environment.py**: テスト実行環境や依存関係の整合性を確認するためのテスト。
    - **test_integration.py**: プロジェクト全体の主要なフロー（リポジトリ取得からMarkdown生成まで）の統合テスト。
    - **test_markdown_generator.py**: Markdown生成ロジックのテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリ情報処理ロジックのテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、メインの処理は `src/generate_repo_list/generate_repo_list.py` が担っています。以下に主要な関数とその役割を説明します。

-   **`src/generate_repo_list/generate_repo_list.py` 内の主要な関数:**
    -   **`main()`**:
        -   **役割**: プログラムのエントリポイント。コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ情報取得、リポジトリデータの処理、Markdownコンテンツの生成、そして最終的なファイルの出力までの一連のワークフローをオーケストレーションします。
        -   **引数**: なし (通常はコマンドライン引数として渡されるものを内部で解析)
        -   **戻り値**: なし
        -   **機能**: 引数パーサーの設定、ConfigManagerからの設定ロード、GitHub APIクライアントの初期化、RepositoryProcessorによるデータ整形、MarkdownGeneratorによるコンテンツ生成、最終ファイルへの書き込みなど。

-   **`src/generate_repo_list/config_manager.py` 内の主要な関数:**
    -   **`load_config(config_path, strings_path)`**:
        -   **役割**: 指定されたパスからYAML形式の設定ファイル (`config.yml` と `strings.yml`) を読み込み、設定オブジェクトとして提供します。
        -   **引数**:
            -   `config_path` (str): メインの設定ファイル (`config.yml`) へのパス。
            -   `strings_path` (str): 表示用文字列ファイル (`strings.yml`) へのパス。
        -   **戻り値**: dict (読み込まれた設定と文字列データを結合した辞書)
        -   **機能**: YAMLファイルをパースし、設定値をプログラム全体で利用できるようにします。

-   **`src/generate_repo_list/repository_processor.py` 内の主要な関数:**
    -   **`process_repositories(username, github_client, config, limit=None)`**:
        -   **役割**: GitHub APIから取得したユーザーのリポジトリリストを受け取り、各リポジトリに対して必要な追加情報（例: プロジェクト概要、バッジ情報、言語、統計）を付加し、最終的な表示用データ構造に整形します。
        -   **引数**:
            -   `username` (str): GitHubユーザー名。
            -   `github_client` (object): GitHub APIクライアントのインスタンス。
            -   `config` (dict): プロジェクト設定。
            -   `limit` (int, optional): 処理するリポジトリ数の上限（デバッグ用）。
        -   **戻り値**: list (整形されたリポジトリ情報のリスト)
        -   **機能**: `project_overview_fetcher` を使って概要を取得したり、`badge_generator` や `language_info` などの他のモジュールと連携して情報を追加します。

-   **`src/generate_repo_list/project_overview_fetcher.py` 内の主要な関数:**
    -   **`fetch_project_overview(github_client, repo_owner, repo_name, config)`**:
        -   **役割**: 特定のリポジトリの `generated-docs/project-overview.md` ファイルの内容をGitHub API経由で取得し、設定されたセクションタイトルに基づいて3行のプロジェクト概要を抽出します。
        -   **引数**:
            -   `github_client` (object): GitHub APIクライアントのインスタンス。
            -   `repo_owner` (str): リポジトリの所有者名。
            -   `repo_name` (str): リポジトリ名。
            -   `config` (dict): プロジェクト設定（概要取得機能の有効/無効、ターゲットファイル名、セクションタイトルなど）。
        -   **戻り値**: list (抽出された3行の概要テキストのリスト、または空のリスト)
        -   **機能**: ファイル内容のダウンロード、Markdownパーサーによるセクション抽出、キャッシュ処理などを実行します。

-   **`src/generate_repo_list/markdown_generator.py` 内の主要な関数:**
    -   **`generate_markdown(repositories_data, config, strings)`**:
        -   **役割**: 整形されたリポジトリ情報と設定データ、表示文字列を元に、GitHub Pagesサイト用の最終的なMarkdownコンテンツを生成します。
        -   **引数**:
            -   `repositories_data` (list): `repository_processor` から受け取った整形済みリポジトリ情報のリスト。
            -   `config` (dict): プロジェクト設定。
            -   `strings` (dict): 表示用文字列データ。
        -   **戻り値**: str (生成されたMarkdown文字列)
        -   **機能**: テンプレートエンジン (`template_processor`) を使用して、リポジトリごとのセクションや全体構成を組み合わせてMarkdownを構築します。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── parse_arguments()                                         // コマンドライン引数を解析
├── ConfigManager.load_config(config_path, strings_path)      // 設定ファイルを読み込む
├── GitHubAPIClient.__init__()                                // GitHub APIクライアントを初期化
├── RepositoryProcessor.process_repositories(username, github_client, config, limit)
│   ├── GitHubAPIClient.get_user_repos(username)              // 指定ユーザーのリポジトリリストを取得
│   ├── for each repository:
│   │   ├── ProjectOverviewFetcher.fetch_project_overview(github_client, repo_owner, repo_name, config) // リポジトリ概要を取得
│   │   │   ├── GitHubAPIClient.get_repo_file_content(repo_owner, repo_name, file_path) // 概要ファイル内容を取得
│   │   │   └── parse_markdown_for_overview()                 // Markdownから概要テキストを抽出
│   │   ├── ReadmeBadgeExtractor.extract_badges(readme_content) // READMEからバッジ情報を抽出 (必要に応じて)
│   │   ├── BadgeGenerator.generate_badge_markdown(badges_data) // バッジのMarkdownを生成
│   │   ├── LanguageInfo.get_language_data(repo_languages_url) // リポジトリの言語情報を取得 (必要に応じて)
│   │   └── StatisticsCalculator.calculate_stats(repo_data)   // スター数などの統計情報を計算
├── MarkdownGenerator.generate_markdown(repositories_data, config, strings) // Markdownコンテンツを生成
│   ├── TemplateProcessor.render_template(template_name, context) // 指定されたテンプレートをレンダリング
│   └── UrlUtils.create_url(base_url, path_segments)          // URLを構築
└── write_output_file(output_path, markdown_content)          // 生成されたMarkdownをファイルに書き出す

---
Generated at: 2026-05-20 07:31:06 JST
