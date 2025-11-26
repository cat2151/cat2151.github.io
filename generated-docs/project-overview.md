Last updated: 2025-11-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdownで自動生成します。
- これにより、GitHub Pagesの検索エンジンクロールを促進し、LLMからのリポジトリ参照性向上も期待されます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式), HTML/CSS (Jekyllによりレンダリングされる最終形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Python (スクリプト実行によるMarkdown生成)
- 言語機能: Python (スクリプト開発), YAML (設定ファイル管理), TOML (設定ファイル管理)
- 自動化・CI/CD: GitHub Pages (自動デプロイ機能を持つが、プロジェクト自体はCI/CDパイプラインを直接含まず、ローカル実行を重視)
- 開発標準: ruff (Pythonコードのリンターおよびフォーマッター), EditorConfig (エディタ設定の統一)
- API連携: GitHub API (リポジトリ情報の取得)

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
index.md
issue-notes/
  10.md
  12.md
  14.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法などが記述された主要なドキュメント。
- **`_config.yml`**: Jekyllサイトの全体設定を定義するファイル。テーマ、プラグイン、パーマリンク構造などを設定。
- **`assets/`**: Jekyllサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: サイトのファビコン画像ファイル群。
- **`debug_project_overview.py`**: `project_overview_fetcher.py`モジュールのデバッグや単体テストを行うためのスクリプト。
- **`generated-docs/`**: プロジェクトによって自動生成されるドキュメントやレポートを格納するためのディレクトリ（現状は空）。
- **`index.md`**: スクリプトによって生成されたリポジトリ一覧のMarkdownコンテンツが出力されるファイル。これがGitHub Pagesのトップページとして表示されることを想定。
- **`issue-notes/`**: 開発中の課題や検討事項、特定のIssueに関連するメモなどを個別のMarkdownファイルとして管理するディレクトリ。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータ定義ファイル。アプリの名称、アイコン、表示設定などを記述。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。テストの実行オプションやパスなどを定義。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonライブラリの依存関係を記述したファイル。
- **`requirements.txt`**: プロジェクトの実行環境で必要となるPythonライブラリの依存関係を記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか、しないかを指示するファイル。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッター`ruff`の設定ファイル。コードスタイルルールや無視するファイルなどを定義。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイル。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスに応じたバッジ（例: Python, Starなど）のMarkdownコードを生成するロジックを実装。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、スクリプトの動作を制御する技術的なパラメータを定義する設定ファイル。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのモジュール。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプト。GitHub APIからのリポジトリ情報取得、処理、Markdown生成の一連のフローを制御する。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレート。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換する。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報とSEOデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成する。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）からプロジェクトの概要説明を抽出する機能を提供する。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、フィルタリング、必要な情報の抽出を行うモジュール。
- **`src/generate_repo_list/seo_template.yml`**: サイト全体のSEOメタデータや、リポジトリごとのSEO情報を設定するためのテンプレートファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: 各リポジトリのスター数やフォーク数といった統計情報を計算・集計する機能を提供する。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元管理する設定ファイル。多言語対応や文言変更を容易にする。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時などに使用されるテンプレートの読み込み、変数置換などの処理を行う汎用モジュール。
- **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URLに関連するユーティリティ関数を集めたモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールに対する単体テストを含むファイル。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`test_config.py`**: `config_manager.py`や設定ファイルの読み込みに関するテスト。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテスト。
    - **`test_integration.py`**: 複数のモジュールやシステムを連携させた統合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator.py`が正しくMarkdownを生成するかどうかを検証するテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`が期待通りにプロジェクト概要を抽出するかを検証するテスト。
    - **`test_repository_processor.py`**: `repository_processor.py`がリポジトリデータを正しく処理するかを検証するテスト。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: スクリプトのエントリポイント。コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ取得、リポジトリデータの処理、Markdown生成、最終的なファイル出力までの一連の流れを統括します。
    - `parse_arguments()`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、処理リミットなどの設定値を取得します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(file_path: str) -> dict`: 指定されたYAMLファイルから設定を読み込み、辞書形式で返します。
    - `get_setting(key: str, default=None)`: 読み込まれた設定から特定のキーの値を取得します。キーが存在しない場合はデフォルト値を返します。
- **`src/generate_repo_list/repository_processor.py`**:
    - `fetch_repositories(username: str, token: str, limit: int = None) -> list`: GitHub APIを使用して指定されたユーザーのリポジトリ一覧を取得します。必要に応じてリポジトリ数を制限できます。
    - `process_repository_data(repo_data: dict) -> dict`: GitHub APIから取得した個々のリポジトリデータ（辞書形式）を整形し、必要な情報のみを抽出し、表示に適した形式に変換します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_name: str, username: str, target_file: str, section_title: str) -> str`: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、指定されたセクションタイトル（例: "プロジェクト概要"）配下の3行説明を抽出し、文字列として返します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_markdown(repo_list: list, seo_data: dict, strings: dict) -> str`: 処理済みのリポジトリ情報のリスト、SEOデータ、および表示文字列を使用して、最終的なリポジトリ一覧のMarkdownコンテンツ全体を生成します。
    - `generate_repo_section(repo_info: dict, strings: dict) -> str`: 個々のリポジトリ情報に基づいて、そのリポジトリ表示用のMarkdownセクションを生成します。
- **`src/generate_repo_list/badge_generator.py`**:
    - `create_badges(repo_info: dict) -> str`: リポジトリ情報（言語、スター数、アーカイブ状態など）に基づいて、対応するバッジのMarkdown文字列（例: Shields.io形式）を生成して返します。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - `calculate_repo_stats(repo_info: dict) -> dict`: 特定のリポジトリ（`repo_info`）から、スター数、フォーク数などの統計情報を計算し、整形された辞書として返します。
- **`src/generate_repo_list/template_processor.py`**:
    - `apply_template(template_content: str, data: dict) -> str`: テンプレート文字列内のプレースホルダーを、提供されたデータ辞書の値で置換し、処理済みの文字列を返します。
- **`src/generate_repo_list/url_utils.py`**:
    - `build_repo_url(username: str, repo_name: str) -> str`: 指定されたユーザー名とリポジトリ名から、GitHubリポジトリの完全なURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-27 07:06:07 JST
