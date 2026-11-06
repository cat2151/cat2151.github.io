Last updated: 2026-11-07

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・整形します。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンからの発見性を高め、LLMによるリポジトリ参照を改善することを目指します。

## 技術スタック
- フロントエンド:
    -   **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトで生成されたMarkdownファイルをレンダリングするために使用されます。
    -   **Markdown**: Jekyllサイトのコンテンツ形式。本プロジェクトの主要な出力形式です。
- 音楽・オーディオ: N/A
- 開発ツール:
    -   **Python**: プロジェクトの主要なスクリプト言語。リポジトリ情報の取得、処理、Markdown生成を行います。
    -   **GitHub API**: GitHubからリポジトリ情報を取得するために利用します。
    -   **PyGithub**: PythonからGitHub APIを操作するためのライブラリ。
    -   **Requests**: HTTPリクエストを送信するためのPythonライブラリ。主に外部リソース（READMEやプロジェクト概要ファイル）の取得に使用されます。
    -   **PyYAML**: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) を読み書きするためのライブラリ。
    -   **TOML**: シークレット設定 (`secrets.toml` など) の読み込みに使用される設定ファイル形式。
    -   **Argparse**: コマンドライン引数を解析し、スクリプトの実行オプションを定義するために使用されます。
- テスト:
    -   **Pytest**: Pythonプロジェクトのテストフレームワーク。単体テスト、結合テストの実行に利用されます。
    -   **pytest-cov**: Pytestのプラグインで、テストカバレッジを測定するために使用されます。
- ビルドツール:
    -   (本プロジェクトはMarkdownコンテンツを「生成」するスクリプト群であり、直接的な「ビルドツール」は持ちません。生成されたMarkdownはJekyllによってビルド・レンダリングされます。)
- 言語機能:
    -   **Python**: オブジェクト指向プログラミング、データ構造操作、文字列処理など、プロジェクトのロジック実装に使用されます。
- 自動化・CI/CD:
    -   **GitHub Pages**: 生成されたMarkdownファイルをホストし、公開するためのプラットフォーム。
    -   **GitHub Actions (示唆)**: `.github_automation` ディレクトリの存在は、GitHub Actionsなどによる自動化スクリプトがデプロイプロセスなどで利用される可能性を示唆しています。
- 開発標準:
    -   **Ruff**: Pythonコードのリンティングとフォーマットを高速に行うツール。`ruff.toml`でルールが定義されています。
    -   **.editorconfig**: さまざまなエディタやIDEでコードのスタイルを一貫させるための設定ファイル。

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
-   `.editorconfig`: 異なるIDEやエディタ間でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    -   `check_large_files/`: 大容量ファイルの検出に関連するスクリプトや設定を格納しています。
        -   `README.md`: `check_large_files`機能に関する説明を提供します。
        -   `check-large-files.toml`: 大容量ファイルチェックの設定（例: 閾値、対象ファイルなど）を定義します。
        -   `scripts/check_large_files.py`: 指定された閾値を超える大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitが追跡しないファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   `README.md`: プロジェクトの概要、使い方、設定、開発者向け情報などを説明するメインのドキュメントファイルです。
-   `_config.yml`: Jekyllサイト全体の共通設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
-   `assets/`: サイトで使用される画像、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）画像です。
-   `debug_project_overview.py`: `project_overview`機能のデバッグや単体テスト実行に使用されるスクリプトです。
-   `generated-docs/`: プロジェクトが生成したドキュメントやファイルを格納するためのディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイルです。
-   `index.md`: GitHub Pagesサイトのトップページとして表示されるMarkdownファイルです。このプロジェクトによってリポジトリ一覧が生成され、このファイルに書き込まれます。
-   `issue-notes/22.md`: 特定のIssueに関するメモや詳細情報を格納するファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の定義ファイルで、アプリの表示方法や動作を設定します。
-   `pytest.ini`: `pytest`テストフレームワークの設定ファイルです。テストの検出パス、マーカー、プラグインなどを設定します。
-   `requirements-dev.txt`: 開発時やテスト時に必要なPythonライブラリの依存関係を記述したファイルです。
-   `requirements.txt`: 本番環境でプロジェクトを実行するために必要なPythonライブラリの依存関係を記述したファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、または拒否するかを指示するファイルです。
-   `ruff.toml`: `ruff`リンター/フォーマッタの設定ファイルです。Pythonコードの品質とスタイルに関するルールを定義します。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリ一覧生成機能に関連するモジュールを格納するパッケージです。
        -   `__init__.py`: Pythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのバッジ（例: 言語バッジ、ステータスバッジ）を生成するロジックを含みます。
        -   `config.yml`: リポジトリ一覧生成スクリプトの技術的なパラメータ（例: プロジェクト概要取得設定、キャッシュ設定）を定義する設定ファイルです。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのメインエントリスクリプト。GitHub APIから情報を取得し、Markdownファイルを生成する処理をorchestrateします。
        -   `json_ld_template.json`: SEO最適化のためのJSON-LD形式の構造化データテンプレートです。
        -   `language_info.py`: リポジトリの言語情報を処理・整形するためのモジュールです。
        -   `markdown_generator.py`: 取得した情報からMarkdownコンテンツを生成するためのロジックを含みます。
        -   `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` から概要説明を抽出する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEからバッジ情報を抽出する機能を提供します。
        -   `repository_processor.py`: GitHubから取得した個々のリポジトリデータを処理し、必要な情報（概要、バッジなど）を抽出・整形するモジュールです。
        -   `seo_template.yml`: SEOメタデータやJSON-LDのテンプレート設定を定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（例: スター数、フォーク数）を計算または整形するモジュールです。
        -   `strings.yml`: UIの表示メッセージや文言を一元管理するための設定ファイルです。
        -   `template_processor.py`: Jekyllのテンプレートエンジンに渡すデータ構造を準備したり、Markdownテンプレートに情報を埋め込んだりする処理を行います。
        -   `url_utils.py`: URLに関連するユーティリティ関数（例: URLの検証、構築）を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールに関連するテストケースを定義するファイルです。
-   `tests/`: プロジェクトのテストコードを格納するディレクトリです。
    -   `conftest.py`: `pytest`のテストフィクスチャやフックを定義するためのファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの統合テストを定義します。
    -   `test_check_large_files.py`: `.github_automation/check_large_files`スクリプトのテストを定義します。
    -   `test_config.py`: 設定ファイルの読み込みや処理に関するテストを定義します。
    -   `test_date_formatter.py`: `date_formatter`モジュールのテストを定義します。
    -   `test_environment.py`: テスト環境の設定や依存関係に関するテストを定義します。
    -   `test_integration.py`: 主要な機能フローの統合テストを定義します。
    -   `test_markdown_generator.py`: `markdown_generator`モジュールのテストを定義します。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールのテストを定義します。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールのテストを定義します。
    -   `test_repository_processor.py`: `repository_processor`モジュールのテストを定義します。

## 関数詳細説明
提供されたプロジェクト情報から、個々の関数の具体的な役割、引数、戻り値、機能を詳細に特定することは困難でした。しかし、ファイル名とプロジェクトの説明に基づき、主要なモジュールにおける想定される関数の概要を以下に記述します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   **`main` 関数 (想定)**:
        -   **役割**: プロジェクトの主要な実行エントリポイント。GitHub APIからリポジトリ情報を取得し、整形してMarkdownファイルを生成する一連の処理を調整します。
        -   **引数**:
            -   `username` (str): GitHubユーザー名。
            -   `output` (str): 生成されたMarkdownファイルの出力先パス。
            -   `limit` (int, オプション): 処理するリポジトリ数の上限（主に開発・テスト用）。
        -   **戻り値**: なし（処理が成功した場合）。
        -   **機能**: コマンドライン引数を解析し、他のモジュール（例: `repository_processor`、`markdown_generator`）を呼び出して、最終的なリポジトリ一覧Markdownコンテンツを生成します。

-   **`src/generate_repo_list/repository_processor.py`**
    -   **`process_repository` 関数 (想定)**:
        -   **役割**: 個々のGitHubリポジトリの生データを解析し、Markdown生成に必要な形式に整形します。
        -   **引数**:
            -   `repository_data` (dictまたはオブジェクト): GitHub APIから取得した生のリポジトリ情報。
            -   `config` (dict): プロジェクト全体の設定情報。
        -   **戻り値**: 整形されたリポジトリ情報を含む辞書。
        -   **機能**: リポジトリ名、URL、説明、言語、スター数などの基本情報を抽出し、必要に応じて`project_overview_fetcher`や`readme_badge_extractor`などを利用して追加情報を取得・統合します。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   **`generate_markdown_content` 関数 (想定)**:
        -   **役割**: 処理されたリポジトリ情報リストを受け取り、最終的なMarkdown文字列を生成します。
        -   **引数**:
            -   `repositories_list` (list of dict): 処理済みのリポジトリ情報が格納されたリスト。
            -   `seo_data` (dict): SEOメタデータなど、Markdownテンプレートに埋め込むための追加データ。
        -   **戻り値**: 生成されたMarkdownコンテンツの文字列。
        -   **機能**: リポジトリ情報をもとに、Jekyll互換のMarkdown形式でリポジトリ一覧ページのコンテンツを構築します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **`fetch_project_overview` 関数 (想定)**:
        -   **役割**: 特定のリポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を抽出し、返します。
        -   **引数**:
            -   `repo_full_name` (str): ターゲットとなるリポジトリの完全な名前（例: "ユーザー名/リポジトリ名"）。
            -   `config` (dict): プロジェクト概要取得機能の設定（有効/無効、対象ファイル名、セクションタイトルなど）。
        -   **戻り値**: 抽出された3行の概要テキスト（文字列）、または取得できなかった場合は空文字列。
        -   **機能**: GitHub API（または直接アクセス）を介して指定されたファイルを読み込み、設定されたセクションタイトルに基づいて3行の概要を解析・抽出します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-07 07:07:33 JST
