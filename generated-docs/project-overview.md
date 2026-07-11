Last updated: 2026-07-12

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- 各リポジトリの情報を取得し、SEOに最適化されたMarkdown形式のページを自動的に生成します。
- 検索エンジンからの発見性を高め、人工知能によるリポジトリ参照を支援することを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイト構築エンジン)、Markdown (コンテンツ記述言語)
- 音楽・オーディオ: 該当なし
- 開発ツール: Ruff (PythonコードのLinter/Formatter)、Pytest (Pythonテストフレームワーク)
- テスト: Pytest (Pythonテストフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報取得からMarkdown生成までを自動化)
- 言語機能: Python (プロジェクトの主要な実装言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報の取得に利用)
- 開発標準: Ruff (コードスタイルの一貫性保持)

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコードスタイルの一貫性を保つための設定を定義します。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。特に `check_large_files` は、リポジトリ内の大規模ファイルを検出する機能を持っています。
-   **`.gitignore`**: Gitがバージョン管理の対象から外すファイルやディレクトリを指定します。
-   **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すファイルです。
-   **`README.md`**: プロジェクト全体の概要、セットアップ方法、使い方などを説明する主要なドキュメントファイルです。
-   **`_config.yml`**: Jekyllサイト全体の挙動を設定するファイルで、テーマ、プラグイン、URL構造などを定義します。
-   **`assets/`**: Jekyllサイトで使用される画像、アイコン（`favicon`など）、CSS、JavaScriptといった静的ファイルを格納するディレクトリです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能（`project_overview_fetcher`）のデバッグを補助するためのスクリプトです。
-   **`generated-docs/`**: 自動生成されたドキュメントや、外部から取得して格納されるドキュメントを配置するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用されるファイルです。
-   **`index.md`**: このプロジェクトによって生成されるリポジトリ一覧の出力先となるMarkdownファイルで、Jekyllサイトのトップページとして機能します。
-   **`issue-notes/`**: 開発中の課題や検討事項に関するメモを記録するためのMarkdownファイルが格納されるディレクトリです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブサイトをモバイルデバイスのホーム画面に追加する際の挙動などを定義します。
-   **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定を記述するファイルです。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージの一覧を定義します。
-   **`requirements.txt`**: プロジェクトの実行に必要となる基本的なPythonパッケージの一覧を定義します。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいは避けるべきかを指示するファイルです。
-   **`ruff.toml`**: Pythonのコードスタイルを統一・整形するツール「Ruff」の設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        -   **`badge_generator.py`**: リポジトリの特性（例：言語、ステータス）を示すバッジのMarkdownを生成するロジックを含みます。
        -   **`config.yml`**: プロジェクト概要取得機能など、システム全体の技術的なパラメータを設定するファイルです。
        -   **`config_manager.py`**: 設定ファイルを読み込み、アプリケーション全体で利用可能な設定を管理する役割を担います。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を実行します。
        -   **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ形式であるJSON-LDのテンプレートを提供します。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、整形します。
        -   **`markdown_generator.py`**: Jekyllの要件に合わせたMarkdown形式のコンテンツを効率的に生成するロジックを含みます。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイルから、そのリポジトリの3行概要を自動的に取得する機能を実装しています。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、プロジェクトのステータスや技術を示すバッジ情報を抽出します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整理する中心的なロジックです。
        -   **`seo_template.yml`**: 生成されるページに適用されるSEO関連のメタデータや設定を定義するテンプレートファイルです。
        -   **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（例：スター数、フォーク数）を計算する機能を提供します。
        -   **`strings.yml`**: アプリケーション内で使用される表示メッセージ、ラベル、文言などを一元的に管理するファイルです。
        -   **`template_processor.py`**: Markdown生成時に使用されるテンプレートの読み込みや変数置換といった処理を行います。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能の単体テストスクリプトです。
-   **`tests/`**: プロジェクト全体の自動テストスクリプトを格納するディレクトリです。

## 関数詳細説明
-   **`src/generate_repo_list/generate_repo_list.py`内の主要関数**:
    -   役割: プログラムのエントリポイントであり、リポジトリ情報の取得、処理、最終的なMarkdown生成の一連の流れを統括します。
    -   機能: コマンドライン引数を解析し、他のモジュールと連携してGitHubリポジトリ一覧のMarkdownファイルを生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`内の主要関数**:
    -   役割: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要説明を自動的に取得します。
    -   機能: GitHub APIを介してファイルコンテンツを読み込み、指定された形式の概要説明を抽出します。キャッシュ機能も備えています。
-   **`src/generate_repo_list/markdown_generator.py`内の主要関数**:
    -   役割: 処理されたリポジトリ情報と定義されたテンプレートに基づき、Jekyllに適したMarkdown形式のコンテンツを生成します。
    -   機能: 各リポジトリの情報を整形し、SEOに適したメタデータやバッジを含んだ最終的なMarkdownテキストを出力します。
-   **`src/generate_repo_list/repository_processor.py`内の主要関数**:
    -   役割: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形します。
    -   機能: リポジトリのフィルタリング（アクティブ、アーカイブ、フォークなど）、言語情報の集計、概要情報の紐付けなどを行います。
-   **`src/generate_repo_list/config_manager.py`内の主要関数**:
    -   役割: プロジェクト全体で使用される設定ファイル（`config.yml`、`strings.yml`など）を読み込み、管理します。
    -   機能: 必要な設定値をロードし、他のモジュールが簡単にアクセスできる形で提供します。
-   **`src/generate_repo_list/badge_generator.py`内の主要関数**:
    -   役割: リポジトリの属性（例: 使用言語、開発状況）を示すための視覚的なバッジをMarkdown形式で生成します。
    -   機能: 特定のリポジトリ情報に基づいて、適切なバッジのURLと代替テキストを含むMarkdownスニペットを作成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-07-12 07:18:50 JST
