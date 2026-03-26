Last updated: 2026-03-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けに一覧ページを自動生成します。
- 検索エンジン最適化されたMarkdownを出力することで、リポジトリの発見性を向上させます。
- 各リポジトリの概要を自動取得・表示し、開発者のLLM参照問題を緩和することを目指します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyllベース)** (静的なウェブサイトホスティングサービス)、**Markdown** (生成されるウェブページのコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なプログラミング言語)、**GitHub API** (リポジトリ情報を取得するためのインターフェース)
- テスト: **pytest** (Pythonプロジェクトのテストを実行するためのフレームワーク)
- ビルドツール: 該当なし (JekyllはGitHub Pages側でウェブサイトをビルドしますが、このプロジェクト自体がビルド処理を持つわけではありません)
- 言語機能: **Pythonの標準機能** (ファイル操作、HTTPリクエストなど、基本的な言語機能)
- 自動化・CI/CD: 該当なし (CI/CDツールの明示的な使用は記載されていませんが、`.github_automation`ディレクトリに自動化スクリプトが配置されています)
- 開発標準: **ruff** (Pythonコードのフォーマットとスタイルチェックを行うツール)

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
- **`.editorconfig`**: コードエディタ間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイル。
- **`README.md`**: プロジェクトの概要、目的、設定方法、使い方などが記載されたメインドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。GitHub Pagesの挙動を制御します。
- **`assets/`**: ウェブサイトで使用される静的リソース（画像、アイコンなど）を格納するディレクトリ。
    - **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズ。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに用いられるスクリプト。
- **`generated-docs/`**: プロジェクトによって自動生成されるドキュメントやデータが格納される予定のディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイル。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイル。リポジトリ一覧がここに生成されます。
- **`issue-notes/`**: プロジェクトに関連する特定の課題や検討事項をメモとして残すためのディレクトリ。
    - **`issue-notes/22.md`**: 22番目の課題またはメモに関する詳細が記述されたMarkdownファイル。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。ウェブアプリの表示や動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージの依存関係を記述したファイル。
- **`requirements.txt`**: プロジェクトの実行（本番環境）に必要なPythonパッケージの依存関係を記述したファイル。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロール・インデックスすべきかを指示するファイル。
- **`ruff.toml`**: Pythonのコードフォーマッター・リンター`ruff`の設定ファイル。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するディレクトリ。
    - **`src/__init__.py`**: Pythonパッケージとして認識させるための初期化ファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧を生成するメインロジックを含むPythonパッケージ。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージの初期化ファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示するバッジ（例: スター数、言語）を生成する機能。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成機能の動作を制御する技術的パラメータ（例: プロジェクト概要取得設定）を定義するYAML設定ファイル。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`, `secrets.toml`など）の読み込みと管理を行うモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を統一するためのユーティリティ機能。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成して出力する。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化(SEO)のためのJSON-LD形式のテンプレートデータ。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語情報を処理するための機能。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジック。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイルからプロジェクト概要の3行説明を抽出する機能。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルからバッジ（例: ビルドステータス）情報を抽出する機能。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを加工、フィルタリング、整理する機能。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するYAMLファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で表示されるテキストメッセージや文言を集中管理するYAMLファイル。
        - **`src/generate_repo_list/template_processor.py`**: Markdownのテンプレート処理や、データに基づいた変数の置換を行う機能。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築や操作に関するユーティリティ機能。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールに対する単体テストスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトのテスト。
    - **`tests/test_config.py`**: 設定ファイルの読み込みと処理に関するテスト。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテスト。
    - **`tests/test_environment.py`**: 実行環境の設定や依存関係に関するテスト。
    - **`tests/test_integration.py`**: プロジェクト全体の主要機能の統合テスト。
    - **`tests/test_markdown_generator.py`**: Markdown生成ロジックのテスト。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテスト。
    - **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテスト。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **`generate_repo_list.py`内の主要関数**:
    - `main()`: このスクリプトの実行エントリポイント。GitHub APIからリポジトリ情報を取得し、他のモジュールを協調させてMarkdownコンテンツを生成し、指定された出力ファイルに書き出す役割を担います。
- **`config_manager.py`内の主要関数**:
    - `load_config()`: 設定ファイル（例: `config.yml`, `secrets.toml`）を読み込み、アプリケーション全体で利用可能な設定オブジェクトとして提供します。
- **`project_overview_fetcher.py`内の主要関数**:
    - `fetch_project_overview()`: 指定されたGitHubリポジトリの特定のパスにある`project-overview.md`ファイルから、プロジェクトの3行概要を抽出して返します。
- **`markdown_generator.py`内の主要関数**:
    - `generate_markdown()`: 処理済みのリポジトリデータと設定情報に基づき、GitHub Pagesに表示されるリポジトリ一覧のMarkdown形式のコンテンツを生成します。
- **`repository_processor.py`内の主要関数**:
    - `process_repositories()`: 指定されたGitHubユーザーのリポジトリをGitHub API経由で取得し、必要に応じてフィルタリング、ソート、追加情報の付与などの加工処理を行います。
- **`badge_generator.py`内の主要関数**:
    - `generate_badge_markdown()`: 特定のバッジ情報（例: 言語、ライセンス、スター数）を受け取り、それに対応するMarkdown形式のバッジ記述を生成します。
- **`date_formatter.py`内の主要関数**:
    - `format_date()`: 日付のタイムスタンプやオブジェクトを受け取り、指定されたフォーマットの日付文字列に変換して返します。
- **`readme_badge_extractor.py`内の主要関数**:
    - `extract_badges_from_readme()`: リポジトリの`README.md`ファイルの内容から、画像やリンクのパターンを解析し、含まれるバッジの情報を抽出します。
- **`statistics_calculator.py`内の主要関数**:
    - `calculate_stats()`: リポジトリデータから、スター数、フォーク数、最終更新日などの統計情報を計算し、整理された形式で提供します。
- **`template_processor.py`内の主要関数**:
    - `render_template()`: 指定されたテンプレートファイル（例: Markdownテンプレート）とデータ辞書を受け取り、データに基づいてテンプレート内のプレースホルダーを置き換え、最終的な文字列を生成します。
- **`url_utils.py`内の主要関数**:
    - `build_github_api_url()`: GitHub APIのエンドポイントやユーザー名、リポジトリ名などの情報を受け取り、正確なAPIリクエストURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-27 07:08:52 JST
