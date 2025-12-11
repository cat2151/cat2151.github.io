Last updated: 2025-12-12

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを自動出力します。
- リポジトリ概要の自動取得、分類表示、Jekyll対応により、検索エンジンからの参照性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)** - 静的サイトジェネレータとしてGitHub Pagesでのホスティングを想定しています。**Markdown** - 生成されるリポジトリ一覧コンテンツの形式です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** - コアリロジックの実装言語として使用されています。**ruff** - Pythonコードのフォーマットとリントを自動で行い、コード品質とスタイルの一貫性を保ちます。**pytest** - Pythonアプリケーションの単体テストおよび結合テストを実行するためのフレームワークです。
- テスト: **pytest** - プロジェクトの各モジュールや機能の正確性を検証するために使用されます。
- ビルドツール: **Pythonスクリプト** - GitHub APIから取得した情報に基づき、最終的なMarkdownファイルを生成する主要な「ビルド」機能を担っています。
- 言語機能: **Python** - プロジェクトのビジネスロジック、データ処理、API連携、ファイル操作など、全ての自動生成処理を記述するために利用されています。
- 自動化・CI/CD: (ローカル開発重視のため、直接的なCI/CDツールとしては言及されていませんが、生成されたファイルはGitHub Pagesを通じて公開されるため、そのデプロイはGitHub Actionsなどの自動化が利用される可能性があります。)
- 開発標準: **.editorconfig** - 異なるIDEやエディタ間でのコードスタイルの一貫性を定義します。**ruff** - Pythonコードのスタイルと品質を自動的に強制し、開発標準を維持します。

## ファイル階層ツリー
```
.editorconfig
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
  2.md
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
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
- **`.gitignore`**: Gitが追跡すべきでないファイルやディレクトリ（一時ファイル、ビルド成果物など）を指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使用方法、機能、開発者向けヒントなどを記述した主要な説明書。
- **`_config.yml`**: Jekyllサイト全体の挙動を制御する設定ファイル。GitHub Pagesサイトのメタデータやテーマ設定などを含む。
- **`assets/`**: GitHub Pagesサイトで使用されるファビコン（アイコン）などの静的アセットを格納するディレクトリ。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるウェブサイトのアイコン。
- **`debug_project_overview.py`**: `project_overview_fetcher.py`モジュールの動作確認やデバッグを目的とした補助スクリプト。
- **`generated-docs/`**: 他のリポジトリから自動取得される「プロジェクト概要」ファイル（例: `project-overview.md`）の想定パス。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権を確認するための認証用HTMLファイル。
- **`index.md`**: このプロジェクトによって生成される主要なMarkdownファイル。最終的にGitHub Pagesサイトのリポジトリ一覧ページとして利用される。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどをMarkdown形式で記録したファイル群。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定情報を提供し、ウェブサイトをよりアプリのように振る舞わせるためのファイル。
- **`pytest.ini`**: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイル。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonライブラリの依存関係リスト。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonライブラリの依存関係リスト。
- **`robots.txt`**: 検索エンジンクローラーに対して、どのページをクロールすべきか、どのページを避けるべきかを指示するためのファイル。
- **`ruff.toml`**: Pythonコードのスタイルチェックおよび自動フォーマットツール`ruff`の設定ファイル。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイル。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ画像を生成するロジックを含むモジュール。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得設定など、本システムの様々な技術的パラメータを定義するYAML形式の設定ファイル。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体でアクセス可能にするための管理モジュール。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、整形して最終的なMarkdownファイルを生成する、本プロジェクトのメイン実行スクリプト。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために利用される構造化データ（JSON-LD形式）のテンプレートファイル。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリから取得されるプログラミング言語に関する情報を処理・整形するロジックを含むモジュール。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータに基づいて、Markdown形式のコンテンツを生成する主要なロジックを含むモジュール。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリに存在する特定のファイル（例: `project-overview.md`）からプロジェクト概要のテキストを抽出する機能を管理するモジュール。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを含むモジュール。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや構造化データに関するテンプレート設定を定義するYAMLファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリ数や言語分布など、様々な統計情報を計算するロジックを含むモジュール。
- **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownファイルやログ出力で使用される、表示メッセージや文言を一元的に管理するYAMLファイル。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成のためのテンプレートファイル（例: Jinja2テンプレート）を読み込み、データに基づいてレンダリングするモジュール。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストを行うスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - `test_config.py`: 設定ファイル（`config.yml`など）の読み込みと動作に関するテストスクリプト。
    - `test_environment.py`: プロジェクトの実行環境（依存関係、設定など）の準備と動作に関するテストスクリプト。
    - `test_integration.py`: 複数のモジュールが連携して動作する際の統合テストスクリプト。
    - `test_markdown_generator.py`: `markdown_generator.py`モジュールのMarkdown生成機能に関するテストスクリプト。
    - `test_project_overview_fetcher.py`: `project_overview_fetcher.py`モジュールのプロジェクト概要取得機能に関するテストスクリプト。
    - `test_repository_processor.py`: `repository_processor.py`モジュールのリポジトリデータ処理機能に関するテストスクリプト。

## 関数詳細説明
提供されたプロジェクト情報からは、各関数の具体的な役割、引数、戻り値、詳細な機能に関する情報が直接的に記述されていませんでした。しかし、各ファイルの役割から、以下のような主要な機能を持つ関数が含まれていると推測されます。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: プログラムのエントリーポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力の各ステップをオーケストレートします。
    - `_get_repositories(username, limit, github_token)`: 指定されたユーザー名でGitHub APIからリポジトリ一覧を取得する関数。
    - `_process_and_generate_markdown(repos_data, config, strings)`: 取得したリポジトリデータを処理し、設定と文言に基づいてMarkdownコンテンツを生成する関数。

- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge_markdown(repo_data)`: リポジトリ情報（言語、スター数など）からバッジのMarkdownスニペットを生成する関数。

- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(filepath)`: 指定されたパスからYAML形式の設定ファイルを読み込む関数。
    - `get_setting(key_path)`: ドット区切りパスで指定された設定値を取得する関数。

- **`src/generate_repo_list/language_info.py`**:
    - `get_top_languages(repo_data)`: リポジトリで使用されている主要なプログラミング言語を特定し、整形する関数。

- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_repo_list_markdown(processed_repos, config, strings)`: 処理済みのリポジトリデータ、設定、文言を基に、完全なリポジトリ一覧のMarkdown文字列を生成する関数。

- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_name, github_token, config)`: 指定されたリポジトリ名と設定に基づき、`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明を抽出し取得する関数。
    - `_parse_overview_markdown(markdown_content, section_title)`: 読み込んだMarkdownコンテンツから、指定されたセクションタイトルの下の概要行を解析して抽出する関数。

- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repository_data(raw_repo_data, config, project_overview_fetcher)`: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出し、整形する関数。この中で`project_overview_fetcher`を使って概要を取得することもあります。

- **`src/generate_repo_list/statistics_calculator.py`**:
    - `calculate_statistics(processed_repos)`: 処理済みリポジトリデータから、リポジトリ総数、言語分布などの統計情報を計算する関数。

- **`src/generate_repo_list/template_processor.py`**:
    - `render_template(template_path, data)`: 指定されたテンプレートファイルにデータを適用し、レンダリング結果（例: Markdown文字列）を返す関数。

- **`src/generate_repo_list/url_utils.py`**:
    - `construct_repo_url(username, repo_name)`: GitHubリポジトリのURLを構築する関数。
    - `sanitize_filename(filename)`: ファイル名として安全な文字列に変換する関数。

## 関数呼び出し階層ツリー
```
提供されたプロジェクト情報からは、関数間の呼び出し階層を特定できませんでした。

---
Generated at: 2025-12-12 07:06:24 JST
