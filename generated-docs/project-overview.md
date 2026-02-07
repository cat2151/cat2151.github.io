Last updated: 2026-02-08

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で収集・整理します。
- JekyllベースのGitHub Pagesサイト向けに、SEOを意識したリポジトリ一覧を生成します。
- 検索エンジンからの参照性を高め、LLMによるリポジトリ情報の利用を支援します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesサイトの静的サイトジェネレーターとして利用され、生成されたMarkdownファイルを基にウェブサイトを構築します。
    - **Markdown**: リポジトリ一覧のコンテンツ生成に用いられ、JekyllによってHTMLに変換されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語として、GitHub APIからの情報取得やMarkdown生成ロジックの実装に使用されます。
    - **pytest**: Pythonコードの単体テストおよび結合テストを行うためのフレームワークです。
    - **ruff**: Pythonコードの静的解析（Linter）とフォーマット（Formatter）を行い、コード品質とスタイルの一貫性を保ちます。
- テスト:
    - **pytest**: Pythonコードの正確性と安定性を保証するためのテストフレームワークです。
- ビルドツール:
    - **Jekyll**: 生成されたMarkdownファイルを基に、GitHub Pagesサイトを構築するための静的サイトジェネレーターです。
    - **Pythonスクリプト**: GitHub APIからデータを取得し、Markdownファイルを生成するプロセス自体がビルドの一部を構成します。
- 言語機能:
    - **Python**: データ処理、API連携、ファイル操作など、システムの中核となるロジックの実装に活用されます。
- 自動化・CI/CD:
    - **GitHub API**: リポジトリ情報の自動取得に利用され、システムの中核的な自動化を支えます。
    - **GitHub Pages**: 生成されたウェブサイトをホスティングし、公開プロセスを自動化します。
    - **`.github_automation`ディレクトリ**: 将来的なGitHub Actionsやその他の自動化スクリプトのためのプレースホルダーとして機能します（現状はローカル開発重視）。
- 開発標準:
    - **ruff**: コードスタイルと品質を自動的にチェックし、統一されたコーディング規約を強制します。
    - **.editorconfig**: 複数のエディタやIDE間で基本的なコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  18.md
  2.md
  20.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 複数のエディタやIDEでコードスタイル（インデント、文字コードなど）の一貫性を保つための設定ファイルです。
- **.github_automation/**: GitHub上での自動化処理（例: GitHub Actions）に関連するスクリプトや設定を格納するディレクトリです。
    - **.github_automation/check_large_files/**: 大容量ファイルを検出・管理するための機能に関連するディレクトリです。
        - **.github_automation/check_large_files/README.md**: `check_large_files`機能に関する説明が記述されたドキュメントです。
        - **.github_automation/check_large_files/check-large-files.toml**: `check_large_files`機能の設定を定義するファイルです。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 大容量ファイルをチェックするPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトのライセンス（MITライセンス）情報が記載されています。
- **README.md**: プロジェクトの目的、機能、使用方法、開発者向け情報などが記述された、プロジェクトのメインドキュメントです。
- **_config.yml**: JekyllによるGitHub Pagesサイトの全体設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像やアイコンなどの静的アセットを格納するディレクトリです。
    - **assets/favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイル群です。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグやテストを目的としたスクリプトです。
- **generated-docs/**: 何らかのプロセスによって生成されたドキュメントやデータが一時的に格納される可能性のあるディレクトリです。プロジェクト概要取得機能のターゲットファイルパスとして利用されます。
- **googled947dc864c270e07.html**: Google Search ConsoleによるWebサイトの所有権確認に使用されるファイルです。このファイルには関数は含まれていません。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このファイルにリポジトリ一覧が自動生成されます。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを記録したMarkdownファイル群です。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示モードなど）を定義するファイルです。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **requirements.txt**: プロジェクトの本番稼働に必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどのページをクロールしてよいか、またはクロールしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターであるruffの設定ファイルです。コードスタイルの一貫性を保ちます。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **src/__init__.py**: Pythonパッケージとして`src`ディレクトリを識別するために必要です（通常は空か、パッケージレベルの初期化コードを含みます）。
    - **src/generate_repo_list/**: GitHubリポジトリ一覧を生成する主要なロジックがまとめられたPythonパッケージです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するために必要です。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの各種バッジ（例: 言語、ライセンス、スター数など）を生成するロジックを扱います。
        - **src/generate_repo_list/config.yml**: `generate_repo_list`機能の動作を制御する技術的なパラメータ（例: プロジェクト概要取得機能のON/OFF、タイムアウト設定）を定義するファイルです。
        - **src/generate_repo_list/config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻のフォーマットに関するユーティリティ関数を提供します。
        - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイル（リポジトリ一覧）を生成する処理を統括します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートファイルです。
        - **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・整形するロジックを扱います。
        - **src/generate_repo_list/markdown_generator.py**: GitHub APIから取得したデータに基づいて、Markdown形式のコンテンツを生成するロジックを提供します。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で取得するロジックを扱います。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報を抽出するロジックを提供します。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に整形するロジックを扱います。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化（SEO）に関連するテンプレート設定を定義するファイルです。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算するロジックを提供します。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージや文言、ラベルなどを一元的に管理するための設定ファイルです。
        - **src/generate_repo_list/template_processor.py**: Jekyllのテンプレート処理や、Markdown生成時に動的なコンテンツを埋め込むためのロジックを提供します。
        - **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関するユーティリティ関数を提供します。
- **test_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher.py`）の単体テストスクリプトです。
- **tests/**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **tests/test_badge_generator_integration.py**: バッジ生成機能の統合テストを行うスクリプトです。
    - **tests/test_check_large_files.py**: 大容量ファイルチェック機能のテストスクリプトです。
    - **tests/test_config.py**: 設定ファイル管理機能（`config_manager.py`）のテストスクリプトです。
    - **tests/test_date_formatter.py**: 日付フォーマット機能（`date_formatter.py`）のテストスクリプトです。
    - **tests/test_environment.py**: 実行環境の設定や依存関係に関するテストスクリプトです。
    - **tests/test_integration.py**: システム全体の主要なフローに関する統合テストスクリプトです。
    - **tests/test_markdown_generator.py**: Markdown生成機能（`markdown_generator.py`）のテストスクリプトです。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能（`project_overview_fetcher.py`）のテストスクリプトです。
    - **tests/test_readme_badge_extractor.py**: READMEからのバッジ抽出機能（`readme_badge_extractor.py`）のテストスクリプトです。
    - **tests/test_repository_processor.py**: リポジトリ情報処理機能（`repository_processor.py`）のテストスクリプトです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値の詳細を特定することはできませんでした。
しかしながら、上記の「ファイル詳細説明」で述べた各Pythonファイル（モジュール）には、それぞれの役割を果たす主要な関数群が含まれています。例えば、`src/generate_repo_list/generate_repo_list.py`にはメインのエントリーポイントとなる関数、`src/generate_repo_list/project_overview_fetcher.py`にはプロジェクト概要を取得する関数などが存在すると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-08 07:07:44 JST
