Last updated: 2025-12-14

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、個人のリポジトリ情報を自動で取得・整理するシステムです。
- GitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧をMarkdown形式で自動生成します。
- 各リポジトリの概要文も自動抽出し、視覚的で網羅的なポートフォリオページを実現します。

## 技術スタック
- フロントエンド: **Jekyll, GitHub Pages**: GitHub Pagesをホスティング基盤とし、静的サイトジェネレーターであるJekyllを用いてMarkdownファイルをHTMLに変換し、ウェブサイトとして公開します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python**: リポジトリ情報の取得、処理、Markdown生成の主要なスクリプト言語として使用されています。**GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために利用されます。
- テスト: **pytest**: Pythonコードの単体テストや統合テストを実行するためのフレームワークです。
- ビルドツール: **Pythonスクリプト**: リポジトリ情報の取得とMarkdown生成のロジックを実装しています。**Jekyll**: GitHub Pages上でサイトをビルドし、公開する役割を担います。
- 言語機能: **Python**: リポジトリ情報の取得、解析、Markdown生成のための中心的なプログラミング言語です。
- 自動化・CI/CD: **GitHub Pages**: Jekyllを用いた静的サイトのデプロイとホスティングを自動化します。
- 開発標準: **ruff**: Pythonコードのスタイルチェック（Linter）と自動フォーマットを行うツールで、コード品質と一貫性を保ちます。

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
- **README.md**: プロジェクトの目的、機能、使用方法、設定、開発者向けの情報などを説明する主要なドキュメント。
- **LICENSE**: プロジェクトがMITライセンスの下で公開されていることを示すファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイル。
- **.editorconfig**: 異なるエディタやIDE間で、コーディングスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイル。
- **_config.yml**: Jekyllサイト全体の共通設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどの設定を含む。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    - **favicon-*.png**: Webサイトのブラウザタブやブックマークに表示されるアイコン。
- **debug_project_overview.py**: `project_overview`機能の動作をデバッグするための補助スクリプト。
- **generated-docs/**: 他のリポジトリから取得した`project-overview.md`などのドキュメントが一時的に格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどの検索エンジン向けウェブマスターツールで、サイトの所有権を確認するために使用される認証ファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。自動生成されたリポジトリ一覧のコンテンツが出力される。
- **issue-notes/**: プロジェクト開発中に発生した課題や検討事項をMarkdown形式で記録・管理するためのディレクトリ。
- **manifest.json**: プログレッシブウェブアプリ（PWA）として動作させるための設定ファイル。アイコンや表示モードなどを定義。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの実行方法やオプションを定義。
- **requirements.txt**: プロジェクトの実行に必要なPythonライブラリとそのバージョンをリストアップしたファイル（本番環境用）。
- **requirements-dev.txt**: 開発時やテスト実行時にのみ必要なPythonライブラリとそのバージョンをリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **ruff.toml**: Pythonコードの整形と品質チェックを行う`ruff`ツールの設定ファイル。コーディングスタイルルールを定義。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **generate_repo_list/**: リポジトリ一覧自動生成システムのコアロジックを含むPythonパッケージ。
        - **__init__.py**: Pythonパッケージの初期化ファイル。
        - **badge_generator.py**: リポジトリのプログラミング言語やステータスを示すバッジ（アイコン）を生成する機能。
        - **config.yml**: リポジトリ一覧生成スクリプトの動作を設定するためのYAMLファイル。GitHub APIのタイムアウトやキャッシュ設定など。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プログラム全体で利用できるように管理するモジュール。
        - **generate_repo_list.py**: メインの実行スクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdownを生成する一連の処理を統括。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義したファイル。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換する機能。
        - **markdown_generator.py**: 処理されたリポジトリ情報を受け取り、最終的なMarkdown形式の出力コンテンツを生成する機能。
        - **project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で取得する機能。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、プログラム内で扱いやすいオブジェクトに変換する機能。
        - **seo_template.yml**: サイトのSEO関連メタデータやテンプレート構造を定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのコミット数や言語使用割合などの統計情報を計算する機能。
        - **strings.yml**: UIに表示される様々なメッセージや文言を一元管理するためのYAMLファイル。多言語対応や文言変更を容易にする。
        - **template_processor.py**: Markdown生成時に使用するテンプレート（JekyllのLiquidなど）を処理し、動的なコンテンツを埋め込む機能。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連の共通ユーティリティ関数を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher`モジュールのテストコード。
- **tests/**: プロジェクトのテストコード全体を格納するディレクトリ。
    - **test_config.py**: 設定ファイルの読み込みや有効性に関するテスト。
    - **test_environment.py**: プロジェクトの実行環境や依存関係の整合性を確認するテスト。
    - **test_integration.py**: 複数のモジュールが連携して正しく機能するかを確認する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator`モジュールが正しくMarkdownコンテンツを生成するかを確認するテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが正しく概要を取得できるかを確認するテスト。
    - **test_repository_processor.py**: `repository_processor`モジュールがリポジトリ情報を正しく処理するかを確認するテスト。

## 関数詳細説明
提供された情報からは、プロジェクト全体の具体的な関数名、引数、戻り値、機能の詳細な説明を生成できませんでした。しかし、ソースコードのファイル名から、以下のような役割を持つ関数群が存在すると推測されます。
- `generate_repo_list.py`内のメイン処理を制御する関数
- `repository_processor.py`内でGitHub APIから取得したリポジトリデータを処理・整形する関数
- `project_overview_fetcher.py`内で特定ファイルからプロジェクト概要を抽出する関数
- `markdown_generator.py`内で整形されたデータからMarkdownコンテンツを生成する関数
- `badge_generator.py`内でリポジトリのバッジを生成する関数

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-14 07:05:48 JST
