Last updated: 2026-04-29

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、自身のリポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧を自動生成します。
- 各リポジトリの概要を自動抽出し、検索エンジンからの発見性を高め、LLM連携も支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - GitHub Pages上で静的サイトを構築し、生成されたMarkdownファイルを表示するために使用されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - pytest: Pythonのテストフレームワーク。コードの品質と信頼性を保証するための単体テストおよび統合テストの実行に使用されます。
    - ruff: Pythonコードのリンティングとフォーマットツール。コードスタイルの一貫性を保ち、潜在的な問題を特定するのに役立ちます。
- テスト: pytest - 上記の通り、テストコードの記述と実行に利用されます。
- ビルドツール: Python - メインのスクリプト言語として、GitHub APIからのデータ取得、加工、Markdownファイルの生成といった一連の処理を実行します。
- 言語機能: Python - プロジェクトの主要な実装言語であり、データ処理、API通信、ファイル操作などを行います。
- 自動化・CI/CD:
    - GitHub Pages: 自動生成されたリポジトリ一覧をホストし、公開するためのプラットフォーム。
    - GitHub Actions (間接的): プロジェクト概要取得機能の設定で言及されており、リポジトリごとのワークフロー管理や共通化されたワークフローでの利用が想定されています。
- 開発標準: ruff - Pythonコードの品質とスタイルを統一するための静的解析ツールです。

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
- **.editorconfig**: IDEやエディタ全体でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトを格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェックに関する自動化スクリプト群を格納します。
        - **README.md**: `check_large_files`スクリプトの目的と使用方法を説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェックの具体的な設定（閾値、対象ファイルなど）を定義するTOMLファイルです。
        - **scripts/check_large_files.py**: 指定されたファイルサイズ制限を超えるファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行方法、設定ファイル、ライセンスなどを説明するメインのドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。
- **assets/**: GitHub Pagesサイトで利用される静的アセット（画像ファイルなど）を格納するディレクトリです。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）画像ファイル群です。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグやテストを目的としたスクリプトです。
- **generated-docs/**: 他のリポジトリから自動的に取得・生成されたドキュメント（例: プロジェクト概要の3行説明）が一時的に配置されることを想定したディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。本プロジェクトによって自動生成されたリポジトリ一覧がこのファイルに出力されます。
- **issue-notes/22.md**: プロジェクトの特定の課題（issue #22）に関するメモや詳細を記録するためのMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、ウェブアプリの名前、アイコン、表示設定などを定義するJSONファイルです。
- **pytest.ini**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの発見ルールや実行オプションなどを定義します。
- **requirements-dev.txt**: 開発環境でプロジェクトに必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: 本番環境でプロジェクトの実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonのリンター兼フォーマッター `ruff` の設定ファイルです。コードスタイルルールや無視するファイルなどを定義します。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための空のファイルです。
- **src/generate_repo_list/**: GitHub APIを利用してリポジトリ一覧を生成する主要なPythonモジュール群を格納するパッケージです。
    - **__init__.py**: `generate_repo_list` サブディレクトリをPythonサブパッケージとして認識させるための空のファイルです。
    - **badge_generator.py**: リポジトリの言語やステータスなどを示すバッジ画像を生成するロジックを担当するモジュールです。
    - **config.yml**: `generate_repo_list`スクリプトが使用する、プロジェクト固有の設定（例: プロジェクト概要機能の有効/無効、対象ファイルパスなど）を定義するYAMLファイルです。
    - **config_manager.py**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するためのユーティリティモジュールです。
    - **date_formatter.py**: GitHub APIから取得した日付情報を、人間が読みやすい形式に整形するためのユーティリティモジュールです。
    - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、取得したデータに基づいてMarkdown形式のリポジトリ一覧を生成する、本プロジェクトのメインスクリプトです。
    - **json_ld_template.json**: SEO強化のためにウェブページに構造化データを埋め込む際に使用されるJSON-LD形式のテンプレートファイルです。
    - **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形式にするためのモジュールです。
    - **markdown_generator.py**: 取得したリポジトリ情報やプロジェクト概要情報などを用いて、最終的なMarkdownコンテンツ（リポジトリ一覧ページ）を生成するロジックを担当するモジュールです。
    - **project_overview_fetcher.py**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得するモジュールです。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するためのモジュールです。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすい形式に加工・整形し、必要な情報を抽出する主要なモジュールです。
    - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するためのモジュールです。
    - **strings.yml**: アプリケーション内で表示される様々なテキストメッセージや文言（例: ヘッダー、フッター、分類ラベルなど）を一元的に管理するYAMLファイルです。
    - **template_processor.py**: MarkdownやJSON-LDなどのテンプレートファイルに動的なデータを挿入し、最終的な出力コンテンツを生成するモジュールです。
    - **url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能に関するユニットテストを記述したファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **conftest.py**: `pytest`テストフレームワークにおける共通のフィクスチャ、フック、ヘルパー関数などを定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの統合テストを行うファイルです。
    - **test_check_large_files.py**: `check_large_files.py`スクリプトのテストを行うファイルです。
    - **test_config.py**: 設定ファイル（`config.yml`など）の読み込みや管理に関するテストを行うファイルです。
    - **test_date_formatter.py**: `date_formatter`モジュールの日付整形機能に関するテストを行うファイルです。
    - **test_environment.py**: 実行環境の設定や依存関係に関するテストを行うファイルです。
    - **test_integration.py**: プロジェクトの主要なコンポーネント間の連携を検証する統合テストを行うファイルです。
    - **test_markdown_generator.py**: `markdown_generator`モジュールのMarkdown生成ロジックに関するテストを行うファイルです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのプロジェクト概要取得機能に関するテストを行うファイルです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのREADMEからのバッジ抽出機能に関するテストを行うファイルです。
    - **test_repository_processor.py**: `repository_processor`モジュールのリポジトリデータ処理ロジックに関するテストを行うファイルです。

## 関数詳細説明
提供されたプロジェクト情報には、特定の関数の役割、引数、戻り値、機能に関する具体的な詳細が記述されていません。そのため、ハルシネーションを避けるため、具体的な関数詳細の説明はできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-29 07:23:21 JST
