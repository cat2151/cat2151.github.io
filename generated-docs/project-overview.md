Last updated: 2026-04-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、JekyllベースのGitHub Pages向けリポジトリ一覧を自動生成します。
- SEO最適化されたMarkdown形式で、リポジトリ情報を整理し表示します。
- 各リポジトリから概要を抽出し、検索エンジンでの発見性を高めることを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレーターとして利用し、Markdown形式でコンテンツを生成します。最終的な出力はHTMLです。)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: GitHub API (リポジトリ情報の取得に利用)、pytest (Pythonコードのテストフレームワーク)、ruff (Pythonコードのスタイルチェックおよびフォーマットツール)。
- テスト: pytest (Pythonアプリケーションのテストフレームワークとして、ユニットテストや統合テストを実行します)。
- ビルドツール: Pythonスクリプト (主に`generate_repo_list.py`がMarkdownファイルを生成する役割を担います)。
- 言語機能: Python (プロジェクトの主要なスクリプト言語として、GitHub APIとの連携やMarkdown生成ロジックの実装に使用されます)。
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリの存在が、GitHub上での自動化されたワークフローの利用を示唆しています)。
- 開発標準: ruff (Pythonコードの品質と一貫性を保つためのリンターおよびフォーマッター)、.editorconfig (異なる開発環境間でのコードスタイル統一を支援します)。

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
-   **.editorconfig**: プロジェクトのコードスタイルを定義し、異なるIDEやエディタ間での一貫性を保証するための設定ファイル。
-   **.github_automation/**: GitHub Actionsなどの自動化されたワークフローやスクリプトを格納するディレクトリ。
    -   **check_large_files/**: 大容量ファイルに関するチェックを自動化するためのスクリプト群。
        -   **README.md**: `check_large_files`機能の目的と使用方法を説明するドキュメント。
        -   **check-large-files.toml**: 大容量ファイル検出スクリプトの設定ファイル。
        -   **scripts/**: 実際のスクリプトを格納するディレクトリ。
            -   **check_large_files.py**: 指定されたサイズを超えるファイルを検出するPythonスクリプト。
-   **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを指定するファイル。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   **README.md**: プロジェクトの目的、機能、セットアップ方法、使い方、開発者向け情報などをまとめたメインのドキュメント。
-   **_config.yml**: Jekyllサイトの全体設定ファイル。GitHub Pagesの振る舞いを制御します。
-   **assets/**: サイトで使用されるファビコンなどの静的アセットを格納するディレクトリ。
    -   **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズで提供されるサイトアイコン（ファビコン）画像ファイル。
-   **debug_project_overview.py**: プロジェクト概要自動取得機能のテストやデバッグを目的としたスクリプト。
-   **generated-docs/**: 各リポジトリから取得・生成されたドキュメントやデータ（例: `project-overview.md`）が一時的または永続的に格納されるディレクトリ。
-   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイル。
-   **index.md**: GitHub Pagesサイトのルートに配置されるMarkdownファイルで、このプロジェクトによって生成されたリポジトリ一覧がここに記述されます。
-   **issue-notes/**: 特定の課題や検討事項に関するメモを格納するディレクトリ。
    -   **22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや解決策の検討が記載されたMarkdownファイル。
-   **manifest.json**: Webアプリケーションマニフェストファイル。プログレッシブウェブアプリ（PWA）として機能させるための設定を含みます。
-   **pytest.ini**: pytestフレームワークの動作を設定するためのファイル。テスト実行時のオプションやパスなどを指定します。
-   **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストするファイル。
-   **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージとそのバージョンをリストするファイル。
-   **robots.txt**: 検索エンジンのウェブクローラーに対し、サイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイル。
-   **ruff.toml**: Ruffリンターおよびフォーマッターのルールや設定を定義するファイル。
-   **src/**: プロジェクトの主要なPythonソースコードを格納するディレクトリ。
    -   **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    -   **generate_repo_list/**: リポジトリ一覧生成機能の中核をなすPythonモジュール群を格納するパッケージ。
        -   **__init__.py**: `generate_repo_list`パッケージであることを示すファイル。
        -   **badge_generator.py**: リポジトリの技術スタックやステータスを示すバッジ（アイコン）を生成するロジックを実装したモジュール。
        -   **config.yml**: リポジトリ一覧生成スクリプトの動作を制御する設定（例: プロジェクト概要取得機能の有効/無効、タイムアウト設定）を定義するYAMLファイル。
        -   **config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション内で利用可能な形式で管理するモジュール。
        -   **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するモジュール。
        -   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式で出力する、本プロジェクトのメインスクリプト。
        -   **json_ld_template.json**: SEO目的で構造化データ（JSON-LD）を生成するためのテンプレートファイル。
        -   **language_info.py**: GitHubリポジトリの主要言語やその他の言語関連情報を処理するモジュール。
        -   **markdown_generator.py**: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装したモジュール。
        -   **project_overview_fetcher.py**: 各リポジトリに存在する`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出・取得するモジュール。
        -   **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、ライセンス）を解析・抽出するモジュール。
        -   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するモジュール。
        -   **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するYAMLファイル。
        -   **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するモジュール。
        -   **strings.yml**: UI表示メッセージ、ラベル、その他の静的テキストを管理するための多言語対応（または単一言語の集約）YAMLファイル。
        -   **template_processor.py**: Markdownテンプレートを読み込み、動的にデータを挿入して最終的なMarkdownファイルを生成するモジュール。
        -   **url_utils.py**: URLの検証、構築、パースなど、URLに関連するユーティリティ関数を提供するモジュール。
-   **test_project_overview.py**: `project_overview_fetcher.py`モジュールなど、プロジェクト概要取得機能の単体テストを行うスクリプト。
-   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **conftest.py**: pytestのフィクスチャ定義やテストヘルパー関数など、複数のテストファイルで共有される設定を記述するファイル。
    -   **test_badge_generator_integration.py**: `badge_generator`モジュールの統合的な動作を検証するテストスクリプト。
    -   **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトの機能をテストするスクリプト。
    -   **test_config.py**: 設定ファイルの読み込み、パース、および設定管理の正確性を検証するテスト。
    -   **test_date_formatter.py**: `date_formatter`モジュールの日付整形機能の正確性を検証するテスト。
    -   **test_environment.py**: プロジェクトの実行環境が正しく設定されているかを確認するテスト。
    -   **test_integration.py**: `generate_repo_list`システム全体の連携と機能を検証する統合テスト。
    -   **test_markdown_generator.py**: `markdown_generator`モジュールが正しくMarkdownコンテンツを生成するかを検証するテスト。
    -   **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールがプロジェクト概要を正確に抽出できるかを検証するテスト。
    -   **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正確に抽出できるかを検証するテスト。
    -   **test_repository_processor.py**: `repository_processor`モジュールがリポジトリデータを正しく処理・整形するかを検証するテスト。

## 関数詳細説明
プロジェクト情報からは、各関数の詳細な役割、引数、戻り値、機能は特定できませんでした。ただし、Pythonスクリプト群（例: `src/generate_repo_list/*.py`）には、ファイル名から推測される役割を持つ関数が実装されていると想定されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-27 07:17:35 JST
