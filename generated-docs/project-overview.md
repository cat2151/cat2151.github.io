Last updated: 2026-10-20

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジンのクロールを促進し、LLMによるリポジトリ参照の精度向上に貢献します。
- 各リポジトリの概要やバッジ表示、アクティブ/アーカイブ分類に対応しています。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーター。MarkdownファイルからHTMLサイトを構築します。
    - **Markdown**: リポジトリ一覧やプロジェクト概要の記述、および生成されるコンテンツの主要な形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: メインの開発言語であり、リポジトリ情報取得およびMarkdown生成スクリプトの実行環境です。
    - **Ruff**: Pythonコードの高速なリンターおよびフォーマッター。コード品質の維持と自動修正に利用されます。
    - **Pytest**: Pythonアプリケーションのテストフレームワーク。テストの記述と実行に利用されます。
    - **EditorConfig**: 異なるIDEやエディタ間でコーディングスタイルを統一するための設定ファイルフォーマットです。
- テスト:
    - **Pytest**: Pythonプロジェクトの単体テスト、結合テスト、システムテストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報の取得、解析、Markdown生成を行うカスタムスクリプト群です。
    - **GitHub Pages**: Jekyllを基盤とする、GitHubが提供する静的サイトホスティングサービス。生成されたMarkdownをWebサイトとして公開します。
- 言語機能:
    - **Python**: シンプルで読みやすい構文を持つ汎用プログラミング言語。データ処理、Web API連携、テキスト処理に強みがあります。
- 自動化・CI/CD:
    - **GitHub Actions**: (暗黙的に) リポジトリ一覧の自動生成やコード品質チェックなど、プロジェクトの自動化フローを構築するためのCI/CDプラットフォームとして利用されます。(`_automation` ディレクトリから推測)
- 開発標準:
    - **Ruff**: Pythonコードのスタイルガイド（PEP 8など）に準拠させるためのリンティングおよびフォーマットツールです。
    - **EditorConfig**: コードのインデント、改行コード、文字エンコーディングなど、基本的なコーディングスタイルをプロジェクト全体で統一します。

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
-   **`.editorconfig`**: コードのインデントスタイル、文字コード、改行コードなど、基本的なエディタ設定を統一するためのファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    -   **`check_large_files/check-large-files.toml`**: リポジトリ内の大容量ファイルをチェックするための設定ファイルです。ファイルサイズの上限や除外パスなどを定義します。
    -   **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の指定されたファイルサイズを超えるファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。一時ファイルやビルド成果物などを除外します。
-   **`LICENSE`**: プロジェクトのライセンス情報（例: MITライセンス）を記載したファイルです。著作権、利用条件などを明示します。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、セットアップ方法、基本的な使い方などを説明するメインのドキュメントです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
-   **`assets/`**: ウェブサイトで使用される画像、アイコン、フォントなどの静的アセットを格納するディレクトリです。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズです。
-   **`debug_project_overview.py`**: `project_overview_fetcher` などの特定の機能を単体でテストしたり、デバッグしたりするためのスクリプトと推測されます。
-   **`generated-docs/`**: GitHub APIから取得した情報に基づいて自動生成されるドキュメントやMarkdownファイルが格納されるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search ConsoleでこのGitHub Pagesサイトの所有権を確認するために配置されるファイルです。関数やインポートは含まれません。
-   **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このファイルに自動生成されたリポジトリ一覧が書き込まれます。
-   **`issue-notes/`**: 開発中に発生した課題や特定の検討事項に関するメモを格納するためのディレクトリです。
    -   **`issue-notes/22.md`**: 特定の課題（例: GitHub Issue #22）に関する詳細な情報や議論を記録したMarkdownファイルです。
-   **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、プログレッシブウェブアプリ (PWA) の設定や、ホーム画面に追加された際の表示などを定義します。
-   **`pytest.ini`**: Pytestテストフレームワークの設定ファイルです。テストの検出方法、プラグイン、オプションなどを設定します。
-   **`requirements-dev.txt`**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`requirements.txt`**: 本番環境でこのプロジェクトが動作するために必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Ruffリンター/フォーマッターの設定ファイルです。Pythonコードのスタイルチェックルールや自動修正の挙動を定義します。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **`src/__init__.py`**: Pythonのパッケージであることを示すファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成機能に関連する全てのモジュールをまとめたPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` パッケージであることを示すファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成または処理する機能を提供します。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを含む、リポジトリ一覧生成スクリプトの実行時設定を定義するYAMLファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: `config.yml` や他の設定ファイルを読み込み、アプリケーション全体で利用できるように管理するモジュールです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形するためのユーティリティ関数を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルとして出力する処理全体を制御します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用されるJSON-LD（構造化データ）のテンプレートファイルです。
        -   **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの主要なプログラミング言語に関する情報を取得・処理するモジュールです。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックを実装しています。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから、既存のバッジ情報を抽出するための機能を提供します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に処理・整形する主要なモジュールです。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや、Jekyllサイトの各ページに適用されるテンプレート設定を定義するYAMLファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算・集計するためのモジュールです。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で表示される様々なメッセージや文言を、一元的に管理するためのYAMLファイルです。国際化にも対応可能です。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用されるテンプレートファイルを読み込み、データに基づいてレンダリングする処理を担うモジュールです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの単体テストを定義するファイルです。
-   **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
    -   **`tests/conftest.py`**: Pytestのテストランナーで共有されるフィクスチャやヘルパー関数を定義するファイルです。
    -   **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を確認するためのテストファイルです。
    -   **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能の正確性を検証するためのテストファイルです。
    -   **`tests/test_config.py`**: 設定ファイルの読み込み、パース、管理が正しく行われることを確認するためのテストファイルです。
    -   **`tests/test_date_formatter.py`**: 日付フォーマットユーティリティの正確性を検証するためのテストファイルです。
    -   **`tests/test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係が正しく機能するかを確認するテストファイルです。
    -   **`tests/test_integration.py`**: 主要なコンポーネントが連携して正しく動作することを確認するための包括的な統合テストファイルです。
    -   **`tests/test_markdown_generator.py`**: Markdown生成ロジックが期待通りに動作し、正しい出力が生成されることを確認するテストファイルです。
    -   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能が正しく動作し、期待される概要を抽出できることを確認するテストファイルです。
    -   **`tests/test_readme_badge_extractor.py`**: READMEからバッジ情報を正確に抽出できるかを確認するテストファイルです。
    -   **`tests/test_repository_processor.py`**: リポジトリデータ処理ロジックが正しく機能し、データを適切に整形できることを確認するテストファイルです。

## 関数詳細説明
提供されたプロジェクト情報には、個別の関数の詳細（役割、引数、戻り値、機能など）は含まれておりません。そのため、ここでは詳細な説明を割愛します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-10-20 07:12:10 JST
