Last updated: 2026-02-10

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pagesサイト向けにMarkdownを自動生成します。
- 生成されたリポジトリ一覧はSEO最適化され、検索エンジンからの可視性を高めます。
- これにより、LLM（大規模言語モデル）によるリポジトリ参照の精度向上と開発効率の改善を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として静的サイトを生成・ホスティングします。生成されるMarkdownコンテンツはJekyllによって表示されます。)
- 音楽・オーディオ: 該当なし（このプロジェクトは音楽・オーディオ関連の技術を使用していません。）
- 開発ツール:
    - Python: プロジェクトの主要なロジックを実装するためのプログラミング言語です。GitHub APIからのデータ取得、加工、Markdown生成などに使用されます。
    - Git: ソースコードのバージョン管理システムです。
    - GitHub API: GitHubリポジトリの情報をプログラム的に取得するために利用されます。
- テスト: Pytest (Pythonで書かれたテストコードを実行するためのフレームワークで、プロジェクトの品質を保証します。)
- ビルドツール: 該当なし（一般的なビルドツールは使用せず、Pythonスクリプトが直接コンテンツを生成します。）
- 言語機能: Python (API連携、データ処理、ファイル操作、文字列処理などの言語機能が活用されています。)
- 自動化・CI/CD:
    - GitHub Pages: 静的サイトのデプロイとホスティングを自動化するGitHubの機能です。
    - `.github_automation`: カスタムの自動化スクリプトや設定を格納し、開発プロセスの一部を自動化します。
- 開発標準:
    - Ruff: Pythonコードのスタイルチェックとフォーマットを自動で行うツールで、コード品質と統一性を保ちます。
    - EditorConfig: 異なるエディタやIDE間でコードの書式設定を統一するためのファイル形式です。

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
- **`.editorconfig`**: 異なる開発環境間でコードのインデントスタイルや文字コードなどの書式設定を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明です。
    - **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義するファイルです。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定、ライセンスなど、プロジェクト全体の基本的な情報が記述されています。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: GitHub Pagesサイトで使用される画像、ファビコンなどの静的ファイルを格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要などのドキュメントを一時的に格納する、または最終的に生成されるドキュメントの出力先となりうるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のためのHTMLファイルです。
- **`index.md`**: このプロジェクトによって生成されるGitHub Pagesサイトのリポジトリ一覧メインページとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモがMarkdown形式で格納されているディレクトリです。
- **`manifest.json`**: Progressive Web App (PWA) の設定ファイルで、ホーム画面への追加やオフライン動作などを定義します。
- **`pytest.ini`**: PythonのテストフレームワークPytestの設定ファイルです。テストの発見方法や実行オプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行する際に必要なPythonライブラリの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールするか、しないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成のメインロジックが格納されているパッケージです。
        - **`__init__.py`**: `generate_repo_list` パッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリの言語や状態を示すバッジのMarkdownを生成するロジックが含まれています。
        - **`config.yml`**: プロジェクト概要の取得設定など、アプリケーション全体の動作に関する技術的なパラメータを定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml` などの設定ファイルを読み込み、管理するユーティリティです。
        - **`date_formatter.py`**: 日付や時刻のフォーマットを処理するためのユーティリティ関数が含まれています。
        - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプトです。GitHub APIから情報を取得し、最終的なMarkdownファイルを生成する一連の処理を調整します。
        - **`json_ld_template.json`**: 検索エンジン最適化のために使用されるJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、整形するロジックが含まれています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pagesに表示されるMarkdownコンテンツを構築する中心的なロジックが含まれています。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出し、取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報を抽出するロジックが含まれています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形に整形するロジックが含まれています。
        - **`seo_template.yml`**: SEO関連のメタデータやコンテンツの構造を定義するためのYAMLテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するロジックが含まれています。
        - **`strings.yml`**: プロジェクト全体で使用される表示メッセージや文言を一元的に管理するためのYAML形式のファイルです。
        - **`template_processor.py`**: Markdownや他の形式のテンプレートを読み込み、データに基づいて動的にコンテンツを生成するロジックが含まれています。
        - **`url_utils.py`**: URLの生成や解析など、URLに関連するユーティリティ関数が含まれています。
- **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストコードです。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストコードです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストコードです。
    - **`test_config.py`**: 設定ファイル読み込み・管理機能のテストコードです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストコードです。
    - **`test_environment.py`**: 実行環境に関するテストコードです。
    - **`test_integration.py`**: プロジェクト全体の主要な処理フローを検証する統合テストコードです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストコードです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストコードです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストコードです。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、主要なモジュールには以下のような役割を持つ関数が含まれています。具体的な引数や戻り値は記述しませんが、その機能について説明します。

- **`generate_repo_list.py`**:
    - `main()`: スクリプトのエントリポイントです。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といった一連の処理をオーケストレートします。
- **`badge_generator.py`**:
    - `generate_badge_markdown()`: リポジトリの言語やアーカイブ状態など、与えられた情報に基づいて、適切なバッジのMarkdownテキストを生成します。
- **`config_manager.py`**:
    - `load_config()`: 指定されたYAMLファイルから設定情報を読み込み、プログラムで利用できる形式で返します。
- **`date_formatter.py`**:
    - `format_date()`: 日付データを指定された形式の文字列に変換します。
- **`language_info.py`**:
    - `get_top_language()`: リポジトリの複数の言語情報から、主要な言語を特定します。
- **`markdown_generator.py`**:
    - `build_repository_list_markdown()`: 処理済みのリポジトリデータのリストを受け取り、GitHub Pages用のリポジトリ一覧を構成するMarkdownコンテンツ全体を生成します。
    - `build_repository_item_markdown()`: 個々のリポジトリ情報から、そのリポジトリの表示ブロックを構成するMarkdownテキストを生成します。
- **`project_overview_fetcher.py`**:
    - `fetch_project_overview()`: 指定されたGitHubリポジトリ内の特定のファイルから、プロジェクトの概要説明文（通常3行）を抽出し、取得します。
- **`readme_badge_extractor.py`**:
    - `extract_badges_from_readme()`: リポジトリの `README.md` の内容を解析し、含まれているバッジのURLやテキスト情報を抽出します。
- **`repository_processor.py`**:
    - `process_repository_data()`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な要素（説明、言語、最終更新日など）を抽出し、整形します。
- **`statistics_calculator.py`**:
    - `calculate_star_count()`: リポジトリのスター数を計算または取得します。
- **`template_processor.py`**:
    - `render_template()`: テンプレートファイルと動的なデータを受け取り、データをテンプレートに埋め込んで最終的なコンテンツ（Markdownなど）を生成します。
- **`url_utils.py`**:
    - `generate_github_repo_url()`: GitHubのユーザー名とリポジトリ名から、リポジトリのURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-10 07:14:34 JST
