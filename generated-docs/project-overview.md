Last updated: 2026-02-18

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンにクロールされにくいGitHubユーザーページの課題を解消し、SEOを最適化します。
- 各リポジトリの概要、バッジ表示、アクティブ・アーカイブ分類など多様な情報を自動的に提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータとしてコンテンツが表示される基盤), **Markdown** (自動生成されるコンテンツの形式)
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール: **Python** (主要なスクリプト言語), **GitHub API** (リポジトリ情報の取得元), **PyYAML** (YAML形式の設定ファイル読み込み用), **TOML** (Secrets.tomlなどの設定ファイル読み込み用), **Requests** (HTTPリクエストによるAPI通信ライブラリ), **Git** (バージョン管理システム)
- テスト: **pytest** (Pythonのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (Markdownコンテンツを生成するロジック自体), **Jekyll** (GitHub Pagesの環境で静的サイトを生成・ホスト)
- 言語機能: **Python** (プロジェクトの主要な開発言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から自動化の意図が見受けられます), **Pythonスクリプト** (リポジトリ一覧生成の自動化ロジック)
- 開発標準: **ruff** (PythonコードのLinterおよびFormatter), **.editorconfig** (複数のエディタやIDE間でコーディングスタイルを統一するための設定)

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
*   **`.editorconfig`**: さまざまなエディタやIDE間で一貫したコーディングスタイルを定義する設定ファイルです。インデントのスタイルや文字コードなどを統一します。
*   **`.github_automation/`**: GitHub Actionsなど、リポジトリの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    *   **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック自動化機能の説明ドキュメントです。
    *   **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。チェック対象や閾値などを定義します。
    *   **`.github_automation/check_large_files/scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
*   **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイルです。一時ファイルやビルド成果物などをバージョン管理から除外します。
*   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されているファイルです。
*   **`README.md`**: プロジェクトの概要、セットアップ方法、使い方、貢献ガイドラインなどを記述した主要なドキュメントファイルです。
*   **`_config.yml`**: Jekyllサイト全体のグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
*   **`assets/`**: ウェブサイトで使用される静的なアセット（画像、アイコン、CSS、JSなど）を格納するディレクトリです。
    *   **`assets/favicon-16x16.png`**: ウェブサイトのファビコン（16x16ピクセル）です。
    *   **`assets/favicon-192x192.png`**: ウェブサイトのファビコン（192x192ピクセル）です。
    *   **`assets/favicon-32x32.png`**: ウェブサイトのファビコン（32x32ピクセル）です。
    *   **`assets/favicon-512x512.png`**: ウェブサイトのファビコン（512x512ピクセル）です。
*   **`debug_project_overview.py`**: `project_overview_fetcher` などのプロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
*   **`generated-docs/`**: GitHub Pagesサイト用に自動生成されたドキュメントやコンテンツが格納されるディレクトリです。
*   **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のための認証ファイルです。
*   **`index.md`**: GitHub Pagesサイトのトップページ（リポジトリ一覧）となるMarkdownファイルです。本スクリプトによってこのファイルが生成されます。
*   **`issue-notes/`**: 開発中のイシューや検討事項に関するメモがMarkdown形式で格納されるディレクトリです。
    *   **`issue-notes/10.md`**, **`issue-notes/12.md`**, ..., **`issue-notes/8.md`**: 各イシューに関する個別のメモファイルです。
*   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブアプリマニフェストファイルです。ホームスクリーンアイコン、表示モードなどを定義します。
*   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行オプションや探索パスなどを指定します。
*   **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記述したファイルです。
*   **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを記述したファイルです。
*   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいはしてはいけないかを指示するファイルです。
*   **`ruff.toml`**: PythonのLinter/FormatterであるRuffの設定ファイルです。コードスタイルのルールや自動修正に関する設定を定義します。
*   **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    *   **`src/__init__.py`**: Pythonパッケージとして `src` ディレクトリを認識させるための空ファイルです。
    *   **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを構成するPythonモジュール群が格納されています。
        *   **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして `generate_repo_list` ディレクトリを認識させるための空ファイルです。
        *   **`src/generate_repo_list/badge_generator.py`**: リポジトリ情報に基づいて各種バッジ（例: 言語、ライセンス、ステータスなど）を生成する機能を提供します。
        *   **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能など、スクリプトの技術的パラメータを設定するためのYAMLファイルです。
        *   **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイル（`config.yml` など）を読み込み、管理する機能を提供します。
        *   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形するユーティリティ関数を提供します。
        *   **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、整形し、Markdown形式で出力するメインスクリプトです。
        *   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
        *   **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報などを処理・分析する機能を提供します。
        *   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages用のMarkdownコンテンツを生成する機能を提供します。
        *   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        *   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報などを抽出する機能を提供します。
        *   **`src/generate_repo_list/repository_processor.py`**: GitHub APIとの連携を担当し、リポジトリ情報の取得、フィルタリング、整形を行います。
        *   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイルです。
        *   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算する機能を提供します。
        *   **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するためのYAMLファイルです。多言語化や文言の一元管理に利用されます。
        *   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートを処理し、データと結合して最終的なコンテンツを生成する機能を提供します。
        *   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
*   **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストや統合テストを含むテストスクリプトです。
*   **`tests/`**: プロジェクト全体のテストスクリプトが格納されるディレクトリです。
    *   **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    *   **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    *   **`tests/test_config.py`**: 設定ファイル読み込み・管理機能のテストです。
    *   **`tests/test_date_formatter.py`**: 日付整形機能のテストです。
    *   **`tests/test_environment.py`**: 実行環境（依存関係など）のテストです。
    *   **`tests/test_integration.py`**: 主要な機能間の連携をテストする統合テストです。
    *   **`tests/test_markdown_generator.py`**: Markdown生成機能のテストです。
    *   **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    *   **`tests/test_readme_badge_extractor.py`**: READMEからバッジ抽出する機能のテストです。
    *   **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
*   **`generate_repo_list.py`内の主要関数 (`main` または類似)**
    *   **役割**: プロジェクトの中心となる実行関数。GitHub APIからリポジトリ情報を取得し、加工して最終的なMarkdownファイルを生成する一連の処理を統括します。
    *   **引数**: `username` (GitHubユーザー名), `output` (出力ファイル名), `limit` (処理するリポジトリ数の上限、任意)。
    *   **戻り値**: なし（副作用として出力ファイルが生成されます）。
    *   **機能**: 設定の読み込み、リポジトリ情報の取得、各リポジトリの詳細処理、Markdownコンテンツの生成、ファイルへの書き出しを行います。
*   **`repository_processor.py`内の主要関数 (`fetch_repositories` または類似)**
    *   **役割**: GitHub APIを呼び出して、指定されたユーザーのリポジトリ情報を取得します。
    *   **引数**: `username` (GitHubユーザー名), `github_token` (認証用トークン), `limit` (取得するリポジトリ数の上限、任意)。
    *   **戻り値**: 取得したリポジトリ情報のリスト（辞書形式）。
    *   **機能**: GitHub REST APIへのHTTPリクエストの送信、エラーハンドリング、取得データのフィルタリングと基本的な整形を行います。
*   **`project_overview_fetcher.py`内の主要関数 (`get_project_overview` または類似)**
    *   **役割**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出します。
    *   **引数**: `repo_name` (リポジトリ名), `username` (GitHubユーザー名), `config` (概要取得設定), `github_token` (認証用トークン)。
    *   **戻り値**: プロジェクト概要の3行説明のリスト、または空のリスト。
    *   **機能**: GitHub APIを介してリポジトリ内のファイルを読み込み、指定されたセクションから箇条書きのテキストを解析して抽出します。
*   **`markdown_generator.py`内の主要関数 (`generate_markdown` または類似)**
    *   **役割**: 整形されたリポジトリ情報と抽出されたプロジェクト概要に基づいて、最終的なMarkdownコンテンツを生成します。
    *   **引数**: `repositories_data` (処理済みリポジトリ情報のリスト), `strings_data` (表示文言データ), `seo_template_data` (SEOテンプレートデータ)。
    *   **戻り値**: 生成されたMarkdown形式の文字列。
    *   **機能**: リポジトリごとに定義されたテンプレートを適用し、バッジ、リンク、概要などの情報を組み合わせてHTML互換のMarkdownを構築します。
*   **`badge_generator.py`内の主要関数 (`generate_badge_markdown` または類似)**
    *   **役割**: リポジトリの属性（言語、ライセンス、スター数など）に対応するMarkdown形式のバッジ文字列を生成します。
    *   **引数**: `repo_data` (個々のリポジトリデータ)。
    *   **戻り値**: バッジのMarkdown文字列。
    *   **機能**: リポジトリのメタデータに基づいて適切なバッジのURLを構築し、Markdown形式で出力します。
*   **`config_manager.py`内の主要関数 (`load_config` または類似)**
    *   **役割**: YAML形式の設定ファイル (`config.yml`, `strings.yml` など) を読み込み、Pythonの辞書オブジェクトとして提供します。
    *   **引数**: `file_path` (設定ファイルのパス)。
    *   **戻り値**: 読み込まれた設定内容を含む辞書。
    *   **機能**: YAMLパーサーを使用してファイルを読み込み、構造化された設定データを提供します。
*   **`date_formatter.py`内の主要関数 (`format_date` または類似)**
    *   **役割**: 日付文字列を人間が読みやすい形式に整形します。
    *   **引数**: `date_string` (ISO 8601形式などの日付文字列)。
    *   **戻り値**: 整形された日付文字列。
    *   **機能**: 日付オブジェクトへの変換、および指定されたフォーマット（例: "YYYY年MM月DD日"）での出力。
*   **`url_utils.py`内の主要関数 (`build_github_repo_url` または類似)**
    *   **役割**: GitHubリポジトリのURLを構築します。
    *   **引数**: `username`, `repo_name`。
    *   **戻り値**: 構築されたURL文字列。
    *   **機能**: 与えられた情報から正確なGitHubリポジトリのURLを生成します。

## 関数呼び出し階層ツリー
```
generate_repo_list.py (メインスクリプト)
├── config_manager.py (設定ファイルの読み込み)
├── repository_processor.py (GitHubリポジトリ情報の取得と整形)
│   └── url_utils.py (GitHub URLの構築)
├── project_overview_fetcher.py (各リポジトリの概要ファイルの取得と解析)
│   └── (GitHub APIを介したファイルコンテンツの読み込み)
├── markdown_generator.py (取得・整形された情報に基づくMarkdownコンテンツの生成)
│   ├── badge_generator.py (リポジトリの属性に応じたバッジの生成)
│   ├── date_formatter.py (日付情報の整形)
│   ├── template_processor.py (Markdownテンプレートへのデータ適用)
│   └── statistics_calculator.py (リポジトリ統計情報の計算)
└── (その他のユーティリティ関数やモジュールが適宜呼び出される)

---
Generated at: 2026-02-18 07:10:19 JST
