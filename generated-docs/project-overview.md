Last updated: 2026-02-21

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、自動で整理します。
- GitHub Pagesサイト用にSEOに最適化されたMarkdown形式のリポジトリ一覧を生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として動作し、生成されたMarkdownファイルをレンダリングします)、Markdown (リポジトリ一覧の出力形式であり、JekyllによってWebページに変換されます)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: pytest (Pythonコードのテストフレームワークで、機能の正しさを検証します)、ruff (Pythonコードのリンターおよびフォーマッターで、コードスタイルを統一し品質を維持します)、PyYAML (YAML形式の設定ファイルを読み書きするために使用されます)
- テスト: pytest (Pythonコードの単体テスト、統合テスト、機能テストを実行するためのフレームワークです)
- ビルドツール: Pythonスクリプト (主要なスクリプト言語として、GitHub APIからのデータ取得、Markdown生成、ファイル出力といった一連の処理を実行します)
- 言語機能: Python (プロジェクトの中核となるスクリプト言語であり、データ処理とファイル生成を担います)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリが存在し、将来的な自動化や継続的インテグレーション/デプロイメントの基盤として活用される可能性がありますが、現状はローカル開発が重視されています)
- 開発標準: ruff (コードベース全体で一貫したPythonコーディングスタイルを強制し、可読性と保守性を高めます)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトや関連設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するファイル群です。
        - **README.md**: 大容量ファイルチェック機能に関する説明が記述されています。
        - **check-large-files.toml**: 大容量ファイルチェックの設定パラメータを定義します。
        - **scripts/check_large_files.py**: 大容量ファイルを検出し、プロジェクトの健全性を保つためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトがMITライセンスの下で提供されていることを示すライセンス情報ファイルです。
- **README.md**: プロジェクトの目的、機能、使用方法など、全体的な概要が記述された主要なドキュメントファイルです。
- **_config.yml**: Jekyll (GitHub Pagesの基盤) サイトのグローバル設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのブラウザタブなどに表示されるファビコン（サイトアイコン）の各種サイズです。
- **debug_project_overview.py**: プロジェクト概要自動取得機能の動作をデバッグするためのスクリプトです。
- **generated-docs/**: 自動生成されたドキュメントやコンテンツが格納される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search ConsoleなどのWebマスターツールによるサイト所有権確認のために使用されるファイルです。
- **index.md**: GitHub Pagesサイトのメインページとして公開されるMarkdownファイルで、このプロジェクトによって生成されたリポジトリ一覧が含まれます。
- **issue-notes/**: プロジェクトの課題や検討事項に関するノートがMarkdown形式で格納されているディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の情報を記述するファイルで、アプリのホーム画面アイコンや表示モードなどを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に必要な本番環境用のPythonパッケージとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールすべきか、またはクロールすべきでないかを指示するファイルです。
- **ruff.toml**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルです。
- **src/__init__.py**: Pythonのパッケージを示すための空ファイル、またはパッケージ初期化コードを含むファイルです。
- **src/generate_repo_list/**: リポジトリ一覧自動生成機能の中核となるPythonモジュール群が格納されています。
    - **__init__.py**: `generate_repo_list`サブパッケージを示すためのファイルです。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ画像を生成するロジックを含んでいます。
    - **config.yml**: プロジェクト概要取得機能など、各種機能の技術的なパラメータを設定するYAMLファイルです。
    - **config_manager.py**: YAMLファイルから設定を読み込み、管理するためのモジュールです。
    - **date_formatter.py**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するためのモジュールです。
    - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプトです。
    - **json_ld_template.json**: 検索エンジン最適化（SEO）のために構造化データを埋め込むためのJSON-LDテンプレートファイルです。
    - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示するためのモジュールです。
    - **markdown_generator.py**: 取得したリポジトリ情報から、GitHub Pages用のMarkdownコンテンツを生成するモジュールです。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイルからプロジェクト概要のテキストを自動的に取得するモジュールです。
    - **readme_badge_extractor.py**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するためのモジュールです。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報に変換・整理する中核的なモジュールです。
    - **seo_template.yml**: SEO関連のメタデータやコンテンツの構造を定義するためのテンプレート設定ファイルです。
    - **statistics_calculator.py**: リポジトリに関する様々な統計情報（例: スター数、フォーク数など）を計算するモジュールです。
    - **strings.yml**: プロジェクト内で使用される表示メッセージや文言を一元管理するためのYAMLファイルです。
    - **template_processor.py**: Markdownやその他の形式のテンプレートを読み込み、動的なデータで埋め込むためのモジュールです。
    - **url_utils.py**: URLの検証、構築、パースなど、URLに関連するユーティリティ関数を集めたモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールが正しく動作するかを検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストを実行するスクリプトです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストスクリプトです。
    - **test_config.py**: 設定ファイルの読み込みと解析に関するテストスクリプトです。
    - **test_date_formatter.py**: 日付整形機能のテストスクリプトです。
    - **test_environment.py**: 開発・実行環境の設定に関するテストスクリプトです。
    - **test_integration.py**: プロジェクト全体の主要な機能の統合テストを実行するスクリプトです。
    - **test_markdown_generator.py**: Markdown生成機能のテストスクリプトです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストスクリプトです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能のテストスクリプトです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストスクリプトです。

## 関数詳細説明
提供された情報からは個々の関数の詳細な役割、引数、戻り値を特定できませんでした。主要な機能は`src/generate_repo_list/generate_repo_list.py`スクリプトを通じて実行され、その内部で他のモジュール内の関数が連携して動作すると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-21 07:07:17 JST
