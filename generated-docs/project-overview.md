Last updated: 2026-05-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、GitHub Pages (Jekyllベース) 向けのSEO最適化されたリポジトリ一覧Markdownを生成します。
- これにより、GitHub Pagesサイトの検索エンジンからのクロールを促進し、リポジトリの可視性を向上させます。

## 技術スタック
- フロントエンド:
    - **GitHub Pages (Jekyll)**: 生成されたMarkdownファイルをホストし、ウェブサイトとして公開するためのプラットフォーム。Jekyllは静的サイトジェネレータです。
    - **Markdown**: リポジトリ一覧や個々のリポジトリ概要を表示するために、本システムが自動生成する軽量マークアップ言語です。
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、GitHub APIからの情報取得、Markdown生成ロジックの実装に使用されます。
    - **GitHub API**: GitHubリポジトリのメタデータをプログラム的に取得するために使用されるインターフェースです。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、設定や表示文言を一元管理します。
    - **TOML**: GitHubトークンなどの機密情報を含む設定ファイル (`secrets.toml`) の記述に使用される設定ファイル形式です。
    - **Git**: プロジェクトのソースコード管理に使用される分散型バージョン管理システムです。
- テスト:
    - **pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py` を中心としたPythonスクリプト群が、GitHub APIからのデータ取得、加工、Markdownファイルの生成という一連の「ビルド」プロセスを実行します。
- 言語機能:
    - **Python言語機能**: f-strings、データ構造（リスト、辞書）、ファイルI/O、モジュール管理など、Pythonが提供する豊富な言語機能と標準ライブラリが利用されています。
- 自動化・CI/CD:
    - **Pythonスクリプトによる自動生成**: GitHub ActionsなどのCI/CDツールは明示的に利用されていませんが、Pythonスクリプト自体がリポジトリ一覧の自動生成という自動化されたプロセスを提供します。
    - **GitHub Automation (check_large_files)**: Gitリポジトリ内の大容量ファイルをチェックする自動化スクリプトが含まれています。
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックと自動フォーマットを行うリンター兼フォーマッターです。コード品質と一貫性を保ちます。
    - **EditorConfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。

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
-   **`.editorconfig`**: コードエディタの設定を定義し、プロジェクト全体で一貫したコーディングスタイルを維持するためのファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリです。
    -   **`check_large_files/README.md`**: `.github_automation`内の「大容量ファイルチェック」機能についての説明ドキュメントです。
    -   **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するTOML形式のファイルです。
    -   **`scripts/check_large_files.py`**: Gitリポジトリ内の指定されたサイズを超えるファイルを検出するPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを記述するファイルです。
-   **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス条項ファイルです。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法、開発者向け情報などを説明する主要なドキュメントです。
-   **`_config.yml`**: JekyllによってGitHub Pagesサイトを構築する際の全体設定を定義するファイルです。
-   **`assets/`**: ウェブサイトで使用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリです。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の様々なサイズを格納しています。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py` の機能) をデバッグするための補助スクリプトです。
-   **`generated-docs/`**: 本システムによって生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を認証するために使用されるHTMLファイルです。
-   **`index.md`**: GitHub Pagesサイトのトップページとして表示されるMarkdownファイルで、生成されたリポジトリ一覧がここに出力されます。
-   **`issue-notes/`**: 課題やメモを管理するためのディレクトリです。
    -   **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモや検討事項を記述したMarkdownファイルです。
-   **`manifest.json`**: ウェブサイトをプログレッシブウェブアプリ (PWA) として機能させるためのメタデータを提供するファイルです。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。
-   **`requirements-dev.txt`**: 開発時やテスト時に必要となるPythonの外部ライブラリを記述したファイルです。
-   **`requirements.txt`**: プロジェクトの実行（本番運用）に必要となるPythonの外部ライブラリを記述したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールして良いか、またはクロールしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定を定義するTOML形式のファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示す空ファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧生成機能の中核となるPythonモジュール群が格納されています。
        -   **`__init__.py`**: `generate_repo_list`がPythonパッケージであることを示す空ファイルです。
        -   **`badge_generator.py`**: リポジトリのステータスや情報を示すバッジ（例：言語、スター数など）を生成するロジックを扱います。
        -   **`config.yml`**: プロジェクト概要取得機能など、本システムの技術的なパラメータや動作設定を定義するYAML形式のファイルです。
        -   **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        -   **`date_formatter.py`**: リポジトリの作成日や更新日などの日付情報を整形し、表示に適した形式に変換する機能を提供します。
        -   **`generate_repo_list.py`**: 本システムのメインエントリスクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理を統括します。
        -   **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために構造化データを埋め込むJSON-LDのテンプレートファイルです。
        -   **`language_info.py`**: リポジトリが使用しているプログラミング言語に関する情報を処理し、表示に役立つデータに変換します。
        -   **`markdown_generator.py`**: 取得・加工したリポジトリ情報から、実際にMarkdown形式のコンテンツを生成するロジックを担います。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内に存在する `generated-docs/project-overview.md` ファイルから、リポジトリの3行概要を自動的に取得する機能を提供します。
        -   **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例：CI/CDステータス、カバレッジなど）を抽出する機能を提供します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、本システムで扱いやすいように加工・整形する役割を担います。
        -   **`seo_template.yml`**: ページのタイトルやディスクリプションなど、SEOに関連するメタ情報を定義するテンプレートです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計する機能を提供します。
        -   **`strings.yml`**: UIに表示されるメッセージ、ラベル、案内文など、様々な文字列定数を一元的に管理するYAML形式のファイルです。多言語対応の基盤にもなり得ます。
        -   **`template_processor.py`**: Markdown生成時に使用されるテンプレート（文字列）内のプレースホルダーに変数を埋め込むなど、テンプレート処理を行います。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: pytestにおいて、複数のテストファイルで共通して使用されるフィクスチャ（テストデータやセットアップ関数）を定義するためのファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator.py`の機能が他のモジュールと連携して正しく動作するかを確認する結合テストです。
    -   **`test_check_large_files.py`**: `.github_automation`内の大容量ファイルチェック機能のテストスクリプトです。
    -   **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや管理が正しく行われるかを検証するテストです。
    -   **`test_date_formatter.py`**: `date_formatter.py`の日付整形機能が期待通りに動作するかを検証するテストです。
    -   **`test_environment.py`**: テスト実行環境や依存関係が適切に設定されているかを検証するテストです。
    -   **`test_integration.py`**: 本システムの主要なエンドツーエンドのフローが正しく機能するかを検証する統合テストです。
    -   **`test_markdown_generator.py`**: `markdown_generator.py`が正しいMarkdown形式の出力を生成するかを検証するテストです。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`が各リポジトリから概要を正しく取得できるかを検証するテストです。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`がREADMEからバッジ情報を正確に抽出できるかを検証するテストです。
    -   **`test_repository_processor.py`**: `repository_processor.py`がGitHub APIからのデータを正しく処理・整形できるかを検証するテストです。

## 関数詳細説明
現在、詳細な関数情報（各関数の役割、引数、戻り値など）は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-08 07:27:25 JST
