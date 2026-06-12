Last updated: 2026-06-13

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジンにクロールされにくいGitHubユーザーページの問題を解決し、SEO最適化されたMarkdownを生成します。
- 各リポジトリの情報を集約し、魅力的で検索可能なリポジトリ紹介ページを構築します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesサイトの基盤としてコンテンツを表示)、**Markdown** (リポジトリ一覧および詳細コンテンツの生成形式)
- 音楽・オーディオ: なし
- 開発ツール: **Python** (主要な開発言語、API連携やファイル生成のロジックを実装)、**GitHub API** (リポジトリ情報の取得元)、**YAML** (設定ファイルやメッセージの定義に利用)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストフレームワーク)
- ビルドツール: **Pythonスクリプト** (GitHub APIから取得したデータに基づいてMarkdownファイルを生成するカスタムビルドプロセス)
- 言語機能: **Python** (オブジェクト指向プログラミング、ファイルI/O、HTTPリクエスト処理など、システムの中核機能の実装に利用)
- 自動化・CI/CD: **なし** (プロジェクトはCI/CD環境を前提とせず、ローカルでの開発と実行を重視しています。ただし、リポジトリ情報の自動取得・生成自体が自動化のコンセプトです)
- 開発標準: **ruff** (Pythonコードのリンティングとフォーマットを自動化し、コード品質と一貫性を保つ)、**.editorconfig** (異なるエディタ間でのコーディングスタイルの一貫性を維持)

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
- **`.editorconfig`**: 異なるエディタやIDE間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/check_large_files/`**: GitHub Actionsを用いて、リポジトリ内の大規模なファイルをチェックするためのスクリプト群です。
    - **`check-large-files.toml`**: 大規模ファイルチェックの設定を定義します。
    - **`scripts/check_large_files.py`**: 実際のファイルサイズチェックロジックを実装したPythonスクリプトです。
- **`.gitignore`**: Gitでバージョン管理しないファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定、クイックテスト方法など、プロジェクト全体の説明を記載した主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定（タイトル、テーマなど）を定義するファイルです。
- **`assets/`**: Jekyllサイトで利用される画像やファビコンなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher` などのプロジェクト概要取得機能のデバッグに利用するスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した `project-overview.md` など、動的に生成されるドキュメントや関連ファイルを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: メインスクリプト (`generate_repo_list.py`) によって生成される、リポジトリ一覧を含むGitHub Pagesサイトのトップページです。
- **`issue-notes/`**: 開発中の課題やメモを記録するためのディレクトリです（例: `22.md` は特定の課題に関するメモ）。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてサイトを定義するための設定ファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージの依存関係をリストアップします。
- **`requirements.txt`**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係をリストアップします。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツール `ruff` の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成のコアロジックを含むPythonパッケージです。
        - **`badge_generator.py`**: リポジトリに関連するバッジ（例: 言語バッジ、ステータスバッジ）のHTML/Markdownを生成するロジックを扱います。
        - **`config.yml`**: リポジトリ概要取得機能など、システム全体の技術的なパラメータを設定します。
        - **`config_manager.py`**: `config.yml` などの設定ファイルを読み込み、管理するためのユーティリティを提供します。
        - **`date_formatter.py`**: リポジトリの最終更新日時などを表示用にフォーマットする機能を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの実行スクリプトです。
        - **`json_ld_template.json`**: SEO強化のためのJSON-LD形式の構造化データテンプレートです。
        - **`language_info.py`**: リポジトリの使用言語に関する情報を処理・整形する機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報から最終的なMarkdownコンテンツを生成するロジックを実装します。
        - **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリの `README.md` から特定のバッジ情報を抽出する機能です。
        - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、必要な情報に整形する主要なビジネスロジックを実装します。
        - **`seo_template.yml`**: SEO関連のメタ情報やテンプレートを定義します。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算する機能を提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元管理するためのファイルです。
        - **`template_processor.py`**: Markdown生成時に利用するテンプレートの読み込みや変数置換などの処理を扱います。
        - **`url_utils.py`**: URLの構築や解析など、URLに関連するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: `pytest` のテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - 他の `test_*.py` ファイルは、それぞれのモジュールや機能に対する具体的なテストケースを実装しています。

## 関数詳細説明
このプロジェクトは複数のPythonファイルで構成されており、それぞれが特定の役割を担う関数群を持っています。以下に主要なファイルとその中の代表的な関数の役割を説明します。具体的な引数や戻り値はコードに依存しますが、一般的な役割を記述します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - `main()`: プログラムのエントリーポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成、ファイル出力までの一連のフローをオーケストレーションします。
        - 引数: `--username` (string), `--output` (string), `--limit` (int)
        - 戻り値: None (ファイル出力を行う)

- **`src/generate_repo_list/repository_processor.py`**:
    - `process_repository(repo_data)`: GitHub APIから取得した個々のリポジトリデータ（JSON形式）を受け取り、表示に必要な整形済みのデータ構造に変換します。プロジェクト概要の取得やバッジ情報の抽出などもこの中で調整されます。
        - 引数: `repo_data` (dict, GitHub APIレスポンスの一部)
        - 戻り値: `processed_repo` (dict, 整形済みのリポジトリ情報)

- **`src/generate_repo_list/markdown_generator.py`**:
    - `generate_markdown(repositories)`: 処理済みリポジトリのリストを受け取り、Jekyllの要件を満たすMarkdown形式の文字列を生成します。
        - 引数: `repositories` (list of dict, 処理済みリポジトリのリスト)
        - 戻り値: `markdown_string` (string, 生成されたMarkdownコンテンツ)

- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - `fetch_project_overview(owner, repo_name, config)`: 指定されたリポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要（3行説明）を非同期に取得します。
        - 引数: `owner` (string), `repo_name` (string), `config` (dict, 設定情報)
        - 戻り値: `overview_text` (string, 抽出されたプロジェクト概要) または None

- **`src/generate_repo_list/config_manager.py`**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (string, 設定ファイルへのパス)
        - 戻り値: `config_data` (dict, 設定内容)

- **`src/generate_repo_list/badge_generator.py`**:
    - `generate_badge_markup(badge_info)`: バッジの情報（名前、URLなど）に基づいて、MarkdownまたはHTML形式のバッジ表示マークアップを生成します。
        - 引数: `badge_info` (dict, バッジのデータ)
        - 戻り値: `badge_markup` (string, 生成されたバッジのマークアップ)

- **`src/generate_repo_list/date_formatter.py`**:
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形します。
        - 引数: `iso_date_string` (string)
        - 戻り値: `formatted_date` (string)

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-06-13 07:35:34 JST
