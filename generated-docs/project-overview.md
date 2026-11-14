Last updated: 2026-11-15

# Project Overview

## プロジェクト概要
- GitHub Pages用のリポジトリ一覧を自動生成し、SEOを強化するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のMarkdownを出力します。
- 検索エンジンからのクロール向上とLLMの参照失敗緩和を目的としています。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesで動作する静的サイトジェネレータ。生成されたMarkdownを元にウェブサイトを構築します。
    - **Markdown**: Jekyllサイトのコンテンツ記述形式。本プロジェクトは最終的にMarkdownファイルを生成します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: リポジトリ情報の取得、処理、Markdown生成の中心となるスクリプト言語です。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために使用されます。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に利用されます。
    - **TOML**: 設定ファイル（`pytest.ini`, `ruff.toml`）やシークレット情報（`secrets.toml`）の記述に利用されます。
- テスト:
    - **pytest**: Pythonコードの単体テスト、統合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py` が実質的なMarkdownファイル生成の「ビルド」を担います。
    - **Jekyll**: 生成されたMarkdownファイルをHTML形式のウェブサイトとして「ビルド」します。
- 言語機能:
    - **Python**: 高度なスクリプト機能やライブラリを活用し、API連携やファイル操作、文字列処理を行います。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリの存在から、コード品質チェックやデプロイなどの自動化に利用されていると推測されます。
- 開発標準:
    - **ruff**: Pythonコードの高速リンターおよびフォーマッター。コード品質の維持と統一されたコーディングスタイルを強制します。
    - **.editorconfig**: 異なるエディタ間でのコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
- **`.editorconfig`**: コードエディタ間でインデントスタイル、文字コード、改行コードなどの基本的な書式設定を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files` ディレクトリ内の機能や使い方に関する説明ドキュメントです。
    - **`check_large_files/check-large-files.toml`**: 大規模なファイルが存在しないかチェックするための設定が記述されています。
    - **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大規模なファイルを検出し、警告またはエラーを出すPythonスクリプトです。
- **`.gitignore`**: Gitによるバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法、テスト方法など、プロジェクト全体の概要を説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイトの全体的な設定（サイト名、テーマ、プラグインなど）を定義するファイルです。
- **`assets/`**: ウェブサイトで使用される画像やその他の静的ファイルを格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるファビコン画像ファイルです（各種サイズ）。
- **`debug_project_overview.py`**: `project_overview` 機能（各リポジトリ概要の取得）の動作確認やデバッグを目的としたスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（例: project-overview.md）が格納される、または参照されるパスを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどでサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: 生成されたリポジトリ一覧が書き出されるメインのMarkdownファイルで、GitHub Pagesのトップページとして表示されます。
- **`issue-notes/22.md`**: 特定のイシュー（課題）に関連するメモや考察を記述したファイルです。ここではイシュー番号22に関するものです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリのメタデータやホーム画面への追加設定を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの検出ルールやオプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトが動作するために必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、どのページをクロールしてよいか、どのページをクロールしてはいけないかを指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびFormatterである `ruff` の設定ファイルです。コードのスタイルチェックや自動修正のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが配置されるディレクトリです。
    - **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やライセンスなどの情報を元に、表示用のバッジ（画像やテキスト）を生成するロジックが含まれます。
    - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの動作を制御するための技術的パラメータが定義された設定ファイルです。
    - **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供します。
    - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマット（例: `YYYY-MM-DD`）に変換するためのユーティリティ関数を提供します。
    - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力ファイルを生成する全体のフローを制御します。
    - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、JSON-LD形式の構造化データを出力する際のテンプレートファイルです。
    - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・分析するためのロジックが含まれます。
    - **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリデータを基に、最終的なMarkdownコンテンツ（例: リポジトリ一覧、各リポジトリの詳細）を生成するロジックを提供します。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するロジックが含まれます。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、表示や処理に適した内部データ構造に変換・整形する役割を担います。
    - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）関連のメタデータやコンテンツ構造に関するテンプレート設定が記述されています。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算し、表示用に提供するロジックが含まれます。
    - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言（タイトル、説明文など）を一元的に管理するための設定ファイルです。多言語化にも対応しやすい構造です。
    - **`src/generate_repo_list/template_processor.py`**: 生成するMarkdownコンテンツの構造を定義するテンプレートを読み込み、データに基づいて埋め込み処理を行う機能を提供します。
    - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、正規化など、URLに関する一般的なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: `pytest` のテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py` モジュールの統合テストを行い、バッジ生成が期待通りに機能するかを検証します。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` の動作を検証するテストです。
    - **`test_config.py`**: `config_manager.py` や関連する設定ファイルの読み込み、パースが正しく行われるかをテストします。
    - **`test_date_formatter.py`**: `date_formatter.py` モジュール内の日付フォーマット機能が正しく動作するかを検証します。
    - **`test_environment.py`**: プロジェクトの実行環境（依存関係、必要な環境変数など）が正しく設定されているかを検証するテストです。
    - **`test_integration.py`**: `generate_repo_list.py` を中心とした、プロジェクト全体の主要な機能の連携動作を検証する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py` モジュールが正しくMarkdownコンテンツを生成するかを検証します。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` の単体テストを行い、概要取得機能が期待通りに動作するかを検証します。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py` モジュールが `README.md` からバッジ情報を正確に抽出できるかを検証します。
    - **`test_repository_processor.py`**: `repository_processor.py` モジュールがGitHub APIからのリポジトリデータを正しく処理・変換できるかを検証します。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャ（引数、戻り値）を抽出できませんでした。以下に、各Pythonファイルが担当する主要な役割と、それに伴い含まれるであろう関数の概要を説明します。

- **`src/generate_repo_list/badge_generator.py`**:
    - **役割**: リポジトリの属性（言語、ライセンス、アーカイブ状態など）に基づいて、視覚的なバッジ情報を生成します。
    - **含まれるであろう関数**: `generate_language_badge(language_name: str, color: str) -> str`, `generate_license_badge(license_key: str) -> str`, `generate_archive_badge(is_archived: bool) -> str` など、特定の情報を受け取り、バッジとして表示されるMarkdownまたはHTML文字列を返す関数群。
- **`src/generate_repo_list/config_manager.py`**:
    - **役割**: YAML形式の設定ファイル（`config.yml`、`strings.yml`など）を読み込み、アプリケーション全体でアクセス可能な設定オブジェクトを提供します。
    - **含まれるであろう関数**: `load_config(config_path: str) -> dict`, `get_setting(key_path: str, default=None) -> Any` など、ファイルパスを指定して設定全体を読み込んだり、特定のキーパスで設定値を取得したりする関数。
- **`src/generate_repo_list/date_formatter.py`**:
    - **役割**: 日付や時刻データを指定された形式で整形するユーティリティ機能を提供します。
    - **含まれるであろう関数**: `format_date_ymd(iso_date_string: str) -> str` など、ISO形式の日付文字列を受け取り、「YYYY-MM-DD」形式などの表示しやすい文字列に変換する関数。
- **`src/generate_repo_list/generate_repo_list.py`**:
    - **役割**: プロジェクト全体の実行エントリポイント。GitHub APIからリポジトリ情報を取得し、各リポジトリの処理を行い、最終的なMarkdownファイルを生成する一連の流れを管理します。
    - **含まれるであろう関数**: `main()` (スクリプトの実行開始点), `_parse_arguments() -> argparse.Namespace` (コマンドライン引数を解析), `_fetch_and_process_repos(username: str, limit: int) -> list[dict]` (リポジトリの取得と処理), `_write_output(output_path: str, content: str)` (結果の書き出し) など。
- **`src/generate_repo_list/language_info.py`**:
    - **役割**: リポジトリのプログラミング言語に関する統計情報（主要言語、使用割合など）を処理し、表示に適した形式に変換します。
    - **含まれるであろう関数**: `get_main_language(languages: dict) -> str`, `get_language_breakdown(languages: dict) -> list[dict]` など、GitHub APIから得られる言語使用率データから主要言語を特定したり、詳細な言語の内訳を生成したりする関数。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **役割**: 処理されたリポジトリデータを受け取り、Jekyllの要件に合わせたMarkdown形式のコンテンツを生成します。
    - **含まれるであろう関数**: `generate_index_markdown(repositories_data: list[dict], seo_data: dict) -> str`, `_create_repo_section(repo_item: dict) -> str` など、リポジトリのリスト全体からメインの`index.md`コンテンツを生成したり、各リポジトリの個別のセクションを生成したりする関数。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **役割**: 他のリポジトリの特定のファイル（`generated-docs/project-overview.md`）から、そのリポジトリの3行概要をHTTPリクエストを通じて取得します。
    - **含まれるであろう関数**: `fetch_project_overview(repo_url: str, file_path: str) -> str` など、リポジトリのURLとファイルパスを指定して、その内容から指定された形式の概要テキストを抽出して返す関数。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
    - **役割**: 各リポジトリの`README.md`を解析し、そこに埋め込まれている既存のバッジ（例: ビルドステータス、ライセンス）の情報を抽出します。
    - **含まれるであろう関数**: `extract_badges_from_readme(readme_content: str) -> list[dict]` など、Markdown形式のREADMEコンテンツを受け取り、そこから画像やリンク形式のバッジを識別し、その情報をリストで返す関数。
- **`src/generate_repo_list/repository_processor.py`**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、アプリケーション内で扱いやすいカスタムオブジェクトまたは辞書の形式に変換・整形します。不要な情報をフィルタリングしたり、必要な情報を追加したりします。
    - **含まれるであろう関数**: `process_repository_data(raw_repo_data: dict) -> dict`, `_filter_repo(repo: dict) -> bool` など、APIレスポンスの辞書を受け取り、加工済みの辞書を返す関数。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - **役割**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、表示用のデータとして提供します。
    - **含まれるであろう関数**: `calculate_repo_statistics(repo_data: dict) -> dict` など、リポジトリデータを受け取り、統計情報をまとめた辞書を返す関数。
- **`src/generate_repo_list/template_processor.py`**:
    - **役割**: Markdown生成の際に使用されるテンプレートファイル（例: `seo_template.yml`）を読み込み、プレースホルダーを実際のデータで置き換える処理を行います。
    - **含まれるであろう関数**: `load_template(template_path: str) -> str`, `render_template(template_content: str, data: dict) -> str` など、テンプレートファイルから内容を読み込み、指定されたデータで埋め込みを実行する関数。
- **`src/generate_repo_list/url_utils.py`**:
    - **役割**: URLの構築、解析、クリーンアップなど、URLに関する一般的なユーティリティ機能を提供します。
    - **含まれるであろう関数**: `build_github_api_url(username: str) -> str`, `build_github_repo_url(username: str, repo_name: str) -> str` など、GitHub APIエンドポイントやリポジトリURLを正確に構築する関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-15 07:07:16 JST
