Last updated: 2025-12-05

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・整理します。
- JekyllベースのGitHub Pagesサイト向けに、SEOに最適化されたリポジトリ一覧を生成します。
- リポジトリの発見性を高め、検索エンジンやLLMからの参照性を向上させることを目的としています。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として使用され、MarkdownファイルをHTMLに変換してサイトを生成します。)、**Markdown** (生成されるリポジトリ一覧やプロジェクト概要の記述に使用される軽量マークアップ言語です。)
- 音楽・オーディオ: 該当なし
- 開発ツール: **pytest** (Pythonで書かれたテストコードを実行するためのフレームワークです。ユニットテストや結合テストに利用されます。)、**ruff** (Pythonのコードスタイルを検査し、自動修正を行う高速なリンター兼フォーマッターです。)
- テスト: **pytest** (プロジェクトの各コンポーネントが期待通りに機能するかを検証するために使用されます。)
- ビルドツール: **Python** (スクリプトの実行環境であり、リポジトリ情報の取得、処理、Markdownファイルの生成といった一連の自動化処理を実行します。)
- 言語機能: **Python** (プロジェクトのコアロジックがこの言語で実装されています。)
- 自動化・CI/CD: 該当なし（本プロジェクトはローカルでの実行を重視しており、明示的なCI/CDパイプラインは採用していません。ただし、GitHub Pagesのデプロイ自体はGitHubの仕組みにより自動化されます。）
- 開発標準: **ruff** (コードの一貫性を保ち、品質を向上させるための静的解析ツールとして利用されています。)

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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタやIDE間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象から外すファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、使い方、設定方法などを説明するドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の基本的な設定（サイト名、テーマ、プラグインなど）を定義するファイルです。
-   **`assets/`**: GitHub Pagesサイトで使用される静的ファイル（ファビコン画像など）を格納するディレクトリです。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: サイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能の動作確認やデバッグを目的としたPythonスクリプトです。
-   **`generated-docs/`**: 他のリポジトリから自動的に取得された `project-overview.md` ファイルが一時的に格納される可能性のあるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために使用される認証ファイルです。
-   **`index.md`**: メインのスクリプトによって生成される、リポジトリ一覧が記述されたマークダウンファイルです。GitHub Pagesのトップページとして表示されます。
-   **`issue-notes/`**: 開発中の課題や検討事項、メモなどを個別のマークダウンファイルとして整理して格納するディレクトリです。
    -   **`10.md`, `12.md`, `14.md`, `2.md`, `4.md`, `6.md`, `8.md`**: 個別の課題やメモの内容を記述したマークダウンファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名称、アイコン、表示モードなど）を定義するファイルです。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイルです。
-   **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonライブラリとそのバージョンを一覧にしたファイルです。
-   **`requirements.txt`**: プロジェクトの本番運用に必要なPythonライブラリとそのバージョンを一覧にしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: Pythonのリンター/フォーマッターであるRuffの設定を定義するファイルです。
-   **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    -   **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧自動生成機能のコアロジックが格納されたPythonパッケージです。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや情報を視覚的に示すバッジ画像を生成するロジックを実装しています。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの詳細な技術的パラメータや設定値を定義するYAML形式の設定ファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）を読み込み、管理するためのクラスや関数を提供します。
        -   **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからのリポジトリ情報取得からMarkdown生成までの一連の処理を統括するメインの実行スクリプトです。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化のためにウェブページに構造化データ（JSON-LD形式）を埋め込む際のテンプレートです。
        -   **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語の統計情報などを処理・整形するロジックを提供します。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報や統計データをもとに、GitHub Pages用のSEO最適化されたMarkdownファイルを生成するロジックです。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 他のリポジトリに存在する `generated-docs/project-overview.md` ファイルからプロジェクト概要を自動的に取得する機能を提供します。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIを通じてリポジトリ情報を取得し、それを整形・フィルタリングするなど、後続の処理に適した形式に変換する役割を担います。
        -   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化に関するメタデータや構造化データ生成のためのテンプレート設定を定義するファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: 各リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するロジックです。
        -   **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownファイルやログ出力などで使用される、表示メッセージや固定文言を一元的に管理するYAMLファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: MarkdownやHTMLテンプレートにデータを埋め込み、最終的なコンテンツをレンダリングする汎用的な処理を提供します。
        -   **`src/generate_repo_list/url_utils.py`**: URLの検証、正規化、構築など、URLに関連するユーティリティ関数を集めたモジュールです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールが提供するプロジェクト概要取得機能の単体テストを記述したスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能に関するテストを行います。
    -   **`test_environment.py`**: 開発・実行環境の設定や依存関係が正しく機能するかを検証するテストです。
    -   **`test_integration.py`**: 複数のモジュールが連携して正しく動作するかを確認する統合テストです。
    -   **`test_markdown_generator.py`**: Markdown生成ロジックが期待通りの出力を行うかを確認するテストです。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールが正しくプロジェクト概要を取得できるかを確認するテストです。
    -   **`test_repository_processor.py`**: `repository_processor`モジュールがGitHubリポジトリ情報を正しく処理できるかを確認するテストです。

## 関数詳細説明
*   **`src/generate_repo_list/generate_repo_list.py`**
    *   **`main()`**: スクリプトのエントリポイント。コマンドライン引数を解析し、リポジトリ一覧生成の主要な処理を呼び出します。
        *   引数: なし (コマンドライン引数は内部で処理)
        *   戻り値: なし
        *   機能: プログラムの実行を開始し、設定、データ取得、Markdown生成の流れを制御します。
    *   **`generate_repo_list(username, output_file, limit=None)`**: 指定されたユーザー名のリポジトリ情報を取得し、指定されたファイルにMarkdown形式のリポジトリ一覧を生成します。
        *   引数: `username` (str): GitHubユーザー名, `output_file` (str): 出力ファイルパス, `limit` (int, optional): 処理するリポジトリ数の上限
        *   戻り値: なし
        *   機能: GitHub APIからリポジトリ情報をフェッチし、各リポジトリを処理してMarkdownを組み立て、最終的にファイルに書き出します。

*   **`src/generate_repo_list/config_manager.py`**
    *   **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
        *   引数: `config_path` (str): 設定ファイルのパス
        *   戻り値: dict: 設定内容を格納した辞書
        *   機能: プロジェクトの動作に必要なパラメータや外部サービスの認証情報などを設定ファイルから取得します。

*   **`src/generate_repo_list/repository_processor.py`**
    *   **`fetch_repositories(username, github_token)`**: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。
        *   引数: `username` (str): GitHubユーザー名, `github_token` (str): GitHub APIアクセストークン
        *   戻り値: list: リポジトリ情報の辞書リスト
        *   機能: GitHub APIへの認証付きリクエストを行い、ユーザーが所有する公開リポジトリのデータを取得します。
    *   **`process_repository_data(repo_data, config)`**: 取得した単一のリポジトリデータに対して、追加情報の取得（プロジェクト概要など）や整形処理を行います。
        *   引数: `repo_data` (dict): 単一のリポジトリの生データ, `config` (dict): プロジェクト設定
        *   戻り値: dict: 処理済みのリポジトリデータ
        *   機能: リポジトリの各種メタデータ（説明、言語、スター数など）を抽出し、必要に応じて外部から追加情報を統合します。

*   **`src/generate_repo_list/project_overview_fetcher.py`**
    *   **`fetch_project_overview(repo_url, config)`**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出します。
        *   引数: `repo_url` (str): リポジトリのGitHub Pages URLまたは生ファイルURL, `config` (dict): プロジェクト概要取得に関する設定
        *   戻り値: list or None: 抽出された3行の説明、またはNone
        *   機能: リモートのMarkdownファイルにHTTPリクエストを送り、指定されたセクションから箇条書きの概要をパースします。

*   **`src/generate_repo_list/markdown_generator.py`**
    *   **`generate_markdown(repositories, config)`**: 処理済みのリポジトリ情報のリストを元に、GitHub Pages用のMarkdownコンテンツを生成します。
        *   引数: `repositories` (list): 処理済みリポジトリデータのリスト, `config` (dict): プロジェクト設定
        *   戻り値: str: 生成されたMarkdown文字列
        *   機能: 各リポジトリを整形し、SEOに適した形式で一覧表示するためのMarkdown構造を構築します。

*   **`src/generate_repo_list/badge_generator.py`**
    *   **`generate_badge(status)`**: 指定されたステータスに基づいたバッジのMarkdownまたはURLを生成します。
        *   引数: `status` (str): リポジトリのステータス（例: "active", "archived", "fork"）
        *   戻り値: str: バッジの表現文字列
        *   機能: リポジトリの種類や状態を視覚的に示すためのバッジを生成します。

*   **`src/generate_repo_list/template_processor.py`**
    *   **`render_template(template_content, data)`**: 提供されたテンプレート文字列とデータを使用して、最終的な文字列を生成します。
        *   引数: `template_content` (str): テンプレート文字列, `data` (dict): テンプレートに埋め込むデータ
        *   戻り値: str: レンダリングされた文字列
        *   機能: プレースホルダーを含むテンプレートに動的な情報を挿入し、カスタマイズされた出力を生成します。

*   **`test_project_overview.py`** や **`tests/*.py`** 内の関数
    *   **`test_something_feature()`**: 各テストファイルには、特定の機能やモジュールの動作を検証するためのテスト関数が含まれています。
        *   引数: 通常なし (pytestのフィクスチャを使用する場合あり)
        *   戻り値: なし (アサーションが失敗するとテストエラー)
        *   機能: 想定される入力に対する出力や、特定の条件での動作が正しいことを確認します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-05 07:06:01 JST
