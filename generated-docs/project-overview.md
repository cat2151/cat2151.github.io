Last updated: 2026-01-20

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 生成されたコンテンツは`github.io`ドメインで公開され、検索エンジン最適化（SEO）とLLMからの参照性向上を目指します。
- リポジトリの分類表示、バッジ、各プロジェクト概要の自動取得など、豊富な表示機能を提供します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesで使用される静的サイトジェネレータで、生成されたMarkdownファイルをHTMLサイトとして公開します。
    - **Markdown**: 生成されるリポジトリ一覧ページのコンテンツ形式です。
    - **JSON-LD**: SEOを強化するための構造化データで、`json_ld_template.json`を介して出力に含められます。
- 音楽・オーディオ:
    - 該当する技術は確認されませんでした。
- 開発ツール:
    - **Python**: リポジトリ情報の取得、処理、Markdown生成を行う主要なスクリプト言語です。
    - **pytest**: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
    - **ruff**: Pythonコードの高速なリンターおよびフォーマッターで、コード品質とスタイルの一貫性を保ちます。
    - **Git/GitHub**: バージョン管理システムおよびリポジトリホスティングサービスとして使用され、GitHub APIを通じてリポジトリ情報を取得します。
- テスト:
    - **pytest**: Pythonベースのテストフレームワークとして、`test_*.py`ファイル群で各モジュールの機能検証に使用されます。
- ビルドツール:
    - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py` を中心とするPythonスクリプト群が、GitHub APIからデータを取得し、最終的なMarkdownファイルを「ビルド」します。
    - **Jekyll (GitHub Pages)**: 生成されたMarkdownファイルはGitHub PagesによってJekyll経由でウェブサイトとして公開されます。
- 言語機能:
    - **Python**: プロジェクトの主要な実装言語です。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）で、柔軟な設定とメッセージ管理を可能にします。
    - **TOML**: 設定ファイル（`ruff.toml`, `pytest.ini`）や、GitHubトークンなどの機密情報管理（`secrets/secrets.toml`）に使用されます。
- 自動化・CI/CD:
    - このプロジェクト自体には明示的なCI/CDパイプラインは設定されておらず、「CI/CD不要のローカル開発重視の構成」とされています。ただし、生成されるリポジトリ概要ではGitHub Actionsに関する言及があります。
- 開発標準:
    - **ruff**: コードスタイルの一貫性を強制し、潜在的なエラーを検出するためのリンター/フォーマッターとして導入されています。
    - **.editorconfig**: 複数の開発者やエディタ間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一します。

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
- **.editorconfig**: さまざまなエディタやIDE間でコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、実行方法、設定オプションなどを記述した主要なドキュメント。
- **_config.yml**: Jekyll静的サイトジェネレータのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどを定義します。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリ。
    - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: サイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の各種サイズ。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールのデバッグを目的としたスクリプト。
- **generated-docs/**: 他のリポジトリから自動取得された`project-overview.md`などのドキュメントを一時的に格納する、または参照するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py`スクリプトによってリポジトリ一覧が自動生成され、サイトのトップページとして機能するMarkdownファイル。
- **issue-notes/**: 開発過程で発生した課題や検討事項をメモとして残すMarkdownファイルのコレクション。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、アプリのメタデータ（名前、アイコン、表示モードなど）を定義するファイル。
- **pytest.ini**: pytestテストフレームワークの動作を設定するためのファイル。テスト検出パターンやレポート形式などを指定します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイル。
- **requirements.txt**: 本番環境（この場合はスクリプトの実行環境）でプロジェクトが必要とするPythonパッケージとそのバージョンを列挙したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイル。
- **ruff.toml**: Ruffリンター/フォーマッターの動作を設定するファイル。コードスタイルルール、無視するファイル、検出するエラーなどを定義します。
- **src/**: プロジェクトの主要なPythonソースコードを格納するルートディレクトリ。
    - **__init__.py**: `src`ディレクトリをPythonパッケージとして識別するためのファイル。
    - **generate_repo_list/**: リポジトリ一覧生成機能に関連するモジュール群をまとめたPythonパッケージ。
        - **__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するためのファイル。
        - **badge_generator.py**: リポジトリのステータスや技術を示すバッジの生成、または既存のバッジ処理に関するロジックを実装します。
        - **config.yml**: プロジェクトの実行時に使用される設定パラメータ（GitHub API関連、プロジェクト概要取得設定など）を定義するYAMLファイル。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プログラム全体で利用できるように管理するモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付データを整形し、表示に適した形式に変換するユーティリティ関数を提供します。
        - **generate_repo_list.py**: プロジェクトのエントリーポイントとなるメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために出力されるJSON-LD形式の構造化データのテンプレート。
        - **language_info.py**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、整形する機能を提供します。
        - **markdown_generator.py**: 取得および処理されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツを生成するロジックを実装します。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出するモジュール。
        - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、特定のバッジ（ステータスバッジなど）の情報を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整形する主要な処理ロジックを担います。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイル。
        - **statistics_calculator.py**: 各リポジトリのスター数、フォーク数などの統計情報を計算・集計するモジュール。
        - **strings.yml**: プログラム内で使用される各種メッセージや表示文言を外部化し、一元管理するためのYAMLファイル。
        - **template_processor.py**: Markdown生成時に使用されるテンプレートの読み込み、データ結合、最終出力を行うモジュール。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能に関する単体テストを記述したスクリプト。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **test_badge_generator_integration.py**: バッジ生成機能の結合テストを記述したファイル。
    - **test_config.py**: 設定ファイルの読み込みや管理機能に関するテストを記述したファイル。
    - **test_date_formatter.py**: 日付フォーマットユーティリティのテストを記述したファイル。
    - **test_environment.py**: プロジェクトの実行環境に関する設定や依存関係のテストを記述したファイル。
    - **test_integration.py**: プロジェクトの主要機能間の連携を検証する結合テストを記述したファイル。
    - **test_markdown_generator.py**: Markdown生成モジュールの機能テストを記述したファイル。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストを記述したファイル。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストを記述したファイル。
    - **test_repository_processor.py**: リポジトリ情報処理モジュールの機能テストを記述したファイル。

## 関数詳細説明
提供された情報からは、プロジェクト内の具体的なPython関数の詳細（役割、引数、戻り値など）を特定できませんでした。各ファイルが特定の機能を持つモジュールとして設計されているため、それぞれのファイル名からその役割を推測することはできますが、具体的な実装レベルの情報は含まれていません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-01-20 07:06:38 JST
