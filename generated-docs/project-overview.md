Last updated: 2026-03-20

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成し、検索エンジン最適化を図るシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のMarkdown形式で出力します。
- これにより、GitHubリポジトリの発見性を高め、Large Language Models (LLM) からの参照品質向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤)、Markdown (生成されるコンテンツ形式)。
- 音楽・オーディオ: 該当なし。
- 開発ツール: Git (バージョン管理)、GitHub (リポジトリホスティング、API提供)。
- テスト: pytest (Python向けテストフレームワーク)。
- ビルドツール: Python (スクリプト実行によるMarkdown生成)、Jekyll (GitHub Pagesでのサイトビルド)。
- 言語機能: Python (スクリプトの主要言語)。
- 自動化・CI/CD: GitHub API (リポジトリ情報取得の自動化)。
- 開発標準: ruff (Pythonコードのフォーマッタおよびリンタ)、.editorconfig (エディタ設定の統一)。

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
- **.editorconfig**: 異なるエディタやIDE間で、コードのインデントや文字コードなどの書式設定を一貫させるための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルがないかチェックするためのサブディレクトリ。
        - **README.md**: `check_large_files` の機能と使用方法を説明するドキュメント。
        - **check-large-files.toml**: 大容量ファイルチェックの具体的なルールや閾値を定義する設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトはMITライセンス）。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使い方などを記述したメインのドキュメント。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義。
- **assets/**: Webサイトの静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）ファイル群。
- **debug_project_overview.py**: `project_overview_fetcher.py` 機能のデバッグや単体動作確認に使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメント（例: プロジェクト概要ファイル）が一時的に配置される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールでサイトの所有権を確認するために配置されるファイル。
- **index.md**: メインのPythonスクリプトによって動的に生成される、リポジトリ一覧を表示するためのMarkdownファイル。JekyllによってHTMLに変換され、GitHub Pagesのトップページとなる。
- **issue-notes/22.md**: プロジェクトの特定の課題（例: GitHub Issue #22）に関する詳細なメモや検討事項を記録したファイル。
- **manifest.json**: プログレッシブウェブアプリ (PWA) のメタデータ（アプリ名、アイコン、表示設定など）を定義するファイル。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイル。テストの検出方法や実行オプションなどを指定。
- **requirements-dev.txt**: 開発環境およびテスト実行時に必要なPythonパッケージとそのバージョンを記述したファイル。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイル。
- **ruff.toml**: Pythonコードの整形（フォーマット）と静的解析（リンティング）を行うツール`ruff`の設定ファイル。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧生成ロジックの中核を担うPythonパッケージ。
        - **__init__.py**: Pythonパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリの言語やライセンスなどのバッジ情報を生成するロジックを実装したモジュール。
        - **config.yml**: プロジェクト概要取得機能などの技術的なパラメータを定義するYAML形式の設定ファイル。
        - **config_manager.py**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するモジュール。
        - **date_formatter.py**: 日付や時刻の表示形式を整形する機能を提供するモジュール。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプト。
        - **json_ld_template.json**: 検索エンジン向けに構造化データを提供するJSON-LD形式のテンプレートファイル。
        - **language_info.py**: リポジトリのプログラミング言語に関する情報を取得・処理するモジュール。
        - **markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するモジュール。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から概要情報を抽出するモジュール。
        - **readme_badge_extractor.py**: READMEファイルから特定のバッジ情報（例: CI/CDステータス）を抽出するモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、表示に適した形式に加工するモジュール。
        - **seo_template.yml**: 検索エンジン最適化 (SEO) に関連するメタデータや設定のテンプレートを定義するYAMLファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するモジュール。
        - **strings.yml**: UI表示メッセージや生成されるMarkdownで使用される文字列を一元管理するYAMLファイル。
        - **template_processor.py**: Markdown生成に使用するテンプレートファイルの読み込みと変数置換を行うモジュール。
        - **url_utils.py**: URLの生成や解析など、URLに関連するユーティリティ機能を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能を検証するためのテストスクリプト。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **test_badge_generator_integration.py**: `badge_generator.py` の結合テスト。
    - **test_check_large_files.py**: `check_large_files.py` スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理機能に関するテスト。
    - **test_date_formatter.py**: 日付整形機能のテスト。
    - **test_environment.py**: 実行環境の依存関係や設定に関するテスト。
    - **test_integration.py**: システム全体の統合テスト。
    - **test_markdown_generator.py**: Markdown生成機能のテスト。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    - **test_repository_processor.py**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
- **badge_generator.py** 内の関数:
    - **generate_badge(repo_data)**: リポジトリデータに基づいて、プログラミング言語やライセンスなどの視覚的なバッジ情報を生成します。
        - **引数**: `repo_data` (リポジトリ情報を格納した辞書)
        - **戻り値**: 生成されたバッジ情報のリストまたは文字列
- **config_manager.py** 内の関数:
    - **load_config(file_path)**: 指定されたパスから設定ファイル（YAMLなど）を読み込み、Pythonオブジェクトとして返します。
        - **引数**: `file_path` (設定ファイルへのパス文字列)
        - **戻り値**: 設定データを格納した辞書
    - **get_github_token()**: 環境変数またはシークレットファイルからGitHub APIトークンを取得します。
        - **引数**: なし
        - **戻り値**: GitHubトークン文字列
- **date_formatter.py** 内の関数:
    - **format_date(timestamp, format_string)**: タイムスタンプを任意のフォーマット文字列に従って日付/時刻形式に変換します。
        - **引数**: `timestamp` (Unixタイムスタンプまたは日付時刻オブジェクト), `format_string` (変換フォーマット文字列)
        - **戻り値**: フォーマットされた日付時刻文字列
- **generate_repo_list.py** 内の関数:
    - **main()**: プログラムの実行エントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連の流れを統括します。
        - **引数**: コマンドライン引数 (例: `--username`, `--output`, `--limit`)
        - **戻り値**: なし
    - **fetch_repositories(username, token, limit)**: 指定されたGitHubユーザー名とAPIトークンを使用し、GitHub APIからリポジトリ情報を取得します。取得数に制限を設けることができます。
        - **引数**: `username` (GitHubユーザー名), `token` (GitHub APIトークン), `limit` (取得するリポジトリ数の上限)
        - **戻り値**: 取得したリポジトリ情報のリスト
    - **generate_output(repositories, output_file)**: 処理済みリポジトリ情報のリストから最終的なMarkdownファイルを生成し、指定されたファイルに出力します。
        - **引数**: `repositories` (処理済みリポジトリ情報のリスト), `output_file` (出力ファイル名文字列)
        - **戻り値**: なし
- **language_info.py** 内の関数:
    - **get_dominant_language(repo_data)**: リポジトリのデータから、最も使用されている（主要な）プログラミング言語を特定します。
        - **引数**: `repo_data` (リポジトリ情報を格納した辞書)
        - **戻り値**: 主要なプログラミング言語の文字列
- **markdown_generator.py** 内の関数:
    - **generate_repo_markdown(repo_data, template)**: 個々のリポジトリデータとテンプレートを使用して、そのリポジトリのMarkdownコンテンツを生成します。
        - **引数**: `repo_data` (リポジトリ情報を格納した辞書), `template` (Markdownテンプレート文字列)
        - **戻り値**: 生成されたMarkdown文字列
    - **generate_index_markdown(repo_list, global_template)**: 全リポジトリのリストとグローバルテンプレートを使用して、`index.md`などのメインのMarkdownファイルコンテンツ全体を生成します。
        - **引数**: `repo_list` (処理済みリポジトリのリスト), `global_template` (全体のMarkdownテンプレート文字列)
        - **戻り値**: 生成されたMarkdown文字列
- **project_overview_fetcher.py** 内の関数:
    - **fetch_project_overview(repo_name, github_token, config)**: 特定のリポジトリ（`repo_name`）から`generated-docs/project-overview.md`ファイルを取得し、その中の「プロジェクト概要」セクションの3行説明を抽出します。
        - **引数**: `repo_name` (リポジトリ名文字列), `github_token` (GitHub APIトークン), `config` (設定辞書)
        - **戻り値**: 3行のプロジェクト概要テキストのリスト
- **readme_badge_extractor.py** 内の関数:
    - **extract_badges_from_readme(readme_content)**: READMEファイルの内容を解析し、含まれるバッジ（例: ビルドステータスバッジ）のURLやテキスト情報を抽出します。
        - **引数**: `readme_content` (READMEファイルのコンテンツ文字列)
        - **戻り値**: 抽出されたバッジ情報のリスト
- **repository_processor.py** 内の関数:
    - **process_repository_data(raw_repo_data, config)**: GitHub APIから直接取得した生のリポジトリデータを、Markdown生成に適した形式に整形・加工します。
        - **引数**: `raw_repo_data` (生のGitHub APIリポジトリデータ辞書), `config` (設定辞書)
        - **戻り値**: 処理済みのリポジトリデータ辞書
- **statistics_calculator.py** 内の関数:
    - **calculate_stats(repo_data)**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または抽出します。
        - **引数**: `repo_data` (リポジトリ情報を格納した辞書)
        - **戻り値**: 統計情報を格納した辞書
- **template_processor.py** 内の関数:
    - **load_template(template_path)**: 指定されたファイルパスからテンプレートの内容を読み込みます。
        - **引数**: `template_path` (テンプレートファイルへのパス文字列)
        - **戻り値**: テンプレートコンテンツ文字列
    - **render_template(template_content, data)**: テンプレートコンテンツ内のプレースホルダーを、提供されたデータで置換して最終的な文字列を生成します。
        - **引数**: `template_content` (テンプレート文字列), `data` (置換データを含む辞書)
        - **戻り値**: レンダリングされた文字列
- **url_utils.py** 内の関数:
    - **generate_repo_url(username, repo_name)**: 指定されたユーザー名とリポジトリ名に基づいて、GitHubリポジトリのURLを生成します。
        - **引数**: `username` (GitHubユーザー名), `repo_name` (リポジトリ名)
        - **戻り値**: リポジトリのURL文字列

## 関数呼び出し階層ツリー
```
提供された情報からは、プロジェクト全体の関数呼び出し階層を詳細に分析できませんでした。
しかし、`generate_repo_list.py` の `main()` 関数がエントリポイントとして機能し、
`config_manager.py` (設定読み込み), `repository_processor.py` (データ加工), `project_overview_fetcher.py` (概要取得), `markdown_generator.py` (Markdown生成) などのモジュールの関数を順次呼び出していると推測されます。

---
Generated at: 2026-03-20 07:08:23 JST
