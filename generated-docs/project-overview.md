Last updated: 2026-01-23

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンからの発見性を高め、LLM連携の効率化に貢献します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤としてマークダウンをHTMLに変換), **Markdown** (本プロジェクトの出力形式であり、Jekyllが処理)
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語および実行環境。
    - **pytest**: Pythonコードのテストフレームワーク。
    - **ruff**: Pythonコードのリンターおよびフォーマッター。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述形式。
    - **TOML**: 設定ファイル (`pytest.ini`, `ruff.toml`, `secrets.toml`) の記述形式。
    - **Git**: ソースコードのバージョン管理システム。
- テスト:
    - **pytest**: Pythonアプリケーションの単体テストおよび結合テストを実行するためのフレームワーク。
- ビルドツール:
    - **Pythonスクリプト**: GitHub APIからの情報取得とMarkdownファイル生成を行う実質的な「ビルド」処理を実行します。
- 言語機能:
    - **Python**: GitHub APIとの連携、データ処理、ファイル操作、Markdown生成など、システムの中核をなすプログラミング言語。
- 自動化・CI/CD:
    - **requirements.txt / requirements-dev.txt**: 依存関係管理により、環境構築の自動化をサポートします。現状はCI/CDを重視せずローカル開発が中心です。
- 開発標準:
    - **ruff**: コードのスタイルチェックと自動修正を行い、コード品質と統一性を保ちます。
    - **.editorconfig**: 複数のエディタ間でインデントスタイルなどのコードフォーマットを統一するための設定ファイル。

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
  16.md
  18.md
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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードのインデントスタイルや文字エンコーディングなどの設定を統一するためのファイル。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイル。ビルド生成物や一時ファイルなどが含まれます。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。プロジェクトの利用条件を明示します。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、機能、設定、クイックテスト実行方法など、プロジェクトに関する包括的な情報を提供する主要なドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の構成設定ファイル。サイトのタイトル、テーマ、プラグインなどのグローバル設定を定義します。
- **`assets/`**: サイトで使用されるファビコンなどの静的アセットを格納するディレクトリ。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるウェブサイトのファビコン画像ファイル。
- **`debug_project_overview.py`**: `project_overview`機能の動作検証やデバッグを目的とした補助スクリプト。
- **`generated-docs/`**: 他のリポジトリから自動取得された`project-overview.md`ファイルなどが一時的または永続的に格納される可能性のあるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
- **`index.md`**: メインのGitHub Pagesコンテンツファイル。本プロジェクトのスクリプトによって、リポジトリ一覧のMarkdownコンテンツがここに生成されます。
- **`issue-notes/`**: 開発中に発生した課題、検討事項、または将来の改善点などを記録するためのMarkdown形式のメモファイル群。
- **`manifest.json`**: Progressive Web App (PWA) の設定ファイル。ウェブサイトをユーザーのホーム画面に追加する際のアイコンや表示方法などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の動作設定ファイル。テストの検出方法やオプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **`requirements.txt`**: プロジェクトの実行に必要な本番環境向けPythonパッケージとそのバージョンを記述したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはクロールすべきでないかを指示するファイル。SEOに影響します。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイル。コードスタイルルールや無視するファイルなどを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧自動生成ロジックが格納されたPythonパッケージ。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの各種情報（言語、ライセンス、スター数など）に基づいて、視覚的なバッジ（SVG/PNGなど）のMarkdownコードを生成する役割を担います。
        - **`src/generate_repo_list/config.yml`**: `generate_repo_list`スクリプトの動作に関する技術的パラメータを設定するファイル。例えば、`project_overview`機能の有効/無効や対象ファイルパスなどを定義します。
        - **`src/generate_repo_list/config_manager.py`**: YAML形式の設定ファイル (`config.yml`, `strings.yml`) を読み込み、設定値へのアクセスを管理するモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマット（例: "YYYY-MM-DD"）に整形するためのユーティリティ関数を提供するモジュール。
        - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdownファイルを生成する一連の処理を制御します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のために、リポジトリ情報を構造化データ (JSON-LD) として記述する際のテンプレートファイル。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語の情報を取得、処理し、表示に適した形式に変換するモジュール。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータやその他の情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを構築する役割を担うモジュール。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル (`generated-docs/project-overview.md`など) から、プロジェクトの3行概要を自動的に抽出し取得するモジュール。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するモジュール。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に加工、フィルタリング、追加情報の付与（例: 概要の取得）を行うモジュール。
        - **`src/generate_repo_list/seo_template.yml`**: サイト全体のSEOメタデータや、Jekyllサイトのフロントマターとして埋め込む情報に関するテンプレートと設定を定義するファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算または集計するモジュール。
        - **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元的に管理するファイル。多言語対応や文言の変更が容易になります。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2など）の処理、データバインディング、レンダリングを担当するモジュール。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能（特にプロジェクト概要の抽出ロジック）に関する単体テストを定義するスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの結合テスト。
    - **`tests/test_config.py`**: `config_manager`モジュールなど、設定ファイルの読み込みと処理に関するテスト。
    - **`tests/test_date_formatter.py`**: `date_formatter`モジュールの日付フォーマット機能に関する単体テスト。
    - **`tests/test_environment.py`**: 開発環境や実行環境のセットアップが正しく行われているかを確認するテスト。
    - **`tests/test_integration.py`**: 主要なコンポーネントが連携して正しく動作するかを確認する、より広範囲な結合テスト。
    - **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールが期待通りにMarkdownコンテンツを生成するかを検証するテスト。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの詳細なテスト。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのテスト。
    - **`tests/test_repository_processor.py`**: `repository_processor`モジュールがリポジトリデータを正しく処理・整形するかを検証するテスト。

## 関数詳細説明
プロジェクト情報から具体的な関数シグネチャは提供されていませんが、各ファイルの役割から主要な機能を担う関数を以下に推測して記述します。

- **`generate_repo_list.py`内のメイン実行関数（例: `main`）**
    - 役割: プログラムのエントリポイントとして、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するまでの一連の処理をオーケストレートします。
    - 引数: `username` (str, GitHubユーザー名), `output` (str, 出力Markdownファイル名), `limit` (int, オプション、処理するリポジトリ数の上限)
    - 戻り値: なし (サイドエフェクトとしてファイル出力を行います)

- **`badge_generator.py`内のバッジ生成関数（例: `generate_badges`）**
    - 役割: 特定のリポジトリ情報に基づき、言語、ライセンス、スター数などの視覚的なバッジを表すMarkdown文字列を生成します。
    - 引数: `repository_data` (dict/object, 処理済みリポジトリのデータ)
    - 戻り値: `str` (生成されたバッジのMarkdown文字列)

- **`config_manager.py`内の設定読み込み関数（例: `load_config`）**
    - 役割: 指定されたYAMLファイルから設定を読み込み、Pythonオブジェクトとして提供します。
    - 引数: `filepath` (str, 設定ファイルのパス)
    - 戻り値: `dict` (読み込まれた設定内容)

- **`date_formatter.py`内の日付フォーマット関数（例: `format_date`）**
    - 役割: `datetime`オブジェクトを指定されたフォーマット文字列に従って整形された日付文字列に変換します。
    - 引数: `datetime_obj` (datetime.datetime, フォーマット対象の日付オブジェクト), `format_str` (str, フォーマット文字列、例: "%Y-%m-%d")
    - 戻り値: `str` (フォーマットされた日付文字列)

- **`markdown_generator.py`内のMarkdown生成関数（例: `generate_markdown`）**
    - 役割: 処理済みのリポジトリデータリストとテンプレート情報を使用して、最終的なリポジトリ一覧のMarkdownコンテンツを構築します。
    - 引数: `repositories_list` (list, 整形されたリポジトリ情報のリスト), `template_context` (dict, テンプレートに渡す追加データ)
    - 戻り値: `str` (生成された完全なMarkdownコンテンツ)

- **`project_overview_fetcher.py`内の概要取得関数（例: `fetch_project_overview`）**
    - 役割: 指定されたGitHubリポジトリから特定のファイル（例: `generated-docs/project-overview.md`）の内容を取得し、そこからプロジェクト概要の3行説明を抽出します。
    - 引数: `repo_full_name` (str, "owner/repo"形式のリポジトリ名), `github_token` (str, GitHub API認証トークン), `config` (dict, 関連設定)
    - 戻り値: `list` (抽出された3行の概要文字列のリスト、または空のリスト)

- **`repository_processor.py`内のリポジトリ処理関数（例: `process_repository_data`）**
    - 役割: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な追加情報（例: プロジェクト概要）を付与し、表示に適した形に整形します。
    - 引数: `raw_repo` (dict, GitHub APIからの生データ), `overview_fetcher` (ProjectOverviewFetcherのインスタンス), `config` (dict, 設定情報)
    - 戻り値: `dict` (整形済みのリポジトリ情報)

- **`url_utils.py`内のURL関連ユーティリティ関数（例: `build_repo_url`）**
    - 役割: リポジトリ名やユーザー名から完全なGitHubリポジトリURLを構築するなど、URL操作に関する補助機能を提供します。
    - 引数: `username` (str), `repo_name` (str)
    - 戻り値: `str` (構築されたURL)

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-23 07:07:09 JST
