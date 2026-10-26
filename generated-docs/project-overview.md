Last updated: 2026-10-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定されたユーザーのリポジトリ情報を取得します。
- 取得した情報に基づき、SEO最適化されたGitHub Pages向けリポジトリ一覧のMarkdownファイルを自動生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤): Markdownファイルを静的サイトとしてHTMLに変換し、Webサイトとして公開するためのフレームワーク。
- 音楽・オーディオ: 該当なし。本プロジェクトでは音楽やオーディオ関連技術は使用していません。
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからの情報取得やMarkdown生成ロジックの実装に使用。
    - **Git**: ソースコードのバージョン管理システム。
    - **GitHub**: ソースコードホスティング、GitHub PagesによるWebサイト公開、GitHub APIの提供元。
    - **`pytest`**: Pythonコードのテストフレームワーク。機能の正確性を保証するために使用。
    - **`ruff`**: Pythonコードの高速リンター・フォーマッター。コード品質と一貫性を維持するために使用。
- テスト: **`pytest`**: Pythonで記述された各種モジュールや機能の単体テスト、結合テストを実行するために使用。
- ビルドツール: **Jekyll**: GitHub Pages上でMarkdownファイルをHTMLに変換するプロセスを担う内部的なビルドメカニズム。
- 言語機能: **Python**: f-strings（文字列フォーマット）、辞書操作、ファイルI/Oなど、Pythonの標準的な言語機能やライブラリを多用。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリ内のスクリプトを通じて、大容量ファイルチェックなどの自動化されたタスクに使用。
    - (注: プロジェクトはCI/CD不要のローカル開発重視とされていますが、GitHub Actionsは一部の自動チェックに利用されています。)
- 開発標準:
    - **`ruff`**: コードのスタイルガイド強制、潜在的なバグの検出に使用。
    - **`.editorconfig`**: 異なるエディタ間でのコーディングスタイル（インデント、改行コードなど）の統一に使用。

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどの基本的なコードスタイルを統一するための設定ファイルです。
-   **`.github_automation/check_large_files/`**: GitHub Actionsを用いて、リポジトリ内の大容量ファイルをチェックする自動化スクリプト群を格納するディレクトリです。
    -   **`README.md`**: 大容量ファイルチェック機能に関する説明が記述されています。
    -   **`check-large-files.toml`**: 大容量ファイルチェックの設定（例: 許容サイズ上限、チェック対象外ファイルなど）を定義するファイルです。
    -   **`scripts/check_large_files.py`**: 実際の大容量ファイルチェック処理を実行するPythonスクリプトです。
-   **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド成果物、一時ファイル、個人情報など）を指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記述されており、プロジェクトの利用条件を明示します。
-   **`README.md`**: プロジェクト全体の目的、概要、機能、セットアップ方法、実行コマンド、ライセンス情報などを説明する、プロジェクトの顔となるファイルです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
-   **`assets/`**: GitHub Pagesサイトで使用される静的アセット（画像ファイル、ファビコンなど）を格納するディレクトリです。
    -   **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるファビコン画像ファイルです。
-   **`debug_project_overview.py`**: `project_overview` 機能（各リポジトリの概要を抽出する機能）のデバッグやテストを目的としたPythonスクリプトです。
-   **`generated-docs/`**: 各リポジトリから自動生成されたドキュメント（例: プロジェクト概要ファイル `project-overview.md`）が配置されることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるウェブサイトの所有権確認に使用されるHTMLファイルです。
-   **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトによって自動生成されたリポジトリ一覧がここに出力されます。
-   **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや調査結果を記録したMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルです。サイトの表示名、アイコン、テーマカラー、起動時の表示モードなどを定義し、モバイルデバイスでの体験を向上させます。
-   **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。テストの検出方法、プラグイン、レポート形式などを定義します。
-   **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonの依存ライブラリをリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトの実行（本番環境）に必要となるPythonの依存ライブラリをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するファイルです。SEO対策に利用されます。
-   **`ruff.toml`**: Pythonコードのリンター・フォーマッターである `ruff` の設定ファイルです。コードスタイル、ルールセット、無視するエラーなどを定義します。
-   **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    -   **`__init__.py`**: Pythonのパッケージであることを示す空のファイルです。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能に関連する全てのPythonモジュールを格納するサブパッケージです。
        -   **`__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
        -   **`badge_generator.py`**: リポジトリの技術スタック、ライセンス、ステータスなどを示すバッジのMarkdownを生成するロジックが含まれます。
        -   **`config.yml`**: プロジェクト概要取得機能やGitHub API関連の技術的パラメータを設定するためのYAMLファイルです。
        -   **`config_manager.py`**: `config.yml` や `strings.yml` など、プロジェクトで使用する各種設定ファイルを読み込み、管理するためのモジュールです。
        -   **`date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: このプロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力する全体の処理を制御します。
        -   **`json_ld_template.json`**: 検索エンジンがWebページの情報をより正確に理解できるよう支援する、JSON-LD形式の構造化データテンプレートです。SEO対策に利用されます。
        -   **`language_info.py`**: GitHubリポジトリが使用しているプログラミング言語に関する情報を処理・整形するロジックが含まれます。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成する主要なロジックを提供します。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動で抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから、特定のバッジ（ステータスバッジなど）の情報を抽出するロジックが含まれます。
        -   **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを詳細に分析し、表示に必要な情報（説明、URL、更新日など）に整形・加工するモジュールです。
        -   **`seo_template.yml`**: 検索エンジン最適化 (SEO) のためのメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算する機能を提供します。
        -   **`strings.yml`**: プロジェクトで使用される表示メッセージや静的な文言を一元的に管理するためのYAMLファイルです。多言語対応や文言修正を容易にします。
        -   **`template_processor.py`**: Markdown生成において、特定のテンプレート形式（Jekyll Liquidなど）を処理し、動的にコンテンツを埋め込むためのロジックを提供します。
        -   **`url_utils.py`**: GitHubリポジトリや関連ドキュメントへのURLを生成・整形するためのユーティリティ関数群です。
-   **`test_project_overview.py`**: `project_overview_fetcher` モジュール（プロジェクト概要取得機能）の単体テストや統合テストを記述したスクリプトです。
-   **`tests/`**: プロジェクトの様々なコンポーネントに対するテストコードを格納するディレクトリです。
    -   **`conftest.py`**: `pytest` のフィクスチャ（テストヘルパー関数やデータ）やテストフックを定義するためのファイルです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストを記述しています。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述しています。
    -   **`test_config.py`**: 設定ファイルの読み込みや解析に関するテストを記述しています。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテストを記述しています。
    -   **`test_environment.py`**: 開発・実行環境の設定が適切であるかを確認するテストを記述しています。
    -   **`test_integration.py`**: プロジェクト全体の主要なフローやモジュール間の連携に関する結合テストを記述しています。
    -   **`test_markdown_generator.py`**: Markdown生成機能のテストを記述しています。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述しています。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを記述しています。
    -   **`test_repository_processor.py`**: リポジトリ情報処理機能のテストを記述しています。

## 関数詳細説明
提供された情報からは具体的なPython関数のシグネチャ（引数、戻り値）を詳細に特定することは困難ですが、主要なモジュールにおける役割と機能を以下に説明します。

-   **`src/generate_repo_list/generate_repo_list.py` 内の主要な関数（例: `main` 関数）**
    *   **役割**: プロジェクト全体のエントリポイントとして、リポジトリ一覧のMarkdown生成プロセスを統括します。
    *   **引数**: コマンドラインから `--username` (GitHubユーザー名), `--output` (出力ファイル名), `--limit` (処理するリポジトリ数の上限、オプション) などの引数を受け取ります。
    *   **戻り値**: なし。処理結果として指定されたファイルにMarkdownを書き出します。
    *   **機能**: 設定ファイルの読み込み、GitHub APIからのリポジトリ情報取得、各リポジトリのデータ処理、Markdownコンテンツの生成、そして最終的なファイルへの書き込みまでの一連の流れをオーケストレーションします。

-   **`src/generate_repo_list/repository_processor.py` 内の主要な関数（例: `process_repository` 関数）**
    *   **役割**: GitHub APIから取得した個々のリポジトリデータを受け取り、表示に適した形に整形・加工します。
    *   **引数**: リポジトリの生データ（辞書形式など）や、処理に必要な設定情報などを受け取ります。
    *   **戻り値**: 整形されたリポジトリ情報（辞書形式など）を返します。
    *   **機能**: リポジトリ名、説明、URL、スター数、最終更新日、言語情報、バッジ、プロジェクト概要など、多岐にわたる情報を抽出し、欠損データの補完や書式設定を行います。

-   **`src/generate_repo_list/project_overview_fetcher.py` 内の主要な関数（例: `fetch_project_overview` 関数）**
    *   **役割**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md` など）から、プロジェクトの簡潔な概要説明を抽出します。
    *   **引数**: 処理対象のリポジトリ情報や、対象となるファイルパス、セクションタイトルなどの設定を受け取ります。
    *   **戻り値**: 抽出された3行のプロジェクト概要（文字列リストなど）を返します。概要が見つからない場合は空のリストなどを返します。
    *   **機能**: 指定されたリポジトリのコンテンツを取得し、設定されたファイルパスとセクションタイトルに基づいて概要部分をパースして抽出します。

-   **`src/generate_repo_list/markdown_generator.py` 内の主要な関数（例: `generate_repo_list_markdown` 関数）**
    *   **役割**: 処理済みのリポジトリ情報リストを受け取り、GitHub Pagesサイト用の最終的なMarkdownコンテンツを生成します。
    *   **引数**: 処理されたリポジトリ情報のリスト、SEO情報、テンプレート設定などを受け取ります。
    *   **戻り値**: 生成されたMarkdown形式の文字列を返します。
    *   **機能**: 各リポジトリの情報をテンプレートに組み込み、バッジ、プロジェクト概要、分類、JSON-LD構造化データなどを含む、SEOに配慮したMarkdown文字列全体を構築します。

-   **`src/generate_repo_list/badge_generator.py` 内の主要な関数（例: `generate_badge_markdown` 関数）**
    *   **役割**: リポジトリのステータス、使用言語、ライセンスなどの情報に基づいて、対応するバッジのMarkdownを生成します。
    *   **引数**: リポジトリの特定の属性（言語、アーカイブ状態など）を受け取ります。
    *   **戻り値**: 生成されたバッジのMarkdown文字列を返します。
    *   **機能**: 条件に応じて適切なバッジのURLとAltテキストを決定し、Markdown形式の画像リンクとして整形します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
（提供された情報では、詳細な関数呼び出し階層を特定できませんでした。）

---
Generated at: 2026-10-27 07:12:34 JST
