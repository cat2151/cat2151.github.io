Last updated: 2026-11-14

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を自動取得し、GitHub Pagesサイト向けに最適化されたMarkdownファイルを生成します。
- これにより、リポジトリ一覧や個々のリポジトリが検索エンジンにクロールされやすくなり、LLM参照時の問題緩和に貢献します。
- バッジ付き表示、アクティブ・アーカイブ・フォーク分類、各リポジトリの概要自動取得など、豊富な機能を提供します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤として利用される静的サイトジェネレーター。本プロジェクトはJekyllが処理するMarkdownファイルを生成します。
    - **Markdown**: 生成されるリポジトリ一覧のコンテンツ形式。
- 音楽・オーディオ: 該当なし。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語。リポジトリ情報の取得、処理、Markdown生成ロジックがPythonで記述されています。
    - **GitHub API**: GitHubリポジトリのメタデータ（説明、言語、更新日時など）を取得するために使用されます。
    - **Git**: ソースコードのバージョン管理システム。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述形式。
    - **TOML**: 設定ファイル (`secrets.toml`, `check-large-files.toml`) の記述形式。
- テスト:
    - **pytest**: Pythonコードのテストを実行するためのフレームワーク。
- ビルドツール:
    - **Python**: 生成スクリプト自体がMarkdownファイルを「ビルド」する役割を担います。
- 言語機能:
    - **Python**: 最新のPython言語仕様と機能が活用されています。
- 自動化・CI/CD:
    - **GitHub Pages**: 生成されたコンテンツをホストし、自動デプロイするプラットフォーム。
    - **GitHub Automation (`.github_automation`ディレクトリ)**: プロジェクトに自動化スクリプトが格納されることを示唆しています（例: 大容量ファイルチェック）。
- 開発標準:
    - **ruff**: Pythonコードのリンティングとフォーマットを自動で行い、コード品質と一貫性を保つためのツール。
    - **.editorconfig**: 異なるエディタやIDE間でのコードスタイルの統一を支援する設定ファイル。

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
-   `.editorconfig`: 異なるエディタ間でインデントスタイル、文字コード、改行コードなどのコードフォーマットを統一するための設定ファイル。
-   `.github_automation/`: GitHubに関連する自動化スクリプトや設定を格納するためのディレクトリ。
    -   `check_large_files/`: 大容量ファイルを検出し、リポジトリの健全性を保つための機能群。
        -   `README.md`: `check_large_files`機能に関する説明。
        -   `check-large-files.toml`: 大容量ファイルチェックのルールや閾値を定義する設定ファイル。
        -   `scripts/check_large_files.py`: 実際に大容量ファイルをスキャン・検出するPythonスクリプト。
-   `.gitignore`: Gitのバージョン管理から除外すべきファイルやディレクトリのパターンを定義するファイル。
-   `LICENSE`: プロジェクトがMITライセンスの下で提供されていることを示すライセンス条項ファイル。
-   `README.md`: プロジェクトの概要、目的、主な機能、設定方法、クイックテスト方法など、プロジェクトの全体像を説明する主要なドキュメント。
-   `_config.yml`: Jekyll（GitHub Pagesの基盤）サイト全体の構成を定義するファイル。
-   `assets/`: GitHub Pagesサイトで使用される静的な画像やアイコンなどのアセットを格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ブラウザタブなどに表示されるアイコン）の異なるサイズ版。
-   `debug_project_overview.py`: プロジェクト概要の自動取得機能（`project_overview_fetcher.py`）を個別にデバッグするためのスクリプト。
-   `generated-docs/`: 各リポジトリのプロジェクト概要情報（`project-overview.md`）が格納されることを想定したディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
-   `index.md`: `generate_repo_list.py`によって生成される、リポジトリ一覧のメインコンテンツを記述したMarkdownファイル。GitHub Pagesのトップページとして公開されます。
-   `issue-notes/`: 開発中に発生した課題や検討事項をメモとして残すためのディレクトリ。
    -   `22.md`: 特定の課題（おそらくIssue #22）に関する詳細なメモ。
-   `manifest.json`: ウェブアプリケーションマニフェスト。プログレッシブウェブアプリ (PWA) の設定を提供し、ホーム画面への追加やオフライン動作などを可能にします。
-   `pytest.ini`: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイル。
-   `requirements-dev.txt`: 開発環境やテスト環境でのみ必要となるPythonパッケージの依存関係をリストアップするファイル。
-   `requirements.txt`: プロジェクトの本番稼働に必要となるPythonパッケージの依存関係をリストアップするファイル。
-   `robots.txt`: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきではないかを指示するファイル。
-   `ruff.toml`: コードリンタおよびフォーマッタであるRuffの動作を設定するファイル。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   `__init__.py`: Pythonがこのディレクトリをパッケージとして認識するために必要なファイル。
    -   `generate_repo_list/`: リポジトリ一覧の生成に関する全てのロジックを含むPythonパッケージ。
        -   `__init__.py`: Pythonがこのディレクトリをパッケージとして認識するために必要なファイル。
        -   `badge_generator.py`: リポジトリの状態（言語、ライセンスなど）を示すバッジを生成するロジックを扱うファイル。
        -   `config.yml`: リポジトリ一覧生成プロセスの様々な技術的パラメータを設定するためのYAMLファイル。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するユーティリティ関数を提供するファイル。
        -   `date_formatter.py`: 日付や時刻を特定のフォーマットに整形するためのユーティリティ関数を提供するファイル。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体をオーケストレーションします。
        -   `json_ld_template.json`: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレートファイル。
        -   `language_info.py`: リポジトリの使用言語とその割合に関する情報を処理するロジックを扱うファイル。
        -   `markdown_generator.py`: 取得・処理されたリポジトリ情報から、最終的なMarkdownコンテンツを構築するロジックを扱うファイル。
        -   `project_overview_fetcher.py`: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から概要を自動取得するロジックを扱うファイル。
        -   `readme_badge_extractor.py`: 各リポジトリのREADMEファイルから、既存のバッジ情報を抽出するロジックを扱うファイル。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出・加工するロジックを扱うファイル。
        -   `seo_template.yml`: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（スター数、フォーク数など）を計算するためのロジックを扱うファイル。
        -   `strings.yml`: UIに表示されるメッセージや文言を国際化・一元管理するためのYAMLファイル。
        -   `template_processor.py`: Markdownテンプレートを読み込み、動的なデータで埋め込んで最終的なコンテンツを生成するロジックを扱うファイル。
        -   `url_utils.py`: URLの構築や解析など、URLに関連するユーティリティ関数を提供するファイル。
-   `test_project_overview.py`: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の単体テストファイル。
-   `tests/`: プロジェクトのテストコードを格納するディレクトリ。
    -   `conftest.py`: `pytest`において、テスト全体で共有されるフィクスチャやヘルパー関数を定義するためのファイル。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テストを実行するファイル。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストファイル。
    -   `test_config.py`: 設定ファイルの読み込みや解析に関するテストファイル。
    -   `test_date_formatter.py`: 日付フォーマットユーティリティのテストファイル。
    -   `test_environment.py`: プロジェクトの実行環境に関する設定や依存関係のテストファイル。
    -   `test_integration.py`: プロジェクト全体の主要なフローに関する統合テストを実行するファイル。
    -   `test_markdown_generator.py`: Markdown生成機能のテストファイル。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストファイル。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストファイル。
    -   `test_repository_processor.py`: リポジトリデータ処理機能のテストファイル。

## 関数詳細説明
本プロジェクトのPythonスクリプトには多数の関数が含まれますが、提供された情報からは具体的な引数、戻り値、詳細なロジックを含んだ説明を生成できません。以下に、主要なスクリプトファイルとその中に含まれると予想される主要な関数の役割を説明します。

-   `src/generate_repo_list/generate_repo_list.py`:
    -   `main()`: スクリプトのエントリポイント。コマンドライン引数の解析、GitHubトークンの取得、リポジトリ情報のフェッチ、処理、Markdown生成といった一連の処理を統括します。
    -   `_parse_arguments()`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、リポジトリ数の上限などを取得します。
    -   `_get_github_token()`: GitHub APIへアクセスするためのトークンを安全に取得します。
-   `src/generate_repo_list/repository_processor.py`:
    -   `fetch_repositories(username)`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIから取得します。
    -   `process_repository_data(repo_raw_data)`: 取得した生のリポジトリデータを受け取り、表示に必要な形式に整形・加工します。
-   `src/generate_repo_list/markdown_generator.py`:
    -   `generate_markdown(processed_repos)`: 処理済みのリポジトリデータを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
-   `src/generate_repo_list/project_overview_fetcher.py`:
    -   `fetch_project_overview(repo_full_name, config)`: 指定されたリポジトリから、設定ファイルで定義されたパスにあるプロジェクト概要ファイルの内容（特に3行の説明）を抽出します。
-   `src/generate_repo_list/badge_generator.py`:
    -   `generate_language_badge(language)`: リポジトリの主要言語を示すバッジの情報を生成します。
    -   `generate_license_badge(license_name)`: リポジトリのライセンスを示すバッジの情報を生成します。
-   `src/generate_repo_list/config_manager.py`:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして提供します。
-   `src/generate_repo_list/date_formatter.py`:
    -   `format_date_for_display(datetime_obj)`: 日付時刻オブジェクトを受け取り、人間が読みやすい形式の文字列に変換します。
-   `src/generate_repo_list/url_utils.py`:
    -   `build_github_repo_url(username, repo_name)`: GitHubリポジトリの完全なURLを構築します。

## 関数呼び出し階層ツリー
```
提供された情報からは、関数呼び出し階層を詳細に分析できませんでした。

---
Generated at: 2026-11-14 07:07:12 JST
