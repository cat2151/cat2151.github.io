Last updated: 2026-04-19

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEOを意識したMarkdownファイルを自動出力します。
- 検索エンジンやLLMからのリポジトリ参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesで静的サイトを構築するためのジェネレータ), Markdown (生成されるページの記述形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用していません。
- 開発ツール: Ruff (Pythonコードの自動整形と静的解析ツール), GitHub API (リポジトリ情報の取得元として利用)
- テスト: Pytest (Python製のテスティングフレームワーク)
- ビルドツール: このプロジェクトはPythonスクリプトで直接ファイルを生成するため、特定のビルドツールは使用していません。
- 言語機能: Python (主要なスクリプト言語として使用)
- 自動化・CI/CD: GitHub Pagesのビルド (`_config.yml`を通じてJekyllのビルドをトリガー)
- 開発標準: Ruff (コードスタイルの一貫性を保つためのルール定義)

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
- **`.editorconfig`**: 異なるエディタ間でコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルを検出するためのツール群を格納しています。
        - **`README.md`**: `check_large_files`ツールの説明ドキュメントです。
        - **`check-large-files.toml`**: `check_large_files`ツールの設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルをチェックするためのPythonスクリプト本体です。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバル設定ファイルです。サイトのタイトルやテーマ、プラグインなどが定義されます。
- **`assets/`**: Jekyllサイトで利用されるファビコンなどの静的コンテンツを格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ウェブサイトアイコン）の様々なサイズの画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用途で使用されるPythonスクリプトです。
- **`generated-docs/`**: 各リポジトリの概要ファイル（`project-overview.md`）など、生成されたドキュメントを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: 自動生成されたリポジトリ一覧が書き込まれるJekyllサイトのトップページとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中の課題やメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（No.22）に関する詳細なメモです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のための設定ファイルで、ウェブアプリのメタデータやアイコンなどを定義します。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイルです。
- **`requirements-dev.txt`**: プロジェクトの開発・テスト時に必要となるPythonパッケージの依存関係リストです。
- **`requirements.txt`**: プロジェクトの本番実行時に必要となるPythonパッケージの依存関係リストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
- **`ruff.toml`**: Pythonのコード整形・静的解析ツールRuffの設定ファイルです。コード品質とスタイルを維持するためのルールが定義されています。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能のコアロジックをまとめたPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの技術スタックやライセンスなどのバッジ画像を生成するロジックを含みます。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの実行に関する詳細な設定（例: プロジェクト概要取得機能の有効・無効、対象ファイル名など）を定義します。
        - **`config_manager.py`**: プロジェクト全体の設定ファイル（`config.yml`やシークレット情報）の読み込みと管理を担当します。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、Jekyllサイト用のMarkdownコンテンツを生成するロジックです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス）を抽出する機能です。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、生成に適した形式に加工・整形する機能です。
        - **`seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータや、テンプレートに埋め込む設定を定義します。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能です。
        - **`strings.yml`**: ユーザーインターフェースや生成されるMarkdown内で使用される、表示メッセージや文言を一元管理するための設定ファイルです。
        - **`template_processor.py`**: Markdownテンプレートの読み込み、変数置換、条件分岐などのテンプレート処理を行います。
        - **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`機能のユニットテストを行うスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: Pytestのフィクスチャ（テスト実行前の準備や後処理）や共通のヘルパー関数を定義します。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを行うスクリプトです。
    - **`test_check_large_files.py`**: `check_large_files`スクリプトのテストを行うスクリプトです。
    - **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みと管理が正しく行われるかをテストするスクリプトです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストを行うスクリプトです。
    - **`test_environment.py`**: 開発環境や依存関係が正しく設定されているかをテストするスクリプトです。
    - **`test_integration.py`**: プロジェクト全体または複数のコンポーネントを結合した際の統合テストを行うスクリプトです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを行うスクリプトです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うスクリプトです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテストを行うスクリプトです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うスクリプトです。

## 関数詳細説明
プロジェクト情報に個別の関数の詳細な説明（引数、戻り値など）は提供されていません。
各ファイルのPythonスクリプトには、それぞれの機能に応じた関数が含まれており、以下のような役割を担っています。
- `src/generate_repo_list/generate_repo_list.py`: メイン処理を orchestrate する関数群。
- `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの概要ファイルを読み込み、指定されたセクションからテキストを抽出する関数群。
- `src/generate_repo_list/markdown_generator.py`: リポジトリ情報とテンプレートを組み合わせてMarkdownテキストを生成する関数群。
- `src/generate_repo_list/repository_processor.py`: GitHub APIから得られた生データを加工し、使いやすい形式に変換する関数群。
- その他各モジュールも、それぞれのファイル名が示す役割を果たすための具体的な関数群を含んでいます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層ツリーは提供された情報からは分析できませんでした。

---
Generated at: 2026-04-19 07:11:38 JST
