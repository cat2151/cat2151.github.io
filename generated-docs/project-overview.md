Last updated: 2026-04-10

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジン最適化（SEO）とLLMによる参照性向上を目的とし、リポジトリ一覧ページと各リポジトリへのリンクを提供します。
- 各リポジトリの概要を自動取得し、バッジ付きで分類表示することで、訪問者にとって魅力的な情報提供を実現します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの静的サイトジェネレーターとして利用), **Markdown** (リポジトリ一覧の出力形式)
- 音楽・オーディオ: このプロジェクトには該当する技術はありません。
- 開発ツール: **pytest** (Pythonテストフレームワーク), **ruff** (Pythonコードリンターおよびフォーマッター), **requirements.txt**/**requirements-dev.txt** (Python依存関係管理)
- テスト: **pytest** (テスト実行), **pytest.ini** (pytest設定ファイル)
- ビルドツール: **Python** (スクリプト実行環境), **GitHub Pages** (生成されたサイトのホスティングおよびビルド環境)
- 言語機能: **Python** (主要な開発言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリ内のスクリプトから自動化の利用を推測)
- 開発標準: **ruff** (コードスタイル自動修正), **.editorconfig** (エディタ設定の統一)

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
- **`.editorconfig`**: コーディングスタイルを定義し、複数のエディタやIDE間で一貫性を保つための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。特に`check_large_files/`は、リポジトリ内の大きなファイルをチェックする自動化プロセスを含みます。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、開発者向けのヒントなどを記述したメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesの振る舞いを制御します。
- **`assets/`**: GitHub Pagesサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグ目的で使用されるスクリプトファイルと推測されます。
- **`generated-docs/`**: 他のリポジトリから取得される`project-overview.md`ファイルが一時的に格納される、または生成されるドキュメントの対象となるディレクトリと推測されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: メインスクリプトによって生成される、リポジトリ一覧を含むMarkdownファイルです。GitHub Pagesサイトのトップページとして表示されます。
- **`issue-notes/`**: 開発中の課題やメモが格納されるディレクトリです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、プログレッシブウェブアプリ（PWA）の機能を提供するために使用されます。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージの依存関係をリスト化したファイルです。
- **`requirements.txt`**: 本番環境で必要なPythonパッケージの依存関係をリスト化したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか/しないかを指示するファイルです。
- **`ruff.toml`**: `ruff`リンター/フォーマッターツールの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するパッケージです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスに応じたバッジ画像を生成する機能を提供します。
        - **`src/generate_repo_list/config.yml`**: `project_overview`機能などの技術的パラメータを設定するためのYAMLファイルです。
        - **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイルを読み込み、管理する機能を提供します。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形する機能を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインのスクリプトファイルです。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のためのJSON-LD形式のテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報を処理する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報に基づいてMarkdownコンテンツを生成するロジックを実装しています。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの`generated-docs/project-overview.md`から概要を自動取得する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルから特定のバッジ情報を抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、表示に必要な形に整形するロジックを提供します。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化に関するテンプレート設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: 表示されるメッセージや文言を管理するためのYAMLファイルです。多言語対応や文言の一元管理に利用されます。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレート処理を行う機能を提供します。
        - **`src/generate_repo_list/url_utils.py`**: URLの操作や検証に関するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview`機能に関する単体テストまたは統合テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義するファイルです。
    - **`tests/test_*.py`**: 各モジュールの機能に対するテストスクリプト群です。

## 関数詳細説明
プロジェクト情報から具体的な関数シグネチャ（引数、戻り値の型）や詳細な実装は提供されていませんが、各Pythonファイルの役割に基づき、主要な関数の機能と役割を推測して説明します。

- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: プログラムのエントリポイントとして、コマンドライン引数をパースし、リポジトリ一覧生成プロセス全体を orchestrate します。
    - `generate_repository_list(username, output_file, limit)`: 指定されたユーザー名のリポジトリ情報をGitHub APIから取得し、整形して指定された出力ファイルにMarkdown形式で書き出す主要な機能を提供します。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge(status)`: リポジトリのアーカイブ状態やフォーク状態などを示すバッジのHTMLまたはMarkdown表現を生成する役割を持ちます。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_file)`: 指定された設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書オブジェクトとして提供する役割を持ちます。
- **`src/generate_repo_list/date_formatter.py`**
    - `format_date(datetime_obj)`: 日付や時刻オブジェクトを指定された形式の文字列に変換する役割を持ちます。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_markdown_output(repo_data_list, strings_data)`: 処理されたリポジトリデータのリストと文言データを受け取り、最終的なMarkdown形式のコンテンツを生成する役割を持ちます。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLから`project-overview.md`ファイルを読み込み、設定に基づいて概要の3行説明を抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**
    - `process_repository(repo_json, config)`: GitHub APIから取得した単一のリポジトリのJSONデータを受け取り、必要な情報を抽出し、整形して他のモジュールが利用しやすいデータ構造に変換する役割を持ちます。
- **`src/generate_repo_list/url_utils.py`**
    - `construct_repo_url(username, repo_name)`: GitHubリポジトリのURLを構成する役割を持ちます。

**注意**: プロジェクト情報からは具体的な引数や戻り値の型、詳細な機能を特定できませんでした。上記の説明は、ファイル名とプロジェクトの文脈に基づいた推測です。

## 関数呼び出し階層ツリー
```
プロジェクト情報からは関数の呼び出し階層ツリーを生成できませんでした。

---
Generated at: 2026-04-10 07:17:44 JST
