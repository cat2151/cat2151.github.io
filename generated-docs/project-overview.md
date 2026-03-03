Last updated: 2026-03-04

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHubリポジトリ情報を自動的に取得します。
- 取得した情報から、SEOに最適化されたGitHub Pages向けのリポジトリ一覧Markdownを生成します。
- これにより、リポジトリの可視性を高め、検索エンジンやLLMからの参照性向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤)、Markdown (生成されるコンテンツ形式)、JSON-LD (SEOのための構造化データ)
- 音楽・オーディオ: 該当なし
- 開発ツール: GitHub API (リポジトリ情報取得)、Python (主要開発言語)、PyYAML (YAML設定ファイルの処理)、toml (シークレット設定ファイルの処理)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Pythonスクリプト (生成処理自体)、pip/requirements.txt (Python依存関係管理)
- 言語機能: Python (バージョン3.x系の機能とライブラリ)
- 自動化・CI/CD: GitHub Actions (リポジトリの自動処理やデプロイの示唆)
- 開発標準: ruff (Pythonコードのフォーマッター兼リンター)、.editorconfig (エディタ設定の統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義する設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
  - **`check_large_files/`**: 大容量ファイルチェックに関する自動化機能が含まれます。
    - **`README.md`**: `check_large_files` 機能の説明文書です。
    - **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義するファイルです。
    - **`scripts/`**: 関連スクリプトを格納するディレクトリです。
      - **`check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法などを説明する主要なドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の基本的な設定を定義するファイルです。
- **`assets/`**: サイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブに表示されるアイコン）の各サイズを格納します。
- **`debug_project_overview.py`**: `project_overview` 機能のデバッグやテストに特化したスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されたドキュメントやデータが格納されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が表示されるMarkdownファイルです。
- **`issue-notes/`**: 課題やメモを記録するためのディレクトリです。
  - **`22.md`**: 特定の課題（Issue #22）に関する詳細なメモや議論が記されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するマニフェストファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonの依存パッケージをリスト化したファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonの依存パッケージをリスト化したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのフォーマットとリンティングを行うRuffツールの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
  - **`__init__.py`**: Pythonパッケージであることを示す空ファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックが含まれるPythonパッケージです。
    - **`__init__.py`**: Pythonサブパッケージであることを示すファイルです。
    - **`badge_generator.py`**: リポジトリの各種ステータス（言語、スターなど）を示すバッジ画像を生成するためのロジックが含まれます。
    - **`config.yml`**: リポジトリ情報取得やMarkdown生成に関する技術的なパラメータを設定するファイルです。
    - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）の読み込みと管理を行うためのスクリプトです。
    - **`date_formatter.py`**: 日付や時刻を特定の形式にフォーマットするためのユーティリティ関数が含まれます。
    - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownを生成するメインのエントリスクリプトです。
    - **`json_ld_template.json`**: SEOのために構造化データを生成する際のJSON-LDテンプレートファイルです。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理するためのスクリプトです。
    - **`markdown_generator.py`**: 取得した情報をもとに、最終的なリポジトリ一覧のMarkdownコンテンツを構築するロジックが含まれます。
    - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を自動取得するロジックが含まれます。
    - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出するためのロジックが含まれます。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を整形し、必要なデータに加工するためのロジックが含まれます。
    - **`seo_template.yml`**: SEOに関連するメタデータや記述のテンプレートを定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するためのロジックが含まれます。
    - **`strings.yml`**: 生成されるMarkdownや表示メッセージで使用される文言を管理する設定ファイルです。
    - **`template_processor.py`**: MarkdownやJSON-LDのテンプレートに変数を埋め込み、最終的なコンテンツを生成するロジックが含まれます。
    - **`url_utils.py`**: URLの構築や検証など、URL関連のユーティリティ関数が含まれます。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
  - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
  - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
  - **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや管理機能のテストです。
  - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストです。
  - **`test_environment.py`**: テスト環境のセットアップや依存関係のテストです。
  - **`test_integration.py`**: システム全体の統合テストです。
  - **`test_markdown_generator.py`**: Markdown生成ロジックのテストです。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
  - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
  - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
このプロジェクトはPythonで書かれており、`src/generate_repo_list/` ディレクトリ内の各ファイルには、その役割に応じた複数の関数が含まれています。具体的な関数の引数や戻り値の詳細は情報が提供されていませんが、各ファイルの主要な機能は以下の通りです。

- **`src/generate_repo_list/badge_generator.py`**: リポジトリの技術スタックやステータスを示すバッジ（例: 使用言語、スター数）を生成する関数群を提供します。
- **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）を読み込み、アプリケーション全体で利用できるように管理する関数群を提供します。
- **`src/generate_repo_list/date_formatter.py`**: リポジトリの作成日や最終更新日などの日付情報を、人間が読みやすい形式に整形する関数群を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからのリポジトリ情報取得、各種データの加工、最終的なMarkdown生成までを一連の流れとして実行する、プロジェクトのメイン処理となる関数群（`main`関数など）を定義します。
- **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語の割合や詳細な情報を処理・分析する関数群を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・加工されたリポジトリ情報をもとに、GitHub Pages用のMarkdown形式のリポジトリ一覧コンテンツを生成する関数群を提供します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの簡潔な概要（3行説明など）を抽出・取得する関数群を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルの内容を解析し、そこに埋め込まれたバッジ（shields.ioなど）の情報を抽出する関数群を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に変換・加工する関数群を提供します。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、ウォッチ数などの各種統計情報を計算・集計する関数群を提供します。
- **`src/generate_repo_list/template_processor.py`**: MarkdownやJSON-LDなどのテンプレートファイルに、動的に取得したデータを埋め込んで最終的な出力コンテンツを生成する関数群を提供します。
- **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリへのリンクや、その他の関連URLを適切に構築・処理するためのユーティリティ関数群を提供します。
- その他、`tests/` ディレクトリ内のテストファイルには、各機能のテストを実行するための関数群が含まれています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-04 07:09:33 JST
