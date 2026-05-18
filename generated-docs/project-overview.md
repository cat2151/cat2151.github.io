Last updated: 2026-05-19

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ情報を自動で取得・生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに配慮したMarkdownファイルを出力します。
- これにより、GitHub Pages上でのリポジトリ情報の検索エンジンによる発見性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレータとしてのGitHub Pagesの基盤), GitHub Pages (サイトホスティングプラットフォーム), Markdown (生成されるコンテンツ形式), JSON-LD (SEOメタデータ記述形式)
- 音楽・オーディオ: なし
- 開発ツール: Git/GitHub (リポジトリ管理、API提供元)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: なし (主要な処理はPythonスクリプトによる生成で行われます)
- 言語機能: Python (主要なスクリプト言語), YAML (設定ファイル形式), JSON (データ交換形式), TOML (設定ファイル形式)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリの存在から、自動化環境での利用が想定されます)
- 開発標準: Ruff (Pythonコードのフォーマッター/リンター), EditorConfig (異なるエディタ間でのコードスタイル統一)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコードスタイルを強制するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連ファイルを格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するディレクトリ。
        - **README.md**: 大容量ファイルチェック機能の説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの目的、機能、使用方法、設定、開発者向け情報などをまとめたメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の共通設定ファイル。GitHub Pagesのビルド設定などを含む。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン画像（異なる解像度）。
- **debug_project_overview.py**: プロジェクト概要取得機能の動作確認やデバッグを行うためのスクリプト。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメントや概要ファイルが一時的に格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。自動生成されたリポジトリ一覧がここに配置される。
- **issue-notes/**: 課題（issue）に関するメモや詳細情報を格納するディレクトリ。
    - **22.md**: 特定のissue（#22）に関する詳細なメモや議論を記録したMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン機能に関する情報を提供する。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テストの発見ルールやオプションなどを指定する。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係リスト。
- **requirements.txt**: 本番環境でこのシステムを実行する際に必要なPythonパッケージの依存関係リスト。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか指示するファイル。
- **ruff.toml**: Pythonコードのフォーマッター/リンターであるRuffの設定ファイル。コードスタイルルールを定義する。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧を生成する主要ロジックを含むサブパッケージ。
        - **__init__.py**: Pythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリのステータスや技術を示すバッジの生成ロジックを扱うモジュール。
        - **config.yml**: リポジトリ一覧生成スクリプトの技術的な動作パラメータを設定するファイル。
        - **config_manager.py**: 複数の設定ファイル（config.yml, strings.ymlなど）の読み込みと管理を行うモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付情報を指定された形式に整形するユーティリティモジュール。
        - **generate_repo_list.py**: GitHub APIを呼び出し、リポジトリ情報を取得・処理し、最終的なMarkdownファイルを生成するメインスクリプト。
        - **json_ld_template.json**: SEO強化のためにコンテンツに埋め込むJSON-LD形式の構造化データのテンプレート。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を取得・処理するモジュール。
        - **markdown_generator.py**: 処理されたリポジトリデータから、指定された形式のMarkdown文字列を生成するモジュール。
        - **project_overview_fetcher.py**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）をフェッチし、その内容からプロジェクト概要を抽出するモジュール。
        - **readme_badge_extractor.py**: 各リポジトリのREADMEから特定のバッジ情報（例: ビルドステータス、カバレッジなど）を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示用に整形・フィルタリングする主要な処理モジュール。
        - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するモジュール。
        - **strings.yml**: UIメッセージ、ヘッダー、フッターなど、表示される各種テキストや文言を一元管理するファイル（国際化対応を考慮）。
        - **template_processor.py**: Markdown生成時に使用するテンプレートファイル（もしあれば）の処理を行うモジュール。
        - **url_utils.py**: URLの検証、整形、生成など、URLに関連するユーティリティ関数を集めたモジュール。
- **test_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher.py`）の単体テストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: pytestの共通フィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: バッジ生成機能の結合テスト。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
    - **test_config.py**: 設定ファイル管理機能のテスト。
    - **test_date_formatter.py**: 日付整形機能のテスト。
    - **test_environment.py**: 実行環境に関するテスト。
    - **test_integration.py**: 主要な機能群の結合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
プロジェクト情報には個別の関数に関する詳細な説明（引数、戻り値など）が直接提供されていないため、主要なモジュールに含まれると推測される代表的な機能と役割を説明します。具体的な関数名やシグネチャは、ソースコードを参照してください。

- **generate_repo_list.py** に含まれる関数:
    - **メイン処理関数**: GitHub APIからリポジトリ情報を取得し、各リポジトリを処理してMarkdown出力を統合する一連の処理を実行します。
    - **コマンドライン引数解析関数**: `--username`, `--output`, `--limit` などのコマンドライン引数をパースし、設定を適用します。
- **badge_generator.py** に含まれる関数:
    - **バッジ生成関数**: 指定された情報（例：言語、ステータス）に基づいて、Markdown形式またはHTML形式のバッジ文字列を生成します。
- **config_manager.py** に含まれる関数:
    - **設定読み込み関数**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、プログラム全体で利用可能な設定オブジェクトを提供します。
    - **設定値取得関数**: キーを指定して設定値を取得します。
- **date_formatter.py** に含まれる関数:
    - **日付整形関数**: UTC形式などの日付文字列を受け取り、ユーザーフレンドリーな形式（例：YYYY年MM月DD日）に変換して返します。
- **markdown_generator.py** に含まれる関数:
    - **リポジトリリスト生成関数**: 処理済みのリポジトリ情報のリストを受け取り、それらを整形して一つのMarkdown文字列として出力します。
    - **個別リポジトリ要素生成関数**: 各リポジトリの情報を基に、Markdown形式のブロック（タイトル、説明、バッジなど）を生成します。
- **project_overview_fetcher.py** に含まれる関数:
    - **プロジェクト概要取得関数**: 指定されたリポジトリの特定のファイル（例：`generated-docs/project-overview.md`）から「プロジェクト概要」セクションの3行説明をフェッチし、抽出します。
    - **キャッシュ管理関数**: 同一実行内でのAPI呼び出し結果をキャッシュし、パフォーマンスを向上させます。
- **repository_processor.py** に含まれる関数:
    - **リポジトリ情報処理関数**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を解析し、必要な情報を抽出し、標準化されたデータ構造に変換します。
    - **フィルタリング関数**: アーカイブ済み、フォークされたリポジトリなど、特定の条件でリポジトリをフィルタリングします。

## 関数呼び出し階層ツリー
```
プロジェクト情報には関数呼び出し階層ツリーを分析するための十分な詳細が提供されていません。
したがって、具体的な呼び出し関係を図示することはできません。

---
Generated at: 2026-05-19 07:24:42 JST
