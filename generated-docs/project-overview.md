Last updated: 2026-04-30

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成します。
- 検索エンジンによるクロールを促進し、開発効率向上やLLMによるリポジトリ参照精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - GitHub Pagesサイトのレンダリングに利用される静的サイトジェネレーター。出力フォーマットとしてMarkdownを採用。
- 音楽・オーディオ: なし
- 開発ツール: Python - プロジェクトの主要なスクリプト言語。GitHub API - リポジトリ情報を取得するために利用。PyYAML - YAML形式の設定ファイル (`config.yml`, `strings.yml`) の読み込みに使用。toml - シークレット設定ファイル (`secrets.toml`) の読み込みに使用。
- テスト: pytest - Pythonコードの単体テストおよび結合テストを実行するためのフレームワーク。
- ビルドツール: なし (Pythonスクリプトがコンテンツ生成の主要な役割を担います。)
- 言語機能: Python - 高度なファイルI/O、API通信、データ処理、文字列操作など、システムの中核となる機能を提供。
- 自動化・CI/CD: なし (プロジェクトはCI/CDに依存しないローカル開発重視の構成を採用しています。)
- 開発標準: Ruff - Pythonコードのフォーマットとリンティングを自動化し、コード品質と一貫性を保つためのツール。

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
- **README.md**: プロジェクトの目的、主要機能、使用方法、設定手順、ライセンスなどの全体的な情報を提供するメインドキュメント。
- **.editorconfig**: 異なるエディタやIDEを使用する開発者が、統一されたコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **.github_automation/check_large_files/**: GitHubリポジトリ内の大容量ファイルをチェックするための自動化スクリプト群。
    - **check-large-files.toml**: 大容量ファイルチェック機能の設定を定義。
    - **scripts/check_large_files.py**: 実際にリポジトリ内のファイルを走査し、設定された閾値を超える大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitバージョン管理システムが追跡しないファイルやディレクトリ（例: ログファイル、一時ファイル、仮想環境など）を指定する設定ファイル。
- **LICENSE**: プロジェクトがMITライセンスの下で公開されていることを示すファイル。
- **_config.yml**: GitHub Pagesで利用されるJekyllのサイト全体の設定ファイル。サイトのタイトル、テーマ、プラグインなどが定義される。
- **assets/**: Webサイトで使用される画像、アイコン（favicon）などの静的アセットを格納するディレクトリ。
- **debug_project_overview.py**: 各リポジトリからプロジェクト概要を自動取得する機能のデバッグを補助するためのスクリプト。
- **generated-docs/**: 各リポジトリの `project-overview.md` など、自動生成または参照されるドキュメントが配置されることを想定したディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって最終的に生成される、リポジトリ一覧を表示するメインのMarkdownファイル。GitHub Pagesのトップページとして機能する。
- **issue-notes/**: 開発中に発生した課題やその検討、対策などに関するメモを格納するディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するファイル。Webサイトをネイティブアプリのようにインストール可能にするための情報（アプリ名、アイコン、表示モードなど）を含む。
- **pytest.ini**: `pytest` テストフレームワークの動作をカスタマイズするための設定ファイル。テストの発見ルール、プラグイン、マーカーなどを定義。
- **requirements-dev.txt**: 開発時およびテスト時にのみ必要となるPythonパッケージの依存関係を記述したファイル（例: `pytest`, `ruff`）。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイル。
- **ruff.toml**: Pythonの高速リンターおよびフォーマッターである`ruff`の設定ファイル。コーディング規約や自動修正ルールを定義。
- **src/generate_repo_list/**: リポジトリ一覧自動生成システムの主要なロジックを格納するPythonパッケージ。
    - **badge_generator.py**: リポジトリのステータス（例: アーカイブ済み）や言語に応じたバッジの画像URLを生成するロジックを実装。
    - **config.yml**: リポジトリ概要の取得方法や各種API設定など、プロジェクトの動作を制御するパラメータを定義するYAML形式の設定ファイル。
    - **config_manager.py**: `config.yml` やシークレットファイル (`secrets.toml`) など、各種設定ファイルを読み込み、管理するユーティリティモジュール。
    - **date_formatter.py**: GitHub APIから取得した日付情報を、ユーザーフレンドリーな形式に整形するためのユーティリティ関数を提供。
    - **generate_repo_list.py**: プロジェクトのメインエントリーポイントとなるスクリプト。GitHub APIからのリポジトリ情報取得、処理、Markdown生成までの一連のフローを統括。
    - **json_ld_template.json**: 検索エンジン最適化 (SEO) のため、リポジトリ情報を構造化データとして埋め込むJSON-LDのテンプレート。
    - **language_info.py**: リポジトリが使用しているプログラミング言語に関する情報を処理し、表示に適した形に加工するモジュール。
    - **markdown_generator.py**: 処理されたリポジトリデータに基づいて、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を抽出・取得するモジュール。
    - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を解析・抽出するモジュール。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、フィルタリング、分類、必要な情報の抽出といった前処理を行うモジュール。
    - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイル。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算し、レポートするモジュール。
    - **strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキストコンテンツを国際化（i18n）や一元管理するためのYAMLファイル。
    - **template_processor.py**: Markdown生成時に使用されるテンプレートファイルを読み込み、動的なデータで埋め込む処理を行うモジュール。
    - **url_utils.py**: URLの検証、構築、パースなど、URL関連の汎用的なユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールに実装されたプロジェクト概要取得機能の単体テストを記述したファイル。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: `pytest` テストフレームワークで共有されるフィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: `badge_generator.py` モジュールの統合テスト。
    - **test_check_large_files.py**: `check_large_files.py` スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理機能のテスト。
    - **test_date_formatter.py**: 日付整形ユーティリティのテスト。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテスト。
    - **test_integration.py**: システム全体または主要コンポーネント間の連携を検証する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator.py` モジュールのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py` モジュールのテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor.py` モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor.py` モジュールのテスト。

## 関数詳細説明
提供されたプロジェクト情報およびファイル詳細分析からは、具体的な関数のシグネチャ、引数、戻り値、詳細な機能を特定することはできません。しかし、プロジェクトの構造から、以下の主要なモジュールにはそれぞれ目的の機能を果たす関数が含まれていると推測されます。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main()`**: プロジェクト全体の実行を管理するメイン関数。GitHub APIからのリポジトリ取得、データ処理、Markdown生成といった一連の処理をオーケストレーションします。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_name, owner_name, config)`**: 指定されたリポジトリから、`generated-docs/project-overview.md` ファイルを読み込み、設定に基づき3行のプロジェクト概要を抽出して返します。API呼び出しやファイル内容の解析ロジックを含みます。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **`generate_repo_list_markdown(repositories_data, config, strings)`**: 処理されたリポジトリデータのリストを受け取り、GitHub Pages向けの整形されたMarkdownコンテンツ全体を生成します。各リポジトリのエントリをループ処理し、テンプレートに沿って出力します。
    - **`_format_repository_entry(repo_data, strings)`**: 個々のリポジトリデータを受け取り、そのリポジトリのMarkdown表示形式（タイトル、説明、バッジ、リンクなど）を生成する内部関数。
- **`src/generate_repo_list/repository_processor.py`**:
    - **`process_repository_data(github_api_data, config)`**: GitHub APIから取得した生のリポジトリデータを受け取り、フィルタリング（例: フォークの除外）、分類（例: アクティブ、アーカイブ）、必要な情報の抽出と整形を行います。
- **`src/generate_repo_list/badge_generator.py`**:
    - **`get_badge_url(status_type, language=None)`**: リポジトリのステータス（アーカイブ、フォークなど）や使用言語に基づいて、適切なバッジの画像URLを生成して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-30 07:23:36 JST
