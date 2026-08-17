Last updated: 2026-08-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにMarkdown形式のリポジトリ一覧を生成します。
- これにより、サイトのSEOを向上させ、検索エンジンやLLMからのリポジトリ参照性を高めます。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages** (静的サイトジェネレーターとして利用し、HTML/CSS/JavaScriptを生成), **Markdown** (リポジトリ一覧のコンテンツ記述), **HTML** (生成される最終的なWebページのマークアップ), **JSON-LD** (SEO最適化のための構造化データ)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用していません。
- 開発ツール: **Python** (主要なスクリプト言語), **Git** (バージョン管理システム), **Visual Studio Code** (一般的な開発エディタとして想定)
- テスト: **pytest** (Python用テストフレームワーク)
- ビルドツール: **Pythonスクリプト** (`generate_repo_list.py` がMarkdownを生成), **Jekyll** (GitHub Pages側でMarkdownからWebページを構築)
- 言語機能: **Python** (標準ライブラリによるファイルI/O, HTTPリクエスト, YAML/TOMLパース, 文字列操作など)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得), GitHub Pages (自動デプロイ機能)。ただし、本プロジェクトはローカル開発重視であり、明示的なCI/CDパイプラインは現状では最小限です。
- 開発標準: **ruff** (Pythonコードのフォーマットとリンティング), **.editorconfig** (エディタのコーディングスタイル統一設定)

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
- **.editorconfig**: 異なるエディタやIDE間で基本的なコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなど、リポジトリ自動化に関連するスクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルがリポジトリに追加されていないかをチェックする機能のサブディレクトリです。
        - **README.md**: `check_large_files` 機能の説明ドキュメントです。
        - **check-large-files.toml**: `check_large_files` 機能の設定ファイルです。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内で設定されたしきい値を超える大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **README.md**: プロジェクト全体の概要、目的、使用方法、設定、ライセンスなど、プロジェクトに関する包括的な情報を提供するドキュメントです。
- **_config.yml**: GitHub Pages（Jekyll）サイトの全体的な設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
- **assets/**: Webサイトで使用される画像、ファビコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズ画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのプロジェクト概要取得機能をデバッグするための補助スクリプトです。
- **generated-docs/**: 各リポジトリから自動的に取得されるプロジェクト概要ドキュメント（例: `project-overview.md`）が格納されることが想定されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのGoogleサービスでサイトの所有権を確認するために使用される検証ファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **issue-notes/22.md**: 課題や改善点に関するメモを格納するディレクトリおよびファイルです。この例では「22.md」という課題に関するメモが含まれています。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、Webアプリをユーザーのホーム画面に追加する際の情報（アプリ名、アイコン、表示モードなど）を提供します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイルです。テストの検出方法、オプションなどが定義されます。
- **requirements-dev.txt**: プロジェクトの開発およびテスト時に必要なPythonパッケージとそのバージョンを記述したファイルです。
- **requirements.txt**: プロジェクトの実行時に最低限必要なPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールして良いか、またはクロールしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonの高速リンター/フォーマッターである`ruff`の設定ファイルです。コードスタイルや静的解析のルールが定義されます。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **__init__.py**: Pythonのパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成するシステムの主要なモジュール群を格納するパッケージです。
        - **__init__.py**: `generate_repo_list` パッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリに関連するステータスバッジ（例: ビルド状態、ライセンス）を生成または処理するロジックを実装しています。
        - **config.yml**: `generate_repo_list` スクリプトの実行時に使用される設定（例: プロジェクト概要取得の有効/無効、対象ファイルパス）を定義するYAMLファイルです。
        - **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのクラスや関数を提供します。
        - **date_formatter.py**: GitHub APIから取得した日付情報を、表示に適した形式にフォーマットする機能を提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、その情報に基づいてMarkdown形式のリポジトリ一覧を生成します。
        - **json_ld_template.json**: SEO最適化のために、Webページに埋め込む構造化データ（JSON-LD）のテンプレートファイルです。
        - **language_info.py**: リポジトリの使用言語情報を処理し、表示に適した形式に変換する機能を提供します。
        - **markdown_generator.py**: 取得したリポジトリ情報とテンプレートに基づいて、Markdown形式のコンテンツを生成するロジックを実装しています。
        - **project_overview_fetcher.py**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクトの概要説明を抽出し、取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: shields.io形式のバッジURL）を抽出するロジックです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理で利用しやすい形式に変換する役割を担います。
        - **seo_template.yml**: WebページのSEOメタデータ（タイトル、ディスクリプションなど）に関するテンプレート設定を定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIに表示されるメッセージ、文言、ラベルなどを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - **template_processor.py**: Markdown生成に使用されるテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なMarkdownコンテンツを生成するロジックです。
        - **url_utils.py**: URLの生成、解析、エンコードなど、URL操作に関するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher` モジュールにおけるプロジェクト概要取得機能の単体テストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **conftest.py**: `pytest`の共通フィクスチャやヘルパー関数、テスト設定などを定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator.py`の機能を統合的にテストするスクリプトです。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py` の機能をテストするスクリプトです。
    - **test_config.py**: 設定ファイル（例: `config.yml`, `strings.yml`）の読み込みや管理機能が正しく動作するかをテストするスクリプトです。
    - **test_date_formatter.py**: `date_formatter.py`の機能が正しく日付をフォーマットするかをテストするスクリプトです。
    - **test_environment.py**: テスト実行環境の設定や依存関係が適切であるかを確認するテストスクリプトです。
    - **test_integration.py**: `generate_repo_list` システム全体の主要な処理フローが連携して正しく動作するかをテストする統合テストスクリプトです。
    - **test_markdown_generator.py**: `markdown_generator.py`の機能が正しくMarkdownコンテンツを生成するかをテストするスクリプトです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`の機能が正しくプロジェクト概要を抽出できるかをテストするスクリプトです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor.py`の機能が`README.md`から正しくバッジを抽出できるかをテストするスクリプトです。
    - **test_repository_processor.py**: `repository_processor.py`の機能がGitHub APIからのリポジトリデータを正しく処理・整形するかをテストするスクリプトです。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main()`: スクリプトのエントリポイント。コマンドライン引数をパースし、リポジトリ一覧生成の主要な処理を呼び出します。
    - `generate_repo_list(username, output_file, limit=None)`: 指定されたユーザー名のリポジトリ情報をGitHub APIから取得し、Markdown形式で整形して指定された出力ファイルに書き出します。`limit`は処理するリポジトリ数の上限（開発用）。
- **repository_processor.py**:
    - `fetch_repositories(username, token)`: GitHub APIを使用して、指定されたユーザーのリポジトリ情報を取得します。認証にはGitHubトークンを使用します。
    - `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすい形式に整形・フィルタリングします。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLから、設定ファイルで定義されたパスにある `project-overview.md` ファイルを読み込み、プロジェクトの概要説明を抽出します。
- **markdown_generator.py**:
    - `generate_markdown(repositories_info, config, strings)`: 処理済みのリポジトリ情報、設定、および表示用の文字列データに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- **config_manager.py**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイル（例: `config.yml`）を読み込み、Pythonオブジェクトとして返します。
    - `load_strings(strings_path)`: 指定されたパスからYAML形式の文字列定義ファイル（例: `strings.yml`）を読み込み、表示メッセージなどを取得します。
- **date_formatter.py**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列（GitHub APIから取得）を、ユーザーフレンドリーな形式に変換して返します。
- **badge_generator.py**:
    - `generate_badge(badge_type, value)`: 指定されたタイプと値に基づいて、バッジ（例: ライセンス、言語）のURLやMarkdownスニペットを生成します。
- **readme_badge_extractor.py**:
    - `extract_badges_from_readme(readme_content)`: リポジトリの`README.md`コンテンツから、特定のパターン（例: shields.io形式）に一致するバッジのURLを抽出します。
- **statistics_calculator.py**:
    - `calculate_statistics(repo_list)`: リポジトリのリスト全体から、合計スター数、フォーク数などの統計情報を計算します。
- **template_processor.py**:
    - `process_template(template_path, data)`: 指定されたテンプレートファイル（例: Markdownテンプレート）を読み込み、提供されたデータでプレースホルダーを置換して最終コンテンツを生成します。
- **url_utils.py**:
    - `build_github_api_url(endpoint, params)`: GitHub APIのエンドポイントとパラメータから完全なAPIリクエストURLを構築します。
    - `build_repo_overview_url(repo_full_name, file_path)`: 特定のリポジトリ内のファイルへのURLを構築します。
- **check_large_files.py**:
    - `check_files(config_path, repo_root)`: 設定ファイルに基づいて、指定されたリポジトリ内で定義されたしきい値を超える大容量ファイルをチェックします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-18 07:06:53 JST
