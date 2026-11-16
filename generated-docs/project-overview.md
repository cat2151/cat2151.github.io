Last updated: 2026-11-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHub APIを活用しリポジトリ一覧を自動生成するシステムです。
- リポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを自動出力します。
- これにより、リポジトリの検索性向上とLLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータ), **Markdown** (生成されるリポジトリ一覧の表示形式)
- 音楽・オーディオ: なし
- 開発ツール: **Python** (スクリプト言語として主要な処理を実行), **GitHub API** (リポジトリ情報を取得するためのインターフェース), **YAML** (設定ファイル `config.yml`, `strings.yml` などに利用), **TOML** (シークレット設定ファイル `secrets.toml` に利用)
- テスト: **pytest** (Pythonコードのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報の取得、加工、Markdown生成の一連の処理)
- 言語機能: **Python** (プロジェクトの主要な実装言語)
- 自動化・CI/CD: **GitHub Pages** (生成されたサイトをホスティングし公開するプラットフォーム)
- 開発標準: **ruff** (Pythonコードのフォーマットとリンティングツール)

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

*   **.editorconfig**: プロジェクト全体のコードスタイル（インデント、改行コードなど）を定義し、異なるエディタ間での統一を保証します。
*   **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関するスクリプトや設定を格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルを検出するための自動化スクリプト群です。
        *   **check-large-files.toml**: 大容量ファイルチェックの設定ファイルです。
        *   **scripts/check_large_files.py**: 大容量ファイルを検知し、レポートするためのPythonスクリプトです。
*   **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
*   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載しています。
*   **README.md**: プロジェクトの概要、機能、使い方、開発者向けのヒントなどを説明するメインのドキュメントです。
*   **_config.yml**: Jekyllのサイト全体の設定ファイルです。GitHub Pagesのサイト挙動を制御します。
*   **assets/**: Webサイトで使用される静的ファイル（画像、ファビコンなど）を格納するディレクトリです。
*   **debug_project_overview.py**: `project_overview` 機能（各リポジトリ概要の取得）を個別にデバッグするためのスクリプトです。
*   **generated-docs/**: 各リポジトリの `project-overview.md` など、生成されたドキュメントを一時的に格納するためのディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認のためのHTMLファイルです。
*   **index.md**: `generate_repo_list.py` スクリプトによって生成されるリポジトリ一覧のメインMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
*   **issue-notes/22.md**: 開発中に発生した特定の課題やメモを記録するファイルです。
*   **manifest.json**: プログレッシブウェブアプリ（PWA）をサポートするためのウェブマニフェストファイルです。
*   **pytest.ini**: `pytest` のテスト実行に関する設定ファイルです。
*   **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を定義します。
*   **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係を定義します。
*   **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールして良いか、または拒否するかを指示するファイルです。
*   **ruff.toml**: Pythonコードのリンター・フォーマッターである `ruff` の設定ファイルです。
*   **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    *   **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するパッケージです。
        *   **badge_generator.py**: リポジトリのステータス（アーカイブ、フォークなど）に応じたバッジの情報を生成する機能を提供します。
        *   **config.yml**: リポジトリ一覧生成に関する技術的パラメータ（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）を定義する設定ファイルです。
        *   **config_manager.py**: 設定ファイル（`config.yml`, `secrets.toml` など）の読み込みと管理を行うモジュールです。
        *   **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ機能を提供します。
        *   **generate_repo_list.py**: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力します。
        *   **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
        *   **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、整形する機能を提供します。
        *   **markdown_generator.py**: 取得したリポジトリ情報やプロジェクト概要を基に、最終的なMarkdownコンテンツを生成する機能を提供します。
        *   **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        *   **readme_badge_extractor.py**: リポジトリの `README.md` から特定のバッジ情報を抽出する機能を提供します。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリ情報を、システムで扱いやすい形式に加工・処理する機能を提供します。
        *   **seo_template.yml**: SEOに関するメタ情報や記述のテンプレートを定義する設定ファイルです。
        *   **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        *   **strings.yml**: UIメッセージや表示文言を一元管理するための設定ファイルです。
        *   **template_processor.py**: Markdown生成時に使用されるテンプレートの読み込みや変数の置き換えなど、テンプレート処理全般を担う機能を提供します。
        *   **url_utils.py**: URLの生成や整形など、URL関連のユーティリティ機能を提供します。
*   **test_project_overview.py**: `project_overview_fetcher.py` の機能を検証するための単体テストスクリプトです。
*   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    *   **conftest.py**: `pytest` のテスト実行時に共通で使用されるフィクスチャや設定を定義します。
    *   **test_badge_generator_integration.py**: バッジ生成機能の統合テストです。
    *   **test_check_large_files.py**: 大容量ファイルチェック機能のテストです。
    *   **test_config.py**: 設定ファイル（`config.yml` など）の読み込みや処理に関するテストです。
    *   **test_date_formatter.py**: 日付整形機能のテストです。
    *   **test_environment.py**: 実行環境のセットアップや依存関係に関するテストです。
    *   **test_integration.py**: 主要なモジュール間の連携を検証する統合テストです。
    *   **test_markdown_generator.py**: Markdown生成機能のテストです。
    *   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストです。
    *   **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストです。
    *   **test_repository_processor.py**: リポジトリ情報処理機能のテストです。

## 関数詳細説明

本プロジェクトでは、`src/generate_repo_list/generate_repo_list.py` がメインの実行スクリプトとなります。
このスクリプトは、以下の主要な機能を持つ関数（またはモジュール内の主要関数）を呼び出して処理を進めます。

*   **`main()` (src/generate_repo_list/generate_repo_list.py)**
    *   **役割**: プログラムのエントリポイント。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成・出力する一連の処理を統括します。
    *   **引数**: コマンドライン引数（`--username`, `--output`, `--limit`など）
    *   **戻り値**: なし
    *   **機能**:
        1.  設定（GitHubトークンなど）の読み込み。
        2.  指定されたユーザー名のリポジトリ一覧をGitHub APIから取得。
        3.  各リポジトリに対して `repository_processor` を呼び出し、詳細情報を加工。
        4.  `project_overview_fetcher` を呼び出し、各リポジトリの概要を取得。
        5.  `markdown_generator` を呼び出し、整形された情報からMarkdownコンテンツを生成。
        6.  生成されたMarkdownを指定された出力ファイルに書き出す。

*   **`fetch_project_overview(repo_name)` (src/generate_repo_list/project_overview_fetcher.py 内)**
    *   **役割**: 特定のリポジトリの `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を抽出します。
    *   **引数**: `repo_name` (string): 概要を取得したいリポジトリ名。
    *   **戻り値**: `overview_text` (string): 抽出されたプロジェクト概要。取得できなかった場合は空文字列。
    *   **機能**:
        1.  指定されたリポジトリの特定パスにある `project-overview.md` ファイルの内容を読み込む。
        2.  Markdownの「プロジェクト概要」セクションから3行の説明をパースして抽出する。
        3.  API呼び出しのキャッシュやリトライ処理を管理する。

*   **`process_repository(repo_data)` (src/generate_repo_list/repository_processor.py 内)**
    *   **役割**: GitHub APIから取得した個々のリポジトリの生データを、Markdown生成に適した形式に加工・整形します。
    *   **引数**: `repo_data` (dict): GitHub APIから取得した単一リポジトリのデータ。
    *   **戻り値**: `processed_data` (dict): 処理され、整形されたリポジトリデータ。
    *   **機能**:
        1.  リポジトリ名、説明、URL、スター数、フォーク数、最終更新日などの主要情報を抽出。
        2.  リポジトリの言語情報を処理し、表示可能な形式に変換。
        3.  アクティブ、アーカイブ、フォークなどのリポジトリステータスを判定。
        4.  必要な場合は `badge_generator` などを呼び出し、バッジ情報を追加。

*   **`generate_markdown(repos_data)` (src/generate_repo_list/markdown_generator.py 内)**
    *   **役割**: 処理済みの複数のリポジトリデータと、それぞれのプロジェクト概要を結合し、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    *   **引数**: `repos_data` (list of dict): 処理済みリポジトリデータのリスト。
    *   **戻り値**: `markdown_content` (string): 生成されたMarkdown形式の文字列。
    *   **機能**:
        1.  SEOテンプレートやJSON-LDテンプレートを適用。
        2.  各リポジトリの情報をループ処理し、Markdown形式で整形。
        3.  アクティブ、アーカイブ、フォークなどのカテゴリでリポジトリを分類し、見出しを付けて表示。
        4.  プロジェクト概要、バッジ、リンクなどを適切に埋め込む。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├── config_manager.load_config()
├── repository_processor.fetch_all_repositories()  (GitHub API呼び出しを含む)
│   └── language_info.get_language_info()
├── project_overview_fetcher.fetch_project_overview()
├── markdown_generator.generate_markdown()
│   ├── template_processor.apply_template()
│   ├── badge_generator.generate_badge()
│   └── date_formatter.format_date()
└── output_file.write()
```

（注: 上記の関数呼び出し階層は、プロジェクトのコード構造と説明から推測した主要な処理フローを示しています。具体的な引数やモジュール内の関数名は一般的な命名規則に基づいています。詳細な分析はプロジェクトのソースコード解析が必要です。）

---
Generated at: 2026-11-17 07:07:39 JST
