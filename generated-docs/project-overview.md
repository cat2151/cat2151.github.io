Last updated: 2026-03-30

# Project Overview

## プロジェクト概要
- GitHub Pages向けにGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、SEOに最適化されたMarkdownファイルを自動作成します。
- リポジトリの概要やバッジを表示し、検索エンジンからの発見性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレーターとして利用), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (Pythonのテストフレームワーク), ruff (Pythonの高速リンター/フォーマッター), GitHub Actions (自動化スクリプトの実行環境、`.github_automation`ディレクトリの存在から推測)
- テスト: pytest (Pythonコードのユニットテストおよび統合テストに使用)
- ビルドツール: Python (スクリプト実行環境), YAML (設定ファイル管理), JSON (構造化データテンプレート)
- 言語機能: Python (主要な開発言語として使用)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリに定義された自動化スクリプトを実行する可能性)
- 開発標準: ruff (コードスタイルチェックと自動修正), .editorconfig (エディタ間のコードスタイル統一設定)

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
- **`.editorconfig`**: コードエディタの設定を統一し、異なる開発環境間での一貫性を保つためのファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリです。
  - **`check_large_files/README.md`**: `check_large_files`機能に関する説明ドキュメントです。
  - **`check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイルです。
  - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法などを説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成を設定するファイルです。
- **`assets/`**: ウェブサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動生成されたドキュメント（プロジェクト概要など）を配置するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が出力されるMarkdownファイルです。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記録したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定や情報を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonライブラリの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットを行うruffツールの設定ファイルです。
- **`src/`**: プロジェクトのソースコードを格納するディレクトリです。
  - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを格納するパッケージです。
    - **`__init__.py`**: `generate_repo_list`パッケージであることを示すファイルです。
    - **`badge_generator.py`**: リポジトリのステータスや技術に応じたバッジ画像を生成するロジックを扱います。
    - **`config.yml`**: プロジェクト概要取得機能などのシステム設定を定義するYAMLファイルです。
    - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するロジックを扱います。
    - **`date_formatter.py`**: 日付や時刻の表示形式を整形するロジックを扱います。
    - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
    - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレートです。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理するロジックを扱います。
    - **`markdown_generator.py`**: 取得した情報を元に、最終的なMarkdownコンテンツを生成するロジックを扱います。
    - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出するロジックを扱います。
    - **`readme_badge_extractor.py`**: READMEファイルから既存のバッジ情報を抽出するロジックを扱います。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報を抽出するロジックを扱います。
    - **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するロジックを扱います。
    - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するYAMLファイルです。
    - **`template_processor.py`**: Markdown生成などで使用されるテンプレートファイルの処理を行うロジックを扱います。
    - **`url_utils.py`**: URLの生成や解析など、URL関連のユーティリティ関数を扱います。
- **`test_project_overview.py`**: `project_overview_fetcher`機能のユニットテストや統合テストを含むファイルです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
  - **`conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義するファイルです。
  - **`test_badge_generator_integration.py`**: `badge_generator`の統合テストです。
  - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
  - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストです。
  - **`test_date_formatter.py`**: 日付整形機能のテストです。
  - **`test_environment.py`**: 実行環境の設定に関するテストです。
  - **`test_integration.py`**: システム全体の主要な統合テストです。
  - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
  - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
  - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群から構成されており、各ファイルは特定の役割を果たす関数やクラスメソッドを含んでいます。具体的な引数や戻り値は提供されていませんが、ファイル名から推測される主要な機能は以下の通りです。

- **`src/generate_repo_list/generate_repo_list.py`内の関数**:
    - **役割**: GitHub APIからリポジトリ情報を取得し、取得したデータを処理して、最終的なMarkdown形式のリポジトリ一覧ファイルを生成する一連の流れをオーケストレーションします。
- **`src/generate_repo_list/badge_generator.py`内の関数**:
    - **役割**: リポジトリの言語、ステータス（アーカイブ、フォークなど）、その他の特性に基づいて、表示用のバッジ（例: Shield.io形式）のURLやMarkdownを生成します。
- **`src/generate_repo_list/config_manager.py`内の関数**:
    - **役割**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、設定値へのアクセスを提供し、設定の検証やデフォルト値の設定を行います。
- **`src/generate_repo_list/date_formatter.py`内の関数**:
    - **役割**: GitHub APIから取得した日付文字列を、人間が読みやすい形式や特定のロケールに合わせた形式に整形します。
- **`src/generate_repo_list/markdown_generator.py`内の関数**:
    - **役割**: 処理されたリポジトリ情報とテンプレート（`seo_template.yml`、`json_ld_template.json`など）に基づいて、HTMLやMarkdown形式のコンテンツを組み立てて出力します。
- **`src/generate_repo_list/project_overview_fetcher.py`内の関数**:
    - **役割**: 各リポジトリ内の`generated-docs/project-overview.md`ファイルを読み込み、設定されたセクションタイトル（例: "## プロジェクト概要"）から指定された行数の概要テキストを抽出します。
- **`src/generate_repo_list/repository_processor.py`内の関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を受け取り、必要な情報（名前、説明、URL、スター数、言語など）を抽出し、プログラム内で扱いやすいデータ構造に変換します。
- **`src/generate_repo_list/statistics_calculator.py`内の関数**:
    - **役割**: リポジトリデータのリストから、総スター数、使用言語の割合など、集計的な統計情報を計算します。
- **`src/generate_repo_list/template_processor.py`内の関数**:
    - **役割**: 指定されたテンプレートファイル（Jinja2などのテンプレートエンジンを使用している可能性）を読み込み、データモデルを適用して最終的な文字列をレンダリングします。
- **`src/generate_repo_list/url_utils.py`内の関数**:
    - **役割**: GitHubリポジトリのURL、GitHub PagesのURL、APIエンドポイントなど、URLに関連する操作（生成、検証、パースなど）を行います。
- **`.github_automation/check_large_files/scripts/check_large_files.py`内の関数**:
    - **役割**: Gitリポジトリをスキャンし、`.github_automation/check_large_files/check-large-files.toml`で定義された基準に基づいて大容量のファイルを特定し、報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-30 07:09:33 JST
