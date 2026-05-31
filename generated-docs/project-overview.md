Last updated: 2026-06-01

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧をMarkdownで生成します。
- リポジトリごとの概要表示や分類機能により、検索性向上とLLMの参照を支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレーターの基盤), Markdown (生成されるコンテンツのフォーマット)
- 音楽・オーディオ: 該当なし
- 開発ツール: GitHub (リポジトリホスティング、API提供), Git (バージョン管理システム)
- テスト: Pytest (Pythonコードのテストフレームワーク)
- ビルドツール: 該当なし (JekyllがGitHub Pages側でサイトのビルドを担うため、本プロジェクト自体は特定のビルドツールを使用していません)
- 言語機能: Python (主要なスクリプト開発言語)
- 自動化・CI/CD: 該当なし (プロジェクトはローカル開発重視であり、明示的なCI/CDツールは提示されていません)
- 開発標準: Ruff (Pythonコードの静的解析およびフォーマッター)

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  22.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
-   **.editorconfig**: プロジェクト全体で一貫したコーディングスタイルを定義するための設定ファイルです。
-   **.github_automation/**: GitHub Actionsなど、リポジトリの自動化に関連するスクリプトや設定ファイルを格納するディレクトリです。
    -   **check_large_files/**: 大容量ファイルのチェック機能に関するファイル群をまとめたディレクトリです。
        -   **README.md**: `check_large_files` ディレクトリの目的や使い方を説明するドキュメントです。
        -   **check-large-files.toml**: 大容量ファイルチェックツールの詳細な設定を記述するTOML形式のファイルです。
        -   **scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを特定し、警告するためのPythonスクリプトです。
-   **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイルです。
-   **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **README.md**: プロジェクトの概要、機能、セットアップ方法、使用方法、開発者向けのヒントなどをまとめたメインのドキュメントファイルです。
-   **_config.yml**: JekyllベースのGitHub Pagesサイト全体のグローバルな設定（テーマ、プラグイン、変数など）を定義するファイルです。
-   **assets/**: GitHub Pagesサイトで使用されるファビコンやその他の静的アセット（画像など）を格納するディレクトリです。
    -   **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズと解像度で提供されるウェブサイトのファビコン画像です。
-   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグや単体テストを目的としたPythonスクリプトです。
-   **generated-docs/**: 本プロジェクトによって自動生成されたドキュメントやデータが格納される予定のディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleによるサイトの所有権確認のために配置されたHTMLファイルです。
-   **index.md**: GitHub Pagesのメインページ（トップページ）となるMarkdownファイルです。本スクリプトによってリポジトリ一覧がこのファイルに生成されます。
-   **issue-notes/**: 開発中に発生した課題や特定のトピックに関するメモを格納するためのディレクトリです。
    -   **22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記述したMarkdownファイルです。
-   **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用されるマニフェストファイルで、アプリの表示方法や動作を定義します。
-   **pytest.ini**: PythonのテストフレームワークであるPytestの設定を記述するファイルです。
-   **requirements-dev.txt**: 開発時およびテスト実行時に必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   **requirements.txt**: 本番環境でのプロジェクト実行に必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   **robots.txt**: 検索エンジンクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
-   **ruff.toml**: Pythonコードの静的解析ツール「Ruff」の設定ファイルで、コーディングスタイルや規約を定義します。
-   **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **__init__.py**: Pythonパッケージであることを示すファイルです。
    -   **generate_repo_list/**: GitHubリポジトリ一覧を生成する主要ロジックを格納するサブパッケージです。
        -   **__init__.py**: `generate_repo_list` サブパッケージであることを示すファイルです。
        -   **badge_generator.py**: リポジトリのステータスや技術を示すバッジ画像を生成または処理するロジックが含まれています。
        -   **config.yml**: `generate_repo_list` スクリプトの技術的なパラメータや機能のON/OFFなどを設定するYAMLファイルです。
        -   **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
        -   **date_formatter.py**: 日付や時刻のフォーマットを一貫して行うためのユーティリティ関数を提供します。
        -   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインスクリプトです。
        -   **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
        -   **language_info.py**: GitHubリポジトリの使用言語情報を解析し、処理するロジックが含まれています。
        -   **markdown_generator.py**: 取得したリポジトリ情報に基づいてMarkdown形式のコンテンツを生成するロジックを提供します。
        -   **project_overview_fetcher.py**: 各リポジトリから特定のファイル（例: `project-overview.md`）を読み込み、プロジェクト概要を抽出するロジックです。
        -   **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出するためのロジックが含まれています。
        -   **repository_processor.py**: GitHub APIから取得した個々のリポジトリ情報を整形し、必要なデータを抽出するための主要な処理ロジックです。
        -   **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジックを提供します。
        -   **strings.yml**: UIメッセージ、ヘッダー、フッターなど、アプリケーション内で使用される各種テキスト文字列を集中管理するYAMLファイルです。
        -   **template_processor.py**: Markdown生成時に使用されるテンプレートを処理し、動的なコンテンツを埋め込むためのロジックです。
        -   **url_utils.py**: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数を提供します。
-   **test_project_overview.py**: `project_overview_fetcher.py` の機能、特にプロジェクト概要の抽出ロジックに対する単体テストまたは統合テストを記述したスクリプトです。
-   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **conftest.py**: Pytestのテスト実行時に共有されるフィクスチャやヘルパー関数を定義するためのファイルです。
    -   **test_badge_generator_integration.py**: バッジ生成機能の統合的な動作を確認するためのテストスクリプトです。
    -   **test_check_large_files.py**: 大容量ファイルチェック機能が正しく動作するか検証するテストスクリプトです。
    -   **test_config.py**: 設定ファイルの読み込みや解析が正しく行われるかを確認するテストスクリプトです。
    -   **test_date_formatter.py**: 日付フォーマットユーティリティが期待通りに動作するか検証するテストスクリプトです。
    -   **test_environment.py**: 実行環境の依存関係や設定が適切であるかを確認するテストスクリプトです。
    -   **test_integration.py**: 主要なコンポーネントが連携して正しく動作するかを確認する統合テストスクリプトです。
    -   **test_markdown_generator.py**: Markdown生成ロジックが期待通りの出力を行うか検証するテストスクリプトです。
    -   **test_project_overview_fetcher.py**: プロジェクト概要取得機能が正しく情報を取得・抽出できるか検証するテストスクリプトです。
    -   **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能が正しく動作するか検証するテストスクリプトです。
    -   **test_repository_processor.py**: リポジトリ情報処理ロジックが正確にデータを処理するか検証するテストスクリプトです。

## 関数詳細説明
提供された情報からは具体的な関数情報を得られませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-06-01 07:24:28 JST
