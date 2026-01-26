Last updated: 2026-01-27

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得します。
- 取得した情報から、GitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンやLLMからの参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として想定), Markdown (生成されるリポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: 該当する技術は使用していません。
- 開発ツール: Python (主要な開発言語および実行環境), pytest (テストフレームワーク), ruff (コードの自動フォーマットおよびリンティングツール)
- テスト: pytest (Pythonコードのユニットテストおよび統合テスト実行に使用されるフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報を基にMarkdownファイルを生成する主要な実行環境)
- 言語機能: Python (汎用プログラミング言語。データ処理、API通信、ファイル生成に利用)
- 自動化・CI/CD: GitHub API (リポジトリ情報の自動取得に利用), 本プロジェクト自体はCI/CDを用いずローカル開発を重視する方針です。
- 開発標準: ruff (Pythonコードの品質とコーディングスタイルを統一するためのツール)

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
  📖 16.md
  📖 18.md
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
  📄 test_badge_generator_integration.py
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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの概要、目的、使い方、設定方法などが記されたメインのドキュメント。
- **_config.yml**: Jekyllサイトのグローバル設定を定義するファイル。テーマ、プラグイン、変数の設定など。
- **assets/**: Webサイトで使用される画像、CSS、JavaScriptなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイル群。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるPythonスクリプト。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメント（例: project-overview.md）が格納されることを想定したディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: 生成スクリプトの出力先となるファイル。GitHub Pagesサイトのトップページとして表示されるMarkdown形式のリポジトリ一覧。
- **issue-notes/**: 開発中に発生した課題や検討事項をメモとして整理したMarkdownファイル群を格納するディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータや表示設定を定義するマニフェストファイル。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を定義するファイル。
- **requirements-dev.txt**: 開発時およびテスト時に必要となるPythonパッケージの依存関係をリストアップしたファイル。
- **requirements.txt**: 本番環境でこのプロジェクトを実行する際に必要となるPythonパッケージの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **ruff.toml**: Pythonのリンター兼フォーマッターであるRuffの設定ファイル。コードスタイルや品質規則を定義します。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/**: リポジトリ一覧を生成するための主要なPythonモジュール群を格納するパッケージ。
    - **__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジを生成または管理するロジック。
    - **config.yml**: プロジェクト概要の取得設定など、アプリケーションの技術的パラメータを定義するYAML形式の設定ファイル。
    - **config_manager.py**: `config.yml` や `secrets.toml` など、各種設定ファイルを読み込み、管理するモジュール。
    - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供するモジュール。
    - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインの実行スクリプト。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）を強化するために、構造化データ（JSON-LD）のテンプレートを定義するファイル。
    - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理するモジュール。
    - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Markdown形式のコンテンツを生成するロジック。
    - **project_overview_fetcher.py**: 各リポジトリ内の `project-overview.md` ファイルからプロジェクト概要を抽出し、取得する機能。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形、フィルタリングし、必要な情報を抽出するロジック。
    - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータや記述のテンプレートを定義するYAMLファイル。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算するモジュール。
    - **strings.yml**: UIメッセージ、説明文、タイトルなど、表示されるテキストコンテンツを一元管理するためのYAMLファイル。
    - **template_processor.py**: Markdownテンプレートやその他のテキストテンプレートに変数を適用し、最終的な出力を生成するモジュール。
    - **url_utils.py**: URLの検証、整形、生成など、URLに関連するユーティリティ関数。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能に関する単体テストまたは結合テスト。
- **tests/**: プロジェクト全体のテストファイルを格納するディレクトリ。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **test_config.py**: 設定管理モジュール（`config_manager.py`）のテスト。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテスト。
    - **test_environment.py**: 実行環境に関する設定や依存関係のテスト。
    - **test_integration.py**: 主要な機能フロー全体の統合テスト。
    - **test_markdown_generator.py**: Markdown生成モジュール（`markdown_generator.py`）のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得モジュール（`project_overview_fetcher.py`）のテスト。
    - **test_readme_badge_extractor.py**: READMEバッジ抽出モジュール（`readme_badge_extractor.py`）のテスト。
    - **test_repository_processor.py**: リポジトリ処理モジュール（`repository_processor.py`）のテスト。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数の役割、引数、戻り値、機能に関する詳細な説明が含まれていません。そのため、具体的な関数の詳細を記述することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-27 07:06:50 JST
