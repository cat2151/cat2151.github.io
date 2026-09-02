Last updated: 2026-09-03

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（`<username>.github.io`）用に、リポジトリ一覧ページと各リポジトリへのリンクを自動生成します。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを自動で作成することで、検索エンジンからの発見性を高めます。
- 各リポジトリの概要（`project-overview.md`）も自動で抽出し、魅力的な一覧表示を実現し、開発効率向上と情報アクセスを支援します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages): 静的サイトジェネレーター。本システムで生成されたMarkdownファイルを元に、ウェブサイトを構築・公開するために利用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからの情報取得、データ処理、Markdown生成など、システムの中核を担います。
    - **GitHub API**: リポジトリ情報（名前、説明、言語、スター数など）をプログラム的に取得するために使用されます。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml` など）やSEOテンプレート (`seo_template.yml`) の記述に使用され、設定の管理を容易にします。
    - **VS Code (`.editorconfig`)**: 開発環境におけるコードスタイルの統一を支援するための設定ファイルが提供されています。
- テスト:
    - **pytest**: Pythonアプリケーションのテストを効率的に記述・実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報を元にMarkdownファイルを生成する主要な「ビルド」処理を実行します。
    - **Jekyll**: 生成されたMarkdownコンテンツをウェブサイトとして構築する静的サイトジェネレーターとして機能します。
- 言語機能:
    - **Markdown**: リポジトリ一覧や各リポジトリの情報表示に利用される、軽量なマークアップ言語です。本システムはこの形式のファイルを生成します。
    - **JSON-LD**: SEOを強化するための構造化データ形式。リポジトリ情報にメタデータを付与し、検索エンジンにより正確な情報を提供します。
- 自動化・CI/CD:
    - **GitHub Actions (`.github_automation/` ディレクトリ)**: リポジトリ内の大規模ファイルをチェックするスクリプト (`check_large_files.py`) など、自動化されたタスクの実行基盤として利用される可能性があります。
- 開発標準:
    - **Ruff**: Pythonコードのリンティング（構文チェック）とフォーマット（コード整形）を行うツール。コード品質の維持と統一されたコーディングスタイルを保証します。

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コードなどの基本的なコードスタイルを統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェックツールに関する説明が記載されています。
    -   **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定を定義するファイルです。
    -   **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の過度に大きなファイルを検出し、管理するPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです。
-   **`LICENSE`**: このプロジェクトがMITライセンスで公開されていることを示すライセンス条項ファイルです。
-   **`README.md`**: プロジェクトの目的、機能、セットアップ方法、実行コマンドなど、概要を説明するメインのドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の共通設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
-   **`assets/`**: ウェブサイトで使用される静的なアセット（画像、ファビコンなど）を格納するディレクトリです。
    -   **`assets/favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像ファイルです。
-   **`debug_project_overview.py`**: `project_overview_fetcher.py` のデバッグや単体テストを目的としたスクリプトの可能性があります。
-   **`generated-docs/`**: システムによって生成されるドキュメントや、各リポジトリから取得されるプロジェクト概要（`project-overview.md`）などが格納されることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認のために配置される認証ファイルです。
-   **`index.md`**: Jekyllサイトのルートページとして機能するMarkdownファイルです。本システムによって生成されたリポジトリ一覧がここに出力されます。
-   **`issue-notes/22.md`**: 開発中の特定の課題に関するメモや詳細情報が記述されているファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるマニフェストファイルで、アプリ名やアイコンなどの情報を定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。
-   **`requirements-dev.txt`**: 開発時やテスト実行時に必要となるPythonのライブラリとそのバージョンをリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonのライブラリとそのバージョンをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいは避けるべきかを指示するファイルです。
-   **`ruff.toml`**: Pythonのコードリンター/フォーマッターであるRuffの設定を定義するファイルです。コーディング規約の自動適用に利用されます。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧を生成する機能に特化したモジュールです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示すファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジ画像を生成または整形するロジックが含まれています。
        -   **`src/generate_repo_list/config.yml`**: `generate_repo_list` モジュールの動作設定（例：プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: システムの設定ファイル（`config.yml`, `strings.yml` など）を読み込み、管理する役割を担います。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するユーティリティ関数を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: このシステムのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdownファイルを生成します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のため、リポジトリ情報を構造化データ（JSON-LD）として埋め込む際のテンプレートです。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語に関する情報を処理し、表示に適した形式に変換する機能を提供します。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得および処理されたリポジトリ情報から、実際にMarkdown形式のコンテンツを生成するロジックが含まれています。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出・取得する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出する機能を提供します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に必要な形式に整形・フィルタリングする主要な処理ロジックです。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや、生成されるページのテンプレート設定を定義するYAMLファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能です。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元的に管理するための設定ファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用される様々なテンプレート（Jinja2などのテンプレートエンジン）を処理するユーティリティ機能です。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得と解析）を検証するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトが格納されているディレクトリです。
    -   **`tests/conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    -   **`tests/test_badge_generator_integration.py`**: `badge_generator.py` の機能が他のモジュールと連携して正しく動作するかを検証する統合テストです。
    -   **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` の機能を検証するためのテストスクリプトです。
    -   **`tests/test_config.py`**: 設定ファイル (`config.yml`など) の読み込みや設定管理が正しく機能するかを検証するテストです。
    -   **`tests/test_date_formatter.py`**: `date_formatter.py` の日付フォーマット機能が正しく動作するかを検証するテストです。
    -   **`tests/test_environment.py`**: 開発・実行環境のセットアップや依存関係が正しく構成されているかを検証するテストです。
    -   **`tests/test_integration.py`**: システム全体のエンドツーエンドの統合テストであり、主要な機能が連携して期待通りに動作するかを検証します。
    -   **`tests/test_markdown_generator.py`**: `markdown_generator.py` のMarkdown生成ロジックが正しく機能するかを検証するテストです。
    -   **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` の機能（プロジェクト概要の抽出）が正しく動作するかを検証するテストです。
    -   **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のREADMEからバッジを抽出する機能が正しく動作するかを検証するテストです。
    -   **`tests/test_repository_processor.py`**: `repository_processor.py` のリポジトリデータ処理ロジックが正しく機能するかを検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には、個別の関数の詳細な役割、引数、戻り値に関する情報が含まれていません。しかし、各ファイルの役割から、以下の主要な機能を持つ関数が存在すると推測されます。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **メイン実行関数 (`main` など)**: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、他のモジュールを呼び出してMarkdownファイルを生成する、システム全体の実行フローを制御する役割を担います。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   **リポジトリ処理関数 (`process_repository_data` など)**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報（名前、説明、言語、スター数など）を抽出し、表示に適した形式に整形・フィルタリングする機能を提供します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **プロジェクト概要取得関数 (`fetch_project_overview` など)**: 指定されたリポジトリとファイルパス（例: `generated-docs/project-overview.md`）に基づいて、そのファイルからプロジェクトの3行概要を抽出し、文字列として返す機能を提供します。APIリクエストやファイル読み込み、テキスト解析が含まれます。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **Markdown生成関数 (`generate_markdown_content` など)**: 整形されたリポジトリデータやその他の情報を元に、指定されたテンプレートを用いて最終的なMarkdown形式の文字列を生成する役割を担います。
-   **`src/generate_repo_list/badge_generator.py`**:
    -   **バッジ生成関数 (`create_badge` など)**: リポジトリのプロパティ（例：言語、アクティビティ）に基づいて、Markdown形式で表示可能なバッジのコードを生成する機能を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-09-03 07:12:18 JST
