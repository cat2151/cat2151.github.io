Last updated: 2026-05-21

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得します。
- GitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧を自動生成します。
- 検索エンジンやLLMからの参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll, GitHub Pages (静的サイトジェネレーターとして最終的な表示基盤を提供)
- 音楽・オーディオ: 特になし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理システム), pytest (テストフレームワーク), ruff (Pythonリンター/フォーマッター), YAML (設定ファイル管理), TOML (秘密情報管理)
- テスト: pytest (Pythonコードのテスト実行)
- ビルドツール: Pythonスクリプト (Markdownコンテンツの生成ロジック), Jekyll (GitHub Pagesサイトのビルド処理)
- 言語機能: Python (GitHub API連携、データ処理), Markdown (出力コンテンツ形式), YAML (設定記述), TOML (秘密情報記述)
- 自動化・CI/CD: GitHub Pages (自動生成されたコンテンツのホスティングと公開), Pythonスクリプトによる自動生成
- 開発標準: ruff (Pythonコードの品質と一貫性を保つためのフォーマッター/リンター)

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
- **`.editorconfig`**: 開発者間でコードスタイル（インデント、改行など）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使い方を説明するドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大きなファイルの検出に関する設定を記述するTOMLファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きなファイルを特定・警告するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などを説明するメインドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動や設定を定義するファイルです。
- **`assets/favicon-16x16.png` など**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン（アイコン）の様々なサイズを格納しています。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグを目的としたPythonスクリプトです。
- **`generated-docs/`**: `generate_repo_list.py` によって生成されたドキュメント（例: 各リポジトリの `project-overview.md`）を格納するためのプレースホルダディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイルです。
- **`index.md`**: このスクリプトによって生成される、GitHub PagesサイトのトップページとなるMarkdownファイルです。リポジトリ一覧がここに記述されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブサイトをモバイルデバイスにインストールする際の表示情報（アプリ名、アイコンなど）を定義します。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の動作設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトが動作するために必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、どのページをクロールしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行う`ruff`ツールの設定ファイルです。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空のファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空のファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示されるバッジ（例: ステータスバッジ）の生成ロジックを管理するスクリプトです。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、主要な機能の技術的パラメータを設定するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で利用可能な状態にするためのモジュールです。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定の表示形式に整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの中核となるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイル（`index.md`など）を生成します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のため、リポジトリ情報をJSON-LD形式で構造化データとして埋め込むためのテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を取得、処理、表示するためのロジックを含みます。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報や設定に基づき、整形されたMarkdownコンテンツを生成するロジックをカプセル化しています。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジックです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリ情報を、表示に適した形に加工、フィルタリング、分類する主要な処理を行います。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータ（タイトル、ディスクリプションなど）を定義するためのテンプレート設定ファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: 各リポジトリの星の数、フォーク数、最終更新日などの統計情報を計算する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示される各種メッセージや文言を一元管理するためのYAMLファイルです。
- **`src/generate_repo_list/template_processor.py`**: Jekyllなどの静的サイトジェネレーターで利用されるテンプレート（例: Liquid）を処理し、動的なコンテンツを埋め込むためのモジュールです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するための単体テストスクリプトです。
- **`tests/conftest.py`**: `pytest`テストフレームワークにおいて、複数のテストファイルで共有されるフィクスチャやヘルパー関数を定義するためのファイルです。
- **`tests/test_badge_generator_integration.py`**: `badge_generator.py`モジュールのバッジ生成機能がシステム全体と連携して正しく動作するかを検証する結合テストです。
- **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトの機能をテストするファイルです。
- **`tests/test_config.py`**: `config_manager.py`による設定ファイルの読み込みと処理が正しく行われるかを検証するテストです。
- **`tests/test_date_formatter.py`**: `date_formatter.py`モジュールの日付整形機能が正しく動作するかを検証するテストです。
- **`tests/test_environment.py`**: プロジェクトの実行環境が期待通りに設定されているかを検証するテストです。
- **`tests/test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく機能するかを検証する統合テストです。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py`モジュールが正しいMarkdownコンテンツを生成するかを検証するテストです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py`がリポジトリ概要を正しく取得できるかを検証するテストです。
- **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールがREADMEからバッジ情報を正しく抽出できるかを検証するテストです。
- **`tests/test_repository_processor.py`**: `repository_processor.py`モジュールがGitHubリポジトリ情報を正しく処理できるかを検証するテストです。

## 関数詳細説明
提供された情報からは具体的な関数名やそのシグネチャは検出されませんでした。しかし、各ファイルが担う役割に基づき、以下の主要な機能が関数として実装されていると想定されます。

- **`generate_repo_list.py`**:
    - **`main()`**: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成をオーケストレートします。
    - **`_generate_markdown_output(username, output_file, limit)`**: 指定されたユーザー名とオプションに基づいて、リポジトリ一覧のMarkdownを生成し、指定されたファイルに出力します。
- **`repository_processor.py`**:
    - **`fetch_repositories(username, token)`**: GitHub APIを呼び出し、指定されたユーザーのリポジトリ情報を取得します。
    - **`process_repository_data(repo_data)`**: 取得した生のリポジトリデータを整形し、必要な情報のみを抽出・加工します。
    - **`filter_repositories(repositories, filters)`**: 特定の条件（例: アクティブ、アーカイブ、フォークなど）に基づいてリポジトリをフィルタリングします。
- **`project_overview_fetcher.py`**:
    - **`get_project_overview(repo_url, config)`**: 指定されたリポジトリから`project-overview.md`を読み込み、設定に基づいて概要の3行説明を抽出します。
- **`markdown_generator.py`**:
    - **`generate_repo_list_markdown(processed_repos, strings_data, config_data)`**: 処理済みのリポジトリデータと設定情報に基づき、GitHub Pages用のリポジトリ一覧Markdown文字列を生成します。
    - **`generate_repo_section(repo_info)`**: 個々のリポジトリの情報を元に、そのリポジトリのMarkdownセクションを生成します。
- **`config_manager.py`**:
    - **`load_config(config_path)`**: 指定されたパスからYAML設定ファイルを読み込みます。
    - **`load_secrets(secrets_path)`**: 指定されたパスからTOML形式の秘密情報ファイルを読み込みます（例: GitHubトークン）。

上記はファイル名から推測される主要な機能であり、具体的な引数や戻り値はプロジェクトの内部実装に依存します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-21 07:34:14 JST
