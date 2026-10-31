Last updated: 2026-11-01

# Project Overview

## プロジェクト概要
- GitHub Pages向けに、GitHub APIを利用してリポジトリ一覧ページを自動生成するシステムです。
- 検索エンジンのクロールを最適化し、各リポジトリへのアクセス性向上とLLMによる参照問題を緩和します。
- 各リポジトリの概要文、バッジ、分類などを自動抽出し、SEOに最適化されたMarkdownを出力します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: 生成されるMarkdownファイルを解釈し、静的ウェブサイトを構築するためのGitHub Pagesの基盤となるツールです。
    - **Markdown**: 生成されるリポジトリ一覧ページや各リポジトリへのリンクのコンテンツ記述形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、GitHub APIとの連携、Markdownファイルの生成ロジックなどを実装しています。
    - **GitHub API**: GitHubリポジトリに関する情報（説明、言語、スター数、トピック、ファイル内容など）をプログラムで取得するために使用されます。
    - **Git**: プロジェクト自体のバージョン管理に使用される分散型バージョン管理システムです。
- テスト:
    - **pytest**: Pythonアプリケーションのユニットテスト、結合テスト、および機能テストを実行するためのテストフレームワークです。
- ビルドツール:
    - **(カスタムPythonスクリプト)**: `generate_repo_list.py` を中心としたPythonスクリプト群が、リポジトリ情報の収集とMarkdownファイル生成という一連の「ビルド」プロセスを担っています。
- 言語機能:
    - **Python標準ライブラリ**: ファイル操作、HTTPリクエストの処理（`requests`ライブラリを介して）、文字列操作、YAML/JSONデータの解析など、スクリプトの基本的な機能を提供します。
- 自動化・CI/CD:
    - **(ローカル開発重視)**: プロジェクト情報に「CI/CD不要のローカル開発重視の構成」と明記されており、このプロジェクト自体には継続的インテグレーション/デリバリーの自動化ツールは明示されていません。
- 開発標準:
    - **Ruff**: Pythonコードのリンターおよびフォーマッターです。コードの品質と一貫性を保ち、スタイルガイドに準拠するために使用されます。
    - **EditorConfig**: 異なるIDEやエディタ間でコードの整形ルール（インデントスタイル、文字コードなど）を統一するための設定ファイルです。

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
- **.editorconfig**: 複数のエディタやIDE間でコードのスタイル設定（インデント、文字コードなど）を統一するための設定ファイル。
- **.github_automation/check_large_files/README.md**: 大容量ファイルチェック自動化スクリプトの目的と使用方法を説明するドキュメント。
- **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能に関する設定を定義するファイル。
- **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内で容量の大きいファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの目的、主な機能、使い方、設定方法、開発者向けのヒントなどをまとめたメインドキュメント。
- **_config.yml**: Jekyllサイト（生成先のGitHub Pagesサイト）全体の設定を定義するファイル。テーマ、プラグイン、変数の設定など。
- **assets/**: GitHub Pagesサイトで使用されるファビコンなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズで提供されるウェブサイトのファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグや単体動作確認に使用されるスクリプト。
- **generated-docs/**: 他のリポジトリから取得された`project-overview.md`ファイルが一時的に格納されたり、将来的に生成されるドキュメントが配置される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによって生成されるリポジトリ一覧が記述される、GitHub PagesサイトのトップページとなるMarkdownファイル。
- **issue-notes/22.md**: 開発中に発生した課題や検討事項に関するメモを記録したファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となる、アプリのメタデータ（名称、アイコン、表示設定など）を定義するファイル。
- **pytest.ini**: `pytest`テストフレームワークの実行に関する設定（テスト検出パス、追加オプションなど）を定義するファイル。
- **requirements-dev.txt**: 開発時およびテスト時に必要となるPythonパッケージの依存関係をリストアップしたファイル。
- **requirements.txt**: プロジェクトの実行に最低限必要なPythonパッケージの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonコードのリンティングとフォーマットに使用される`Ruff`ツールの設定ファイル。
- **src/__init__.py**: `src`ディレクトリをPythonパッケージとして識別させるためのファイル。
- **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして識別させるためのファイル。
- **src/generate_repo_list/badge_generator.py**: 各リポジトリの言語、スター数、フォーク数などの情報を基に、表示用のバッジ（例: Markdown形式の画像リンク）を生成する機能を提供するファイル。
- **src/generate_repo_list/config.yml**: プロジェクト概要取得機能の有効/無効、対象ファイルパス、タイムアウト時間など、本プロジェクトの動作に関する各種技術的パラメータを設定するファイル。
- **src/generate_repo_list/config_manager.py**: `config.yml`ファイルから設定値を読み込み、アプリケーション全体で利用できるように管理するモジュール。
- **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付情報を、読みやすい形式に整形するためのユーティリティ関数を提供するファイル。
- **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdown形式のリポジトリ一覧ファイルを生成します。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のために利用される、JSON-LD形式の構造化データテンプレート。リポジトリ情報と組み合わせて使用されます。
- **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形式に変換する機能を提供するファイル。
- **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリデータから、最終的なMarkdown形式の出力文字列を構築するロジックを実装したファイル。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルから、指定されたセクション（「プロジェクト概要」など）の3行説明を自動で取得する機能を提供するファイル。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報（例：CI/CDステータス、ライセンスなど）を抽出する機能を提供するファイル。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した個々のリポジトリの生データを、アプリケーション内で扱いやすいように整形・加工し、必要な情報を抽出する役割を持つファイル。
- **src/generate_repo_list/seo_template.yml**: サイトの検索エンジン最適化（SEO）関連のメタデータやテンプレート設定を定義するファイル。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算または集計する機能を提供するファイル。
- **src/generate_repo_list/strings.yml**: アプリケーションのユーザーインターフェースや出力メッセージで使用される、多言語対応可能な文字列リソースを管理するファイル。
- **src/generate_repo_list/template_processor.py**: JSON-LDテンプレートやSEOテンプレートなど、各種テンプレートファイルの読み込みと、データを用いたレンダリングを行う機能を提供するファイル。
- **src/generate_repo_list/url_utils.py**: URLの構築、パスの結合、URLエンコード・デコードなど、URLに関連する様々なユーティリティ関数を提供するファイル。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能が期待通りに動作するかを検証するためのテストスクリプト。
- **tests/conftest.py**: `pytest`テストフレームワークで使用されるフィクスチャ（テスト環境のセットアップやティアダウンを行う関数）を定義するファイル。
- **tests/test_badge_generator_integration.py**: `badge_generator`モジュールと関連する機能の結合テスト。
- **tests/test_check_large_files.py**: 大容量ファイルチェック機能の単体テスト。
- **tests/test_config.py**: `config_manager`モジュールによる設定読み込みと管理が正しく行われるかを検証するテスト。
- **tests/test_date_formatter.py**: `date_formatter`モジュールの日付整形機能のテスト。
- **tests/test_environment.py**: 開発環境のセットアップや依存関係が正しく構成されているかを検証するテスト。
- **tests/test_integration.py**: プロジェクト全体の主要な機能（GitHub API連携からMarkdown生成まで）を網羅する結合テスト。
- **tests/test_markdown_generator.py**: `markdown_generator`モジュールのMarkdown生成ロジックが期待通りに動作するかを検証するテスト。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールの単体テスト。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールによるREADMEからのバッジ抽出機能のテスト。
- **tests/test_repository_processor.py**: `repository_processor`モジュールによるリポジトリ情報処理機能のテスト。

## 関数詳細説明
提供されたプロジェクト情報および分析結果からは、各関数の具体的な引数、戻り値、内部ロジックの詳細を抽出することはできませんでした。
しかし、各ファイル名から以下の役割を持つ関数群が存在すると推測されます。

- **`src/generate_repo_list/badge_generator.py`**: リポジトリのメタデータに基づいてバッジ文字列を生成する関数。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイルを読み込み、設定値にアクセスするための関数。
- **`src/generate_repo_list/date_formatter.py`**: 日付オブジェクトを特定のフォーマットの文字列に変換する関数。
- **`src/generate_repo_list/generate_repo_list.py`**: プログラムのエントリポイントとなるメイン処理関数。GitHub APIからデータを取得し、Markdownを生成する一連のプロセスを orchestration する関数群。
- **`src/generate_repo_list/language_info.py`**: リポジトリの言語情報を解析し、主要言語などを特定する関数。
- **`src/generate_repo_list/markdown_generator.py`**: 整理されたリポジトリデータを受け取り、Markdown形式の文字列を生成する関数。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 指定されたURLからMarkdownファイルを読み込み、特定のセクションの概要テキストを抽出する関数。
- **`src/generate_repo_list/readme_badge_extractor.py`**: READMEの内容から特定のバッジの情報を正規表現などで抽出する関数。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得したJSONデータを解析し、必要なリポジトリ情報を整形して返す関数。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算または集計する関数。
- **`src/generate_repo_list/template_processor.py`**: テンプレートファイルの内容を読み込み、変数置換などを行って最終的な文字列を生成する関数。
- **`src/generate_repo_list/url_utils.py`**: URLの結合、エンコード、デコードなど、URL操作に関するユーティリティ関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-01 07:07:17 JST
