Last updated: 2026-02-14

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHubリポジトリ情報を自動で取得します。
- 取得した情報から、SEOに最適化されたMarkdown形式のリポジトリ一覧ページを生成します。
- GitHub Pagesサイトにデプロイすることで、検索エンジンやLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターであり、生成されたMarkdownファイルをHTMLサイトに変換・公開する基盤を提供します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python - プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成ロジックの実装に使用されます。YAML - 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に使用されます。TOML - 設定ファイル（`ruff.toml`, `pytest.ini`）やシークレットファイル（`secrets.toml`）の記述に使用されます。Markdown - GitHub Pagesサイトのコンテンツ（リポジトリ一覧ページ）の出力形式です。
- テスト: pytest - Pythonコードのユニットテストおよび統合テストを実行するためのテストフレームワークです。
- ビルドツール: Pythonスクリプト - GitHub APIからのデータ取得、その加工、および最終的なMarkdownファイルの生成という一連の処理を実行する主要な「ビルド」ツールとして機能します。
- 言語機能: Python - プロジェクトのほぼすべてのロジックがこの言語で実装されています。
- 自動化・CI/CD: GitHub API - リポジトリ情報の自動取得を実現するための主要なインターフェースです。Pythonスクリプト - 定期的な実行や手動実行により、リポジトリ一覧の自動更新を可能にする自動化の役割を果たします。
- 開発標準: ruff - Pythonコードの静的解析ツールであり、コードスタイルの一貫性を保ち、潜在的な問題を検出するために使用されます。

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
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

*   **.editorconfig**: コーディングスタイル（インデント、改行コードなど）を定義し、複数のエディタやIDE間で一貫性を保つための設定ファイルです。
*   **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプト群を格納するディレクトリです。
    *   **check_large_files/**: 大容量ファイルのチェックに関連する自動化処理を格納します。
        *   **README.md**: `check_large_files`機能の概要と使用方法を説明するドキュメントです。
        *   **check-large-files.toml**: 大容量ファイルチェックの設定（例：閾値、除外パス）を定義するTOML形式の設定ファイルです。
        *   **scripts/check_large_files.py**: 指定されたリポジトリ内で容量の大きいファイルを検出するためのPythonスクリプトです。
*   **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリ（例：一時ファイル、ビルド成果物、ローカル設定）をリストアップするファイルです。
*   **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すファイルです。
*   **README.md**: プロジェクトの目的、機能、セットアップ方法、使用例、ライセンス情報などを記述したメインのドキュメントです。
*   **_config.yml**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの基本的な情報を含みます。
*   **assets/**: GitHub Pagesサイトで利用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    *   **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（ウェブサイトのアイコン）の各サイズ画像です。
*   **debug_project_overview.py**: `project_overview_fetcher`モジュールなどの、プロジェクト概要取得機能のデバッグや単体テストを支援するためのスクリプトです。
*   **generated-docs/**: GitHubリポジトリから取得した`project-overview.md`など、外部から取得または自動生成されたドキュメントを格納するプレースホルダディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイルです。
*   **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧をまとめたメインのMarkdownファイルです。このファイルがGitHub Pagesのトップページとして表示されます。
*   **issue-notes/**: 開発中に検討された課題や決定事項、将来の計画に関するメモをMarkdown形式で記録したディレクトリです。
*   **manifest.json**: Webアプリケーションマニフェストファイルで、プログレッシブウェブアプリ（PWA）としてサイトをインストールするための情報（アプリ名、アイコン、テーマカラーなど）を定義します。
*   **pytest.ini**: `pytest`テストフレームワークの挙動を設定するファイルです（例：テスト検出パターン、プラグイン設定）。
*   **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
*   **requirements.txt**: プロジェクトの実行時に最低限必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
*   **robots.txt**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、またはクロールしてはいけないかを指示するファイルです。
*   **ruff.toml**: Pythonコードのスタイルチェックツール`ruff`の設定ファイルです。コードの整形ルールやlintingの規則を定義します。
*   **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    *   **__init__.py**: Pythonパッケージであることを示す空ファイルです。
    *   **generate_repo_list/**: GitHubリポジトリ一覧生成の主要なロジックを構成するモジュール群を格納するPythonパッケージです。
        *   **__init__.py**: `generate_repo_list`パッケージであることを示します。
        *   **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（例：ビルドステータス、ライセンス）を生成するロジックを扱います。
        *   **config.yml**: リポジトリ一覧生成スクリプトの技術的な設定パラメータ（例：プロジェクト概要取得の有効/無効、タイムアウト時間）を定義するYAMLファイルです。
        *   **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、設定値を管理・提供するモジュールです。
        *   **date_formatter.py**: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数を提供します。
        *   **generate_repo_list.py**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdown形式のリポジトリ一覧を生成します。
        *   **json_ld_template.json**: SEO最適化のために、JSON-LD形式で構造化データを埋め込むためのテンプレートファイルです。
        *   **language_info.py**: GitHubリポジトリのプログラミング言語に関する情報を解析・処理するモジュールです。
        *   **markdown_generator.py**: 取得・加工されたリポジトリデータから、最終的なMarkdownコンテンツ（リポジトリ一覧）を生成するコアロジックを実装しています。
        *   **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得するモジュールです。
        *   **readme_badge_extractor.py**: 各リポジトリのREADMEファイルから特定のパターン（例：ステータスバッジ）を抽出し、利用するモジュールです。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に整形・フィルタリングする処理を担います。
        *   **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート構造に関する設定を定義するYAMLファイルです。
        *   **statistics_calculator.py**: リポジトリに関する様々な統計情報（例：スター数、フォーク数、最終更新日時）を計算するモジュールです。
        *   **strings.yml**: UIに表示されるメッセージ、文言、ラベルなどを一元的に管理するYAMLファイルです。多言語対応や文言変更を容易にします。
        *   **template_processor.py**: Markdown生成のためのテンプレートエンジン機能を提供し、変数置換や条件分岐などを用いて柔軟なコンテンツ生成を可能にします。
        *   **url_utils.py**: URLの解析、生成、検証など、URLに関連するユーティリティ関数を集めたモジュールです。
*   **test_project_overview.py**: `project_overview_fetcher`モジュールで実装されているプロジェクト概要取得機能に特化したテストスクリプトです。
*   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    *   **test_badge_generator_integration.py**: `badge_generator`モジュールの機能が他のシステムと正しく連携するかを確認する統合テストです。
    *   **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストケースを格納します。
    *   **test_config.py**: `config_manager`モジュールや各種設定ファイルの読み込み、パース、値の取得に関するテストです。
    *   **test_date_formatter.py**: `date_formatter`モジュールの日付フォーマット機能が期待通りに動作するかを検証します。
    *   **test_environment.py**: プロジェクトの実行環境（依存関係、設定など）が正しくセットアップされているかを確認するテストです。
    *   **test_integration.py**: `generate_repo_list.py`の主要なエンドツーエンドのフローや、複数のモジュールが連携する際の動作を検証する統合テストです。
    *   **test_markdown_generator.py**: `markdown_generator`モジュールが正しくMarkdownコンテンツを生成するかを検証します。
    *   **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが正しくプロジェクト概要を抽出できるかを検証します。
    *   **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEから正しくバッジ情報を抽出できるかを検証します。
    *   **test_repository_processor.py**: `repository_processor`モジュールがGitHub APIから取得したリポジトリ情報を正しく整形・加工できるかを検証します。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数の具体的な役割、引数、戻り値に関する詳細な記述がありませんでした。そのため、個別の関数について詳細な説明を生成することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-14 07:11:52 JST
