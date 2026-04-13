Last updated: 2026-04-14

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で取得・整理するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、プロジェクトの検索エンジンでの可視性を高め、LLMによる参照性向上にも貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - GitHub Pages上で動的なコンテンツ表示を可能にする静的サイトジェネレーター。
- 開発ツール:
    - Python: メインのスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成ロジックに使用されています。
    - GitHub API: GitHubからリポジトリ情報をプログラム的に取得するためのインターフェース。
- テスト: pytest - Pythonコードの単体テストおよび統合テストフレームワーク。
- ビルドツール: Pythonスクリプト - GitHub APIから取得したデータをもとに、最終的なMarkdownコンテンツを生成するカスタムロジック。
- 言語機能:
    - Python: プロジェクトの主要なプログラミング言語。
    - YAML: `config.yml`や`strings.yml`など、設定ファイルやメッセージ管理に使用されるデータ記述言語。
    - TOML: `ruff.toml`や`check-large-files.toml`など、設定ファイルに使用されるデータ記述言語。
    - Markdown: 生成されるリポジトリ一覧の出力形式であり、Jekyllサイトのコンテンツ形式。
    - JSON: `json_ld_template.json`など、構造化データ（JSON-LD）の記述に使用されるデータ形式。
- 自動化・CI/CD:
    - Pythonスクリプトによる自動生成: メインの`generate_repo_list.py`がリポジトリ一覧の自動生成を実行します。
    - `.github_automation`: GitHubの自動化処理（例: 大容量ファイルチェック）に関連するスクリプトや設定を格納します。
- 開発標準:
    - ruff: Pythonコードの品質と一貫性を保つためのリンターおよびフォーマッター。
    - .editorconfig: 異なるエディタやIDE間でコードスタイルを統一するための設定ファイル。

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
-   **`.editorconfig`**: さまざまなエディタやIDE間で、インデントスタイルや文字コードなどのコードフォーマット設定を統一するためのファイルです。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトに関連するファイルや設定を格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルのチェックに関する自動化機能のディレクトリです。
        -   **`README.md`**: `check_large_files`機能についての説明ドキュメントです。
        -   **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
        -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
-   **`README.md`**: プロジェクト全体の目的、機能、使い方、設定方法などを説明するメインのドキュメントです。
-   **`_config.yml`**: Jekyllサイトの全体設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
-   **`assets/`**: GitHub Pagesサイトで使用される画像やアイコンなどの静的ファイルを格納するディレクトリです。
    -   **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）のさまざまなサイズです。
-   **`debug_project_overview.py`**: リポジトリごとのプロジェクト概要取得機能のデバッグ用途で使用されるPythonスクリプトです。
-   **`generated-docs/`**: 自動生成されたドキュメントや、特定の機能（例: プロジェクト概要取得）のターゲットとなるファイルを格納する可能性があります。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイルです。
-   **`index.md`**: GitHub Pagesサイトのトップページとして、自動生成されたリポジトリ一覧が出力されるMarkdownファイルです。
-   **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（番号22）に関する詳細なノートです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示方法や動作を設定します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`requirements.txt`**: 本番環境でこのプロジェクトを実行する際に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツールであるruffの設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧生成機能の中核をなすPythonモジュール群のディレクトリです。
        -   **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        -   **`badge_generator.py`**: リポジトリに表示されるバッジ（例: 言語、ライセンス）を生成または管理する機能を提供します。
        -   **`config.yml`**: リポジトリ一覧生成スクリプトの技術的な設定パラメータ（例: APIリトライ回数、キャッシュ設定）を定義するファイルです。
        -   **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのモジュールです。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ機能を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメイン実行スクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体を制御します。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、リポジトリ情報を構造化データとして記述するJSON-LDのテンプレートファイルです。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、整形する機能を提供します。
        -   **`markdown_generator.py`**: GitHub APIから取得したデータとテンプレートを使用して、最終的なMarkdownコンテンツを生成するロジックを実装しています。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得する機能です。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス）を抽出する機能を提供します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形するための機能を提供します。
        -   **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        -   **`strings.yml`**: ユーザーインターフェースに表示されるメッセージ、ラベル、その他のテキスト文言を一元的に管理するためのファイルです。
        -   **`template_processor.py`**: Markdownテンプレートの読み込み、変数置換、条件分岐などのテンプレート処理を行う機能を提供します。
        -   **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するさまざまなユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの動作を検証するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを行うスクリプトです。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files`機能のテストを行うスクリプトです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能に関するテストを行うスクリプトです。
    -   **`test_date_formatter.py`**: 日付フォーマット機能のテストを行うスクリプトです。
    -   **`test_environment.py`**: 実行環境の設定や依存関係に関するテストを行うスクリプトです。
    -   **`test_integration.py`**: プロジェクトの主要なコンポーネント間の連携を検証する統合テストを行うスクリプトです。
    -   **`test_markdown_generator.py`**: Markdown生成機能のロジックを検証するテストを行うスクリプトです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うスクリプトです。
    -   **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを行うスクリプトです。
    -   **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うスクリプトです。

## 関数詳細説明
提供された情報では、個別の関数詳細を特定できませんでした。
（ファイル詳細分析で`googled947dc864c270e07.html`は関数を持たないと記述されていましたが、他のPythonスクリプト内の関数については詳細な情報が提供されていません。）

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-14 07:22:29 JST
