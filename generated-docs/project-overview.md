Last updated: 2026-10-05

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、検索エンジンやLLMからのリポジトリ参照性を向上させます。
- 各リポジトリの概要を自動取得・表示し、アクティブ/アーカイブ/フォークで分類された分かりやすい一覧を提供します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (Markdownベースのサイト生成), Markdown (コンテンツ記述)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要な開発言語およびスクリプト実行環境), GitHub API (リポジトリ情報の取得), Git (バージョン管理)
- テスト: pytest (Pythonのテストフレームワーク)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py`) (Markdownファイルを生成するカスタムビルドロジック)
- 言語機能: Python (ファイル操作、HTTPリクエスト処理、文字列処理など)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリ内のスクリプトを通じて自動化をサポート)
- 開発標準: ruff (Pythonコードのリンティングおよびフォーマット), .editorconfig (エディタ設定の統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub ActionsなどのCI/CDや自動化タスクに関連するスクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能の説明ドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方、開発者向けのヒントなどを記述したメインドキュメント。
- **`_config.yml`**: Jekyllのサイト設定ファイル。GitHub Pagesサイト全体の振る舞いや表示に関する設定を定義。
- **`assets/`**: サイトで使用される静的アセット（ファビコンなどの画像ファイル）を格納するディレクトリ。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコンおよびアプリアイコン。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプト。
- **`generated-docs/`**: 自動生成されたドキュメント（例: 各リポジトリの概要ファイル）が格納されることを想定したディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用されるファイル。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成されるメインのリポジトリ一覧Markdownファイル。GitHub Pagesのトップページとして表示される。
- **`issue-notes/`**: 開発中の課題やメモを記録するためのMarkdownファイル群。
    - `issue-notes/22.md`: 特定の課題（Issue #22）に関するメモ。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブアプリの表示や動作に関する情報を提供。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの実行オプションやパスなどを定義。
- **`requirements-dev.txt`**: 開発環境およびテスト環境で必要なPython依存パッケージをリストアップしたファイル。
- **`requirements.txt`**: 本番環境でこのプロジェクトが動作するために必要なPython依存パッケージをリストアップしたファイル。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツール `ruff` の設定ファイル。コードスタイルルールを定義。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの技術スタックやステータスを示すバッジ画像を生成または準備するロジック。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、リポジトリ一覧生成の技術的パラメータを定義する設定ファイル。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示フォーマットを処理するユーティリティ。
        - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する。
        - **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートファイル。SEOを強化するために使用。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立てるモジュール。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを組み立てるロジック。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` からプロジェクト概要を抽出するモジュール。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルからバッジ情報（例: ビルドステータス）を抽出するモジュール。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、表示に適した形式に変換する。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造に関するテンプレート定義。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算するモジュール。
        - **`src/generate_repo_list/strings.yml`**: UIに表示されるメッセージや文言、翻訳可能な文字列などを一元管理する設定ファイル。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレートを読み込み、データで埋め込む処理。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールのテストスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`tests/conftest.py`**: pytestのフィクスチャやプラグイン、共通設定を定義するファイル。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テスト。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` のテスト。
    - **`tests/test_config.py`**: `config_manager.py` など、設定ファイルの読み込みと管理に関するテスト。
    - **`tests/test_date_formatter.py`**: `date_formatter.py` の日付フォーマット機能のテスト。
    - **`tests/test_environment.py`**: 環境設定や依存関係のチェックに関するテスト。
    - **`tests/test_integration.py`**: システムの主要なエンドツーエンドの統合テスト。
    - **`tests/test_markdown_generator.py`**: `markdown_generator.py` のMarkdown生成機能のテスト。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のプロジェクト概要取得機能のテスト。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のREADMEからのバッジ抽出機能のテスト。
    - **`tests/test_repository_processor.py`**: `repository_processor.py` のリポジトリ情報処理機能のテスト。

## 関数詳細説明
提供されたプロジェクト情報には、個別の関数の詳細な役割、引数、戻り値、機能に関する具体的な記述が含まれていないため、詳細な説明はできません。各ファイルの役割から、関連する機能を持つ関数群が含まれていると推測されますが、ハルシネーションを避けるため、具体的な記述は控えさせていただきます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-05 07:12:21 JST
