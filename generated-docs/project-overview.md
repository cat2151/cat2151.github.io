Last updated: 2026-05-03

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・処理します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けに最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、リポジトリの検索エンジンからの発見性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesで静的サイトを構築するためのエンジンで、生成されたMarkdownファイルがこの上で動作します。
    - **Markdown**: サイトのコンテンツを記述するための軽量マークアップ言語。このプロジェクトではリポジトリ一覧をMarkdown形式で出力します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **GitHub API**: GitHub上のリポジトリ情報をプログラムから取得するためのインターフェースです。
    - **pytest**: Pythonアプリケーションのテストを効率的に行うためのフレームワークです。
    - **ruff**: Pythonコードのリンティングとフォーマットを高速に行うツールで、コード品質の維持に貢献します。
- テスト:
    - **pytest**: Pythonのテストフレームワークであり、ユニットテストや結合テストの記述・実行に使用されます。
- ビルドツール:
    - **Python**: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得からMarkdown生成までの一連の処理を実行します。
    - **Jekyll (静的サイトジェネレーション)**: 厳密には本プロジェクトの出力物が利用される環境ですが、最終的なWebサイトの「ビルド」を担う要素として重要です。
- 言語機能:
    - **Python**: このプロジェクトの全てのロジックはPythonで実装されており、強力なデータ処理能力と豊富なライブラリを活用しています。
- 自動化・CI/CD:
    - **GitHub Actions (関連)**: プロジェクト概要に「プロジェクトごとのGitHub Actions管理」の言及があり、`.github_automation` ディレクトリが存在することから、このシステムがGitHub Actions環境での自動化や、GitHub Actionsの設定ファイルの生成/管理に何らかの形で関与している可能性があります。
- 開発標準:
    - **ruff**: コードのスタイルを統一し、潜在的な問題を早期に発見するためのリンター/フォーマッタとして使用されます。
    - **.editorconfig**: 複数の開発者が異なるエディタを使用しても、コードのインデントスタイルなどの書式設定を統一するための設定ファイルです。

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
- **`.editorconfig`**: コードエディタの設定を定義し、プロジェクトに関わる全開発者間で一貫したコーディングスタイル（インデント、改行コードなど）を維持します。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定ファイルを格納するディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files` サブディレクトリの目的と使用法を説明するドキュメントです。
    - **`check_large_files/check-large-files.toml`**: 大きいファイルのチェックに関する設定を記述するファイルです。
    - **`check_large_files/scripts/check_large_files.py`**: 特定の閾値を超えるサイズのファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義します（例：生成された一時ファイル、環境設定ファイル）。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイルです。著作権、利用条件などが明記されています。
- **`README.md`**: プロジェクト全体の概要、目的、主な機能、使い方、開発者向けのヒントなどをまとめたメインのドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、ビルドオプションなどが定義されます。
- **`assets/`**: サイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用される可能性のあるスクリプトです。
- **`generated-docs/`**: 何らかのプロセスによって自動生成されたドキュメントやファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどの検索エンジンツールでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧がここに出力されます。
- **`issue-notes/`**: 課題やノート、メモなどを格納するためのディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（Issue #22など）に関する詳細な情報や議論が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを定義するファイルです。アプリの表示名、アイコン、起動URLなどをブラウザに伝えます。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の動作設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要となるPythonパッケージとそのバージョンを定義するファイルです。
- **`requirements.txt`**: プロジェクトの実行（本番環境など）に必要となるPythonパッケージとそのバージョンを定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしても良いか、あるいはクロールしてはいけないかを指示するファイルです。
- **`ruff.toml`**: `ruff`リンター/フォーマッタのルールや設定を定義するファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/generate_repo_list/`**: リポジトリ一覧を生成する機能に特化したモジュール群を格納するディレクトリです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジのMarkdownコードを生成するロジックを含みます。
        - **`src/generate_repo_list/config.yml`**: `generate_repo_list` スクリプトの動作に関する設定（APIリトライ数、タイムアウト、プロジェクト概要取得機能のON/OFFなど）を定義します。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理する役割を担います。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の形式に整形するための機能を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルとして出力するこのプロジェクトのメインスクリプトです。
        - **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートです。SEO強化のためにリポジトリ情報に付加される可能性があります。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語情報を解析し、詳細な情報を提供するモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報をもとに、Jekyllに適したMarkdown形式のコンテンツを生成するロジックを含みます。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの `README.md` などからバッジ情報を抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に必要な情報（カテゴリ分類、概要など）に整形する役割を担います。
        - **`src/generate_repo_list/seo_template.yml`**: SEO（検索エンジン最適化）を目的としたメタデータなどのテンプレート設定を定義します。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示される各種メッセージや文言を一元的に管理するためのファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成におけるテンプレートエンジンの処理（変数の埋め込みなど）を担当します。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築や解析など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関する単体テストや結合テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストコードが格納されるディレクトリです。
    - **`tests/conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義し、テスト間で共有するために使用されます。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    - **`tests/test_check_large_files.py`**: `check_large_files.py` スクリプトのテストを記述したファイルです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストを記述したファイルです。
    - **`tests/test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係のテストを記述したファイルです。
    - **`tests/test_integration.py`**: プロジェクトの主要コンポーネント間の連携に関する統合テストを記述したファイルです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
    - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストを記述したファイルです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: このスクリプトのエントリポイントです。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、情報の加工、Markdown生成、そして最終的なファイル出力までの一連の流れを制御します。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge_markdown()`: リポジトリのプログラミング言語やステータス（例：アーカイブ）を示すためのバッジを、Markdown形式で生成します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config()`: プロジェクトの各種設定（`config.yml`や`strings.yml`など）を読み込み、アプリケーション全体で利用可能な形で提供します。
- **`src/generate_repo_list/date_formatter.py`**
    - `format_date()`: 日付情報（例：リポジトリの最終更新日）をユーザーフレンドリーな形式（例：YYYY年MM月DD日）に整形します。
- **`src/generate_repo_list/language_info.py`**
    - `get_language_details()`: 特定のリポジトリで使用されているプログラミング言語に関する詳細情報を取得し、整理します。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_repository_entry()`: 個々のリポジトリの情報を基に、そのリポジトリ専用のMarkdown形式のエントリ（タイトル、概要、リンクなど）を生成します。
    - `generate_full_markdown()`: 全てのリポジトリのエントリを結合し、最終的なリポジトリ一覧のMarkdownコンテンツ全体を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview()`: 各リポジトリ内に存在する特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの要約（3行の説明）を抽出し取得します。
- **`src/generate_repo_list/repository_processor.py`**
    - `process_repository_data()`: GitHub APIから取得した生のリポジトリデータを、表示や分類に適した形に加工・整形する主要な処理を行います。
- **`src/generate_repo_list/statistics_calculator.py`**
    - `calculate_statistics()`: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算し、提供します。
- **`src/generate_repo_list/template_processor.py`**
    - `render_template()`: 指定されたテンプレートファイル（Markdownの一部など）に、動的に生成されたデータを埋め込み、最終的な出力を生成します。
- **`src/generate_repo_list/url_utils.py`**
    - `build_github_api_url()`: GitHub APIへアクセスするための適切なURLを、指定されたパラメータに基づいて構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-05-03 07:16:24 JST
