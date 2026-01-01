Last updated: 2026-01-02

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHubリポジトリ情報を自動で取得します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにリポジトリ一覧のMarkdownファイルを生成します。
- これにより、SEO最適化されたリポジトリ一覧ページを提供し、検索エンジンやLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (Markdownからのサイト生成), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Git (バージョン管理), VS Code (.editorconfig), ruff (Pythonリンター/フォーマッター)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: Python (スクリプト実行環境), GitHub API (リポジトリ情報取得)
- 言語機能: Python (主要な開発言語)
- 自動化・CI/CD: 該当なし (CI/CD不要のローカル開発重視の構成)
- 開発標準: .editorconfig (エディタ設定), ruff.toml (Pythonコードスタイル設定)
- その他: YAML (設定ファイル管理), TOML (シークレット・pytest設定), JSON (JSON-LDテンプレート, manifest.json)

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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: さまざまなエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、機能、セットアップ方法、使い方などを説明するメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の基本的な設定（サイト名、テーマ、プラグインなど）を定義するファイル。
- **`assets/`**: Jekyllサイトで利用される画像やファビコンなどの静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズ。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトファイル。
- **`generated-docs/`**: 各リポジトリから自動取得される `project-overview.md` など、生成されたドキュメントやデータが配置される、または参照されるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイル。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧が記述されたMarkdownファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: プロジェクト開発における特定の課題や議論、メモなどを記述したMarkdownファイルのコレクション。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイル。サイトの表示名、アイコン、テーマカラーなどを定義し、モバイルデバイスなどでのユーザー体験を向上させます。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の設定ファイル。テストの実行方法やオプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンを記載したファイル。
- **`requirements.txt`**: プロジェクトが本番環境で動作するために必要となるPythonパッケージとそのバージョンを記載したファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、またはクロールしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツール `ruff` の設定ファイル。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリ。
    - **`src/generate_repo_list/`**: GitHubリポジトリ一覧を生成するための主要なPythonモジュール群。
        - **`badge_generator.py`**: リポジトリの技術スタックやステータスを示すバッジ画像を生成するロジックが含まれています。
        - **`config.yml`**: プロジェクトの実行時設定（GitHubトークン、プロジェクト概要取得設定など）を定義するYAMLファイル。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        - **`generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成する処理を orchestrate します。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ（JSON-LD）のテンプレートを定義するファイル。
        - **`language_info.py`**: GitHubリポジトリで使用されているプログラミング言語に関する情報を処理・整形するモジュール。
        - **`markdown_generator.py`**: 取得したリポジトリ情報とテンプレートをもとに、最終的なリポジトリ一覧のMarkdownファイルを生成するモジュール。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要を抽出し、取得するモジュール。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に加工するモジュール。
        - **`seo_template.yml`**: SEO関連のメタデータや表示設定のテンプレートを定義するYAMLファイル。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するモジュール。
        - **`strings.yml`**: プロジェクト内で使用される表示メッセージや文言を国際化・一元管理するためのYAMLファイル。
        - **`template_processor.py`**: Markdown生成時に使用されるテキストテンプレートに変数を埋め込むなどの処理を行うモジュール。
        - **`url_utils.py`**: URLの整形や検証など、URL関連のユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得とパース）をテストするためのスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトが格納されているディレクトリ。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテスト。
    - **`test_environment.py`**: 実行環境の設定や依存関係に関するテスト。
    - **`test_integration.py`**: 複数のモジュール間の連携をテストする結合テスト。
    - **`test_markdown_generator.py`**: `markdown_generator.py` モジュールによるMarkdown生成ロジックのテスト。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールに関するテスト。
    - **`test_repository_processor.py`**: `repository_processor.py` モジュールによるリポジトリ情報処理に関するテスト。

## 関数詳細説明
このプロジェクトはPythonスクリプトを中心に構成されており、主要なモジュールには以下のような関数が含まれています。

- **`generate_repo_list.py`**
    - `main()`: スクリプトの主要な実行ロジックを制御します。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成までの一連の流れを呼び出します。
        - 引数: なし (コマンドライン引数は内部で解析)
        - 戻り値: なし (ファイル出力を行う)
    - `_parse_arguments()`: コマンドラインから `--username`, `--output`, `--limit` などの引数を解析し、プログラムで利用可能な形式に変換します。
        - 引数: なし
        - 戻り値: `argparse.Namespace` オブジェクト（解析された引数を持つ）

- **`repository_processor.py`**
    - `fetch_repositories(username, token)`: 指定されたGitHubユーザー名とアクセストークンを使用して、GitHub APIからユーザーのリポジトリ情報を取得します。
        - 引数: `username` (str), `token` (str)
        - 戻り値: リポジトリ情報のリスト (list of dict)
    - `process_repository(repo_data, config, cache)`: 単一のリポジトリデータを受け取り、必要な情報を抽出し、整形してMarkdown生成に適した形式に加工します。
        - 引数: `repo_data` (dict), `config` (dict), `cache` (dict)
        - 戻り値: 処理されたリポジトリ情報 (dict)

- **`project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name, github_token, config, cache)`: 指定されたリポジトリ名とトークンを使って、そのリポジトリ内の `project-overview.md` ファイルから概要をフェッチします。
        - 引数: `repo_name` (str), `github_token` (str), `config` (dict), `cache` (dict)
        - 戻り値: 抽出されたプロジェクト概要の文字列 (str)
    - `_parse_overview_markdown(markdown_content, section_title)`: Markdownコンテンツから指定されたセクションタイトル以下の3行の概要を抽出します。
        - 引数: `markdown_content` (str), `section_title` (str)
        - 戻り値: 抽出された概要文字列 (str) または None

- **`markdown_generator.py`**
    - `generate_markdown(processed_repos, strings, seo_template, json_ld_template)`: 処理されたリポジトリ情報のリストを受け取り、HTMLのヘッド部分 (SEO用) とリポジトリ一覧のMarkdownコンテンツ全体を生成します。
        - 引数: `processed_repos` (list of dict), `strings` (dict), `seo_template` (dict), `json_ld_template` (dict)
        - 戻り値: 生成されたMarkdownコンテンツ (str)
    - `_generate_repo_section(repo, strings)`: 個々のリポジトリデータに基づいて、そのリポジトリの表示セクションをMarkdown形式で生成します。
        - 引数: `repo` (dict), `strings` (dict)
        - 戻り値: 単一リポジトリのMarkdownセクション (str)

- **`config_manager.py`**
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Python辞書として返します。
        - 引数: `config_path` (str)
        - 戻り値: 設定データ (dict)

- **`badge_generator.py`**
    - `generate_badge_url(label, message, color)`: 指定されたラベル、メッセージ、色に基づいてShields.ioなどのバッジURLを生成します。
        - 引数: `label` (str), `message` (str), `color` (str)
        - 戻り値: バッジ画像のURL (str)

## 関数呼び出し階層ツリー
関数呼び出し階層に関する詳細な分析情報は提供されていませんが、メインスクリプト `generate_repo_list.py` を中心に、以下のような論理的な流れで各モジュールの主要関数が呼び出されると推測されます。

```
main() (generate_repo_list.py)
├── _parse_arguments() (generate_repo_list.py)
├── load_config() (config_manager.py)
├── fetch_repositories() (repository_processor.py)
│   └── (GitHub API呼び出し)
├── (ループ: 各リポジトリに対して)
│   ├── process_repository() (repository_processor.py)
│   │   ├── fetch_project_overview() (project_overview_fetcher.py)
│   │   │   └── _parse_overview_markdown() (project_overview_fetcher.py)
│   │   ├── get_language_data() (language_info.py)
│   │   ├── calculate_stats() (statistics_calculator.py)
│   │   └── generate_badge_url() (badge_generator.py)
│   └── (その他のデータ整形・準備)
└── generate_markdown() (markdown_generator.py)
    └── (ループ: 各処理済みリポジトリに対して)
        └── _generate_repo_section() (markdown_generator.py)

---
Generated at: 2026-01-02 07:06:34 JST
