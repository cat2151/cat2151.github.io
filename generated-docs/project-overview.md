Last updated: 2026-09-27

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動的に収集します。
- 取得した情報に基づき、SEO最適化されたGitHub Pages向けリポジトリ一覧Markdownを生成します。
- これにより、検索エンジンでの可視性を高め、LLMによる参照を容易にする目的があります。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、生成されたMarkdownファイルを表示します), Markdown (GitHub Pagesサイトのコンテンツとして自動生成されるマークアップ言語)
- 音楽・オーディオ: なし
- 開発ツール: Python (プロジェクトの主要な開発言語であり、リポジトリ情報取得とMarkdown生成のスクリプトに使用されます), GitHub API (リポジトリ情報を取得するための主要なデータソースとして利用されます)
- テスト: pytest (Pythonスクリプトのテストフレームワークとして、機能の正確性を検証するために使用されます)
- ビルドツール: なし (特定のビルドツールは使用せず、Pythonスクリプトが直接コンテンツを生成します)
- 言語機能: Python (Python言語の標準機能とライブラリが、API通信、データ処理、ファイル操作などに活用されています)
- 自動化・CI/CD: 本プロジェクト自体は「CI/CD不要のローカル開発重視」とされていますが、`generate_repo_list.py`スクリプトがリポジトリ一覧生成プロセスを自動化します。
- 開発標準: ruff (Pythonコードのフォーマットとリンティングを自動化し、コード品質と一貫性を保ちます), .editorconfig (異なるエディタやIDE間で一貫したコーディングスタイルを定義します)
- 設定・データ形式: YAML (プロジェクトの設定ファイルや文字列管理、SEOテンプレートに使用されます), TOML (pytestやruffの設定、GitHubトークンなどの秘密情報を管理するのに使用されます), JSON (SEO用のJSON-LDテンプレートに使用されます)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsで利用される自動化スクリプト群を格納するディレクトリです。このプロジェクト自体が利用するCI/CDではなく、他のリポジトリの自動化を想定しているようです。
    - **check_large_files/**: 大容量ファイルをチェックするためのスクリプト群です。
        - **README.md**: `check_large_files`機能に関する説明です。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **scripts/**: 実際のチェック処理を行うスクリプトを格納するディレクトリです。
            - **check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、使い方、設定方法などが記載された、プロジェクトの玄関となるドキュメントです。
- **_config.yml**: JekyllベースのGitHub Pagesサイト全体のグローバル設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**: 16x16ピクセルのファビコン画像です。
    - **favicon-192x192.png**: 192x192ピクセルのファビコン画像です。
    - **favicon-32x32.png**: 32x32ピクセルのファビコン画像です。
    - **favicon-512x512.png**: 512x512ピクセルのファビコン画像です。
- **debug_project_overview.py**: `project_overview_fetcher`機能の動作をデバッグするための補助スクリプトです。
- **generated-docs/**: プロジェクトのドキュメントが生成される出力先として設定されているディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって、生成されたリポジトリ一覧が最終的に出力されるメインのMarkdownファイルです。
- **issue-notes/**: プロジェクトの課題や検討事項に関するメモを格納するディレクトリです。
    - **22.md**: 特定の課題（Issue #22）に関する詳細メモです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）としてGitHub Pagesを機能させるための設定情報を提供するファイルです。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定を定義するファイルです。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **requirements.txt**: 本番環境でこのプロジェクトを実行するために必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリンター/フォーマッターであるRuffの設定を定義するファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: Pythonパッケージの初期化ファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成の中核となるモジュール群を格納するディレクトリです。
        - **__init__.py**: `generate_repo_list`ディレクトリがPythonモジュールであることを示します。
        - **badge_generator.py**: リポジトリの各種バッジ（例: 言語、ステータス）を生成する機能を提供します。
        - **config.yml**: プロジェクト概要取得機能など、主要な技術的パラメータや動作設定を定義するYAML形式の設定ファイルです。
        - **config_manager.py**: YAML形式の設定ファイルを読み込み、プロジェクト全体の各種設定を管理する役割を担います。
        - **date_formatter.py**: 日付や時刻の情報を、人間が読みやすい形式や特定の表示形式に整形するための機能を提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理を統括します。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のため、JSON-LD形式の構造化データを生成する際のテンプレートとして使用されます。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を取得・処理し、表示に適した形式で提供する機能です。
        - **markdown_generator.py**: 取得したリポジトリ情報や設定に基づき、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアモジュールです。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイルから、プロジェクトの概要説明を自動的に抽出し、提供します。
        - **readme_badge_extractor.py**: 各リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス）を抽出し、リポジトリ一覧に表示できるように処理します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整理する主要な処理ロジックを含みます。
        - **seo_template.yml**: SEO関連のメタデータや設定を定義するためのYAMLテンプレートファイルです。
        - **statistics_calculator.py**: リポジトリに関する様々な統計情報（例: スター数、フォーク数、最終更新日）を計算または集計する機能を提供します。
        - **strings.yml**: UI表示メッセージや文言など、ユーザーに表示される静的テキストを管理するためのYAMLファイルです。
        - **template_processor.py**: Markdown生成に使用されるテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成する役割を担います。
        - **url_utils.py**: URLの検証、整形、生成など、URLに関連する各種ユーティリティ機能を提供します。
- **test_project_overview.py**: `project_overview_fetcher`モジュールのテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **conftest.py**: pytestのテストフィクスチャやヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    - **test_config.py**: 設定管理機能のテストです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストです。
    - **test_environment.py**: 実行環境に関するテストです。
    - **test_integration.py**: プロジェクトの主要な機能間の統合テストです。
    - **test_markdown_generator.py**: Markdown生成機能のテストです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
提供された情報では個々の関数の詳細を特定できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-27 07:12:20 JST
