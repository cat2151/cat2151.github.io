Last updated: 2026-04-06

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けリポジトリ一覧を自動生成するシステムです。
- SEO最適化されたMarkdownファイルを生成し、検索エンジンでの発見性を高めます。
- LLMによるリポジトリ参照失敗の課題を緩和し、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターとして利用され、生成されたMarkdownファイルを美しいWebサイトに変換します。
- 音楽・オーディオ: なし
- 開発ツール:
    - Python: プロジェクトの主要な開発言語です。
    - PyGithub: GitHub APIと連携し、リポジトリ情報を取得するためのPythonライブラリです。
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`) の読み書きに使用されます。
    - requests: HTTPリクエストを送信するためのPythonライブラリで、GitHub APIとの通信に利用されます。
    - ruff: 高速なPythonリンターおよびフォーマッターで、コード品質の維持とスタイルの統一に貢献します。
- テスト: pytest - Pythonプロジェクトのテストフレームワークとして利用され、コードの動作検証を行います。
- ビルドツール: GitHub Pages (Jekyll) - 生成されたMarkdownファイルから静的サイトをホスト・公開するためのプラットフォームです。
- 言語機能: Python - 高い生産性と豊富なライブラリを持つ汎用プログラミング言語です。
- 自動化・CI/CD: なし (GitHub Actionsでの運用が示唆されていますが、本プロジェクトの技術スタックとしては含まれません)。
- 開発標準:
    - ruff: コードスタイルチェックと自動修正により、一貫性のあるコードベースを維持します。
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを定義します。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    - **`.github_automation/check_large_files/check-large-files.toml`**: プロジェクト内の大容量ファイルをチェックするツールの設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定、ライセンスなど、全体的な説明を提供するメインドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイルで、GitHub Pagesの動作を制御します。
- **`assets/`**: 静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（アイコン）画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメント（例: 各リポジトリの `project-overview.md` など）が格納されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルで、本プロジェクトで生成されるリポジトリ一覧が出力されます。
- **`issue-notes/`**: 開発中の課題やメモを保管するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモを記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面に追加されるアプリの表示などを定義します。
- **`pytest.ini`**: `pytest` テストフレームワークの動作設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発およびテスト時に必要なPythonパッケージとそのバージョンを記述したファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、またどのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: `ruff` リンター/フォーマッターの動作設定を定義するファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージであることを示す空のファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能に関連するモジュールをまとめたPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: Pythonサブパッケージであることを示す空のファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やライセンスなどのバッジ情報を生成する機能を持つモジュールです。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成システムの動作に関する技術的パラメータを定義する設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: YAML形式の設定ファイル (`config.yml` など) を読み込み、管理するためのモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティモジュールです。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を統括します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO強化のためのJSON-LD形式の構造化データテンプレートです。
        - **`src/generate_repo_list/language_info.py`**: GitHubリポジトリのプログラミング言語に関する情報を処理するモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要を自動取得・抽出するモジュールです。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイル内に埋め込まれたバッジ情報（例: ビルドステータス）を抽出するモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: 個々のGitHubリポジトリ情報を処理し、必要なデータを整形するためのモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連の設定やテンプレートを定義するYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するモジュールです。
        - **`src/generate_repo_list/strings.yml`**: UI表示メッセージや文言を管理するための設定ファイルです。
        - **`src/generate_repo_list/template_processor.py`**: テンプレートエンジンを用いてコンテンツをレンダリングするモジュールです。
        - **`src/generate_repo_list/url_utils.py`**: URLに関連するユーティリティ関数（生成、解析など）を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest` のフィクスチャ（テストヘルパー）を定義するファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator` モジュールの結合テストを記述したファイルです。
    - **`tests/test_check_large_files.py`**: `check_large_files.py` スクリプトのテストを記述したファイルです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    - **`tests/test_date_formatter.py`**: `date_formatter` モジュールのテストを記述したファイルです。
    - **`tests/test_environment.py`**: 実行環境に関するテストを記述したファイルです。
    - **`tests/test_integration.py`**: プロジェクト全体の主要な結合テストを記述したファイルです。
    - **`tests/test_markdown_generator.py`**: `markdown_generator` モジュールのテストを記述したファイルです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールのテストを記述したファイルです。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールのテストを記述したファイルです。
    - **`tests/test_repository_processor.py`**: `repository_processor` モジュールのテストを記述したファイルです。

## 関数詳細説明
関数に関する詳細な情報は提供されていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-06 07:09:21 JST
