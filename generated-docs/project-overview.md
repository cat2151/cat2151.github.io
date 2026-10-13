Last updated: 2026-10-14

# Project Overview

## プロジェクト概要
- GitHub APIを用いてリポジトリ情報を取得し、GitHub Pages用のMarkdownファイルを自動生成するシステムです。
- SEO最適化されたリポジトリ一覧を作成することで、検索エンジンやLLMによる参照性を向上させます。
- 各リポジトリの概要、バッジ、分類などを動的に生成し、サイトの効率的な更新を支援します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll) - 生成されたMarkdownファイルに基づいて静的サイトをホスト・構築します。生成物はMarkdown形式です。
- 音楽・オーディオ: 該当なし - このプロジェクトはオーディオ関連技術を使用していません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語として、GitHub APIからのデータ取得、処理、Markdown生成に利用されています。
    - Git: ソースコードのバージョン管理システム。
    - GitHub API: GitHubリポジトリの情報をプログラム的に取得するためのインターフェース。
- テスト: pytest - Pythonアプリケーションのテストフレームワークとして、コードの品質と正確性を保証するために使用されています。
- ビルドツール:
    - Markdown生成: このプロジェクト自体がMarkdownファイルを生成するツールです。
    - Jekyll: GitHub Pagesの基盤であり、生成されたMarkdownファイルを最終的なウェブサイトとして構築します。
- 言語機能: Python - コマンドライン引数パーシング (argparse)、YAML/JSONファイルの読み書き、文字列処理、HTTPリクエスト (requestsライブラリなど) などの言語機能を活用しています。
- 自動化・CI/CD:
    - GitHub Actions (間接的): このプロジェクトの実行を自動化するためのGitHubのCI/CDサービスとして言及されていますが、プロジェクト自体がCI/CDパイプラインを構築するわけではありません。
- 開発標準: ruff - Pythonコードのフォーマット、リンティング、スタイルチェックを自動化し、コード品質と一貫性を維持するために使用されています。

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
- **`.editorconfig`**: 複数のエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **`.github_automation/`**: GitHub関連の自動化スクリプトや設定を格納するディレクトリ。
    - **`check_large_files/`**:
        - **`README.md`**: `check_large_files` 機能に関する説明。
        - **`check-large-files.toml`**: Gitリポジトリ内の大容量ファイルをチェックするための設定ファイル。
        - **`scripts/check_large_files.py`**: Gitリポジトリをスキャンし、設定された閾値を超える大容量ファイルを検出するPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリ（例: ビルド成果物、ログファイル、一時ファイル）を指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）。
- **`README.md`**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、開発者向けのヒントなどを記述したメインドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各種サイズ画像。
- **`debug_project_overview.py`**: `project_overview_fetcher` モジュールのデバッグや単体テストを目的としたスクリプト。
- **`generated-docs/`**: 各リポジトリから自動取得されるプロジェクト概要などのドキュメントが格納されるパス。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト認証サービスで使用される所有権確認用のファイル。
- **`index.md`**: メインスクリプトによって生成されるMarkdownファイル。GitHub Pagesのルートページとして機能し、リポジトリ一覧が表示されます。
- **`issue-notes/`**: 開発中の特定の課題やメモを格納するディレクトリ。
    - **`22.md`**: 22番目の課題（Issue #22）に関する詳細なメモや解決策が記述されたMarkdownファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブサイトをユーザーのデバイスにインストールするためのメタデータを提供します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの発見ルール、マーカー、フィクスチャなどを定義します。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを記述したファイル。本番環境の依存関係とは別に管理されます。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、どの部分を避けるべきかを指示するファイル。
- **`ruff.toml`**: PythonのLinterおよびFormatterであるruffの設定ファイル。コーディング規約や自動修正ルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが配置されるディレクトリ。
    - **`__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能のコアロジックを格納するPythonパッケージ。
        - **`__init__.py`**: `generate_repo_list` パッケージとして認識させるためのファイル。
        - **`badge_generator.py`**: リポジトリの状態（アクティブ、アーカイブなど）や技術スタックを示すバッジを生成するロジックをカプセル化しています。
        - **`config.yml`**: プロジェクト概要取得機能の有効/無効、対象ファイル、タイムアウト時間などの技術的パラメータを設定するためのYAMLファイル。
        - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`、`strings.yml`など）を読み込み、管理するためのユーティリティモジュール。
        - **`date_formatter.py`**: リポジトリの更新日時などを人間が読みやすい形式に整形するための関数を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、その情報を基にMarkdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプト。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のためにウェブページに構造化データを埋め込むためのJSON-LD形式のテンプレートファイル。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語の情報を取得し、表示に利用するための処理ロジックを含みます。
        - **`markdown_generator.py`**: 取得・処理されたリポジトリデータをもとに、GitHub Pages向けのMarkdownコンテンツ（一覧、詳細など）を動的に生成するコアロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）からプロジェクトの概要説明を自動的に抽出し取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイル内に記述されている既存のバッジ（Shield.ioなど）情報を解析・抽出するためのモジュール。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を解析し、表示に必要な情報に整形・加工する主要な処理ロジック。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタ情報やサイト構造に関する設定を定義するYAMLテンプレート。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、一覧表示に利用するためのモジュール。
        - **`strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、カテゴリ名などのテキストコンテンツを一元的に管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jekyll Liquidシンタックスなど）を処理し、データと結合して最終的なコンテンツを生成するユーティリティ。
        - **`url_utils.py`**: URLの生成、検証、エンコード・デコードなど、URL操作に関連する汎用的なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールに特化した単体テストコード。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`conftest.py`**: pytestテスト実行時に使用される共通のフィクスチャや設定を定義するファイル。
    - **`test_badge_generator_integration.py`**: `badge_generator` モジュールが正しく機能するかを検証する統合テスト。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files.py` スクリプトの機能テスト。
    - **`test_config.py`**: `config_manager` モジュールが設定ファイルを正しく読み込み、処理するかを検証するテスト。
    - **`test_date_formatter.py`**: `date_formatter` モジュールの日付整形機能が期待通りに動作するかを検証するテスト。
    - **`test_environment.py`**: プロジェクトの実行環境や依存関係が正しくセットアップされているかを検証するテスト。
    - **`test_integration.py`**: `generate_repo_list` スクリプトの主要な処理フロー全体を検証する統合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator` モジュールが適切なMarkdown出力を生成するかを検証するテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールがプロジェクト概要を正しく抽出できるかを検証するテスト。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールがREADMEからバッジ情報を正確に抽出できるかを検証するテスト。
    - **`test_repository_processor.py`**: `repository_processor` モジュールがGitHub APIからのリポジトリデータを正しく整形できるかを検証するテスト。

## 関数詳細説明
提供された情報では、各関数の具体的な引数や戻り値は記載されていませんが、各モジュールが担う主要な機能から推測される関数について説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: このスクリプトのエントリーポイントとなる関数。GitHub APIからリポジトリ情報を取得し、`repository_processor`、`markdown_generator`などを呼び出してMarkdownファイルを生成する一連の処理をオーケストレーションします。
- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge_markdown(repo_data)`: リポジトリのプロパティ（アーカイブ状態、言語、スター数など）に基づき、Markdown形式のバッジ文字列を生成します。
- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(config_path)`: 指定されたYAML設定ファイルのパスを受け取り、その内容を辞書形式で読み込みます。
    - `load_strings(strings_path)`: 指定されたYAML文字列ファイルのパスを受け取り、その内容を辞書形式で読み込みます。
- **`src/generate_repo_list/date_formatter.py`**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式（例: "YYYY-MM-DD"）に整形して返します。
- **`src/generate_repo_list/language_info.py`**:
    - `get_top_languages(repo_languages_data)`: リポジトリの言語使用状況データを受け取り、主要な言語を抽出して返します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_repository_list_markdown(repositories_data, config, strings)`: 処理済みのリポジトリデータのリストと設定、文言データを受け取り、GitHub Pages用のリポジトリ一覧Markdownコンテンツ全体を生成します。
    - `generate_repository_card(repo_data, config, strings)`: 個々のリポジトリデータを受け取り、そのリポジトリの表示カード（タイトル、概要、バッジなど）に対応するMarkdownスニペットを生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリ名とオーナー情報、設定を受け取り、該当リポジトリからプロジェクト概要テキスト（例: `generated-docs/project-overview.md`内の3行説明）を抽出して返します。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
    - `extract_badges_from_readme(readme_content)`: リポジトリのREADMEファイルの内容を受け取り、その中からバッジ（Shield.ioなど）のURLや情報を抽出します。
- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repositories(username, token, config, limit=None)`: GitHubユーザー名、APIトークン、設定、および処理制限数を受け取り、GitHub APIからリポジトリ情報を取得し、整形・フィルタリングなどの前処理を行います。
    - `get_repo_data(repo, project_overview_fetcher, config)`: 個々のGitHubリポジトリオブジェクトとプロジェクト概要フェッチャー、設定を受け取り、表示に必要な形式に加工します。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - `calculate_stats(repo_data)`: リポジトリデータを受け取り、スター数やフォーク数などの統計情報を計算して返します。
- **`src/generate_repo_list/template_processor.py`**:
    - `render_template(template_string, data)`: Liquidなどのテンプレート文字列とレンダリング用のデータを受け取り、最終的な文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**:
    - `build_github_api_url(username)`: GitHub APIのエンドポイントURLを構築します。
    - `create_repo_url(owner, repo_name)`: リポジトリのGitHub.com上のURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-14 07:10:54 JST
