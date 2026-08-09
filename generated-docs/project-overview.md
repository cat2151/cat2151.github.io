Last updated: 2026-08-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト用のMarkdownファイルを生成します。
- これにより、リポジトリの検索エンジン最適化とLLMによる参照性向上を図ります。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式), HTML/CSS (Jekyllが生成するウェブページの構成要素)
- 音楽・オーディオ: なし (このプロジェクトでは音楽・オーディオ関連技術は使用されていません)
- 開発ツール: Git (バージョン管理), GitHub API (リポジトリ情報取得), Pytest (Pythonテストフレームワーク), Ruff (Pythonコードリンタ・フォーマッタ)
- テスト: Pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIクライアント、Markdown生成ロジックとして機能)
- 言語機能: Python (主要なプログラミング言語), YAML (設定ファイル管理), TOML (秘密情報や設定ファイル管理)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリでファイルサイズチェックなどの自動化を想定)
- 開発標準: Ruff (コードスタイルの一貫性を保つためのリンタ・フォーマッタ), EditorConfig (異なるエディタ間でのコーディングスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: GitHub Actionsなどの自動化環境で、リポジトリ内の大規模なファイルをチェックするためのツール群を格納しています。
    - **`README.md`**: `check_large_files`ツールの説明ドキュメントです。
    - **`check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイルで、チェック対象のファイルサイズ閾値などを定義します。
    - **`scripts/check_large_files.py`**: 実際の大規模ファイルチェックロジックを実装したPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを記述する設定ファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けのヒントなどを記述したメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの情報を設定します。
- **`assets/`**: Jekyllサイトで使用される画像、アイコン、フォントなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の様々なサイズを格納しています。
- **`debug_project_overview.py`**: `project_overview`機能の開発やテスト中に使用されるデバッグ用のスクリプトです。
- **`generated-docs/`**: `generate_repo_list.py`スクリプトによって生成されたMarkdownファイルなどを格納することを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために使用される認証ファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。`generate_repo_list.py`の出力先として指定されることが多いです。
- **`issue-notes/22.md`**: プロジェクトの特定の課題（例: issue #22）に関するメモや詳細を記述したファイルです。
- **`manifest.json`**: ウェブサイトをプログレッシブウェブアプリ（PWA）として動作させるための設定ファイルです。ホーム画面に追加されるアイコン、表示モードなどを定義します。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの検出方法、プラグイン、オプションなどを指定します。
- **`requirements-dev.txt`**: プロジェクトの開発時やテスト時に必要なPythonライブラリとそのバージョンを定義したファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行される際に最低限必要なPythonライブラリとそのバージョンを定義したファイルです。
- **`robots.txt`**: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてもよいか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonの高速リンタ・フォーマッタであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        - **`__init__.py`**: Pythonサブパッケージであることを示すファイルです。
        - **`badge_generator.py`**: 各リポジトリに表示する言語やスター数などのバッジを生成するロジックを実装しています。
        - **`config.yml`**: `generate_repo_list`パッケージ全体の動作を制御する設定ファイルです（例: プロジェクト概要取得機能の有効/無効、対象ファイルなど）。
        - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのユーティリティクラスや関数を提供します。
        - **`date_formatter.py`**: リポジトリの作成日や更新日などの日付情報を整形するための関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownを生成する一連の処理を調整します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートを格納しています。
        - **`language_info.py`**: リポジトリの主要言語に関する情報を取得・処理するためのロジックを実装しています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、Markdown形式の出力を生成する主要なロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADME.mdファイルから特定のバッジ情報を抽出するためのロジックを実装しています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理に適した形式に変換する役割を担います。
        - **`seo_template.yml`**: サイトのSEO関連のメタ情報やMarkdown生成時のテンプレートに関する設定を定義しています。
        - **`statistics_calculator.py`**: リポジトリ数、言語分布などの統計情報を計算するための関数を提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元管理するための設定ファイルです。
        - **`template_processor.py`**: Markdownテンプレートファイルや文字列を処理し、動的なコンテンツを埋め込むためのユーティリティを提供します。
        - **`url_utils.py`**: URLの構築、検証、エンコードなどのURL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能に対するテストコードです。
- **`tests/`**: プロジェクトの各種モジュールや機能に対するテストコードを格納するディレクトリです。
    - **`conftest.py`**: Pytestのフィクスチャ（テスト関数に共通のセットアップを提供する関数）を定義するためのファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`モジュールの結合テストを記述しています。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストコードです。
    - **`test_config.py`**: `config_manager.py`など、設定ファイルの読み込みや管理に関するテストを記述しています。
    - **`test_date_formatter.py`**: `date_formatter.py`モジュールの日付整形機能に関するテストを記述しています。
    - **`test_environment.py`**: プロジェクトの実行環境や依存関係が正しく設定されているかを確認するテストです。
    - **`test_integration.py`**: プロジェクトの主要な機能が連携して正しく動作するかを確認する結合テストを記述しています。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールのMarkdown生成ロジックに関するテストを記述しています。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールのプロジェクト概要取得機能に関するテストを記述しています。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールのREADMEからのバッジ抽出機能に関するテストを記述しています。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールのリポジトリデータ処理機能に関するテストを記述しています。

## 関数詳細説明
提供されたプロジェクト情報には、特定の関数の引数、戻り値、詳細な機能に関する情報が直接含まれていません。そのため、主要なファイルから代表的な関数の役割と目的を推測して説明します。

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main()`**: スクリプトのエントリポイント。コマンドライン引数を解析し、リポジトリ情報を取得し、Markdownを生成する一連のプロセスをオーケストレートします。
    - **`parse_arguments()`**: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、その値を返す関数です。
    - **`generate_repo_list(username, output_file, limit)`**: 指定されたGitHubユーザー名のリポジトリ情報を取得し、整形し、Markdownとして指定されたファイルに出力する主要なロジックを包含する関数です。
- **`src/generate_repo_list/repository_processor.py`**
    - **`fetch_repositories(username, token, limit)`**: GitHub APIを介して、指定されたユーザーのリポジトリ一覧を取得する関数です。認証トークンを使用し、取得数を制限できます。
    - **`process_repository_data(repo_data)`**: GitHub APIから取得した生のリポジトリデータを受け取り、プロジェクト内で扱いやすいように整形・加工する関数です。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`get_project_overview(repo_url, token, config)`**: 指定されたリポジトリのURLから、設定ファイルに定義されたパス（例: `generated-docs/project-overview.md`）のファイルを読み込み、その中の「プロジェクト概要」セクションから3行の説明を抽出して返す関数です。
- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_markdown_output(repositories_data, config, strings)`**: 処理済みのリポジトリデータ、設定、表示文言を受け取り、それらを基にGitHub Pages用のリポジトリ一覧を記述したMarkdown形式の文字列を生成する関数です。
- **`src/generate_repo_list/badge_generator.py`**
    - **`generate_badges(repo_info)`**: 個々のリポジトリ情報を受け取り、そのリポジトリに関連するバッジ（例: 使用言語、スター数、アーカイブ状態など）を表すMarkdown文字列を生成する関数です。
- **`src/generate_repo_list/config_manager.py`**
    - **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返す関数です。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-10 07:08:53 JST
