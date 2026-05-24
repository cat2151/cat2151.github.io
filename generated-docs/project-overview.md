Last updated: 2026-05-25

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pagesサイト用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンによるクロールを最適化し、LLMからのリポジトリ参照失敗を緩和することを目的としています。
- リポジトリ一覧ページ、個別のリポジトリ概要、SEO最適化されたMarkdown生成などの機能を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (コンテンツ生成形式), HTML (生成されるウェブページの構造)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), pytest (テストフレームワーク), Ruff (Pythonコードリンター)
- テスト: pytest (Pythonコードの単体・統合テストに使用)
- ビルドツール: プロジェクト自体にビルドツールは含まれませんが、生成されたMarkdownはJekyllによってウェブサイトとして処理されます。
- 言語機能: Python (CLIオプション解析、ファイル操作、HTTPリクエスト、文字列処理など)
- 自動化・CI/CD: GitHub Actions (プロジェクト内の自動化スクリプト`check_large_files`の実行示唆あり), `_config.yml` (Jekyllによるサイト生成自動化)
- 開発標準: Ruff (Pythonコードのスタイルガイド強制), .editorconfig (エディタ設定の統一)

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
- **.editorconfig**: 複数の開発者が一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsや関連する自動化スクリプトを格納するディレクトリ。
    - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック用スクリプトの説明ドキュメント。
    - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック用スクリプトの設定ファイル。
    - **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記載されたファイル。
- **README.md**: プロジェクトの概要、使い方、設定方法、主な機能などを説明するルートドキュメント。
- **_config.yml**: Jekyllサイトの全体設定ファイル。GitHub Pagesのビルド設定やテーマなどを定義。
- **assets/**: Webサイトで使用される画像、アイコン、フォントなどの静的アセットを格納するディレクトリ。
    - **assets/favicon-16x16.png**, **assets/favicon-192x192.png**, **assets/favicon-32x32.png**, **assets/favicon-512x512.png**: サイトの各種サイズのファビコン（ウェブサイトのアイコン）。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプト。
- **generated-docs/**: 自動生成されたドキュメントやコンテンツが格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のためのHTML認証ファイル。
- **index.md**: GitHub PagesサイトのメインページとなるMarkdownファイル。リポジトリ一覧がこのファイルに生成される。
- **issue-notes/22.md**: プロジェクトの特定の課題やノートを記録するためのMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイル。ウェブアプリの表示や動作を定義。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイル。
- **requirements-dev.txt**: 開発環境およびテスト時に必要なPythonパッケージとそのバージョンを列挙したファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージとそのバージョンを列挙したファイル。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしても良いか、または避けるべきかを指示するファイル。
- **ruff.toml**: PythonコードのリンティングツールRuffの設定ファイル。コードの品質と一貫性を保つためのルールを定義。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    - **src/generate_repo_list/**: リポジトリ一覧生成システムの主要なモジュール群。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの言語やステータスなどのバッジ画像を生成する機能を担当するモジュール。
        - **src/generate_repo_list/config.yml**: リポジトリ一覧生成機能固有の設定（例：プロジェクト概要取得機能のON/OFF、ターゲットファイル名など）。
        - **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`や`secrets.toml`など）の読み込み、解析、管理を行うモジュール。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティモジュール。
        - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインスクリプト。
        - **src/generate_repo_list/json_ld_template.json**: SEO最適化のためのJSON-LD形式の構造化データテンプレート。
        - **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理・整形するモジュール。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報をもとに、最終的なMarkdownコンテンツを構築するモジュール。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリから特定のファイル（例：`generated-docs/project-overview.md`）を読み込み、プロジェクト概要を抽出するモジュール。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報（例：CI/CDステータスバッジ）を抽出するモジュール。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換するモジュール。
        - **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するファイル。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するモジュール。
        - **src/generate_repo_list/strings.yml**: アプリケーション内で使用される静的な文字列やメッセージを集中管理するためのファイル。多言語対応の基盤にもなりうる。
        - **src/generate_repo_list/template_processor.py**: Markdown生成のためのテンプレートファイル（例：Jekyllテンプレート）を処理し、データと結合するモジュール。
        - **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URL関連の共通ユーティリティ関数を集めたモジュール。
- **test_project_overview.py**: プロジェクト概要取得機能に対するテストコード。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **tests/conftest.py**: pytestのテスト実行時に共通で使用されるフィクスチャ（テスト用データやセットアップ）を定義するファイル。
    - **tests/test_badge_generator_integration.py**: `badge_generator`モジュールの統合テスト。
    - **tests/test_check_large_files.py**: 大容量ファイルチェック用スクリプトのテストコード。
    - **tests/test_config.py**: 設定ファイルの読み込みや管理機能に関するテスト。
    - **tests/test_date_formatter.py**: 日付整形モジュールの機能テスト。
    - **tests/test_environment.py**: プロジェクトの実行環境設定に関するテスト。
    - **tests/test_integration.py**: プロジェクトの主要機能間の連携を検証する統合テスト。
    - **tests/test_markdown_generator.py**: Markdown生成モジュールの機能テスト。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能のモジュールテスト。
    - **tests/test_readme_badge_extractor.py**: READMEからバッジ情報を抽出する機能のモジュールテスト。
    - **tests/test_repository_processor.py**: リポジトリデータ処理モジュールの機能テスト。

## 関数詳細説明
関数に関する詳細な情報（役割、引数、戻り値、機能）は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-25 07:23:03 JST
