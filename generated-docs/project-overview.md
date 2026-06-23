Last updated: 2026-06-24

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得するシステムです。
- 取得した情報から、SEOに最適化されたGitHub Pages (Jekyll) サイト用のMarkdown形式リポジトリ一覧を生成します。
- 各リポジトリの概要を自動抽出し表示することで、検索エンジンやLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして利用), **Markdown** (生成されるコンテンツ形式)
- 音楽・オーディオ: なし
- 開発ツール: **Python** (スクリプト言語、主要なロジックの実装に使用), **requests** (HTTPクライアント、GitHub APIとの通信に使用), **PyYAML** (YAMLファイルのパースに使用), **toml** (TOMLファイルのパースに使用), **BeautifulSoup4/lxml** (HTML/XMLパース、プロジェクト概要の抽出に使用)
- テスト: **pytest** (Python用テストフレームワーク)
- ビルドツール: なし (Pythonスクリプト自体がMarkdownを生成する「ビルド」の役割を果たす)
- 言語機能: **Python** (データ処理、ファイル操作、Web API連携など)
- 自動化・CI/CD: なし (現在の構成ではローカルでの開発・実行が重視されており、CI/CDパイプラインは明示されていませんが、`.github_automation` ディレクトリから将来的な自動化の可能性が示唆されます)
- 開発標準: **ruff** (Pythonコードのリンターおよびフォーマッター)

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
-   **`.editorconfig`**: エディタの設定ファイル。複数の開発者間でコードのスタイル（インデント、改行コードなど）を統一するために使用されます。
-   **`.github_automation/check_large_files/README.md`**: `.github_automation` ディレクトリ内の大規模ファイルチェック機能に関する説明ドキュメントです。
-   **`.github_automation/check_large_files/check-large-files.toml`**: 大規模ファイルチェック機能の設定ファイルです。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大規模ファイルを検出し、管理を補助するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   **`README.md`**: プロジェクトの概要、目的、使用方法、設定、開発者向けのヒントなどを記述した、プロジェクトの入口となるドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。GitHub PagesでJekyllを使用する際に読み込まれます。
-   **`assets/`**: faviconなどの静的アセットを格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイルです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
-   **`generated-docs/`**: 自動生成されたドキュメント（主に各リポジトリの `project-overview.md` など）が格納される可能性があるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために使用される認証ファイルです。
-   **`index.md`**: メインのPythonスクリプトによって生成される、リポジトリ一覧を含むGitHub Pagesサイトのトップページ（インデックス）ファイルです。
-   **`issue-notes/22.md`**: 特定のイシュー（課題）に関するメモや詳細情報が記述されたファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するマニフェストファイルです。ホーム画面に追加する際のアプリ名、アイコンなどを指定します。
-   **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの発見方法や実行オプションなどを定義します。
-   **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonの依存ライブラリをリストしたファイルです。
-   **`requirements.txt`**: プロジェクトが本番環境で実行される際に必要となるPythonの依存ライブラリをリストしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンター兼フォーマッターである `ruff` の設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
-   **`src/`**: プロジェクトのソースコードが格納されるルートディレクトリです。
    -   **`src/__init__.py`**: Pythonパッケージとして `src` ディレクトリを認識させるための空ファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを含むパッケージディレクトリです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための空ファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種情報に基づいてバッジ（例：言語、ステータス）を生成する機能を提供します。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの実行時パラメータや設定を定義するYAML形式の設定ファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル (`config.yml` など) を読み込み、管理するためのモジュールです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するユーティリティ機能を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: リポジトリ一覧生成システムのエントリーポイントとなるメインスクリプトです。GitHub APIからデータを取得し、Markdownを生成する全体の処理フローを制御します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートファイルです。SEOのためにリポジトリ情報などをマークアップする際に使用されます。
        -   **`src/generate_repo_list/language_info.py`**: プロジェクトで使用されているプログラミング言語に関する情報（例：アイコン、色）を管理・提供するモジュールです。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータから、最終的なMarkdown形式のコンテンツを生成するロジックを提供します。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリから `project-overview.md` ファイルをフェッチし、そこからプロジェクト概要の3行説明を抽出する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルなどから特定のバッジ情報を抽出する機能を提供します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に整形・加工する主要なロジックを実装しています。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや設定を定義するテンプレートファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する各種統計情報（例：スター数、フォーク数）を計算する機能を提供します。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するYAML形式のファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: Markdownなどのテンプレートファイルを読み込み、動的なデータで埋め込む処理を行うモジュールです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、正規化など、URLに関連するユーティリティ機能を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールに関連するテストケースを記述したファイルです。
-   **`tests/`**: プロジェクト全体のテストコードが格納されるディレクトリです。
    -   **`tests/conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義するファイルです。
    -   **`tests/test_badge_generator_integration.py`**: `badge_generator` の統合テストを行うファイルです。
    -   **`tests/test_check_large_files.py`**: 大規模ファイルチェック機能のテストを行うファイルです。
    -   **`tests/test_config.py`**: 設定ファイル (`config.yml`) の読み込みや設定管理に関するテストを行うファイルです。
    -   **`tests/test_date_formatter.py`**: 日付フォーマットユーティリティのテストを行うファイルです。
    -   **`tests/test_environment.py`**: 実行環境に関するテストを行うファイルです。
    -   **`tests/test_integration.py`**: プロジェクト全体の主要な機能の統合テストを行うファイルです。
    -   **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを行うファイルです。
    -   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うファイルです。
    -   **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを行うファイルです。
    -   **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うファイルです。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、各ファイルが特定の機能を担当する関数群を持っています。コードが直接提供されていないため、具体的な関数名、引数、戻り値は記述できませんが、各モジュールが提供する主要な機能の役割を以下に示します。

-   **`generate_repo_list.py`**:
    -   **主要な実行フローを制御する関数**: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、その情報を他のモジュールに渡して処理させ、最終的にMarkdownファイルを生成する一連の流れを管理します。
-   **`config_manager.py`**:
    -   **設定を読み込む関数**: YAMLやTOML形式の設定ファイルを読み込み、プロジェクト全体で利用可能な設定オブジェクトを提供します。
-   **`repository_processor.py`**:
    -   **リポジトリデータを処理する関数**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報（説明、言語、最終更新日など）を抽出し、Markdown生成に適した形式に整形します。内部で `project_overview_fetcher` や `badge_generator` などの機能と連携します。
-   **`project_overview_fetcher.py`**:
    -   **プロジェクト概要を取得する関数**: 指定されたリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、定義されたセクション（例: "プロジェクト概要"）の3行の説明を抽出し、返します。必要に応じてネットワークリクエストを行います。
-   **`markdown_generator.py`**:
    -   **Markdownコンテンツを生成する関数**: 処理済みのリポジトリ情報とテンプレート（`seo_template.yml`, `json_ld_template.json`など）を用いて、GitHub Pages用の最終的なMarkdownファイルを構築します。
-   **`badge_generator.py`**:
    -   **バッジを生成する関数**: リポジトリのプログラミング言語、アーカイブ状態、フォーク状態などに基づいて、表示用のバッジ（例: Markdown形式の画像リンク）を作成します。
-   **`date_formatter.py`**:
    -   **日付をフォーマットする関数**: 日付オブジェクトや文字列を受け取り、ユーザーフレンドリーな形式や特定のMarkdown形式の日付文字列に変換します。
-   **`url_utils.py`**:
    -   **URL関連のユーティリティ関数**: GitHubリポジトリのURLやGitHub PagesのURLなど、プロジェクト内で使用される各種URLを生成、検証、または加工します。

これらの関数は、互いに連携し、GitHubリポジトリ情報の取得からMarkdownファイル生成までの一連の自動化プロセスを構成しています。

## 関数呼び出し階層ツリー
```
main (generate_repo_list.py)
├── read_configuration (config_manager.py)
├── fetch_github_repositories (requestsライブラリを利用)
├── for each repository:
│   ├── process_repository_data (repository_processor.py)
│   │   ├── fetch_project_overview (project_overview_fetcher.py)
│   │   ├── generate_badges (badge_generator.py)
│   │   ├── format_date (date_formatter.py)
│   │   └── (other data processing and utility functions)
│   └── generate_markdown_section (markdown_generator.py)
└── write_output_file (file I/O)

---
Generated at: 2026-06-24 07:30:45 JST
