Last updated: 2026-08-03

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧を自動生成するシステム。
- GitHub APIからリポジトリ情報を取得し、SEO最適化されたMarkdown形式で出力。
- 検索エンジンによるクロール向上と、LLMによるリポジトリ参照効率化を目的。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesのベースフレームワーク), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), `ruff` (Pythonコードの静的解析・フォーマットツール)
- テスト: `pytest` (Python向けテストフレームワーク)
- ビルドツール: Pythonスクリプト (Markdownコンテンツ生成), Jekyll (GitHub Pagesのサイトビルド)
- 言語機能: Python (汎用プログラミング言語)
- 自動化・CI/CD: Pythonスクリプトによるリポジトリ情報取得・Markdown生成の自動化。
- 開発標準: `ruff` (コードスタイル統一), `.editorconfig` (エディタ設定統一)

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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   `.github_automation/check_large_files/`: 大容量ファイルチェック機能に関連するディレクトリ。
    -   `README.md`: 大容量ファイルチェック機能に関する説明文書。
    -   `check-large-files.toml`: 大容量ファイルチェックのルールや閾値を定義する設定ファイル。
    -   `scripts/check_large_files.py`: 指定された設定に基づき、リポジトリ内の大容量ファイルを検出するPythonスクリプト。
-   `.gitignore`: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。
-   `LICENSE`: このプロジェクトのソフトウェアライセンス（MITライセンス）に関する情報。
-   `README.md`: プロジェクトの目的、主な機能、使い方、設定方法などを説明するメインのドキュメント。
-   `_config.yml`: Jekyllサイト全体の挙動を制御する設定ファイル。
-   `assets/`: ウェブサイトで使用される静的アセット（画像ファイルなど）を格納するディレクトリ。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザタブなどに表示される小さなアイコン）の各種サイズ。
-   `debug_project_overview.py`: `project_overview` 機能の動作確認やデバッグを目的とした補助スクリプト。
-   `generated-docs/`: 他のリポジトリからプロジェクト概要が自動取得される際の参照元となるファイルを格納する想定のディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧を含むメインのMarkdownファイル。GitHub Pagesのトップページとして機能する。
-   `issue-notes/22.md`: 特定の課題（Issue #22など）に関するメモや詳細を記録するためのファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイル。アプリの表示方法や振る舞いを定義する。
-   `pytest.ini`: `pytest` テストフレームワークの動作設定ファイル。
-   `requirements-dev.txt`: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `requirements.txt`: プロジェクトの本番環境での実行に必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
-   `ruff.toml`: `ruff` リンターおよびフォーマッターのルール、設定を定義するファイル。
-   `src/`: プロジェクトのソースコードを格納するメインディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示す空ファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成ロジックを含むPythonパッケージ。
        -   `__init__.py`: Pythonパッケージであることを示す空ファイル。
        -   `badge_generator.py`: リポジトリの言語やスター数などのバッジを生成するためのロジックを実装したファイル。
        -   `config.yml`: リポジトリ一覧生成スクリプト（例：APIタイムアウト、キャッシュ設定など）固有の設定を定義するYAMLファイル。
        -   `config_manager.py`: `config.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        -   `date_formatter.py`: 日付や時刻を特定の形式で整形するためのユーティリティ関数を提供するファイル。
        -   `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力するメインの実行スクリプト。
        -   `json_ld_template.json`: SEO強化のため、検索エンジンに構造化データを提供するJSON-LDのテンプレートファイル。
        -   `language_info.py`: リポジトリのプログラミング言語に関する情報を取得・処理するロジックを実装したファイル。
        -   `markdown_generator.py`: 処理されたリポジトリデータから、最終的なMarkdownコンテンツを生成するロジックを実装したファイル。
        -   `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出するロジックを実装したファイル。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータスなど）を抽出するロジックを実装したファイル。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、表示に適した形式に変換するロジックを実装したファイル。
        -   `seo_template.yml`: 検索エンジン最適化（SEO）のためのメタデータやテンプレートを定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（例: スター数、フォーク数など）を計算するロジックを実装したファイル。
        -   `strings.yml`: UI表示や生成されるMarkdown内で使用される各種テキスト（タイトル、ラベル、説明文など）を管理するYAMLファイル。
        -   `template_processor.py`: Markdown生成時に利用するテンプレートのレンダリングを処理するロジックを実装したファイル。
        -   `url_utils.py`: URLの構築や解析など、URLに関連するユーティリティ関数を提供するファイル。
-   `test_project_overview.py`: `project_overview_fetcher` 機能のテストスクリプト。
-   `tests/`: プロジェクト全体のテストスクリプトをまとめたディレクトリ。
    -   `conftest.py`: `pytest` のフィクスチャや共通設定を定義するためのファイル。
    -   `test_badge_generator_integration.py`: `badge_generator.py` の統合テスト。
    -   `test_check_large_files.py`: `.github_automation/check_large_files/` 機能のテスト。
    -   `test_config.py`: 設定ファイルの読み込みや処理に関するテスト。
    -   `test_date_formatter.py`: `date_formatter.py` の日付整形機能のテスト。
    -   `test_environment.py`: 開発・実行環境に関する設定や依存関係のテスト。
    -   `test_integration.py`: プロジェクトの主要なフローや機能の統合テスト。
    -   `test_markdown_generator.py`: `markdown_generator.py` のMarkdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher.py` のプロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor.py` のREADMEバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: `repository_processor.py` のリポジトリデータ処理機能のテスト。

## 関数詳細説明
*   **badge_generator.py**
    *   `generate_badge()`:
        *   役割: リポジトリの特性（言語、スター数など）を示すバッジを生成する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: 特定のリポジトリ情報に基づき、HTMLまたはMarkdown形式のバッジコードを生成します。
*   **config_manager.py**
    *   `load_config()`:
        *   役割: 指定された設定ファイル（例: `config.yml`）を読み込み、Pythonオブジェクトとして提供する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: YAML形式の設定ファイルをパースし、アプリケーションが利用できる設定データを返します。
*   **date_formatter.py**
    *   `format_date()`:
        *   役割: 日付オブジェクトを指定された書式で整形された文字列に変換する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: `datetime` オブジェクトなどを受け取り、読みやすい日付文字列として出力します。
*   **generate_repo_list.py**
    *   `main()`:
        *   役割: プロジェクト全体の実行エントリポイント。GitHub APIからの情報取得、データの処理、Markdown生成、ファイル出力までの一連の流れを orchestrate する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: コマンドライン引数をパースし、設定をロード後、GitHub API経由でリポジトリ情報をフェッチし、最終的なリポジトリ一覧Markdownファイルを生成します。
*   **language_info.py**
    *   `get_language_info()`:
        *   役割: リポジトリの主要なプログラミング言語に関する情報を取得・処理する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: GitHub APIから取得したリポジトリの言語データから、利用頻度の高い言語やその割合などを抽出します。
*   **markdown_generator.py**
    *   `generate_markdown()`:
        *   役割: 処理済みのリポジトリデータから、最終的なリポジトリ一覧のMarkdownコンテンツを生成する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: テンプレートとリポジトリデータを組み合わせ、整形されたMarkdown文字列を生成します。
*   **project_overview_fetcher.py**
    *   `fetch_project_overview()`:
        *   役割: 特定のリポジトリ内にある `generated-docs/project-overview.md` ファイルから、プロジェクト概要の3行説明を抽出する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: GitHubのrawファイルAPIなどを使用してリモートファイルの内容を取得し、指定されたセクションから概要テキストをパースします。
*   **readme_badge_extractor.py**
    *   `extract_badges()`:
        *   役割: リポジトリのREADMEファイルの内容から、特定の形式のバッジ情報（例: CIステータスバッジ）を抽出する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: READMEのMarkdownテキストを解析し、正規表現などを用いてバッジのURLやテキストを特定します。
*   **repository_processor.py**
    *   `process_repository()`:
        *   役割: GitHub APIから取得した個々のリポジトリの生データを、アプリケーションが扱いやすい形式に整形・加工する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: リポジトリの公開日、更新日、説明、言語、スター数などの情報を抽出し、必要な変換を適用します。
*   **statistics_calculator.py**
    *   `calculate_statistics()`:
        *   役割: 複数のリポジトリデータに基づいて、統計情報（例: 総スター数、最も使われている言語の分布など）を計算する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: リポジトリのリストを分析し、全体的な傾向や集計値を算出します。
*   **template_processor.py**
    *   `render_template()`:
        *   役割: 指定されたテンプレートファイルと提供されたデータを用いて、最終的なコンテンツ（Markdownなど）をレンダリングする。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: プレースホルダーを含むテンプレートに動的なデータを埋め込み、出力テキストを生成します。
*   **url_utils.py**
    *   `construct_url()`:
        *   役割: 複数のコンポーネント（ベースURL、パス、クエリパラメータなど）から完全なURLを構築する。
        *   引数: (未検出)
        *   戻り値: (未検出)
        *   機能: URLエンコーディングなどを適切に行い、安全で有効なURL文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-03 07:20:32 JST
