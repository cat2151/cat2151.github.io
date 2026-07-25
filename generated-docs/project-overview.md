Last updated: 2026-07-26

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、検索エンジンに最適化されたMarkdownファイルを自動で作成します。
- これにより、リポジトリの可視性を高め、情報参照を容易にすることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesをベースとした静的サイト生成に使用されるフレームワーク)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要な開発言語。スクリプトの実行環境として使用), GitHub API (リポジトリ情報の取得元として利用)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: なし (直接的なビルドツールは使用せず、Pythonスクリプトで生成処理を実行)
- 言語機能: Python (スクリプト全体の記述に使用されるプログラミング言語), YAML (設定ファイルの記述), Markdown (出力されるリポジトリ一覧ファイルのフォーマット)
- 自動化・CI/CD: GitHub Actions (リポジトリ自動化スクリプトの実行基盤として利用される可能性を想定)
- 開発標準: Ruff (Pythonコードの整形と品質管理ツール), EditorConfig (異なるエディタ間でのコーディングスタイル統一を支援)

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/README.md`**: `.github_automation/check_large_files` ディレクトリの目的や使い方を説明するドキュメントです。
    -   **`check-large-files.toml`**: リポジトリ内の大容量ファイルをチェックするためのツールの設定ファイルです。
    -   **`scripts/check_large_files.py`**: リポジトリ内の特定のファイルが設定されたサイズ制限を超えていないかをチェックするPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを指定するファイルです。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの概要、機能、セットアップ方法、使用方法などを説明する主要なドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。GitHub Pagesの基本的な動作を制御します。
-   **`assets/`**: ウェブサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリです。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   **`debug_project_overview.py`**: 各リポジトリのプロジェクト概要を取得する機能のデバッグや単体テストを目的としたスクリプトです。
-   **`generated-docs/`**: `project-overview.md` など、プロジェクトによって自動生成されたドキュメントやデータが一時的に配置されることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのウェブサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: このプロジェクトによってGitHubリポジトリ一覧が生成され、GitHub Pagesのメインページとして表示されるMarkdownファイルです。
-   **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモや考察を記述したMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを提供するマニフェストファイルで、アプリのホーム画面アイコンや表示モードなどを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するためのファイルです。
-   **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしても良いか、またはクロールしてはならないかを指示するファイルです。
-   **`ruff.toml`**: PythonのLinterおよびフォーマッターであるRuffの設定ファイルで、コードスタイルや品質管理のルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`__init__.py`**: Pythonがこのディレクトリをパッケージとして認識するために必要なファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧を生成するメインロジックを含むパッケージです。
        -   **`__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
        -   **`badge_generator.py`**: リポジトリの技術スタックや状態を示すバッジ（例: 使用言語）を生成する機能を提供します。
        -   **`config.yml`**: `generate_repo_list`パッケージ固有の設定パラメータを定義するYAMLファイルです。
        -   **`config_manager.py`**: アプリケーション全体の設定ファイル（`config.yml`や`strings.yml`など）を読み込み、管理する役割を担います。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する主要な実行スクリプトです。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためにウェブページに構造化データを提供するJSON-LD形式のテンプレートです。
        -   **`language_info.py`**: 各リポジトリの主要言語や使用されている言語に関する情報を処理・整形するロジックを扱います。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成する機能を提供します。
        -   **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要説明を抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス）を抽出するロジックです。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換する役割を担います。
        -   **`seo_template.yml`**: 検索エンジン最適化に関連するメタデータやテンプレート構造を定義するYAMLファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
        -   **`strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、その他のテキスト文字列を一元的に管理するYAMLファイルです。
        -   **`template_processor.py`**: MarkdownやHTMLのテンプレートを処理し、動的なデータを埋め込む機能を提供します。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher`モジュール（プロジェクト概要取得機能）のテストコードを格納しています。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャ（テストのための準備や後処理を行う関数）やヘルパー関数を定義します。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を確認するためのテストコードです。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストコードです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能のテストコードです。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテストコードです。
    -   **`test_environment.py`**: 実行環境の依存関係や設定に関するテストコードです。
    -   **`test_integration.py`**: プロジェクトの主要コンポーネントが連携して正しく動作するかを確認する結合テストコードです。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテストコードです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
    -   **`test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能のテストコードです。
    -   **`test_repository_processor.py`**: リポジトリデータ処理機能のテストコードです。

## 関数詳細説明
このプロジェクトでは、Pythonスクリプトとして機能が提供されていますが、提供されたプロジェクト情報には個々の関数の具体的な詳細（役割、引数、戻り値など）が記述されていませんでした。そのため、個別の関数の詳細な説明はここでは提供できません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-26 07:20:06 JST
