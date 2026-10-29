Last updated: 2026-10-30

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・整理するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧Markdownを自動生成します。
- これにより、GitHub Pagesの検索エンジンによるクロールを促進し、リポジトリの可視性とLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として利用され、生成されたMarkdownファイルをレンダリング), **Markdown** (リポジトリ一覧の出力形式), **GitHub Pages** (生成されたコンテンツを公開するプラットフォーム), **HTML/JSON-LD** (SEO最適化のために生成される構造化データやWeb App Manifestの基盤)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なスクリプト言語としてリポジトリ情報の取得・加工・Markdown生成を担う), **pytest** (テストフレームワーク), **ruff** (コードスタイルリンター・フォーマッター), **YAML** (設定ファイル `config.yml`, `strings.yml`, `seo_template.yml` の記述に使用), **TOML** (pytest設定 `pytest.ini`, コードスタイル設定 `ruff.toml`, 秘密情報 `secrets.toml` の記述に使用)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストに使用されるフレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報の取得からMarkdownファイル生成までの一連の処理を自動で行うため、実質的なビルド・生成ツールとして機能します)
- 言語機能: **Python** (GitHub APIとの連携、データ処理、ファイルI/Oなど、プロジェクトの全般的なロジックを実装)
- 自動化・CI/CD: **Pythonスクリプト** (リポジトリ情報の取得とMarkdown生成自体が自動化されたプロセス。`.github_automation` ディレクトリには、潜在的にCI/CDパイプラインの一部として利用される可能性のある補助スクリプトが含まれます)
- 開発標準: **ruff** (Pythonコードの品質と一貫性を保つためのリンティングおよびフォーマットツール), **.editorconfig** (異なるエディタ間でのコーディングスタイルの一貫性を保つための設定ファイル)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルを検出するためのスクリプト群。
        - **README.md**: `check_large_files`機能に関する説明。
        - **check-large-files.toml**: `check_large_files`スクリプトの設定ファイル。
        - **scripts/check_large_files.py**: 指定された閾値を超える大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitによってバージョン管理されるべきではないファイルやディレクトリを指定するファイル。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）。
- **README.md**: プロジェクトの目的、機能、使用方法、開発者向けのヒントなどが記述されたメインドキュメント。
- **_config.yml**: Jekyllサイトのグローバルな設定ファイル。GitHub Pagesの振る舞いを制御します。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザタブなどに表示されるアイコン）ファイル群。
- **debug_project_overview.py**: `project_overview`機能のデバッグ目的で使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得される `project-overview.md` などが格納されることが想定されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイル。
- **issue-notes/**: 開発中の課題やメモを記録するためのディレクトリ。
    - **22.md**: 特定の課題に関するメモ。
- **manifest.json**: Web App Manifest。プログレッシブウェブアプリ（PWA）のインストール情報などを定義します。
- **pytest.ini**: `pytest`フレームワークの挙動を設定するファイル。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を定義するファイル。
- **requirements.txt**: プロジェクトが本番稼働するために必要なPythonパッケージの依存関係を定義するファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか/しないかを指示するファイル。
- **ruff.toml**: `ruff`リンター・フォーマッターのルール設定ファイル。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成機能に関連するモジュール群。
        - **__init__.py**: Pythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのバッジ（例: 言語バッジ、ステータスバッジ）のMarkdownを生成するロジックを実装。
        - **config.yml**: プロジェクト概要取得機能など、主要な機能の技術的パラメータを設定するYAMLファイル。
        - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するユーティリティ。
        - **date_formatter.py**: 日付や時刻のフォーマット処理を提供するモジュール。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、最終的なリポジトリ一覧のMarkdownファイルを生成するメインスクリプト。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するモジュール。
        - **markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要を抽出し、取得する機能。
        - **readme_badge_extractor.py**: リポジトリの `README.md` から特定のバッジ情報を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを加工、整形し、表示に適した形に準備するモジュール。
        - **seo_template.yml**: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュール。
        - **strings.yml**: UIメッセージ、文言、キャプションなどを一元的に管理する多言語対応可能なYAMLファイル。
        - **template_processor.py**: Markdown生成時に使用されるテンプレートを処理する汎用モジュール。
        - **url_utils.py**: URLの生成、解析、検証などのユーティリティ関数。
- **test_project_overview.py**: `project_overview`機能のテストケースを記述したスクリプト。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのテストフィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: `badge_generator`の統合テスト。
    - **test_check_large_files.py**: `check_large_files.py`スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込み・管理に関するテスト。
    - **test_date_formatter.py**: 日付フォーマット機能のテスト。
    - **test_environment.py**: 実行環境に関するテスト。
    - **test_integration.py**: 主要な機能間の統合テスト。
    - **test_markdown_generator.py**: Markdown生成ロジックのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリデータ処理ロジックのテスト。

## 関数詳細説明
提供されたプロジェクト情報から、特定の関数の引数や戻り値の詳細な情報は特定できませんでしたが、主要なファイルにおける中心的な関数の役割を以下に説明します。

- **`generate_repo_list.py`内の主要関数**:
    - `main()`: このスクリプトのエントリポイント。コマンドライン引数の解析、GitHubトークンの読み込み、リポジトリ情報の取得、加工、Markdown生成、ファイル出力までの一連の処理を統括します。
    - `_parse_arguments()`: コマンドラインから渡されるユーザー名、出力ファイル名、リポジトリ数制限などの引数を解析し、利用可能な形式に変換します。
    - `_get_github_repos(username, limit)`: 指定されたGitHubユーザー名に基づき、GitHub APIからリポジトリの一覧を取得します。`limit`オプションが指定されている場合は、その数に処理を制限します。
    - `_generate_markdown_output(processed_repos)`: 処理済みのリポジトリ情報から、GitHub Pages向けのリポジトリ一覧Markdownコンテンツを生成します。
    - `_write_output(output_file_path, content)`: 生成されたMarkdownコンテンツを指定されたファイルパスに書き込みます。

- **`project_overview_fetcher.py`内の主要関数**:
    - `fetch_project_overview(repo_name, owner_name, config)`: 指定されたリポジトリ名と所有者名に基づき、そのリポジトリ内の`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出し、取得します。`config`オブジェクトから設定（ファイル名、セクションタイトルなど）を参照します。

- **`markdown_generator.py`内の主要関数**:
    - `generate_repository_list_markdown(repos_data, config)`: 複数のリポジトリデータを受け取り、それら全てをまとめたリポジトリ一覧のMarkdown文字列を生成します。設定(`config`)に応じて、バッジや概要を含めます。
    - `generate_repo_details_markdown(repo_info)`: 個々のリポジトリの詳細情報を受け取り、そのリポジトリに特化したMarkdownスニペットを生成します。

- **`repository_processor.py`内の主要関数**:
    - `process_repository_data(raw_repo_data, config)`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式（言語情報、スター数、最終更新日など）に整形・加工します。`project_overview_fetcher`を呼び出して概要を取得する処理も含まれます。

- **`badge_generator.py`内の主要関数**:
    - `generate_badge_markdown(badge_type, value)`: 指定されたバッジタイプ（例: 言語、ステータス）と値に基づいて、対応するMarkdown形式のバッジ文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-30 07:09:04 JST
