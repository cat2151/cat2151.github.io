Last updated: 2026-01-16

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたリポジトリ一覧はSEOに最適化されたMarkdown形式で出力され、検索エンジンでの視認性を高めます。
- これにより、プロジェクトの発見可能性が向上し、LLMによるリポジトリ参照の精度向上も期待されます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターとして、生成されたMarkdownファイルを美しいウェブサイトとして公開し、検索エンジンに最適化されたコンテンツを提供します。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python - プロジェクトの主要なスクリプト言語です。pytest - Pythonコードのテストを実行するためのフレームワークです。ruff - コードスタイルの一貫性を保ち、品質を向上させるための自動整形およびリンターツールです。
- テスト: pytest - プロジェクトの各モジュールや機能の動作を検証するためのテストスイートを実行します。
- ビルドツール: Pythonスクリプト - GitHub APIからデータを取得し、最終的なMarkdownコンテンツを生成するプロセスを自動化します。
- 言語機能: Python - プロジェクト全体のロジック、データ処理、ファイル操作に利用されています。
- 自動化・CI/CD: GitHub Pages - 生成されたコンテンツをGitHubのリポジトリにプッシュすることで、自動的にウェブサイトとしてデプロイ・公開するためのプラットフォームです。
- 開発標準: ruff - Pythonコードの静的解析とフォーマットを行い、コードの可読性と保守性を統一された基準で維持します。

## ファイル階層ツリー
```
📄 .editorconfig
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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどのコーディングスタイルの一貫性を維持するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理システムに対し、指定されたファイルやディレクトリ（例: ビルド生成物、一時ファイル、秘密情報）を無視するよう指示します。
- **LICENSE**: このプロジェクトのソフトウェアライセンス（MITライセンス）に関する情報が記述されています。
- **README.md**: プロジェクトの目的、主要機能、使用方法、設定、開発者向け情報などがまとめられた、プロジェクトの入口となる説明ファイルです。
- **_config.yml**: Jekyll静的サイトジェネレーターの設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造など、サイト全体の動作を定義します。
- **assets/**: GitHub Pagesサイトで使用される静的リソース（例: ファビコン画像）が格納されるディレクトリです。
- **debug_project_overview.py**: 各リポジトリからプロジェクト概要を自動取得する機能（`project_overview_fetcher`）のデバッグや単体テストを行うための補助スクリプトです。
- **generated-docs/**: リポジトリの概要（`project-overview.md`）を含むドキュメントが配置される、あるいは参照されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって動的に生成される、ユーザーのGitHubリポジトリ一覧を記述したMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: 開発中に検討された課題や決定事項、アイデアなどがMarkdown形式で記録されているディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブサイトをユーザーのデバイスにインストール可能なアプリケーションのように振る舞わせるための設定を含みます。
- **pytest.ini**: `pytest`フレームワークのテスト設定ファイルです。テストの検出方法、追加オプション、テストレポートの出力などを定義します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージのリストです。
- **requirements.txt**: プロジェクトを本番稼働させるために必要な最小限のPythonパッケージのリストです。
- **robots.txt**: 検索エンジンのウェブクローラーに対し、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイルです。
- **ruff.toml**: `ruff`というPythonリンター/フォーマッターツールの設定ファイルです。コードスタイルのルール、無視するファイル、フォーマットオプションなどを定義し、コード品質を維持します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **src/generate_repo_list/**: リポジトリ一覧を生成するコアロジックを含むPythonモジュール群です。
        - **__init__.py**: Pythonがこのディレクトリをパッケージとして認識するために必要なファイルです。
        - **badge_generator.py**: リポジトリの言語やステータスなどを示すバッジ（画像）をMarkdown形式で生成する機能を提供します。
        - **config.yml**: リポジトリ一覧生成スクリプト（`generate_repo_list.py`）固有の設定（例: プロジェクト概要取得機能の有効/無効、タイムアウト）を定義するYAMLファイルです。
        - **config_manager.py**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するユーティリティ関数を提供します。
        - **date_formatter.py**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換する関数を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、リポジトリ情報から生成されるJSON-LDデータのテンプレートを定義します。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に利用する機能を提供します。
        - **markdown_generator.py**: 取得・処理されたリポジトリ情報に基づいて、SEOに最適化されたMarkdown形式のコンテンツを生成するロジックをカプセル化しています。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、そのリポジトリの3行の概要説明を自動的に取得する役割を担います。
        - **readme_badge_extractor.py**: 各リポジトリのREADMEファイルから特定の形式のバッジ情報を抽出し、一覧表示に利用する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、表示に適した形に加工する主要な処理を行います。
        - **seo_template.yml**: サイトの検索エンジン最適化（SEO）関連のメタデータや構造化データに関するテンプレート設定を定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言の変更が容易になります。
        - **template_processor.py**: Markdown生成の際に使用するJekyllなどのテンプレートファイルを処理し、動的なデータを組み込む機能を提供します。
        - **url_utils.py**: GitHubリポジトリのURLやGitHub PagesのURLなど、URL関連の操作や生成を行うユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールが正しく機能するかどうかを検証するための単体テストスクリプトです。
- **tests/**: プロジェクト全体のテストコードが格納されているディレクトリです。

## 関数詳細説明
提供されたプロジェクト情報から、具体的な関数の引数や戻り値の詳細な情報は特定できませんでした。しかし、各ファイルの役割に基づいて、プロジェクト内で主要な役割を果たすであろう関数について、その目的と機能の概要を説明します。

-   **`generate_repo_list.py`内の関数群**:
    -   **`main()`**: スクリプトの実行を開始するエントリポイント。コマンドライン引数の解析、GitHub APIからのデータ取得、リポジトリ情報の処理、Markdown生成、そして結果のファイルへの書き込みといった一連の処理フローをオーケストレーションします。
    -   **`_parse_arguments()`**: コマンドラインから渡された引数（例: `--username`, `--output`, `--limit`）を解析し、スクリプトが使用できる形式に変換します。
    -   **`_fetch_repositories(username)`**: 指定されたGitHubユーザー名に基づき、GitHub APIと連携してそのユーザーのリポジトリ一覧データを取得します。

-   **`repository_processor.py`内の関数群**:
    -   **`process_repository_data(repo_json)`**: GitHub APIから取得した生のリポジトリ情報（JSON形式）を受け取り、表示に必要な要素（名前、説明、言語、スター数など）を抽出・整形し、分類（アクティブ、アーカイブ、フォークなど）を行います。

-   **`project_overview_fetcher.py`内の関数群**:
    -   **`fetch_project_overview(repo_name, owner, config)`**: 指定されたリポジトリ（`repo_name`と`owner`で識別）の中から、設定で指定されたファイルパス（例: `generated-docs/project-overview.md`）を見つけ、そのファイルからプロジェクトの3行概要を抽出して返します。APIリクエストやファイル内容の解析を行います。
    -   **`_parse_overview_markdown(markdown_content)`**: 取得したMarkdown形式のコンテンツから、特定のセクションタイトル（例: "## プロジェクト概要"）の下にある3行の説明文を解析し、抽出します。

-   **`markdown_generator.py`内の関数群**:
    -   **`generate_repo_list_markdown(processed_repos, strings_data)`**: `repository_processor`によって処理されたリポジトリ情報のリストと、表示用の文言データを受け取り、GitHub Pagesに掲載される最終的なMarkdown形式のリポジトリ一覧コンテンツ全体を構築します。
    -   **`generate_repository_section(repo_data)`**: 個々のリポジトリの情報を基に、そのリポジトリに関するMarkdownスニペット（タイトル、リンク、概要、バッジなど）を生成します。

-   **`badge_generator.py`内の関数群**:
    -   **`generate_language_badge(language)`**: 特定のプログラミング言語（例: Python, JavaScript）に対応するスタイルで、言語名を示すバッジのMarkdown文字列（例: `![Python](...)`）を生成します。
    -   **`generate_status_badge(status)`**: リポジトリの現在のステータス（例: "Archived", "Active"）を示すバッジのMarkdown文字列を生成します。

-   **`config_manager.py`内の関数群**:
    -   **`load_config(file_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
    -   **`load_secrets(file_path)`**: 指定されたパスからTOML形式の秘密情報ファイル（例: GitHubトークン）を読み込みます。

-   **`date_formatter.py`内の関数群**:
    -   **`format_date(iso_date_string)`**: ISO 8601形式などの日付文字列を受け取り、ユーザーにとって読みやすい形式（例: "YYYY年MM月DD日"）に整形して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-01-16 07:06:45 JST
