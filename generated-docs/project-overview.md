Last updated: 2026-08-06

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で収集・整理します。
- JekyllベースのGitHub Pages向けにSEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンからの発見性を高め、開発リソースへのアクセスを容易にします。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages**: 静的サイトジェネレーターJekyllを使用し、GitHub Pagesで公開されるウェブサイトを構築します。**Markdown**: リポジトリ一覧のコンテンツ生成に使用します。**HTML/JSON-LD**: 生成されるページのSEO最適化のため、HTML構造と構造化データ（JSON-LD）を活用します。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: **Python**: プロジェクトの主要なスクリプト言語です。**GitHub API**: リポジトリ情報の取得に使用します。**secrets.toml**: GitHubトークンなどの機密情報を安全に管理します。
- テスト: **Pytest**: Pythonコードの単体テストおよび結合テストを行うためのフレームワークです。`test_*.py` ファイル群でテストが記述されています。
- ビルドツール: **Python**: スクリプトの実行環境として機能します。**requirements.txt / requirements-dev.txt**: Pythonプロジェクトの依存関係を管理し、必要なライブラリをインストールします。
- 言語機能: **Python**: 高度なデータ構造、ファイルI/O、HTTPリクエスト処理、文字列操作など、Pythonの標準的な言語機能とライブラリを活用しています。
- 自動化・CI/CD: **GitHub API**: リポジトリ情報の自動取得プロセスの中核をなします。**`.github_automation`**: 大容量ファイルチェックなど、補助的な自動化スクリプトが格納されています。
- 開発標準: **Ruff**: Pythonコードのフォーマットとリンティングを自動化し、コード品質と一貫性を維持します。**`.editorconfig`**: 複数のエディタ間でコードの書式設定を統一します。

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
- **`.editorconfig`**: 複数の開発者が異なるエディタを使用しても、コードの書式設定（インデントサイズ、エンコーディングなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックするためのツール関連ファイル群です。
        - **`README.md`**: `check_large_files` ツールの説明ドキュメントです。
        - **`check-large-files.toml`**: `check_large_files` ツールの設定を定義するファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。
- **`assets/`**: Jekyllサイトで使用される画像、アイコン、スタイルシートなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズ画像です。
- **`debug_project_overview.py`**: `project_overview_fetcher` モジュールのデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されるプロジェクト概要（`project-overview.md`）が配置されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認に使用される認証ファイルです。
- **`index.md`**: Jekyllサイトのルートページ（トップページ）となるMarkdownファイルで、生成されたリポジトリ一覧がここに出力されます。
- **`issue-notes/22.md`**: プロジェクトの課題や検討事項をメモとして記録しているファイルの一例です。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を定義し、ウェブサイトをよりアプリのように動作させるためのファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発環境およびテスト実行時に必要となるPythonライブラリとそのバージョンをリスト化したファイルです。
- **`requirements.txt`**: プロジェクトの実行に最低限必要なPythonライブラリとそのバージョンをリスト化したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいは避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッターであるRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の中核をなすモジュール群です。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: 各リポジトリに関連する言語やステータスなどのバッジ画像を生成するロジックを含みます。
        - **`config.yml`**: リポジトリ一覧生成機能の技術的なパラメータ（例：プロジェクト概要取得の有効/無効、対象ファイル名）を設定するファイルです。
        - **`config_manager.py`**: アプリケーション全体の設定（`config.yml`やシークレット）を読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形する機能を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力する主要なスクリプトファイルです。
        - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために使用されるJSON-LD形式のテンプレートデータです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報を処理・分析するモジュールです。
        - **`markdown_generator.py`**: 取得および整形されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、既存のバッジ（CI/CDステータスなど）情報を抽出するモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、分類（アクティブ、アーカイブ、フォーク）やフィルタリングを行い、アプリケーションで扱いやすい形式に整形するモジュールです。
        - **`seo_template.yml`**: SEO関連のメタデータや構造化データのテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算するモジュールです。
        - **`strings.yml`**: UIに表示されるメッセージ、ラベル、文言などを一元的に管理するためのファイルです。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイルを読み込み、動的なデータを埋め込む処理を行うモジュールです。
        - **`url_utils.py`**: URLの操作（解析、構築、バリデーションなど）を行うためのユーティリティ関数群です。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestのフィクスチャやヘルパー関数など、複数のテストファイルで共通して使用される設定を定義します。
    - **`test_badge_generator_integration.py`**: `badge_generator` の結合テストです。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files.py` のテストです。
    - **`test_config.py`**: 設定管理モジュール（`config_manager.py`）のテストです。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストです。
    - **`test_environment.py`**: 開発環境や依存関係の整合性に関するテストです。
    - **`test_integration.py`**: システム全体の統合的な動作を確認するテストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルが特定の役割を担う関数群を提供しています。具体的な関数シグネチャはコードを参照する必要がありますが、主な機能は以下の通りです。

- **`generate_repo_list.py`**:
    - **役割**: GitHub APIを介してリポジトリ情報を取得し、Jekyll対応のMarkdown形式でリポジトリ一覧を出力する主要な処理を実行します。
    - **引数**: GitHubユーザー名、出力ファイル名、処理するリポジトリ数の上限（オプション）など。
    - **戻り値**: なし（指定されたファイルにMarkdownコンテンツを出力）。
    - **機能**: 引数で指定されたユーザーのリポジトリをGitHub APIからフェッチし、各リポジトリの詳細情報を他のモジュール（`repository_processor`、`project_overview_fetcher` など）に処理させ、最終的に`markdown_generator`を使ってMarkdownファイルを生成します。
- **`config_manager.py`**:
    - **役割**: 設定ファイル（`config.yml`、`secrets.toml`など）を読み込み、アプリケーション全体で利用可能な設定オブジェクトを提供する関数群です。
    - **引数**: 設定ファイルのパスなど。
    - **戻り値**: 設定値を格納した辞書やオブジェクト。
    - **機能**: プロジェクトの実行に必要な各種設定値を安全かつ効率的に取得・管理します。
- **`project_overview_fetcher.py`**:
    - **役割**: 各リポジトリの `generated-docs/project-overview.md` ファイルから、指定されたセクションの3行説明を抽出・取得する関数群です。
    - **引数**: GitHubリポジトリのURL、設定情報（タイムアウト、リトライ設定、キャッシュ有効化フラグなど）。
    - **戻り値**: 抽出されたプロジェクト概要の文字列リスト、または取得失敗を示す値。
    - **機能**: GitHubリポジトリ内の特定のファイルにアクセスし、指定されたマーカー（例: `## プロジェクト概要`）の下にある3行のテキストを解析して返します。APIリクエストの失敗に備え、リトライやキャッシュの機構も備えています。
- **`markdown_generator.py`**:
    - **役割**: 処理されたリポジトリデータや抽出された概要情報などを用いて、最終的なSEO最適化されたMarkdownコンテンツを生成する関数群です。
    - **引数**: 整形されたリポジトリデータのリスト、設定情報、テンプレートデータなど。
    - **戻り値**: 生成されたMarkdownコンテンツの文字列。
    - **機能**: 渡されたリポジトリごとの情報（名前、説明、言語、バッジ、概要など）を事前に定義されたテンプレート（`template_processor`を利用）に埋め込み、GitHub Pagesで表示可能なMarkdown形式の文字列を作成します。
- **`repository_processor.py`**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内部で利用しやすい形式に整形・フィルタリングする関数群です。
    - **引数**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）。
    - **戻り値**: 処理され、カテゴリ分けされたリポジトリデータのリスト。
    - **機能**: リポジトリを「アクティブ」「アーカイブ」「フォーク」などのカテゴリに分類し、必要な情報（URL、説明、言語、更新日時など）を抽出し、一貫したデータ構造に変換します。
- **`badge_generator.py`**:
    - **役割**: リポジトリの言語や状態を示すバッジ（アイコンとテキスト）のHTMLまたはMarkdownコードを生成する関数群です。
    - **引数**: リポジトリの言語、スター数、最終更新日などの情報。
    - **戻り値**: バッジを示すHTMLまたはMarkdownの文字列。
    - **機能**: 各リポジトリの属性に基づき、視覚的に情報を伝えるためのバッジを動的に生成します。
- **`date_formatter.py`**:
    - **役割**: 日付や時刻の情報を特定のフォーマット文字列に変換する関数群です。
    - **引数**: 日付/時刻オブジェクトまたは文字列、フォーマット指定文字列。
    - **戻り値**: フォーマットされた日付/時刻の文字列。
    - **機能**: GitHub APIから取得される日付情報を、ウェブサイト表示に適した形式に変換します。
- **`url_utils.py`**:
    - **役割**: URLのパース、結合、バリデーションなど、URL関連の共通ユーティリティ関数群です。
    - **引数**: URL文字列、パスなど。
    - **戻り値**: 処理されたURL文字列またはURLオブジェクト。
    - **機能**: リポジトリURLやその他のリンクの操作を支援します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-06 07:25:48 JST
