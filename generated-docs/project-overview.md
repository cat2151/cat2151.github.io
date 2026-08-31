Last updated: 2026-09-01

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、公開リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- これにより、検索エンジンや大規模言語モデル（LLM）からの参照性を高め、プロジェクトの可視性を向上させます。

## 技術スタック
- フロントエンド:
  - Jekyll: GitHub Pages上で静的サイトを構築するためのフレームワークです。生成されたMarkdownファイルやアセットを元にウェブサイトをレンダリングします。
  - Markdown: GitHub Pagesのコンテンツ記述に広く用いられる軽量マークアップ言語です。生成されるリポジトリ一覧のフォーマットとして利用されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
  - Python: プロジェクトの主要なスクリプト言語です。GitHub APIとの連携、リポジトリ情報の処理、Markdownファイルの生成ロジックがPythonで実装されています。
  - GitHub API: GitHubのリポジトリ情報（名前、説明、言語、星の数、トピックなど）をプログラムから取得するために使用されます。
  - Git: プロジェクトのバージョン管理システムとして利用されています。
- テスト:
  - pytest: Pythonアプリケーションの単体テスト、統合テスト、機能テストを記述・実行するためのフレームワークです。
- ビルドツール:
  - (Pythonスクリプト自身): プロジェクトのPythonスクリプトが、GitHub APIから取得したデータに基づいてMarkdownファイルを生成する「ビルド」ツールとして機能します。
- 言語機能:
  - Python: 高度なデータ構造、ファイルI/O、ネットワーク通信、文字列処理など、Pythonの標準ライブラリと豊富な機能が活用されています。
- 自動化・CI/CD:
  - GitHub Actions (示唆): `.github_automation`ディレクトリが存在し、`check_large_files`スクリプトなど、特定の自動化タスクがGitHub ActionsなどのCI/CD環境で実行されることを想定しています。
- 開発標準:
  - Ruff: Pythonコードの品質と一貫性を保つための高速リンターおよびフォーマッターです。コードスタイルガイドラインの自動適用に利用されます。

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
- **`.editorconfig`**: 異なる開発環境（エディタ、IDE）間でコードのインデントスタイル、文字コード、改行コードなど、基本的な書式設定を一貫させるための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローで使用されるスクリプトや設定ファイルを格納するディレクトリです。
  - **`check_large_files/`**: プロジェクト内の大容量ファイルを検出するための機能群です。
    - **`README.md`**: `check_large_files`機能に関する説明を提供します。
    - **`check-large-files.toml`**: `check_large_files`スクリプトの動作を設定するためのファイルです（例: 許容するファイルサイズの上限、対象外とするパスなど）。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックし、レポートするPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです（例: 自動生成ファイル、一時ファイル、個人設定ファイルなど）。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法、ライセンスなどの概要を説明する主要なドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定を定義するファイルです（例: サイトタイトル、テーマ設定、プラグイン設定など）。
- **`assets/`**: Jekyllサイトで利用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像です。
- **`debug_project_overview.py`**: プロジェクト概要自動取得機能の動作確認やデバッグを行うための補助的なPythonスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要などのドキュメントを一時的に、またはキャッシュとして格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールで、サイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: このプロジェクトによって生成されたリポジトリ一覧のコンテンツが書き出される、GitHub Pagesサイトのメインページファイルです。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録するためのディレクトリです。
  - **`22.md`**: 特定の課題（例: issue #22）に関する詳細なメモや考察を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルです。ホーム画面への追加、起動時の表示設定、アイコンなどのメタデータを定義します。
- **`pytest.ini`**: pytestテストフレームワークの動作を設定するファイルです（例: テストファイルの検出パターン、プラグイン設定、カバレッジ設定など）。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働に最低限必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラー（ロボット）に対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: Ruffリンターおよびフォーマッターの動作を設定するファイルです（例: 有効なルール、無視するファイル、フォーマット設定など）。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
  - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
  - **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能に関連する全てのモジュールを格納するサブパッケージです。
    - **`__init__.py`**: `generate_repo_list`がPythonサブパッケージであることを示すファイルです。
    - **`badge_generator.py`**: プロジェクトの言語、ステータス、アーカイブ状態などを視覚的に示すバッジのMarkdownまたはURLを生成するロジックを実装しています。
    - **`config.yml`**: GitHub APIのタイムアウト設定、リトライ回数、プロジェクト概要取得機能の有効/無効、対象ファイルパスなど、プロジェクト固有の技術的パラメータを定義するYAML形式の設定ファイルです。
    - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム内でアクセスしやすい形で管理するモジュールです。
    - **`date_formatter.py`**: 日付や時刻の情報を様々な形式で整形するためのユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: プロジェクトのメインエントリスクリプトです。コマンドライン引数を解析し、GitHub APIからの情報取得、データの処理、Markdown生成を統括します。
    - **`json_ld_template.json`**: 検索エンジン最適化（SEO）を強化するために、構造化データ（JSON-LD形式）のテンプレートを定義します。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換するモジュールです。
    - **`markdown_generator.py`**: 処理されたリポジトリデータに基づいて、最終的なリポジトリ一覧を含むMarkdown形式の文字列を生成する役割を担います。
    - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得する機能を提供します。
    - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、特定のバッジ（例: ビルドステータス、ライセンス）やその他の構造化された情報を抽出するモジュールです。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（プロジェクト概要、言語、バッジなど）を抽出し、整形する主要な処理モジュールです。
    - **`seo_template.yml`**: ウェブサイト全体のSEOに関連するメタデータや設定（例: サイトのキーワード、ディスクリプション）のテンプレートを定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するためのユーティリティモジュールです。
    - **`strings.yml`**: ウェブサイトで表示される様々なメッセージ、文言、テンプレート内の文字列などを一元的に管理するYAMLファイルです。
    - **`template_processor.py`**: Markdownテンプレートに変数を埋め込んだり、条件に基づいてコンテンツを生成したりするなど、テンプレート処理を行うモジュールです。
    - **`url_utils.py`**: URLの構築、検証、エンコーディング、デコーディングなど、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールで実装されているプロジェクト概要取得機能の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **`conftest.py`**: pytestテストフレームワークで使用される共通のフィクスチャ、フック、設定などを定義するファイルです。
  - **`test_badge_generator_integration.py`**: `badge_generator.py`が他のモジュールと連携して正しく動作するかを確認する統合テストです。
  - **`test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトの機能をテストするファイルです。
  - **`test_config.py`**: `config_manager.py`モジュールが設定ファイルを正しく読み込み、解析できるかをテストします。
  - **`test_date_formatter.py`**: `date_formatter.py`モジュールの日付整形機能が意図通りに動作するかをテストします。
  - **`test_environment.py`**: プロジェクトの実行環境（例: 依存関係のインストール状況）に関するテストを行うファイルです。
  - **`test_integration.py`**: `generate_repo_list.py`が実行する主要な処理フロー全体を網羅する統合テストです。
  - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールが正確なMarkdown出力を生成できるかをテストします。
  - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールがプロジェクト概要を正しく取得できるかをテストします。
  - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールがREADMEファイルからバッジ情報を正しく抽出できるかをテストします。
  - **`test_repository_processor.py`**: `repository_processor.py`モジュールがGitHub APIからの生データを適切に処理し、整形できるかをテストします。

## 関数詳細説明
提供されたプロジェクト情報からは具体的な関数シグネチャが直接的に得られないため、各モジュールの役割に基づいて想定される主要な関数とその機能を抽象的に説明します。

- **`generate_repo_list.py`**:
  - `main()`: プログラムのエントリポイントです。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成という一連のワークフローを統括します。
  - `_get_repositories(username, limit)`: 指定されたGitHubユーザー名でGitHub APIを呼び出し、リポジトリ情報を取得します。オプションで取得数を制限できます。
  - `_process_repository(repo_data)`: GitHub APIから取得した個々のリポジトリの生データを受け取り、表示に必要な情報を抽出・整形し、追加データを付与します。
  - `_generate_markdown(processed_repos)`: 処理済みのリポジトリデータのリストを受け取り、これらを元に最終的なMarkdown形式のリポジトリ一覧文字列を生成します。
- **`project_overview_fetcher.py`**:
  - `fetch_project_overview(repo_url, target_file, section_title)`: 指定されたリポジトリのURLとファイルパス、セクションタイトルに基づき、非同期でプロジェクト概要の3行説明をリモートから取得します。
- **`markdown_generator.py`**:
  - `generate_repo_list_markdown(repositories_data)`: 整形されたリポジトリデータのリストを受け取り、個々のリポジトリの情報を組み合わせて、完全なリポジトリ一覧のMarkdown文字列を作成します。
  - `_format_repository_entry(repo_info)`: 単一のリポジトリ情報から、そのリポジトリ表示用のMarkdownスニペット（タイトル、説明、バッジ、リンクなど）を生成します。
- **`config_manager.py`**:
  - `load_config(config_path)`: 指定されたパスにあるYAML形式の設定ファイルを読み込み、その内容をプログラムが利用しやすい形式（例: 辞書やオブジェクト）で返します。
- **`badge_generator.py`**:
  - `create_badge(label, message, color)`: 与えられたラベル、メッセージ、色情報に基づいて、Shields.io形式などのバッジを表現するMarkdownまたはURL文字列を生成します。
- **`repository_processor.py`**:
  - `process_github_repo_data(raw_repo_data)`: GitHub APIから取得した未加工のリポジトリデータ（JSON辞書形式）を受け取り、プロジェクトで利用する整形されたデータ構造に変換します。これには、不要な情報の削除や必要な情報の計算などが含まれます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-01 07:11:48 JST
