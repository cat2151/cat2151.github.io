Last updated: 2025-11-21

# Project Overview

## プロジェクト概要
- GitHub Pages用のリポジトリ一覧を自動生成し、WebサイトのSEOとLLMによる参照性を向上させるシステムです。
- GitHub APIからリポジトリ情報を取得し、各リポジトリの魅力的な概要を含むMarkdownファイルを自動生成します。
- プロジェクト概要の自動取得、バッジ表示、アクティブ・アーカイブ・フォーク分類など多彩な機能を備えています。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll) - 静的サイトホスティングサービスJekyllベースで、リポジトリ一覧サイトを構築します。Markdown - 生成されるリポジトリ一覧のフォーマットであり、読みやすく構造化されたコンテンツを提供します。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python - プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成ロジックを実装しています。GitHub API - GitHubのリポジトリ情報をプログラムから取得するために使用されます。YAML - 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に用いられ、設定の管理を容易にします。
- テスト: pytest - Pythonコードのユニットテストおよび統合テストフレームワークとして、コードの品質と信頼性を保証します。
- ビルドツール: Python (スクリプト) - プロジェクトのPythonスクリプト自体が、リポジトリ情報を処理し、最終的なMarkdownファイルを生成するビルドプロセスを担います。
- 言語機能: Python - プロジェクト全体のロジックがPythonで記述されており、その豊富なライブラリとエコシステムを活用しています。
- 自動化・CI/CD: GitHub Pages - 生成されたコンテンツをホストするプラットフォームであり、変更があった際に自動でデプロイされる仕組みと連携可能です。
- 開発標準: ruff - Pythonコードのフォーマッター兼リンターとして、コードスタイルを自動修正し、一貫性を保ちます。`.editorconfig` - 異なるエディタやIDE間でコードの書式設定を一貫させるための設定ファイルです。

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
- **`.editorconfig`**: 複数の開発者やエディタ間でコードの書式設定（インデントサイズ、空白の扱いなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです（例：一時ファイル、ビルド成果物、開発環境固有の設定ファイルなど）。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルで、このプロジェクトの利用条件を示します。
- **`README.md`**: プロジェクトの概要、目的、機能、セットアップ方法、基本的な使用方法などを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン設定などが含まれます。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのアイコン（ファビコン）の各種サイズが格納されています。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能の動作を個別にデバッグするためのスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されたドキュメント（このプロジェクトではMarkdownファイル）を格納するためのプレースホルダーディレクトリです。
- **`index.md`**: メインのリポジトリ一覧が生成され出力されるMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: プロジェクトの課題や検討事項をメモとして格納するためのMarkdownファイル群です。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるWebアプリマニフェストファイルで、アプリの表示方法や動作を定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルで、テストの実行オプションや挙動を定義します。
- **`requirements-dev.txt`**: 開発およびテストに必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターである`ruff`の設定ファイルで、コードの品質とスタイルを維持するためのルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`generate_repo_list/`**: リポジトリ一覧生成ロジックが格納されたPythonパッケージです。
        - **`__init__.py`**: Pythonパッケージとして認識させるための初期化ファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックが含まれます。
        - **`config.yml`**: プロジェクトの実行時設定（GitHubトークン、プロジェクト概要取得設定など）を定義するファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのユーティリティが含まれます。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインのエントリーポイントスクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・整理するロジックが含まれます。
        - **`markdown_generator.py`**: GitHub APIから取得した情報をもとに、リポジトリ一覧のMarkdownコンテンツを生成するロジックが含まれます。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要テキストを自動的に取得する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換するロジックが含まれます。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリの各種統計情報（スター数、フォーク数、最終更新日など）を計算するロジックが含まれます。
        - **`strings.yml`**: 生成されるMarkdownやUIに表示される様々なテキストメッセージや文言を一元的に管理するファイルです。
        - **`template_processor.py`**: 汎用的なテンプレート処理（Jinja2など）を用いて、動的にコンテンツを生成するロジックが含まれます。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数が含まれます。
- **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込み・管理に関するテストが含まれます。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストが含まれます。
    - **`test_integration.py`**: 複数のコンポーネントが連携して動作する際の統合テストが含まれます。
    - **`test_markdown_generator.py`**: Markdownコンテンツ生成ロジックに関するテストが含まれます。
    - **`test_project_overview_fetcher.py`**: 各リポジトリからプロジェクト概要を取得する機能に関するテストが含まれます。
    - **`test_repository_processor.py`**: リポジトリ情報の処理ロジックに関するテストが含まれます。

## 関数詳細説明
- **`generate_repo_list.py`内の主要関数 (例: `main`)**:
    - **役割**: プロジェクトのメインエントリポイントであり、リポジトリ情報の取得からMarkdownファイル生成までの一連の処理を統括します。
    - **引数**:
        - `username` (str): GitHubユーザー名。
        - `output` (str): 生成されたMarkdownの出力ファイル名。
        - `limit` (int, optional): 処理するリポジトリ数の上限（開発用）。
    - **戻り値**: なし。指定されたパスにMarkdownファイルを生成します。
    - **機能**: GitHub APIから指定されたユーザーのリポジトリ情報を取得し、取得した情報を処理・整形した上で、Markdown形式のリポジトリ一覧ファイルを作成します。
- **`badge_generator.py`内の主要関数 (例: `generate_badge_markdown`)**:
    - **役割**: 特定のリポジトリや言語に対するバッジ（例: 使用言語、ステータス）のMarkdown形式を生成します。
    - **引数**:
        - `repo_info` (dict): 処理対象のリポジトリ情報。
        - `badge_type` (str): 生成するバッジの種類（例: 'language', 'status'）。
    - **戻り値**: (str) 生成されたバッジのMarkdown文字列。
    - **機能**: リポジトリ情報に基づき、適切なバッジのURLと表示テキストを構成し、Markdown形式で出力します。
- **`config_manager.py`内の主要関数 (例: `load_config`)**:
    - **役割**: YAML形式の設定ファイルを読み込み、Pythonオブジェクトとして提供します。
    - **引数**:
        - `file_path` (str): 設定ファイルのパス。
    - **戻り値**: (dict) 読み込まれた設定内容を含む辞書。
    - **機能**: 指定されたパスからYAMLファイルを解析し、設定情報をアプリケーション全体で利用可能な形式で提供します。
- **`markdown_generator.py`内の主要関数 (例: `generate_repository_list_markdown`)**:
    - **役割**: 処理済みのリポジトリデータを受け取り、SEOを考慮したリポジトリ一覧のMarkdownコンテンツを生成します。
    - **引数**:
        - `repositories` (list): 処理済みのリポジトリ情報のリスト。
        - `seo_data` (dict): SEO関連のメタデータ。
    - **戻り値**: (str) 生成されたリポジトリ一覧のMarkdown文字列。
    - **機能**: リポジトリごとに詳細情報を整理し、タイトル、説明、リンク、バッジなどを含む構造化されたMarkdownを組み立てます。
- **`project_overview_fetcher.py`内の主要関数 (例: `fetch_project_overview_from_repo`)**:
    - **役割**: 指定されたGitHubリポジトリ内の特定のファイルから、プロジェクト概要の3行説明を抽出します。
    - **引数**:
        - `repo_owner` (str): リポジトリの所有者。
        - `repo_name` (str): リポジトリ名。
        - `config` (dict): プロジェクト概要取得に関する設定（ファイルパス、セクションタイトルなど）。
    - **戻り値**: (list of str or None) 抽出された3行の説明のリスト、または取得できなかった場合はNone。
    - **機能**: GitHub APIを介してリポジトリ内のファイルコンテンツを読み込み、設定に基づいて「プロジェクト概要」セクションから指定された行数を抽出します。
- **`repository_processor.py`内の主要関数 (例: `process_repositories`)**:
    - **役割**: GitHub APIから取得した生のリポジトリデータに対して、必要な情報の抽出、整形、フィルタリングなどの処理を行います。
    - **引数**:
        - `raw_repositories` (list): GitHub APIから直接取得したリポジトリデータのリスト。
        - `config` (dict): 処理に関する設定。
    - **戻り値**: (list) 処理され、表示準備が整ったリポジトリ情報のリスト。
    - **機能**: 各リポジトリの言語情報、スター数、最終更新日などのデータを整理し、必要に応じて分類（アクティブ、アーカイブ、フォークなど）を行います。
- **`statistics_calculator.py`内の主要関数 (例: `calculate_repo_statistics`)**:
    - **役割**: 個々のリポジトリから各種統計情報（例: コミット数、貢献者数、コード行数など）を計算します。
    - **引数**:
        - `repo_info` (dict): 特定のリポジトリのデータ。
    - **戻り値**: (dict) 計算された統計情報。
    - **機能**: リポジトリの活動や規模を示す数値データを集計し、概要表示に役立てます。
- **`template_processor.py`内の主要関数 (例: `render_template`)**:
    - **役割**: テンプレートファイル（例: Jinja2テンプレート）とデータを使用して、最終的なテキストコンテンツを生成します。
    - **引数**:
        - `template_path` (str): テンプレートファイルのパス。
        - `data` (dict): テンプレートに埋め込むデータ。
    - **戻り値**: (str) レンダリングされたテキストコンテンツ。
    - **機能**: 定義されたテンプレートに動的な情報を流し込み、マークダウンやJSON-LDなどの最終出力を生成します。
- **`url_utils.py`内の主要関数 (例: `build_github_api_url`)**:
    - **役割**: GitHub APIのURLを構築したり、URLから情報を抽出したりするユーティリティ機能を提供します。
    - **引数**:
        - `endpoint` (str): APIエンドポイント（例: 'repos/{owner}/{repo}'）。
        - `params` (dict, optional): クエリパラメータ。
    - **戻り値**: (str) 構築された完全なURL。
    - **機能**: GitHub APIへの正確なリクエストURLを組み立て、外部リソースへのアクセスを容易にします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-21 07:06:24 JST
