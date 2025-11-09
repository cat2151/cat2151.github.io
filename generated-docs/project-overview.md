Last updated: 2025-11-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンからの参照性を高め、LLMによるリポジトリ情報の利用を円滑にすることを目指します。

## 技術スタック
- フロントエンド: GitHub Pages (JekyllベースでMarkdownファイルをレンダリング)
- 音楽・オーディオ: N/A
- 開発ツール: pytest (テストフレームワーク), ruff (コード整形・静的解析), GitHub API (リポジトリ情報取得)
- テスト: pytest (Pythonコードの単体・結合テスト実行)
- ビルドツール: N/A (PythonスクリプトによるMarkdownファイル生成)
- 言語機能: Python (スクリプト言語、主要なロジックを実装)
- 自動化・CI/CD: N/A (ローカルでの実行を重視し、明示的なCI/CDツールは使用していません)
- 開発標準: ruff (Pythonコードのスタイルガイドとリンティング)

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
  📖 2.md
  📖 4.md
  📖 6.md
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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   `.gitignore`: Gitによってバージョン管理されるべきではないファイルやディレクトリを指定するファイル。
-   `LICENSE`: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   `README.md`: プロジェクトの目的、機能、セットアップ方法、使い方などが記述されたメインドキュメント。
-   `_config.yml`: Jekyllサイト全体の構成設定ファイル。GitHub Pagesのビルド設定に影響します。
-   `assets/`: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
-   `debug_project_overview.py`: `project_overview`機能の動作検証やデバッグのために使用される補助スクリプト。
-   `generated-docs/`: 他のリポジトリから抽出された概要ファイル（`project-overview.md`）などが格納される可能性のあるディレクトリ。
-   `index.md`: スクリプトによって自動生成される、リポジトリ一覧のメインMarkdownファイル。GitHub Pagesのトップページとして表示されます。
-   `issue-notes/`: 開発中に発生した課題や検討事項に関するメモをMarkdown形式で保存するディレクトリ。
    -   `2.md`, `4.md`, `6.md`: 個別の課題やメモの内容を記述したファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）として動作させるための設定ファイル。アプリの表示方法や動作を定義します。
-   `pytest.ini`: Pythonのテストフレームワークである`pytest`の設定ファイル。テストの実行オプションなどを定義します。
-   `requirements-dev.txt`: 開発環境やテスト実行時に必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `requirements.txt`: プロジェクトの実行時に最低限必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか指示するファイル。
-   `ruff.toml`: PythonのLinterおよびFormatterである`ruff`の設定ファイル。コードの品質と一貫性を保ちます。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   `__init__.py`: Pythonがこのディレクトリをパッケージとして認識するために必要なファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成機能に関連するPythonモジュールをまとめたパッケージ。
        -   `__init__.py`: このディレクトリをPythonパッケージとして認識させるためのファイル。
        -   `badge_generator.py`: リポジトリの各種ステータスや言語を示すバッジ画像を生成するロジックを提供します。
        -   `config.yml`: リポジトリ一覧生成に関する各種設定（例: `project_overview`機能の有効/無効、対象ファイルパス）を定義します。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形式で管理するモジュール。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を統括します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義します。
        -   `language_info.py`: リポジトリのプログラミング言語情報を処理し、表示に適した形式に変換するモジュール。
        -   `markdown_generator.py`: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装しています。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、表示やMarkdown生成に適した形に加工・整形するモジュール。
        -   `seo_template.yml`: SEO関連のメタデータや、生成されるMarkdownのSEO要素に関するテンプレート設定を定義します。
        -   `statistics_calculator.py`: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算するモジュール。
        -   `strings.yml`: アプリケーション内で使用される表示テキストやメッセージを国際化/一元管理するための設定ファイル。
        -   `template_processor.py`: Markdown生成時に利用するテンプレート（JekyllのLiquidなど）の処理を扱うモジュール。
        -   `url_utils.py`: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプト。
-   `tests/`: プロジェクト全体のテストケースをまとめたディレクトリ。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理が正しく行われるかをテストします。
    -   `test_environment.py`: 開発環境のセットアップや依存関係が適切に構成されているかをテストします。
    -   `test_integration.py`: 複数のモジュールが連携して期待通りに動作するかを検証する統合テスト。
    -   `test_markdown_generator.py`: `markdown_generator`モジュールが正しいMarkdownを生成するかをテストします。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールが正しく概要を抽出できるかをテストします。
    -   `test_repository_processor.py`: `repository_processor`モジュールがリポジトリデータを適切に処理するかをテストします。

## 関数詳細説明
-   `main()`: (src/generate_repo_list/generate_repo_list.py)
    -   役割: コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成といった主要な処理フロー全体をオーケストレートします。
    -   引数: なし (コマンドライン引数は`argparse`などで内部的に処理)
    -   戻り値: なし (サイドエフェクトとしてファイル生成を行います)
-   `fetch_repositories(username, limit=None)`: (src/generate_repo_list/repository_processor.py 内で、または `generate_repo_list.py` から呼び出される)
    -   役割: GitHub APIを介して、指定されたユーザーのリポジトリ一覧を取得します。
    -   引数: `username` (str) - GitHubのユーザー名、`limit` (int, optional) - 取得するリポジトリ数の上限（デバッグ用）
    -   戻り値: GitHub APIから取得した生のリポジトリ情報のリスト (list of dict)
-   `process_repository_data(repo_data)`: (src/generate_repo_list/repository_processor.py)
    -   役割: GitHub APIから取得した個々のリポジトリの生データを整形し、表示やMarkdown生成に適した形式に加工します。
    -   引数: `repo_data` (dict) - 単一リポジトリの生データ
    -   戻り値: 処理済みのリポジトリ情報 (dict)
-   `generate_markdown(processed_repos, config)`: (src/generate_repo_list/markdown_generator.py)
    -   役割: 処理済みのリポジトリ情報のリストを受け取り、Jekyll対応のMarkdown形式コンテンツを生成します。
    -   引数: `processed_repos` (list of dict) - 処理済みリポジトリ情報のリスト、`config` (dict) - プロジェクト設定
    -   戻り値: 生成されたMarkdown文字列 (str)
-   `fetch_project_overview(repo_owner, repo_name, file_path, config)`: (src/generate_repo_list/project_overview_fetcher.py)
    -   役割: 指定されたリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、「プロジェクト概要」セクションの3行説明を抽出し取得します。
    -   引数: `repo_owner` (str), `repo_name` (str), `file_path` (str), `config` (dict) - プロジェクト設定
    -   戻り値: 抽出されたプロジェクト概要の文字列 (str) または None
-   `load_config(config_path)`: (src/generate_repo_list/config_manager.py)
    -   役割: 指定されたYAMLファイルパスから設定データを読み込みます。
    -   引数: `config_path` (str) - 設定ファイルのパス
    -   戻り値: 読み込まれた設定データ (dict)

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-10 07:05:45 JST
