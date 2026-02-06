Last updated: 2026-02-07

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を取得します。
- 取得した情報から、JekyllベースのGitHub Pages用Markdownファイルを自動生成します。
- 検索エンジン最適化(SEO)とLLMによる参照改善を目指し、リポジトリ一覧と各リポジトリへのリンクを提供します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllを利用して静的サイトを構築), Markdown (コンテンツ生成形式), HTML (最終的なウェブページの構成要素)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (主要なスクリプト言語), Pytest (テストフレームワーク), Ruff (コードリンター/フォーマッター), GitHub API (リポジトリ情報取得), YAML (設定ファイル形式)
- テスト: Pytest (Pythonコードの単体テストおよび結合テストに使用)
- ビルドツール: Pythonスクリプト自体がMarkdownファイルを生成するビルドプロセスを担い、Jekyllが生成されたMarkdownから静的サイトを最終的にビルドします。
- 言語機能: Python (バージョン3.xの機能を使用)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリや、言及されている「プロジェクトごとのGitHub Actions管理」から、自動化への意識が見られます)
- 開発標準: Ruff (コードスタイルの一貫性を保つための自動フォーマットとリンティング), .editorconfig (異なるエディタ間でのコーディングスタイルの統一)

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
- **.editorconfig**: 異なるエディタ間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **.github_automation/check_large_files/**: 大容量ファイルのチェックに関連するファイルを格納します。
        - **.github_automation/check_large_files/README.md**: `check_large_files`機能に関する説明を提供します。
        - **.github_automation/check_large_files/check-large-files.toml**: `check_large_files.py`スクリプトの設定を定義します。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出し、管理を支援するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載しています。
- **README.md**: プロジェクトの目的、主要機能、使用方法、開発者向けのヒントなどをまとめた主要なドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成設定ファイルであり、GitHub Pagesのビルド設定を含みます。
- **assets/**: Jekyllサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **assets/favicon-16x16.png**, **assets/favicon-192x192.png**, **assets/favicon-32x32.png**, **assets/favicon-512x512.png**: サイトのアイコンファイルで、異なる解像度に対応しています。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールのデバッグや単体テストを目的として使用されるスクリプトです。
- **generated-docs/**: このプロジェクトが生成するドキュメント、または他のリポジトリから取得した概要などのファイルを格納するために予約されたディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイルです。
- **index.md**: このプロジェクトの主要な出力ファイルです。自動生成されたGitHubリポジトリ一覧のMarkdownコンテンツがここに書き込まれ、GitHub Pagesのメインページとなります。
- **issue-notes/**: 開発中に発生した課題や検討事項をMarkdown形式で記録するディレクトリです。
    - **issue-notes/10.md**, ..., **issue-notes/8.md**: 特定の課題やタスクに関する個別のメモファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示方法や動作を定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの挙動やオプションを定義します。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしています。
- **requirements.txt**: プロジェクトが本番稼働するために最低限必要となるPythonパッケージとそのバージョンをリストアップしています。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonの高速なリンター兼フォーマッターであるRuffの設定ファイルです。コードの品質とスタイルの一貫性を自動的に維持します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すためのファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧生成機能に関連する全てのモジュールを格納するパッケージです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`がPythonパッケージであることを示します。
        - **src/generate_repo_list/badge_generator.py**: リポジトリのステータス（例: `active`, `archived`）や技術スタックを示すバッジ画像を生成または管理するロジックを提供します。
        - **src/generate_repo_list/config.yml**: `generate_repo_list`機能に関する技術的なパラメータ（例: プロジェクト概要取得機能のON/OFF）を定義する設定ファイルです。
        - **src/generate_repo_list/config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するユーティリティモジュールです。
        - **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付や時刻の情報を、人間が読みやすい特定のフォーマットに変換するユーティリティ関数を提供します。
        - **src/generate_repo_list/generate_repo_list.py**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、その情報に基づいてMarkdown形式のリポジトリ一覧を生成します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化(SEO)のために、構造化データ（JSON-LD）のテンプレートを定義するファイルです。
        - **src/generate_repo_list/language_info.py**: GitHubリポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換する機能を提供します。
        - **src/generate_repo_list/markdown_generator.py**: 取得および処理されたリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックをカプセル化します。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要文（3行説明）を自動的に抽出・取得する機能を提供します。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、shields.ioなどのサービスで生成されたバッジの情報を抽出し、解析する機能を提供します。
        - **src/generate_repo_list/repository_processor.py**: 個々のGitHubリポジトリオブジェクトを詳細に処理し、生成するMarkdownコンテンツに必要なデータ構造（例: 名前、説明、URL、スター数など）に変換する役割を担います。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算し、集計する機能を提供します。
        - **src/generate_repo_list/strings.yml**: ユーザーインターフェースに表示されるテキストメッセージ、文言、ラベルなどを一元的に管理する設定ファイルです。多言語対応にも利用できます。
        - **src/generate_repo_list/template_processor.py**: Markdownテンプレートや他のテキストベースのテンプレートを読み込み、動的なデータで埋め込んで最終的なコンテンツを生成する汎用的な機能を提供します。
        - **src/generate_repo_list/url_utils.py**: URLの構築、解析、検証など、URL操作に関連する共通のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能に関する単体テストを記述したスクリプトです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **tests/test_badge_generator_integration.py**: `badge_generator`モジュールの統合的な動作を検証するテストです。
    - **tests/test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストです。
    - **tests/test_config.py**: 設定ファイル（例: `config.yml`）の読み込みや管理機能に関するテストです。
    - **tests/test_date_formatter.py**: `date_formatter`モジュールの機能に関するテストです。
    - **tests/test_environment.py**: プロジェクトの実行環境が正しく設定されているかを検証するテストです。
    - **tests/test_integration.py**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テストです。
    - **tests/test_markdown_generator.py**: `markdown_generator`モジュールの機能に関するテストです。
    - **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールの機能に関するテストです。
    - **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールの機能に関するテストです。
    - **tests/test_repository_processor.py**: `repository_processor`モジュールの機能に関するテストです。

## 関数詳細説明
- **generate_repo_list.py**:
    - `main(username, output_file, limit)`: プロジェクトの主要な実行エントリポイントです。GitHub APIからリポジトリ情報を取得し、処理して、指定された形式のMarkdownファイルに出力する一連の処理を調整します。
        - 引数: `username` (str): GitHubユーザー名, `output_file` (str): 出力ファイルパス, `limit` (int, optional): 処理するリポジトリ数の上限。
        - 戻り値: None
- **repository_processor.py**:
    - `process_repository(repo_data)`: 個々のGitHubリポジトリデータを整形し、Markdown生成に必要な情報（名前、説明、URL、言語、スター数など）を抽出・加工します。
        - 引数: `repo_data` (dict): GitHub APIから取得した生のリポジトリデータ。
        - 戻り値: dict: 整形され、表示に適した形式に変換されたリポジトリ情報。
- **project_overview_fetcher.py**:
    - `fetch_project_overview(repo_full_name, config)`: 指定されたリポジトリから`project-overview.md`ファイルを読み込み、設定に基づいてその中からプロジェクト概要（3行説明）を抽出します。
        - 引数: `repo_full_name` (str): リポジトリのフルネーム (例: `username/reponame`), `config` (dict): `config.yml`から読み込まれた設定情報。
        - 戻り値: list[str]: 抽出された3行の概要説明のリスト。ファイルが存在しない、または抽出できない場合は空のリストを返します。
- **markdown_generator.py**:
    - `generate_repo_markdown(processed_repos, config)`: 処理済みのリポジトリ情報リストと設定に基づいて、最終的なMarkdown形式のリポジトリ一覧コンテンツ全体を生成します。
        - 引数: `processed_repos` (list[dict]): `repository_processor`によって処理されたリポジトリ情報のリスト, `config` (dict): 設定情報。
        - 戻り値: str: 生成されたMarkdownコンテンツの文字列。
- **config_manager.py**:
    - `load_config(config_path)`: 指定されたファイルパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (str): 読み込む設定ファイルのパス。
        - 戻り値: dict: 読み込まれた設定データ。
- **badge_generator.py**:
    - `create_badge_markdown(status, language)`: リポジトリのステータス（例: アクティブ、アーカイブ）や主要なプログラミング言語に基づいたバッジのMarkdown文字列を生成します。
        - 引数: `status` (str): リポジトリのステータス（例: "active", "archived", "fork"), `language` (str, optional): リポジトリの主要プログラミング言語。
        - 戻り値: str: 生成されたバッジのMarkdown文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-02-07 07:06:48 JST
