Last updated: 2026-09-24

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を取得・加工するシステムです。
- 取得した情報からGitHub Pages向けにSEO最適化されたMarkdownを自動生成します。
- これにより、リポジトリの検索エンジンインデックス促進とLLMからの参照改善を期待します。

## 技術スタック
- フロントエンド: **Jekyll, Markdown** (GitHub Pagesサイトのコンテンツ生成と表示に使用されます。JekyllはMarkdownファイルをHTMLに変換し、サイトを構築します。)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Git** (バージョン管理システムとして利用), **pytest** (Pythonコードの単体・統合テストフレームワーク), **ruff** (Pythonの高速Linterおよびフォーマッター。コード品質とスタイルを維持します。)
- テスト: **pytest** (プロジェクトのテスト実行に用いられ、コードの品質と信頼性を保証します。)
- ビルドツール: **Pythonスクリプト, Jekyll** (PythonスクリプトがGitHub APIからデータを取得しMarkdownファイルを生成する実質的な「ビルド」を担います。Jekyllは生成されたMarkdownから静的サイトを構築します。)
- 言語機能: **Python** (プロジェクトの主要な開発言語であり、GitHub APIとの連携、データ処理、Markdown生成など、コアロジックを実装しています。)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から、特定のリポジトリチェックなどの自動化に利用される可能性があります。ただし、メインのMarkdown生成はローカル実行が推奨されています。)
- 開発標準: **ruff**, **.editorconfig**, **requirements.txt**, **requirements-dev.txt** (コードスタイル統一、依存関係の明示を通じて、開発標準と品質を維持します。)

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
- **.editorconfig**: 複数の開発者が異なるエディタやIDEを使用しても、一貫したコーディングスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
  - **check_large_files/**: 大容量ファイルチェックに関するスクリプトや設定を格納するサブディレクトリです。
    - **README.md**: `check_large_files` 機能に関する説明ドキュメントです。
    - **check-large-files.toml**: 大容量ファイルチェックの具体的な設定（閾値など）を定義するTOML形式の設定ファイルです。
    - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの概要、目的、主な機能、クイックスタートガイド、開発者向けのヒントなどが記載されたプロジェクトの顔となるドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **assets/**: Webサイトで使用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリです。
  - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（アイコン）の様々なサイズです。
- **debug_project_overview.py**: `project_overview` 機能のデバッグやテスト実行を補助するためのスクリプトです。
- **generated-docs/**: リポジトリごとの `project-overview.md` など、プロジェクト概要取得機能の対象となるファイルが存在する可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのWebマスターツールによるサイトの所有権確認に使用されるファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧コンテンツが記述されるメインのMarkdownファイルです。
- **issue-notes/22.md**: 特定のIssue（この場合はIssue番号22）に関するメモや詳細情報が記述されたファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、Webアプリのメタデータ（名前、アイコン、表示モードなど）を定義するファイルです。
- **pytest.ini**: pytestフレームワークの実行設定を定義するファイルです。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを記述したファイルです。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールし、どのページをクロールしないかを指示するファイルです。
- **ruff.toml**: PythonのLinterおよびフォーマッターであるRuffの設定ファイルです。コードスタイルのルールが定義されています。
- **src/**: プロジェクトのソースコードが格納されているメインのディレクトリです。
  - **__init__.py**: Pythonパッケージであることを示すファイルです。
  - **generate_repo_list/**: リポジトリ一覧を生成するための主要なPythonモジュール群が格納されています。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ画像を生成または処理するロジックが含まれます。
    - **config.yml**: リポジトリ一覧生成に関する技術的なパラメータ（例: プロジェクト概要取得設定）を定義する設定ファイルです。
    - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、管理するためのユーティリティが含まれます。
    - **date_formatter.py**: 日付や時刻の情報を特定の形式にフォーマットするための関数群が含まれます。
    - **generate_repo_list.py**: プロジェクトのメイン実行スクリプトであり、GitHub APIからのデータ取得、処理、Markdown生成を統括します。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレートファイルです。
    - **language_info.py**: GitHubリポジトリのプログラミング言語に関する情報を処理し、集計するためのロジックが含まれます。
    - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、GitHub Pages用のMarkdownコンテンツを生成するロジックが含まれます。
    - **project_overview_fetcher.py**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクト概要の3行説明を抽出する機能を提供します。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出するためのロジックが含まれます。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、生成に適した形式に加工・整形するためのロジックが含まれます。
    - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのロジックが含まれます。
    - **strings.yml**: UIメッセージ、説明文、ラベルなど、表示される文言を一元管理するためのファイルです。
    - **template_processor.py**: MarkdownやJSON-LDのテンプレートを処理し、動的なデータを埋め込むための汎用的なロジックが含まれます。
    - **url_utils.py**: URLの検証、構築、パースなど、URL関連のユーティリティ関数が含まれます。
- **test_project_overview.py**: `project_overview_fetcher.py` に実装されたプロジェクト概要取得機能のテストコードです。
- **tests/**: プロジェクトの自動テストコードを格納するディレクトリです。
  - **conftest.py**: pytestのテスト実行において、フィクスチャやヘルパー関数などの共通設定を定義するファイルです。
  - **test_badge_generator_integration.py**: バッジ生成機能の統合テストが含まれます。
  - **test_check_large_files.py**: 大容量ファイルチェック機能のテストが含まれます。
  - **test_config.py**: 設定ファイルの読み込みや管理機能のテストが含まれます。
  - **test_date_formatter.py**: 日付フォーマット機能のテストが含まれます。
  - **test_environment.py**: 実行環境の設定や依存関係に関するテストが含まれます。
  - **test_integration.py**: プロジェクト全体の主要なフローに関する統合テストが含まれます。
  - **test_markdown_generator.py**: Markdown生成機能のテストが含まれます。
  - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストが含まれます。
  - **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能のテストが含まれます。
  - **test_repository_processor.py**: リポジトリデータ処理機能のテストが含まれます。

## 関数詳細説明
このプロジェクトはPythonで実装されており、各ファイルが特定の機能やロジックを担当する関数群を提供しています。具体的な関数シグネチャは提供されていませんが、ファイル名からその主要な役割を推測できます。

- **badge_generator.py**:
    - **目的**: リポジトリの言語やライセンス、ステータス（例: Active, Archived）を示すバッジ情報を生成または取得する関数群を提供します。
    - **機能**: 入力されたリポジトリ情報に基づいて、適切なバッジのURLやマークダウン形式のバッジ記述を生成します。
- **config_manager.py**:
    - **目的**: プロジェクトの設定ファイル（例: `config.yml`）を読み込み、設定値にアクセスするための関数群を提供します。
    - **機能**: 設定ファイルのパスを受け取り、パースして設定オブジェクトを返したり、特定のキーに対応する設定値を提供する機能などが含まれます。
- **date_formatter.py**:
    - **目的**: 日付や時刻の情報を人間が読みやすい形式や、特定のシステム要件に合った形式に変換するための関数群を提供します。
    - **機能**: 日付オブジェクトやタイムスタンプを引数として受け取り、指定されたフォーマット文字列に従って整形された日付文字列を返します。
- **generate_repo_list.py**:
    - **目的**: プロジェクトの主要な処理フローを統括するメイン関数群を提供します。GitHub APIからのデータ取得、データの加工、Markdownファイルの生成までの一連の流れを調整します。
    - **機能**: コマンドライン引数を解析し、GitHub APIクライアントを初期化、リポジトリ情報をフェッチし、`repository_processor`、`markdown_generator`などのモジュールと連携して最終的なMarkdownファイルを生成します。
- **language_info.py**:
    - **目的**: GitHub APIから取得したリポジトリの言語使用状況を分析し、整形するための関数群を提供します。
    - **機能**: 各リポジトリで使用されているプログラミング言語とそのバイト数を受け取り、パーセンテージ計算や主要言語の特定などを行います。
- **markdown_generator.py**:
    - **目的**: 処理されたリポジトリデータを受け取り、GitHub Pages向けのSEO最適化されたMarkdownコンテンツを生成するための関数群を提供します。
    - **機能**: リポジトリごとの詳細情報（名前、説明、URL、バッジ、言語、プロジェクト概要など）を引数として受け取り、指定されたテンプレートに基づいて個別のリポジトリブロックや一覧ページ全体のMarkdown文字列を構築します。
- **project_overview_fetcher.py**:
    - **目的**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明（3行）を抽出するための関数群を提供します。
    - **機能**: リポジトリのURLとファイルパスを引数として受け取り、HTTPリクエストでファイルを読み込み、指定されたセクションから概要テキストを解析して返します。キャッシュやリトライ処理も担当します。
- **readme_badge_extractor.py**:
    - **目的**: リポジトリのREADMEファイルから、既存のバッジ（例: ビルドステータス、カバレッジなど）の情報を抽出するための関数群を提供します。
    - **機能**: READMEのコンテンツを解析し、特定のパターンに一致するバッジのURLやイメージ情報を識別します。
- **repository_processor.py**:
    - **目的**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するための関数群を提供します。
    - **機能**: APIレスポンスから必要な情報を抽出し、欠損値の補完、日付の変換、言語情報の集計、プロジェクト概要の取得（`project_overview_fetcher`との連携）などを行います。
- **statistics_calculator.py**:
    - **目的**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算または集計するための関数群を提供します。
    - **機能**: 数値データを引数として受け取り、合計、平均、最大/最小などの統計量を計算します。
- **template_processor.py**:
    - **目的**: Markdownやその他のテキストテンプレートに動的なデータを埋め込み、最終的な文字列を生成するための汎用的な関数群を提供します。
    - **機能**: テンプレート文字列とデータ辞書を引数として受け取り、プレースホルダーを実際の値に置換してレンダリングされた文字列を返します。
- **url_utils.py**:
    - **目的**: URLの検証、構築、エンコード/デコードなど、URL操作に関するユーティリティ関数群を提供します。
    - **機能**: 文字列が有効なURLであるかを確認したり、ベースURLとパスから完全なURLを構築したりする機能が含まれます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-24 07:12:12 JST
