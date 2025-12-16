Last updated: 2025-12-17

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、GitHub Pagesサイト用のリポジトリ一覧Markdownファイルを自動生成するシステムです。
- 生成されたページはSEOが最適化され、検索エンジンやLLMによるリポジトリ参照の改善に貢献します。
- 各リポジトリの概要を自動取得・表示することで、訪問者にプロジェクトの魅力的な情報を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的生成エンジン), GitHub Pages (生成コンテンツのホスティングサービス), Markdown (コンテンツ記述形式)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得)
- テスト: pytest (Pythonアプリケーションのテストフレームワーク)
- ビルドツール: なし (Pythonスクリプトが直接Markdownを生成するため、従来のビルドツールは使用していません)
- 言語機能: Python (スクリプトの記述と実行に使用)
- 自動化・CI/CD: なし (ローカルでの開発・実行を重視した構成です)
- 開発標準: Ruff (PythonコードのLinterおよびフォーマッター), .editorconfig (複数エディタ間でのコーディングスタイル統一)

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
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、ライセンス情報などを説明するメインのドキュメントファイルです。
- **_config.yml**: Jekyllサイトの全体的な設定（タイトル、テーマ、プラグインなど）を定義するファイルです。
- **assets/**: Webサイトで使用される静的なアセット（例: ファビコン画像）を格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 各種デバイスやブラウザで使用されるファビコン画像です。
- **debug_project_overview.py**: `project_overview_fetcher` 機能のデバッグや単体テストを目的としたスクリプトです。
- **generated-docs/**: 各リポジトリから取得した`project-overview.md`などの情報を格納する、または一時的に生成されたドキュメントを配置するディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイトの所有権確認に使用されるファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧のメインページとなるMarkdownファイルです。
- **issue-notes/**: プロジェクト開発中に発生した課題や検討事項、メモなどを記録したMarkdownファイルのコレクションです。
    - **10.md**, **12.md**, **14.md**, **2.md**, **4.md**, **6.md**, **8.md**: 個別の課題やメモを記述したファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）として動作するためのメタデータ（アプリ名、アイコン、表示モードなど）を定義するファイルです。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定（テストの検出方法、プラグインなど）を定義するファイルです。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、どのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **ruff.toml**: PythonコードのLinterおよびフォーマッターであるRuffの設定ファイルです。
- **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（画像）の生成ロジックを扱うモジュールです。
- **src/generate_repo_list/config.yml**: プロジェクト概要取得機能など、スクリプトの技術的なパラメータを設定するYAMLファイルです。
- **src/generate_repo_list/config_manager.py**: YAMLファイルなどの設定ファイルを読み込み、管理するためのユーティリティモジュールです。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、その情報に基づいてMarkdownファイルを生成する、このプロジェクトのメインスクリプトです。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のために使用される、JSON-LD形式の構造化データテンプレートです。
- **src/generate_repo_list/language_info.py**: GitHubリポジトリの言語情報を分析・整形するためのロジックを含むモジュールです。
- **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックをカプセル化したモジュールです。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の`generated-docs/project-overview.md`ファイルから、プロジェクト概要（3行説明）を抽出する機能を担当するモジュールです。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するためのモジュールです。
- **src/generate_repo_list/seo_template.yml**: ページタイトルやメタディスクリプションなど、SEOに関連する情報のテンプレートや設定を定義するYAMLファイルです。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュールです。
- **src/generate_repo_list/strings.yml**: UIメッセージ、キャプション、ラベルなど、表示されるテキストを集中管理するためのYAMLファイルです。
- **src/generate_repo_list/template_processor.py**: Markdown生成に使用するテンプレート（例: Jinja2など）を処理し、データと結合して最終出力を生成するモジュールです。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URL関連の汎用的なユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
- **tests/**: pytestを使用して書かれたテストファイルを格納するディレクトリです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを記述したファイルです。
    - **test_integration.py**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを確認する統合テストファイルです。
    - **test_markdown_generator.py**: Markdownコンテンツの生成ロジックが正しく機能するかをテストするファイルです。
    - **test_project_overview_fetcher.py**: 各リポジトリからのプロジェクト概要の取得機能に関するテストファイルです。
    - **test_repository_processor.py**: GitHub APIから取得したリポジトリデータの処理ロジックに関するテストファイルです。

## 関数詳細説明
提供された情報からは具体的な関数リストが与えられていないため、各関数の役割、引数、戻り値、機能を詳細に説明することはできませんでした。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-17 07:06:16 JST
