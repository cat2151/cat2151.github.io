Last updated: 2026-04-13

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、JekyllベースのGitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたリポジトリ一覧は、検索エンジンやLLMからの参照性を向上させ、情報発見性を高めます。
- リポジトリ情報の取得からSEO最適化されたMarkdown出力まで、一貫して自動化されたワークフローを提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータとして最終的なコンテンツを表示), **Markdown** (出力形式であり、JekyllによってHTMLに変換され表示される)
- 音楽・オーディオ: 特になし
- 開発ツール: **Python** (主要な開発言語としてスクリプトを実行), **GitHub API** (リポジトリ情報の取得に利用), **PyYAML** (YAML設定ファイルの読み込み), **Toml** (TOML設定ファイルの読み込み)
- テスト: **pytest** (Pythonコードの単体・統合テストフレームワーク)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報を取得しMarkdownファイルを生成する実質的なビルドプロセス), **Jekyll** (GitHub Pages側でMarkdownからサイトを生成する静的サイトジェネレータ)
- 言語機能: **Python** (ファイルI/O、HTTPリクエスト、文字列処理、データ構造操作などの豊富な標準ライブラリおよび構文機能を利用)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から、自動化されたワークフローやCI/CDの実行基盤として利用されていると推測されます)
- 開発標準: **ruff** (Pythonコードの高速なLinterおよびFormatter), **.editorconfig** (異なるエディタ間でのコードスタイル統一を支援)

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
- **.editorconfig**: 異なるエディタやIDE間でコードの書式設定（インデント、改行コードなど）を統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリ。
    - **check_large_files/README.md**: `check_large_files`スクリプトの目的と使い方を説明するドキュメント。
    - **check-large-files.toml**: リポジトリ内の大容量ファイルをチェックするための設定ファイル。
    - **scripts/check_large_files.py**: 指定された設定に基づいてリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを指定する設定ファイル。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使用方法などを記述した、プロジェクトの顔となるドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの挙動に影響します。
- **assets/**: Webサイトで使用される画像、アイコン（favicon）、スタイルシートなどの静的アセットを格納するディレクトリ。
    - `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグや単体テストを行うためのスクリプト。
- **generated-docs/**: スクリプトによって生成されたドキュメントや一時ファイルを格納するためのディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。このプロジェクトによってリポジトリ一覧がここに生成されます。
- **issue-notes/22.md**: 特定の課題（Issue #22）に関する詳細なメモや検討事項を記述したファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供するウェブアプリマニフェストファイル。
- **pytest.ini**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイル。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: 本番環境でこのスクリプトを実行するために必要なPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **ruff.toml**: PythonコードのLinter/FormatterであるRuffの設定ファイル。コードスタイルのルールを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧を生成するコアロジックを格納するPythonパッケージ。
        - **__init__.py**: `generate_repo_list`がPythonサブパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの言語やライセンスなどの情報を視覚的なバッジとして生成するロジックを実装します。
        - **config.yml**: リポジトリ概要の取得設定など、プロジェクト全体の技術的なパラメータを定義する設定ファイル。
        - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するユーティリティモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付データを、人間が読みやすい形式に整形する機能を提供します。
        - **generate_repo_list.py**: GitHub APIを呼び出し、リポジトリ情報を処理し、最終的なMarkdownファイルを生成するプロジェクトのメインスクリプト。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレート。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・表示するためのロジック。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdown形式のコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリから特定のMarkdownファイル（例: `generated-docs/project-overview.md`）をフェッチし、その中からプロジェクト概要を抽出する機能を提供します。
        - **readme_badge_extractor.py**: READMEファイル内に埋め込まれたバッジ（Shields.ioなど）のURLや情報を抽出するロジック。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
        - **seo_template.yml**: 各リポジトリのMarkdown生成時に使用されるSEOメタデータ（タイトル、ディスクリプションなど）のテンプレート。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算するロジック。
        - **strings.yml**: アプリケーション内で使用される表示メッセージや静的な文言を一元管理するファイル。
        - **template_processor.py**: Markdownテンプレートを読み込み、プレースホルダーを実際のデータで置き換える処理を行うモジュール。
        - **url_utils.py**: URLの構築や検証など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールのテストケースを記述したファイル。
- **tests/**: プロジェクトの様々なコンポーネントに対するテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャやテストヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの統合テスト。
    - **test_check_large_files.py**: `check_large_files.py`スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテスト。
    - **test_date_formatter.py**: 日付整形機能のテスト。
    - **test_environment.py**: 実行環境や依存関係のチェックに関するテスト。
    - **test_integration.py**: プロジェクト全体の主要な処理フローの統合テスト。
    - **test_markdown_generator.py**: Markdown生成ロジックのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**
    - `main()`: プロジェクトの主要な実行エントリポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ取得、各リポジトリの処理、Markdown生成、最終ファイル出力までの一連のフローを制御します。
        - 引数: なし
        - 戻り値: なし
    - `parse_arguments()`: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、その値を返します。
        - 引数: なし
        - 戻り値: `argparse.Namespace`オブジェクト、解析された引数を含む
    - `get_repositories(username, token, limit=None)`: 指定されたGitHubユーザー名のリポジトリ一覧をGitHub APIを介して取得します。オプションで取得数を制限できます。
        - 引数: `username` (str), `token` (str), `limit` (int, optional)
        - 戻り値: リポジトリデータのリスト (list of dict)
    - `process_repository(repo_data, config, strings)`: 個々のリポジトリデータを整形し、バッジ情報、プロジェクト概要、整形済み日付などを含んだ辞書を作成します。
        - 引数: `repo_data` (dict), `config` (dict), `strings` (dict)
        - 戻り値: 処理済みリポジトリ情報 (dict)
    - `generate_markdown(processed_repos, config, strings)`: 処理済みリポジトリデータのリストから、最終的なMarkdown形式の文字列を生成します。
        - 引数: `processed_repos` (list of dict), `config` (dict), `strings` (dict)
        - 戻り値: 生成されたMarkdown文字列 (str)
    - `write_output(filename, content)`: 生成されたMarkdownコンテンツを指定されたファイルに書き込みます。
        - 引数: `filename` (str), `content` (str)
        - 戻り値: なし
- **src/generate_repo_list/repository_processor.py**
    - `process_repository_data(repo, config, strings, github_token)`: GitHub APIから取得した生のリポジトリデータを解析し、表示に必要な情報を抽出・整形します。`project_overview_fetcher`を呼び出し、概要も取得します。
        - 引数: `repo` (dict), `config` (dict), `strings` (dict), `github_token` (str)
        - 戻り値: 整形されたリポジトリ情報 (dict)
- **src/generate_repo_list/project_overview_fetcher.py**
    - `fetch_project_overview(repo_name, owner, config, github_token, cache=None)`: 特定のリポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要の3行説明をフェッチします。
        - 引数: `repo_name` (str), `owner` (str), `config` (dict), `github_token` (str), `cache` (dict, optional)
        - 戻り値: プロジェクト概要の文字列 (str) または None
    - `_extract_overview_from_markdown(markdown_content, section_title)`: Markdownコンテンツから指定されたセクション（例: "プロジェクト概要"）の3行説明を抽出します。
        - 引数: `markdown_content` (str), `section_title` (str)
        - 戻り値: 抽出された概要文字列 (str)
- **src/generate_repo_list/markdown_generator.py**
    - `generate_repo_markdown(repo_info, config, strings)`: 単一のリポジトリ情報を受け取り、そのリポジトリの表示ブロックに対応するMarkdown文字列を生成します。
        - 引数: `repo_info` (dict), `config` (dict), `strings` (dict)
        - 戻り値: 単一リポジトリのMarkdown文字列 (str)
    - `generate_full_markdown(repos_data, config, strings)`: すべての処理済みリポジトリデータとSEO情報を含め、最終的な`index.md`全体のMarkdownコンテンツを生成します。
        - 引数: `repos_data` (list of dict), `config` (dict), `strings` (dict)
        - 戻り値: 完全なMarkdown文字列 (str)
- **src/generate_repo_list/config_manager.py**
    - `load_config(config_path)`: YAML形式の設定ファイルを読み込み、辞書として返します。
        - 引数: `config_path` (str)
        - 戻り値: 設定データ (dict)
    - `load_strings(strings_path)`: YAML形式の文言ファイルを読み込み、辞書として返します。
        - 引数: `strings_path` (str)
        - 戻り値: 文言データ (dict)
    - `get_github_token()`: `secrets/secrets.toml`または環境変数からGitHubパーソナルアクセストークンを取得します。
        - 引数: なし
        - 戻り値: GitHubトークン (str)
- **src/generate_repo_list/badge_generator.py**
    - `generate_language_badge(language)`: 指定されたプログラミング言語に対応するShields.ioのバッジURLを生成します。
        - 引数: `language` (str)
        - 戻り値: バッジURL (str)
    - `generate_license_badge(license_name)`: 指定されたライセンス名に対応するShields.ioのバッジURLを生成します。
        - 引数: `license_name` (str)
        - 戻り値: バッジURL (str)
- **src/generate_repo_list/date_formatter.py**
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を、例えば「YYYY年MM月DD日」のようなユーザーフレンドリーな形式に整形します。
        - 引数: `iso_date_string` (str)
        - 戻り値: フォーマットされた日付文字列 (str)
- **src/generate_repo_list/url_utils.py**
    - `build_repo_url(username, repo_name)`: 指定されたユーザー名とリポジトリ名からGitHubリポジトリの完全なURLを構築します。
        - 引数: `username` (str), `repo_name` (str)
        - 戻り値: リポジトリURL (str)

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── parse_arguments() (generate_repo_list.py)
├── config_manager.load_config() (config_manager.py)
├── config_manager.load_strings() (config_manager.py)
├── config_manager.get_github_token() (config_manager.py)
├── get_repositories() (generate_repo_list.py)
│   └── (GitHub API call)
├── process_repository() (generate_repo_list.py) [各リポジトリに対してループ]
│   ├── repository_processor.process_repository_data() (repository_processor.py)
│   │   ├── project_overview_fetcher.fetch_project_overview() (project_overview_fetcher.py)
│   │   │   └── _extract_overview_from_markdown() (project_overview_fetcher.py)
│   │   └── url_utils.build_repo_url() (url_utils.py)
│   ├── badge_generator.generate_language_badge() (badge_generator.py)
│   ├── badge_generator.generate_license_badge() (badge_generator.py)
│   └── date_formatter.format_date() (date_formatter.py)
├── generate_markdown() (generate_repo_list.py)
│   └── markdown_generator.generate_full_markdown() (markdown_generator.py)
│       └── markdown_generator.generate_repo_markdown() (markdown_generator.py) [各リポジトリに対してループ]
│           └── template_processor.process_template() (template_processor.py)
└── write_output() (generate_repo_list.py)

---
Generated at: 2026-04-13 07:11:32 JST
