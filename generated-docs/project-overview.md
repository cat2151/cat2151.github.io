Last updated: 2026-10-25

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、JekyllベースのGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- リポジトリ情報からSEOに最適化されたMarkdownファイルを生成し、Webサイトに公開します。
- これにより、検索エンジンやLLMによるリポジトリの参照性を向上させ、情報発見と開発効率の向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages, Markdown**
  静的サイトジェネレータJekyll上で動作するGitHub Pagesサイト向けに、標準的なMarkdown形式でコンテンツを生成します。生成されたMarkdownは、最終的にGitHub PagesによってHTMLに変換され公開されます。
- 音楽・オーディオ: (該当なし)
  このプロジェクトの目的とは直接関連しないため、該当する技術は使用されていません。
- 開発ツール: **Python, Pytest, Ruff, Git/GitHub, YAML, TOML**
  Pythonがメインのプログラミング言語であり、テストにはPytest、コードスタイルの統一にはRuffを使用しています。ソースコード管理とホスティングにはGitおよびGitHubを利用し、設定管理にはYAML、シークレット管理にはTOMLファイルを使用しています。
- テスト: **Pytest**
  Pythonコードの単体テストや結合テストフレームワークとしてPytestを利用し、コードの品質と信頼性を確保しています。
- ビルドツール: **Pythonスクリプト**
  特定の外部ビルドツールは使用せず、Pythonスクリプト自体がGitHub APIからの情報取得、データ処理、Markdownファイル生成といった一連の「ビルド」プロセスを実行します。
- 言語機能: **Python**
  GitHub APIとの連携、ファイル操作、文字列処理、データ構造の操作など、プロジェクトの主要なロジックを実装するためにPythonが活用されています。
- 自動化・CI/CD: **GitHub API**
  GitHub APIを直接利用することで、リポジトリ情報の取得プロセスを自動化しています。これにより、手動での情報収集や更新の手間を省き、常に最新のリポジトリ一覧を生成することが可能になります。
- 開発標準: **Ruff**
  Ruffを使用することで、コードの品質を維持し、プロジェクト全体で統一されたコーディングスタイルを強制しています。これにより、コードの可読性と保守性が向上します。

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
- **.editorconfig**: 異なるエディタやIDE間で基本的なコーディングスタイル（インデント、エンコードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub関連の自動化スクリプトや設定を格納するディレクトリです。
    - **.github_automation/check_large_files/**: 大容量ファイルを検出するためのスクリプト群です。
        - **README.md**: `check_large_files` 機能の説明ドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェックに関する設定を定義するファイルです。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理対象外とするファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、使い方などを説明するメインドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの全体設定を定義します。
- **assets/**: Webサイトで使用される静的なアセット（画像、CSS、JavaScriptなど）を格納するディレクトリです。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザタブなどに表示される小さなアイコン）画像ファイル群です。
- **debug_project_overview.py**: `project_overview` 機能のデバッグやテスト実行を補助するためのスクリプトです。
- **generated-docs/**: GitHub Pagesサイト用に自動生成されたドキュメントや、各リポジトリの概要ファイルなどが格納されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイト所有権の確認に使用されるファイルです。
- **index.md**: 生成されたリポジトリ一覧のメインページとなるMarkdownファイルで、GitHub Pagesのトップページとして表示されます。
- **issue-notes/**: 開発中の課題や検討事項、メモなどを記録するためのディレクトリです。
    - **22.md**: 特定の課題（Issue #22）に関する詳細なメモや情報が記述されたMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となる設定ファイルで、アプリの表示方法やアイコンなどを定義します。
- **pytest.ini**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの発見ルールやプラグインなどを定義します。
- **requirements-dev.txt**: 開発環境やテスト環境でのみ必要となるPythonパッケージの依存関係を定義するファイルです。
- **requirements.txt**: プロジェクトが本番環境で実行される際に必要となるPythonパッケージの依存関係を定義するファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。リンティングルールやコードフォーマットの基準を定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **generate_repo_list/**: GitHubリポジトリ一覧の生成に関するメインロジックを含むPythonパッケージです。
        - **__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
        - **badge_generator.py**: リポジトリに関連するバッジ（例: ビルドステータス、ライセンス）のMarkdown生成ロジックを管理します。
        - **config.yml**: プロジェクトの技術的な設定パラメータ（例: `project_overview` 機能の有効/無効、対象ファイルなど）を定義するYAMLファイルです。
        - **config_manager.py**: `config.yml` やシークレットファイル (`secrets.toml` など) の読み込みと管理を行うモジュールです。
        - **date_formatter.py**: 日付情報を読みやすい形式にフォーマットするためのユーティリティ関数を提供します。
        - **generate_repo_list.py**: GitHubリポジトリ一覧生成プロセスのメインエントリーポイントとなるスクリプトです。GitHub APIからの情報取得、データ処理、Markdown生成の全体フローを制御します。
        - **json_ld_template.json**: JSON-LD形式の構造化データテンプレートで、SEO最適化のために検索エンジンにリッチな情報を提供します。
        - **language_info.py**: リポジトリで使用されているプログラミング言語の情報（割合など）を処理するロジックを管理します。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを実装します。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動取得するロジックを管理します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ（shields.ioなど）の情報を抽出し、表示に利用するロジックを管理します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、アプリケーションが扱いやすい形式に処理・整形するロジックを管理します。
        - **seo_template.yml**: SEO関連のメタデータや構造化データに関する設定やテンプレートを定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、整理するロジックを管理します。
        - **strings.yml**: アプリケーション内で使用される表示メッセージや文言を多言語対応や一元管理のために定義するYAMLファイルです。
        - **template_processor.py**: Markdownテンプレートやその他のテキストテンプレートにデータを適用し、最終的な出力を生成するロジックを管理します。
        - **url_utils.py**: URLの生成、検証、パースなど、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview` 機能の単体テストを記述したスクリプトです。
- **tests/**: プロジェクトのテストコードを格納するディレクトリです。
    - **conftest.py**: Pytestのフィクスチャ（テスト実行前に準備する共通データや設定）やヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator` モジュールの統合テストを記述したファイルです。
    - **test_check_large_files.py**: 大容量ファイルチェック (`.github_automation/check_large_files/scripts/check_large_files.py`) スクリプトのテストを記述したファイルです。
    - **test_config.py**: `config_manager` モジュールなど、設定ファイルの読み込みに関するテストを記述したファイルです。
    - **test_date_formatter.py**: `date_formatter` モジュールの日付フォーマット関数の単体テストを記述したファイルです。
    - **test_environment.py**: 実行環境に関する前提条件や設定のテストを記述したファイルです。
    - **test_integration.py**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テストを記述したファイルです。
    - **test_markdown_generator.py**: `markdown_generator` モジュールのMarkdown生成ロジックの単体テストを記述したファイルです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールのプロジェクト概要取得機能の単体テストを記述したファイルです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor` モジュールのREADMEからのバッジ抽出機能の単体テストを記述したファイルです。
    - **test_repository_processor.py**: `repository_processor` モジュールのリポジトリデータ処理ロジックの単体テストを記述したファイルです。

## 関数詳細説明
- `src/generate_repo_list/badge_generator.py`
    - `generate_badge_markdown(repo: dict) -> str`: 特定のリポジトリ情報に基づいて、そのリポジトリに表示するためのバッジ（例: 言語バッジ、スター数バッジ）のMarkdown文字列を生成します。
- `src/generate_repo_list/config_manager.py`
    - `load_config(config_path: str) -> dict`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書として返します。
    - `load_secrets(secrets_path: str) -> dict`: 指定されたパスからTOML形式のシークレットファイルを読み込み、機密情報（例: GitHubトークン）を辞書として返します。
- `src/generate_repo_list/date_formatter.py`
    - `format_date(iso_date_string: str) -> str`: ISO 8601形式の日付文字列（例: "2023-01-01T12:34:56Z"）を受け取り、人間が読みやすい形式（例: "2023年1月1日"）に整形して返します。
- `src/generate_repo_list/generate_repo_list.py`
    - `main()`: プログラムのエントリーポイントです。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の全体フローをオーケストレーションします。
    - `_parse_arguments() -> argparse.Namespace`: コマンドライン引数を解析し、ユーザー名、出力ファイル名、処理リミット数などを取得します。
- `src/generate_repo_list/language_info.py`
    - `get_language_breakdown(repo_languages: dict) -> dict`: リポジトリの言語ごとのバイト数情報を受け取り、各言語の使用割合などを計算して返します。
- `src/generate_repo_list/markdown_generator.py`
    - `generate_markdown(repositories: list, output_path: str, config: dict, strings: dict) -> None`: 処理されたリポジトリ情報と設定、文言データを使用して、最終的なリポジトリ一覧のMarkdownファイルを指定されたパスに生成します。
    - `_generate_repo_section(repo: dict, strings: dict) -> str`: 個々のリポジトリデータを受け取り、そのリポジトリの詳細（タイトル、概要、バッジなど）を含むMarkdownセクションを生成します。
- `src/generate_repo_list/project_overview_fetcher.py`
    - `fetch_project_overview(repo_url: str, config: dict) -> Optional[str]`: 指定されたリポジトリのURLと設定に基づき、リモートリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、返します。
    - `_extract_overview_lines(content: str, section_title: str) -> Optional[str]`: Markdownコンテンツから指定されたセクションタイトルの下に続く3行の説明を抽出します。
- `src/generate_repo_list/readme_badge_extractor.py`
    - `extract_badges_from_readme(readme_content: str) -> list`: リポジトリのREADMEファイルのMarkdownコンテンツを解析し、含まれるバッジ（画像リンク）のURLやaltテキスト情報をリストとして抽出します。
- `src/generate_repo_list/repository_processor.py`
    - `fetch_repositories(username: str, github_token: str, limit: Optional[int] = None) -> list`: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。必要に応じて処理するリポジトリ数に上限を設けることができます。
    - `process_repository_data(repo_data: dict, project_overview_config: dict) -> dict`: GitHub APIから取得した個々の生のリポジトリデータから、必要な情報を抽出し、整形・強化します。`project_overview_fetcher` を呼び出して概要を取得する役割も持ちます。
- `src/generate_repo_list/statistics_calculator.py`
    - `calculate_repo_statistics(repo_list: list) -> dict`: 処理済みのリポジトリリスト全体から、合計スター数、フォーク数、主要言語の分布など、全体的な統計情報を計算して返します。
- `src/generate_repo_list/template_processor.py`
    - `apply_template(template_content: str, data: dict) -> str`: プレースホルダーを含むテンプレート文字列に、提供されたデータ辞書を適用して最終的な文字列を生成します。
- `src/generate_repo_list/url_utils.py`
    - `construct_github_api_url(username: str, repo_name: Optional[str] = None) -> str`: 指定されたGitHubユーザー名と任意のリポジトリ名に基づいて、GitHub APIのエンドポイントURLを構築します。
    - `is_valid_url(url: str) -> bool`: 与えられた文字列が有効なURL形式であるかどうかを検証し、真偽値を返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-25 07:10:29 JST
