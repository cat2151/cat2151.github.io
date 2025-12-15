Last updated: 2025-12-16

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEOに最適化されたMarkdown形式で出力します。
- 検索エンジンや大規模言語モデル (LLM) によるリポジトリの発見性を向上させることを目的としています。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyll), Markdown
  - **GitHub Pages (Jekyll)**: GitHubによってホスティングされる静的サイトジェネレーター。本プロジェクトで生成されたMarkdownファイルを読み込み、公開Webサイトを構築する基盤として利用されます。
  - **Markdown**: 本プロジェクトの主要な出力形式。シンプルで読みやすいテキスト形式であり、JekyllによってHTMLに変換され、Webページとして表示されます。
- 音楽・オーディオ: 該当なし
- 開発ツール: Python, GitHub API, YAML, TOML
  - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報の取得、処理、Markdown生成を行うスクリプトの実行環境です。
  - **GitHub API**: GitHub上のリポジトリ情報をプログラムから取得するために利用されるインターフェースです。
  - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、設定や表示文言を管理します。
  - **TOML**: シークレット情報 (`secrets.toml`) や他の設定ファイル (`ruff.toml`, `pytest.ini`) の記述に使用されます。
- テスト: pytest
  - **pytest**: Python用のテストフレームワークです。プロジェクトの機能が期待通りに動作するか検証するために使用されます。
- ビルドツール: Pythonスクリプト, Jekyll
  - **Pythonスクリプト**: 各種データ処理とMarkdownコンテンツの生成を行います。これが実質的なコンテンツ「ビルド」の中心となります。
  - **Jekyll**: GitHub Pagesの基盤として、生成されたMarkdownファイルをWebサイトとして構築します。
- 言語機能: Python
  - **Python**: 高い可読性と豊富なライブラリを持つ汎用プログラミング言語で、本プロジェクトのロジック全体を実装するために使用されています。
- 自動化・CI/CD: GitHub API, Pythonスクリプト
  - **GitHub API**: リポジトリ情報の定期的な取得を自動化する基盤です。
  - **Pythonスクリプト**: 情報取得からMarkdown生成までの一連のプロセスを自動実行するために使用されます。
- 開発標準: Ruff
  - **Ruff**: Pythonコードのリンターとフォーマッターです。コードの品質を均一に保ち、可読性を向上させるために使用されます。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのインデントスタイル、文字コード、改行コードなどのフォーマットを統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。一時ファイルや自動生成ファイルなどが含まれます。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法、開発者向けのヒントなどを記述した、プロジェクトの主要な説明書です。
- **`_config.yml`**: Jekyllサイト全体の挙動や設定（テーマ、プラグイン、変数など）を定義するファイルです。
- **`assets/`**: Jekyllサイトで利用される画像、アイコン、CSS、JavaScriptなどの静的ファイルを格納するディレクトリです。
  - **`favicon-*.png`**: Webサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各サイズバージョンです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` の機能を独立してデバッグ・テストするためのスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した「プロジェクト概要」などのドキュメントを一時的に格納したり、参照元として利用したりするディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。本プロジェクトによって生成されたリポジトリ一覧がこのファイルに出力されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどをMarkdown形式で記録するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルです。サイトをモバイル端末のホーム画面に追加する際の情報などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テスト実行時の挙動やオプションを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時にのみ必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの実行（本番環境）に必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、Webサイトのどのページをクロールして良いか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
  - **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして識別するためのファイルです。
  - **`src/generate_repo_list/`**: リポジトリ一覧生成に関する核心的なロジックやモジュールを格納するサブディレクトリです。
    - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリの特性（例: アクティブ、アーカイブ、フォーク）に応じたバッジのテキストやスタイルを生成するロジックを提供します。
    - **`src/generate_repo_list/config.yml`**: リポジトリ情報の取得、プロジェクト概要の自動取得機能などの技術的なパラメータを設定するYAMLファイルです。
    - **`src/generate_repo_list/config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
    - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリスクリプトです。GitHub APIからリポジトリ情報を取得し、加工して最終的なMarkdownファイルを生成する全体の処理を制御します。
    - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジンの最適化（SEO）のため、Webサイトの内容を構造化データとして記述するJSON-LD形式のテンプレートファイルです。
    - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換するモジュールです。
    - **`src/generate_repo_list/markdown_generator.py`**: 処理済みのリポジトリ情報とテンプレートをもとに、最終的なリポジトリ一覧のMarkdownコンテンツを生成するモジュールです。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明（3行）を自動的に取得する機能を提供します。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報（説明、言語、スター数など）を抽出・加工するモジュールです。
    - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュールです。
    - **`src/generate_repo_list/strings.yml`**: アプリケーション内で表示される様々なメッセージや文言（例: 見出し、ラベル）を一元的に管理するためのYAMLファイルです。国際化対応にも利用できます。
    - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートを処理し、動的なデータを埋め込んで最終的なテキストを生成するモジュールです。
    - **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリへのリンクやその他の関連URLを生成・処理するためのユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能をテストするためのスクリプトです。
- **`tests/`**: プロジェクトのテストスクリプトが格納されているディレクトリです。
  - **`tests/test_config.py`**: 設定管理モジュール（`config_manager.py`など）のテストを行うスクリプトです。
  - **`tests/test_environment.py`**: 開発・実行環境のセットアップや依存関係に関するテストを行うスクリプトです。
  - **`tests/test_integration.py`**: 複数のモジュールが連携して動作する際の統合テストを行うスクリプトです。
  - **`tests/test_markdown_generator.py`**: Markdown生成モジュール（`markdown_generator.py`）の機能をテストするスクリプトです。
  - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得モジュール（`project_overview_fetcher.py`）の機能をテストするスクリプトです。
  - **`tests/test_repository_processor.py`**: リポジトリ情報処理モジュール（`repository_processor.py`）の機能をテストするスクリプトです。

## 関数詳細説明
提供された情報から、各関数の詳細なシグネチャ（引数、戻り値）は特定できませんが、ファイル名とプロジェクトの説明に基づき、主要な関数の役割と機能を推測して説明します。

- **`src/generate_repo_list/generate_repo_list.py` 内の主要な関数**
  - **`main()`**:
    - **役割**: プログラムのエントリポイント。
    - **機能**: コマンドライン引数をパースし、設定を読み込み、GitHub APIからリポジトリ情報を取得し、各リポジトリを処理してMarkdown形式のリポジトリ一覧を生成し、指定されたファイルに出力する一連のプロセスをオーケストレートします。
- **`src/generate_repo_list/project_overview_fetcher.py` 内の主要な関数**
  - **`fetch_project_overview()`**:
    - **役割**: 指定されたリポジトリからプロジェクト概要を抽出。
    - **機能**: 特定のリポジトリの`generated-docs/project-overview.md`ファイルにアクセスし、その中から「プロジェクト概要」セクションの3行の説明を読み込み、返します。APIリクエストのタイムアウトやリトライ処理も考慮されます。
- **`src/generate_repo_list/markdown_generator.py` 内の主要な関数**
  - **`generate_markdown()`**:
    - **役割**: 処理済みリポジトリ情報からMarkdownコンテンツを生成。
    - **機能**: 整理されたリポジトリデータのリストと、必要に応じてSEOテンプレートやJSON-LDデータを受け取り、リポジトリ一覧を表現する最終的なMarkdown文字列を構築します。
- **`src/generate_repo_list/repository_processor.py` 内の主要な関数**
  - **`process_repository_data()`**:
    - **役割**: GitHub APIから取得したリポジトリデータを整形。
    - **機能**: GitHub APIから直接取得した生のリポジトリオブジェクトを受け取り、プロジェクト内で利用しやすい形式に変換・加工します。これには、必要な情報の抽出や計算、不要なデータのフィルタリングなどが含まれます。
- **`src/generate_repo_list/badge_generator.py` 内の主要な関数**
  - **`generate_badge()`**:
    - **役割**: リポジトリの状態を示すバッジを生成。
    - **機能**: リポジトリがアーカイブされているか、フォークであるかなどの情報に基づき、表示用のバッジ（例: "Archived", "Fork"）のテキストや関連するスタイル情報を生成します。
- **`src/generate_repo_list/config_manager.py` 内の主要な関数**
  - **`load_config()`**:
    - **役割**: 設定ファイルを読み込む。
    - **機能**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、アプリケーション内で利用できる設定オブジェクトとして提供します。
- **`src/generate_repo_list/statistics_calculator.py` 内の主要な関数**
  - **`calculate_statistics()`**:
    - **役割**: リポジトリの統計情報を計算。
    - **機能**: リポジトリのスター数、フォーク数、言語の使用率、最終更新日などの統計情報を集計し、表示に適した形式で提供します。
- **`src/generate_repo_list/template_processor.py` 内の主要な関数**
  - **`render_template()`**:
    - **役割**: テンプレートにデータを適用して出力。
    - **機能**: 指定されたテンプレート文字列と、そのテンプレート内で使用される変数を含むデータを受け取り、変数を実際の値で置き換えた最終的なテキスト（例: Markdownの一部）を生成します。
- **`src/generate_repo_list/url_utils.py` 内の主要な関数**
  - **`build_repo_url()`**:
    - **役割**: リポジトリのURLを構築。
    - **機能**: GitHubのユーザー名やリポジトリ名などの情報に基づき、GitHub上のリポジトリページへの正確なURLを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-16 07:06:35 JST
