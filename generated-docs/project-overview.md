Last updated: 2026-03-29

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・整理するシステムです。
- 取得した情報から、GitHub Pages向けにSEO最適化されたMarkdown形式のリポジトリ一覧ページを生成します。
- これにより、リポジトリが検索エンジンにインデックスされやすくなり、LLMの参照失敗といった課題を緩和します。

## 技術スタック
- フロントエンド: Jekyll/GitHub Pages (生成されたMarkdownファイルがGitHub Pages上で表示されます)
- 音楽・オーディオ: なし
- 開発ツール:
    - Python: メインのスクリプト言語として利用
    - GitHub API: リポジトリ情報の取得に使用
- テスト:
    - pytest: Pythonプロジェクトのテストフレームワーク
- ビルドツール:
    - Pythonスクリプト: GitHub APIからデータを取得しMarkdownファイルを生成する、実質的なビルドプロセス
- 言語機能:
    - Python 3.x: 最新のPython言語機能を利用
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation` ディレクトリ配下で自動化スクリプトが構成されており、ファイルチェックなどに利用
- 開発標準:
    - ruff: Pythonコードのフォーマッター兼リンター。コードの品質と一貫性を保つために使用
    - .editorconfig: 異なるエディタ間でのコードスタイル統一のための設定

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
- **.editorconfig**: 異なるエディタやIDE間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェックに関する自動化機能のディレクトリです。
        - **README.md**: `check_large_files` 機能の説明文書です。
        - **check-large-files.toml**: `check_large_files` 機能の設定ファイルです。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルをチェックするPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、使い方、設定方法などを説明するメインのドキュメントです。
- **_config.yml**: Jekyllサイト全体の共通設定（テーマ、プラグインなど）を定義するファイルです。
- **assets/**: GitHub Pagesサイトで使用される画像、アイコンなどの静的ファイルを格納するディレクトリです。
    - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: 異なるサイズのファビコン画像ファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグや単体テストを目的としたスクリプトです。
- **generated-docs/**: スクリプトによって生成されたドキュメントや、特定の情報を抽出する対象となるドキュメントを格納するディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイルです。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトのスクリプトによってリポジトリ一覧がこのファイルに生成されます。
- **issue-notes/**: 開発中の課題やメモを管理するためのディレクトリです。
    - **22.md**: 特定の課題（Issue #22など）に関するメモや詳細を記述したMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などを定義します。
- **pytest.ini**: Pythonのテストフレームワークである `pytest` の設定ファイルです。テストの実行オプションなどを指定します。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonコードのフォーマッター兼リンターである `ruff` の設定ファイルです。コードスタイルや潜在的な問題をチェックします。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: `src` ディレクトリがPythonパッケージであることを示します。
    - **generate_repo_list/**: リポジトリ一覧を生成するための主要なPythonモジュール群を格納するパッケージです。
        - **__init__.py**: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        - **badge_generator.py**: リポジトリのステータスや技術を示すバッジの生成、またはMarkdownへの挿入に関連するロジックを扱います。
        - **config.yml**: リポジトリ一覧生成スクリプトの実行時設定（GitHub APIトークン、プロジェクト概要取得機能の有効/無効、タイムアウト設定など）を定義するファイルです。
        - **config_manager.py**: `config.yml` やその他の設定ファイルを読み込み、プログラム内で利用可能な形式で管理するクラスです。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する、プロジェクトのメインスクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化(SEO)のために、JSON-LD形式の構造化データテンプレートを定義するファイルです。
        - **language_info.py**: 各リポジトリで使用されているプログラミング言語の情報を取得し、整形するロジックを扱います。
        - **markdown_generator.py**: 取得・処理されたリポジトリ情報に基づいて、最終的なMarkdown形式の出力コンテンツを生成するクラスです。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出するロジックを提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（ステータス、カバレッジなど）を抽出するロジックを扱います。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーションで利用しやすいオブジェクトや辞書形式に整形・加工するクラスです。
        - **seo_template.yml**: サイトのSEO関連のメタデータや、生成されるMarkdownのSEO要素に関するテンプレート設定を定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIメッセージ、ヘッダー、フッターなど、アプリケーション内で使用される各種表示文言を一元的に管理する設定ファイルです。多言語対応の基盤にもなり得ます。
        - **template_processor.py**: Jekyllなどのテンプレートエンジンに渡すデータの準備や、テンプレートのレンダリングを処理する役割を担います。
        - **url_utils.py**: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの単体テストを記述したファイルです。
- **tests/**: プロジェクトの各種テストファイルを格納するディレクトリです。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストを記述したファイルです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能 (`.github_automation/check_large_files/scripts/check_large_files.py`) のテストを記述したファイルです。
    - **test_config.py**: 設定ファイルの読み込みや管理 (`config_manager.py`) に関するテストを記述したファイルです。
    - **test_date_formatter.py**: 日付フォーマット機能 (`date_formatter.py`) のテストを記述したファイルです。
    - **test_environment.py**: プロジェクトの実行環境（依存関係、設定など）が正しくセットアップされているかを確認するテストを記述したファイルです。
    - **test_integration.py**: プロジェクトの主要な機能が連携して正しく動作するかを確認する、総合的な統合テストを記述したファイルです。
    - **test_markdown_generator.py**: Markdown生成機能 (`markdown_generator.py`) のテストを記述したファイルです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテストを記述したファイルです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能 (`readme_badge_extractor.py`) のテストを記述したファイルです。
    - **test_repository_processor.py**: リポジトリ情報処理機能 (`repository_processor.py`) のテストを記述したファイルです。

## 関数詳細説明
提供された情報からは具体的な関数の詳細を特定できませんでした。そのため、個々の関数の役割、引数、戻り値、機能について詳細な説明はできません。

## 関数呼び出し階層ツリー
```

---
Generated at: 2026-03-29 07:08:44 JST
