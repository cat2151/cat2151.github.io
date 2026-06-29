Last updated: 2026-06-30

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身の公開リポジトリ一覧をGitHub Pages向けに自動生成します。
- SEO最適化されたMarkdown形式で出力し、検索エンジンやLLMからの参照性を向上させます。
- 各リポジトリの概要を自動取得し、バッジ付きで一覧表示することで利便性を高めます。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレータとしてGitHub Pagesサイトの基盤), Markdown (生成されるリポジトリ一覧のコンテンツ形式), HTML/CSS (GitHub Pagesサイトのレンダリング)。
- 音楽・オーディオ: (該当する技術は使用されていません。)
- 開発ツール: Python (主要な開発言語), Git (バージョン管理システム), pytest (Pythonテストフレームワーク), ruff (Pythonコードスタイルチェッカー/フォーマッタ)。
- テスト: pytest (Pythonコードの単体および結合テストを実行するためのフレームワーク)。
- ビルドツール: Python (スクリプト自体がGitHub APIからデータを取得しMarkdownファイルを生成する「ビルド」プロセスを担います), YAML (設定ファイルの記述), TOML (設定ファイルの記述)。
- 言語機能: Python (スクリプト実行環境、GitHub APIとの連携、ファイル操作), YAML (設定ファイルの構造化), JSON (データ形式、JSON-LDテンプレートに使用), TOML (設定ファイルの構造化)。
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得), Pythonスクリプト (ファイルの自動生成や、大規模ファイルチェックなどの自動処理を担当)。
- 開発標準: ruff (Pythonコードの統一されたスタイルと品質を維持するためのリンティングおよびフォーマットツール), .editorconfig (異なるIDEやエディタ間でコーディングスタイルの一貫性を保つための設定ファイル)。

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
- **`.editorconfig`**: 異なるIDEやエディタを使用する開発者間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイル。
- **`.github_automation/`**: GitHub関連の自動化スクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大規模なファイルを検出し、管理するためのPythonスクリプト。
- **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイル。
- **`README.md`**: プロジェクトの目的、機能、使用方法、セットアップ手順など、プロジェクト全体に関する主要な情報を提供するドキュメント。
- **`_config.yml`**: Jekyllサイト全体の挙動や設定（テーマ、プラグイン、変数など）を制御するファイル。
- **`assets/`**: Jekyllサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の各種サイズ。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや単独テストを目的としたスクリプト。
- **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するディレクトリ（GitHub Pagesでホストされる可能性のあるコンテンツを含む）。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権の確認に使用されるHTMLファイル。
- **`index.md`**: GitHub Pagesサイトのルートページ（トップページ）。このプロジェクトによって生成されたリポジトリ一覧がここに表示されます。
- **`issue-notes/22.md`**: 特定のIssueに関連するメモや詳細情報を格納するファイル（例としてIssue 22のメモ）。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイル。ホーム画面アイコン、表示モードなどを設定します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの発見方法、プラグイン、引数などを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
- **`requirements.txt`**: 本番環境でこのプロジェクトが実行されるために必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、あるいはクロールしてはならないかを指示するファイル。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッターである `ruff` の設定ファイル。コードスタイルや潜在的なバグのチェックルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **`src/__init__.py`**: Pythonパッケージを示すためのファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能の中核を成すモジュール群。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや言語に応じたバッジ（アイコン）を生成または管理するロジックを実装。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、システム全体の技術的なパラメータを設定するファイル。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）の読み込みや管理を行うモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を統一・整形するためのユーティリティ関数を提供。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリポイント。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を統括するスクリプト。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、ウェブページの内容を構造化データとして記述するJSON-LD形式のテンプレート。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報（例: 表示色など）を処理するモジュール。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報と概要に基づき、SEO最適化されたMarkdownコンテンツを生成するロジックを実装。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要を自動取得するロジックを実装。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報などを抽出するモジュール。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報に加工するロジックを実装。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや設定を定義するファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュール。
        - **`src/generate_repo_list/strings.yml`**: UIに表示されるメッセージや文言などを一元的に管理する設定ファイル。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用するテンプレートの読み込みや変数置換を行うモジュール。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、パス操作などのユーティリティ機能を提供。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするための単体テストファイル。
- **`tests/`**: プロジェクトのテストファイルを格納するディレクトリ。
    - **`tests/conftest.py`**: `pytest` のテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義するファイル。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテスト。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや解析に関するテスト。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`tests/test_environment.py`**: 実行環境（依存関係など）に関するテスト。
    - **`tests/test_integration.py`**: プロジェクト全体の主要なフローに関する統合テスト。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテスト。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    - **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
プロジェクト情報に具体的な関数の詳細説明は提供されていません。

## 関数呼び出し階層ツリー
```
プロジェクト情報に関数呼び出し階層の詳細は提供されていません。

---
Generated at: 2026-06-30 07:26:30 JST
