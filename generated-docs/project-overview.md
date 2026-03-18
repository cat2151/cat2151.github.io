Last updated: 2026-03-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得します。
- GitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- これにより、検索エンジンでの発見性を高め、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: GitHub Pages (JekyllベースでMarkdownコンテンツを公開), Markdown (コンテンツ生成フォーマット)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (Pythonコードのテストフレームワーク), ruff (Pythonコードの高速リンター/フォーマッター), GitHub API (リポジトリ情報取得のためのインターフェース)
- テスト: pytest (テスト実行、設定管理)
- ビルドツール: Python (リポジトリ情報の取得とMarkdown生成スクリプトの実行環境)
- 言語機能: Python (メインの開発言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリの存在から、自動化ワークフローで使用される可能性が高い)
- 開発標準: ruff (コードスタイルと品質の統一), .editorconfig (複数のエディタ間での設定統一)

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリ。
    -   **`check_large_files/README.md`**: `check_large_files`ディレクトリの目的と使い方を説明するMarkdownファイル。
    -   **`check-large-files.toml`**: 大容量ファイルチェックに関する設定（例: チェック対象のファイルサイズ閾値など）を定義するTOML形式のファイル。
    -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイル。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、使い方、設定方法などを説明するメインのドキュメントファイル。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。GitHub Pagesサイトの動作を制御する。
-   **`assets/`**: ウェブサイトで使用されるファビコン画像などのアセットを格納するディレクトリ。
-   **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグやテストに特化したスクリプト。
-   **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（例: プロジェクト概要）が格納される可能性があるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイル。
-   **`index.md`**: メインのリポジトリ一覧ページとして生成されるMarkdownファイル。GitHub Pagesのトップページとして表示される。
-   **`issue-notes/22.md`**: 特定のイシュー（ID 22）に関するメモや議論を記録したファイル。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを提供するJSONファイル。ホーム画面への追加、オフライン機能などを可能にする。
-   **`pytest.ini`**: pytestのテスト実行に関する設定（テストの検出方法、プラグイン、マーカーなど）を定義するファイル。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイル。
-   **`requirements.txt`**: 本番環境でこのスクリプトを実行する際に必要となるPythonパッケージとそのバージョンを列挙したファイル。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
-   **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。コードスタイルや静的解析のルールを定義する。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空ファイル。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成ロジック全体を含むPythonパッケージ。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空ファイル。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）の情報を生成するモジュール。
        -   **`config.yml`**: プロジェクト概要取得機能などの技術的なパラメータや設定を定義するYAMLファイル。
        -   **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）を読み込み、管理するためのモジュール。
        -   **`date_formatter.py`**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するユーティリティモジュール。
        -   **`generate_repo_list.py`**: プロジェクトのメインエントリスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体を orchestrate する。
        -   **`json_ld_template.json`**: SEO目的で構造化データ（JSON-LD形式）を生成するためのテンプレートファイル。
        -   **`language_info.py`**: リポジトリで使用されているプログラミング言語の情報を処理・整形するモジュール。
        -   **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するモジュール。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出するモジュール。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するモジュール。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報に整形・加工するモジュール。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータや記述のテンプレートを定義するYAMLファイル。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するモジュール。
        -   **`strings.yml`**: アプリケーション内で表示される様々なメッセージや文言を国際化・一元管理するためのYAMLファイル。
        -   **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2など）のレンダリングを管理するモジュール。
        -   **`url_utils.py`**: URLの操作や検証、生成などを行うためのユーティリティ関数を集めたモジュール。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを確認するためのテストスクリプト。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトの単体テスト。
    -   **`test_config.py`**: `config_manager`モジュールや設定ファイルの読み込みに関するテスト。
    -   **`test_date_formatter.py`**: `date_formatter`モジュールの機能が正しく動作するかを確認するためのテスト。
    -   **`test_environment.py`**: 開発・実行環境のセットアップが適切であるかを確認するテスト。
    -   **`test_integration.py`**: プロジェクト全体の主要なコンポーネントが連携して正しく機能するかを確認する統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator`モジュールの機能テスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの単体テスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールの機能テスト。
    -   **`test_repository_processor.py`**: `repository_processor`モジュールの機能テスト。

## 関数詳細説明
（具体的な関数シグネチャが提供されていないため、主要なファイルにおける想定される主要関数の役割を記述します。）

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main(username: str, output_file: str, limit: Optional[int] = None)`: プログラムのエントリポイント。指定されたGitHubユーザーのリポジトリ情報を取得し、整形してMarkdownファイルとして出力します。
        -   **引数**: `username` (対象GitHubユーザー名), `output_file` (出力ファイルパス), `limit` (処理するリポジトリ数の上限、オプション)
        -   **戻り値**: なし
        -   **機能**: 設定の読み込み、GitHub APIからのリポジトリ取得、各リポジトリの処理、Markdown生成、ファイル書き込みを統括します。

-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_and_process_repositories(username: str, github_token: str, limit: Optional[int] = None)`: GitHub APIを介して指定ユーザーのリポジトリを取得し、必要な情報に加工します。
        -   **引数**: `username` (GitHubユーザー名), `github_token` (認証用GitHubトークン), `limit` (取得するリポジトリ数の上限、オプション)
        -   **戻り値**: 処理されたリポジトリ情報のリスト（辞書形式）
        -   **機能**: GitHub APIへのリクエスト送信、レスポンスのパース、各リポジトリデータの整形・フィルタリングを行います。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_data: dict, config: dict)`: 指定されたリポジトリの特定のパスからプロジェクト概要のテキストを非同期的に取得します。
        -   **引数**: `repo_data` (単一のリポジトリ情報), `config` (プロジェクト概要取得機能の設定)
        -   **戻り値**: 抽出された3行のプロジェクト概要（文字列）、またはNone
        -   **機能**: リポジトリのURLから指定ファイルの内容を読み込み、設定されたセクションタイトルに基づいて概要を抽出します。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown_content(processed_repos: list, template_config: dict, strings: dict)`: 処理済みのリポジトリ情報とテンプレート設定、文言データを使用して最終的なMarkdownコンテンツを生成します。
        -   **引数**: `processed_repos` (処理されたリポジトリ情報のリスト), `template_config` (Markdownテンプレートの設定), `strings` (表示文言データ)
        -   **戻り値**: 生成されたMarkdownコンテンツ（文字列）
        -   **機能**: 各リポジトリ情報を整形し、JekyllのフォーマットやSEOメタデータを含んだMarkdownテキストを構築します。

-   **`src/generate_repo_list/badge_generator.py`**
    -   `create_badges(repo: dict)`: リポジトリ情報に基づき、対応するバッジ（アクティブ、アーカイブ、フォークなど）のMarkdownスニペットを生成します。
        -   **引数**: `repo` (単一のリポジトリ情報)
        -   **戻り値**: バッジのMarkdown文字列のリスト
        -   **機能**: リポジトリのプロパティ（アーカイブ済みか、フォークか、言語など）を判定し、それに応じた視覚的なバッジを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-03-19 07:11:44 JST
