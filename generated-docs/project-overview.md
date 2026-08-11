Last updated: 2026-08-12

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンによるクロールを最適化し、LLMがリポジトリ参照に失敗する課題の緩和を目指します。
- リポジトリ一覧、各リポジトリへのリンク、バッジ表示、プロジェクト概要の自動取得などの機能を提供します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages): 静的サイトジェネレーターとしてGitHub Pagesの基盤を形成し、生成されたMarkdownファイルを美しいWebサイトとして公開します。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからのデータ取得、処理、Markdown生成に利用されます。
    - **GitHub API**: リポジトリ情報（説明、言語、スター数など）をプログラム的に取得するためのインターフェースです。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`など）の記述に用いられ、システムの振る舞いや表示内容を柔軟に管理します。
    - **TOML**: `pytest.ini`, `ruff.toml`などの設定ファイル、およびGitHubトークン管理に利用されます。
    - **JSON**: SEO最適化のためのJSON-LDテンプレートやPWAマニフェストファイルに利用されます。
- テスト: **Pytest**: Pythonプロジェクトのテストフレームワークであり、機能の正確性を検証し、品質を保証するための単体テストおよび結合テストが記述されています。
- ビルドツール:
    - **Pythonスクリプト**: 取得したデータをもとにMarkdown形式のファイルを生成する中心的な役割を担います。
    - **Jekyll** (GitHub Pages): 最終的に生成されたMarkdownファイルをHTMLページへと変換し、Webサイトとして公開する役割を担います。
- 言語機能: **Python**: 高い可読性と豊富なライブラリエコシステムを持つプログラミング言語で、本プロジェクトのデータ処理、API連携、ファイル操作の基盤となっています。
- 自動化・CI/CD: **限定的な自動化スクリプト**: `github_automation` ディレクトリ配下に、大きなファイルのチェックなど、CI/CDに繋がる可能性のあるユーティリティスクリプトが含まれていますが、プロジェクト自体はローカル開発重視とされています。
- 開発標準: **Ruff**: Pythonコードのリンター兼フォーマッターであり、コードの一貫性を保ち、可読性を向上させるための自動コードスタイルチェックおよび修正を行います。

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
-   `.editorconfig`: エディタのコードスタイル設定を定義し、複数の開発者が異なるエディタを使用しても一貫したフォーマットを保つための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   `check_large_files/`: 大きなファイルがリポジトリに含まれていないかチェックする自動化プロセスです。
        -   `README.md`: `check_large_files` プロセスの説明ドキュメントです。
        -   `check-large-files.toml`: `check_large_files` スクリプトの設定を定義するTOMLファイルです。
        -   `scripts/check_large_files.py`: 指定された閾値を超えるサイズのファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリのパターンを指定するファイルです。
-   `LICENSE`: プロジェクトがMITライセンスで公開されていることを示すファイルです。
-   `README.md`: プロジェクトの概要、目的、主な機能、設定方法、開発者向けヒントなどを記述した、プロジェクトの玄関口となるドキュメントです。
-   `_config.yml`: Jekyll（GitHub Pagesの基盤）の全体設定ファイルで、サイトのタイトル、テーマ、プラグインなどの挙動を制御します。
-   `assets/`: Webサイトで使用される画像、ファビコンなどの静的リソースを格納するディレクトリです。
    -   `favicon-*.png`: Webサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher` モジュールのデバッグを目的とした補助スクリプトです。
-   `generated-docs/`: 他のリポジトリから自動取得された `project-overview.md` ファイルが一時的に格納される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために利用されるHTMLファイルです。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイルです。これがGitHub Pagesのトップページとして表示されます。
-   `issue-notes/`: 開発中に発生した課題や検討事項をメモとして残すためのディレクトリです。
    -   `22.md`: 特定の課題番号22に関する詳細なメモや考察が記述されたMarkdownファイルです。
-   `manifest.json`: Webアプリケーションマニフェストファイルで、PWA (Progressive Web App) としての振る舞い（ホーム画面アイコン、表示モードなど）を定義します。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出ルールやオプションを定義します。
-   `requirements-dev.txt`: 開発環境やテスト実行時に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   `requirements.txt`: 本番環境でプロジェクトを実行するために必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどのページをクロールしてよいか、あるいは避けるべきかを指示するファイルです。
-   `ruff.toml`: Pythonの高速リンター/フォーマッターであるRuffの設定ファイルです。コードスタイルや静的解析のルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリ一覧を生成するシステムの主要モジュールを格納するディレクトリです。
        -   `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: プロジェクトの言語やステータスを示すバッジのMarkdownを生成する機能を提供します。
        -   `config.yml`: プロジェクト概要取得機能など、リポジトリ一覧生成に関する主要な設定パラメータを定義するYAMLファイルです。
        -   `config_manager.py`: YAML形式の設定ファイルを読み込み、管理するためのユーティリティモジュールです。
        -   `date_formatter.py`: GitHub APIから取得した日付情報を、ユーザーにとって読みやすい形式に整形する機能を提供します。
        -   `generate_repo_list.py`: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために利用される構造化データ（JSON-LD）のテンプレートです。
        -   `language_info.py`: 各リポジトリの主要言語とその統計情報を取得・処理する機能を提供します。
        -   `markdown_generator.py`: 取得・整形されたリポジトリ情報とテンプレートをもとに、Markdown形式のコンテンツを生成するモジュールです。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のMarkdownファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出する機能を提供します。
        -   `readme_badge_extractor.py`: 各リポジトリのREADMEファイルから、既存のバッジ情報（画像URLなど）を解析・抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得したリポジトリの生データを、Markdown生成に適した形式に整形・加工する主要なロジックを提供します。
        -   `seo_template.yml`: 検索エンジン最適化（SEO）に関連するメタ情報や記述のテンプレートを定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算・整形する機能を提供します。
        -   `strings.yml`: プロジェクト内で使用される各種表示メッセージや文言を一元的に管理するためのYAMLファイルです。
        -   `template_processor.py`: Jinja2などのテンプレートエンジンを用いて、Markdown生成に使用されるテンプレートのレンダリング（データ埋め込み）を行うモジュールです。
        -   `url_utils.py`: GitHub APIエンドポイントのURL構築など、URLに関するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: pytestのフィクスチャやヘルパー関数を定義し、テスト間で共通のセットアップやリソースを提供します。
    -   `test_badge_generator_integration.py`: `badge_generator` の統合的な動作を検証するテストです。
    -   `test_check_large_files.py`: `check_large_files` スクリプトの機能を検証するテストです。
    -   `test_config.py`: `config_manager` を使った設定ファイルの読み込みやアクセスが正しく行われるかを検証するテストです。
    -   `test_date_formatter.py`: `date_formatter` の日付フォーマット機能が正しく動作するかを検証するテストです。
    -   `test_environment.py`: プロジェクトの実行環境が正しく設定されているかを確認するテストです。
    -   `test_integration.py`: システム全体の主要なフローが正しく連携して動作するかを検証する統合テストです。
    -   `test_markdown_generator.py`: `markdown_generator` が正しくMarkdownコンテンツを生成するかを検証するテストです。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher` が期待通りにプロジェクト概要を抽出できるかを検証するテストです。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor` がREADMEからバッジ情報を正確に抽出できるかを検証するテストです。
    -   `test_repository_processor.py`: `repository_processor` がGitHub APIからのリポジトリデータを正しく処理・整形できるかを検証するテストです。

## 関数詳細説明
-   `generate_repo_list.py` の `main()` 関数:
    -   役割: コマンドライン引数を解析し、設定ファイルを読み込み、GitHub APIからリポジトリ情報を取得・処理し、最終的にMarkdownファイルを生成するプロジェクトの主要な実行フローを制御します。
    -   引数: なし (コマンドライン引数は内部で処理されます)
    -   戻り値: なし
-   `config_manager.py` の `load_config(config_path)` 関数:
    -   役割: 指定されたパスにあるYAML形式の設定ファイル（例: `config.yml`, `strings.yml`）を読み込み、Pythonの辞書オブジェクトとして返します。
    -   引数: `config_path` (str): 読み込む設定ファイルのファイルパス。
    -   戻り値: `dict`: 読み込んだ設定内容を格納した辞書。
-   `repository_processor.py` の `fetch_repositories(username, token)` 関数:
    -   役割: 指定されたGitHubユーザー名とアクセストークンを使用し、GitHub APIを通じてそのユーザーが所有するすべてのリポジトリの生データを取得します。
    -   引数: `username` (str): GitHubのユーザー名, `token` (str): GitHub個人アクセストークン。
    -   戻り値: `list[dict]`: 取得したリポジトリ情報（各リポジトリが辞書形式）のリスト。
-   `repository_processor.py` の `process_repository_data(repo_data)` 関数:
    -   役割: GitHub APIから取得した単一のリポジトリの生データを受け取り、Markdown生成や表示に適した形に整形・加工します。不要な情報を除外し、必要なデータを抽出・変換します。
    -   引数: `repo_data` (dict): 単一リポジトリのGitHub APIからの生データ。
    -   戻り値: `dict`: 整形され、表示に適したリポジトリ情報。
-   `project_overview_fetcher.py` の `get_project_overview(repo_name, owner, config)` 関数:
    -   役割: 特定のリポジトリ (`repo_name`, `owner`) に存在する `generated-docs/project-overview.md` ファイルから、設定 (`config`) に基づいて「プロジェクト概要」セクションの3行説明を抽出します。
    -   引数: `repo_name` (str): 対象リポジトリの名前, `owner` (str): リポジトリの所有者名, `config` (dict): プロジェクト概要取得機能に関する設定。
    -   戻り値: `str`: 抽出されたプロジェクト概要の3行説明、または抽出できなかった場合は空文字列。
-   `language_info.py` の `get_language_stats(repo_name, owner, token)` 関数:
    -   役割: 指定されたリポジトリ (`repo_name`, `owner`) の言語使用統計（各言語のバイト数など）をGitHub API経由で取得します。
    -   引数: `repo_name` (str): 対象リポジトリの名前, `owner` (str): リポジトリの所有者名, `token` (str): GitHub個人アクセストークン。
    -   戻り値: `dict`: 各言語とそのバイト数をマッピングした辞書。
-   `badge_generator.py` の `generate_badge_markdown(language_stats)` 関数:
    -   役割: `get_language_stats` で取得した言語統計情報に基づき、Webサイトに表示する言語バッジのMarkdown文字列を生成します。
    -   引数: `language_stats` (dict): 言語とそのバイト数を格納した辞書。
    -   戻り値: `str`: 生成されたバッジのMarkdown文字列。
-   `date_formatter.py` の `format_date(iso_date_string)` 関数:
    -   役割: GitHub APIから返されるISO 8601形式の日付文字列（例: "2023-01-01T12:00:00Z"）を、人間が読みやすい形式（例: "2023年1月1日"）に変換します。
    -   引数: `iso_date_string` (str): フォーマットするISO形式の日付文字列。
    -   戻り値: `str`: フォーマットされた日付文字列。
-   `statistics_calculator.py` の `calculate_repository_statistics(repo_data)` 関数:
    -   役割: 単一リポジトリの生データから、スター数、フォーク数、コミット数などの数値情報を抽出し、表示に適した統計情報として計算・整形します。
    -   引数: `repo_data` (dict): 単一リポジトリの生データ。
    -   戻り値: `dict`: 計算された統計情報。
-   `readme_badge_extractor.py` の `extract_badges_from_readme(readme_content)` 関数:
    -   役割: リポジトリのREADMEファイルのMarkdownコンテンツから、プロジェクトのステータスや技術を示すバッジの画像URLなどの情報を解析して抽出します。
    -   引数: `readme_content` (str): READMEファイルのMarkdown文字列。
    -   戻り値: `list[str]`: 抽出されたバッジURL（または関連情報）のリスト。
-   `markdown_generator.py` の `generate_markdown(repo_list, output_file, templates, strings)` 関数:
    -   役割: 処理済みのリポジトリ情報のリスト、Markdownテンプレート、表示文言データを用いて、最終的なMarkdownコンテンツを生成し、指定されたファイル (`output_file`) に書き出します。
    -   引数: `repo_list` (list[dict]): 処理済みリポジトリ情報のリスト, `output_file` (str): 出力するMarkdownファイルのパス, `templates` (dict): Markdown生成に使用するテンプレート群, `strings` (dict): 表示文言を管理する辞書。
    -   戻り値: なし
-   `template_processor.py` の `render_template(template_string, data)` 関数:
    -   役割: プレースホルダーを含むテンプレート文字列に、動的なデータ (`data`) を埋め込み、最終的なレンダリング済み文字列を生成します。Jinja2のようなテンプレートエンジンが内部的に利用されます。
    -   引数: `template_string` (str): プレースホルダーを含むテンプレート文字列, `data` (dict): テンプレートに埋め込むデータ。
    -   戻り値: `str`: データが埋め込まれたレンダリング済み文字列。
-   `url_utils.py` の `build_github_api_url(username, endpoint)` 関数:
    -   役割: GitHub APIのベースURLと指定されたユーザー名、特定のエンドポイント（例: `repos`）を組み合わせて、APIリクエストを行うための完全なURLを構築します。
    -   引数: `username` (str): GitHubユーザー名, `endpoint` (str): アクセスするAPIのエンドポイントパス。
    -   戻り値: `str`: 構築されたGitHub APIのURL。

## 関数呼び出し階層ツリー
```
main (generate_repo_list.py)
├── load_config (config_manager.py)
├── fetch_repositories (repository_processor.py)
│   └── build_github_api_url (url_utils.py)
├── process_each_repository (internal loop)
│   ├── process_repository_data (repository_processor.py)
│   ├── get_project_overview (project_overview_fetcher.py)
│   ├── get_language_stats (language_info.py)
│   ├── generate_badge_markdown (badge_generator.py)
│   ├── format_date (date_formatter.py)
│   ├── calculate_repository_statistics (statistics_calculator.py)
│   └── extract_badges_from_readme (readme_badge_extractor.py)
└── generate_markdown (markdown_generator.py)
    └── render_template (template_processor.py)

---
Generated at: 2026-08-12 07:17:20 JST
