Last updated: 2026-08-25

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIを用いてリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- これにより、リポジトリの検索エンジンによる発見性を高め、LLMからの参照性向上も期待されます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤技術で、生成されたMarkdownファイルを静的サイトとして公開します), Markdown (GitHub APIから取得した情報に基づき、整形されたMarkdownファイルが自動生成されます)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得・加工・Markdown生成の全てを担います), Ruff (Pythonコードの品質を維持するためのLinterおよびFormatterです)
- テスト: pytest (Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです)
- ビルドツール: Pythonスクリプト (本プロジェクトでは、Pythonスクリプト自体がリポジトリ情報からMarkdownファイルを「ビルド」する役割を担います), Jekyll (生成されたMarkdownファイルを静的サイトとして公開する際に利用されます)
- 言語機能: Python (汎用的なプログラミング言語であり、スクリプト実行環境として使用されます)
- 自動化・CI/CD: GitHub Actions (リポジトリ内に自動化スクリプトが含まれるため、GitHub Actionsによる自動実行も想定されますが、プロジェクトのREADMEでは「CI/CD不要のローカル開発重視」と明記されています), Pythonスクリプト (ローカルでの自動生成プロセスを担います)
- 開発標準: Ruff (コードスタイルと品質を統一し、保守性を高めるために利用されます)
- その他: GitHub API (GitHubからリポジトリ情報を取得するために利用されます), YAML/TOML (設定ファイルの記述に利用されます)

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
- **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックするための特定の自動化機能です。
        - **`README.md`**: この自動化機能の説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
        - **`scripts/check_large_files.py`**: 実際に大容量ファイルをチェックするPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです（例: ビルド生成物、一時ファイルなど）。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクト全体の概要、セットアップ方法、使い方、利用可能なコマンドなどが記された主要なドキュメントファイルです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の基本的な設定を定義するファイルです。
- **`assets/`**: Webサイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブなどに表示されるファビコン（サイトアイコン）の様々なサイズを格納しています。
- **`debug_project_overview.py`**: 各リポジトリの概要取得機能（`project_overview`）をデバッグするための補助スクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した概要情報など、自動生成されたドキュメントを格納するための場所として想定されています。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイト所有権を確認するために配置されるHTMLファイルです。内容には影響しません。
- **`index.md`**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: プロジェクト開発中の特定の課題やメモを記録するためのディレクトリです。
    - **`22.md`**: 特定の課題（Issue #22）に関するメモが記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてウェブサイトを定義するためのJSONファイルです。ホーム画面への追加、起動時の表示方法などを設定します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テスト実行時のオプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonの依存ライブラリをリストしたファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要となるPythonの依存ライブラリをリストしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのLinter/FormatterであるRuffの設定ファイルです。コーディング規約や自動修正のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するための主要なロジックがまとめられたPythonパッケージです。
        - **`badge_generator.py`**: リポジトリに表示するバッジ（状態を示す小さなアイコン）を生成するための機能を提供します。
        - **`config.yml`**: プロジェクト概要取得機能など、本システム固有の技術的パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: YAMLやTOML形式の設定ファイルを読み込み、管理するためのロジックを提供します。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ機能を提供します。
        - **`generate_repo_list.py`**: プロジェクトの中核となるスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を実行します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートを定義するJSONファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理するための機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するための機能を提供します。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動で取得する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルからバッジ情報を抽出するための機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを加工し、整形するためのロジックを提供します。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するテンプレートや設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリの各種統計情報（例: スター数、フォーク数）を計算するための機能を提供します。
        - **`strings.yml`**: プロジェクト内で使用される表示メッセージや文言を一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Markdown生成などで使用されるテンプレートファイルを処理し、動的なコンテンツを埋め込むための機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で提供されるプロジェクト概要取得機能の単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャ（テストデータやセットアップ関数）を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを行うスクリプトです。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/`機能のテストを行うスクリプトです。
    - **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや解析に関するテストを行うスクリプトです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストを行うスクリプトです。
    - **`test_environment.py`**: プロジェクトの実行環境に関するテストを行うスクリプトです。
    - **`test_integration.py`**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テスト全般を行うスクリプトです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを行うスクリプトです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うスクリプトです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを行うスクリプトです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストを行うスクリプトです。

## 関数詳細説明
提供された情報では、個別の関数の詳細な説明は特定できませんでした。コードベースを直接参照することで、各関数の役割、引数、戻り値、機能の詳細を確認できます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-25 07:07:40 JST
