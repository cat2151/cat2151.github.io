Last updated: 2026-04-03

# Project Overview

## プロジェクト概要
- GitHub PagesサイトのSEOを向上させるため、リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のMarkdownファイルを生成します。
- 各リポジトリの概要表示や分類、JSON-LDによるSEO最適化機能を提供します。

## 技術スタック
- フロントエンド: Jekyll/GitHub Pages (生成されたMarkdownコンテンツを表示するプラットフォーム)、Markdown (リポジトリ一覧の出力形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語)、GitHub API (リポジトリ情報の取得元)、Git (バージョン管理)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得からMarkdown生成までの一連の処理を実行)
- 言語機能: Pythonの標準ライブラリおよびファイルI/O、ネットワークリクエスト、設定ファイル解析などの機能
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリから推測される大規模ファイルチェックなどの自動化処理)
- 開発標準: ruff (Pythonコードのフォーマットとリントを自動化し、コード品質を維持)

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
- **`.editorconfig`**: エディタ全体でコードスタイルを統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: 大容量ファイルをチェックするための自動化スクリプト群を格納するディレクトリです。
  - **`README.md`**: `check_large_files` 機能に関する説明です。
  - **`check-large-files.toml`**: `check_large_files` スクリプトの設定ファイルです。
  - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクト全体の目的、機能、使い方、開発ヒントなどを説明するメインのドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の構成設定ファイルです。
- **`assets/`**: GitHub Pagesサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
  - **`favicon-*.png`**: サイトのファビコン画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグに使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Googleサイト認証用のHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのルートページとなるMarkdownファイルで、このファイルにリポジトリ一覧が生成されます。
- **`issue-notes/22.md`**: プロジェクトの特定の課題に関するメモやドキュメントを格納するディレクトリおよびファイルです。
- **`manifest.json`**: ウェブアプリマニフェストファイルで、プログレッシブウェブアプリ（PWA）関連の設定を含みます。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要なPythonライブラリの依存関係リストです。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonライブラリの依存関係リストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか/しないかを指示するファイルです。
- **`ruff.toml`**: PythonのコードフォーマッタおよびリンターであるRuffの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージの初期化ファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧生成の主要ロジックを含むPythonパッケージです。
  - **`__init__.py`**: パッケージの初期化ファイルです。
  - **`badge_generator.py`**: リポジトリのバッジ（例: 言語バッジ、スター数バッジ）を生成または処理するロジックを含みます。
  - **`config.yml`**: プロジェクトの技術的なパラメータや設定（APIタイムアウト、キャッシュ設定など）を定義するYAMLファイルです。
  - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するロジックを提供します。
  - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
  - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなる主要なスクリプトです。GitHub APIからの情報取得、処理、Markdown生成を統括します。
  - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD）のテンプレートを提供します。
  - **`language_info.py`**: GitHubリポジトリの言語情報を取得、解析、表示するためのロジックを含みます。
  - **`markdown_generator.py`**: 最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを担当します。
  - **`project_overview_fetcher.py`**: 各リポジトリから `generated-docs/project-overview.md` ファイルを読み込み、3行の概要を抽出する機能を提供します。
  - **`readme_badge_extractor.py`**: リポジトリの `README.md` から既存のバッジ情報を抽出するロジックを含みます。
  - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に整形・加工するロジックです。
  - **`seo_template.yml`**: ページごとのSEOメタデータ（タイトル、説明など）のテンプレートを定義するYAMLファイルです。
  - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算する機能を提供します。
  - **`strings.yml`**: プロジェクト全体で使用される表示メッセージや文言を管理するためのYAMLファイルです。
  - **`template_processor.py`**: Markdownテンプレートの読み込み、変数置換、条件分岐などの処理を行うロジックを含みます。
  - **`url_utils.py`**: URLの生成、解析、検証などのユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能のテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストケースを格納するディレクトリです。
  - **`conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義するファイルです。
  - **`test_*.py`**: 各モジュールの単体・結合テストファイルです。

## 関数詳細説明
※プロジェクト全体から具体的な関数情報は提供されていないため、各ファイルの役割から想定される主要な関数を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: プロジェクトのエントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成の各ステップをオーケストレーションします。
    - `_get_repos()`: 指定されたユーザー名のリポジトリ情報をGitHub APIから取得します。
    - `_generate_markdown()`: 処理されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツを生成します。
- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge_url(badge_type, value)`: 指定された種類と値に基づき、バッジ画像のURLを生成します。
    - `get_language_badge(language)`: 指定されたプログラミング言語に対応するバッジのURLを取得します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(config_path)`: 指定されたパスからYAML設定ファイル（例: `config.yml`）を読み込み、Python辞書として返します。
    - `load_strings(strings_path)`: 指定されたパスからYAML文言ファイル（例: `strings.yml`）を読み込み、Python辞書として返します。
- **`src/generate_repo_list/date_formatter.py`**:
    - `format_date(iso_date_string, format_string="%Y年%m月%d日")`: ISO形式の日付文字列を指定されたフォーマットで整形します。
- **`src/generate_repo_list/language_info.py`**:
    - `get_top_languages(repo_languages, limit=3)`: リポジトリの言語使用率データから、主要な言語を複数取得します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_repo_section(repo_data, overview_text)`: 単一のリポジトリデータとその概要から、Markdown形式のリポジトリセクションを生成します。
    - `generate_index_markdown(repositories_data, config, strings)`: 複数のリポジトリデータと設定、文言情報から、全体の `index.md` ファイルのコンテンツを生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview(username, repo_name, config)`: 指定されたリポジトリの `generated-docs/project-overview.md` から3行のプロジェクト概要をHTTP経由で取得します。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
    - `extract_badges_from_readme(readme_content)`: READMEのMarkdownコンテンツからバッジのURLやテキストを抽出します。
- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repository_data(raw_repo_data)`: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出・変換します。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - `calculate_age_in_years(created_at)`: リポジトリの作成日時から経過年数を計算します。
- **`src/generate_repo_list/template_processor.py`**:
    - `render_template(template_content, context)`: テンプレート文字列内のプレースホルダーを、与えられたコンテキストデータで置換します。
- **`src/generate_repo_list/url_utils.py`**:
    - `build_github_api_url(username, endpoint)`: GitHub APIのエンドポイントURLを構築します。
    - `build_repo_url(username, repo_name)`: 指定されたユーザー名とリポジトリ名からGitHubリポジトリのURLを構築します。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**:
    - `main()`: 大容量ファイルチェックスクリプトのエントリポイント。リポジトリ内のファイルを走査し、設定された閾値を超えるファイルを報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-03 07:13:33 JST
