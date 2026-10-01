Last updated: 2026-10-02

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- 取得した情報からGitHub Pages向けにSEO最適化されたリポジトリ一覧を生成します。
- これにより、検索エンジンでの発見性を高め、LLMによる参照失敗を緩和します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、MarkdownファイルをHTMLに変換して公開します), Markdown (生成されるリポジトリ一覧ページの記述形式です)
- 音楽・オーディオ: 該当なし
- 開発ツール: GitHub API (リポジトリ情報の取得に使用します), PyYAML (設定ファイル `config.yml` や `strings.yml` の読み書きに利用されます), argparse (コマンドライン引数 `--username` などの解析に使用されます), requests (GitHub APIとのHTTP通信に利用されることが想定されます)
- テスト: pytest (Pythonコードの単体テストおよび結合テストフレームワークとして利用されます)
- ビルドツール: Pythonスクリプト (リポジトリ一覧をMarkdown形式で自動生成する主要なツールです)
- 言語機能: Python (プロジェクトの主要な開発言語です)
- 自動化・CI/CD: Pythonスクリプトによる自動生成 (本プロジェクトはローカルでのスクリプト実行による自動生成を重視しており、継続的インテグレーション/デリバリー機能は直接提供しません)
- 開発標準: Ruff (Pythonコードのフォーマットとリンティングを行い、コード品質と一貫性を保ちます), EditorConfig (異なるエディタ間でのコーディングスタイルを統一するための設定ファイルです)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **.github_automation/**: GitHubに関連する自動化スクリプトや設定を格納するディレクトリです。
    - **.github_automation/check_large_files/**: 大容量ファイルをチェックするための機能を含むディレクトリです。
        - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明ドキュメントです。
        - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（一時ファイル、ビルド成果物、設定ファイルなど）を指定するファイルです。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **README.md**: プロジェクトの概要、目的、使い方、インストール手順、開発者向け情報などを説明するメインドキュメントです。
- **_config.yml**: Jekyll (GitHub Pages) のサイト全体の設定を定義するファイルです。テーマ、パーマリンク構造などが設定されます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **assets/favicon-16x16.png**: 16x16ピクセルのファビコン画像です。
    - **assets/favicon-192x192.png**: 192x192ピクセルのファビコン画像です。
    - **assets/favicon-32x32.png**: 32x32ピクセルのファビコン画像です。
    - **assets/favicon-512x512.png**: 512x512ピクセルのファビコン画像です。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグやテスト実行に使用される補助スクリプトです。
- **generated-docs/**: リポジトリから自動取得されたプロジェクト概要ファイルなどが一時的に保存されたり、生成されたりするディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでのサイト所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧メインページ（トップページ）となるMarkdownファイルです。
- **issue-notes/**: 開発中の課題や調査結果、メモなどを記録するためのディレクトリです。
    - **issue-notes/22.md**: 特定の課題に関するノートファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの情報を含みます。
- **pytest.ini**: pytestフレームワークの挙動をカスタマイズするための設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonライブラリとバージョンを記述したファイルです。
- **requirements.txt**: プロジェクトの実行に必要なPythonライブラリとバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、または避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンティング（構文チェック、スタイルガイド違反検出）とフォーマットを行うRuffツールの設定ファイルです。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **src/__init__.py**: Pythonパッケージであることを示す空ファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧生成機能に関連する全てのPythonモジュールを格納するパッケージディレクトリです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list` がPythonパッケージであることを示す空ファイルです。
        - **src/generate_repo_list/badge_generator.py**: リポジトリのバッジ（状態、言語などを示すアイコン）を生成するロジックを扱います。
        - **src/generate_repo_list/config.yml**: プロジェクト概要取得機能などの技術的パラメータを設定するためのYAMLファイルです。
        - **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`など）の読み込みと管理を行うモジュールです。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティモジュールです。
        - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力するメインの実行スクリプトです。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化(SEO)のためのJSON-LD形式の構造化データテンプレートです。
        - **src/generate_repo_list/language_info.py**: リポジトリが使用するプログラミング言語に関する情報を処理するモジュールです。
        - **src/generate_repo_list/markdown_generator.py**: 取得したデータに基づいて最終的なMarkdownファイルを生成するロジックを扱います。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出・取得するモジュールです。
        - **src/generate_repo_list/readme_badge_extractor.py**: READMEファイルからバッジ情報（例: ビルド状態、カバレッジなど）を抽出するモジュールです。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、整形するためのロジックを扱います。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレートを定義するYAMLファイルです。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリに関する様々な統計情報（スター数、フォーク数など）を計算するモジュールです。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージや文言を管理するためのYAMLファイルです。
        - **src/generate_repo_list/template_processor.py**: Markdown生成に使用されるテンプレートファイルの読み込みとデータへの適用を行うモジュールです。
        - **src/generate_repo_list/url_utils.py**: URLの検証、整形、生成などのユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: プロジェクト概要取得機能の単体テストや統合テストを含むファイルです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **tests/conftest.py**: pytestのフィクスチャ（テスト実行前に準備される共通データや設定）を定義するファイルです。
    - **tests/test_badge_generator_integration.py**: バッジ生成機能の統合テストを行うファイルです。
    - **tests/test_check_large_files.py**: 大容量ファイルチェック機能のテストを行うファイルです。
    - **tests/test_config.py**: 設定ファイル（`config.yml`など）の読み込みや設定値のテストを行うファイルです。
    - **tests/test_date_formatter.py**: 日付フォーマットユーティリティのテストを行うファイルです。
    - **tests/test_environment.py**: 実行環境に関するテスト（必要な依存関係の確認など）を行うファイルです。
    - **tests/test_integration.py**: プロジェクト全体の主要なフローに関する統合テストを行うファイルです。
    - **tests/test_markdown_generator.py**: Markdown生成機能のテストを行うファイルです。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストを行うファイルです。
    - **tests/test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストを行うファイルです。
    - **tests/test_repository_processor.py**: リポジトリデータ処理機能のテストを行うファイルです。

## 関数詳細説明
提供された情報に個々の関数の詳細な役割、引数、戻り値の記述がないため、ファイルごとの主要な機能を提供する関数群として説明します。

- **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや特性を示すバッジ（アイコン）を生成するロジックをカプセル化する関数群です。
- **src/generate_repo_list/config_manager.py**: YAML形式の設定ファイル (`config.yml`, `strings.yml`) を読み込み、設定値にアクセスするための関数群を提供します。
- **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付データを、人間が読みやすい形式や指定された形式に変換するためのユーティリティ関数群です。
- **src/generate_repo_list/generate_repo_list.py**: このプロジェクトの主要なエントリーポイントとなるスクリプトで、GitHub APIからのデータ取得、データ処理、Markdown生成といった一連の処理をオーケストレートする関数群を含みます。
- **src/generate_repo_list/language_info.py**: リポジトリの主要言語やその他の言語関連情報を取得・処理するための関数群です。
- **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報を受け取り、JekyllベースのGitHub Pagesで表示されるMarkdown形式のコンテンツを生成する関数群です。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内に存在する `generated-docs/project-overview.md` ファイルから、指定されたセクションの3行のプロジェクト概要を抽出・取得するための関数群です。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のステータスバッジ（例: ビルド状況、テストカバレッジ）のURLや情報を検出・抽出するための関数群です。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、Markdown生成に適した内部データ構造に変換・整形する関数群です。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計するための関数群です。
- **src/generate_repo_list/template_processor.py**: Markdown生成の際に使用されるテンプレートファイル (`json_ld_template.json`, `seo_template.yml` など) を読み込み、動的なデータで埋め込んで最終コンテンツを生成する関数群です。
- **src/generate_repo_list/url_utils.py**: URLの構造解析、相対パスから絶対パスへの変換、有効性チェックなど、URLに関連する様々なユーティリティ関数群を提供します。
- **.github_automation/check_large_files/scripts/check_large_files.py**: 定義されたルールに基づいて、リポジトリ内の大容量ファイルを検出・報告するための関数群です。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールの動作を確認するためのテスト実行やデバッグ支援の関数群です。
- **test_project_overview.py**: `project_overview_fetcher` の機能が正しく動作するかを検証するテストケースを提供する関数群です。
- **tests/conftest.py**: pytestのテスト実行時に使用される共通のフィクスチャ（テストデータやヘルパー関数など）を定義する関数群です。
- **tests/test_badge_generator_integration.py**: `badge_generator` モジュールが他のコンポーネントと正しく連携するかを検証する統合テストケースの関数群です。
- **tests/test_check_large_files.py**: 大容量ファイルチェック機能の正確性と堅牢性を検証するテストケースの関数群です。
- **tests/test_config.py**: 設定ファイルの読み込み、パース、および設定値の有効性を検証するテストケースの関数群です。
- **tests/test_date_formatter.py**: 日付フォーマットユーティリティが各種入力に対して期待される出力を行うかを検証するテストケースの関数群です。
- **tests/test_environment.py**: プロジェクトの実行に必要な環境設定や依存関係が正しく準備されているかを検証するテストケースの関数群です。
- **tests/test_integration.py**: プロジェクト全体の主要なワークフローがエンドツーエンドで正しく動作するかを検証する統合テストケースの関数群です。
- **tests/test_markdown_generator.py**: Markdown生成機能が様々なデータ入力に対して正しいMarkdownコンテンツを生成するかを検証するテストケースの関数群です。
- **tests/test_project_overview_fetcher.py**: プロジェクト概要抽出機能が `project-overview.md` から正しく情報を取得できるかを検証するテストケースの関数群です。
- **tests/test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能が正しく動作するかを検証するテストケースの関数群です。
- **tests/test_repository_processor.py**: リポジトリデータ処理機能がGitHub APIからの生データを正確に変換・整形できるかを検証するテストケースの関数群です。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-02 07:12:54 JST
