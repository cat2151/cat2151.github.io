Last updated: 2025-11-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定したユーザーのリポジトリ情報を取得します。
- 取得した情報に基づき、JekyllベースのGitHub Pagesサイト向けにリポジトリ一覧のMarkdownファイルを自動生成します。
- 生成されたページは検索エンジンやLLMによる参照を最適化し、リポジトリの可視性向上と情報アクセスを促進します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesで動作する静的サイトジェネレータ。生成されたMarkdownファイルをHTMLに変換し、サイトを構築します)、**Markdown** (リポジトリ一覧コンテンツの記述形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (リポジトリ情報取得およびMarkdown生成スクリプトの主要言語・実行環境)、**GitHub API** (リポジトリ情報をプログラムから取得するためのインタフェース)
- テスト: **pytest** (Pythonプロジェクトのテストフレームワーク。単体テストや結合テストを実行し、コードの品質を保証します)
- ビルドツール: **pip** (Pythonパッケージ管理ツール。プロジェクトの依存関係をインストールします)、**Pythonスクリプト** (リポジトリ情報収集からMarkdownファイル生成までの一連の処理を自動化します)
- 言語機能: **Python** (バージョン3.x。標準ライブラリおよび`requirements.txt`で指定された各種サードパーティライブラリを利用して機能を実現しています)
- 自動化・CI/CD: **GitHub Pages** (生成された静的サイトをホスティングし、公開するサービス。デプロイの自動化に寄与します)、**Pythonスクリプト** (コンテンツ生成プロセスそのものを自動化するスクリプト)
- 開発標準: **ruff** (Pythonコードの高速リンターおよびフォーマッタ。コードスタイルの一貫性を保ち、潜在的なエラーを検出します)、**.editorconfig** (異なるエディタやIDE間でコードスタイルを統一するための設定ファイル)

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
- **.editorconfig**: 異なるIDEやエディタ間で、インデントスタイル、文字コードなどのコードフォーマットを統一するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: 本プロジェクトがMITライセンスの下で公開されていることを示すライセンス条項が記述されています。
- **README.md**: プロジェクトの概要、目的、機能、使用方法、開発者向けのヒントなどが記載された、プロジェクトの顔となるドキュメントです。
- **_config.yml**: Jekyllサイト全体の基本的な設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが含まれます。
- **assets/**: Webサイトで使用される画像やアイコンなどの静的ファイルを格納するディレクトリです。
    - **favicon-*.png**: サイトのブラウザタブやブックマークアイコンとして表示されるファビコン画像ファイルです。様々なサイズが用意されています。
- **debug_project_overview.py**: `project_overview_fetcher.py`モジュールが意図通りに機能するかを個別にテスト・デバッグするための補助スクリプトです。
- **generated-docs/**: スクリプトによって生成されたMarkdownファイルやその他のドキュメントが出力される予定のディレクトリです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される主要なMarkdownファイルです。GitHub Pagesのトップページとして、リポジトリの一覧が表示されます。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを個別のMarkdownファイルとして記録したディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるWebアプリマニフェストファイルです。アプリの表示名、アイコン、テーマカラーなどを定義します。
- **pytest.ini**: `pytest`テストフレームワークの設定ファイルです。テストの検出ルールやオプションなどを指定します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonライブラリの一覧が記載されています。
- **requirements.txt**: 本番環境でスクリプトを実行する際に必要となるPythonライブラリの一覧が記載されています。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどのページをクロールしてよいか、またはしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
- **src/**: プロジェクトのソースコードが格納されているルートディレクトリです。
    - **generate_repo_list/**: リポジトリ一覧を生成するための主要なPythonモジュール群を格納するパッケージです。
        - **badge_generator.py**: リポジトリのプロパティ（例: アクティブ、アーカイブ）に基づいて、表示されるバッジ（アイコンなど）のURLやテキストを生成するロジックを扱います。
        - **config.yml**: リポジトリ一覧生成スクリプトの実行に関する設定パラメータ（例: プロジェクト概要取得のON/OFF、対象ファイル名、APIタイムアウトなど）を定義するYAML形式のファイルです。
        - **config_manager.py**: `config.yml`やその他の設定ファイル（例: `secrets.toml`）を読み込み、アプリケーション全体で利用可能な形で管理する機能を提供します。
        - **generate_repo_list.py**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、それを処理し、最終的に`index.md`などのMarkdownファイルを生成する一連の処理を調整します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために利用されるJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: リポジトリが使用しているプログラミング言語に関する情報を処理し、表示に適した形式に変換する機能を提供します。
        - **markdown_generator.py**: 取得・処理されたリポジトリ情報を受け取り、最終的なMarkdown形式のコンテンツを生成するコアロジックを実装しています。
        - **project_overview_fetcher.py**: 各GitHubリポジトリ内の`generated-docs/project-overview.md`ファイルから、プロジェクトの3行概要を抽出・取得する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した構造に整形・フィルタリング・集計する役割を担います。
        - **seo_template.yml**: SEO関連のメタ情報（タイトル、ディスクリプションなど）のテンプレートや設定を定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
        - **strings.yml**: 生成されるMarkdownやログメッセージなどで使用される固定の文字列や文言を管理するためのYAMLファイルです。国際化対応に利用できます。
        - **template_processor.py**: Markdown生成の際に使用されるテンプレートファイル（例: ヘッダー、フッター、各リポジトリの表示ブロックなど）を読み込み、動的なデータを埋め込む機能を提供します。
        - **url_utils.py**: URLの生成、解析、検証など、URL操作に関連する汎用的なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能に関する単体テストを記述したファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **test_config.py**: `config_manager.py`やその他の設定ファイルの読み込み、パースに関するテストです。
    - **test_environment.py**: 実行環境（例: 環境変数の設定、必要なツールの存在）が正しく構成されているかを確認するテストです。
    - **test_integration.py**: 複数のモジュールが連携して正しく機能するかを確認する結合テストです。
    - **test_markdown_generator.py**: `markdown_generator.py`が期待通りのMarkdownコンテンツを生成するかを確認するテストです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`が正確にプロジェクト概要を抽出できるかを検証するテストです。
    - **test_repository_processor.py**: `repository_processor.py`がGitHub APIデータを適切に処理・変換できるかを検証するテストです。

## 関数詳細説明
このプロジェクトでは、主に`src/generate_repo_list/generate_repo_list.py`が全体の処理を制御し、他のモジュールの関数を呼び出して機能を実現しています。

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main()`**:
        - **役割**: プログラムのエントリポイント。コマンドライン引数の解析から、リポジトリ情報の取得、処理、最終的なMarkdownファイルの生成までの一連の流れをオーケストレーションします。
        - **引数**: なし（コマンドライン引数を内部で解析）。
        - **戻り値**: なし。処理の成功または失敗を示すステータスコードで終了します。
        - **機能**: 引数解析、GitHub APIからのリポジトリ取得、取得データの前処理、Markdownコンテンツ生成、ファイル書き出し。
    - **`parse_arguments()`**:
        - **役割**: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、スクリプト実行に必要なパラメータを取得します。
        - **引数**: なし。
        - **戻り値**: `argparse.Namespace`オブジェクト。解析された引数が含まれます。
        - **機能**: `argparse`モジュールを使用して、引数の定義と解析を行います。
- **`src/generate_repo_list/repository_processor.py`**
    - **`process_repository_data(repo_data)`**:
        - **役割**: GitHub APIから取得した個々の生のリポジトリデータ（辞書形式）を受け取り、Markdown生成に適した形式に整形・必要な情報を抽出します。
        - **引数**: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
        - **戻り値**: `dict`: 整形されたリポジトリ情報（名前、説明、URL、言語、スター数など）。
        - **機能**: 不要な情報の除去、データ型変換、URL生成、関連するサブモジュール（例: `language_info.py`）の呼び出し。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_name, owner, config)`**:
        - **役割**: 指定されたリポジトリの`generated-docs/project-overview.md`ファイルを読み込み、その中の「プロジェクト概要」セクションから3行の要約を抽出します。
        - **引数**: `repo_name` (str): リポジトリ名、`owner` (str): リポジトリの所有者、`config` (dict): 設定情報（ターゲットファイル名、セクションタイトルなど）。
        - **戻り値**: `list[str]`または`None`: 抽出された3行の概要リスト、またはファイルが見つからない、セクションがない場合は`None`。
        - **機能**: GitHub APIまたはキャッシュを介して指定ファイルの内容を取得し、Markdownを解析して特定セクションの箇条書きを抽出します。
- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_repo_list_markdown(processed_repos, config)`**:
        - **役割**: `repository_processor.py`によって処理されたリポジトリ情報のリストを受け取り、全体のリポジトリ一覧を含むMarkdownコンテンツを生成します。
        - **引数**: `processed_repos` (list): 整形されたリポジトリ情報のリスト、`config` (dict): 設定情報。
        - **戻り値**: `str`: 生成されたMarkdown形式の文字列。
        - **機能**: ヘッダー、各リポジトリのセクション、フッターなどを`template_processor.py`を用いて組み合わせて最終的なMarkdownを作成します。
    - **`generate_repo_section(repo_info, config)`**:
        - **役割**: 個々のリポジトリ情報に基づいて、そのリポジトリ専用のMarkdownブロックを生成します。
        - **引数**: `repo_info` (dict): 単一の整形されたリポジトリ情報、`config` (dict): 設定情報。
        - **戻り値**: `str`: 個々のリポジトリに関するMarkdown文字列。
        - **機能**: リポジトリ名、説明、言語、スター数、プロジェクト概要などをテンプレートに埋め込みます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-22 07:06:05 JST
