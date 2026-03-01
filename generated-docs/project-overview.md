Last updated: 2026-03-02

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成します。
- 検索エンジンからのクロールを容易にし、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として、生成されたMarkdownファイルをレンダリング)
- 音楽・オーディオ: (該当なし)
- 開発ツール:
    - `pytest`: Pythonコードのテストフレームワーク
    - `ruff`: Pythonコードのリンターおよびフォーマッター
    - `requirements.txt`/`requirements-dev.txt`: Pythonの依存関係管理
    - `config.yml`/`strings.yml`: プロジェクトの設定と表示文言の管理
- テスト: `pytest` (単体テスト、統合テストの実行)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py`) がMarkdownコンテンツを生成する役割を担います。最終的なサイトはJekyllがビルドします。
- 言語機能: Python (主要なロジックが記述されているプログラミング言語)
- 自動化・CI/CD: GitHub PagesのデプロイはGitHubのインフラによって自動化されますが、プロジェクト自体には明示的なCI/CDパイプラインは含まれていません（ローカル開発重視）。
- 開発標準:
    - `ruff`: Pythonコードのスタイルガイドと静的解析
    - `.editorconfig`: 複数エディタ間でのコーディングスタイル統一

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.github_automation/check_large_files/`**: 大容量ファイルをチェックする自動化スクリプト群を格納するディレクトリです。
    - **`README.md`**: 大容量ファイルチェック機能に関する説明を提供します。
    - **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義します。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法など、全体的な概要を説明するメインドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の挙動を設定するファイルです。
- **`assets/`**: GitHub Pagesサイトで利用される画像ファイルなどのアセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）ファイル群です。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに特化したスクリプトと推測されます。
- **`generated-docs/`**: 他のリポジトリから自動取得される `project-overview.md` など、生成されたドキュメントの基準となるディレクトリ、または生成物の出力先として機能する可能性があります。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト認証に使用される可能性のあるファイルです。
- **`index.md`**: メインのPythonスクリプトによって生成される、リポジトリ一覧が記述されたMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定の課題や問題に関するメモを記述したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、ウェブアプリマニフェストファイルです。
- **`pytest.ini`**: `pytest` のテスト実行に関する設定を記述するファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの実行時に最低限必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonリンター/フォーマッターである `ruff` の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして認識させるための空ファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成ロジックを格納するサブパッケージです。
        - **`__init__.py`**: Pythonサブパッケージとして認識させるための空ファイルです。
        - **`badge_generator.py`**: リポジトリの技術スタックなどを示すバッジ画像を生成または整形する機能を提供します。
        - **`config.yml`**: `project_overview` 機能などの技術的なパラメータを設定するためのファイルです。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理する役割を担います。
        - **`date_formatter.py`**: リポジトリの更新日などの日付情報を、適切なフォーマットに整形するための機能を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD形式）のテンプレートです。
        - **`language_info.py`**: リポジトリが使用しているプログラミング言語の情報を処理し、表示に役立つ形式に変換する機能を提供します。
        - **`markdown_generator.py`**: 取得・整形されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツを構築する役割を担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形する主要なロジックを格納します。
        - **`seo_template.yml`**: SEOメタデータに関するテンプレート設定を記述したファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するためのファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイル（例: リスト形式の項目）を読み込み、データと結合して最終的な文字列を生成する機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを実行します。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを実行します。
    - **`test_config.py`**: 設定管理機能のテストを実行します。
    - **`test_date_formatter.py`**: 日付整形機能のテストを実行します。
    - **`test_environment.py`**: テスト環境の設定や依存関係のテストを実行します。
    - **`test_integration.py`**: 主要なコンポーネント間の連携をテストする統合テストを実行します。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを実行します。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを実行します。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを実行します。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを実行します。

## 関数詳細説明
このプロジェクトはPythonスクリプトを主体としており、各Pythonファイルが特定の役割を持つ関数群を内包しています。例えば、`generate_repo_list.py` はGitHub APIとの連携、データ取得、各処理モジュールの呼び出しをオーケストレーションするメイン関数を持ちます。`repository_processor.py` や `markdown_generator.py` などは、それぞれリポジトリデータの整形やMarkdownの組み立てを行う複数のヘルパー関数を含んでいます。これらの関数は、引数としてデータを受け取り、処理結果を返すことで、モジュール間の連携を実現しています。具体的な関数名、引数、戻り値の詳細については、各Pythonファイルのソースコードを参照する必要があります。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-02 07:07:03 JST
