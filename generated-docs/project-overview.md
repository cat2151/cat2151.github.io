Last updated: 2025-12-10

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を取得するシステムです。
- 取得した情報から、GitHub Pages向けのSEO最適化されたリポジトリ一覧を自動生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照失敗の課題を緩和することを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレータとしてコンテンツを公開するために利用されます。Markdown - プロジェクト情報を記述し、ウェブページとして表示するための軽量マークアップ言語です。
- 音楽・オーディオ: (該当なし)
- 開発ツール: pytest - Pythonアプリケーションのテストを効率的に行うためのフレームワークです。ruff - Pythonコードのスタイルチェック（リンター）と自動フォーマットを行うツールで、コード品質と一貫性を保ちます。
- テスト: pytest - Pythonアプリケーションの単体テスト、結合テスト、統合テストを実行するためのフレームワークです。
- ビルドツール: Pythonスクリプト (`generate_repo_list.py`) - GitHub APIからのデータ取得、リポジトリ情報の処理、最終的なMarkdownファイルの生成といった主要なロジックを担います。
- 言語機能: Python - プロジェクトの主要な開発言語として、データ処理、API連携、ファイル生成ロジックの実装に利用されています。
- 自動化・CI/CD: GitHub Actions - プロジェクト自体には含まれていませんが、生成されたGitHub Pagesサイトのデプロイや、このスクリプトの実行を自動化するために利用されることが想定されます。
- 開発標準: ruff - Pythonコードのスタイルガイド（例: PEP 8）への準拠を強制し、コードの一貫性と可読性を向上させるためのツールです。

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
- **.editorconfig**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルの一貫性を維持するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。一時ファイル、ログ、依存関係などが含まれます。
- **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイル。
- **README.md**: プロジェクトの概要、目的、機能、セットアップ方法、使い方、コマンド例などが記述された主要なドキュメントファイル。
- **_config.yml**: Jekyll（GitHub Pagesの基盤）サイト全体の構成設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **assets/**: GitHub Pagesサイトで利用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各サイズ画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能のテストやデバッグを行うためのスクリプト。
- **generated-docs/**: 各リポジトリの特定のファイル（例: `project-overview.md`）が存在すると想定されるディレクトリ。このプロジェクト自体が生成するのではなく、他のリポジトリが持つパスを指します。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブサイト所有権確認プロセスで使用される、特定の文字列を含むHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧が表示されるGitHub Pagesサイトのトップページコンテンツ（Markdown形式）。
- **issue-notes/**: GitHub Issuesに関連する開発メモや検討事項をMarkdown形式で記録するディレクトリ。
    - **[番号].md**: 個別のIssueに関する詳細なメモや議論が記述されたMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するファイル。ウェブアプリの名前、アイコン、表示モードなどを指定し、ユーザーがアプリをホーム画面に追加できるようにします。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイル。テストの実行オプションや、検出対象となるファイルパターンなどを指定します。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonライブラリの依存関係をリストするファイル。`pytest`や`ruff`などが含まれます。
- **requirements.txt**: 本番環境でこのプロジェクトを実行するために最低限必要なPythonライブラリの依存関係をリストするファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、またはしてはいけないかを指示するファイル。SEO対策の一環として利用されます。
- **ruff.toml**: Pythonのリンター兼フォーマッターである`ruff`の設定ファイル。コードスタイルルール、無視するエラー、フォーマット設定などを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **generate_repo_list/**: リポジトリ一覧を生成するためのPythonモジュール群をまとめたパッケージ。
        - **badge_generator.py**: リポジトリの特性（アーカイブ、言語など）を示すバッジのMarkdownを生成するロジックを含むファイル。
        - **config.yml**: プロジェクト概要取得機能など、スクリプトの動作を制御する技術的パラメータが記述されたYAML設定ファイル。
        - **config_manager.py**: YAMLファイルから設定を安全に読み込み、アクセスするためのユーティリティ関数を提供するファイル。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownを生成するメインの実行スクリプト。コマンドライン引数を解析し、他のモジュールを連携させます。
        - **json_ld_template.json**: SEO強化のために利用されるJSON-LD形式の構造化データテンプレート。検索エンジンにコンテンツの意味をより正確に伝えます。
        - **language_info.py**: GitHub APIから取得したリポジトリの言語情報を処理し、表示に適した形式に整形するロジックを含むファイル。
        - **markdown_generator.py**: 処理済みのリポジトリデータを受け取り、最終的なMarkdown形式の出力コンテンツを生成するロジックを含むファイル。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出するロジックを含むファイル。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、Markdown生成に適した内部データ構造に加工・整形するロジックを含むファイル。
        - **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・取得するロジックを含むファイル。
        - **strings.yml**: UIに表示される各種メッセージや文言を一元的に管理するYAMLファイル。多言語対応や文言の変更が容易になります。
        - **template_processor.py**: Markdown生成時に使用されるテンプレート（文字列）を処理し、動的なデータを埋め込むロジックを含むファイル。
        - **url_utils.py**: URLの検証、構築、エンコードなどのURL関連ユーティリティ関数を提供するファイル。
- **test_project_overview.py**: `project_overview_fetcher.py`の機能（プロジェクト概要の取得と解析）を検証するためのテストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトが格納されるディレクトリ。
    - **test_config.py**: 設定ファイルの読み込みや管理 (`config_manager.py`) が正しく機能するかを検証するテストスクリプト。
    - **test_environment.py**: プロジェクトの実行環境（依存関係、設定など）が正しくセットアップされているかを検証するテストスクリプト。
    - **test_integration.py**: 複数のモジュールが連携して全体として正しく動作するかを検証する統合テストスクリプト。
    - **test_markdown_generator.py**: Markdown生成ロジック (`markdown_generator.py`) が期待通りの出力を生成するかを検証するテストスクリプト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`モジュールのテスト。
    - **test_repository_processor.py**: リポジトリ情報の処理 (`repository_processor.py`) が正しく行われるかを検証するテストスクリプト。

## 関数詳細説明
- **`generate_repo_list.py`**
    - `main()`: プログラムのエントリーポイント。コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ情報取得、情報の処理、Markdown生成といった一連の処理を統括します。
    - `parse_arguments()`: コマンドライン引数（ユーザー名、出力ファイル名、リポジトリ数制限など）を解析し、プログラムの動作に必要な設定値を取得します。
- **`config_manager.py`**
    - `load_config(file_path)`: 指定されたYAML形式の設定ファイル (`config.yml`, `strings.yml`など) を読み込み、Pythonの辞書オブジェクトとして返します。設定値へのアクセスを簡素化します。
- **`repository_processor.py`**
    - `fetch_repositories(username, token, limit=None)`: GitHub APIを使用して指定された`username`の公開リポジトリ一覧を取得します。必要に応じて`token`を使用し、`limit`で取得数を制限できます。
    - `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータ（JSON形式）を整形し、後続のMarkdown生成処理で使いやすいPythonオブジェクト（例: カスタムクラスや辞書）に変換します。
- **`project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリ名とオーナーに基づき、そのリポジトリ内の特定のパス（`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出して返します。GitHub APIを介してファイルを読み込みます。
- **`markdown_generator.py`**
    - `generate_markdown(repositories, seo_config, strings_config)`: 処理済みのリポジトリ情報のリスト、SEO設定、表示文言設定を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。Jekyllの構文やSEOメタデータも考慮されます。
- **`badge_generator.py`**
    - `create_badges(repo_status_data)`: リポジトリの状態（アーカイブ済み、フォーク、アクティブなど）や言語情報に基づいて、適切なバッジ（Shields.io形式など）のMarkdownコードを生成します。
- **`statistics_calculator.py`**
    - `calculate_stats(repo_data)`: 各リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または抽出し、リポジトリデータに追加します。
- **`language_info.py`**
    - `get_language_details(languages_url, top_n=3)`: GitHub APIから提供されるリポジトリの言語URLを使用して、使用されているプログラミング言語とその割合を取得し、表示に適した形式（例: 上位N言語）で返します。
- **`template_processor.py`**
    - `render_template(template_string, data)`: 指定されたテンプレート文字列とデータ辞書を使用して、プレースホルダーを実際の値で置き換え、レンダリングされた文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-10 07:06:23 JST
