Last updated: 2025-12-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で収集・整理します。
- 収集した情報からGitHub Pages用のSEO最適化されたリポジトリ一覧を自動生成します。
- これにより、リポジトリの検索エンジン可視性を高め、LLMによる参照の改善を目指します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: 生成されるGitHub Pagesサイトの静的サイトジェネレータ基盤です。
    - **Markdown**: 生成されるリポジトリ一覧ページの出力形式として使用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語として、スクリプトの作成に使用されます。
    - **Git**: ソースコードのバージョン管理と共同開発に使用されます。
- テスト:
    - **Pytest**: Pythonプロジェクトのテストフレームワークとして、コードの品質と機能の検証に使用されます。
- ビルドツール:
    - **Python**: 生成スクリプト自体が、GitHub APIから取得したデータに基づいてMarkdownファイルを構築（ビルド）する役割を担います。
- 言語機能:
    - **Python**: 汎用プログラミング言語としての機能が活用されます。
- 自動化・CI/CD: 該当する技術はありません。このプロジェクトはGitHub Pagesへのデプロイを目的としますが、CI/CDプロセス自体はこのプロジェクトの技術スタックには含まれません。
- 開発標準:
    - **Ruff**: Pythonコードのフォーマットと静的解析を行い、コードの一貫性と品質を保つために使用されます。

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイルとフォーマットを統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリ（一時ファイル、ビルド成果物、秘密情報など）を指定します。
- **`LICENSE`**: このプロジェクトのライセンス（MITライセンス）に関する情報が記載されています。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を含みます。
- **`assets/`**: ウェブサイトのアセット（画像、アイコン、CSS、JavaScriptなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各種サイズを提供します。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストを行うための補助スクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（例: 各リポジトリの個別のプロジェクト概要）を格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスにおけるサイトの所有権確認に使用されるファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このファイルに自動生成されたリポジトリ一覧が表示されます。
- **`issue-notes/`**: プロジェクト開発中に発生した課題や検討事項を記録したメモが格納されるディレクトリです。
    - **`10.md`, `12.md`, `14.md`, `2.md`, `4.md`, `6.md`, `8.md`**: 個々の課題やメモの詳細を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルで、テストの実行オプションや挙動を定義します。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonパッケージとそのバージョンをリストアップします。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンをリストアップします。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットを行う`ruff`ツールの設定ファイルで、コードスタイルルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータス（例: アクティブ、アーカイブ）に応じたバッジの生成や管理を担うモジュールです。
        - **`config.yml`**: GitHub APIからのリポジトリ情報取得や、各リポジトリのプロジェクト概要取得機能に関する技術的パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`やシークレットファイルなど）を読み込み、管理するモジュールです。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成します。
        - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために構造化データ（JSON-LD）を生成する際のテンプレートファイルです。
        - **`language_info.py`**: 各リポジトリの主要なプログラミング言語に関する情報を取得し、処理するモジュールです。
        - **`markdown_generator.py`**: 取得および処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出・取得するモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理に適した形式に変換するモジュールです。
        - **`seo_template.yml`**: 検索エンジン最適化(SEO)に関連するメタデータや記述のテンプレートおよび設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数など、各種統計情報を計算するモジュールです。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言（例: ヘッダー、フッターテキスト）を一元管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に、Liquidなどのテンプレートエンジンを利用した動的なコンテンツ埋め込み処理を担うモジュールです。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数群を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するための単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_config.py`**: `config_manager.py`など、設定ファイルの読み込みや管理に関するモジュールをテストします。
    - **`test_environment.py`**: テスト実行環境（依存関係、設定など）が適切に設定されているかを検証するテストです。
    - **`test_integration.py`**: 複数のモジュールが連携して期待通りに動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールが正しいMarkdownコンテンツを生成するかをテストします。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールがプロジェクト概要を正しく抽出できるかをテストします。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールがリポジトリデータを正しく処理・整形できるかをテストします。

## 関数詳細説明
現在、プロジェクト情報からは具体的な関数の詳細情報（役割、引数、戻り値など）は提供されていません。`googled947dc864c270e07.html`ファイルには関数が含まれていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-31 07:06:08 JST
