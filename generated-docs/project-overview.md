Last updated: 2026-01-04

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- これにより、リポジトリの可視性を高め、検索エンジンやAIからの参照を向上させます。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (静的サイトジェネレーター), Markdown (コンテンツフォーマット)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (スクリプト言語), GitHub API (リポジトリ情報取得)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py`が実質的なビルドツール)
- 言語機能: Python (プログラムの記述に使用される主要言語)
- 自動化・CI/CD: GitHub Actions (システムの実行環境としての可能性、README中でプロジェクト概要取得機能での活用が示唆されているが、このプロジェクト自体のCI/CDは明示されていないため、ここでは来訪者向けに「自動化の基盤として利用可能」程度に留める)
- 開発標準: ruff (Pythonの高速なLinterおよびフォーマッター)

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
  16.md
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
    date_formatter.py
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
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者が、統一されたコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイル。一時ファイルや生成物などを追跡しないようにします。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイル。利用条件を明示します。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法などが詳細に記述された、プロジェクトの玄関口となるドキュメント。
- **`_config.yml`**: Jekyllサイト全体のグローバルな設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **`assets/`**: ウェブサイトで使用される静的なリソース（画像、アイコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるウェブサイトのアイコンファイル。異なるサイズで用意されています。
- **`debug_project_overview.py`**: `project_overview_fetcher`モジュールの動作をデバッグするための補助スクリプト。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたプロジェクト概要などのドキュメントが格納されることを想定したディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるファイル。
- **`index.md`**: GitHub Pagesサイトのメインページとして表示されるMarkdownファイル。このプロジェクトでは、自動生成されたリポジトリ一覧が含まれます。
- **`issue-notes/`**: 開発中に検討された課題や決定事項、メモなどを記述したMarkdownファイル群。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。ウェブアプリの表示情報（名前、アイコン、起動方法など）を定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。テストの実行オプションなどが記述されます。
- **`requirements-dev.txt`**: 開発・テスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイル。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンを列挙したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいはクロールしないべきかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットを行うツール`ruff`の設定ファイル。コード品質とスタイルを維持します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`__init__.py`**: Pythonパッケージであることを示すファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを格納するパッケージ。
        - **`__init__.py`**: `generate_repo_list`パッケージであることを示すファイル。
        - **`badge_generator.py`**: リポジトリの言語やステータスを示すバッジ（アイコン）を生成するロジックを実装。
        - **`config.yml`**: プロジェクト概要取得機能など、システムの動作パラメータを定義する設定ファイル。
        - **`config_manager.py`**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのモジュール。
        - **`date_formatter.py`**: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数を提供。
        - **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する全体の流れを制御。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ（JSON-LD形式）のテンプレートを定義。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するモジュール。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートを組み合わせて、最終的なMarkdownコンテンツを生成するロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクトの3行概要を抽出する機能。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、システムで使いやすい形式に整形・フィルタリングするロジック。
        - **`seo_template.yml`**: 検索エンジン最適化 (SEO) 関連のメタデータやテンプレート設定を定義するファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能。
        - **`strings.yml`**: プロジェクトで使用される表示メッセージ、ラベル、文言などを一元的に管理するためのファイル。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイル（例：JekyllのLiquidテンプレート）を処理し、データと結合する機能。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールのテストコード。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`test_config.py`**: 設定関連機能のテストコード。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストコード。
    - **`test_environment.py`**: 実行環境に関する設定や依存関係のテストコード。
    - **`test_integration.py`**: 複数のモジュールが連携する統合的な動作を検証するテストコード。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストコード。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコード。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストコード。

## 関数詳細説明
- **`generate_repo_list.py`内の主要関数**:
    - **`main`関数**: プログラムのエントリーポイント。コマンドライン引数を解析し、設定の読み込み、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成という一連の処理を調整します。
- **`repository_processor.py`内の主要関数**:
    - リポジトリの生データを受け取り、必要な情報（リポジトリ名、説明、URL、スター数、最終更新日など）を抽出・整形する関数群。アクティブ、アーカイブ、フォークなどのリポジトリ状態に基づいて分類する機能も持ちます。
- **`project_overview_fetcher.py`内の主要関数**:
    - 特定のリポジトリ内の指定されたファイル（`generated-docs/project-overview.md`）から、特定のセクション（「プロジェクト概要」）に記述された3行の要約を非同期で取得する関数群。キャッシュやリトライ機能も提供します。
- **`markdown_generator.py`内の主要関数**:
    - 処理済みのリポジトリ情報とプロジェクト概要を受け取り、Jekyllの要件に合わせたMarkdown形式の文字列を生成する関数群。SEOメタデータやリポジトリの表示レイアウトを含みます。
- **`badge_generator.py`内の主要関数**:
    - リポジトリのプログラミング言語、アーカイブ状態、フォーク状態などに応じて、表示用のバッジ（例：アイコンやテキストラベル）を生成する関数群。
- **`date_formatter.py`内の主要関数**:
    - 日付オブジェクトや日付文字列を、ウェブサイト表示に適した形式（例：「YYYY年MM月DD日」）に変換する関数群。
- **`config_manager.py`内の主要関数**:
    - YAML形式の設定ファイルを安全に読み込み、設定値をプログラム全体で利用できるように管理する関数群。設定値の検証やデフォルト値の提供も行います。
- **`template_processor.py`内の主要関数**:
    - Markdown生成時に使用されるテンプレート（例：Liquidテンプレート）を読み込み、動的なデータ（リポジトリ情報など）を埋め込んで最終的なコンテンツを生成する関数群。
- **`url_utils.py`内の主要関数**:
    - GitHubリポジトリのURL構築、ファイルのURL解決など、URLに関連するさまざまなユーティリティ操作を提供する関数群。
- **`language_info.py`内の主要関数**:
    - リポジトリの主要言語を識別し、その言語に関連する情報（例：言語名、色）を提供したり、表示形式を整形したりする関数群。
- **`statistics_calculator.py`内の主要関数**:
    - リポジトリのスター数、フォーク数、ウォッチ数などの数値データを集計し、必要に応じて整形する関数群。

## 関数呼び出し階層ツリー
```
main (generate_repo_list.py)
├─── config_manager.load_config (設定ファイル読み込み)
├─── repository_processor.fetch_and_process_repositories (リポジトリ情報取得・処理)
│    ├─── GitHub API呼び出し (外部サービス)
│    └─── project_overview_fetcher.get_project_overview (各リポジトリ概要取得)
│         └─── url_utils.build_repo_content_url (コンテンツURL構築)
│         └─── HTTPリクエスト (外部リポジトリのoverview.md取得)
├─── markdown_generator.generate_markdown (Markdown生成)
│    ├─── template_processor.render_template (テンプレートレンダリング)
│    ├─── badge_generator.generate_badge_markdown (バッジ生成)
│    ├─── date_formatter.format_date (日付整形)
│    ├─── language_info.get_language_display (言語情報表示整形)
│    └─── statistics_calculator.calculate_statistics (統計情報計算)
└─── ファイル出力

---
Generated at: 2026-01-04 07:06:09 JST
