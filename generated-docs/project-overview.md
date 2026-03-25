Last updated: 2026-03-26

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・整理します。
- GitHub Pagesサイト（`*.github.io`）向けにSEOに最適化されたリポジトリ一覧Markdownファイルを生成します。
- 各リポジトリの概要文を自動取得し、検索エンジンのクロール対象となりやすい形で公開することで、プロジェクトの可視性を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターとして利用され、生成されたMarkdownファイルからHTMLサイトを構築・公開します。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python, GitHub API - Pythonはスクリプト実行環境として、GitHub APIはリポジトリ情報のプログラム的取得のために使用されます。
- テスト: Pytest - Pythonコードの単体テストおよび統合テストフレームワークとして、機能の正確性を保証します。
- ビルドツール: 該当なし（Jekyllが静的サイト生成を担いますが、別途ビルドツールとしては分類しません。）
- 言語機能: Python - プロジェクトの主要なプログラミング言語であり、データ処理やファイル生成のロジックを実装しています。
- 自動化・CI/CD: 該当なし（本プロジェクトはローカル開発重視の構成であり、CI/CDパイプラインは採用していません。）
- 開発標準: Ruff - Pythonコードのフォーマットとリンティングを自動化し、コードの一貫性と品質を保ちます。

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
-   **`.editorconfig`**: 異なる開発環境間でのコードスタイル（インデント、改行コードなど）の一貫性を定義する設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトが格納されるディレクトリです。
    -   **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトの説明ドキュメントです。
    -   **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイルです。
    -   **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定する設定ファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの概要、目的、機能、使用方法など、プロジェクトに関する包括的な情報を提供するメインドキュメントです。
-   **`_config.yml`**: Jekyllのサイト全体の設定ファイルです。GitHub Pagesの振る舞いをカスタマイズするために使用されます。
-   **`assets/`**: ウェブサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    -   **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）画像ファイルです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
-   **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要ファイル（`project-overview.md`）などが一時的、または永続的に格納される可能性のあるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: プロジェクトの主要な出力ファイルであり、生成されたリポジトリ一覧が記述されるGitHub PagesのトップページとなるMarkdownファイルです。
-   **`issue-notes/`**: プロジェクトの課題や検討事項に関するメモが格納されるディレクトリです。
    -   **`issue-notes/22.md`**: 特定の課題に関する詳細なメモです。
-   **`manifest.json`**: ウェブアプリケーションマニフェストファイルで、PWA (Progressive Web App) の設定情報を提供します。
-   **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
-   **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージをリストアップするファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージをリストアップするファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージを識別するためのファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリの特性に応じたバッジ（例：言語、ステータス）を生成または取得する機能を提供します。
        -   **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成に関する各種設定（プロジェクト概要機能の有効/無効、タイムアウトなど）を定義するファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理する機能を提供します。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の形式に整形する機能を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの中核となるスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する全体のフローを制御します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化(SEO)のための構造化データ（JSON-LD）のテンプレートファイルです。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語に関する情報を処理し、表示に役立つデータを提供する機能です。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツの構造を組み立て、生成する機能を提供します。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクトの概要説明を抽出し、取得する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから既存のバッジ情報（ビルドステータス、カバレッジなど）を抽出する機能です。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを受け取り、必要な追加情報の処理や整形を行う中核的なロジックです。
        -   **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータ（タイトル、ディスクリプションなど）のテンプレートを定義するファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算し、表示に利用できる形式で提供する機能です。
        -   **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するためのファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: マークダウン生成時に使用される様々なテンプレート（SEOテンプレートなど）を処理し、データと結合する機能を提供します。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証などのユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher`機能に関する単体テストまたは結合テストを記述したファイルです。
-   **`tests/`**: プロジェクト全体のテストコードが格納されるディレクトリです。
    -   **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
    -   **`tests/test_check_large_files.py`**: 大容量ファイルチェックツールのテストを記述したファイルです。
    -   **`tests/test_config.py`**: 設定管理機能に関するテストを記述したファイルです。
    -   **`tests/test_date_formatter.py`**: 日付整形機能のテストを記述したファイルです。
    -   **`tests/test_environment.py`**: 実行環境に関するテストを記述したファイルです。
    -   **`tests/test_integration.py`**: プロジェクトの主要なコンポーネント間の統合テストを記述したファイルです。
    -   **`tests/test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
    -   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
    -   **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを記述したファイルです。
    -   **`tests/test_repository_processor.py`**: リポジトリ処理機能のテストを記述したファイルです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルは特定の機能を担当する関数を含んでいます。具体的な関数名や詳細なシグネチャはプロジェクト情報に明記されていませんが、それぞれの役割に基づいて以下のような関数が存在すると考えられます。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **`main()`**: スクリプトのエントリーポイントです。コマンドライン引数をパースし、設定を読み込み、リポジトリ情報の取得から最終的なMarkdownファイルの生成まで、全体の処理フローを統括します。引数なし。システム終了コードを返します。
    -   **`get_user_repositories(username, github_token)`**: 指定されたGitHubユーザー名とトークンを使用して、GitHub APIからリポジトリの一覧を取得します。引数: `username` (str), `github_token` (str)。戻り値: リポジトリデータのリスト。
    -   **`process_all_repositories(repositories_data, config)`**: 取得した複数のリポジトリデータを受け取り、それぞれに対して追加情報（概要、バッジなど）の取得と処理を行います。引数: `repositories_data` (list), `config` (dict)。戻り値: 処理済みのリポジトリデータのリスト。
    -   **`output_markdown(markdown_content, output_filepath)`**: 生成されたMarkdownコンテンツを指定されたファイルパスに出力します。引数: `markdown_content` (str), `output_filepath` (str)。戻り値: なし。

-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **`fetch_project_overview(repo_url, target_file, section_title, config)`**: 指定されたリポジトリのURLから、`target_file`（例: `generated-docs/project-overview.md`）の内容を読み込み、`section_title`で指定されたセクションからプロジェクト概要の3行説明を抽出します。引数: `repo_url` (str), `target_file` (str), `section_title` (str), `config` (dict)。戻り値: 抽出された概要テキスト (list of str) または空のリスト。

-   **`src/generate_repo_list/repository_processor.py`**:
    -   **`process_single_repository(repo_data, config)`**: GitHub APIから取得した単一のリポジトリデータを受け取り、そのリポジトリに関する追加情報（プロジェクト概要、バッジ、言語情報、統計など）を収集・整形し、結合したデータ構造を生成します。引数: `repo_data` (dict), `config` (dict)。戻り値: 強化されたリポジトリデータ (dict)。

-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **`generate_repo_list_markdown(processed_repositories, seo_template, strings)`**: 処理済みのリポジトリデータ、SEOテンプレート、表示文言データを受け取り、それらを組み合わせて最終的なリポジトリ一覧のMarkdownコンテンツを生成します。引数: `processed_repositories` (list), `seo_template` (dict), `strings` (dict)。戻り値: 生成されたMarkdownコンテンツ (str)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-26 07:14:37 JST
