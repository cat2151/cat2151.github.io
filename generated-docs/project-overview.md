Last updated: 2026-01-25

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、Jekyllに対応したSEO最適化済みのMarkdownファイルを生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照成功率の向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), `requests` (GitHub APIとのHTTP通信), `PyYAML` (YAML設定ファイルの読み込み), `toml` (TOML設定ファイルの読み込み), GitHub API (リポジトリ情報の取得)
- テスト: `pytest` (Python向けテストフレームワーク)
- ビルドツール: Pythonスクリプト (Markdownファイルの生成ロジック), Jekyll (GitHub Pages側でのサイト構築)
- 言語機能: Python (スクリプト開発における言語仕様と標準機能)
- 自動化・CI/CD: GitHub Pages (自動デプロイ先プラットフォーム), **注: プロジェクト自体はローカル開発重視でCI/CD機能は含まない**
- 開発標準: `ruff` (Pythonコードのリンターおよびフォーマッター), `.editorconfig` (IDE/エディタ間のコーディングスタイル統一)

## ファイル階層ツリー
```
📄 .editorconfig
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
- **`.editorconfig`**: 複数の開発者が一貫したコーディングスタイルを維持するための設定ファイル。インデントサイズや文字コードなどを定義します。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。ビルド成果物や一時ファイルなどを無視するために使用されます。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。プロジェクトの利用条件を明示します。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、開発者向けのヒントなどを記述した、プロジェクトの顔となるMarkdownファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグイン設定など、GitHub Pagesサイト全体の挙動を制御します。
- **`assets/`**: サイトで使用される静的ファイル（例: ファビコン画像）を格納するディレクトリ。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのアイコン（ファビコン）の各種サイズ画像ファイル。ブラウザのタブやブックマークなどで表示されます。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグや単体テストのために使用されるPythonスクリプト。
- **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメントを格納するためのディレクトリ。特に、各リポジトリのプロジェクト概要ファイルがここに格納されることが想定されます。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイル。
- **`index.md`**: メインのMarkdownファイルであり、生成されたGitHubリポジトリ一覧が出力される主要なページです。GitHub Pagesのトップページとして機能します。
- **`issue-notes/`**: 開発中の課題や検討事項、メモなどをMarkdown形式で記録したファイル群を格納するディレクトリ。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブサイトをユーザーのホーム画面に追加する際の表示名、アイコン、起動時の挙動などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の設定ファイル。テスト検出パターン、マーカー、実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発時およびテスト時にのみ必要なPythonパッケージの依存関係をリスト化したファイル。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージの依存関係をリスト化したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールすべきか、どのページをクロールすべきでないかを指示するファイル。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッターである`ruff`の設定ファイル。コードの品質と一貫性を保つためのルールを定義します。
- **`src/`**: プロジェクトのソースコードを格納するルートディレクトリ。
    - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す空ファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成に関するコアロジックを格納するPythonパッケージ。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空ファイル。
        - **`badge_generator.py`**: GitHubリポジトリのバッジ（例: 言語バッジ、ステータスバッジ）を生成するロジックを実装します。
        - **`config.yml`**: `generate_repo_list`パッケージ固有の技術的パラメータを設定するYAMLファイル。例: プロジェクト概要取得機能の設定。
        - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`など）を読み込み、管理するためのユーティリティ関数を提供します。
        - **`date_formatter.py`**: リポジトリの更新日などの日付情報を整形するための関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプト。GitHub APIからの情報取得からMarkdown生成までの一連の処理を orchestrate します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のための構造化データであるJSON-LDのテンプレートファイル。
        - **`language_info.py`**: GitHubリポジトリの言語使用に関する情報を処理し、表示に役立つ形式に変換する機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックを実装します。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定ファイル (`generated-docs/project-overview.md` など) からプロジェクト概要の3行説明を自動取得する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、テストカバレッジ）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換する役割を担います。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - **`strings.yml`**: サイトに表示される各種メッセージや文言を一元管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2などを想定）の処理を行う機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数をまとめたファイル。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能のテストケースを記述したスクリプト。
- **`tests/`**: プロジェクトの各種テストスクリプトを格納するディレクトリ。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の結合テスト。
    - **`test_config.py`**: 設定管理機能 (`config_manager.py`) のテスト。
    - **`test_date_formatter.py`**: 日付整形機能 (`date_formatter.py`) のテスト。
    - **`test_environment.py`**: 開発環境や依存関係の健全性をチェックするテスト。
    - **`test_integration.py`**: プロジェクト全体の主要な機能の結合テスト。
    - **`test_markdown_generator.py`**: Markdown生成機能 (`markdown_generator.py`) のテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテスト。
    - **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能 (`readme_badge_extractor.py`) のテスト。
    - **`test_repository_processor.py`**: リポジトリ処理機能 (`repository_processor.py`) のテスト。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、各ファイルは特定の役割を持つ関数群を内包しています。以下は、各主要ファイルが持つと推定される関数の説明です。具体的な引数や戻り値の型は、一般的なPythonの慣習に基づいています。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - **`main(username: str, output_file: str, limit: Optional[int] = None)`**: プログラムのエントリーポイント。指定されたGitHubユーザーのリポジトリ情報を取得し、Markdown形式で出力ファイルに書き出す一連の処理を制御します。
        - 引数: `username` (GitHubユーザー名), `output_file` (出力Markdownファイルパス), `limit` (処理するリポジトリ数の上限、オプション)
        - 戻り値: なし
- **`src/generate_repo_list/badge_generator.py`**:
    - **`generate_badge_markdown(badge_info: Dict[str, str]) -> str`**: 与えられたバッジ情報（例: 名前、URL、画像URL）からMarkdown形式のバッジ文字列を生成します。
        - 引数: `badge_info` (バッジ情報を格納する辞書)
        - 戻り値: Markdown形式のバッジ文字列
- **`src/generate_repo_list/config_manager.py`**:
    - **`load_config(config_path: str) -> Dict`**: 指定されたパスのYAMLまたはTOML設定ファイルを読み込み、辞書として返します。
        - 引数: `config_path` (設定ファイルのパス)
        - 戻り値: 設定内容を格納する辞書
- **`src/generate_repo_list/date_formatter.py`**:
    - **`format_date(date_string: str) -> str`**: 日付文字列を読みやすい形式に整形します。
        - 引数: `date_string` (整形前のISO形式などの日付文字列)
        - 戻り値: 整形された日付文字列
- **`src/generate_repo_list/markdown_generator.py`**:
    - **`generate_repository_list_markdown(repositories: List[Dict], config: Dict) -> str`**: 複数のリポジトリ情報と設定に基づいて、Jekyll互換のリポジトリ一覧Markdownコンテンツ全体を生成します。
        - 引数: `repositories` (処理済みリポジトリ情報のリスト), `config` (プロジェクト設定)
        - 戻り値: 生成されたMarkdownコンテンツ文字列
    - **`generate_single_repository_entry(repo_data: Dict, config: Dict) -> str`**: 個々のリポジトリのMarkdownエントリ（タイトル、説明、バッジなど）を生成します。
        - 引数: `repo_data` (単一リポジトリの詳細データ), `config` (プロジェクト設定)
        - 戻り値: 単一リポジトリのMarkdownエントリ文字列
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_url: str, config: Dict) -> Optional[str]`**: 指定されたリポジトリのURLから、`generated-docs/project-overview.md`ファイルを読み込み、「プロジェクト概要」セクションの3行説明を抽出します。
        - 引数: `repo_url` (リポジトリのURL), `config` (プロジェクト概要取得に関する設定)
        - 戻り値: 抽出されたプロジェクト概要文字列、またはNone
- **`src/generate_repo_list/repository_processor.py`**:
    - **`process_repositories(raw_repos: List[Dict], config: Dict) -> List[Dict]`**: GitHub APIから取得した生のリポジトリデータリストを受け取り、整形、フィルタリング、追加情報（プロジェクト概要など）の付与を行い、Markdown生成に適した形式に変換します。
        - 引数: `raw_repos` (生のリポジトリデータリスト), `config` (プロジェクト設定)
        - 戻り値: 処理済みのリポジトリデータリスト
- **`googled947dc864c270e07.html`**:
  - 関数: なし (静的HTMLファイルのため)

上記以外にも、ユーティリティファイル (`language_info.py`, `statistics_calculator.py`, `url_utils.py`など) にはそれぞれ、言語情報処理、統計計算、URL操作に関する補助関数が含まれています。テストファイル (`tests/`ディレクトリ内のファイル) には、各機能のテストロジックが実装されています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-01-25 07:06:10 JST
