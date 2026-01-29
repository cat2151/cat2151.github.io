Last updated: 2026-01-30

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成し、WebサイトのSEO（検索エンジン最適化）を強化します。
- GitHub APIを活用してリポジトリ情報を取得し、Jekyllに対応したマークダウンファイルを出力します。
- 各リポジトリの概要を自動取得し表示することで、検索エンジンやLLMからの参照性向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 生成されたMarkdownファイルをHTMLに変換し、Webサイトとして公開するための静的サイトジェネレータです。
- 音楽・オーディオ: 該当なし
- 開発ツール: Ruff - Pythonコードのフォーマットとリンティングを自動化し、コード品質と統一性を保つためのツールです。
- テスト: Pytest - Pythonアプリケーションの単体テスト、結合テスト、および機能テストを効率的に実行するためのフレームワークです。
- ビルドツール: Python - プロジェクトの主要な処理ロジックを実装しており、リポジトリ情報の取得からMarkdownファイルの生成までの一連のプロセスを実行します。
- 言語機能:
    - Python: プロジェクトの主要開発言語です。
    - YAML: 設定ファイル（`config.yml`, `strings.yml` など）やテンプレートの記述に使用される人間が読みやすいデータシリアライゼーション言語です。
    - Markdown: GitHub Pagesのコンテンツとして生成される、軽量なマークアップ言語です。
    - JSON: SEOメタデータ（`json_ld_template.json`）やAPIレスポンスのデータ形式として使用されます。
- 自動化・CI/CD: 本プロジェクト自体はCI/CDツールを直接利用していませんが、Pythonスクリプトによるリポジトリ一覧の自動生成という形でタスク自動化を実現しています。
- 開発標準: Ruff - コードスタイルの一貫性を保つためのツールです。

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
- **.editorconfig**: 複数の開発者間でコードのフォーマットスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（ビルド生成物、ログファイルなど）を指定するファイルです。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行方法、利用可能なオプション、ライセンスなどの包括的な情報を提供するメインドキュメントです。
- **_config.yml**: Jekyll静的サイトジェネレータのためのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
- **assets/**: Webサイトで使用される静的リソース（画像、ファビコンなど）を格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webブラウザのタブやブックマークなどに表示されるサイトアイコンの、異なるサイズバリエーションです。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグやテスト実行を目的としたスクリプトです。
- **generated-docs/**: 他のリポジトリから自動的に取得された `project-overview.md` ファイルなどのドキュメントを一時的に格納する、またはその役割を想定したディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなど、Webサイトの所有権確認のために配置される認証ファイルです。
- **index.md**: 生成スクリプトの出力先となるファイルで、GitHub Pagesサイトのメインページとして表示されるリポジトリ一覧のMarkdownコンテンツを含みます。
- **issue-notes/**: 開発中に発生した課題、検討事項、メモなどを記録したMarkdownファイルを格納するディレクトリです。
- **manifest.json**: プログレッシブWebアプリ（PWA）のWebマニフェストファイルで、アプリの表示設定、ホーム画面への追加機能などを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。テスト検出ルール、プラグイン、マークなどを指定します。
- **requirements-dev.txt**: 開発時およびテスト実行時にのみ必要なPythonパッケージとその依存関係をリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に不可欠なPythonパッケージとその依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンのWebクローラーに対して、サイト内でクロールを許可または禁止するパスを指定するファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        - **__init__.py**: Pythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリの言語やステータス（アーカイブなど）を示すバッジを生成するロジックを提供します。
        - **config.yml**: リポジトリ情報の取得方法やプロジェクト概要機能の有効/無効、対象ファイルパスなどの技術的パラメータを設定するファイルです。
        - **config_manager.py**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、プロジェクト全体で設定値にアクセスするためのインターフェースを提供します。
        - **date_formatter.py**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトです。コマンドライン引数を解析し、GitHub APIからのデータ取得、リポジトリ情報の処理、Markdown生成といった一連の処理を統括します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレートファイルです。
        - **language_info.py**: リポジトリの主要言語や言語ごとの使用率などの情報を処理・整形するロジックを扱います。
        - **markdown_generator.py**: 処理されたリポジトリデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを構築するロジックを含みます。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動的に取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するためのロジックを含みます。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報（名前、説明、言語、スター数など）を抽出し、後の処理に適した形式に整形します。
        - **seo_template.yml**: サイトのSEOメタデータや、検索エンジン向けの特別な記述に関するテンプレート設定を定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計するロジックを提供します。
        - **strings.yml**: プロジェクトで表示される各種メッセージ、ラベル、文言などを一元管理するためのファイルです。国際化対応（i18n）を容易にします。
        - **template_processor.py**: Markdown生成時に使用するテンプレートファイルに対して、動的にデータを挿入したり、条件付きでコンテンツをレンダリングしたりする処理を担当します。
        - **url_utils.py**: URLの構築、検証、解析など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能に対する単体テストを記述したファイルです。
- **tests/**: pytestフレームワークを使用して記述された、プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールが他のコンポーネントと連携して正しく機能するかを確認する統合テストです。
    - **test_config.py**: `config_manager`モジュールが設定ファイルを正しく読み込み、解析するかを確認するテストです。
    - **test_date_formatter.py**: `date_formatter`モジュールの日付フォーマット機能が意図通りに動作するかを確認するテストです。
    - **test_environment.py**: プロジェクトの実行環境が正しく設定されているか、必要な依存関係が満たされているかなどを確認するテストです。
    - **test_integration.py**: プロジェクトの主要なフロー（APIアクセスからMarkdown生成まで）が全体として正しく機能するかを確認する統合テストです。
    - **test_markdown_generator.py**: `markdown_generator`モジュールが期待されるMarkdownコンテンツを生成するかを確認するテストです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールがリポジトリから概要を正しく取得できるかを確認するテストです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEファイルからバッジ情報を正しく抽出できるかを確認するテストです。
    - **test_repository_processor.py**: `repository_processor`モジュールがGitHub APIからのリポジトリデータを適切に処理・整形するかを確認するテストです。

## 関数詳細説明
以下の関数は、ファイル名とプロジェクトの目的から推測される主要な役割を説明したものです。具体的な引数や戻り値はソースコードを参照する必要があります。

- **`src/generate_repo_list/generate_repo_list.py`**: メインスクリプト
    - **`main()`**: プロジェクトのエントリーポイント。コマンドライン引数の解析、GitHub APIからのデータ取得、リポジトリ情報の処理、Markdown生成、ファイル出力という一連の処理をオーケストレートします。
    - **`_parse_arguments()`**: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、設定オブジェクトとして返します。
    - **`_run_generation(username, output_path, limit)`**: 指定されたユーザー名に基づいてリポジトリ情報の取得からMarkdown生成、そしてファイルへの書き込みまでを実行します。
- **`src/generate_repo_list/repository_processor.py`**: リポジトリ情報処理
    - **`fetch_repositories(username, github_token, config)`**: GitHub APIを呼び出し、指定されたユーザーのリポジトリ情報を取得します。プライベートリポジトリへのアクセスにはGitHubトークンを使用します。
    - **`process_single_repository(repo_data, config)`**: GitHub APIから取得した単一のリポジトリの生データを受け取り、表示に必要な情報（名前、説明、URL、スター数、最終更新日など）を抽出し、整形された辞書形式で返します。
- **`src/generate_repo_list/markdown_generator.py`**: Markdown生成
    - **`generate_repo_list_markdown(repositories, config, strings)`**: 処理済みのリポジトリ情報のリストを受け取り、これらを基にしてGitHub Pagesサイト用の最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    - **`_generate_repo_section(repo_info, config, strings)`**: 単一のリポジトリ情報から、そのリポジトリに関する個別のMarkdownセクション（タイトル、説明、バッジ、リンクなど）を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: プロジェクト概要取得
    - **`fetch_project_overview(repo_full_name, file_path, github_token, config)`**: 指定されたリポジトリ（`repo_full_name`）内の特定のファイル（`file_path`）から、プロジェクト概要の3行説明を抽出して返します。APIリクエストにはGitHubトークンが使用される可能性があります。

## 関数呼び出し階層ツリー
```
現在の情報では詳細な関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-01-30 07:09:01 JST
