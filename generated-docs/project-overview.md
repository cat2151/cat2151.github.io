Last updated: 2026-09-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、各リポジトリの情報からJekyllサイト用のSEO最適化されたMarkdownファイルを自動作成します。
- 検索エンジンや大規模言語モデルによるリポジトリ情報の発見性を向上させ、情報アクセスと開発効率の向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として使用), Markdown (Jekyllサイトに表示されるコンテンツのフォーマット)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: GitHub API (リポジトリ情報の取得に使用), Ruff (Pythonコードのフォーマットとリント), Pytest (Pythonコードのテストフレームワーク)
- テスト: Pytest (ユニットテストおよび統合テストの実行に利用)
- ビルドツール: Python (リポジトリ一覧生成スクリプトの実行環境), Jekyll (MarkdownファイルをHTMLに変換し、サイトを構築)
- 言語機能: Python (主要なスクリプト言語として使用)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリから、コードチェックや自動デプロイなどのワークフローが存在すると推測されます)
- 開発標準: Ruff (コードの品質と一貫性を保つためのリンターおよびフォーマッター)

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
- **`.editorconfig`**: コードエディタの設定ファイルで、インデントスタイルや文字コードなど、プロジェクト全体のコーディング規約を定義し、開発者間のコードの一貫性を保ちます。
- **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化ワークフローに関連するファイル群を格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
    - **`check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出し、警告するためのPythonスクリプトです。
- **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトがMITライセンスであることを示すファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法などを説明するメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの挙動に影響を与えます。
- **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: さまざまなサイズで表示されるウェブサイトのファビコン画像ファイルです。
- **`debug_project_overview.py`**: リポジトリの`project-overview.md`ファイルから概要を取得する機能のデバッグに用いられるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（例：`project-overview.md`）を一時的または恒久的に格納する場所です。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルで、自動生成されたリポジトリ一覧がここに表示されます。
- **`issue-notes/22.md`**: プロジェクトの特定の課題（Issue #22）に関するメモや詳細を記録したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルで、ウェブアプリのインストール情報や表示方法などを定義します。
- **`pytest.ini`**: Pytestテストフレームワークの設定ファイルで、テストの発見方法や実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルで、コードスタイルや品質に関するルールを定義します。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示される言語やライセンスなどのバッジ画像を生成または処理する機能を提供します。
- **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行に関する詳細な設定（例：プロジェクト概要取得機能の有効/無効、リトライ回数、タイムアウト）を定義します。
- **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`や`secrets.toml`など）を読み込み、管理するためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理全体を orchestrate します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために構造化データ（JSON-LD形式）を生成する際のテンプレートです。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの主要言語に関する情報を処理・解析するためのモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdown形式のコンテンツを生成する機能を提供します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクトの概要説明を抽出する機能です。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例：CI/CDステータス、カバレッジ）を抽出する機能です。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に加工する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: ページのタイトル、説明、キーワードなどのSEO関連メタデータを定義するためのテンプレートファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するためのファイルで、多言語対応にも利用できます。
- **`src/generate_repo_list/template_processor.py`**: Jekyllのテンプレートエンジンを模倣し、Markdownファイル内で動的にコンテンツを挿入する処理を扱います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
- **`tests/conftest.py`**: Pytestのテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するための設定ファイルです。
- **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テストを行い、バッジ生成が期待通りに動作するかを確認します。
- **`tests/test_check_large_files.py`**: `.github_automation/check_large_files`スクリプトの機能をテストし、大容量ファイルの検出が正しく行われるかを確認します。
- **`tests/test_config.py`**: 設定ファイルの読み込みや解析が正しく行われるか、`config_manager`モジュールをテストします。
- **`tests/test_date_formatter.py`**: `date_formatter`モジュールの日付整形機能が期待通りに動作するかをテストします。
- **`tests/test_environment.py`**: プロジェクトの実行環境が正しくセットアップされているか、必要な依存関係が満たされているかなどを確認するテストです。
- **`tests/test_integration.py`**: プロジェクト全体の主要機能が連携して動作するかを確認する統合テストです。
- **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールのMarkdown生成機能が期待通りに動作し、正しい出力が得られるかをテストします。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールが正しくリポジトリ概要を抽出できるかをテストします。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールが`README.md`から正確にバッジ情報を抽出できるかをテストします。
- **`tests/test_repository_processor.py`**: `repository_processor`モジュールがGitHub APIから取得したデータを適切に処理・変換できるかをテストします。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数の役割、引数、戻り値、機能に関する詳細な説明は含まれていませんでした。したがって、具体的な関数情報を提供することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析するための詳細な情報が提供されていないため、ツリーを生成することはできません。

---
Generated at: 2026-09-17 07:11:06 JST
