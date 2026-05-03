Last updated: 2026-05-04

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHub APIを利用してリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、検索エンジンとLLMからの参照性を向上させます。
- 各リポジトリの概要を自動取得・表示し、ユーザーへの情報提供を効率化します。

## 技術スタック
- フロントエンド: Jekyll: 静的サイトジェネレータであり、GitHub Pagesの基盤として利用され、MarkdownファイルをHTMLに変換してウェブサイトを構築します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Pytest: Python用のテストフレームワーク。堅牢なテストスイートの構築と実行をサポートします。
    - Ruff: 超高速なPythonリンターおよびフォーマッター。コードの品質と一貫性を維持します。
- テスト: Pytest: Pythonアプリケーションのテストを効率的に記述・実行するためのフレームワークです。
- ビルドツール: Python: このプロジェクトの主要な開発言語であり、GitHub APIからのデータ取得とMarkdown生成スクリプトを実行します。
- 言語機能: Python: GitHub APIとの連携、データ処理、Markdown生成のための主要なプログラミング言語です。
- 自動化・CI/CD: GitHub Actions (部分的に示唆): `.github_automation`ディレクトリの存在から、将来的、または部分的な自動化の可能性が示唆されますが、現在のプロジェクトはローカル開発を重視しています。
- 開発標準:
    - Ruff: Pythonコードの品質と一貫性を自動的にチェックし、修正するためのリンターおよびフォーマッターです。
    - EditorConfig: 異なるIDEやエディタ間でコードの書式設定を統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: プロジェクト内の大きなファイルを検出し、管理するためのサブディレクトリです。
        - **`README.md`**: `check_large_files`機能の目的、使用方法、設定に関する説明を記載したドキュメントです。
        - **`check-large-files.toml`**: 大きなファイルのチェック機能に関する設定（例: サイズ上限、対象外パス）を定義するファイルです。
        - **`scripts/check_large_files.py`**: 実際の大きなファイル検出ロジックを実装したPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から外すファイルやディレクトリ（例: ログファイル、一時ファイル、依存関係のキャッシュ）を指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス条項が記載されています。
- **`README.md`**: プロジェクトの目的、背景、主な機能、開発者向けのヒント、クイックテスト実行方法、設定ファイル、コマンド例などが記述された主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体のグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: ウェブサイトで使用される静的なアセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なる解像度バージョンです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能のデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動生成されたドキュメント（例えば、各リポジトリのプロジェクト概要）が一時的に保存される、または参照されることを意図したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: `generate_repo_list.py`スクリプトによって、GitHubリポジトリの一覧がMarkdown形式で生成され出力されるメインファイルです。このファイルがGitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 特定のGitHub Issueに関するメモや詳細な議論を格納するディレクトリです。
    - **`22.md`**: Issue #22に関連する詳細なメモや情報が記述されたMarkdownファイルです。
- **`manifest.json`**: Progressive Web App (PWA) のマニフェストファイルです。ウェブアプリの表示方法、アイコン、起動画面などを定義し、ユーザーがアプリをホーム画面に追加できるようにします。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの実行方法、テストファイルの発見ルール、プラグイン設定などを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージの依存関係リストです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージの依存関係リストです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしてはならないかを指示するファイルです。
- **`ruff.toml`**: PythonのリンターおよびフォーマッターであるRuffの設定ファイルです。コードスタイル規則、無視するエラー、フォーマットオプションなどを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するメインロジックを含むPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージを示すファイルです。
        - **`badge_generator.py`**: リポジトリの言語バッジやその他の情報バッジを生成するためのロジックを実装しています。
        - **`config.yml`**: プロジェクトの実行時設定（例: プロジェクト概要取得機能の有効/無効、タイムアウト設定）を定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml`や外部のシークレットファイル（例: `secrets.toml`）から設定値を読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: リポジトリの作成日や更新日などの日付情報を、ユーザーフレンドリーな形式に整形するための機能を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成します。
        - **`json_ld_template.json`**: 検索エンジンのSEOを強化するために、構造化データ（JSON-LD形式）を生成するためのテンプレートファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を取得、処理、整形するためのロジックを提供します。
        - **`markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なGitHub Pages向けのMarkdownコンテンツを構造化して生成する役割を担います。
        - **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動的に抽出するための機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジックを実装しています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、Markdown生成に適した内部データ構造に加工・変換する中心的な役割を担います。
        - **`seo_template.yml`**: ウェブサイトのSEOメタデータ（タイトル、ディスクリプション、キーワードなど）を設定するためのテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するための機能を提供します。
        - **`strings.yml`**: ウェブサイトで表示される各種メッセージ、ラベル、文言などを一元的に管理するためのファイルです（多言語対応や文言の統一に利用）。
        - **`template_processor.py`**: Markdown生成のためのテンプレート（Jinja2などのテンプレートエンジン）をロードし、データを使ってレンダリングする処理を抽象化します。
        - **`url_utils.py`**: URLの構築、解析、検証など、URLに関連する汎用的なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: Pytestのテストにおいて共通で利用されるフィクスチャ（テスト環境のセットアップ・ティアダウン）やフックを定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`が他のシステムと連携して正しく動作するかを確認する統合テストです。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトの機能を検証するためのテストです。
    - **`test_config.py`**: `config_manager.py`など、設定ファイルの読み込みと管理が正しく行われるかを確認するテストです。
    - **`test_date_formatter.py`**: `date_formatter.py`モジュールの日付整形機能が正しく動作するかを検証するテストです。
    - **`test_environment.py`**: プロジェクトが想定する実行環境（例: 依存関係のインストール状況、環境変数）が正しく設定されているかを確認するテストです。
    - **`test_integration.py`**: プロジェクト全体の主要なフロー（GitHub APIからのデータ取得からMarkdown生成まで）が正しく連携して動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールが意図通りにMarkdownコンテンツを生成するかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールが正しくプロジェクト概要を抽出できるかを検証するテストです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールがREADMEから正しくバッジを抽出できるかを検証するテストです。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールがGitHub APIからのデータを正しく処理・変換できるかを検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には、個別の関数の詳細な情報（引数、戻り値、具体的な機能）が含まれていません。また、「関数呼び出し階層を分析できませんでした」とあります。そのため、具体的な関数名やその詳細な説明を提供することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-04 07:17:08 JST
