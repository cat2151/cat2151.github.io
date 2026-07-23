Last updated: 2026-07-24

# Project Overview

## プロジェクト概要
- GitHub Pagesサイトに表示するリポジトリ一覧を自動生成するシステムです。
- GitHub APIから情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- 検索エンジンからの発見性を高め、LLMによるリポジトリ参照精度向上に貢献します。

## 技術スタック
- フロントエンド: **Jekyll** (静的サイトジェネレーターとしてGitHub Pagesで利用)、**Markdown** (リポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (主要開発言語)、**GitHub API** (リポジトリ情報取得)、**GitHub Pages** (コンテンツホスティングプラットフォーム)
- テスト: **pytest** (Pythonコードのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (`generate_repo_list.py` がMarkdownファイルを生成するビルドプロセスを担う)、**Jekyll** (最終的なウェブページ生成)
- 言語機能: **Python** (プロジェクトの主要プログラミング言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリ内のスクリプトによるファイルサイズチェックなどの自動化処理に使用)
- 開発標準: **ruff** (Pythonコードのリンター、フォーマッターによるコード品質とスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードの書式設定（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsによる自動化タスクに関連するスクリプトや設定ファイルを格納するディレクトリです。
    - **`check_large_files/`**: プロジェクト内の大容量ファイルをチェックする機能を含みます。
        - **`README.md`**: `check_large_files` 機能に関する説明ドキュメントです。
        - **`check-large-files.toml`**: `check_large_files` 機能の設定ファイルです。
        - **`scripts/check_large_files.py`**: 大容量ファイルを検出・報告するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリ（例: 一時ファイル、ビルド成果物、ローカル設定）を指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesの動作やサイトのメタデータを制御します。
- **`assets/`**: ウェブサイトで使用される画像やアイコンなどの静的ファイルを格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各サイズです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストを目的とした補助スクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要などのドキュメントが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト所有者認証に使用されるファイルです。
- **`index.md`**: メインの出力ファイルであり、GitHub Pages上でリポジトリ一覧を表示するMarkdownファイルです。
- **`issue-notes/22.md`**: 開発中の特定の課題や検討事項を記録したメモファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、Webアプリがユーザーのデバイス上でどのように表示・動作するかを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発環境およびテスト実行時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: 本番環境でスクリプトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するための中心的なロジックが配置されています。
        - **`__init__.py`**: Pythonサブパッケージとして認識させるためのファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（例: `GitHub Actions`バッジ）を生成するロジックを含みます。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの動作を制御する設定ファイル（例: プロジェクト概要取得の有効/無効、対象ファイルパスなど）です。
        - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml` や秘密情報ファイルなど）の読み込みと管理を担当するモジュールです。
        - **`date_formatter.py`**: 日付情報を読みやすい形式に整形するためのユーティリティ関数群を含みます。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式のデータテンプレートです。
        - **`language_info.py`**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するロジックを含みます。
        - **`markdown_generator.py`**: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを含みます。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得する機能を提供します。
        - **`readme_badge_extractor.py`**: READMEファイル内に記述されている既存のバッジ情報を解析・抽出するロジックを含みます。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で利用しやすい形式に加工・整形するロジックを含みます。
        - **`seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータを定義するためのテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        - **`strings.yml`**: アプリケーション内で表示されるメッセージや文言を一元的に管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdownテンプレート内のプレースホルダーに変数を埋め込み、最終的なコンテンツを生成するロジックを含みます。
        - **`url_utils.py`**: URLの生成、検証、解析など、URLに関連するユーティリティ関数群です。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能に対する単体テストを含むファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト実行時に共通で利用されるフィクスチャや設定を定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定読み込み・管理機能のテストです。
    - **`test_date_formatter.py`**: 日付整形機能のテストです。
    - **`test_environment.py`**: 実行環境に関するテストです。
    - **`test_integration.py`**: システム全体の主要な統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
プロジェクト情報からは、各ファイルの具体的な関数名、引数、戻り値、およびその機能の詳細な説明は提供されていません。しかし、各Pythonモジュールの役割に基づき、以下のような機能を持つ関数が含まれていると推測されます。

- **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種情報（言語、ステータスなど）に基づいて、Markdown形式のバッジ文字列を生成する関数群。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`、秘密情報ファイルなど）を読み込み、アプリケーション全体で利用可能な設定値を提供する関数群。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のオブジェクトを、指定されたフォーマットの人間が読みやすい文字列に変換する関数群。
- **`src/generate_repo_list/generate_repo_list.py`**: プログラムのメインエントリポイントとなる関数（例: `main`関数）を含み、GitHub APIからのデータ取得、各処理モジュールの呼び出し、最終的なMarkdownファイルの出力といった一連のフローを制御する関数群。
- **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語データを解析し、例えば主要言語の特定や複数言語の整理など、表示に適した形式に加工する関数群。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータを受け取り、それをMarkdown形式の文字列として整形し、出力する関数群。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 特定のファイルパス（例: `generated-docs/project-overview.md`）から指定されたセクション（例: 「プロジェクト概要」）のテキストを抽出し、整形する関数群。
- **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルの内容を解析し、その中に埋め込まれているバッジ（例: ビルドステータスバッジ）の情報（URLやaltテキストなど）を抽出する関数群。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーションの他の部分で利用しやすい内部データ構造に変換・加工する関数群。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計する関数群。
- **`src/generate_repo_list/template_processor.py`**: Markdownテンプレートファイル内のプレースホルダー（例: `{{ repo.name }}`）を実際のリポジトリデータで置き換え、最終的な出力コンテンツを生成する関数群。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、有効性の検証、パスの結合など、URLに関連する様々なユーティリティ関数群。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: 指定されたしきい値を超えるサイズのファイルを検出し、報告する関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-07-24 07:23:44 JST
