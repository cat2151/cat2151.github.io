Last updated: 2026-06-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたリポジトリ一覧はSEO最適化され、検索エンジンからの参照性を向上させます。
- 各リポジトリの「プロジェクト概要」を自動取得・表示し、サイト来訪者に魅力的な情報を提供します。

## 技術スタック
- フロントエンド: JekyllベースのGitHub Pagesサイトを構築し、Markdown形式でコンテンツを生成します。最終的にHTML/CSSとしてブラウザに表示されます。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連の技術は使用されていません。
- 開発ツール: メインスクリプト言語としてPythonを使用し、バージョン管理にはGitを利用しています。GitHub APIを介してリポジトリ情報を取得します。
- テスト: Pythonのテストフレームワークであるpytestを使用して、コードの品質と機能の正確性を保証します。
- ビルドツール: Pythonスクリプト自身がMarkdownファイルを生成する役割を担います。生成されたMarkdownファイルはJekyllによって最終的なHTMLサイトにビルドされます。
- 言語機能: Pythonの強力な標準ライブラリを利用し、YAML/TOMLファイルの解析、HTTPリクエスト処理（GitHub APIとの通信）、ファイルI/O、文字列操作などを実現しています。
- 自動化・CI/CD: `.github_automation`ディレクトリの存在から、GitHub Actionsなどの自動化ツールを使用して、リポジトリ一覧の生成プロセスを自動化していると推測されます。
- 開発標準: コードの一貫性を保つため、Ruffによるコードフォーマットとリンティング、および.editorconfigによるエディタ設定の統一が導入されています。

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
-   **`.editorconfig`**: コードエディタの設定を定義し、プロジェクト内の開発者間で一貫したコーディングスタイルを維持するためのファイルです。
-   **`.github_automation/`**: GitHub Actionsなど、自動化スクリプトや設定を含むディレクトリです。
    -   **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    -   **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    -   **`.github_automation/check_large_files/scripts/check_large_files.py`**: プロジェクト内の大容量ファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するためのファイルです。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定方法などを説明するメインのドキュメントです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの全体設定を定義します。
-   **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    -   **`assets/favicon-16x16.png`**: 16x16ピクセルのファビコン画像です。
    -   **`assets/favicon-192x192.png`**: 192x192ピクセルのファビコン画像です。
    -   **`assets/favicon-32x32.png`**: 32x32ピクセルのファビコン画像です。
    -   **`assets/favicon-512x512.png`**: 512x512ピクセルのファビコン画像です。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
-   **`generated-docs/`**: プロジェクトによって生成されたドキュメントや、一時的な出力ファイルを格納するためのディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認（認証）に使用されるHTMLファイルです。
-   **`index.md`**: GitHubリポジトリの一覧が自動生成されて出力されるメインのMarkdownファイルです。Jekyllによってウェブページとして処理されます。
-   **`issue-notes/`**: 開発中の課題や検討事項をメモとして記録するディレクトリです。
    -   **`issue-notes/22.md`**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモや考察が記述されたファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を定義するマニフェストファイルで、アプリの表示方法や動作を指定します。
-   **`pytest.ini`**: Pythonのテストフレームワークpytestの設定ファイルで、テストの実行方法やオプションを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
-   **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: Pythonのコードリンター兼フォーマッターであるRuffの設定ファイルで、コードスタイルや品質チェックのルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧を生成する機能の中核となるPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの技術スタックやライセンスなどのバッジ画像を生成するロジックを持つスクリプトです。
        -   **`src/generate_repo_list/config.yml`**: プロジェクトの実行時設定（GitHub APIのリトライ回数、タイムアウト、キャッシュ有効化など）を定義するYAML形式の設定ファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プロジェクト全体で設定を一元管理するためのユーティリティスクリプトです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するスクリプトです。
        -   **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する、このプロジェクトのメインスクリプトです。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ（JSON-LD）を生成する際のテンプレートとなるJSONファイルです。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理するためのユーティリティスクリプトです。
        -   **`src/generate_repo_list/markdown_generator.py`**: リポジトリ情報をもとに、最終的なMarkdown形式のコンテンツを生成するロジックを実装したスクリプトです。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリに存在する`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出・取得するスクリプトです。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリの`README.md`ファイルから、特定のバッジ情報を抽出するためのスクリプトです。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形して後続処理に渡す役割を持つスクリプトです。
        -   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータや記述のテンプレートを定義するYAMLファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するためのスクリプトです。
        -   **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成において、特定のテンプレート形式を処理し、動的なデータを埋め込むためのスクリプトです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するスクリプトです。
-   **`test_project_overview.py`**: プロジェクト概要取得機能の動作を検証するための単体テストスクリプトです。
-   **`tests/`**: プロジェクトのテストコードが格納されているディレクトリです。
    -   **`tests/conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    -   **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    -   **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
    -   **`tests/test_config.py`**: 設定管理機能が正しく動作するかを検証するテストファイルです。
    -   **`tests/test_date_formatter.py`**: 日付フォーマット機能の正確性を検証するテストファイルです。
    -   **`tests/test_environment.py`**: 開発・実行環境に関する前提条件や設定を検証するテストファイルです。
    -   **`tests/test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを検証する統合テストファイルです。
    -   **`tests/test_markdown_generator.py`**: Markdown生成機能のロジックを検証するテストファイルです。
    -   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能が正しく情報を取得できるかを検証するテストファイルです。
    -   **`tests/test_readme_badge_extractor.py`**: READMEファイルからのバッジ情報抽出機能のテストを記述したファイルです。
    -   **`tests/test_repository_processor.py`**: GitHub APIから取得したリポジトリデータの処理ロジックを検証するテストファイルです。

## 関数詳細説明
このプロジェクトでは、提供された情報からは具体的な関数の詳細（役割、引数、戻り値など）を抽出できませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-27 07:29:36 JST
