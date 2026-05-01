Last updated: 2026-05-02

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してGitHub Pages向けMarkdownを生成します。
- SEOを考慮したリポジトリ一覧を自動作成し、検索エンジンやLLMからの参照性を向上させます。
- リポジトリ概要、バッジ表示、カテゴリ分類など、豊富な情報を持つ一覧ページを生成可能です。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤とし、生成されたMarkdownファイルが表示されます。Markdown自体も出力形式として利用されます。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連の技術は使用されていません。
- 開発ツール: Python (スクリプト言語) を主要言語とし、GitHub APIを介してリポジトリ情報を取得します。設定にはYAMLおよびTOML形式のファイルを使用し、SEO関連のメタデータにはJSON-LDテンプレートを活用しています。
- テスト: `Pytest` をテストフレームワークとして採用しており、コードの品質と信頼性を保証するための単体テストおよび統合テストが記述されています。
- ビルドツール: Pythonスクリプト自体がMarkdownファイルを生成する役割を担います。JekyllはGitHub Pages側でマークダウンをHTMLに変換する役割を果たします。
- 言語機能: 主に `Python` 言語の機能を利用して、GitHub APIとの連携、データ処理、ファイルI/O、文字列操作などを行っています。
- 自動化・CI/CD: GitHub APIを利用してリポジトリ情報の取得とMarkdown生成を自動化していますが、CI/CDパイプラインは「ローカル開発重視」のため直接的には導入されていません。
- 開発標準: コードの品質と一貫性を保つため、`Ruff` を使用してコードのリンティングとフォーマットを行います。`.editorconfig` でエディタのコードスタイルを統一しています。

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
- **.editorconfig**: 異なるエディタやIDE間で、インデントスタイル、文字コードなどのコードスタイルを統一するための設定ファイルです。
- **.github_automation/**: 特定のGitHub自動化タスク（例: 大容量ファイルチェック）に関連するスクリプトと設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェックに関するファイル群です。
        - **README.md**: `check_large_files`機能の説明です。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、使い方、設定方法、テスト実行手順などがまとめられたメインのドキュメントファイルです。
- **_config.yml**: JekyllによるGitHub Pagesサイトの全体設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像（ファビコンなど）やその他の静的アセットを格納するディレクトリです。
- **debug_project_overview.py**: `project_overview`機能のデバッグや単体テストを目的としたスクリプトです。
- **generated-docs/**: リポジトリの`project-overview.md`などの生成されたドキュメントを格納するためのプレースホルダー、または参照されるパスです。
- **googled947dc864c270e07.html**: Google Search Consoleなどでサイトの所有権を確認するために配置されるHTMLファイルです。
- **index.md**: 生成されたリポジトリ一覧が実際に書き出されるメインのMarkdownファイルです。このファイルがGitHub Pagesによって表示されます。
- **issue-notes/22.md**: 開発中に発生した課題や検討事項、メモなどを記録するためのファイル群です。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、アプリのメタデータを定義するファイルです。
- **pytest.ini**: PythonのテストフレームワークであるPytestの設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonライブラリの依存関係を定義したファイルです。
- **requirements.txt**: 本番環境でこのプロジェクトを実行するために必要となるPythonライブラリの依存関係を定義したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、あるいは除外するかを指示するためのファイルです。
- **ruff.toml**: Pythonコードのリンティングとフォーマットを行うツール`Ruff`の設定ファイルです。
- **src/**: プロジェクトのソースコードを格納するメインのディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示す空ファイルです。
    - **generate_repo_list/**: リポジトリ一覧生成の主要なロジックを含むサブパッケージです。
        - **__init__.py**: `generate_repo_list`がPythonパッケージであることを示します。
        - **badge_generator.py**: リポジトリの各種情報（言語、スター数など）に応じたバッジを生成するロジックを含みます。
        - **config.yml**: プロジェクト概要取得機能など、アプリケーション固有の技術的パラメータを設定するファイルです。
        - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、アプリケーション全体でアクセス可能な形で管理するロジックを提供します。
        - **date_formatter.py**: 日付や時刻の情報を、指定されたフォーマットで整形する機能を提供します。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプトで、GitHub APIからのデータ取得からMarkdown生成までの全体フローをオーケストレートします。
        - **json_ld_template.json**: SEOを目的としたJSON-LD形式のメタデータテンプレートです。
        - **language_info.py**: リポジトリの主要言語情報や、その表示に関する処理ロジックを含みます。
        - **markdown_generator.py**: 取得したリポジトリ情報や統計情報に基づき、Markdownコンテンツを生成するロジックを担います。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得するロジックを提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報を抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形する主要な処理ロジックを含みます。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータや構造に関するテンプレート設定です。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算するロジックを含みます。
        - **strings.yml**: UIメッセージ、表示文言、カテゴリ名など、アプリケーション内で使用されるテキストコンテンツを一元管理するためのファイルです。
        - **template_processor.py**: 汎用的なテンプレート処理や文字列置換などを行うユーティリティ機能を提供します。
        - **url_utils.py**: URLの生成、解析、バリデーションなど、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能に関するテストコードです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **conftest.py**: Pytestで共有されるフィクスチャやヘルパー関数などを定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator.py`の統合的な動作を確認するためのテストコードです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストコードです。
    - **test_config.py**: 設定ファイルの読み込みや解析に関するテストコードです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストコードです。
    - **test_environment.py**: 実行環境の設定や依存関係に関する基本的なテストコードです。
    - **test_integration.py**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを確認する統合テストコードです。
    - **test_markdown_generator.py**: Markdown生成ロジックのテストコードです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストコードです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストコードです。
    - **test_repository_processor.py**: リポジトリ情報処理ロジックのテストコードです。

## 関数詳細説明
提供されたプロジェクト情報からは、個々の関数の具体的な役割、引数、戻り値、機能の詳細を特定することができませんでした。
しかし、各ファイルが担当する主要な機能は以下の通り推測されます。

- **badge_generator.py**: リポジトリの言語、スター数、最終更新日などの情報に基づいて、視覚的なバッジ（アイコン）を生成する関数群を含みます。
- **config_manager.py**: アプリケーションの動作に必要な設定値（YAMLファイルなどから）を読み込み、管理、および提供する関数群を含みます。
- **date_formatter.py**: GitHub APIから取得した日付データを、人間が読みやすい形式や、特定のロケールに合わせた形式に変換する関数群を含みます。
- **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、それを処理し、最終的にMarkdown形式の出力ファイルを生成する一連の主要な処理を調整する関数群を含みます。
- **language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形に整形する関数群を含みます。
- **markdown_generator.py**: 処理されたリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツ文字列を生成する関数群を含みます。
- **project_overview_fetcher.py**: 各リポジトリの特定のパスにある`project-overview.md`ファイルから、定められた形式（3行要約など）でプロジェクト概要を抽出・取得する関数群を含みます。
- **readme_badge_extractor.py**: リポジトリのREADMEファイルの内容を解析し、そこに埋め込まれたバッジ（例: Shield.io形式）のURLや情報を抽出する関数群を含みます。
- **repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、必要な属性（名前、説明、URL、スター数など）を抽出し、アプリケーションの内部モデルに変換する関数群を含みます。
- **statistics_calculator.py**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を集計し、計算する関数群を含みます。
- **template_processor.py**: 汎用的なテンプレート文字列の置換や、条件に応じたテキスト生成を行う関数群を含みます。
- **url_utils.py**: URLの構築、検証、エンコード・デコードなど、URLに関連する様々なユーティリティ機能を提供する関数群を含みます。

## 関数呼び出し階層ツリー
```
提供された情報からは、プロジェクト全体の関数の呼び出し階層ツリーを分析できませんでした。

---
Generated at: 2026-05-02 07:20:10 JST
