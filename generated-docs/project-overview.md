Last updated: 2025-12-23

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ情報を自動生成するシステムです。
- GitHub APIからリポジトリデータを取得し、SEO最適化されたMarkdown形式で出力します。
- 検索エンジンやLLMからの参照性を向上させ、プロジェクトの認知度と開発効率を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (テストフレームワーク), ruff (コードリンター), secrets.toml (シークレット管理), config.yml (設定管理), strings.yml (文言管理)
- テスト: pytest (Pythonコードの単体・統合テスト)
- ビルドツール: Python (リポジトリ情報の取得・加工・Markdown生成を行うスクリプト実行環境)
- 言語機能: Python (プロジェクトの主要な開発言語)
- 自動化・CI/CD: (CI/CD不要のローカル開発重視。GitHub Pagesへのデプロイは別途GitHub Actionsなどで行われることを想定)
- 開発標準: ruff (コードスタイルの自動修正・チェック), requirements.txt / requirements-dev.txt (依存関係管理)

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方、設定、ライセンスなどを説明する主要なドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバル設定を定義するファイル。
- **`assets/`**: サイトで利用される画像（例: ファビコン）などの静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の各種サイズ。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` モジュールのデバッグや単体テスト実行のために使用される補助スクリプト。
- **`generated-docs/`**: 各リポジトリから取得した `project-overview.md` など、自動生成されたドキュメントを格納することが想定されるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるファイル。
- **`index.md`**: `generate_repo_list.py` スクリプトによって自動生成される、リポジトリ一覧を記述したメインのMarkdownファイル。GitHub Pagesのトップページとして表示される。
- **`issue-notes/`**: 開発中に発生した特定の課題や検討事項について記録されたMarkdown形式のメモファイル群。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。ウェブアプリの名前、アイコン、表示方法などを定義する。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の挙動をカスタマイズするための設定ファイル。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記述するファイル。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンを記述するファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイル。コードスタイルや潜在的なバグのチェックルールを定義する。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    - **`src/generate_repo_list/`**: GitHubリポジトリ一覧生成ロジックのコア部分を含むPythonパッケージ。
        - **`__init__.py`**: Pythonパッケージであることを示すファイル。
        - **`badge_generator.py`**: リポジトリの言語やライセンスなどの情報から、表示用のバッジ画像を生成または整形するロジックを扱うモジュール。
        - **`config.yml`**: プロジェクト概要取得機能など、システム全体の技術的パラメータや動作設定を定義するYAMLファイル。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、アプリケーション内で利用可能な形式で管理するモジュール。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理をオーケストレーションする。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために使用されるJSON-LD形式の構造化データテンプレート。
        - **`language_info.py`**: GitHubリポジトリの言語使用状況に関する情報を取得、処理、整形するロジックを含むモジュール。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、最終的なリポジトリ一覧のMarkdown形式コンテンツを生成するロジックを担うモジュール。
        - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得する機能を提供するモジュール。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出、フィルタリング、整形するロジックを含むモジュール。
        - **`seo_template.yml`**: SEO関連のメタデータ（タイトル、説明など）やテンプレートの構造を定義するYAMLファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計するロジックを扱うモジュール。
        - **`strings.yml`**: アプリケーションで表示されるメッセージ、ラベル、文言などを一元的に管理するためのYAMLファイル。多言語対応の基盤にもなり得る。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレートを読み込み、リポジトリデータを埋め込んで最終的な文字列を生成するモジュール。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールに関連するテストケースを定義するスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`test_config.py`**: 設定管理 (`config_manager.py`) 関連モジュールのテスト。
    - **`test_environment.py`**: 実行環境や外部依存関係に関するテスト。
    - **`test_integration.py`**: システムの異なるコンポーネメントが連携して正しく動作するかを確認する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成ロジック (`markdown_generator.py`) のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテスト。
    - **`test_repository_processor.py`**: リポジトリ情報処理ロジック (`repository_processor.py`) のテスト。

## 関数詳細説明
このプロジェクトではPythonスクリプトが中心となっており、具体的な関数名や引数、戻り値の詳細は提供されていませんが、各ファイルの役割から以下の主要な関数とその機能が推測されます。

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main(username: str, output_file: str, limit: Optional[int] = None)`**: プログラムのエントリポイント。GitHubユーザー名、出力ファイル名、処理リポジトリ数上限を引数に取り、GitHub APIからリポジトリ情報を取得し、整形して指定されたファイルにMarkdown形式で出力します。
- **`src/generate_repo_list/badge_generator.py`**
    - **`generate_badge_markdown(repo_data: Dict) -> str`**: リポジトリデータを受け取り、使用言語やライセンスなどの情報に基づいてMarkdown形式のバッジ文字列を生成します。
- **`src/generate_repo_list/config_manager.py`**
    - **`load_config(config_path: str) -> Dict`**: 指定されたパスからYAML設定ファイルを読み込み、辞書形式で返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_repository_markdown(repo_list: List[Dict], seo_data: Dict) -> str`**: 処理されたリポジトリ情報のリストとSEOメタデータを受け取り、完全なリポジトリ一覧のMarkdownコンテンツを生成します。
    - **`generate_single_repo_section(repo_data: Dict) -> str`**: 個々のリポジトリ情報から、そのリポジトリ表示用のMarkdownセクションを生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_url: str, config: Dict) -> Optional[str]`**: 指定されたリポジトリのURLと設定情報に基づき、`generated-docs/project-overview.md`から3行のプロジェクト概要を抽出して返します。APIリクエストのキャッシュやリトライ機能を持つと推測されます。
- **`src/generate_repo_list/repository_processor.py`**
    - **`fetch_repositories(username: str, github_token: str) -> List[Dict]`**: 指定されたGitHubユーザー名とトークンを使用して、GitHub APIからそのユーザーのリポジトリ情報を取得し、リスト形式で返します。
    - **`process_repository_data(raw_repo_data: List[Dict]) -> List[Dict]`**: 取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、フィルタリング、整形して構造化されたデータリストを生成します。
- **`src/generate_repo_list/statistics_calculator.py`**
    - **`calculate_stats(repo_data: Dict) -> Dict`**: リポジトリの生データからスター数、フォーク数、最終更新日などの統計情報を計算し、整形された辞書で返します。
- **`src/generate_repo_list/template_processor.py`**
    - **`render_template(template_content: str, data: Dict) -> str`**: テンプレート文字列とデータ辞書を受け取り、テンプレート内のプレースホルダーをデータで置換して最終的な文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**
    - **`build_github_repo_url(username: str, repo_name: str) -> str`**: GitHubユーザー名とリポジトリ名から、そのリポジトリのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-23 07:06:53 JST
