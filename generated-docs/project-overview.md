Last updated: 2026-06-03

# Project Overview

## プロジェクト概要
- GitHub APIを利用して、GitHub Pagesサイトのリポジトリ一覧を自動生成するシステムです。
- SEOに最適化されたMarkdownファイルを生成し、ウェブサイトの発見性を高めます。
- 各リポジトリの概要を自動取得し、検索エンジンやLLMからの参照性を改善します。

## 技術スタック
- フロントエンド:
    - GitHub Pages: 静的サイトホスティングサービス。JekyllをベースにMarkdownファイルをHTMLに変換し公開します。
    - Jekyll: GitHub Pagesで利用される静的サイトジェネレータ。本プロジェクトが生成するMarkdownコンテンツを処理します。
    - Markdown: プロジェクトがGitHub Pages向けに生成するコンテンツの記述言語です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: プロジェクトの主要開発言語であり、リポジトリ情報取得とMarkdown生成スクリプトが記述されています。
    - GitHub API: GitHubのリポジトリ情報をプログラム的に取得するために使用されます。
- テスト:
    - pytest: Pythonのテストフレームワークで、プロジェクトの機能が正しく動作することを確認するためのテストが記述されています。
- ビルドツール:
    - Pythonスクリプト: GitHub APIから取得した情報に基づき、Markdownファイルを生成する主要な処理を実行します。
- 言語機能:
    - Python: オブジェクト指向プログラミング、ファイルI/O、HTTPリクエスト処理などをサポートする汎用プログラミング言語。
- 自動化・CI/CD:
    - GitHub Actions: (間接的に) 各リポジトリの `generated-docs/project-overview.md` を作成する際に利用される可能性のあるワークフロー管理ツール。本システム自体がこの環境で動作することも想定されます。
- 開発標準:
    - ruff: Pythonコードのリンティングとフォーマットを高速に行うツールで、コード品質と統一性を保ちます。

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
- **`.editorconfig`**: 異なる開発環境間でのコーディングスタイル (インデント、改行コードなど) の統一を定義する設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `.github_automation/check_large_files` ディレクトリ内の機能、特に大きなファイルのチェックに関する説明が記述されています。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大きなファイルをチェックするスクリプトの設定を定義するファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きなファイルを検出し、管理を補助するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義します。ビルド生成物や一時ファイルなどが含まれます。
- **`LICENSE`**: プロジェクトのライセンス情報が記述されています。本プロジェクトはMITライセンスで公開されています。
- **`README.md`**: プロジェクト全体の概要、目的、主な機能、使い方、開発者向けのヒントなどが記述された、プロジェクトの玄関口となるファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
- **`assets/favicon-*.png`**: ウェブサイトのファビコン (ブラウザのタブやブックマークに表示されるアイコン) 画像ファイル群です。様々なサイズに対応しています。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 各リポジトリのプロジェクト概要 (project-overview.md) が配置される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: 本プロジェクトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定の課題やタスクに関するメモ、調査結果、または議論を記録したMarkdownファイルです。
- **`manifest.json`**: Progressive Web App (PWA) の設定ファイルで、ウェブアプリの表示モード、アイコン、テーマカラーなどを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出パターン、プラグインなどを指定します。
- **`requirements-dev.txt`**: 開発時やテスト実行時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行される際に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。コードスタイルルール、無視するエラーなどを定義します。
- **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: GitHubリポジトリの言語やスター数などの情報に基づき、マークダウン形式のバッジを生成するロジックが含まれています。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプト固有の設定（例：`project_overview` 機能の有効化、ターゲットファイルパスなど）を定義するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル (`config.yml`, `strings.yml` など) を読み込み、管理するためのクラスや関数を提供します。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットで文字列に変換するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、それを処理して最終的なMarkdownファイルを生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD形式) のテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語に関する情報を処理し、表示に適した形式に変換するロジックを含みます。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報とテンプレートを使用して、最終的なMarkdownコンテンツを構築する責任を担います。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動的に取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報（例：CI/CDステータス、バージョン情報）を抽出するためのロジックです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を、システムで使いやすい形式に加工、フィルタリング、整理する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータや記述のテンプレートを定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算または集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージ、ラベル、その他の固定文言を一元的に管理するためのYAMLファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートを読み込み、動的なデータで埋め込んで最終的な文字列を生成する役割を持ちます。
- **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URL操作に関連する汎用的なユーティリティ関数を集約したモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能が正しく動作するかを検証するテストスクリプトです。
- **`tests/conftest.py`**: pytestフレームワーク用の設定ファイルで、テスト間で共有されるフィクスチャやヘルパー関数を定義します。
- **`tests/test_badge_generator_integration.py`**: `badge_generator.py` が他のモジュールと連携して正しく機能するかを検証する統合テストスクリプトです。
- **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` スクリプトの機能を検証するテストです。
- **`tests/test_config.py`**: 設定ファイル (`config.yml` など) の読み込み、解析、値の取得が正しく行われるかを検証するテストです。
- **`tests/test_date_formatter.py`**: `date_formatter.py` モジュールの日付フォーマット機能が意図通りに動作するかを検証するテストです。
- **`tests/test_environment.py`**: プロジェクトの実行環境や依存関係が正しく設定されているかを検証するテストです。
- **`tests/test_integration.py`**: プロジェクトの主要なコンポーネントが連携して全体として正しく機能するかを検証する統合テストです。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py` モジュールが正しくMarkdownコンテンツを生成するかを検証するテストです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールのプロジェクト概要取得機能の正確性を検証するテストです。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` モジュールがREADMEファイルからバッジ情報を正しく抽出するかを検証するテストです。
- **`tests/test_repository_processor.py`**: `repository_processor.py` モジュールのリポジトリ情報処理機能の正確性を検証するテストです。

## 関数詳細説明
提供された情報では個別の関数に関する詳細な説明が不足しているため、主要なファイルにおける役割から一般的な関数機能を推測して説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連のワークフローをオーケストレートします。
    -   `_parse_arguments()`: コマンドライン引数を定義・解析し、ユーザー名や出力ファイル名、リミット数などを取得します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_repositories(username, token, limit=None)`: 指定されたGitHubユーザーのリポジトリをGitHub APIから取得します。トークンを用いて認証し、必要に応じて取得数を制限します。
    -   `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、整形し、アクティブ、アーカイブ、フォークなどのカテゴリに分類します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `get_project_overview(repo_full_name, file_path, config)`: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出し、返却します。キャッシュやリトライ設定も考慮されます。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown(repositories, templates, strings, config)`: 処理済みのリポジトリ情報、各種テンプレート、表示文言、設定情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badges(language_stats)`: リポジトリの言語統計情報を受け取り、それぞれの言語に対応するバッジのMarkdown文字列を生成します。
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
    -   `load_strings(strings_path)`: 指定されたパスからYAML形式の文字列定義ファイルを読み込み、多言語対応や文言の一元管理に利用します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-03 07:44:56 JST
