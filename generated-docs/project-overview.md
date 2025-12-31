Last updated: 2026-01-01

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧のMarkdownファイルを自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたコンテンツを生成します。
- 検索エンジンによるクロールとLLMによる参照性を向上させ、プロジェクト情報を効果的に公開します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトが生成するMarkdownファイルはJekyllによってサイトとしてレンダリングされます。
    - **Markdown**: 生成されるリポジトリ一覧のコンテンツ形式。読みやすく構造化されたテキストを記述するための軽量マークアップ言語です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **pytest**: Python用のテストフレームワーク。プロジェクトの機能が正しく動作するかを検証するためのテストを記述・実行します。
    - **ruff**: Pythonの高速なLinterおよびFormater。コードの品質を維持し、スタイルを統一するために使用されます。
    - **Git**: 分散型バージョン管理システム。ソースコードの変更履歴を管理し、複数人での開発を支援します。
- テスト:
    - **pytest**: Pythonコードの単体テスト、統合テストを行うための標準的なフレームワークです。
- ビルドツール:
    - **Python**: スクリプトの実行環境および主要な開発言語。リポジトリ情報の取得、処理、Markdown生成の中核を担います。
    - **GitHub Pages**: 静的ウェブサイトをホスティングするGitHubのサービス。本システムが生成したコンテンツを公開するために利用されます。
- 言語機能:
    - **Python**: 本プロジェクトの主要な開発言語。豊富なライブラリと高い可読性が特徴です。
- 自動化・CI/CD:
    - このプロジェクトはCI/CDを必須とせず、ローカルでの開発・実行を重視した構成となっています。
- 開発標準:
    - **ruff**: コードスタイルを自動修正し、コード品質の標準化を推進します。
    - **.editorconfig**: 複数のエディタやIDEでコードスタイルを統一するための設定ファイルです。

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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 複数の開発者が同じコーディングスタイルを維持するための設定を定義します。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
- **`LICENSE`**: 本プロジェクトがMITライセンスの下で公開されていることを示します。
- **`README.md`**: プロジェクトの概要、目的、主な機能、使い方、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: ウェブサイトで使用される画像、スタイルシート、JavaScriptファイルなどの静的アセットを格納するディレクトリです。
    - `favicon-*.png`: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` モジュールのデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得された `project-overview.md` ファイルが一時的に保存される、またはその構造を模倣するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成される主要なMarkdownファイルで、GitHub Pagesのトップページとしてリポジトリ一覧が表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、アイデアなどを記録するためのMarkdown形式のノートファイル群です。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン機能などの挙動を定義します。
- **`pytest.ini`**: `pytest` テストフレームワークの動作を設定するためのファイルです。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージの依存関係をリストアップします。
- **`requirements.txt`**: 本番環境で本スクリプトを実行するために必要なPythonパッケージの依存関係をリストアップします。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: `ruff` コードスタイルチェッカーおよびフォーマッターのルールと設定を定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - `__init__.py`: Pythonパッケージであることを示し、パッケージの初期化コードを含めることができます。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを構成するPythonモジュール群です。
        - `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        - `badge_generator.py`: リポジトリの言語やライセンスなどの情報に基づいて、ウェブサイトに表示するバッジのMarkdownを生成する機能を提供します。
        - `config.yml`: プロジェクト概要取得機能などの技術的パラメータや設定値を定義するYAML形式の設定ファイルです。
        - `config_manager.py`: `config.yml` や `strings.yml` など、プロジェクトで使用される各種設定ファイルを読み込み、管理するモジュールです。
        - `generate_repo_list.py`: このプロジェクトのメインとなる実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を制御します。
        - `json_ld_template.json`: 検索エンジン最適化 (SEO) のために構造化データを記述するJSON-LD形式のテンプレートファイルです。
        - `language_info.py`: GitHub APIから取得したリポジトリの言語情報を処理し、表示に適した形式に整形する機能を提供します。
        - `markdown_generator.py`: 処理されたリポジトリデータや設定情報に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するモジュールです。
        - `project_overview_fetcher.py`: 他のGitHubリポジトリに存在する `generated-docs/project-overview.md` ファイルから、プロジェクトの概要説明文を自動的に取得する機能を提供します。
        - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、それを加工・整理して、Markdown生成に適した形式に変換する主要モジュールです。
        - `seo_template.yml`: ウェブサイトのSEOを強化するためのメタデータやテンプレート設定を定義するYAMLファイルです。
        - `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・整形する機能を提供します。
        - `strings.yml`: プロジェクトで表示される様々なメッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - `template_processor.py`: Markdown生成時に使用されるJekyllテンプレートやその他の汎用テンプレートをロードし、動的なデータで埋め込む処理を行います。
        - `url_utils.py`: GitHub APIエンドポイントやリポジトリリンクなど、URLに関連するユーティリティ関数（生成、検証、整形など）を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（特にプロジェクト概要の取得）が正しく動作するかを確認するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - `test_config.py`: 設定ファイル (`config.yml`, `strings.yml`) の読み込みとパースが正しく行われるかをテストします。
    - `test_environment.py`: プロジェクトの実行環境（例: 依存ライブラリのインストール状況）に関するテストを行います。
    - `test_integration.py`: 複数のモジュールが連携して動作する際の統合的なテストを実施します。
    - `test_markdown_generator.py`: `markdown_generator.py` が期待通りのMarkdownコンテンツを生成するかをテストします。
    - `test_project_overview_fetcher.py`: `project_overview_fetcher.py` の機能、特にリモートファイルからの概要取得ロジックをテストします。
    - `test_repository_processor.py`: `repository_processor.py` がGitHub APIからのデータを正しく処理・整形するかをテストします。

## 関数詳細説明
- **`generate_repo_list.py`**
    - `main()`: このスクリプトのエントリポイント。コマンドライン引数の解析、設定の読み込み、リポジトリ情報の取得・処理、Markdown生成といった一連のワークフローをオーケストレートします。
    - `parse_arguments()`: コマンドラインから `--username`, `--output`, `--limit` などの引数を解析し、プログラムが使用するオプションとして提供します。
- **`repository_processor.py`**
    - `fetch_repositories()`: GitHub APIと連携し、指定されたユーザーのリポジトリ情報を取得します。プライベートリポジトリへのアクセスにはGitHubトークンを使用します。
    - `process_repository_data()`: 取得した生のリポジトリデータ（JSON形式）を受け取り、必要な情報（説明、言語、スター数など）を抽出・加工して、後のMarkdown生成に適したデータ構造に変換します。
- **`project_overview_fetcher.py`**
    - `fetch_project_overview()`: 特定のリポジトリ（通常は他のGitHubリポジトリ）から、定義されたパス（例: `generated-docs/project-overview.md`）にあるファイルを読み込み、その内容から指定されたセクション（「プロジェクト概要」など）の3行の説明を抽出します。
- **`markdown_generator.py`**
    - `generate_markdown()`: `repository_processor.py` から渡された整形済みのリポジトリデータと、設定ファイルから読み込まれたテンプレートや文字列を使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    - `render_template()`: テンプレートエンジン（Jinja2などを想定）を利用して、Markdownテンプレートに動的なデータを埋め込み、出力用のテキストを生成します。
- **`config_manager.py`**
    - `load_config()`: 指定されたYAMLファイル（例: `config.yml`, `strings.yml`）を読み込み、その内容をPythonの辞書オブジェクトとして返します。設定値のデフォルト処理やバリデーションも行うことがあります。
- **`badge_generator.py`**
    - `generate_badge_markdown()`: リポジトリのプログラミング言語やライセンスなどの特性を表すアイコンやテキストを含むMarkdown形式のバッジを生成します。
- **`language_info.py`**
    - `get_language_details()`: リポジトリの主要なプログラミング言語に関する詳細情報（例: 色、アイコン）を取得し、表示に適した形式で提供します。
- **`statistics_calculator.py`**
    - `calculate_statistics()`: リポジトリのスター数、フォーク数、Issue数、最終コミット日時などの統計情報を計算し、整形された形式で提供します。
- **`url_utils.py`**
    - `build_github_api_url()`: GitHub APIのエンドポイントURLを、ユーザー名やリポジトリ名などのパラメータに基づいて構築します。
    - `sanitize_url_path()`: URLパス内の特殊文字をエンコードするなど、URLを安全な形式に整形します。
- **`template_processor.py`**
    - `process_template()`: Markdown生成時に使用されるテキストテンプレートをロードし、提供されたデータ（リポジトリ情報など）を適用して最終的なテキストコンテンツを生成します。

## 関数呼び出し階層ツリー
```
generate_repo_list.py (メイン実行スクリプト)
├── config_manager.py.load_config() (設定ファイルの読み込み)
├── repository_processor.py.fetch_repositories() (GitHub APIからリポジトリ情報を取得)
│   └── repository_processor.py.process_repository_data() (取得データを整形)
│       ├── project_overview_fetcher.py.fetch_project_overview() (各リポジトリの概要を取得)
│       ├── language_info.py.get_language_details() (言語情報を処理)
│       └── statistics_calculator.py.calculate_statistics() (統計情報を計算)
└── markdown_generator.py.generate_markdown() (Markdownコンテンツを生成)
    ├── markdown_generator.py.render_template() (テンプレートをレンダリング)
    │   └── template_processor.py.process_template() (テンプレートを処理)
    ├── badge_generator.py.generate_badge_markdown() (バッジを生成)
    └── url_utils.py (URL関連のユーティリティ関数を利用)

---
Generated at: 2026-01-01 07:06:46 JST
