Last updated: 2026-11-05

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ情報を自動取得し一覧を生成するシステムです。
- GitHub APIを用いてリポジトリ詳細情報を取得し、SEO最適化されたMarkdownを出力します。
- 検索エンジンやLLMからのリポジトリ参照性を高め、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) は最終的なウェブサイトのレンダリングに使用され、Markdown形式でコンテンツを記述します。`manifest.json`はPWA関連のメタデータを提供します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - GitHub API: リポジトリ情報（説明、スター数、言語など）をプログラムで取得するために使用されます。
    - `ruff`: Pythonコードのフォーマットとスタイルチェックを自動化するリンターです。
    - `pytest`: Pythonコードのテストを記述・実行するためのフレームワークです。
- テスト:
    - `pytest`: Pythonのユニットテスト、統合テスト、機能テストを実行するために使用されます。`pytest.ini`で設定を管理します。
- ビルドツール:
    - Python: リポジトリ情報取得、Markdown生成、ファイル処理といった主要なスクリプトがPythonで記述されています。
- 言語機能:
    - Python: メインのスクリプト言語として利用されています。
    - Markdown: GitHub Pagesのコンテンツ記述フォーマット、およびリポジトリ概要の抽出元フォーマットとして使用されます。
    - YAML: プロジェクトの設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用されます。
    - TOML: 開発設定ファイル (`secrets.toml`, `ruff.toml`) の記述に使用されます。
    - JSON: SEOメタデータテンプレート (`json_ld_template.json`) やPWAマニフェスト (`manifest.json`) に使用されます。
- 自動化・CI/CD:
    - GitHub APIを活用したリポジトリ情報の自動取得、およびMarkdownファイルの自動生成が主な自動化プロセスです。
    - 同一実行内でのキャッシュ機能により、API呼び出しの効率化が図られています。
- 開発標準:
    - `ruff`: コードの品質を維持し、スタイルを統一するために自動修正機能が利用されます。
    - `.editorconfig`: 複数の開発環境でのコードスタイルの一貫性を保つための設定ファイルです。

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
  22.md
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
  conftest.py
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
-   `.editorconfig`: 異なるエディタやIDE間でコードスタイル（インデント、改行コードなど）を統一するための設定ファイル。
-   `.github_automation/check_large_files/check-large-files.toml`: GitHubリポジトリ内の大容量ファイルをチェックするツールの設定。
-   `.github_automation/check_large_files/scripts/check_large_files.py`: 大容量ファイルを検出し、リポジトリの健全性を保つためのPythonスクリプト。
-   `.gitignore`: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイル。
-   `LICENSE`: このプロジェクトがMITライセンスで提供されていることを示すファイル。
-   `README.md`: プロジェクトの目的、機能、使い方、設定方法などが記載されたメインドキュメント。
-   `_config.yml`: Jekyllサイト全体の構成設定を定義するファイル。
-   `assets/favicon-*.png`: ウェブサイトのファビコンとして使用される各種サイズの画像ファイル。
-   `debug_project_overview.py`: `project_overview` 機能の動作確認やデバッグを目的とした補助スクリプト。
-   `generated-docs/`: 他のリポジトリから自動的に取得・生成されたドキュメント（例: 各リポジトリのプロジェクト概要）を格納するディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイル。
-   `index.md`: GitHub PagesサイトのトップページとなるMarkdownファイルで、このプロジェクトによってリポジトリ一覧が生成されて出力されます。
-   `issue-notes/22.md`: プロジェクトの課題や検討事項を記録するためのメモファイル。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などのメタデータを定義します。
-   `pytest.ini`: `pytest` テストフレームワークの動作設定を定義するファイル。
-   `requirements-dev.txt`: 開発およびテスト時に必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、または除外すべきかを指示するファイル。
-   `ruff.toml`: `ruff` リンターのコードスタイルルールや設定を定義するファイル。
-   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
-   `src/generate_repo_list/badge_generator.py`: 各リポジトリに表示する言語、ステータスなどのバッジを生成するロジックを管理します。
-   `src/generate_repo_list/config.yml`: リポジトリ一覧生成の動作設定、特にプロジェクト概要取得機能などの技術的パラメータを定義します。
-   `src/generate_repo_list/config_manager.py`: `config.yml` などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供します。
-   `src/generate_repo_list/date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
-   `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレートを定義します。
-   `src/generate_repo_list/language_info.py`: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つデータを提供するスクリプトです。
-   `src/generate_repo_list/markdown_generator.py`: 処理されたリポジトリ情報に基づいて、SEO最適化されたMarkdownコンテンツを効率的に生成します。
-   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを自動的に取得する機能を提供します。
-   `src/generate_repo_list/readme_badge_extractor.py`: リポジトリのREADMEファイルから、既存のバッジ情報を解析し抽出する機能を提供します。
-   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に処理・整形する主要なロジックを担います。
-   `src/generate_repo_list/seo_template.yml`: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定を定義するファイルです。
-   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
-   `src/generate_repo_list/strings.yml`: プロジェクト内で使用される表示メッセージや各種文言を一元管理するためのファイルです。
-   `src/generate_repo_list/template_processor.py`: Markdown生成の際に、定義されたテンプレートに変数を埋め込むなどの処理を行う機能を提供します。
-   `src/generate_repo_list/url_utils.py`: URLの構築、解析、検証など、URL関連の様々なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview` 機能（各リポジトリから概要を自動取得する機能）のテストスクリプト。
-   `tests/conftest.py`: `pytest` でテストを実行する際に使用される共通のフィクスチャやヘルパー関数を定義するファイル。
-   `tests/test_*.py`: 各機能（バッジ生成、設定、日付フォーマット、Markdown生成、プロジェクト概要取得など）のテストコードを含むファイル群。

## 関数詳細説明
このプロジェクトは複数のPythonスクリプトで構成されており、各ファイルが特定の役割を持つ関数群を提供しています。具体的な関数の引数や戻り値は提供されていませんが、各スクリプトが担う主要な機能は以下の通りです。

-   **`generate_repo_list.py`**:
    -   役割: GitHub APIからリポジトリ情報を取得し、取得したデータを処理して最終的なMarkdown形式のリポジトリ一覧ファイルを生成するメインの実行関数を提供します。
-   **`repository_processor.py`**:
    -   役割: GitHub APIから取得した生のリポジトリデータを受け取り、それをMarkdown生成に適した形式に整形・加工する関数群を提供します。
-   **`project_overview_fetcher.py`**:
    -   役割: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）からプロジェクトの概要文を抽出し、取得する関数群を提供します。
-   **`markdown_generator.py`**:
    -   役割: 処理済みのリポジトリ情報とテンプレートを基に、SEO最適化されたMarkdownコンテンツを構築・出力する関数群を提供します。
-   **`badge_generator.py`**:
    -   役割: リポジトリの言語、アクティブ状態、アーカイブ状態などの情報に基づいて、視覚的なバッジのURLやマークアップを生成する関数群を提供します。
-   **`readme_badge_extractor.py`**:
    -   役割: リポジトリの`README.md`ファイルの内容を解析し、そこに含まれる既存のバッジ情報を抽出する関数群を提供します。
-   **`statistics_calculator.py`**:
    -   役割: リポジトリのスター数、フォーク数、最終更新日といった統計情報を計算・集計し、表示用に整形する関数群を提供します。
-   **`config_manager.py`**:
    -   役割: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、アプリケーション全体で安全かつ一貫した方法で設定値にアクセスするための関数を提供します。
-   **`date_formatter.py`**:
    -   役割: 日付や時刻のデータを、人間が読みやすい特定のフォーマットに変換するユーティリティ関数を提供します。
-   **`language_info.py`**:
    -   役割: プロジェクトで使用されているプログラミング言語に関する情報を処理し、言語バッジの生成や表示順序の決定などに利用する関数を提供します。
-   **`template_processor.py`**:
    -   役割: Markdownのテンプレートファイル内のプレースホルダーに変数を埋め込み、最終的なMarkdownコンテンツを生成する関数を提供します。
-   **`url_utils.py`**:
    -   役割: GitHubリポジトリへのリンクやGitHub PagesのURLなど、URLに関連する操作（構築、検証、エンコードなど）を行うユーティリティ関数を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-05 07:07:22 JST
