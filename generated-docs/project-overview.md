Last updated: 2026-10-03

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で収集・整理します。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照の精度向上を支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターで、GitHub Pagesの基盤として利用され、生成されたMarkdownファイルを美しいウェブサイトとして公開します。
- 音楽・オーディオ: 該当なし - このプロジェクトでは音楽やオーディオ関連の技術は使用していません。
- 開発ツール:
    - pytest: Pythonのテストフレームワークで、効率的なテスト記述と実行を可能にします。
    - Ruff: Pythonの高速なLinterおよびFormatterで、コードの品質と一貫性を自動的に保ちます。
    - GitHub API: GitHubのリポジトリ情報やユーザー情報をプログラムから取得するための公式APIです。
- テスト: pytest - Pythonコードのユニットテスト、統合テスト、機能テストに利用され、コードの品質と信頼性を保証します。
- ビルドツール: Pythonスクリプト - リポジトリ情報の取得からMarkdown生成までの一連の処理をPythonスクリプトが担い、ウェブサイトのコンテンツを構築します。
- 言語機能: Python - プロジェクトの主要な開発言語であり、GitHub APIとの連携やMarkdown生成ロジックの実装に使用されます。
- 自動化・CI/CD: GitHub Actions (示唆) - プロジェクト自身がGitHub Actionsで動くというより、本システムが生成するMarkdownを通じて、各リポジトリのGitHub Actions活用を支援する意図が見られます。
- 開発標準: Ruff - `ruff.toml` ファイルを通じて、プロジェクト全体のPythonコードスタイルと品質基準を定義し、自動的に適用します。

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
-   `.editorconfig`: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどのコードフォーマットを統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    -   `.github_automation/check_large_files/`: 大容量ファイルのチェックに関する機能のディレクトリです。
        -   `.github_automation/check_large_files/README.md`: 大容量ファイルチェック機能の説明ドキュメントです。
        -   `.github_automation/check_large_files/check-large-files.toml`: 大容量ファイルチェックのルールや設定を定義するTOMLファイルです。
        -   `.github_automation/check_large_files/scripts/check_large_files.py`: 指定された基準を超える大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです（例: ログファイル、一時ファイル、依存関係のインストールディレクトリ）。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの概要、目的、インストール方法、使い方、設定、貢献方法などを説明する主要なドキュメントです。
-   `_config.yml`: Jekyllサイト全体の挙動を設定するためのファイルです（例: テーマ、プラグイン、パーマリンク構造）。
-   `assets/`: GitHub Pagesサイトで使用される静的リソース（画像、ファビコン、CSS、JavaScriptなど）を格納するディレクトリです。
    -   `assets/favicon-*.png`: サイトのファビコン（ウェブサイトのアイコン）ファイル群です。
-   `debug_project_overview.py`: `project_overview_fetcher` モジュールのデバッグや単体テストを行うための補助スクリプトです。
-   `generated-docs/`: 他のリポジトリから自動取得されたドキュメント（例: プロジェクト概要）を一時的に保存するディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
-   `index.md`: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧コンテンツが書き込まれます。
-   `issue-notes/`: 課題や開発に関するメモを格納するディレクトリです。
    -   `issue-notes/22.md`: 特定の課題（Issue #22など）に関する詳細なメモや考察を記述したファイルです。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの挙動を定義します。
-   `pytest.ini`: pytestテストフレームワークのグローバル設定ファイルで、テストの発見方法やオプションなどを指定します。
-   `requirements-dev.txt`: 開発環境やテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `requirements.txt`: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をインデックスするか、どの部分を避けるかを指示するファイルです。
-   `ruff.toml`: Ruff Linter/Formatterの詳細な設定を定義するTOMLファイルで、コードスタイルルールや無視するファイルなどを指定します。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   `src/__init__.py`: `src` ディレクトリをPythonパッケージとして認識させるための空ファイルです。
    -   `src/generate_repo_list/`: GitHubリポジトリ一覧生成システムのメインパッケージです。
        -   `src/generate_repo_list/__init__.py`: `generate_repo_list` ディレクトリをPythonサブパッケージとして認識させるための空ファイルです。
        -   `src/generate_repo_list/badge_generator.py`: リポジトリのプログラミング言語やステータスなどのバッジ画像を生成または参照するためのロジックを含むモジュールです。
        -   `src/generate_repo_list/config.yml`: リポジトリ情報取得やMarkdown生成に関する技術的なパラメータ（例: プロジェクト概要取得の有効化、キャッシュ設定）を定義する設定ファイルです。
        -   `src/generate_repo_list/config_manager.py`: `config.yml` や外部の秘密情報 (`secrets.toml`) などの設定ファイルを読み込み、管理するためのモジュールです。
        -   `src/generate_repo_list/date_formatter.py`: 日付や時刻のフォーマットを統一的に処理するためのユーティリティモジュールです。
        -   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理全体を制御します。
        -   `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレートファイルです。
        -   `src/generate_repo_list/language_info.py`: リポジトリのプログラミング言語に関する統計や表示情報を処理するためのモジュールです。
        -   `src/generate_repo_list/markdown_generator.py`: 取得したリポジトリ情報に基づいて、SEOに最適化されたMarkdownコンテンツを生成するロジックをカプセル化したモジュールです。
        -   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で抽出し取得するモジュールです。
        -   `src/generate_repo_list/readme_badge_extractor.py`: リポジトリのREADMEファイルから既存のバッジ情報（例: ビルドステータスバッジ）を解析・抽出するためのモジュールです。
        -   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報を抽出・変換する処理を行うモジュールです。
        -   `src/generate_repo_list/seo_template.yml`: サイト全体のSEO設定やメタデータに関するテンプレートを定義するYAMLファイルです。
        -   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、レポートするためのモジュールです。
        -   `src/generate_repo_list/strings.yml`: UIの表示メッセージ、説明文、ラベルなど、ユーザーに見せるためのすべてのテキスト文字列を一元的に管理する設定ファイルです。
        -   `src/generate_repo_list/template_processor.py`: Markdown生成の際に使用されるテンプレートファイル（例: Jinja2テンプレート）を読み込み、データと組み合わせて最終的なテキストをレンダリングするモジュールです。
        -   `src/generate_repo_list/url_utils.py`: GitHub APIのエンドポイントやリポジトリのURLなど、URL関連の構築や処理を行うユーティリティ関数を集めたモジュールです。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールに関するテストコードを含むファイルです。
-   `tests/`: プロジェクトの各種テストスクリプトを格納するディレクトリです。
    -   `tests/conftest.py`: pytestのフィクスチャやプラグイン、ヘルパー関数などを定義し、複数のテストファイルで共有するためのファイルです。
    -   `tests/test_badge_generator_integration.py`: `badge_generator` モジュールの統合テストを行うファイルです。
    -   `tests/test_check_large_files.py`: 大容量ファイルチェック (`.github_automation/check_large_files/scripts/check_large_files.py`) 機能のテストを行うファイルです。
    -   `tests/test_config.py`: 設定ファイル (`config.yml`, `secrets.toml`) の読み込みや管理に関するテストを行うファイルです。
    -   `tests/test_date_formatter.py`: `date_formatter` モジュールの日付フォーマット機能に関するテストを行うファイルです。
    -   `tests/test_environment.py`: プロジェクトの実行環境が適切に設定されているかを確認するテストを行うファイルです。
    -   `tests/test_integration.py`: システム全体の主要なフロー（GitHub API連携からMarkdown生成まで）を検証する統合テストを行うファイルです。
    -   `tests/test_markdown_generator.py`: `markdown_generator` モジュールのMarkdown生成ロジックに関するテストを行うファイルです。
    -   `tests/test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールが正しくプロジェクト概要を抽出できるかをテストするファイルです。
    -   `tests/test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールがREADMEからバッジ情報を正確に抽出できるかをテストするファイルです。
    -   `tests/test_repository_processor.py`: `repository_processor` モジュールがGitHubリポジトリデータを適切に処理・整形できるかをテストするファイルです。

## 関数詳細説明
提供された情報からは具体的な関数の引数や戻り値の詳細は分析できませんでしたが、ファイル名とプロジェクトの機能から各関数の役割を推測して説明します。

-   **`src/generate_repo_list/badge_generator.py`**
    -   役割: リポジトリの属性（例: 言語、ステータス）に基づいたバッジのMarkdownまたはURLを生成します。
-   **`src/generate_repo_list/config_manager.py`**
    -   役割: YAML設定ファイルや秘密情報ファイル（例: GitHubトークン）を読み込み、設定値を管理します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   役割: 日付や時刻の情報を指定された形式の文字列に変換し、表示用に整形します。
-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()` 関数（エントリーポイント）: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、各モジュールを連携させてMarkdownコンテンツを生成し、指定されたファイルに出力する一連の処理を統括します。
-   **`src/generate_repo_list/language_info.py`**
    -   役割: リポジトリのプログラミング言語に関する詳細情報（例: 使用率、色）を処理し、提供します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   役割: 処理されたリポジトリ情報とテンプレートを使用して、個々のリポジトリや全体のリポジトリ一覧をMarkdown形式で記述します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   役割: 指定されたGitHubリポジトリ内の特定のパスにあるファイル（例: `project-overview.md`）からプロジェクトの3行概要をHTTPリクエストで取得し、抽出します。
-   **`src/generate_repo_list/readme_badge_extractor.py`**
    -   役割: リポジトリのREADMEファイルの内容を解析し、そこに埋め込まれている既存のバッジ（例: Shield.io形式のバッジ）の情報を抽出します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   役割: GitHub APIから取得した生のリポジトリデータを、表示に適した形式に加工・整形し、必要な情報を抽出します。
-   **`src/generate_repo_list/statistics_calculator.py`**
    -   役割: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、集計します。
-   **`src/generate_repo_list/template_processor.py`**
    -   役割: Markdown生成に使用するテンプレートファイル（例: Jinja2）をロードし、提供されたデータで埋め込んで最終的な文字列（Markdownコンテンツ）を生成します。
-   **`src/generate_repo_list/url_utils.py`**
    -   役割: GitHub APIのエンドポイントURLやリポジトリのウェブURLなど、さまざまなURLを構築・操作するためのユーティリティ機能を提供します。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**
    -   `main()` 関数（エントリーポイント）: リポジトリ内のファイルサイズをチェックし、設定された閾値を超える大容量ファイルがある場合に警告またはエラーを報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-03 07:12:27 JST
