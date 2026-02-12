Last updated: 2026-02-13

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を取得・整理します。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧を自動生成するシステムです。
- 検索エンジンでの視認性を高め、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll / GitHub Pages** (静的サイトジェネレーターとして利用され、生成されたMarkdownファイルを公開するためのプラットフォーム), **Markdown** (システムによって自動生成される主要なコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (スクリプト言語としてプロジェクト全体のロジックを実装), **GitHub API** (リポジトリ情報を取得するための主要なインターフェース), **PyYAML** (設定ファイル `config.yml`, `strings.yml` などのYAML形式ファイルを読み込むために使用), **requests** (GitHub APIとのHTTP通信を行うためのライブラリ), **toml** (`secrets.toml` などTOML形式の設定ファイルを読み込むために使用)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストを実行するためのフレームワーク)
- ビルドツール: **Pythonスクリプト** (システム自体がリポジトリ情報からMarkdownファイルを「ビルド」する役割を担います)
- 言語機能: **Python 3.x** (プロジェクト全体の開発に使用されているプログラミング言語とそのバージョン)
- 自動化・CI/CD: **Pythonスクリプトによる自動生成** (このシステム自体がリポジトリ一覧の自動生成という自動化を実現します。具体的なCI/CDパイプラインツールは直接明記されていませんが、GitHub Pagesへのデプロイなどで利用される可能性があります。)
- 開発標準: **ruff** (Pythonコードのスタイルチェックとフォーマットを自動的に行うためのリンター/フォーマッター)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
  📖 4.md
  📖 6.md
  📖 8.md
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

*   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
*   **`.github_automation/`**: GitHub Actionsなどと連携して自動化を行うためのスクリプトや設定を格納するディレクトリです。
    *   **`check_large_files/`**: 大容量ファイルをチェックするための機能関連ファイルを格納します。
        *   **`README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
        *   **`check-large-files.toml`**: 大容量ファイルチェックの設定（ファイルサイズの上限、除外パスなど）を定義するTOML形式のファイルです。
        *   **`scripts/check_large_files.py`**: 大容量ファイルを検出して警告またはエラーを出すためのPythonスクリプトです。
*   **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリ（例: ログファイル、一時ファイル、仮想環境など）を指定します。
*   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載しています。ソフトウェアの利用、配布、改変に関する条件を定めます。
*   **`README.md`**: プロジェクト全体の概要、セットアップ方法、実行コマンド、ライセンスなど、このプロジェクトに関する基本的な情報を提供します。
*   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
*   **`assets/`**: GitHub Pagesサイトで使用される画像やファビコンなどの静的アセットを格納するディレクトリです。
    *   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: 異なるサイズのファビコン（ウェブサイトのアイコン）画像ファイルです。
*   **`debug_project_overview.py`**: プロジェクト概要取得機能（`project_overview_fetcher.py`）のデバッグやテストを目的とした補助スクリプトです。
*   **`generated-docs/`**: 他のリポジトリから自動取得されたドキュメント（例: 各リポジトリの`project-overview.md`）が一時的に格納される可能性のあるディレクトリですが、現在のツリーでは空です。
*   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイルです。
*   **`index.md`**: このプロジェクトの`generate_repo_list.py`によって最終的に生成される、リポジトリ一覧を含むメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
*   **`issue-notes/`**: 開発中に発生した課題、検討事項、または特定のイシューに関するメモをMarkdown形式で格納するディレクトリです。
*   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリのメタデータ、ホーム画面への追加設定、表示オプションなどを定義します。
*   **`pytest.ini`**: `pytest`フレームワークのテスト実行に関する設定ファイルです。テストの検出方法、プラグイン、マーカーなどを定義します。
*   **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージとそのバージョンをリストアップします。
*   **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要なPythonパッケージとそのバージョンをリストアップします。
*   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
*   **`ruff.toml`**: Pythonコードのスタイルリンター/フォーマッターである`ruff`の設定ファイルです。コード品質と一貫性を維持するためのルールを定義します。
*   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    *   **`generate_repo_list/`**: リポジトリ一覧を生成するシステムの主要なPythonモジュール群を格納します。
        *   **`badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジ（アイコン）を生成する機能を提供します。
        *   **`config.yml`**: プロジェクト全体の動作パラメータや、`project_overview`機能などの詳細設定を定義するYAML形式の設定ファイルです。
        *   **`config_manager.py`**: `config.yml`や他の設定ファイルを読み込み、プログラム全体で利用可能な設定オブジェクトとして管理する機能を提供します。
        *   **`date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ機能を提供します。
        *   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールを呼び出して最終的なMarkdownファイルを生成する一連の処理を調整します。
        *   **`json_ld_template.json`**: SEO強化のためのJSON-LD形式の構造化データテンプレートを定義します。検索エンジンにコンテンツの意味を正確に伝達します。
        *   **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示するための機能を提供します。
        *   **`markdown_generator.py`**: 処理されたリポジトリ情報とバッジを用いて、Jekyll/GitHub Pages向けのMarkdown形式のコンテンツを生成するコアモジュールです。
        *   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動取得・抽出する機能を提供します。
        *   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を解析・抽出する機能を提供します。
        *   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を処理し、フィルタリング、ソート、必要な情報への変換、アクティブ・アーカイブ・フォークなどの分類を行う機能を提供します。
        *   **`seo_template.yml`**: SEO関連のメタデータや、Markdown生成時に使用される構造化された情報を定義するテンプレートファイルです。
        *   **`statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数、最終更新日など）を計算し、整形する機能を提供します。
        *   **`strings.yml`**: UIに表示される各種メッセージや文言を管理するYAML形式のファイルです。多言語対応や文言変更を容易にします。
        *   **`template_processor.py`**: Markdown生成時に使用されるテンプレート（`seo_template.yml`など）を処理し、動的なデータと結合する機能を提供します。
        *   **`url_utils.py`**: URLの生成、検証、パス操作など、URLに関連する共通ユーティリティ機能を提供します。
*   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールおよびその機能に関するテストスクリプトです。
*   **`tests/`**: プロジェクトのテストコードを格納するディレクトリです。
    *   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを実行するスクリプトです。
    *   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストスクリプトです。
    *   **`test_config.py`**: 設定管理モジュールのテストスクリプトです。
    *   **`test_date_formatter.py`**: 日付整形ユーティリティのテストスクリプトです。
    *   **`test_environment.py`**: 実行環境（依存関係など）のテストスクリプトです。
    *   **`test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストを実行するスクリプトです。
    *   **`test_markdown_generator.py`**: Markdown生成モジュールのテストスクリプトです。
    *   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストスクリプトです。
    *   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストスクリプトです。
    *   **`test_repository_processor.py`**: リポジトリ情報処理モジュールのテストスクリプトです。

## 関数詳細説明

*   **`generate_repo_list.py` 内の主要関数 (`main` 関数など)**
    *   **役割**: プロジェクトのエントリポイントです。コマンドライン引数を解析し、設定ファイルを読み込み、GitHub APIからリポジトリ情報を取得します。その後、取得したデータを処理し、Markdown生成モジュールを呼び出して最終的なリポジトリ一覧ファイルを作成します。
    *   **機能**: 引数解析、設定初期化、API呼び出し、データフロー制御、ファイル出力。

*   **`repository_processor.py` 内の主要関数 (`process_repositories` など)**
    *   **役割**: GitHub APIから取得した生のリポジトリデータのリストを受け取り、整形、フィルタリング、ソートを行います。また、リポジトリをアクティブ、アーカイブ、フォークなどのカテゴリに分類する処理を担当します。
    *   **機能**: データ構造変換、フィルタリングロジック適用、ソート、カテゴリ分類。

*   **`project_overview_fetcher.py` 内の主要関数 (`fetch_project_overview` など)**
    *   **役割**: 特定のGitHubリポジトリ内にある指定されたパスのファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出し、取得します。APIリクエストの失敗時にはリトライやキャッシュ機能も考慮されます。
    *   **機能**: ファイル内容の取得（HTTPリクエスト）、Markdown解析、特定セクションからのテキスト抽出、キャッシュ管理。

*   **`markdown_generator.py` 内の主要関数 (`generate_markdown` など)**
    *   **役割**: 処理済みのリポジトリ情報、バッジデータ、SEO関連情報など、様々なデータを組み合わせて、GitHub Pagesで表示される最終的なMarkdown形式のコンテンツを生成します。
    *   **機能**: テンプレートへのデータ挿入、Markdown形式での文字列構築、コンテンツの構造化。

*   **`badge_generator.py` 内の主要関数 (`generate_badge` など)**
    *   **役割**: リポジトリのプログラミング言語、最終更新日、ステータス（アーカイブなど）に基づいて、視覚的な情報を示すMarkdown形式のバッジ（例: Shields.io形式）文字列を生成します。
    *   **機能**: 条件に応じたバッジ文字列の生成、色やテキストのカスタマイズ。

*   **`config_manager.py` 内の主要関数 (`load_config` など)**
    *   **役割**: プロジェクトで使用されるYAML形式の設定ファイルを読み込み、設定値を辞書やオブジェクトとして提供します。これにより、設定の一元管理と変更が容易になります。
    *   **機能**: ファイルI/O、YAMLパース、デフォルト値の適用、設定値のアクセス。

*   **`date_formatter.py` 内の主要関数 (`format_date` など)**
    *   **役割**: 日付オブジェクトを受け取り、人間が読みやすい形式や、特定の表示形式（例: "YYYY年MM月DD日"）に整形した文字列を返します。
    *   **機能**: 日付オブジェクトのフォーマット、タイムゾーン変換（必要な場合）。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-13 07:10:52 JST
