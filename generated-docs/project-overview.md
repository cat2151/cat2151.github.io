Last updated: 2026-07-04

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンによるクロールとLLMからの参照性向上を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベース) - GitHubが提供するウェブサイトホスティングサービスで、Jekyll静的サイトジェネレーターを利用してMarkdownからサイトを構築します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - pytest: Pythonで書かれたテストコードを実行するためのフレームワーク。
    - ruff: 高速なPythonリンターおよびフォーマッター。コードスタイルを自動修正し、品質を維持します。
    - config.yml / strings.yml: プロジェクトの設定値や表示メッセージ、文言を管理するためのYAMLファイル。
    - requirements.txt / requirements-dev.txt: プロジェクトの実行時および開発時に必要なPythonパッケージとそのバージョンを管理するファイル。
- テスト:
    - pytest: Pythonのテストフレームワークとして、ユニットテストや結合テストの実行に利用されます。
- ビルドツール:
    - Pythonスクリプト: GitHub APIから取得した情報に基づき、マークダウンファイルを生成する主要なスクリプトです。
- 言語機能:
    - Python: このプロジェクトの主要な開発言語であり、GitHub APIとの連携、データ処理、マークダウン生成など全てのロジックを担います。
- 自動化・CI/CD:
    - GitHub Actions (部分的に示唆): `.github_automation`ディレクトリの存在から、特定のアクション（例: 大容量ファイルチェック）の自動化が示唆されますが、主要なCI/CDパイプラインは構築されていません。GitHub PagesのデプロイはGitHub自体が自動的に行います。
- 開発標準:
    - ruff: コードのフォーマットとリンティングにより、一貫したコードスタイルと品質を強制します。
    - .editorconfig: 異なるエディタやIDE間で一貫したコーディングスタイルを定義するための設定ファイル。

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
- **`.editorconfig`**: 異なる開発環境間でコードのインデントスタイルや文字コードなどの設定を統一するためのファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定ファイルを格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルがないかをチェックする自動化スクリプト群です。
        - **`README.md`**: `check_large_files`機能に関する説明です。
        - **`check-large-files.toml`**: 大容量ファイルチェックの具体的な設定が記述されています。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitでバージョン管理しないファイルやディレクトリを指定するための設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクト全体の目的、機能、使用方法、設定、ライセンスなど、概要を説明するドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定を行うファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコン画像などの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した「project-overview.md」などのドキュメントを一時的に格納する可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: メインの出力ファイルであり、生成されたリポジトリ一覧を含むGitHub Pagesのトップページとなるマークダウンファイルです。
- **`issue-notes/`**: 開発中の課題やメモが格納されている可能性があります。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの見た目や動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発環境でのみ必要なPythonパッケージとその依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行されるために必要なPythonパッケージとその依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットに使用される`ruff`ツールの設定ファイルです。
- **`src/`**: プロジェクトのソースコードを格納するディレクトリです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成する主要なロジックが配置されています。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックが含まれています。
        - **`config.yml`**: リポジトリ一覧生成に関する詳細な設定（例: プロジェクト概要取得機能のON/OFF）が記述されています。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体を制御します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートファイルです。
        - **`language_info.py`**: リポジトリの使用言語情報を処理・表示するためのロジックが含まれています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成する主要なモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの`generated-docs/project-overview.md`からプロジェクト概要を自動取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEからバッジ情報を抽出するためのロジックが含まれています。
        - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に整形する役割を担います。
        - **`seo_template.yml`**: SEOメタデータに関するテンプレート設定ファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する各種統計情報（スター数、フォーク数など）を計算するロジックが含まれています。
        - **`strings.yml`**: プロジェクト内で使用される表示文言やメッセージを一元管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdown生成におけるテンプレート処理（例: JekyllのLiquidテンプレート）を担うモジュールです。
        - **`url_utils.py`**: URLの操作や検証を行うためのユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関するテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト設定やフィクスチャを定義するためのファイルです。
    - その他の`test_*.py`ファイル: 各モジュールや機能に対するユニットテストや統合テストが記述されています。

## 関数詳細説明
提供された情報では、個々の関数の具体的な役割、引数、戻り値、詳細な機能は特定できませんでした。
一般的に、このプロジェクトには以下のような関数が含まれていると推測されますが、具体的な実装詳細は不明です。
- `fetch_repositories(username)`: GitHub APIを使用して指定されたユーザーのリポジトリ情報を取得する。
- `process_repository_data(repo_data)`: 取得したリポジトリデータを整形し、必要な情報を抽出する。
- `fetch_project_overview(repo_name, owner)`: 特定のリポジトリからプロジェクト概要を読み込む。
- `generate_markdown_output(repositories)`: 処理されたリポジトリ情報から最終的なMarkdownコンテンツを生成する。
- `save_to_file(filename, content)`: 生成されたコンテンツを指定されたファイルに書き込む。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-04 07:24:35 JST
