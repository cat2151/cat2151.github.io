Last updated: 2025-11-29

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、SEOに最適化されたMarkdown形式でリポジトリ情報を出力します。
- これにより、検索エンジンでの発見性を高め、LLMからの参照も容易にします。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして利用), **Markdown** (リポジトリ一覧の出力形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (スクリプトの実行環境), **pip** (依存ライブラリ管理), **VS Code** (`.editorconfig`, `ruff.toml`から推測される一般的な開発環境)
- テスト: **pytest** (Pythonコードのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ一覧の生成ロジックを実装)
- 言語機能: **Python** (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: **Pythonスクリプトによる自動生成** (GitHub APIからの情報取得とMarkdown生成のプロセス自体が自動化されています)
- 開発標準: **ruff** (Pythonコードのリンターおよびフォーマッタ), **.editorconfig** (IDEやエディタ間のコードスタイル統一設定)

## ファイル階層ツリー
```
📄 .editorconfig
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
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 2.md
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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載しています。
-   **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方、設定オプションなどを説明するメインドキュメントです。
-   **`_config.yml`**: Jekyllサイトの全体設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を定義します。
-   **`assets/`**: Jekyllサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（Webサイトのアイコン）の各サイズです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストを目的としたスクリプトです。
-   **`generated-docs/`**: 各リポジトリから取得した概要や生成されたドキュメントを配置するためのディレクトリです。
-   **`index.md`**: メインの出力ファイルであり、GitHub Pagesサイトで表示されるリポジトリ一覧のMarkdownコンテンツが生成されます。
-   **`issue-notes/`**: 開発中の課題や検討事項、メモなどを個別のMarkdownファイルとして記録しているディレクトリです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、Webアプリのメタデータ（名前、アイコン、表示モードなど）を定義します。
-   **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。テストの検出ルールやオプションなどを指定します。
-   **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの一覧を定義しています。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境用のPythonライブラリの一覧を定義しています。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Pythonのリンター兼フォーマッタであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
-   **`src/`**: プロジェクトのソースコードを格納するルートディレクトリです。
    -   **`src/__init__.py`**: `src`ディレクトリがPythonのパッケージであることを示します。
    -   **`src/generate_repo_list/`**: リポジトリ一覧を生成するメインロジックを含むパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonのサブパッケージであることを示します。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジのMarkdown文字列を生成するロジックを扱います。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得設定など、システムが使用する各種技術的パラメータを定義する設定ファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`や`strings.yml`など）を読み込み、管理するためのモジュールです。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの主要な実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用されるJSON-LD形式の構造化データテンプレートです。
        -   **`src/generate_repo_list/language_info.py`**: GitHub APIから取得したリポジトリの言語情報を処理し、表示に適した形式に整形するロジックを実装しています。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報から、最終的なMarkdownコンテンツ（リポジトリ一覧ページ）を生成する役割を担います。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出する機能を提供します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報に加工・整形するためのロジックを含んでいます。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや、検索エンジン向けのコンテンツ生成に使用されるテンプレート設定を定義します。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックです。
        -   **`src/generate_repo_list/strings.yml`**: サイトや生成されるコンテンツに表示される各種メッセージ、ラベル、文言などを一元管理するためのファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（文字列フォーマットなど）を処理し、動的なコンテンツを埋め込むためのユーティリティです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールに関連する単体テストを記述したファイルです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`test_config.py`**: 設定管理モジュール（`config_manager.py`）のテストを行います。
    -   **`test_environment.py`**: プロジェクトの実行環境（依存関係、ファイルパスなど）に関するテストを行います。
    -   **`test_integration.py`**: システムの各コンポーネントが連携して正しく動作するかを確認する統合テストです。
    -   **`test_markdown_generator.py`**: Markdown生成ロジック（`markdown_generator.py`）のテストを行います。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能（`project_overview_fetcher.py`）のテストを行います。
    -   **`test_repository_processor.py`**: リポジトリデータ処理ロジック（`repository_processor.py`）のテストを行います。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数名、その引数、戻り値、詳細な機能が記述されていないため、ハルシネーションを避けるため、個別の関数についての詳細な説明はできません。
ただし、各ファイルがその役割に応じた関数群を持っていることが推測されます。例えば、`generate_repo_list.py`にはメイン処理を制御する関数、`repository_processor.py`にはリポジトリデータを処理する関数、`markdown_generator.py`にはMarkdownコンテンツを生成する関数などが存在すると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-29 07:05:47 JST
