Last updated: 2026-03-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- 各リポジトリの概要、バッジ、分類などを表示し、検索エンジンからの発見性とLLMの参照性を高めます。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースで動作する静的サイトホスティング), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: このプロジェクトには該当する技術はありません。
- 開発ツール: pytest (テストフレームワーク), ruff (Pythonコードリンター), PowerShell (スクリプト実行例で使用)
- テスト: pytest (Pythonコードの単体・統合テスト実行ツール)
- ビルドツール: Pythonスクリプト (動的なMarkdown生成ロジック自体がビルドの役割を担う)
- 言語機能: Python 3.x (主要な開発言語)
- 自動化・CI/CD: GitHub API (リポジトリ情報取得の基盤), GitHub Pages (生成されたサイトのホスティング先), `.github_automation` ディレクトリ (GitHub Actionsなどの自動化スクリプト格納の可能性)
- 開発標準: ruff (Pythonコードのフォーマットとリンティングによる品質管理)

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
- **`.editorconfig`**: さまざまなエディタやIDE間でコードスタイルの一貫性を保つための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化されたワークフローやスクリプトを格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルを検出するためのスクリプト群を格納します。
        - **`README.md`**: `check_large_files` ディレクトリに関する説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルをチェックするためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報 (MITライセンス) を示します。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、機能などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどを定義します。
- **`assets/`**: ウェブサイトで使用される画像 (faviconなど) やその他の静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに用いられるスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されるドキュメントや、外部リポジトリから取得された概要ファイルなどを一時的または永続的に格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が組み込まれるMarkdownファイルです。
- **`issue-notes/`**: 開発中に発生した課題や検討事項に関するメモをMarkdown形式で格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、アプリのホーム画面アイコンや表示方法などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出方法や実行オプションを定義します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonの依存パッケージをリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonの依存パッケージをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。コードの品質と一貫性を保つためのルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`__init__.py`**: Pythonのパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するコアロジックを格納するパッケージです。
        - **`__init__.py`**: Pythonのパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを含みます。
        - **`config.yml`**: プロジェクトの動作に関する各種設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するYAMLファイルです。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するユーティリティモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD形式) のテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・解析するロジックを含みます。
        - **`markdown_generator.py`**: 最終的なMarkdown形式の出力コンテンツを構築・生成するロジックを担当します。
        - **`project_overview_fetcher.py`**: 他のリポジトリから `generated-docs/project-overview.md` ファイルの内容をフェッチし、プロジェクト概要を抽出するロジックです。
        - **`readme_badge_extractor.py`**: 各リポジトリの `README.md` から既存のバッジ情報を抽出し、解析するロジックです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・処理するロジックです。
        - **`seo_template.yml`**: サイトのSEOメタデータ（タイトル、ディスクリプションなど）に関する設定テンプレートです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算するロジックです。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を国際化対応できるように管理するYAMLファイルです。
        - **`template_processor.py`**: Markdownテンプレートファイルの読み込み、変数置換、レンダリングなどの処理を行うモジュールです。
        - **`url_utils.py`**: URLの構築、解析、検証など、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能に関するテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を確認するテストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定管理機能が正しく動作するかを確認するテストです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストです。
    - **`test_environment.py`**: 実行環境の設定や依存関係に関するテストです。
    - **`test_integration.py`**: プロジェクトの主要なフローが全体として正しく機能するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
プロジェクト情報には、関数の具体的な役割、引数、戻り値に関する詳細な説明は提供されていません。Pythonスクリプトとして多くの関数が存在しますが、ハルシネーションを避けるため、ここでは具体的な記述を省略します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-23 07:07:58 JST
