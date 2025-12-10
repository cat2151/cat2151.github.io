Last updated: 2025-12-11

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、指定されたユーザーのリポジトリ情報を自動で取得します。
- GitHub Pagesサイト向けに、SEOを意識したリポジトリ一覧をMarkdown形式で生成します。
- サイトの検索エンジンからの発見性を高め、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (MarkdownをHTMLに変換する静的サイトジェネレータ), Markdown (ウェブコンテンツ記述言語)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得インターフェース), PyYAML (YAML設定ファイル処理), TOML (設定ファイル形式), argparse (コマンドライン引数解析)
- テスト: pytest (Python用のテスティングフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報を元にMarkdownファイルを動的に生成)
- 言語機能: Python (ファイルI/O、HTTPリクエスト、データ構造処理、文字列操作など、標準ライブラリを活用)
- 自動化・CI/CD: (プロジェクト情報には具体的なCI/CDツールの記載はありませんが、自動生成システムとして運用されます)
- 開発標準: ruff (Pythonコードの高速リンター・フォーマッター), EditorConfig (異なるエディタ間でのコーディングスタイル統一設定)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方、開発者向けのヒントなどが記述された主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの動作に影響を与えます。
- **`assets/`**: サイトで使用される画像、アイコン（favicon）などの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` のデバッグやテストに特化したスクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した `project-overview.md` などの生成済みドキュメントを一時的に格納する、あるいはそのためのプレースホルダーとなるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトによってリポジトリ一覧が生成され、ここに記述されます。
- **`issue-notes/`**: プロジェクト開発中に発生した課題や検討事項に関するメモ（Markdown形式）を格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータや挙動を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonライブラリの一覧を定義したファイルです。
- **`requirements.txt`**: プロジェクトの実行（本番環境）に必要なPythonライブラリの一覧を定義したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターであるRuffの設定ファイルです。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空のファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示す空のファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを管理するファイルです。
- **`src/generate_repo_list/config.yml`**: プロジェクトの動作に関する各種設定（例: プロジェクト概要取得機能の有効/無効、対象ファイル名、タイムアウトなど）を定義するYAML形式の設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` やその他の設定ファイル (`secrets.toml`, `strings.yml`) を読み込み、管理するためのユーティリティを提供するファイルです。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownコンテンツを生成する、このプロジェクトのメインスクリプトです。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD形式) のテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立てるためのロジックを含むファイルです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報と設定に基づいて、SEOに適したMarkdownコンテンツを組み立てる中心的なロジックを担うファイルです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルから、指定された形式のプロジェクト概要（3行説明）を自動的に抽出する機能を提供するファイルです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを担うファイルです。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやコンテンツ構造に関するテンプレート設定を定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供するファイルです。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言を一元的に管理するためのYAMLファイルです（国際化・多言語化に対応）。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成プロセスにおいて、定義されたテンプレートに変数を埋め込むなどの処理を行うファイルです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、正規化など、URLに関連するユーティリティ関数を集めたファイルです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能を検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
- **`tests/test_config.py`**: 設定ファイルの読み込みや管理機能に関するテストを行うファイルです。
- **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテストを行うファイルです。
- **`tests/test_integration.py`**: システムの異なるコンポーネントが連携して正しく動作するかを検証する統合テストファイルです。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py` のロジックが期待通りにMarkdownを生成するかをテストするファイルです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` が正しくプロジェクト概要を抽出できるかをテストするファイルです。
- **`tests/test_repository_processor.py`**: `repository_processor.py` がリポジトリデータを適切に処理するかをテストするファイルです。

## 関数詳細説明
このプロジェクトは複数のPythonファイルで構成されており、各ファイルが特定の機能を提供するために、関連する関数やクラスを定義しています。個別の引数や戻り値の詳細は提供されていませんが、ファイル名からその役割を推測できます。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main`関数: プロジェクト全体の処理フローを制御する主要なエントリポイントです。コマンドライン引数を解析し、他のモジュールの関数を呼び出してリポジトリ情報の取得からMarkdown生成までの一連の処理を実行します。
- **`src/generate_repo_list/badge_generator.py`**:
    - リポジトリの特性（言語、状態など）に基づいたバッジ（アイコン）を生成する関数群を提供します。
- **`src/generate_repo_list/config_manager.py`**:
    - 設定ファイル (`config.yml`, `strings.yml`, `secrets.toml`) の読み込み、解析、および管理を行う関数群を提供します。設定値へのアクセスを抽象化し、一貫した方法で利用できるようにします。
- **`src/generate_repo_list/language_info.py`**:
    - リポジトリの言語情報を取得し、加工するための関数群を提供します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - 処理されたリポジトリデータを受け取り、それを構造化されたMarkdown形式の文字列に変換する関数群を提供します。SEOテンプレートや文字列リソースを活用します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - 各リポジトリから指定された `project-overview.md` ファイルを読み込み、そこからプロジェクトの概要（3行説明）を抽出する関数群を提供します。GitHub API を介してファイル内容を取得します。
- **`src/generate_repo_list/repository_processor.py`**:
    - GitHub APIから取得した生のリポジトリデータ（JSON形式）を、Markdown生成や表示に適した内部データ構造に変換・整形する関数群を提供します。フィルタリングやソートもここで行われる可能性があります。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、レポートや表示に利用するための関数群を提供します。
- **`src/generate_repo_list/template_processor.py`**:
    - YAMLやJSONなどのテンプレートファイルを使用して、動的なコンテンツ生成（例: 変数の埋め込み）を行うための関数群を提供します。
- **`src/generate_repo_list/url_utils.py`**:
    - URLの構築、検証、エンコード・デコードなど、URL操作に関連する汎用的なユーティリティ関数群を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-11 07:06:57 JST
