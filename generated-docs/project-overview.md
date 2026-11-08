Last updated: 2026-11-09

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages用のコンテンツを自動生成するシステムです。
- JekyllとMarkdownを活用し、リポジトリ一覧や各プロジェクトの概要を効率的に公開します。
- 検索エンジン最適化(SEO)と大規模言語モデル(LLM)からの参照性向上を目的としています。

## 技術スタック
- フロントエンド:
    - **GitHub Pages**: 静的サイトのホスティングサービスで、Jekyllと組み合わせてコンテンツを公開します。
    - **Jekyll**: GitHub Pagesで利用される静的サイトジェネレーター。Markdown形式の情報をHTMLに変換し、サイトを構築します。
    - **Markdown**: リポジトリ情報やプロジェクト概要を記述し、サイトコンテンツとして利用します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: GitHub APIからの情報取得、Markdownファイルの生成、各種データ処理を行うメインのスクリプト言語です。
    - **GitHub API**: GitHubリポジトリの情報をプログラム的に取得するためのインターフェースです。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`など）の記述に使用されます。
    - **TOML**: `pytest`の設定ファイル (`pytest.ini`) や、秘密情報（GitHubトークンなど）の管理 (`secrets.toml`を想定) に使用されます。
- テスト:
    - **pytest**: Pythonプロジェクトのテストフレームワークで、機能の単体テストや結合テストを実行します。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py`がリポジトリ一覧のMarkdownファイルを生成する主要なビルドプロセスを担います。
- 言語機能:
    - **Python標準ライブラリ**: ファイル操作、HTTPリクエスト処理 (`requests`ライブラリを介して)、文字列操作など、Pythonの標準的な機能が幅広く利用されています。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation`ディレクトリに設定があり、大規模ファイルチェックのような特定のアクションを自動実行するために利用される可能性があります。
- 開発標準:
    - **ruff**: PythonコードのLinterとFormatterとして機能し、コードスタイルと品質を自動的にチェック・修正することで、一貫性のあるコードベースを維持します。
    - **.editorconfig**: 異なるエディタやIDEを使用する開発者の間で、コードのインデントや文字コードなどのフォーマットルールを統一するために使用されます。

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
### プロジェクトルートファイル
- `README.md`: プロジェクト全体の概要、セットアップ方法、使い方、オプションなどを説明するメインのドキュメントです。
- `_config.yml`: Jekyllサイト全体の挙動を設定するファイルです。テーマ、パーマリンク構造、プラグインなどを指定します。
- `index.md`: `generate_repo_list.py`スクリプトによって生成される、GitHub Pagesサイトのトップページです。リポジトリの一覧が表示されます。
- `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を定めます。
- `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
- `.editorconfig`: 異なるエディタやIDE間で、コードのインデントスタイルや文字コードなどの基本的な書式設定を統一します。
- `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの検出方法やプラグインなどを指定します。
- `requirements.txt`: プロジェクトが実行時に必要とするPythonライブラリの一覧を定義します。
- `requirements-dev.txt`: 開発時やテスト時にのみ必要となるPythonライブラリの一覧を定義します。
- `ruff.toml`: PythonコードのLinter/Formatterである`ruff`の設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
- `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示名、アイコン、表示モードなどを定義します。
- `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権を確認するために配置されるファイルです。
- `debug_project_overview.py`: `project_overview_fetcher`モジュールの動作をデバッグするためのスクリプトです。
- `test_project_overview.py`: `project_overview_fetcher`モジュールのテストを行うスクリプトです。

### `src/generate_repo_list/` ディレクトリ（メイン処理モジュール）
- `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、Jekyll対応のMarkdownファイルを生成する、このプロジェクトのメインスクリプトです。
- `config.yml`: プロジェクト概要取得機能の有効/無効、対象ファイル名、タイムアウト時間などの技術的なパラメータを設定するファイルです。
- `strings.yml`: 生成されるMarkdownファイル内で使用される表示メッセージや文言（例: 「アクティブなリポジトリ」「アーカイブ済み」など）を管理するファイルです。
- `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形に整形・加工するロジックを提供します。
- `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動取得する機能を提供します。
- `markdown_generator.py`: 整形されたリポジトリデータをもとに、Jekyllサイトで表示されるMarkdownコンテンツを生成する役割を担います。
- `badge_generator.py`: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）を示すバッジをMarkdown形式で生成するユーティリティです。
- `date_formatter.py`: リポジトリの更新日時などを、人間が読みやすい形式に整形するユーティリティ関数を提供します。
- `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報（主要言語、使用率など）を処理・表示するためのモジュールです。
- `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、特定のバッジ情報（ビルドステータスなど）を抽出する機能を提供します。
- `statistics_calculator.py`: リポジトリのスター数やフォーク数など、統計情報を計算する機能を提供します。
- `template_processor.py`: Markdown生成に使用するテンプレートの読み込みや、動的な値の埋め込み処理を行います。
- `url_utils.py`: URLの生成や解析など、URLに関連するユーティリティ関数を提供します。
- `config_manager.py`: `config.yml`や`strings.yml`などの設定ファイルを読み込み、アプリケーション全体で利用できるように管理するモジュールです。
- `seo_template.yml`: 検索エンジン最適化(SEO)のためのメタデータや、JSON-LDテンプレートを定義するファイルです。
- `json_ld_template.json`: JSON-LD形式の構造化データ（サイト情報など）のテンプレートです。

### `tests/` ディレクトリ
- `conftest.py`: `pytest`のテスト実行時に共通で利用されるフィクスチャ（テスト用のセットアップ・クリーンアップ処理）や設定を定義します。
- `test_*.py`: 各ファイルは、特定の機能やモジュールに対する単体テストまたは結合テストを記述したものです。例えば、`test_markdown_generator.py`はMarkdown生成機能のテストを、`test_integration.py`はシステム全体の統合テストを行います。

### その他ディレクトリ
- `assets/`: GitHub Pagesサイトで使用される画像（ファビコンなど）やCSS、JavaScriptファイルなどの静的アセットを格納します。
- `generated-docs/`: 各リポジトリに存在することを想定している、プロジェクト概要ファイル（`project-overview.md`）が格納されるパスです。
- `issue-notes/`: 開発中に発生した課題や検討事項、メモなどを記録するためのディレクトリです。
- `.github_automation/check_large_files/`: GitHub Actionsと連携し、リポジトリ内に大規模なファイルが存在しないかチェックするためのスクリプト群です。
    - `check_large_files.py`: 実際に大規模ファイルチェックを行うPythonスクリプト。
    - `check-large-files.toml`: 大規模ファイルチェックの対象や閾値などの設定を定義するファイル。

## 関数詳細説明
このプロジェクトはPythonスクリプトが主要な処理を担っており、以下の役割を持つ関数が推測されます。具体的な引数や戻り値は提供された情報からは断定できないため、一般的な説明に留めます。

- **`generate_repo_list.py` 内の主要関数**:
    - `main()`:
        - **役割**: プログラムのエントリポイント。コマンドライン引数の解析、設定ファイルの読み込み、GitHubリポジトリ情報の取得、取得した情報の処理、最終的なMarkdownファイルの生成という一連のフローを制御します。
        - **引数**: なし（コマンドライン引数は内部で解析）
        - **戻り値**: なし
    - `fetch_github_repositories(username, token)`:
        - **役割**: 指定されたGitHubユーザー名と認証トークンを使用して、GitHub APIからそのユーザーのリポジトリ一覧情報を取得します。
        - **引数**: `username` (string), `token` (string, オプション)
        - **戻り値**: リポジトリ情報のリスト (list of dict)
    - `generate_markdown_output(repo_data_list, output_file_path)`:
        - **役割**: 処理済みのリポジトリデータリストを受け取り、Jekyll互換のMarkdown形式で整形し、指定されたファイルパスに出力します。
        - **引数**: `repo_data_list` (list of dict), `output_file_path` (string)
        - **戻り値**: なし

- **`project_overview_fetcher.py` 内の主要関数**:
    - `fetch_project_overview(repo_url, target_file_path, config)`:
        - **役割**: 指定されたリポジトリのURLから、`config`で指定された`target_file_path`にある`project-overview.md`ファイルを読み込み、その中の「プロジェクト概要」セクションから3行の説明を抽出します。
        - **引数**: `repo_url` (string), `target_file_path` (string), `config` (dict)
        - **戻り値**: 抽出された3行のプロジェクト概要 (list of string) または None

- **`repository_processor.py` 内の主要関数**:
    - `process_repository_data(raw_repo_data, config, strings)`:
        - **役割**: GitHub APIから取得した個々のリポジトリの生データを受け取り、必要な情報（名前、説明、URL、更新日時、言語、概要など）を抽出し、Markdown生成に適した形式に加工・整形します。
        - **引数**: `raw_repo_data` (dict), `config` (dict), `strings` (dict)
        - **戻り値**: 整形されたリポジトリ情報 (dict)

- **`markdown_generator.py` 内の主要関数**:
    - `create_repo_list_markdown(processed_repo_list, strings)`:
        - **役割**: `repository_processor`によって整形されたリポジトリデータのリストを受け取り、Jekyllの要件に合わせたMarkdown形式の文字列（リポジトリ一覧ページ全体）を生成します。
        - **引数**: `processed_repo_list` (list of dict), `strings` (dict)
        - **戻り値**: 生成されたMarkdown文字列 (string)

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-09 07:07:16 JST
