Last updated: 2026-06-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのGitHub Pages用Markdownを自動生成します。
- GitHub PagesサイトにSEO最適化されたリポジトリ一覧を作成し、検索エンジンでの発見性を向上させます。
- LLMによるリポジトリ参照の失敗を緩和し、開発効率の向上に貢献するシステムです。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (コンテンツ生成形式), HTML (生成されるページの表示形式)
- 音楽・オーディオ: (該当なし)
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), Ruff (コードフォーマッタ), Pytest (テストフレームワーク), YAML (設定ファイル形式), TOML (設定ファイル形式)
- テスト: Pytest (Python用テストフレームワーク)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py`が中心となり、Markdownファイルを生成)
- 言語機能: Python 3.x (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリの存在から、自動化にGitHub Actionsを利用していると推測されます)
- 開発標準: Ruff (Pythonコードのスタイルチェックとフォーマット), .editorconfig (エディタ間の設定統一)

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
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
  22.md
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
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなど、リポジトリ自動化に関連するスクリプトや設定を格納するディレクトリ。
    - **check_large_files/README.md**: 大容量ファイルチェック機能に関する説明。
    - **check-large-files.toml**: 大容量ファイルチェックのルールや設定を定義するTOMLファイル。
    - **scripts/check_large_files.py**: GitHub Actionsの一部として、リポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）。
- **README.md**: プロジェクトの目的、機能、使い方、開発者向けのヒントなどを記述したメインのドキュメントファイル。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどを定義します。
- **assets/**: Webサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのファビコン（アイコン）の様々なサイズ。
- **debug_project_overview.py**: `project-overview.md`からの概要取得機能をデバッグするためのスクリプト。
- **generated-docs/**: 各リポジトリの`project-overview.md`が存在しうるディレクトリ、または同様の自動生成ドキュメントが配置される可能性のある場所。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイル。
- **index.md**: `generate_repo_list.py`によって自動生成される、GitHub PagesサイトのトップページとなるMarkdownファイル。リポジトリ一覧が含まれます。
- **issue-notes/**: 開発中の課題やノートを管理するディレクトリ。
    - **22.md**: 特定の課題（Issue #22）に関する詳細なメモや情報。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供するWeb App Manifestファイル。ホーム画面に追加されるアプリのメタデータを定義します。
- **pytest.ini**: pytestフレームワークの設定ファイル。テストの実行方法やオプションを定義します。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonパッケージの依存関係を記述したファイル。
- **requirements.txt**: 本番環境での実行に必要なPythonパッケージの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイル。
- **ruff.toml**: Pythonコードのリンティング（構文やスタイルチェック）とフォーマットを行うRuffツールの設定ファイル。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成機能の中核をなすPythonモジュール群。
        - **__init__.py**: Pythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのバッジ（例: ビルドステータス、ライセンス）を生成または処理する機能を持つ。
        - **config.yml**: プロジェクト概要取得機能などの技術的パラメータを設定するYAMLファイル。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するクラスや関数を提供する。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供する。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdown形式で出力する。
        - **json_ld_template.json**: SEO最適化のため、JSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理、分析する。
        - **markdown_generator.py**: 処理されたリポジトリ情報と概要をもとに、Jekyll互換のMarkdownコンテンツを生成する。
        - **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を自動取得する機能を持つ。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルからバッジ（例: CI/CDステータス）を抽出する機能。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示用に必要な情報を抽出、整形するロジックをカプセル化する。
        - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータや設定を定義するYAMLテンプレート。
        - **statistics_calculator.py**: リポジトリに関する様々な統計情報（スター数、フォーク数など）を計算する。
        - **strings.yml**: UI表示や生成されるMarkdown内で使用される各種メッセージ、文言、ラベルなどを管理するYAMLファイル。
        - **template_processor.py**: MarkdownやHTMLテンプレートの処理、変数置換などを行う汎用的な機能。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供する。
- **test_project_overview.py**: `project-overview.md`からの概要取得機能に関する単体テストファイル。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのテストフィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
    - **test_config.py**: 設定ファイルの読み込みと処理に関するテスト。
    - **test_date_formatter.py**: 日付フォーマット機能のテスト。
    - **test_environment.py**: テスト実行環境のセットアップや依存関係に関するテスト。
    - **test_integration.py**: プロジェクト全体の主要なフローに関する統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細を網羅的に特定することは困難です。しかし、プロジェクトの主要なファイルからその役割に基づき、想定される主要な関数を以下に説明します。

- **`src/generate_repo_list/generate_repo_list.py` 内の `main()` 関数**:
    - **役割**: プログラムのエントリポイント。コマンドライン引数の解析、GitHubトークンの読み込み、設定の初期化を行います。リポジトリ情報の取得から処理、最終的なMarkdownファイルへの出力をオーケストレーションします。
    - **引数**: （通常、`sys.argv`を介してコマンドライン引数を受け取るか、特定のオプションオブジェクトを受け取る）
    - **戻り値**: （通常、`None`または成功/失敗を示す整数ステータスコード）
    - **機能**: GitHub APIからのリポジトリ取得、`repository_processor`を通じたデータ整形、`project_overview_fetcher`による概要取得、`markdown_generator`によるMarkdown生成、そして結果のファイルへの書き出しを制御します。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の `fetch_project_overview(repo_data, config)` 関数**:
    - **役割**: 指定されたリポジトリの`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を非同期で取得します。キャッシュ機能やリトライ機構も利用する可能性があります。
    - **引数**:
        - `repo_data`: 処理対象のリポジトリに関する情報（例: リポジトリ名、オーナー名などを含む辞書）。
        - `config`: プロジェクト概要取得機能に関する設定パラメータ（例: ターゲットファイル名、セクションタイトル、タイムアウトなど）。
    - **戻り値**: 取得したプロジェクト概要の3行説明のリスト、または取得できなかった場合は空のリストやデフォルト値。
    - **機能**: GitHub APIを介してリポジトリのコンテンツを取得し、指定されたセクションからテキストをパースして抽出します。

- **`src/generate_repo_list/markdown_generator.py` 内の `generate_markdown(repo_list, seo_config, strings_config)` 関数**:
    - **役割**: 処理され整形されたリポジトリデータのリストと、SEOおよび表示メッセージの設定に基づいて、Jekyll互換のMarkdown文字列全体を生成します。
    - **引数**:
        - `repo_list`: 整形済みで表示準備ができたリポジトリ情報のリスト。
        - `seo_config`: SEOテンプレートやメタデータに関する設定。
        - `strings_config`: 表示メッセージや文言を定義する設定。
    - **戻り値**: 生成されたMarkdownコンテンツを含む文字列。
    - **機能**: 提供されたリポジトリ情報と設定をテンプレートに適用し、バッジ、概要、分類、SEOメタデータなどを含む完全なMarkdownドキュメントを構築します。

- **`src/generate_repo_list/repository_processor.py` 内の `process_repositories(api_client, username, limit)` 関数**:
    - **役割**: GitHub APIクライアントを使用して指定されたユーザーのリポジトリ情報を取得し、必要なデータだけを抽出し、表示に適した形式に整形します。フォーク、アーカイブの状態も考慮します。
    - **引数**:
        - `api_client`: GitHub APIと通信するためのクライアントインスタンス。
        - `username`: GitHubユーザー名。
        - `limit`: 処理するリポジトリ数の上限（開発用）。
    - **戻り値**: 整形され、表示可能な状態のリポジトリ情報のリスト。
    - **機能**: GitHub APIから取得した生のJSONデータから、リポジトリ名、説明、スター数、最終更新日などのキー情報を抽出し、カテゴリ（アクティブ、アーカイブ、フォーク）に基づいて分類します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-06-18 07:37:25 JST
