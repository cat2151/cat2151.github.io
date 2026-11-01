Last updated: 2026-11-02

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのGitHub Pages用Markdownを自動生成します。
- これにより、リポジトリ一覧や各リポジトリページが検索エンジンにインデックスされやすくなります。
- LLMがGitHubリポジトリを参照できない課題を緩和し、開発効率向上を目指します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesで静的サイトを生成するためのエンジン。このプロジェクトで生成されるMarkdownファイルをウェブサイトとしてレンダリングします。
    - **Markdown**: Jekyllサイトのコンテンツ記述形式。リポジトリ一覧がこの形式で自動生成されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語。GitHub APIとの通信、リポジトリ情報の処理、Markdownの生成など、コアなロジックを実装しています。
    - **Git/GitHub**: ソースコードのバージョン管理システムであり、リポジトリ情報のAPI提供元です。
- テスト:
    - **pytest**: Pythonプロジェクトの単体テストおよび統合テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py`が、GitHub APIから取得した情報をもとにMarkdownファイルを「ビルド」（生成）する役割を担います。
    - **Jekyll**: 生成されたMarkdownファイルをGitHub Pages上で静的サイトとして「ビルド」します。
- 言語機能:
    - **Python標準ライブラリ**: ファイルI/O、JSON/YAMLパース、コマンドライン引数 (`argparse`) 処理、文字列操作など、Pythonの基本的な機能とライブラリが活用されています。
- 自動化・CI/CD:
    - **GitHub API**: リポジトリ情報の自動取得に利用されます。
    - **GitHub Actions (間接的)**: `.github_automation`ディレクトリの存在から、関連する自動化ワークフローが存在する可能性を示唆しますが、本プロジェクト自体がCI/CDパイプラインを構築するわけではありません。
- 開発標準:
    - **ruff**: Pythonコードのスタイルを検査（リンティング）し、自動修正（フォーマット）するためのツールです。
    - **.editorconfig**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどのコード書式を統一するための設定ファイルです。

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
-   `.editorconfig`: 開発環境（エディタ/IDE）間でコードの書式（インデント、文字コードなど）を統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   `check_large_files/`: Gitリポジトリ内の大容量ファイルをチェックするためのサブディレクトリです。
        -   `README.md`: `check_large_files`機能に関する説明を提供します。
        -   `check-large-files.toml`: 大容量ファイル検出スクリプトの設定（例: 閾値）を定義します。
        -   `scripts/check_large_files.py`: 指定されたサイズを超えるファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理から除外すべきファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの概要、目的、主な機能、使い方、設定、テスト方法などをまとめたメインのドキュメントファイルです。
-   `_config.yml`: Jekyllサイト全体の構成や設定（サイトタイトル、テーマなど）を定義するファイルです。
-   `assets/`: GitHub Pagesサイトで使用される静的リソース（ファビコン画像など）を格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なる解像度のファビコン画像ファイルです。
-   `debug_project_overview.py`: プロジェクト概要取得機能のテストやデバッグに特化したスクリプトです。
-   `generated-docs/`: 各リポジトリから取得されるプロジェクト概要が記述された`project-overview.md`ファイルが格納されることが想定されるディレクトリです（このリポジトリ内では空）。
-   `googled947dc864c270e07.html`: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイルです。このファイル自体には機能的なロジックはありません。
-   `index.md`: `src/generate_repo_list/generate_repo_list.py`スクリプトによって出力される、リポジトリ一覧を含むMarkdownファイルです。Jekyllによってウェブページとしてレンダリングされます。
-   `issue-notes/`: 開発中の課題や検討事項に関するメモを格納するためのディレクトリです。
    -   `22.md`: 特定のGitHub Issue（#22）に関する詳細なメモや考察が記述されているファイルです。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加、アイコン、表示モードなどを定義します。
-   `pytest.ini`: `pytest`フレームワークの実行設定を定義するファイルです。テストの検出パスやプラグインなどを指定します。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   `requirements.txt`: プロジェクトの実行環境（本番環境など）で必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   `robots.txt`: 検索エンジンクローラーに対して、ウェブサイトのどのページをクロールしてよいか、どのページを無視すべきかを指示するファイルです。
-   `ruff.toml`: Pythonのリンター/フォーマッターである`ruff`の設定ファイルです。コードスタイルや静的解析のルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: `src`ディレクトリがPythonパッケージであることを示します。
    -   `generate_repo_list/`: リポジトリ一覧を生成するコアロジックを構成するモジュール群です。
        -   `__init__.py`: `generate_repo_list`ディレクトリがPythonパッケージであることを示します。
        -   `badge_generator.py`: リポジトリの言語やステータスに応じたバッジのMarkdownを生成する機能を提供します。
        -   `config.yml`: プロジェクト概要取得機能などの技術的なパラメータや設定値を定義するYAML形式の設定ファイルです。
        -   `config_manager.py`: `config.yml`や外部の秘密情報 (`secrets.toml`) などの設定ファイルを読み込み、管理するためのモジュールです。
        -   `date_formatter.py`: ISO形式の日付文字列をユーザーフレンドリーな形式に変換するなど、日付のフォーマットに関連するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、その情報に基づいてJekyll対応のMarkdownファイルを生成する、このプロジェクトのメインスクリプトです。
        -   `json_ld_template.json`: SEO（検索エンジン最適化）のために使用されるJSON-LD形式の構造化データテンプレートです。
        -   `language_info.py`: 各リポジトリのプログラミング言語情報を処理し、表示に利用するためのロジックを実装しています。
        -   `markdown_generator.py`: 取得・整形されたリポジトリデータから、最終的なリポジトリ一覧のMarkdownコンテンツを構築する役割を担います。
        -   `project_overview_fetcher.py`: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        -   `readme_badge_extractor.py`: READMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、表示に適した形に加工・整形するためのロジックを実装しています。
        -   `seo_template.yml`: SEO関連のメタデータやページ固有のテンプレート設定を定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算し、Markdown出力に利用する機能を提供します。
        -   `strings.yml`: プロジェクト全体で表示されるメッセージや文言（例: ヘッダー、フッターのテキスト）を一元的に管理するYAMLファイルです。
        -   `template_processor.py`: Markdown生成の際に、特定のテンプレートを処理し、動的なコンテンツを埋め込む機能を提供します。
        -   `url_utils.py`: GitHub PagesのURL生成など、URLに関連する様々なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest`テスト実行時に共通で利用されるフィクスチャや設定を定義するファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator.py`モジュールの統合テストを行います。
    -   `test_check_large_files.py`: `check_large_files.py`スクリプトのテストを行います。
    -   `test_config.py`: 設定ファイル (`config.yml`, `secrets.toml`) の読み込みとパースが正しく行われるかをテストします。
    -   `test_date_formatter.py`: `date_formatter.py`モジュールの日付フォーマット機能のテストを行います。
    -   `test_environment.py`: プロジェクトの実行環境に関する基本的なテスト（例: 必要な依存関係の存在）を行います。
    -   `test_integration.py`: 主要なモジュール間の連携を含む、プロジェクト全体の主要機能の統合テストです。
    -   `test_markdown_generator.py`: `markdown_generator.py`モジュールが正しいMarkdownを生成するかをテストします。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher.py`モジュールがプロジェクト概要を正確に抽出するかをテストします。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor.py`モジュールがREADMEから正しくバッジを抽出するかをテストします。
    -   `test_repository_processor.py`: `repository_processor.py`モジュールがリポジトリデータを正しく処理・整形するかをテストします。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、主要な機能は以下のファイル内の関数群で実現されています（具体的な引数や戻り値は情報から推測）。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`:
        -   **役割**: プログラムのエントリーポイントであり、リポジトリ一覧生成処理全体のオーケストレーションを行います。コマンドライン引数の解析、GitHub APIからの情報取得、データの処理、Markdownコンテンツの生成、ファイルへの出力といった一連のフローを制御します。
        -   **引数**: なし（内部で`argparse`を用いてコマンドライン引数を処理します）
        -   **戻り値**: なし（主な結果はMarkdownファイルの生成です）

-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_repositories(username, limit=None)`:
        -   **役割**: GitHub APIを呼び出し、指定されたユーザーのリポジトリ情報を取得します。オプションで取得するリポジトリ数を制限できます。
        -   **引数**: `username` (str): GitHubユーザー名、`limit` (int, optional): 取得するリポジトリ数の上限。
        -   **戻り値**: `list[dict]`: GitHub APIから取得した、加工前のリポジトリ情報のリスト。
    -   `process_repository_data(repo_data)`:
        -   **役割**: GitHub APIから取得した個々の生のリポジトリデータ（辞書形式）を受け取り、必要な情報を抽出し、整形して、後のMarkdown生成に適した形式に変換します。アクティブ/アーカイブ/フォークの分類なども行います。
        -   **引数**: `repo_data` (dict): 単一のリポジトリに関するGitHub APIからの生データ。
        -   **戻り値**: `dict`: 処理され、整形されたリポジトリ情報。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_markdown(repositories)`:
        -   **役割**: 処理済みのリポジトリ情報（リスト）を受け取り、それらをJekyllが解釈できる形式のMarkdown文字列として構築します。SEO最適化されたメタデータやバッジ、プロジェクト概要なども組み込みます。
        -   **引数**: `repositories` (list[dict]): `repository_processor.py`によって整形されたリポジトリ情報のリスト。
        -   **戻り値**: `str`: 生成されたMarkdownコンテンツの全体文字列。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `get_project_overview(repo_name, owner)`:
        -   **役割**: 指定されたリポジトリ（`repo_name`と`owner`で識別）の`generated-docs/project-overview.md`ファイルをGitHubから取得し、そこから「プロジェクト概要」セクションの3行説明を抽出します。
        -   **引数**: `repo_name` (str): リポジトリ名、`owner` (str): リポジトリの所有者名。
        -   **戻り値**: `str`: 抽出された3行のプロジェクト概要（抽出できない場合は空文字列またはデフォルトメッセージ）。

-   **`src/generate_repo_list/badge_generator.py`**
    -   `create_badge_markdown(language)`:
        -   **役割**: 指定されたプログラミング言語やその他の属性（例: アクティブ、アーカイブ）に基づいて、対応するMarkdown形式のバッジを生成します。
        -   **引数**: `language` (str): プログラミング言語名（例: "Python"）。
        -   **戻り値**: `str`: バッジを表すMarkdown文字列。

-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config()`:
        -   **役割**: `config.yml`や`secrets/secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で利用可能な設定値を提供します。APIトークンなどの機密情報も安全に扱います。
        -   **引数**: なし
        -   **戻り値**: `dict`: ロードされた設定値を含む辞書。

-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(iso_date_string)`:
        -   **役割**: GitHub APIから返されるISO 8601形式の日付文字列（例: "2023-01-01T12:00:00Z"）を受け取り、ユーザーにとって読みやすい形式（例: "2023年1月1日"）に変換します。
        -   **引数**: `iso_date_string` (str): ISO 8601形式の日付と時刻の文字列。
        -   **戻り値**: `str`: フォーマットされた日付文字列。

-   **`src/generate_repo_list/url_utils.py`**
    -   `get_github_pages_url(username, repo_name)`:
        -   **役割**: 指定されたGitHubユーザー名とリポジトリ名に基づいて、そのリポジトリのGitHub PagesのURLを構築します。
        -   **引数**: `username` (str): GitHubユーザー名、`repo_name` (str): リポジトリ名。
        -   **戻り値**: `str`: 完成したGitHub PagesのURL。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
（提供された情報からは具体的な呼び出し階層を生成できませんでしたが、
`src/generate_repo_list/generate_repo_list.py` の `main` 関数が中心となり、
`config_manager.py`, `repository_processor.py`, `project_overview_fetcher.py`, `markdown_generator.py`
などのモジュール内の関数を順次呼び出していると推測されます。）

---
Generated at: 2026-11-02 07:08:26 JST
