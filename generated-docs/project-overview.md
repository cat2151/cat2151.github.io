Last updated: 2026-01-03

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、各リポジトリの概要を抽出します。
- SEOに最適化されたMarkdownファイルを生成し、検索エンジンやLLMからの参照性を高めます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤。MarkdownをHTMLに変換し、ウェブサイトとして公開します。)
- 音楽・オーディオ: (該当する技術は使用されていません。)
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成のロジックを実装しています。), GitHub API (リポジトリ情報の取得元として利用されます。)
- テスト: Pytest (Pythonコードのユニットテストおよび統合テストを行うためのフレームワークです。)
- ビルドツール: (直接的なビルドツールは使用されていませんが、生成されたMarkdownファイルはJekyllによってウェブサイトとしてビルド・公開されます。)
- 言語機能: Python (主要なスクリプト言語), YAML (設定ファイルの記述に使用されます。例: `config.yml`, `strings.yml`), TOML (GitHubトークンなどの秘密情報を設定する際に使用されます。例: `secrets.toml`), Markdown (リポジトリ一覧の出力形式であり、Jekyllによるレンダリング対象です。)
- 自動化・CI/CD: GitHub API (リポジトリ情報の「自動取得」を実現する主要な技術です。本プロジェクト自体はCI/CDを重視しないローカル開発向けに設計されています。)
- 開発標準: Ruff (Pythonコードのフォーマットとリンティングを行い、コードスタイルを統一するためのツールです。)

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
- **`.editorconfig`**: 複数のエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.gitignore`**: Gitのリポジトリでバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法などを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバルな設定を定義するファイルで、サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
- **`assets/`**: ウェブサイトで使用されるファビコン画像やその他の静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるアイコン画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストのために一時的に使用されるPythonスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（特に`project-overview.md`）が一時的に保存される、または参照されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権の確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページとして表示されるMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧のコンテンツが出力されます。
- **`issue-notes/`**: プロジェクトの開発中に発生した課題や検討事項、メモなどを個別のMarkdownファイルとして記録しているディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定やメタデータ（アプリ名、アイコン、表示モードなど）を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの実行設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、ウェブサイトのどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター兼フォーマッターであるRuffの設定を定義するファイルです。
- **`src/__init__.py`**: Pythonが`src`ディレクトリをパッケージとして認識するための初期化ファイルです。
- **`src/generate_repo_list/__init__.py`**: Pythonが`generate_repo_list`ディレクトリをパッケージとして認識するための初期化ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: GitHubリポジトリの言語やステータスを示すバッジ（例: 使用言語、アーカイブ済みなど）を生成するロジックを管理するファイルです。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得機能やAPI呼び出しに関する技術的なパラメータなど、アプリケーションの具体的な設定を定義するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`strings.yml`といった設定ファイルから情報を読み込み、アプリケーション内で利用可能な形式で管理する役割を担うファイルです。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する一連の処理を実行します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データをJSON-LD形式で記述するためのテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理、分析するロジックを含むファイルです。
- **`src/generate_repo_list/markdown_generator.py`**: GitHub APIから取得したリポジトリ情報と設定に基づき、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成するロジックを実装したファイルです。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動的に抽出・取得する機能を提供するファイルです。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを加工し、アプリケーションで利用しやすい形式に整形・フィルタリングするロジックを含むファイルです。
- **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownファイルのメタデータや構造化データに関するSEO設定のテンプレートを定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算し、Markdown生成時に利用するロジックを含むファイルです。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや静的な文言（例: ヘッダー、フッターのテキストなど）を一元的に管理するYAMLファイルです。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレートエンジンとして機能し、取得したデータをテンプレートに埋め込んで最終的な出力を作成するロジックを管理するファイルです。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供するファイルです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の単体テストを行うPythonスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`test_config.py`**: 設定ファイル (`config.yml`など) の読み込みや設定値の整合性をテストするスクリプトです。
    - **`test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係が正しく機能するかをテストするスクリプトです。
    - **`test_integration.py`**: プロジェクトの複数のコンポーネントが連携して正しく動作するかを検証する統合テストスクリプトです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`で実装されたMarkdown生成ロジックが期待通りに動作するかをテストするスクリプトです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`がリポジトリ概要を正しく取得できるかをテストするスクリプトです。
    - **`test_repository_processor.py`**: `repository_processor.py`がGitHub APIから取得したリポジトリデータを正しく処理・整形できるかをテストするスクリプトです。

## 関数詳細説明
提供された情報では、各ファイルの関数の詳細な説明（役割、引数、戻り値、機能）は含まれていません。`googled947dc864c270e07.html`は関数を含まない静的ファイルです。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-03 07:06:19 JST
