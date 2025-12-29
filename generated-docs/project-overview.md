Last updated: 2025-12-30

# Project Overview

## プロジェクト概要
- GitHub PagesサイトにGitHubリポジトリ一覧を自動生成し、Web上での可視性を高めるシステムです。
- GitHub APIからリポジトリ情報を取得し、SEO最適化されたJekyll対応のマークダウンファイルを出力します。
- 検索エンジンやLLMからの参照性を向上させ、プロジェクト内容の発見を容易にすることを目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの構築フレームワークとして、生成されたMarkdownファイルを表示), Markdown (リポジトリ一覧の出力形式)
- 音楽・オーディオ: (このプロジェクトでは該当する技術を使用していません)
- 開発ツール: GitHub API (リポジトリ情報を取得するためのインターフェース), Git (プロジェクトのバージョン管理), YAML (設定ファイル管理), TOML (設定ファイル管理)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得とMarkdownファイル生成を行う主要な実行環境)
- 言語機能: Python (プロジェクトの主要な開発言語)
- 自動化・CI/CD: (このシステムはGitHub APIを利用してリポジトリ情報の取得を自動化しますが、プロジェクト自体のCI/CDはローカル開発重視です)
- 開発標準: ruff (Pythonコードのリンティングおよびフォーマットツール)

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
- **.editorconfig**: 異なるエディタやIDE間でコードスタイルの一貫性を保つための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されています。これにより、他のユーザーがどのようにコードを使用、配布、変更できるかが示されます。
- **README.md**: プロジェクトの概要、目的、主な機能、開発者向けのヒント、クイックテスト方法、設定、コマンド例、ライセンス情報などが含まれる、プロジェクトの主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。GitHub Pagesの設定などに利用されます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズと解像度で提供されるファビコン画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールからプロジェクト概要を取得する機能をデバッグするためのスクリプトです。
- **generated-docs/**: 他のリポジトリから取得した`project-overview.md`ファイルが一時的に格納される、または生成されたドキュメントが配置される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用される認証ファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、GitHubリポジトリ一覧のメインページとなるMarkdownファイルです。
- **issue-notes/**: 開発中に見つかった課題や将来の改善点に関するメモを記録したMarkdownファイルが格納されているディレクトリです。
    - **10.md**, **12.md**, **14.md**, **2.md**, **4.md**, **6.md**, **8.md**: 個別の課題やメモを記録したファイルです。
- **manifest.json**: Progressive Web App (PWA) のマニフェストファイルで、Webサイトをモバイルアプリのようにインストールするための情報を提供します。
- **pytest.ini**: `pytest`フレームワークのテスト実行に関する設定を定義するファイルです。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- **ruff.toml**: `ruff`（Pythonの高速なリンター・フォーマッター）の設定ファイルで、コードスタイルや品質に関するルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: `src`ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成するメインロジックを含むPythonサブパッケージです。
        - **__init__.py**: `generate_repo_list`ディレクトリをPythonサブパッケージとして識別するためのファイルです。
        - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを実装しています。
        - **config.yml**: プロジェクト概要取得機能などの技術的パラメータや設定を定義するYAMLファイルです。
        - **config_manager.py**: 設定ファイル（例: `config.yml`, `strings.yml`）の読み込みと管理を行うモジュールです。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成するメインの実行スクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ (`JSON-LD`) のテンプレートファイルです。
        - **language_info.py**: GitHubリポジトリから取得したプログラミング言語の使用状況などの情報を処理するロジックを実装しています。
        - **markdown_generator.py**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するモジュールです。
        - **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動的に取得する機能を担当します。
        - **repository_processor.py**: GitHub APIからリポジトリ情報を取得し、そのデータを整形・処理する主要なロジックを実装しています。
        - **seo_template.yml**: 検索エンジン最適化に関するテンプレート設定を定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリに関する様々な統計情報（例：スター数、フォーク数）を計算するロジックを実装しています。
        - **strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を一元管理するためのYAMLファイルです。
        - **template_processor.py**: Markdown生成のためのテンプレートファイルの読み込み、変数置換などの処理を行うモジュールです。
        - **url_utils.py**: URLの構築、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能に関する単体テストを記述したファイルです。
- **tests/**: プロジェクトの様々なコンポーネントに対するテストスクリプトが格納されているディレクトリです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを記述しています。
    - **test_environment.py**: テスト実行環境の設定や依存関係に関するテストを記述しています。
    - **test_integration.py**: プロジェクトの複数のコンポーネントが連携して正しく動作するかを確認する統合テストを記述しています。
    - **test_markdown_generator.py**: `markdown_generator.py`モジュールが正しいMarkdownコンテンツを生成するかをテストします。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`モジュールが正しくプロジェクト概要を取得できるかをテストします。
    - **test_repository_processor.py**: `repository_processor.py`モジュールがリポジトリ情報を正しく処理できるかをテストします。

## 関数詳細説明
このプロジェクトの詳細な関数情報（引数、戻り値、具体的な機能説明）は提供されていません。そのため、個々の関数の詳細な説明はできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-30 07:06:10 JST
