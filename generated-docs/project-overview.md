Last updated: 2026-08-14

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動的に取得するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEOに最適化されたリポジトリ一覧ページを自動生成します。
- これにより、リポジトリの検索エンジンへの可視性を高め、LLMなどからの参照性も向上させることを目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータ), **Markdown** (生成されるコンテンツの形式) - GitHub Pages上で公開される静的サイトの基盤と、そのサイトのコンテンツ形式です。
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要な開発言語) - リポジトリ情報の取得、処理、Markdown生成のためのスクリプトがPythonで記述されています。
- テスト: **pytest** (Pythonテストフレームワーク) - プロジェクトのコードが正しく機能するかを検証するためのテストツールです。
- ビルドツール: **Pythonスクリプト** (リポジトリ一覧生成プロセス) - GitHub APIからデータを取得し、Jekyllサイト用のMarkdownファイルを生成する一連の処理がPythonスクリプトによって行われます。
- 言語機能: **Python** - システムの全てのロジックを実装するためのプログラミング言語です。
- 自動化・CI/CD: **GitHub Actions** (関連自動化スクリプト群), **Pythonスクリプト** (自動生成処理自体) - `_github_automation` ディレクトリには、GitHub Actionsと連携する可能性のある自動化スクリプトが含まれています。このプロジェクト自体が「自動生成」を目的としており、その実行は自動化に適しています。
- 開発標準: **ruff** (Python用Linter/Formatter), **.editorconfig** (コードスタイル統一) - コードの品質を維持し、開発者間での一貫したコーディングスタイルを強制するためのツールと設定ファイルです。

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
-   **`.editorconfig`**: 異なる開発環境（エディタ、IDE）を使用する開発者間で、コードのインデントスタイル、文字エンコーディング、改行コードなどのフォーマットを自動的に統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルを検出・管理するための自動化機能が含まれています。
        -   **`README.md`**: `check_large_files` 機能の目的と使用方法を説明するドキュメントです。
        -   **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。チェック対象のファイルサイズや除外パスなどを定義します。
        -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを特定し、報告するためのPythonスクリプトです。
-   **`.gitignore`**: Gitによるバージョン管理の対象から除外するファイルやディレクトリ（例: ビルド成果物、一時ファイル、設定情報など）を定義するファイルです。
-   **`LICENSE`**: このプロジェクトのソフトウェアライセンス（MITライセンス）に関する情報が記載されています。プロジェクトの利用条件を示します。
-   **`README.md`**: プロジェクトの目的、機能、セットアップ方法、基本的な使用コマンド、ライセンス情報などを説明する、プロジェクトの顔となるドキュメントです。
-   **`_config.yml`**: Jekyll静的サイトジェネレータのグローバルな設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
-   **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）およびプログレッシブウェブアプリ（PWA）用の各種サイズのアイコンファイルです。
-   **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグやテストを目的としたスクリプトです。単体での動作確認に利用されます。
-   **`generated-docs/`**: 他のリポジトリから自動取得されるプロジェクト概要ファイル（`project-overview.md`）など、生成されるドキュメントのテンプレートや格納場所として利用されるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認のために配置されるHTMLファイルです。検索エンジンへの登録やSEO対策に利用されます。
-   **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧がここに書き出されます。
-   **`issue-notes/`**: プロジェクト開発中に発生した課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモや考察を記述したMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルです。ウェブサイトをスマートフォンなどのホーム画面に追加した際の表示名、アイコン、表示モードなどを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法、検出ルール、プラグインの設定などを定義します。
-   **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。本番環境では不要なツールなどが含まれます。
-   **`requirements.txt`**: プロジェクトを本番環境で実行するために最低限必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイルです。SEO対策に利用されます。
-   **`ruff.toml`**: PythonのLinterおよびFormatterであるRuffの設定ファイルです。コードスタイルのルール、エラー検出、自動修正に関する設定を定義します。
-   **`src/`**: プロジェクトの主要なPythonソースコードを格納するルートディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示す空ファイルです。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するメイン機能を提供するパッケージです。
        -   **`__init__.py`**: `generate_repo_list` がPythonパッケージであることを示すファイルです。
        -   **`badge_generator.py`**: リポジトリの言語、ライセンス、ステータスなどを示すバッジのMarkdownコードを生成するスクリプトです。
        -   **`config.yml`**: リポジトリ一覧生成スクリプトの実行時設定（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）を定義するファイルです。
        -   **`config_manager.py`**: `config.yml` や外部のシークレットファイル（例: `secrets.toml`）から設定を読み込み、管理するためのユーティリティスクリプトです。
        -   **`date_formatter.py`**: リポジトリの最終更新日時などの日付情報を、人間が読みやすい形式に整形するための機能を提供します。
        -   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なリポジトリ一覧Markdownを生成する、このプロジェクトのメイン実行スクリプトです。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、リポジトリ情報を構造化データ（JSON-LD形式）として埋め込むためのテンプレートファイルです。
        -   **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に利用するための機能を提供します。
        -   **`markdown_generator.py`**: 処理されたリポジトリデータを受け取り、最終的なMarkdown形式のリポジトリ一覧コンテンツを組み立てる役割を担います。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動的に抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリのREADMEファイル内に既に存在するバッジ情報を抽出し、重複を避けたり情報を利用したりするための機能です。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、整形、フィルタリングを行うことで、Markdown生成に必要な情報に変換する中心的な処理を行います。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやキーワードなどの設定テンプレートです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算し、表示に利用するための機能です。
        -   **`strings.yml`**: アプリケーション内で表示される様々なメッセージや文言（例: ヘッダー、フッター、分類名など）を一元的に管理するためのファイルです。多言語対応などにも利用できます。
        -   **`template_processor.py`**: Markdown生成のための各種テンプレート（例: リポジトリごとの表示形式）を処理し、データと結合して最終的なコンテンツを生成する機能です。
        -   **`url_utils.py`**: URLの生成、検証、解析など、URLに関連する共通のユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能が正しく動作するかを検証するための単体テストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: pytestのテスト実行時に共通で利用されるフィクスチャ（テストのための準備や後処理を行う関数）やフックを定義するファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator` の機能が他のモジュールと連携して正しく動作するかを検証する統合テストです。
    -   **`test_check_large_files.py`**: `check_large_files` スクリプトが意図通りに大容量ファイルを検出するかを検証するテストです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理を行う `config_manager` の機能が正しく動作するかを検証するテストです。
    -   **`test_date_formatter.py`**: 日付整形機能が期待通りに動作するかを検証するテストです。
    -   **`test_environment.py`**: テスト実行環境が適切に設定されているかを検証するテストです。
    -   **`test_integration.py`**: プロジェクトの主要なコンポーネントが連携して動作するエンドツーエンドの統合テストです。
    -   **`test_markdown_generator.py`**: `markdown_generator` が正しくMarkdownコンテンツを生成するかを検証するテストです。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher` がプロジェクト概要を正確に抽出するかを検証するテストです。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor` がREADMEからバッジ情報を正しく抽出するかを検証するテストです。
    -   **`test_repository_processor.py`**: `repository_processor` がGitHub APIから取得したデータを正確に処理・整形するかを検証するテストです。

## 関数詳細説明
提供された情報からは具体的な関数の詳細を特定できませんでしたが、各ファイルが担当する主要な処理は以下の通りです。

-   **`src/generate_repo_list/generate_repo_list.py`内の主要関数**
    -   役割: リポジトリ一覧の自動生成処理全体を制御するメイン関数
    -   引数: `username` (GitHubユーザー名), `output` (出力ファイルパス), `limit` (処理リポジトリ数上限、オプション) など
    -   戻り値: なし（指定された出力ファイルにMarkdownを書き出す）
    -   機能: GitHub APIからユーザーのリポジトリ情報を取得し、各リポジトリデータを整形・処理し、SEOに最適化されたMarkdown形式のリポジトリ一覧コンテンツを生成して指定されたファイルに書き出します。

-   **`src/generate_repo_list/project_overview_fetcher.py`内の主要関数**
    -   役割: 各リポジトリのプロジェクト概要を抽出する関数
    -   引数: `repository_url` (リポジトリのURL), `config` (設定オブジェクト)
    -   戻り値: プロジェクト概要の3行説明（文字列のリスト）
    -   機能: 指定されたリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、「プロジェクト概要」セクションの3行説明を抽出し、返却します。

-   **`src/generate_repo_list/markdown_generator.py`内の主要関数**
    -   役割: 処理済みリポジトリ情報からMarkdownコンテンツを生成する関数
    -   引数: `repository_data` (整形されたリポジトリ情報オブジェクト), `config` (設定オブジェクト)
    -   戻り値: 生成されたMarkdown文字列
    -   機能: 入力されたリポジトリのデータに基づいて、リポジトリ名、説明、バッジ、リンク、プロジェクト概要などを含む、整形されたMarkdown形式のコンテンツを組み立てて出力します。

-   **`src/generate_repo_list/badge_generator.py`内の主要関数**
    -   役割: リポジトリに関するバッジのMarkdown文字列を生成する関数
    -   引数: `repository_info` (リポジトリの詳細情報、例: 言語、ライセンス、アーカイブ状態など)
    -   戻り値: バッジのMarkdown文字列のリスト
    -   機能: リポジトリのプログラミング言語、ライセンス、アクティブ/アーカイブ状態などの情報に基づき、視覚的なバッジ（例: Shields.ioのバッジ）に対応するMarkdown形式のリンクを生成します。

-   **`src/generate_repo_list/repository_processor.py`内の主要関数**
    -   役割: GitHub APIから取得した生のリポジトリデータを処理・整形する関数
    -   引数: `raw_repo_json` (GitHub APIからの生データ), `config` (設定オブジェクト)
    -   戻り値: Markdown生成に適した形式に整形されたリポジトリ情報（辞書形式）
    -   機能: GitHub APIから取得したJSONデータを解析し、必要な情報を抽出し、日付のフォーマット、URLの生成、カテゴリ分類（アクティブ、アーカイブ、フォークなど）といった処理を行い、後続のMarkdown生成フェーズで利用しやすい形式に変換します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-08-14 07:17:07 JST
