Last updated: 2025-12-21

# Project Overview

## プロジェクト概要
- GitHub Pages サイト向けに、リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを生成します。
- これにより、プロジェクトの公開情報が検索エンジンやLLMに認識されやすくなることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (テストフレームワーク), ruff (コードリンター/フォーマッター)
- テスト: pytest (Pythonコードの単体・統合テスト実行)
- ビルドツール: なし (Pythonスクリプトがコンテンツを直接生成)
- 言語機能: Python (スクリプトの主要開発言語)
- 自動化・CI/CD: GitHub Actions (生成されたMarkdownのデプロイや他のリポジトリのワークフロー管理に言及)
- 開発標準: ruff (Pythonコードの品質と統一性を保つためのルール)

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
googled947dc864c270e07.html
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
- **`.gitignore`**: Gitがバージョン管理の対象から外すファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述するファイル。
- **`README.md`**: プロジェクトの概要、セットアップ方法、機能、使い方などが記述されたメインドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動を制御する設定ファイル。
- **`assets/`**: サイトで使用される画像（ファビコンなど）やその他の静的アセットを格納するディレクトリ。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグ目的で使用されるスクリプト。
- **`generated-docs/`**: 他のリポジトリから自動取得・生成されたドキュメント（例: 各リポジトリの`project-overview.md`）が一時的に格納される可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認に使用される認証ファイル。
- **`index.md`**: メインスクリプトによって自動生成されたリポジトリ一覧のMarkdownコンテンツが出力されるファイル。GitHub Pagesのトップページとして機能する。
- **`issue-notes/`**: 開発中に発生した課題や検討事項を記録するためのMarkdownファイル群。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイル。サイトのホーム画面追加やオフライン機能に関する情報を提供する。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。
- **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonライブラリとそのバージョンをリストアップするファイル。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要なPythonライブラリとそのバージョンをリストアップするファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行うツール`ruff`の設定ファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）に応じたバッジを生成するロジックを管理。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、本プロジェクトの技術的な動作パラメータを定義する設定ファイル。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`strings.yml`といった設定ファイルを読み込み、管理する機能を提供。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプト。
- **`src/generate_repo_list/json_ld_template.json`**: SEOのために、検索結果にリッチスニペット表示を促すJSON-LD形式の構造化データテンプレート。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形する機能。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジック。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（`generated-docs/project-overview.md`など）からプロジェクト概要を抽出し、取得する機能。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報に加工する機能。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや、コンテンツ生成に使用されるSEO最適化テンプレートの設定。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するファイル。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成のための各種テンプレートを処理し、データと結合する機能。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview_fetcher.py`の単体テストを記述したファイル。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
- **`tests/test_config.py`**: 設定ファイルの読み込みやアクセスに関するテスト。
- **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテスト。
- **`tests/test_integration.py`**: 複数のコンポーネントが連携して動作するかを確認する統合テスト。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py`が正しくMarkdownを生成するかどうかのテスト。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py`の動作（概要の取得・解析）に関するテスト。
- **`tests/test_repository_processor.py`**: `repository_processor.py`がリポジトリデータを正しく処理するかどうかのテスト。

## 関数詳細説明
※プロジェクト情報に具体的な関数リストの提供がないため、各ファイルの役割から主要な公開関数や内部ヘルパー関数を推測して記述します。

- **`generate_repo_list.py`**
    - `main()`: プログラムのエントリポイント。リポジトリ情報の取得、処理、Markdown生成の全体フローをオーケストレートします。引数としてGitHubユーザー名や出力ファイルパスを受け取ります。
    - `parse_arguments()`: コマンドライン引数を解析し、必要なオプション（`--username`, `--output`, `--limit`など）を処理します。
- **`config_manager.py`**
    - `load_config(config_path: str) -> dict`: 指定されたパスからYAML設定ファイルを読み込み、辞書形式で返します。
    - `get_setting(key_path: str, default_value: Any = None) -> Any`: ドット区切りパスで指定された設定値を取得します。設定が存在しない場合はデフォルト値を返します。
- **`repository_processor.py`**
    - `fetch_repositories(username: str, github_token: str, limit: int = None) -> list[dict]`: GitHub APIを使用して指定されたユーザーのリポジトリ一覧を取得します。認証にはGitHubトークンを使用し、取得数を制限することも可能です。
    - `process_repository_data(repo_data: dict) -> dict`: 生のGitHubリポジトリデータ（辞書）を受け取り、必要な情報のみを抽出し、整形された形式で返します。
- **`project_overview_fetcher.py`**
    - `fetch_project_overview(repo_url: str, config: dict) -> str`: 指定されたリポジトリURLから、設定（`config.yml`）に基づき`generated-docs/project-overview.md`などのファイルを探し、その内容からプロジェクト概要の3行説明を抽出して返します。APIリクエストやファイル読み込みを行います。
    - `parse_overview_markdown(markdown_content: str, section_title: str) -> str`: Markdownコンテンツと抽出対象のセクションタイトルを受け取り、指定されたセクションからプロジェクト概要の3行を解析して返します。
- **`markdown_generator.py`**
    - `generate_markdown(repositories: list[dict], template: str, strings: dict) -> str`: 処理済みのリポジトリ情報リストと、Markdown生成用のテンプレート、表示文言を受け取り、最終的なMarkdown形式の文字列を生成します。
- **`badge_generator.py`**
    - `generate_badge(repo_status: str) -> str`: リポジトリのステータス（例: "active", "archived", "fork"）に応じて、対応するバッジのMarkdownまたはHTMLスニペットを生成します。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── parse_arguments() (generate_repo_list.py)
├── config_manager.load_config()
├── repository_processor.fetch_repositories()
│   └── (GitHub API呼び出し)
├── (各リポジトリに対するループ)
│   ├── repository_processor.process_repository_data()
│   ├── project_overview_fetcher.fetch_project_overview()
│   │   └── project_overview_fetcher.parse_overview_markdown()
│   ├── badge_generator.generate_badge()
│   └── statistics_calculator.(計算関数)
└── markdown_generator.generate_markdown()
    └── template_processor.(テンプレート処理関数)

---
Generated at: 2025-12-21 07:05:39 JST
