Last updated: 2026-10-16

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを出力します。
- 検索エンジンでの視認性を高め、LLMによるリポジトリ参照を支援することを目的としています。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーターとして利用され、生成されたMarkdownファイルを元にサイトを構築します。
    - **Markdown**: リポジトリ一覧やプロジェクト概要の出力形式として採用されており、Jekyllと連携してHTMLに変換されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **pytest**: Pythonコードの単体テストおよび結合テストを行うためのフレームワークです。
    - **ruff**: Pythonコードのフォーマットとリンティングを自動的に行い、コードスタイルを統一・維持します。
    - **Git/GitHub**: ソースコードのバージョン管理とリポジトリホスティングに使用されます。
- テスト:
    - **pytest**: Pythonプロジェクトのテストフレームワークとして、コードの品質と信頼性を保証するために使用されます。
- ビルドツール:
    - **Pythonスクリプト**: メインの`generate_repo_list.py`スクリプトが、GitHub APIからのデータ取得、加工、Markdownファイルの生成を担当します。
    - **Jekyll**: GitHub Pagesの基盤として、生成されたMarkdownファイルやその他の静的アセットを処理し、公開可能なウェブサイトを構築します。
- 言語機能:
    - **Python**: プロジェクトの中核をなすスクリプト言語であり、リポジトリ情報の取得、処理、Markdown生成のロジックが実装されています。
- 自動化・CI/CD:
    - このプロジェクトは「CI/CD不要のローカル開発重視」と明記されており、一般的なCI/CDパイプラインは構築されていません。ただし、特定の自動化スクリプト（例: `.github_automation/check_large_files.py`）が存在します。
- 開発標準:
    - **ruff**: Pythonコードのスタイルガイド（PEP 8など）に準拠させるためのリンターおよびフォーマッターとして使用され、コード品質と可読性を維持します。

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
- **`.editorconfig`**: 異なるIDEやエディタ間で、インデントスタイル、文字コード、行末文字などのコード整形ルールを統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトの目的と使用方法を説明するドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイルで、大きなファイルと見なす閾値などを定義します。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: GitHubリポジトリ内で指定された閾値を超える大きなファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義します。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンスファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、設定方法、クイックテスト、コマンド例などを説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグやテストに特化したスクリプトである可能性があります。
- **`generated-docs/`**: `project_overview_fetcher`機能によって各リポジトリから取得される概要ファイルなどを格納する想定のディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **`index.md`**: メインの出力ファイルであり、生成されたGitHubリポジトリ一覧がMarkdown形式で記述されます。GitHub Pagesのトップページとして機能します。
- **`issue-notes/22.md`**: 開発中の特定の課題（Issue #22）に関するメモや詳細を記録したファイルである可能性があります。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリ名、アイコン、表示モードなどを定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの挙動やオプションをカスタマイズします。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを定義します。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンを定義します。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットツールであるruffの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージの初期化ファイルであり、`src`ディレクトリがPythonパッケージであることを示します。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示します。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックをカプセル化しています。
- **`src/generate_repo_list/config.yml`**: プロジェクト固有の技術的パラメータ（例: プロジェクト概要取得機能の有効/無効、対象ファイルパス、タイムアウト設定）を定義する設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で利用可能な設定オブジェクトを提供するモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換する機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理を orchestrate します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報などを処理・整形する機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報やプロジェクト概要などを元に、最終的なMarkdownコンテンツを生成するロジックをカプセル化しています。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出・取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを受け取り、表示用に整形・加工する主要なロジックを担います。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関するメタデータやテンプレート設定を定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言（例: ヘッダー、フッター、カテゴリ名）を一元的に管理するファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートの読み込みや変数置換を行う機能を提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、整形など、URL関連のユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview`機能の単体テストや統合テストを含むファイルです。
- **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するための設定ファイルです。
- **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを行うファイルです。
- **`tests/test_check_large_files.py`**: `check_large_files.py`スクリプトのテストを行うファイルです。
- **`tests/test_config.py`**: `config_manager`や設定ファイルの読み込みに関するテストを行うファイルです。
- **`tests/test_date_formatter.py`**: `date_formatter`モジュールのテストを行うファイルです。
- **`tests/test_environment.py`**: 開発・実行環境のセットアップや依存関係に関するテストを行うファイルです。
- **`tests/test_integration.py`**: プロジェクト全体の主要な機能が連携して動作するかを確認する統合テストを行うファイルです。
- **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールのテストを行うファイルです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのテストを行うファイルです。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのテストを行うファイルです。
- **`tests/test_repository_processor.py`**: `repository_processor`モジュールのテストを行うファイルです。

## 関数詳細説明
提供されたプロジェクト情報およびファイル分析からは、個々の関数の詳細（役割、引数、戻り値など）を具体的に特定できませんでした。
しかし、各ファイル名から推測される役割に基づき、主要な処理が特定の関数として実装されていると考えられます。

例えば、以下のモジュールにはそれぞれの目的を達成するための関数群が含まれると推測されますが、具体的なシグネチャは不明です。
- `src/generate_repo_list/generate_repo_list.py`: メイン処理を制御する関数（例: `main()`, `run_generation()`）や、GitHub APIとの連携関数などが含まれると推測されます。
- `src/generate_repo_list/project_overview_fetcher.py`: リモートファイルから特定のセクションを抽出する関数（例: `fetch_project_overview(repo_url, config)`）などが含まれると推測されます。
- `src/generate_repo_list/markdown_generator.py`: リポジトリデータからMarkdown形式の文字列を生成する関数（例: `generate_repo_markdown(repo_data)`）などが含まれると推測されます。
- `src/generate_repo_list/config_manager.py`: 設定ファイルを読み込む関数（例: `load_config(config_path, secrets_path)`）などが含まれると推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-16 07:11:41 JST
