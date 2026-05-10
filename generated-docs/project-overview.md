Last updated: 2026-05-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- GitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- 検索エンジンでのリポジトリ発見性を高め、LLMによる参照失敗問題を緩和することを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: N/A (該当なし)
- 開発ツール: Python (主要開発言語), Git (バージョン管理), YAML (設定ファイル形式), TOML (設定ファイル形式)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub API経由でのリポジトリ情報取得およびMarkdown生成を行うカスタムスクリプト)
- 言語機能: Python (プログラム言語そのもの)
- 自動化・CI/CD: `.github_automation` ディレクトリ内のスクリプト (ファイルサイズチェックなどの特定の自動化処理)
- 開発標準: ruff (Pythonコードフォーマッター/リンター), EditorConfig (エディタ設定の統一)

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
-   **.editorconfig**: コードエディタの設定を統一し、異なる開発環境間でのフォーマットのばらつきを防ぐためのファイルです。
-   **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    -   **.github_automation/check_large_files/**: 大容量ファイルのコミットを防ぐためのスクリプトと設定を格納します。
        -   **README.md**: `check_large_files`機能に関する説明ドキュメントです。
        -   **check-large-files.toml**: 大容量ファイルチェックの設定を定義するTOML形式のファイルです。
        -   **scripts/check_large_files.py**: 大容量ファイルをチェックするPythonスクリプトです。
-   **.gitignore**: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイルです。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **README.md**: プロジェクトの概要、セットアップ方法、使い方、開発者向け情報などを記述したメインのドキュメントファイルです。
-   **_config.yml**: Jekyllサイト全体の挙動を設定するためのファイルです。GitHub Pagesの基本的な設定を定義します。
-   **assets/**: GitHub Pagesサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   **favicon-16x16.png**: 16x16ピクセルのファビコン画像です。
    -   **favicon-192x192.png**: 192x192ピクセルのファビコン画像です。
    -   **favicon-32x32.png**: 32x32ピクセルのファビコン画像です。
    -   **favicon-512x512.png**: 512x512ピクセルのファビコン画像です。
-   **debug_project_overview.py**: `project_overview`機能のデバッグやテストに使用される独立したスクリプトです。
-   **generated-docs/**: 自動生成されたドキュメント（例: 各リポジトリの`project-overview.md`）の格納を想定したディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認（認証）のために配置されるHTMLファイルです。
-   **index.md**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。主要なリポジトリ一覧がここに自動生成され出力されます。
-   **issue-notes/22.md**: 特定のIssue番号（ここでは#22）に関するメモや詳細を記述したファイルです。
-   **manifest.json**: Webアプリケーションマニフェスト。PWA（プログレッシブウェブアプリ）などで使用され、アプリの表示方法や動作を定義します。
-   **pytest.ini**: `pytest`テストフレームワークの挙動を設定するためのファイルです。
-   **requirements-dev.txt**: 開発およびテスト環境で必要なPythonパッケージの依存関係を定義するファイルです。
-   **requirements.txt**: 本番環境でこのプロジェクトが動作するために必要なPythonパッケージの依存関係を定義するファイルです。
-   **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
-   **ruff.toml**: `ruff`リンター/フォーマッターのルールや設定を定義するTOML形式のファイルです。
-   **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示す初期化ファイルです。
    -   **src/generate_repo_list/**: リポジトリ一覧自動生成システムの主要なロジックを格納するPythonパッケージです。
        -   **src/generate_repo_list/__init__.py**: `generate_repo_list`パッケージの初期化ファイルです。
        -   **src/generate_repo_list/badge_generator.py**: リポジトリの各種バッジ（例: 言語、ステータス）を生成するためのロジックを含みます。
        -   **src/generate_repo_list/config.yml**: リポジトリ一覧生成に関する各種設定（例: `project_overview`機能の有効/無効、対象ファイルなど）を定義するYAMLファイルです。
        -   **src/generate_repo_list/config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するためのクラスや関数を提供します。
        -   **src/generate_repo_list/date_formatter.py**: 日付のフォーマットに関するユーティリティ関数（例: ISO形式から人間が読みやすい形式への変換）を含みます。
        -   **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成までの全プロセスを orchestrate します。
        -   **src/generate_repo_list/json_ld_template.json**: JSON-LD形式の構造化データテンプレート。SEO最適化の一環として、リポジトリ情報を検索エンジンに提供するために使用されます。
        -   **src/generate_repo_list/language_info.py**: リポジトリの言語情報を処理・整形し、主要なプログラミング言語などを特定するロジックを含みます。
        -   **src/generate_repo_list/markdown_generator.py**: 取得および処理されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを含みます。
        -   **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出するロジックを含みます。
        -   **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルの内容(`readme_content`)から、既存のバッジの画像URLやリンク情報を抽出します。
        -   **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した個々のリポジトリデータを整形し、表示に必要な追加情報（分類、リンク、メタデータなど）を付与するロジックを含みます。
        -   **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算または集計するロジックを含みます。
        -   **src/generate_repo_list/strings.yml**: UIに表示されるメッセージや文言を管理する国際化/ローカライズ用ファイルです。
        -   **src/generate_repo_list/template_processor.py**: Markdown生成時に使用するテンプレートを読み込み、データと組み合わせて最終コンテンツをレンダリングするロジックを含みます。
        -   **src/generate_repo_list/url_utils.py**: GitHub APIのエンドポイントURLやリポジトリのWeb URLなど、URLに関連するユーティリティ関数を提供します。
-   **test_project_overview.py**: `project_overview_fetcher`機能に関する単体テストを記述したファイルです。
-   **tests/**: プロジェクトの各種テストスクリプトを格納するディレクトリです。
    -   **conftest.py**: `pytest`のテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義するファイルです。
    -   **test_badge_generator_integration.py**: `badge_generator`モジュールの結合テストを記述したファイルです。
    -   **test_check_large_files.py**: `.github_automation/check_large_files`機能のテストを記述したファイルです。
    -   **test_config.py**: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    -   **test_date_formatter.py**: `date_formatter`モジュールのテストを記述したファイルです。
    -   **test_environment.py**: テスト環境の設定や依存関係に関するテストを記述したファイルです。
    -   **test_integration.py**: プロジェクトの主要なフローに関する統合テストを記述したファイルです。
    -   **test_markdown_generator.py**: `markdown_generator`モジュールのテストを記述したファイルです。
    -   **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテストを記述したファイルです。
    -   **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのテストを記述したファイルです。
    -   **test_repository_processor.py**: `repository_processor`モジュールのテストを記述したファイルです。

## 関数詳細説明
以下の主要なPythonファイルに含まれると推測される関数の役割と機能について説明します。具体的な引数や戻り値は提供情報にないため、一般的な想定に基づきます。

-   **src/generate_repo_list/generate_repo_list.py**
    -   `main()`: このスクリプトのエントリポイントです。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力という一連のプロセスを制御します。
    -   `get_repositories(username, limit)`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIから取得します。`limit`オプションで取得数を制限できます。
    -   `generate_output(repositories, output_file)`: 取得・処理されたリポジトリ情報を受け取り、Markdown形式のコンテンツを生成して指定されたファイルに書き出します。

-   **src/generate_repo_list/repository_processor.py**
    -   `process_repository(repo_data, config)`: GitHub APIから取得した個々のリポジトリの生データ(`repo_data`)を受け取り、表示に必要な情報（カテゴリ、バッジ、プロジェクト概要など）を抽出・追加して整形されたリポジトリオブジェクトを返します。

-   **src/generate_repo_list/markdown_generator.py**
    -   `generate_markdown(processed_repositories, config)`: `repository_processor`によって処理されたリポジトリのリスト(`processed_repositories`)を受け取り、JekyllベースのGitHub Pagesに適したMarkdown形式のリポジトリ一覧コンテンツ全体を生成します。
    -   `_format_repo_entry(repo_item)`: 個々のリポジトリ項目をMarkdown形式で表現するための文字列を生成する内部ヘルパー関数です。

-   **src/generate_repo_list/project_overview_fetcher.py**
    -   `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリ (`repo_name`, `owner`) の `generated-docs/project-overview.md` ファイルから「プロジェクト概要」セクションの3行説明を自動取得し、文字列として返します。設定(`config`)に基づいてキャッシュやリトライ処理を行います。

-   **src/generate_repo_list/badge_generator.py**
    -   `generate_badge_markdown(badge_type, value)`: 指定されたバッジの種類(`badge_type`)と値(`value`)に基づいて、Markdown形式で表示可能なバッジ文字列を生成します。

-   **src/generate_repo_list/config_manager.py**
    -   `load_config(config_path)`: 指定されたパス(`config_path`)からYAML形式の設定ファイルを読み込み、設定内容をPythonオブジェクトとして返します。

-   **src/generate_repo_list/date_formatter.py**
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列(`iso_date_string`)を受け取り、人間が読みやすい形式（例: "YYYY年MM月DD日"）に整形して返します。

-   **src/generate_repo_list/language_info.py**
    -   `get_language_data(repo_languages_url)`: GitHub APIの言語エンドポイントURL(`repo_languages_url`)からリポジトリの言語分布データを取得し、主要なプログラミング言語情報などを返します。

-   **src/generate_repo_list/readme_badge_extractor.py**
    -   `extract_badges_from_readme(readme_content)`: リポジトリのREADMEファイルの内容(`readme_content`)から、既存のバッジの画像URLやリンク情報を抽出します。

-   **src/generate_repo_list/statistics_calculator.py**
    -   `calculate_repo_statistics(repo_data)`: GitHub APIから取得したリポジトリデータ(`repo_data`)から、スター数、フォーク数、最終更新日時などの統計情報を計算または抽出し、返します。

-   **src/generate_repo_list/template_processor.py**
    -   `render_template(template_content, context)`: テンプレートのコンテンツ(`template_content`)と、レンダリングに必要なデータ(`context`)を受け取り、最終的な文字列コンテンツを生成します。

-   **src/generate_repo_list/url_utils.py**
    -   `build_github_api_url(username)`: 指定されたGitHubユーザー名(`username`)に基づいて、GitHub APIのリポジトリ一覧エンドポイントURLを構築します。
    -   `build_repo_url(username, repo_name)`: 指定されたGitHubユーザー名(`username`)とリポジトリ名(`repo_name`)に基づいて、GitHubリポジトリのWebページのURLを構築します。

-   **.github_automation/check_large_files/scripts/check_large_files.py**
    -   `check_files_for_size(config_path)`: 設定ファイル(`config_path`)で定義されたルールに基づき、リポジトリ内のファイルサイズをチェックし、大きすぎるファイルを検出します。

## 関数呼び出し階層ツリー
```
提供された情報では、詳細な関数呼び出し階層ツリーを自動分析できませんでした。
しかし、プロジェクトの主要な処理フローは以下のようであると推測されます。

1. `src/generate_repo_list/generate_repo_list.py` の `main()` 関数がプログラムの実行を開始します。
2. `main()` は、まず `src/generate_repo_list/config_manager.py` を使用して設定ファイル (`config.yml`、`secrets.toml`など) を読み込みます。
3. 次に、GitHub APIクライアントを通じてユーザーのリポジトリ情報を取得します。この際、`src/generate_repo_list/url_utils.py` でAPI URLが構築されることがあります。
4. 取得した各リポジトリデータは、`src/generate_repo_list/repository_processor.py` の `process_repository()` 関数に渡され、詳細な処理が行われます。
5. `process_repository()` の中で、必要に応じて以下のモジュールが呼び出されます。
    -   `src/generate_repo_list/project_overview_fetcher.py` の `fetch_project_overview()` で各リポジトリの概要を取得します。
    -   `src/generate_repo_list/language_info.py` で言語情報を処理します。
    -   `src/generate_repo_list/statistics_calculator.py` で統計情報を計算します。
    -   `src/generate_repo_list/readme_badge_extractor.py` や `src/generate_repo_list/badge_generator.py` でバッジ情報を処理・生成します。
    -   `src/generate_repo_list/date_formatter.py` で日付を整形します。
6. 全てのリポジトリが処理された後、`src/generate_repo_list/markdown_generator.py` の `generate_markdown()` 関数が、処理済みのリポジトリデータと `src/generate_repo_list/template_processor.py` を用いて、最終的なMarkdownコンテンツを生成します。
7. 生成されたMarkdownコンテンツは、`main()` 関数に戻り、指定された出力ファイル（例: `index.md`）に書き出されます。

---
Generated at: 2026-05-11 07:20:03 JST
