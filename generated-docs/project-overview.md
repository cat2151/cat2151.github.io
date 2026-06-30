Last updated: 2026-07-01

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照の課題緩和を目的としています。
- リポジトリ概要、バッジ、分類などを自動表示し、SEO最適化された一覧ページを生成します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの基盤), **Markdown** (生成されるコンテンツ形式)
- 音楽・オーディオ: (該当する技術情報がありません)
- 開発ツール: **pytest** (Pythonテストフレームワーク), **ruff** (Pythonコードリンター・フォーマッター), **GitHub API** (リポジトリ情報取得)
- テスト: **pytest** (単体・統合テストの実行)
- ビルドツール: **Python** (スクリプト実行環境、Markdown生成ロジックの実装)
- 言語機能: **Python** (主要な開発言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリ内のスクリプトがCI/CDで利用される可能性を示唆)
- 開発標準: **ruff** (コードスタイルと品質の維持)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードスタイルを統一するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリ。
  - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
  - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックの具体的なルールや設定を定義するファイル。
  - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトがMITライセンスであることを示すライセンス情報ファイル。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定、開発者向けヒントなどを記述したメインのドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどを設定します。
- **`assets/`**: GitHub Pagesサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリ。
  - **`assets/favicon-16x16.png`**: 16x16ピクセルのファビコン画像。
  - **`assets/favicon-192x192.png`**: 192x192ピクセルのファビコン画像（PWAなどで使用）。
  - **`assets/favicon-32x32.png`**: 32x32ピクセルのファビコン画像。
  - **`assets/favicon-512x512.png`**: 512x512ピクセルのファビコン画像（PWAなどで使用）。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のテストやデバッグに特化したPythonスクリプト。
- **`generated-docs/`**: `project-overview.md`など、自動生成されたドキュメントやデータが配置される可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認に使用されるファイル。
- **`index.md`**: 生成されたリポジトリ一覧が書き込まれる、GitHub PagesサイトのトップページとなるMarkdownファイル。
- **`issue-notes/`**: プロジェクト開発中の特定の課題やメモを保管するためのディレクトリ。
  - **`issue-notes/22.md`**: 特定のIssue（課題22番）に関連する詳細なメモや情報。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブアプリケーションマニフェストファイル。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。テスト検出ルールやプラグインなどを定義します。
- **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンをリストしたファイル。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境向けPythonパッケージとそのバージョンをリストしたファイル。
- **`robots.txt`**: 検索エンジンクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットを担う`ruff`ツールの設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリ。
  - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空ファイル。
  - **`src/generate_repo_list/`**: GitHubリポジトリ一覧を生成する機能の中核となるPythonパッケージ。
    - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示す空ファイル。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリに関連するバッジ（例: 言語、ライセンス、ステータス）の情報を処理・生成するモジュール。
    - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成プロセスの技術的パラメータや動作設定を定義するYAMLファイル。
    - **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するためのモジュール。
    - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の形式にフォーマットするためのユーティリティモジュール。
    - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
    - **`src/generate_repo_list/json_ld_template.json`**: SEO目的で使用されるJSON-LD形式の構造化データテンプレート。
    - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理するモジュール。
    - **`src/generate_repo_list/markdown_generator.py`**: 最終的なリポジトリ一覧のMarkdownコンテンツを構築・生成するモジュール。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から概要説明を抽出するモジュール。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するモジュール。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換するモジュール。
    - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するYAMLファイル。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するモジュール。
    - **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元的に管理するYAMLファイル。
    - **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレートファイル（例: Jinja2など）を処理し、データと結合するモジュール。
    - **`src/generate_repo_list/url_utils.py`**: URLの操作や検証など、URLに関連するユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能に関する具体的なテストスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
  - **`tests/conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
  - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を確認するためのテスト。
  - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトの機能をテスト。
  - **`tests/test_config.py`**: 設定ファイル(`config.yml`など)の読み込みや管理に関するテスト。
  - **`tests/test_date_formatter.py`**: 日付フォーマットモジュールの機能テスト。
  - **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテスト。
  - **`tests/test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを確認する統合テスト。
  - **`tests/test_markdown_generator.py`**: Markdown生成ロジックが正しく機能するかをテスト。
  - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要抽出モジュールの機能をテスト。
  - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテスト。
  - **`tests/test_repository_processor.py`**: リポジトリ情報処理モジュールの機能をテスト。

## 関数詳細説明
プロジェクト情報から具体的な関数名、引数、戻り値、機能は特定できませんでした。
しかし、`src/generate_repo_list/`ディレクトリ内の各モジュール（例: `badge_generator.py`, `markdown_generator.py`, `project_overview_fetcher.py`など）に、それぞれのファイル名が示す役割を果たす関数群が実装されていると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-01 07:33:11 JST
