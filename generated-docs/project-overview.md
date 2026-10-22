Last updated: 2026-10-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHubリポジトリ情報を自動で取得・処理します。
- 取得した情報から、GitHub Pagesサイト（`<username>.github.io`）向けのSEO最適化されたリポジトリ一覧Markdownファイルを生成します。
- これにより、リポジトリ一覧が検索エンジンにクロールされやすくなり、各リポジトリの発見性やLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド:
  - **Jekyll**: GitHub Pagesの基盤となる静的サイトジェネレータ。生成されたMarkdownファイルがJekyllによってサイトとしてレンダリングされます。
  - **Markdown**: リポジトリ一覧の出力形式。SEO最適化されたコンテンツ構造を提供します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
  - **GitHub API**: リポジトリ名、説明、言語、スター数などのリポジトリ情報をプログラム的に取得するために使用されます。
  - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報の取得、処理、Markdown生成ロジックが実装されています。
  - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に使用され、設定や文言の管理に利用されます。
  - **TOML**: シークレット情報（GitHubトークン）や開発ツール（`ruff.toml`, `check-large-files.toml`）の設定に利用されます。
  - **`.editorconfig`**: 異なる開発環境やエディタ間でのコードスタイルの一貫性を保つための設定ファイルです。
- テスト:
  - **Pytest**: Pythonプロジェクトのテストフレームワーク。単体テスト、統合テストの実行に利用され、コードの品質と信頼性を保証します。
- ビルドツール:
  - **Pythonスクリプト**: `src/generate_repo_list/generate_repo_list.py`がメインのビルドスクリプトとして機能し、リポジトリ情報の取得からMarkdownファイル生成までの一連の処理を実行します。
- 言語機能:
  - **Python**: 高レベルな汎用プログラミング言語。GitHub APIクライアントの実装、データ処理、ファイル操作など、システムの中核をなします。
- 自動化・CI/CD:
  - **GitHub Pages**: 生成されたリポジトリ一覧をホスティングし、公開するためのプラットフォーム。Jekyllと連携して静的サイトをデプロイします。
  - **ローカル開発重視**: CI/CDパイプラインは明示的に設定されていませんが、GitHub Pagesのデプロイ機能により結果が自動的に公開されます。
- 開発標準:
  - **Ruff**: 高速なPythonリンターおよびフォーマッター。`ruff.toml`に基づき、コードの一貫したスタイルと品質を維持します。
  - **MITライセンス**: プロジェクトの公開条件を定義し、利用、改変、再配布を許可します。

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を強制するための設定ファイルです。
- **.github_automation/**: GitHub Actionsや関連する自動化スクリプトを格納するためのディレクトリです。
  - **check_large_files/**: 大容量ファイルに関するチェックを自動化する機能が含まれています。
    - **README.md**: `check_large_files`機能の概要と使用方法を説明するドキュメントです。
    - **check-large-files.toml**: 大容量ファイルチェック機能の設定（例: 許容サイズ、対象ファイルタイプ）を記述するファイルです。
    - **scripts/check_large_files.py**: 指定された設定に基づいてリポジトリ内の大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリ（例: ビルド成果物、一時ファイル、個人設定）を指定するファイルです。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。プロジェクトの利用条件を定めます。
- **README.md**: プロジェクトの全体概要、目的、主な機能、クイックスタートガイド、設定方法、開発者向けのヒントなどをまとめた主要なドキュメントです。
- **_config.yml**: GitHub Pages（Jekyll）サイト全体の構成を設定するファイルです。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
  - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズです。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグや単体動作確認のために使用されるPythonスクリプトです。
- **generated-docs/**: プロジェクト実行中に生成されるドキュメントや一時ファイルを格納するためのディレクトリです。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのWebマスターツールでサイトの所有権を確認するために使用される認証ファイルです。
- **index.md**: `generate_repo_list.py`によって生成されるリポジトリ一覧が書き込まれる主要なMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **issue-notes/**: 開発中の特定の課題や検討事項に関するメモを記録するためのディレクトリです。
  - **22.md**: 特定の課題（おそらくIssue #22）に関する詳細なメモや考察が記述されたMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のWebマニフェストファイルです。アプリの表示名、アイコン、起動モードなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイルです。テストの検出パターンやプラグイン設定などが含まれます。
- **requirements-dev.txt**: 開発環境およびテスト環境でのみ必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コードスタイル規則や整形ルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
  - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
  - **generate_repo_list/**: リポジトリ一覧自動生成機能のコアロジックを格納するサブパッケージです。
    - **__init__.py**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイルです。
    - **badge_generator.py**: リポジトリのステータス（例: アーカイブ、フォーク）や言語などの情報を基に、表示用のバッジを生成するロジックを実装しています。
    - **config.yml**: プロジェクト概要取得機能など、システムの技術的なパラメータを設定するファイルです。
    - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供します。
    - **date_formatter.py**: 日付や時刻の情報を特定のフォーマット（例: `YYYY-MM-DD`）に変換するためのユーティリティ機能です。
    - **generate_repo_list.py**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式で出力ファイルを生成する一連の処理を統括します。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データをJSON-LD形式で出力するためのテンプレートファイルです。
    - **language_info.py**: リポジトリの使用言語に関する情報を処理し、表示に利用できる形式に変換する機能です。
    - **markdown_generator.py**: 取得・処理されたリポジトリ情報から、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成するロジックを実装しています。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの3行概要を自動的に抽出し、取得する機能です。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイル内に記述されているバッジ（例: ビルドステータス、カバレッジ）を解析し、情報を抽出する機能です。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に加工・整形するビジネスロジックを実装しています。
    - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータや構造化データに関するテンプレート設定を記述するファイルです。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するための機能です。
    - **strings.yml**: UIメッセージ、ヘッダー、フッターなど、アプリケーション内で使用される各種表示文言を一元管理するためのファイルです。多言語対応にも利用されます。
    - **template_processor.py**: MarkdownやJekyllのテンプレートを処理し、動的なデータを埋め込んで最終的なコンテンツを生成する機能です。
    - **url_utils.py**: URLの生成、解析、検証など、URL関連の共通ユーティリティ機能を提供します。
- **test_project_overview.py**: `project_overview_fetcher`機能の単体テストを記述したスクリプトです。
- **tests/**: プロジェクトのテストスクリプト群を格納するディレクトリです。
  - **conftest.py**: pytestテストフレームワークの共通フィクスチャ（テストデータやセットアップ/ティアダウン処理）を定義するファイルです。
  - **test_badge_generator_integration.py**: `badge_generator.py`の統合テストを行い、バッジ生成が期待通りに行われるか検証します。
  - **test_check_large_files.py**: `check_large_files.py`スクリプトのテストを行い、大容量ファイル検出機能が正しく動作するか検証します。
  - **test_config.py**: `config_manager.py`のテストを行い、設定ファイルの読み込みや値の取得が正確に行われるか検証します。
  - **test_date_formatter.py**: `date_formatter.py`のテストを行い、日付のフォーマット処理が正しく行われるか検証します。
  - **test_environment.py**: 環境変数や必要なツールが正しく設定されているかを確認するテストです（推測）。
  - **test_integration.py**: プロジェクト全体の主要なフロー（API取得からMarkdown生成まで）の統合テストを行い、システム全体の連携を確認します。
  - **test_markdown_generator.py**: `markdown_generator.py`のテストを行い、生成されるMarkdownの構造と内容が期待通りであるか検証します。
  - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`のテストを行い、プロジェクト概要の抽出機能が正しく動作するか検証します。
  - **test_readme_badge_extractor.py**: `readme_badge_extractor.py`のテストを行い、READMEからのバッジ抽出が正しく行われるか検証します。
  - **test_repository_processor.py**: `repository_processor.py`のテストを行い、リポジトリ情報の整形・処理ロジックが正しく動作するか検証します。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数の役割、引数、戻り値、機能に関する詳細な説明が含まれていません。
そのため、個々の関数について詳細に説明することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-23 07:11:39 JST
