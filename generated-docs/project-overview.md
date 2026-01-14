Last updated: 2026-01-15

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得します。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧を自動生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として、生成されたMarkdownファイルを表示するために使用されます。)
- 音楽・オーディオ: なし
- 開発ツール: GitHub API (リポジトリ情報の取得に利用されるAPI群です。)
- テスト: pytest (Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。)
- ビルドツール: なし (Markdownファイルの自動生成が主な機能であり、専用のビルドツールは使用していません。)
- 言語機能: Python (プロジェクトのメイン開発言語であり、スクリプトの実行環境です。)
- 自動化・CI/CD: なし (プロジェクト情報から明示的な自動化・CI/CDツールは確認できませんでした。)
- 開発標準: ruff (Pythonコードの静的解析とフォーマットを行うための高速なリンターです。)

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。一時ファイルやログ、依存関係などが含まれます。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。著作権と利用条件を定めます。
-   **`README.md`**: プロジェクトの概要、目的、セットアップ方法、使い方、ライセンスなど、プロジェクトに関する基本的な情報を提供するマークダウンファイルです。
-   **`_config.yml`**: Jekyllサイトのグローバルな設定ファイルです。テーマ、パーマリンク構造、プラグインなどの設定を定義します。
-   **`assets/`**: Jekyllサイトで使用される静的なアセット（画像、アイコン、CSS、JavaScriptファイルなど）を格納するディレクトリです。
    -   **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグを目的としたPythonスクリプトです。機能の単体テストや動作確認に利用されます。
-   **`generated-docs/`**: `project-overview.md` など、このシステムが他のリポジトリから取得するプロジェクト概要ファイルが一時的、または参照元として配置されることが想定されるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイトの所有権を証明するために使用されるHTMLファイルです。
-   **`index.md`**: GitHub Pagesサイトのルートページ（トップページ）となるマークダウンファイルです。このプロジェクトによってリポジトリ一覧がここに自動生成されます。
-   **`issue-notes/`**: プロジェクト開発中の課題や検討事項に関するメモを格納するディレクトリです。Markdown形式で記録されています。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示モードなど）を定義するファイルです。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法や検出ルールなどを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト環境で必要なPythonパッケージとそのバージョンを列挙したファイルです。
-   **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、あるいは除外すべきかを指示するファイルです。
-   **`ruff.toml`**: PythonコードのリンティングとフォーマットツールであるRuffの設定ファイルです。コードスタイルのルールや除外パスを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術を示すバッジ画像を生成するロジックを実装したファイルです。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト固有の実行時設定（例: GitHubトークン、API設定など）を定義するYAMLファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）の読み込み、解析、管理を行うためのユーティリティ関数やクラスが含まれるファイルです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに変換するためのユーティリティ関数を提供するファイルです。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリポイントとなるスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD形式）のテンプレートファイルです。SEO向上のため、リポジトリ情報のメタデータを定義します。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・解析するためのロジックを実装したファイルです。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けの整形されたMarkdownコンテンツを生成するロジックが含まれるファイルです。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要を抽出し、取得する機能を提供するファイルです。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出し、解析する機能を提供するファイルです。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形、フィルタリング、追加情報付与などの処理を行うコアロジックを実装したファイルです。
        -   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するYAMLファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数、最終更新日時など）を計算・集計するロジックを提供するファイルです。
        -   **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        -   **`src/generate_repo_list/template_processor.py`**: Markdown生成などで使用されるテンプレートファイルの読み込み、変数の置換などの処理を行うファイルです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供するファイルです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのPythonスクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`tests/test_badge_generator_integration.py`**: `badge_generator.py` の統合テストを行うファイルです。
    -   **`tests/test_config.py`**: 設定管理関連のロジックをテストするファイルです。
    -   **`tests/test_date_formatter.py`**: `date_formatter.py` の日付フォーマット機能をテストするファイルです。
    -   **`tests/test_environment.py`**: プロジェクトの実行環境に関するテストを行うファイルです。
    -   **`tests/test_integration.py`**: プロジェクトの主要なコンポーネント間の連携をテストする統合テストファイルです。
    -   **`tests/test_markdown_generator.py`**: `markdown_generator.py` のMarkdown生成機能をテストするファイルです。
    -   **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のテストを行うファイルです。
    -   **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` の機能をテストするファイルです。
    -   **`tests/test_repository_processor.py`**: `repository_processor.py` のリポジトリ処理機能をテストするファイルです。

## 関数詳細説明
プロジェクト情報に具体的な関数名やシグネチャに関する詳細な記述がないため、各ファイルの役割に基づいて主要な関数の概要を説明します。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badge(repo_data: dict) -> str`: リポジトリ情報（言語、ステータスなど）を受け取り、対応するバッジのマークダウンまたはURLを生成します。
-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(file_path: str) -> dict`: 指定されたパスのYAML設定ファイルを読み込み、辞書形式で返します。
    -   `get_setting(key: str, default=None)`: 設定値を取得します。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_date(datetime_obj, format_string: str) -> str`: 日時オブジェクトを指定されたフォーマット文字列で整形します。
-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: プロジェクトの主要な実行フローを制御する関数です。GitHub APIからのリポジトリ取得、処理、Markdown生成、ファイル出力までの一連のプロセスを管理します。
    -   `parse_arguments()`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、リミットなどのオプションを取得します。
-   **`src/generate_repo_list/language_info.py`**:
    -   `get_language_breakdown(repo_data: dict) -> dict`: リポジトリの言語使用状況を分析し、主要な言語とその割合を返します。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repository_markdown(repo_data: dict, overview_text: str) -> str`: 個々のリポジトリデータと概要テキストから、リポジトリ表示用のMarkdownスニペットを生成します。
    -   `generate_index_markdown(repo_list: list) -> str`: 処理されたリポジトリのリスト全体から、`index.md` 用の最終的なMarkdownコンテンツを生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_owner: str, repo_name: str, config: dict) -> str`: 指定されたリポジトリの `generated-docs/project-overview.md` ファイルから、設定に基づいてプロジェクト概要の3行説明を非同期に取得します。
-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   `extract_badges_from_readme(readme_content: str) -> list`: READMEのコンテンツから、Markdown形式のバッジ情報を解析・抽出します。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository(repo_data: dict, github_token: str) -> dict`: GitHub APIから取得した個々のリポジトリデータに追加処理（概要取得、バッジ抽出など）を適用し、表示用に整形されたデータを返します。
    -   `get_repositories(username: str, github_token: str, limit: int) -> list`: 指定されたユーザー名とGitHubトークンを使用して、GitHub APIからリポジトリのリストを取得します。
-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   `calculate_repository_statistics(repo_list: list) -> dict`: リポジトリのリスト全体から、総数、言語分布、最終更新の傾向などの統計情報を計算します。
-   **`src/generate_repo_list/template_processor.py`**:
    -   `render_template(template_content: str, data: dict) -> str`: 指定されたテンプレートコンテンツとデータを使用して、プレースホルダーを実際の値で置換し、最終的な文字列を生成します。
-   **`src/generate_repo_list/url_utils.py`**:
    -   `build_repo_url(username: str, repo_name: str) -> str`: GitHubリポジリのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析するための詳細な情報が提供されていないため、ツリーを生成できません。

---
Generated at: 2026-01-15 07:07:35 JST
