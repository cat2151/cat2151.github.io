Last updated: 2026-09-11

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得します。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- GitHub Pagesの検索エンジン可視性を高め、LLMによるリポジトリ参照も支援します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースの静的サイトホスティング), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Python: 主要なスクリプト言語として、リポジトリ情報の取得・処理・Markdown生成に利用されます。
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の読み込みに使用されます。
    - requests: GitHub APIとの通信を行い、リポジトリ情報を取得するために使用されます。
    - toml: GitHubトークンなどの秘密情報を設定ファイル (`secrets.toml`) から読み込むために使用されます。
    - argparse: コマンドライン引数 (`--username`, `--output`, `--limit`) の解析に使用されます。
- テスト:
    - pytest: Pythonプロジェクトの単体テストおよび統合テストを実行するためのテストフレームワークです。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py` が直接コンテンツ生成の役割を担い、特定のビルドツールは使用しません。
- 言語機能:
    - Pythonの標準機能: プロジェクトはPythonの基本的な構文と標準ライブラリを活用しています。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation/check_large_files` ディレクトリの存在から、コード品質チェックやデプロイなどの自動化にGitHub Actionsが利用されている可能性があります。
- 開発標準:
    - ruff: Pythonコードのスタイルチェックとフォーマットを行うためのリンターおよびフォーマッターです (`ruff.toml` で設定)。
    - EditorConfig: 異なるエディタ間でのコーディングスタイル (インデント、改行コードなど) を統一するための設定ファイルです (`.editorconfig` で設定)。

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
-   **googled947dc864c270e07.html**: Google Search Consoleのサイト認証に使用される空のHTMLファイルです。
-   **README.md**: プロジェクトの目的、背景、機能、使い方、設定方法、ライセンスなど、プロジェクト全体の概要を説明する主要なドキュメントファイルです。
-   **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどのコーディングスタイルを統一するための設定ファイルです。
-   **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを指定するファイルです。
-   **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
-   **_config.yml**: Jekyll (GitHub Pagesで使用される静的サイトジェネレータ) のサイト全体の挙動や設定を定義するファイルです。
-   **assets/**: GitHub Pagesサイトで利用される画像やファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
-   **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトや設定を格納するディレクトリです。
    -   `check_large_files/`: 大容量ファイルの存在をチェックする自動化スクリプトを格納するサブディレクトリです。
        -   `README.md`: `check_large_files` 機能の説明ドキュメントです。
        -   `check-large-files.toml`: 大容量ファイルチェックの設定ファイルです。
        -   `scripts/check_large_files.py`: 指定された閾値を超える大容量ファイルを検出するPythonスクリプトです。
-   **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグや単体テストを目的としたスクリプトです。
-   **generated-docs/**: 各リポジトリから取得した `project-overview.md` など、自動生成されたドキュメントを一時的に格納する、またはその参照パスを示すディレクトリです。
-   **index.md**: `generate_repo_list.py` スクリプトによって最終的に生成される、リポジトリ一覧のMarkdownファイルです。これがGitHub Pagesのメインページとして表示されます。
-   **issue-notes/**: 課題に関するメモや詳細情報を格納するディレクトリです。
    -   `22.md`: 特定の課題 (Issue #22 など) に関するメモです。
-   **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するファイルで、ホーム画面への追加やオフライン対応などの機能を提供します。
-   **pytest.ini**: `pytest` テストフレームワークの動作を設定するファイルです (例: テストファイルの検索パターン、追加オプション)。
-   **requirements.txt**: プロジェクトの本番稼働に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **requirements-dev.txt**: 開発時およびテスト時にのみ必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **robots.txt**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
-   **ruff.toml**: Pythonコードの整形と静的解析を行う `ruff` ツールの設定ファイルです。
-   **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを含むパッケージです。
        -   `__init__.py`: Pythonパッケージであることを示します。
        -   `badge_generator.py`: リポジトリの言語やステータスなどを示すバッジのMarkdownを生成する機能を提供します。
        -   `config.yml`: プロジェクト概要取得機能など、`generate_repo_list` の動作を設定するYAMLファイルです。
        -   `config_manager.py`: `config.yml` などの設定ファイルを読み込み、プログラム内で利用可能な形式で管理するモジュールです。
        -   `date_formatter.py`: 日付や時刻の情報を特定のフォーマット文字列に変換するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: このプロジェクトのメインスクリプトであり、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成までの一連のプロセスをオーケストレーションします。
        -   `json_ld_template.json`: 検索エンジン最適化 (SEO) のために構造化データを記述するJSON-LD形式のテンプレートファイルです。
        -   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に変換するモジュールです。
        -   `markdown_generator.py`: 取得・処理されたリポジトリ情報から、最終的なリポジトリ一覧のMarkdownコンテンツを生成するコアロジックを実装しています。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル (`generated-docs/project-overview.md` など) からプロジェクトの3行概要を抽出し、取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから既存のバッジ情報を解析し、抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報のみを抽出し、さらに表示や処理に適した形に整形するモジュールです。
        -   `seo_template.yml`: SEO関連のメタデータや、Jekyllサイトの `<head>` タグ内に挿入される情報のためのテンプレートを定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        -   `strings.yml`: ユーザーインターフェースに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。
        -   `template_processor.py`: MarkdownやHTMLのテンプレートを読み込み、変数置換などを行って最終的なコンテンツを生成する汎用的な処理を提供します。
        -   `url_utils.py`: URLの解析、生成、検証など、URL関連のユーティリティ関数をまとめたモジュールです。
-   **test_project_overview.py**: `project_overview_fetcher` モジュールのテストスクリプトです。
-   **tests/**: プロジェクトのテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest` のテスト実行時に共通で利用されるフィクスチャやヘルパー関数を定義するファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator` の統合テストです。
    -   `test_check_large_files.py`: `check_large_files.py` スクリプトのテストです。
    -   `test_config.py`: 設定ファイルの読み込みや管理を行うモジュール (`config_manager`) のテストです。
    -   `test_date_formatter.py`: 日付フォーマットユーティリティ (`date_formatter`) のテストです。
    -   `test_environment.py`: テスト環境が正しくセットアップされているかを確認するテストです。
    -   `test_integration.py`: プロジェクト全体の主要な機能が正しく連携するかを検証する統合テストです。
    -   `test_markdown_generator.py`: `markdown_generator` モジュールのテストです。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールのテストです。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールのテストです。
    -   `test_repository_processor.py`: `repository_processor` モジュールのテストです。

## 関数詳細説明
-   **src/generate_repo_list/generate_repo_list.py**:
    -   `main()`: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ一覧生成の全体フローを制御します。
    -   `generate_list(username, output_file, limit)`: 指定されたユーザー名のリポジトリ情報を取得し、整形して指定のファイルにMarkdown形式で出力する主要な関数です。
-   **src/generate_repo_list/badge_generator.py**:
    -   `generate_badge_markdown(repo_data)`: リポジトリのメタデータ（言語、トピック、アーカイブ状態など）に基づいて、視覚的なバッジを表すMarkdown文字列を生成します。
-   **src/generate_repo_list/config_manager.py**:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、設定オブジェクトとして返します。
    -   `get_value(key_path)`: ドット区切りパス (`project_overview.enabled`) を使用して、読み込んだ設定値を取得します。
-   **src/generate_repo_list/date_formatter.py**:
    -   `format_date(date_string, format_type)`: 日付文字列を解析し、指定されたフォーマットタイプ（例: 短縮形、詳細形）で整形された文字列を返します。
-   **src/generate_repo_list/markdown_generator.py**:
    -   `generate_repo_section(repo_info, strings, config)`: 個々のリポジトリ情報を受け取り、そのリポジトリ表示用のMarkdownセクション（タイトル、説明、バッジなど）を生成します。
    -   `generate_index_markdown(all_repo_data, strings, config, seo_data)`: すべてのリポジトリデータと関連情報を結合し、最終的な `index.md` ファイルのコンテンツ全体を生成します。
-   **src/generate_repo_list/project_overview_fetcher.py**:
    -   `fetch_project_overview(repo_url, target_file, section_title, config)`: 指定されたリポジトリのURLから、特定のファイル (`target_file`) を取得し、その中の指定されたセクション (`section_title`) からプロジェクト概要の3行説明を抽出します。
-   **src/generate_repo_list/repository_processor.py**:
    -   `fetch_and_process_repositories(username, token, limit, config)`: GitHub APIを介して指定されたユーザーのリポジトリ情報を取得し、それを整形・加工して、プログラムで扱いやすい形式のデータ構造として返します。
-   **src/generate_repo_list/template_processor.py**:
    -   `apply_template(template_content, data)`: テンプレート文字列とデータ辞書を受け取り、テンプレート内のプレースホルダーを対応するデータで置換した結果の文字列を返します。
-   **src/generate_repo_list/url_utils.py**:
    -   `build_repo_url(username, repo_name)`: GitHubのユーザー名とリポジトリ名から、そのリポジトリのURLを構築します。

## 関数呼び出し階層ツリー
```
main() (src/generate_repo_list/generate_repo_list.py)
├─── generate_list()
│    ├─── config_manager.load_config()
│    ├─── repository_processor.fetch_and_process_repositories()
│    │    └─── project_overview_fetcher.fetch_project_overview() (オプション)
│    ├─── markdown_generator.generate_index_markdown()
│    │    ├─── markdown_generator.generate_repo_section()
│    │    │    ├─── badge_generator.generate_badge_markdown()
│    │    │    └─── date_formatter.format_date()
│    │    └─── template_processor.apply_template()
│    └─── (ファイル出力処理)
└─── (コマンドライン引数解析)

---
Generated at: 2026-09-11 07:11:43 JST
