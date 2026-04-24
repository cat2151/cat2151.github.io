Last updated: 2026-04-25

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages向けのMarkdownを自動生成します。
- GitHubユーザーページでの検索エンジンクロール効率の課題を解決します。
- リポジトリ一覧と各リポジトリへのリンクをGitHub Pagesに生成し、SEOとLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド:
    -   Jekyll: GitHub Pagesで静的サイトを生成するためのエンジンとして、生成されたMarkdownファイルが利用されます。
    -   GitHub Pages: 生成されたリポジトリ一覧サイトをホストするためのプラットフォーム。
    -   Markdown: 本システムで生成されるリポジトリ一覧ページの記述形式。
    -   JSON-LD: 検索エンジン最適化（SEO）のための構造化データ形式で、`json_ld_template.json` で利用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    -   Python: メインのスクリプト言語として、リポジトリ情報の取得とMarkdown生成ロジックの実装に使用されます。
    -   Git / GitHub: プロジェクトのバージョン管理およびリポジトリホスティングに利用されます。
    -   `requests` ライブラリ: GitHub APIとのHTTP通信を行い、リポジトリ情報を取得するために使用されます。
    -   `PyYAML`: `config.yml` や `strings.yml` などのYAML形式の設定ファイルを読み書きするために使用されます。
    -   `toml`: `secrets.toml` などTOML形式の秘密情報ファイルを読み書きするために使用されます。
    -   `ruff`: Pythonコードの静的解析、フォーマット、リンティングを行い、コード品質を維持するために使用されます。
- テスト:
    -   `pytest`: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
- ビルドツール:
    -   Pythonスクリプト: 主要なMarkdownファイル生成ロジックを担います。
    -   Jekyll: (間接的に) 生成されたMarkdownを元にGitHub Pagesの静的サイトをビルドします。
- 言語機能:
    -   Python: オブジェクト指向プログラミング、標準ライブラリ、コマンドライン引数処理など、Python言語の豊富な機能が活用されています。
- 自動化・CI/CD:
    -   GitHub Actions: `.github_automation` ディレクトリ内のスクリプト (`check_large_files.py` など) を通じて、自動化されたタスク（例：大容量ファイルチェック）を実行するために利用されます。
- 開発標準:
    -   `ruff`: コードスタイルの自動修正、統一されたコーディング規約の強制、コード品質の維持に貢献します。

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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコードスタイルを維持するための設定ファイル。
-   `.github_automation/`: GitHub Actionsなどを用いた自動化スクリプトや設定を格納するディレクトリ。
    -   `.github_automation/check_large_files/README.md`: 大容量ファイルチェック機能の説明ドキュメント。
    -   `.github_automation/check_large_files/check-large-files.toml`: 大容量ファイルチェックの設定パラメータを定義するTOMLファイル。
    -   `.github_automation/check_large_files/scripts/check_large_files.py`: プロジェクト内の大容量ファイルを検出するためのPythonスクリプト。
-   `.gitignore`: Gitによってバージョン管理対象から除外するファイルやディレクトリのパターンを定義するファイル。
-   `LICENSE`: 本プロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイル。
-   `README.md`: プロジェクトの目的、機能、使用方法、セットアップ手順、開発者向けヒントなどを記述した主要なドキュメント。
-   `_config.yml`: Jekyllサイトのグローバル設定を定義するファイル。GitHub Pagesサイトの動作に影響を与えます。
-   `assets/`: サイトで使用される静的アセット（画像など）を格納するディレクトリ。
    -   `assets/favicon-16x16.png`, `assets/favicon-192x192.png`, `assets/favicon-32x32.png`, `assets/favicon-512x512.png`: 異なるサイズで提供されるサイトのファビコン画像ファイル。
-   `debug_project_overview.py`: `project_overview_fetcher.py` の機能を独立してテスト・デバッグするためのスクリプト。
-   `generated-docs/`: 各リポジトリから自動取得された `project-overview.md` ファイルが配置されることが想定されるディレクトリ（またはそのプレースホルダー）。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
-   `index.md`: GitHub PagesサイトのトップページとなるMarkdownファイル。`generate_repo_list.py` によって生成されたリポジトリ一覧が出力されます。
-   `issue-notes/`: 開発中の課題や特定のイシューに関するメモを格納するディレクトリ。
    -   `issue-notes/22.md`: 特定のイシュー（ID 22）に関する詳細なメモや情報。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるWebアプリマニフェストファイル。
-   `pytest.ini`: Pythonのテストフレームワークである`pytest`の設定を定義するファイル。
-   `requirements-dev.txt`: 開発環境でのみ必要となるPythonパッケージの依存関係をリストアップするファイル。
-   `requirements.txt`: 本番環境で必要なPythonパッケージの依存関係をリストアップするファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイル。
-   `ruff.toml`: Pythonのコードリンター/フォーマッターである`ruff`の設定を定義するファイル。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   `src/__init__.py`: `src` ディレクトリがPythonパッケージであることを示すファイル。
    -   `src/generate_repo_list/`: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        -   `src/generate_repo_list/__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイル。
        -   `src/generate_repo_list/badge_generator.py`: リポジトリのステータスや情報を示すバッジ（例: Shields.io）を生成するロジックを管理するスクリプト。
        -   `src/generate_repo_list/config.yml`: プロジェクト概要取得機能など、アプリケーション固有の技術的パラメータを定義する設定ファイル。
        -   `src/generate_repo_list/config_manager.py`: `config.yml` や `strings.yml` などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するスクリプト。
        -   `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を特定のフォーマットで表示するためのユーティリティ関数を定義するスクリプト。
        -   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する主要な処理を実行します。
        -   `src/generate_repo_list/json_ld_template.json`: SEO強化のために、リポジトリ情報をJSON-LD形式で構造化するためのテンプレートファイル。
        -   `src/generate_repo_list/language_info.py`: リポジトリの主要言語や言語の使用割合に関する情報を処理・整形するロジックを格納するスクリプト。
        -   `src/generate_repo_list/markdown_generator.py`: 最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを管理するスクリプト。
        -   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得するスクリプト。
        -   `src/generate_repo_list/readme_badge_extractor.py`: リポジトリの `README.md` ファイルから特定のバッジ情報（例: ビルドステータス）を抽出するロジックを管理するスクリプト。
        -   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報を抽出し、整形されたデータ構造に変換するスクリプト。
        -   `src/generate_repo_list/seo_template.yml`: 検索エンジン最適化に関連するテンプレート設定やメタデータを定義するYAMLファイル。
        -   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するロジックを管理するスクリプト。
        -   `src/generate_repo_list/strings.yml`: アプリケーションのUIに表示される様々なメッセージや文言を国際化・一元管理するための設定ファイル。
        -   `src/generate_repo_list/template_processor.py`: Markdown生成の際に使用されるテンプレート（文字列フォーマットなど）を処理する汎用的なユーティリティスクリプト。
        -   `src/generate_repo_list/url_utils.py`: URLの構築、解析、検証など、URL関連のユーティリティ関数を定義するスクリプト。
-   `test_project_overview.py`: `project_overview_fetcher.py` の機能に対する単体テストスクリプト。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリ。
    -   `tests/conftest.py`: `pytest` で共有されるフィクスチャやヘルパー関数を定義するファイル。
    -   `tests/test_badge_generator_integration.py`: `badge_generator.py` の結合テスト。
    -   `tests/test_check_large_files.py`: `.github_automation/check_large_files/scripts/check_large_files.py` のテスト。
    -   `tests/test_config.py`: 設定ファイルの読み込みや管理に関するテスト。
    -   `tests/test_date_formatter.py`: `date_formatter.py` のテスト。
    -   `tests/test_environment.py`: 実行環境のセットアップや依存関係に関するテスト。
    -   `tests/test_integration.py`: プロジェクトの主要な機能フロー全体をカバーする結合テスト。
    -   `tests/test_markdown_generator.py`: `markdown_generator.py` のテスト。
    -   `tests/test_project_overview_fetcher.py`: `project_overview_fetcher.py` のテスト。
    -   `tests/test_readme_badge_extractor.py`: `readme_badge_extractor.py` のテスト。
    -   `tests/test_repository_processor.py`: `repository_processor.py` のテスト。

## 関数詳細説明
提供された情報では個々の関数のシグネチャ（引数、戻り値）は具体的に検出されませんでしたが、ファイル名とプロジェクトの目的から主要な機能を提供する関数について以下のように推測されます。

-   **`src/generate_repo_list/generate_repo_list.py` 内の主要関数**:
    -   **役割**: プログラムのエントリポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、処理、最終的なMarkdown生成までのワークフロー全体を指揮します。
    -   **引数**: `None` (または内部で `sys.argv` を直接処理)。
    -   **戻り値**: `None` (サイドエフェクトとしてファイル出力)。
    -   **機能**: GitHubユーザー名、出力ファイル名、処理リミットなどの引数を処理し、リポジトリ情報の取得、整形、Markdown形式での出力という一連の処理を実行します。

-   **`src/generate_repo_list/config_manager.py` 内の主要関数**:
    -   **役割**: 指定されたYAML設定ファイルを読み込み、設定データを辞書形式で提供します。
    -   **引数**: `file_path` (str): 読み込む設定ファイルのパス。
    -   **戻り値**: `dict`: 読み込まれた設定データ。
    -   **機能**: YAMLファイルをパースし、アプリケーション全体で使用される設定パラメータ（例: APIキー、タイムアウト設定）を供給します。

-   **`src/generate_repo_list/repository_processor.py` 内の主要関数**:
    -   **役割**: GitHub APIから取得した個々の生のリポジトリデータ（JSON形式）を整形し、アプリケーションで利用しやすい構造に変換します。
    -   **引数**: `repo_json` (dict): GitHub APIからの生のリポジトリデータ。`config` (dict): プロジェクト設定。
    -   **戻り値**: `dict`: 整形されたリポジトリデータ。
    -   **機能**: リポジトリ名、説明、URL、スター数、言語、最終更新日などの情報を抽出し、必要な追加処理（例：プロジェクト概要の取得）を調整します。

-   **`src/generate_repo_list/project_overview_fetcher.py` 内の主要関数**:
    -   **役割**: 特定のリポジトリURLから `generated-docs/project-overview.md` ファイルの内容を取得し、その中からプロジェクト概要の3行説明を抽出します。
    -   **引数**: `repo_url` (str): 対象リポジトリのURL。`config` (dict): プロジェクト設定。
    -   **戻り値**: `str`: 抽出された3行のプロジェクト概要。取得できなかった場合は空文字列など。
    -   **機能**: HTTPリクエストを送信してMarkdownファイルをフェッチし、正規表現や文字列操作を用いて指定されたセクション（例: `## プロジェクト概要`）から概要テキストをパースします。

-   **`src/generate_repo_list/markdown_generator.py` 内の主要関数**:
    -   **役割**: 処理済みのリポジトリデータリストを受け取り、GitHub Pages向けの整形されたMarkdown文字列を生成します。
    -   **引数**: `repositories` (list[dict]): 整形済みリポジトリデータのリスト。`strings_config` (dict): 表示文言の設定。`seo_config` (dict): SEO関連の設定。
    -   **戻り値**: `str`: 生成されたMarkdownコンテンツ。
    -   **機能**: 各リポジトリの情報を適切なMarkdown形式（タイトル、説明、バッジ、リンク、カテゴリ分けなど）で組み立て、最終的な出力ファイルの内容を作成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は提供された情報から分析できませんでした。

---
Generated at: 2026-04-25 07:18:25 JST
