Last updated: 2026-01-06

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定されたユーザーのリポジトリ情報を自動で取得します。
- 取得した情報から、JekyllベースのGitHub Pages向けにSEO最適化されたリポジトリ一覧をMarkdown形式で自動生成します。
- これにより、プロジェクトの発見性を高め、検索エンジンやLLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用される静的サイトジェネレータ), Markdown (リポジトリ一覧の出力形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報を取得するためのインターフェース)
- テスト: pytest (Pythonコードの単体・統合テストフレームワーク)
- ビルドツール: PyYAML (YAML設定ファイルの解析に使用), requests (HTTP通信によるGitHub APIへのアクセスに使用)
- 言語機能: Python (汎用プログラミング言語。ファイル操作、文字列処理、データ構造操作などで利用)
- 自動化・CI/CD: GitHub Pages (生成されたコンテンツのホスティング環境), Pythonスクリプト自体が情報の自動取得と生成を行う
- 開発標準: Ruff (Pythonコードの高速なLinterおよびFormatter), .editorconfig (異なるエディタ間でのコードスタイルの一貫性を保つための設定)

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
🌐 googled947dc864c270e07.html
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
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
    📄 date_formatter.py
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
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコードスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理システムが追跡しないファイルやディレクトリを指定します。一時ファイルや依存関係などが含まれます。
- **LICENSE**: プロジェクトのライセンス情報（この場合はMITライセンス）を明記しており、ソフトウェアの利用、配布、変更に関する条件を定義します。
- **README.md**: プロジェクトの概要、目的、設定方法、使い方、開発者向け情報などが記載された主要なドキュメントファイルです。
- **_config.yml**: JekyllベースのGitHub Pagesサイト全体のグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **assets/**: Webサイトで使用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: ブラウザのタブやブックマークに表示されるウェブサイトのファビコン（アイコン）ファイルです。様々なサイズが用意されています。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールのデバッグや単体テストを行うための補助スクリプトです。
- **generated-docs/**: 他のリポジトリから取得した「プロジェクト概要」などのドキュメントが一時的に保存されたり、生成されたドキュメントの参照元となるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置される特殊なHTMLファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして表示されるMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧がここに配置されます。
- **issue-notes/**: 開発中に発生した課題や検討事項、設計メモなどをMarkdown形式で記録するディレクトリです。
    - **[番号].md**: 個別の課題やメモの詳細が記述されたファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリのホーム画面アイコン、表示モード、起動URLなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイルです。テストの検出方法や実行オプションが指定されます。
- **requirements-dev.txt**: 開発環境やテスト実行時にのみ必要となるPythonパッケージとそのバージョンをリストアップするファイルです。
- **requirements.txt**: プロジェクトの実行（本番環境）に最低限必要となるPythonパッケージとそのバージョンをリストアップするファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールしないようにするかを指示するファイルです。
- **ruff.toml**: Pythonコードの整形と品質チェックを行う`Ruff`ツールの設定ファイルです。コーディング規約やリンティングルールが定義されています。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成するための主要なロジックをまとめたPythonサブパッケージです。
        - **__init__.py**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリの言語やライセンスなどの情報を元に、バッジ（小さなアイコンやラベル）を生成する機能を提供します。
        - **config.yml**: リポジトリ一覧生成スクリプト固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）を定義するファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、設定値へのアクセスを管理するモジュールです。
        - **date_formatter.py**: 日付や時刻の情報を特定の形式に整形するユーティリティ関数を提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownコンテンツを生成する処理全体を制御します。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のため、JSON-LD形式の構造化データを生成するためのテンプレートファイルです。
        - **language_info.py**: GitHubリポジトリから取得したプログラミング言語の利用状況や割合を処理・分析する機能を提供します。
        - **markdown_generator.py**: 取得・整形されたリポジトリデータに基づいて、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成するロジックを実装しています。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
        - **seo_template.yml**: サイトのSEO（検索エンジン最適化）関連のメタデータや、Jekyllサイトに組み込むためのテンプレート設定を定義するファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIメッセージ、見出し、説明文など、アプリケーション内で使用される各種テキスト文字列を一元管理するための設定ファイルです。
        - **template_processor.py**: Markdownコンテンツ生成時に、特定のプレースホルダーを実際のデータに置き換えるなどのテンプレート処理を行います。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関する一般的なユーティリティ機能を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能を検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **test_config.py**: 設定管理モジュール（`config_manager.py`など）の機能を検証するテストです。
    - **test_date_formatter.py**: 日付フォーマットモジュール（`date_formatter.py`）の機能を検証するテストです。
    - **test_environment.py**: プロジェクトの実行環境や依存関係が正しく設定されているかを検証するテストです。
    - **test_integration.py**: 複数のモジュールが連携して正しく動作するかを確認する統合テストです。
    - **test_markdown_generator.py**: Markdown生成モジュール（`markdown_generator.py`）が正しいMarkdownを出力するかを検証するテストです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得モジュール（`project_overview_fetcher.py`）の機能を検証するテストです。
    - **test_repository_processor.py**: リポジトリ処理モジュール（`repository_processor.py`）の機能を検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には具体的な関数の説明が含まれていないため、詳細な説明はできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-06 07:06:40 JST
