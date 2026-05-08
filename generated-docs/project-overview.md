Last updated: 2026-05-09

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のリポジトリ情報を自動で収集・整理します。
- 収集した情報から、検索エンジン最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- これにより、GitHub Pagesサイトの可視性を高め、リポジトリの発見性を向上させることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用)、Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: (このプロジェクトでは該当する技術を使用していません)
- 開発ツール: Python (主要な開発言語)、Git (バージョン管理)、GitHub (リポジトリホスティングとAPI連携)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Pythonスクリプト (自身がMarkdown形式のファイルを生成するカスタムビルドツール)
- 言語機能: Python (スクリプト言語としての機能、ファイル操作、HTTP通信など)、YAML (設定ファイルの記述)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリの存在から、CI/CDワークフローの可能性)
- 開発標準: ruff (Pythonコードの高速リンター/フォーマッター)、.editorconfig (エディタ間のコーディングスタイル統一)

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
-   **`.editorconfig`**: 異なる開発環境やエディタ間で、インデントや文字コードなどのコーディングスタイルを統一するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    -   **`check-large-files.toml`**: 大容量ファイルチェックの設定ファイル。チェック対象のファイルサイズ閾値などを定義。
    -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを記述するファイル。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   **`README.md`**: プロジェクトの目的、機能、使い方、開発者向けのヒントなどを説明する主要なドキュメント。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定ファイル。サイトのタイトルやテーマなどを定義。
-   **`assets/`**: サイトで利用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    -   **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるファビコン画像ファイル。複数のサイズが用意されている。
-   **`debug_project_overview.py`**: 各リポジトリからプロジェクト概要を自動取得する機能のデバッグ用途で利用されるスクリプト。
-   **`generated-docs/`**: 自動生成されたドキュメントやデータが格納されることを意図したディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイル。
-   **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイル。GitHub Pagesのトップページとして表示される。
-   **`issue-notes/22.md`**: 特定のイシュー（課題）に関するメモや詳細を記述したファイル。
-   **`manifest.json`**: ウェブサイトをプログレッシブウェブアプリ（PWA）として動作させるための設定ファイル。ホーム画面アイコン、表示モードなどを定義。
-   **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの挙動をカスタマイズする。
-   **`requirements-dev.txt`**: プロジェクトの開発時やテスト実行時に必要となるPythonパッケージとそのバージョンを定義するファイル。
-   **`requirements.txt`**: プロジェクトの実行（本番環境）に必要となるPythonパッケージとそのバージョンを定義するファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいは避けるべきかを指示するファイル。
-   **`ruff.toml`**: Pythonのコードリンター・フォーマッターである `ruff` の設定ファイル。コードスタイルのルールを定義。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧生成システムの核心部分を含むPythonパッケージ。
        -   **`badge_generator.py`**: リポジトリの技術スタックやステータスを示すバッジ画像を生成または準備するモジュール。
        -   **`config.yml`**: `generate_repo_list` システムの実行時設定（例：GitHub APIのタイムアウト、キャッシュ設定など）を定義するファイル。
        -   **`config_manager.py`**: YAML形式の設定ファイル（`config.yml`など）を読み込み、管理するためのモジュール。
        -   **`date_formatter.py`**: GitHub APIから取得した日付情報を、表示に適した形式に変換するユーティリティモジュール。
        -   **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIを呼び出し、リポジトリ情報を処理し、最終的なMarkdownファイルを生成する。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレート。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を取得・処理するモジュール。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報から、SEOを考慮したMarkdown形式のコンテンツを生成するロジックをカプセル化。
        -   **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要を自動的に取得する機能を提供するモジュール。
        -   **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報（例: ビルドステータス、ライセンス）を抽出するモジュール。
        -   **`repository_processor.py`**: GitHub APIからリポジトリ情報を取得し、それを整形・フィルタリングして、Markdown生成に適したデータ構造に変換する主要なロジック。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレートに関する設定を定義するファイル。
        -   **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュール。
        -   **`strings.yml`**: 生成されるMarkdownコンテンツ内の各種メッセージや文言を一元管理するためのファイル（多言語対応の可能性も含む）。
        -   **`template_processor.py`**: Markdown生成時に使用するテンプレート（例：JekyllのLiquid構文）を処理するためのモジュール。
        -   **`url_utils.py`**: URLの操作や検証に役立つユーティリティ関数を提供するモジュール。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能に関する単体テストスクリプト。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`conftest.py`**: `pytest` のテストフィクスチャ（テストの前処理や後処理を定義する機能）を配置するためのファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator` の機能が他のモジュールと連携して正しく動作するかを確認する統合テスト。
    -   **`test_check_large_files.py`**: `check_large_files.py` スクリプトの機能に関するテスト。
    -   **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや管理が正しく行われるかを確認するテスト。
    -   **`test_date_formatter.py`**: `date_formatter` モジュールの日付変換機能に関するテスト。
    -   **`test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係が正しく機能するかを確認するテスト。
    -   **`test_integration.py`**: プロジェクトの主要なフローが全体として正しく動作するかを確認する統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator` モジュールが意図したMarkdownコンテンツを生成するかを確認するテスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールがリポジトリ概要を正しく取得するかを確認するテスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールがREADMEからバッジ情報を正しく抽出するかを確認するテスト。
    -   **`test_repository_processor.py`**: `repository_processor` モジュールがGitHubリポジトリ情報を正しく処理するかを確認するテスト。

## 関数詳細説明
このプロジェクトの情報からは、個々の具体的な関数のシグネチャ（引数、戻り値）や詳細な実装は提供されていません。しかし、ファイル名とその役割から、主要なモジュールが持つであろう機能的な関数群を推測することができます。

-   **`generate_repo_list.py`**:
    -   **`main()`**: プロジェクトのエントリーポイントとなる関数。GitHub APIからリポジトリ情報を取得し、他のモジュールを協調させてMarkdownファイルを生成する一連の処理を統括します。
    -   **`parse_arguments()`**: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、スクリプトの実行に必要な設定を取得します。
-   **`repository_processor.py`**:
    -   **`fetch_repositories(username, token)`**: 指定されたユーザー名とGitHubトークンを使用して、GitHub APIからリポジトリ情報のリストを取得します。
    -   **`process_repository_data(repo_list)`**: 取得した生のリポジトリデータを、必要な情報（名前、説明、言語、スター数など）に整形・フィルタリングします。
-   **`markdown_generator.py`**:
    -   **`generate_markdown(processed_data, template)`**: 整形されたリポジトリデータとテンプレートを基に、最終的なリポジトリ一覧のMarkdown文字列を生成します。
    -   **`format_repository_entry(repo)`**: 個々のリポジトリ情報をMarkdown形式の一項目として整形します。
-   **`project_overview_fetcher.py`**:
    -   **`get_project_overview(repo_url, config)`**: 指定されたリポジトリURLから、設定ファイルに定義されたパスの `project-overview.md` を読み込み、3行の概要を抽出します。
-   **`badge_generator.py`**:
    -   **`create_badge_url(language)`**: プログラミング言語などの情報に基づき、バッジ画像（例：Shields.ioなど）のURLを生成します。

これらの関数は、それぞれのモジュールの責任範囲内で特定のタスクを実行し、プロジェクト全体のリポジトリ一覧生成フローを構成しています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-09 07:24:00 JST
