Last updated: 2026-03-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するPythonシステムです。
- GitHub APIを利用し、各リポジトリの詳細情報や概要をSEO最適化されたMarkdownで出力します。
- これにより、検索エンジンからの視認性を高め、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll: GitHub Pagesサイトの構築に利用される静的サイトジェネレータ。生成されたMarkdownファイルを美しいWebページに変換します。
- 音楽・オーディオ: N/A
- 開発ツール:
  - Python: プロジェクトの主要なスクリプト言語。リポジトリ情報の取得、処理、Markdown生成を行います。
  - GitHub API: GitHubからリポジトリ情報をプログラム的に取得するためのインターフェース。
- テスト: pytest: Python用のテストフレームワーク。プロジェクトの各機能が意図通りに動作するかを検証します。
- ビルドツール: Python (カスタムスクリプト): Pythonスクリプト自体が、GitHub APIから取得したデータをもとにMarkdownファイルを「ビルド」する役割を担います。
- 言語機能: Python: スクリプトの記述に利用されるプログラミング言語。
- 自動化・CI/CD: N/A (本プロジェクトはローカル開発での実行を重視しており、継続的インテグレーション/デリバリーの仕組みは明示的に採用していません。)
- 開発標準: ruff: Pythonコードのスタイルチェックと自動フォーマットを行うツール。一貫性のあるコード品質を維持するために使用されます。

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
- **.editorconfig**: 異なるエディタやIDE間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
  - **check_large_files/**: 大容量ファイルチェック機能に関するファイル群。
    - **README.md**: 大容量ファイルチェック機能の説明ドキュメント。
    - **check-large-files.toml**: 大容量ファイルチェックツールの設定ファイル。
    - **scripts/check_large_files.py**: リポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報 (MITライセンス)。著作権や利用条件を定義します。
- **README.md**: プロジェクトの概要、目的、セットアップ方法、使い方などを記述したメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定ファイル。テーマ、プラグイン、変数の定義などが含まれます。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
  - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズ。
- **debug_project_overview.py**: `project_overview` 機能のデバッグを目的としたPythonスクリプト。
- **generated-docs/**: 各リポジトリの `project-overview.md` など、プロジェクトによって自動生成されたドキュメントやデータが格納されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するための認証用HTMLファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。本システムにより生成されたリポジトリ一覧がここに書き込まれます。
- **issue-notes/**: 開発中に発生した課題や検討事項に関するメモを格納するディレクトリ。
  - **22.md**: 特定の課題（例: Issue #22）に関する詳細なMarkdownメモ。
- **manifest.json**: プログレッシブWebアプリ（PWA）のWebアプリマニフェストファイル。アプリのメタデータや表示設定を定義します。
- **pytest.ini**: pytestテストフレームワークのグローバル設定ファイル。テストの発見や実行に関する設定を定義します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイル。
- **requirements.txt**: 本番環境（または最小限の実行環境）に必要なPythonパッケージとそのバージョンをリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイル。
- **ruff.toml**: PythonコードのリンティングおよびフォーマットツールであるRuffの設定ファイル。コードスタイルの規則を定義します。
- **src/**: プロジェクトの主要なソースコードが配置されているディレクトリ。
  - **__init__.py**: Pythonパッケージであることを示すファイル。
  - **generate_repo_list/**: リポジトリ一覧生成機能の中核をなすPythonモジュール。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **badge_generator.py**: プロジェクトの言語やステータスを示すバッジ（アイコン）を生成する機能を提供します。
    - **config.yml**: `generate_repo_list` モジュール固有の設定パラメータ（例: プロジェクト概要取得機能の設定）を定義するYAMLファイル。
    - **config_manager.py**: YAMLファイルから設定を読み込み、アプリケーション全体で利用可能にするためのユーティリティ。
    - **date_formatter.py**: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数。
    - **generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を統括します。
    - **json_ld_template.json**: 検索エンジン最適化(SEO)のために構造化データを埋め込むためのJSON-LDテンプレート。
    - **language_info.py**: リポジトリの使用言語情報を処理し、集計や整形を行う機能。
    - **markdown_generator.py**: 取得したリポジトリ情報をもとに、GitHub Pages用のMarkdown形式のコンテンツを生成する機能。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得する機能。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に処理するビジネスロジック。
    - **seo_template.yml**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するYAMLファイル。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算する機能。
    - **strings.yml**: UIに表示されるメッセージや文言を管理するYAMLファイル。多言語対応（i18n）にも利用できます。
    - **template_processor.py**: Markdown生成時に特定のテンプレート構文を処理し、動的なデータを埋め込むユーティリティ。
    - **url_utils.py**: URLの構築、検証、解析など、URLに関連するユーティリティ関数。
- **test_project_overview.py**: `project_overview_fetcher` 機能の単体テストを記述したPythonスクリプト。
- **tests/**: プロジェクトの様々なコンポーネントのテストコードを格納するディレクトリ。
  - **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
  - **test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
  - **test_config.py**: 設定管理機能 (`config_manager.py`) のテスト。
  - **test_date_formatter.py**: 日付フォーマット機能 (`date_formatter.py`) のテスト。
  - **test_environment.py**: 実行環境に関するテスト（例: 必要な環境変数の存在チェック）。
  - **test_integration.py**: 主要なコンポーネント間の連携を検証する統合テスト。
  - **test_markdown_generator.py**: Markdown生成機能 (`markdown_generator.py`) のテスト。
  - **test_project_overview_fetcher.py**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテスト。
  - **test_readme_badge_extractor.py**: READMEバッジ抽出機能 (`readme_badge_extractor.py`) のテスト。
  - **test_repository_processor.py**: リポジトリ処理機能 (`repository_processor.py`) のテスト。

## 関数詳細説明
提供された情報には具体的なPython関数の詳細なシグネチャ（引数、戻り値）は含まれておりません。ここでは、各モジュールの主な役割に基づいて、想定される主要な機能について説明します。

- `generate_repo_list.py` (メイン処理):
  - **役割**: プログラムのエントリーポイント。GitHub APIからリポジトリ情報を取得し、取得したデータを処理して、最終的にMarkdown形式のリポジトリ一覧ファイルを生成します。
  - **機能**: 設定の読み込み、GitHub API呼び出し、データ加工、Markdown生成の各ステップをオーケストレーションします。

- `badge_generator.py` (バッジ生成):
  - **役割**: リポジトリの言語やステータスなどを示す視覚的なバッジ（アイコン）を生成します。
  - **機能**: 特定のデータに基づいて、適切なデザインとテキストを持つバッジのMarkdown/HTMLコードを生成します。

- `config_manager.py` (設定管理):
  - **役割**: YAMLファイルから設定データを読み込み、アプリケーション内で利用できる形式で提供します。
  - **機能**: 設定ファイルのパスを指定して内容を解析し、設定オブジェクトとして返します。

- `date_formatter.py` (日付フォーマット):
  - **役割**: 日付や時刻データを特定のユーザーフレンドリーな形式に変換します。
  - **機能**: APIから取得した日付文字列などを、読みやすい「YYYY年MM月DD日」のような形式に変換します。

- `markdown_generator.py` (Markdown生成):
  - **役割**: 処理されたリポジトリデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを構築します。
  - **機能**: テンプレートとリポジトリデータを組み合わせて、整形されたMarkdown文字列を生成します。

- `project_overview_fetcher.py` (プロジェクト概要取得):
  - **役割**: 各リポジトリに存在する特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの概要テキストを抽出します。
  - **機能**: リポジトリのURLとファイルパスを指定し、そのファイルの内容を読み込み、指定されたセクション（例: `## プロジェクト概要`）のテキストをパースして抽出します。

- `repository_processor.py` (リポジトリ処理):
  - **役割**: GitHub APIから取得した生のリポジトリデータを分析し、Markdown生成に必要な情報（バッジ情報、統計、概要など）を抽出・整形します。
  - **機能**: リポジトリのJSONデータを受け取り、言語、スター数、フォーク数、最終更新日などの詳細情報を取り出し、必要に応じて他のモジュールを呼び出して追加情報を取得します。

## 関数呼び出し階層ツリー
```
generate_repo_list.py (メインスクリプト)
├── config_manager.py (設定ファイルの読み込み)
├── [GitHub API呼び出し] (リポジトリ情報の取得)
└── repository_processor.py (取得データの処理)
    ├── project_overview_fetcher.py (各リポジトリの概要取得)
    ├── readme_badge_extractor.py (READMEからのバッジ情報抽出)
    ├── language_info.py (言語情報の処理)
    └── statistics_calculator.py (統計情報の計算)
└── markdown_generator.py (Markdownコンテンツの生成)
    ├── badge_generator.py (バッジの生成)
    ├── date_formatter.py (日付の整形)
    ├── template_processor.py (Markdownテンプレートの適用)
    └── url_utils.py (URL関連のユーティリティ)
└── [ファイル出力] (index.md などへの書き出し)

---
Generated at: 2026-03-17 07:13:01 JST
