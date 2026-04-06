Last updated: 2026-04-07

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ一覧を自動で取得・整形します。
- JekyllベースのGitHub Pages向けに、SEOを意識したリポジトリ一覧のMarkdownファイルを生成します。
- これにより検索エンジンによるインデックスを促進し、LLMからのリポジトリ参照精度向上に貢献します。

## 技術スタック
- フロントエンド: **GitHub Pages** (生成されたサイトをホスト), **Jekyll** (Markdownファイルを静的サイトとしてビルド), **Markdown** (コンテンツ生成フォーマット), **HTML/CSS** (Jekyllが生成するウェブページの基盤技術)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なスクリプト言語), **GitHub API** (リポジトリ情報の取得元)
- テスト: **pytest** (Pythonアプリケーションのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報からMarkdownファイルを生成するカスタムビルドロジックを実装)
- 言語機能: **Python** (データ構造、ファイルI/O、HTTP通信、文字列処理など)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリの存在から推測されるが、プロジェクト情報ではローカル開発重視とされているため限定的)
- 開発標準: **ruff** (PythonコードのLinterおよびFormatter), **.editorconfig** (各種エディタでのコードスタイル統一設定)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: GitHub Actionsを用いて、リポジトリ内の大規模なファイルをチェックする自動化スクリプト群を格納するディレクトリです。
    - **`README.md`**: `check_large_files`機能に関する説明ドキュメントです。
    - **`check-large-files.toml`**: 大規模ファイルチェックの設定ファイルです。
    - **`scripts/check_large_files.py`**: 大規模ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、使い方などを説明する主要なドキュメントです。
- **`_config.yml`**: GitHub Pagesサイトのビルドに使用されるJekyllの設定ファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要ファイルなどが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイルです。
- **`index.md`**: 生成されたリポジトリ一覧が記述され、GitHub Pagesサイトのトップページとして表示されるMarkdownファイルです。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを提供するマニフェストファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリをリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトを実行するために必要な本番環境用のPythonライブラリをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールするか指示するファイルです。
- **`ruff.toml`**: PythonコードのLinterおよびFormatterである`ruff`の設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するためのファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリ情報に基づいてバッジ（例: 言語バッジ）を生成するロジックを実装したスクリプトです。
- **`src/generate_repo_list/config.yml`**: プロジェクトの動作に関する技術的なパラメータ（例: プロジェクト概要取得機能の設定）を定義する設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイルを読み込み、管理するためのユーティリティスクリプトです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のフォーマット処理を行うユーティリティスクリプトです。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するプロジェクトの主要な実行スクリプトです。
- **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートファイルです。SEO目的で使用されます。
- **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理するスクリプトです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを実装したスクリプトです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動的に取得する機能を提供するスクリプトです。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEから特定のバッジ情報を抽出するスクリプトです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、利用しやすい形式に処理するスクリプトです。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやコンテンツのテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数）を計算するスクリプトです。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で表示される様々なメッセージや文言を一元管理する設定ファイルです。
- **`src/generate_repo_list/template_processor.py`**: テンプレートファイル（例: Markdownテンプレート）を処理し、動的なコンテンツを埋め込むためのスクリプトです。
- **`src/generate_repo_list/url_utils.py`**: URLの操作や処理を行うユーティリティスクリプトです。
- **`test_project_overview.py`**: `project_overview`機能の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: `pytest`のテスト設定やフィクスチャを定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_check_large_files.py`**: 大規模ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能のテストです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストです。
    - **`test_environment.py`**: 実行環境に関するテストです。
    - **`test_integration.py`**: 主要な機能間の統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
プロジェクト情報からは個々の関数の詳細な情報（引数、戻り値、具体的な内部ロジック）は提供されていません。しかし、各Pythonスクリプトの役割から、主要な関数が果たすであろう機能について以下に概要を説明します。

- **`src/generate_repo_list/generate_repo_list.py`** 内の関数群:
    - メイン処理を orchestrate する関数: GitHub APIからリポジトリを取得し、各リポジトリを処理し、最終的なMarkdownファイルを生成する一連の流れを制御します。
    - コマンドライン引数をパースする関数: `--username`, `--output`, `--limit` などの引数を解析します。
- **`src/generate_repo_list/project_overview_fetcher.py`** 内の関数群:
    - リポジトリから概要を取得する関数: 指定されたリポジトリのURLとファイルパスに基づき、`project-overview.md`などのファイル内容をフェッチし、所定のセクションから3行の説明を抽出します。
    - キャッシュ管理関数: 同一実行内でのAPI呼び出しを減らすため、取得した概要をキャッシュします。
- **`src/generate_repo_list/markdown_generator.py`** 内の関数群:
    - リポジトリリストからMarkdownを生成する関数: 処理済みのリポジトリデータを受け取り、Jekyllの要件に沿ったMarkdown形式の文字列を構築します。
    - SEOメタデータ生成関数: `json_ld_template.json`や`seo_template.yml`を元に、検索エンジン最適化のためのメタデータをMarkdownに含めます。
- **`src/generate_repo_list/repository_processor.py`** 内の関数群:
    - GitHub APIレスポンスを処理する関数: GitHub APIから返される生のリポジトリJSONデータを、プロジェクト内で扱いやすいPythonオブジェクトや辞書の形式に変換します。
    - リポジトリ情報を分類する関数: アクティブ、アーカイブ、フォークなどの属性に基づいてリポジトリを分類します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-07 07:12:55 JST
