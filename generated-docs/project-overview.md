Last updated: 2025-12-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- 検索エンジン最適化（SEO）とLLMによる参照性を向上させ、リポジトリの可視性を高めることを目的としています。
- 各リポジトリから3行のプロジェクト概要を自動取得・表示する機能も持ち、魅力的な一覧を提供します。

## 技術スタック
- フロントエンド: **JekyllベースのGitHub Pages** (静的サイトジェネレータでHTML/CSS/JavaScriptを生成), **Markdown** (リポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なスクリプト言語), **pytest** (テストフレームワーク), **ruff** (コードリンター/フォーマッター)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストに使用)
- ビルドツール: **Jekyll** (GitHub Pagesが利用する静的サイトジェネレータ), **Pythonスクリプト** (Markdownファイル生成の核心)
- 言語機能: **Python** (GitHub APIとの連携、ファイル操作、データ処理)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の自動取得), **ローカル実行スクリプト** (リポジトリ一覧の自動生成)
- 開発標準: **ruff** (Pythonコードのスタイル統一と品質維持), **.editorconfig** (各種エディタでのコードスタイル統一)

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
- **.editorconfig**: 複数の開発者が異なるエディタを使用する際に、コードの整形ルール（インデント、改行など）を統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド生成物、一時ファイル）を指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載しており、本プロジェクトの利用条件を示します。
- **README.md**: プロジェクトの目的、機能、使用方法、設定、開発者向けのヒントなどを記述したメインのドキュメントです。
- **_config.yml**: JekyllベースのGitHub Pagesサイト全体の共通設定（サイトタイトル、テーマなど）を定義するファイルです。
- **assets/**: サイトで使用する画像やアイコンなどの静的ファイルを格納するディレクトリです。
    - `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各種サイズを格納しています。
- **debug_project_overview.py**: 「プロジェクト概要自動取得」機能のデバッグや単体テストを行うためのスクリプトです。
- **generated-docs/**: 他のリポジトリから自動取得された `project-overview.md` などのドキュメントを一時的、あるいは永続的に格納する可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどでサイトの所有権を確認するために配置される認証ファイルです。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このファイルにリポジトリ一覧が自動生成されます。
- **issue-notes/**: 開発中に発生した課題や検討事項をMarkdown形式で記録したメモファイル群を格納するディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブサイトをモバイルデバイスのホーム画面に追加した際の表示や動作を定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイルです。
- **requirements-dev.txt**: 開発時やテスト実行時に必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に最低限必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール（読み込み）してよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリンター/フォーマッターであるruffの設定ファイルで、コードのスタイルや品質を自動的にチェック・修正するためのルールを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    - `__init__.py`: Pythonがこのディレクトリをパッケージとして認識するために必要なファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧自動生成システムのコアロジックを構成するPythonパッケージです。
        - `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        - `badge_generator.py`: リポジトリのプロパティ（例：言語、ステータス）に基づいて、視覚的なバッジ（アイコン）を生成する機能を提供します。
        - `config.yml`: 「プロジェクト概要自動取得」機能の有効/無効、対象ファイル名、リトライ回数などの技術的なパラメータを設定するファイルです。
        - `config_manager.py`: `config.yml` や `strings.yml` などの設定ファイルを読み込み、プログラム全体で利用できるように管理するモジュールです。
        - `generate_repo_list.py`: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成します。
        - `json_ld_template.json`: 検索エンジン最適化（SEO）のために、構造化データを提供するJSON-LD形式のテンプレートファイルです。
        - `language_info.py`: GitHubリポジトリのプログラミング言語情報を処理し、集計や整形を行うモジュールです。
        - `markdown_generator.py`: 取得・処理されたリポジトリ情報から、Jekyllの要件に合わせたSEO最適化されたMarkdown形式の出力コンテンツ（HTML断片も含む）を生成する主要モジュールです。
        - `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` ファイルから、指定されたセクション（3行の概要）を自動的に抽出・取得するモジュールです。
        - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に加工・整形する役割を担うモジュールです。
        - `seo_template.yml`: 検索エンジン最適化に関連する追加のテンプレート設定やメタ情報を定義するファイルです。
        - `statistics_calculator.py`: リポジトリ数、言語ごとの使用率などの統計情報を計算する機能を提供します。
        - `strings.yml`: プロジェクト内で使用される表示メッセージや各種文言を一元的に管理する設定ファイルです。多言語対応や文言変更を容易にします。
        - `template_processor.py`: MarkdownやJSON-LDなどのテンプレートファイルを読み込み、動的なデータと結合して最終的なコンテンツを生成するモジュールです。
        - `url_utils.py`: URLの生成、解析、検証など、URLに関連するユーティリティ関数を集めたモジュールです。
- **test_project_overview.py**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - `test_config.py`: 設定ファイルの読み込みや管理に関する機能をテストします。
    - `test_environment.py`: プロジェクトが想定する実行環境や依存関係が正しく設定されているかをテストします。
    - `test_integration.py`: 複数のモジュールが連携して動作する際の整合性やエンドツーエンドの機能をテストする統合テストです。
    - `test_markdown_generator.py`: `markdown_generator.py` が正しくMarkdownコンテンツを生成するかをテストします。
    - `test_project_overview_fetcher.py`: `project_overview_fetcher.py` が正しくプロジェクト概要を取得できるかをテストします。
    - `test_repository_processor.py`: `repository_processor.py` がリポジトリ情報を正しく処理・整形できるかをテストします。

## 関数詳細説明
このプロジェクトでは、具体的な関数名やそのシグネチャに関する詳細情報が提供されていません。しかし、各ファイルが担当する役割から、以下のような主要な処理（関数群）が存在すると推測されます。

- `src/generate_repo_list/generate_repo_list.py` における主要処理:
    - GitHub APIへのアクセスとリポジトリ情報の取得。
    - 取得したリポジトリデータのフィルタリング、並べ替え、制限（`--limit`オプションなど）の適用。
    - 他のモジュール（例: `repository_processor`, `project_overview_fetcher`, `markdown_generator`）を呼び出し、全体的な生成フローをオーケストレーション。
    - 最終的なMarkdownファイルとして結果を保存する処理。

- `src/generate_repo_list/repository_processor.py` における主要処理:
    - 生のGitHub APIレスポンスから、必要なリポジトリ情報を抽出・整形し、内部で扱いやすいデータ構造（例: Python辞書）に変換する処理。
    - リポジトリのアクティブ/アーカイブ/フォークといったステータスを判定し、分類する処理。

- `src/generate_repo_list/project_overview_fetcher.py` における主要処理:
    - 指定されたリポジトリパスとファイル名（例: `generated-docs/project-overview.md`）に基づいて、該当ファイルのコンテンツを読み込む処理。
    - ファイルコンテンツ内から特定のセクションタイトル（例: "プロジェクト概要"）を見つけ出し、その直後の指定行数（例: 3行）のテキストを抽出する処理。
    - 取得した概要テキストを整形し、戻り値として提供する処理。API呼び出しのキャッシュやリトライ機構も含む。

- `src/generate_repo_list/markdown_generator.py` における主要処理:
    - 処理済みのリポジトリデータを受け取り、Markdown形式の文字列を生成する処理。
    - リポジトリの各プロパティ（名前、説明、リンク、言語など）を適切なMarkdownシンタックスに変換して埋め込む処理。
    - バッジや分類、SEO最適化のためのJSON-LD（`json_ld_template.json`を利用）などを組み込んだ最終的なコンテンツを構成する処理。

- `src/generate_repo_list/badge_generator.py` における主要処理:
    - リポジトリの言語情報やその他の属性（例: アクティブ、アーカイブ）を受け取り、それに対応するMarkdown形式のバッジ（例: `![Python](https://img.shields.io/badge/Python-...)`）文字列を生成する処理。

## 関数呼び出し階層ツリー
```
提供された情報には、具体的な関数の呼び出し階層ツリーは含まれていません。
「関数呼び出し階層を分析できませんでした」と記載されているため、このセクションは詳細を記述できません。

---
Generated at: 2025-12-22 07:06:17 JST
