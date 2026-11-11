Last updated: 2026-11-12

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pagesサイト用にMarkdownファイルを自動生成するシステムです。
- SEOに最適化されたリポジトリ一覧ページをJekyll形式で出力し、Web検索やLLMからの参照性を向上させます。
- 各リポジトリの概要文やバッジ、統計情報を自動で組み込み、情報の充実と可視化を実現します。

## 技術スタック
- フロントエンド: **GitHub Pages / Jekyll** (静的サイトホスティングとブログジェネレーター、生成されたMarkdownファイルをレンダリングするために使用)、**Markdown** (リポジトリ一覧コンテンツの記述形式)
- 音楽・オーディオ: 特になし (本プロジェクトには該当する技術は使用されていません)
- 開発ツール: **GitHub API** (リポジトリ情報の取得に利用)、**Pytest** (Pythonコードのテストフレームワーク)、**Ruff** (Pythonコードのリンター兼フォーマッター)
- テスト: **Pytest** (Pythonコードのユニットテストおよび統合テストフレームワーク)
- ビルドツール: **Python** (スクリプト実行環境として利用、リポジトリ情報の取得・処理・Markdown生成の主要なロジックを担います)
- 言語機能: **Python** (主要なプログラミング言語として、リポジトリ情報処理、ファイル生成、API連携などに利用)
- 自動化・CI/CD: **Pythonスクリプト** (GitHub APIを利用したリポジトリ一覧の自動生成プロセス自体が自動化の中核をなします)
- 開発標準: **Ruff** (コードスタイルと品質を統一するためのリンターおよびフォーマッター)、**.editorconfig** (IDEやエディタ全体でコードスタイルを統一するための設定ファイル)

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
-   `.editorconfig`: 異なる開発環境間でのコーディングスタイル（インデント、改行コードなど）の一貫性を定義するファイル。
-   `.github_automation/`: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリ。
    -   `check_large_files/`: 大容量ファイルのチェックに関するスクリプトや設定。
        -   `README.md`: このディレクトリ内の機能に関する説明。
        -   `check-large-files.toml`: 大容量ファイルチェックの設定ファイル。
        -   `scripts/`: 大容量ファイルチェックを実行するPythonスクリプト。
            -   `check_large_files.py`: 実際に大容量ファイルを検出するPythonスクリプト。
-   `.gitignore`: Gitが追跡しないファイルやディレクトリを指定するファイル。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）。
-   `README.md`: プロジェクトの概要、目的、主な機能、使い方などを記述したメインドキュメント。
-   `_config.yml`: Jekyllサイト全体の挙動を制御する設定ファイル。GitHub Pagesの設定に利用されます。
-   `assets/`: ウェブサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズ。
-   `debug_project_overview.py`: `project_overview_fetcher`機能のデバッグ用途で使用されるスクリプト。
-   `generated-docs/`: プロジェクト実行時に自動生成されるドキュメントやデータが格納されることを想定したディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権確認で使用される認証ファイル。
-   `index.md`: GitHub Pagesサイトのトップページとして表示されるMarkdownファイル。リポジトリ一覧がここに生成されます。
-   `issue-notes/`: 課題や検討事項、開発メモなどを記録するためのディレクトリ。
    -   `22.md`: 特定の課題に関連するメモファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のメタデータ定義ファイル。ウェブアプリの表示設定などを指定します。
-   `pytest.ini`: `pytest`フレームワークの挙動を設定するファイル。
-   `requirements-dev.txt`: 開発時およびテスト時に必要なPythonライブラリの依存関係リスト。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行するために必要なPythonライブラリの依存関係リスト。
-   `robots.txt`: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、あるいは避けるべきかを指示するファイル。
-   `ruff.toml`: `Ruff`（Pythonのリンター兼フォーマッター）の設定ファイル。コードのスタイルや品質ルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   `__init__.py`: `src`ディレクトリがPythonパッケージであることを示すファイル。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成の主要なロジックを格納するPythonパッケージ。
        -   `__init__.py`: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリに表示されるバッジ（例: 言語、ライセンス）のMarkdownを生成するロジックを扱います。
        -   `config.yml`: プロジェクト概要取得機能などの技術的パラメータや、その他のプロジェクト固有の設定を定義するYAMLファイル。
        -   `config_manager.py`: 設定ファイル（`config.yml`など）の読み込みと管理を行うモジュール。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理を orchestrate します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のためのJSON-LD形式のデータ構造テンプレート。
        -   `language_info.py`: プログラミング言語に関する情報を処理し、表示に活用するロジック。
        -   `markdown_generator.py`: リポジトリ情報からSEO最適化されたMarkdown形式のコンテンツを生成するコアロジックを担います。
        -   `project_overview_fetcher.py`: 各リポジトリの`generated-docs/project-overview.md`から3行のプロジェクト概要を自動取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するロジック。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換するモジュール。
        -   `seo_template.yml`: SEOメタデータやキーワードなどの設定テンプレート。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（スター数、フォーク数など）を計算するロジック。
        -   `strings.yml`: UIに表示されるメッセージや文言を一元管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: Markdownテンプレートを処理し、動的なデータを埋め込むためのロジック。
        -   `url_utils.py`: URLの生成や検証など、URLに関連するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`機能のユニットテストを行うスクリプト。
-   `tests/`: プロジェクト全体のテストコードが格納されるディレクトリ。
    -   `conftest.py`: `pytest`のテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義するファイル。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テスト。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテスト。
    -   `test_config.py`: 設定ファイルの読み込みや解析に関するテスト。
    -   `test_date_formatter.py`: 日付フォーマット機能のテスト。
    -   `test_environment.py`: 環境設定や依存関係のテスト。
    -   `test_integration.py`: プロジェクト全体の主要なフローに関する統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリデータ処理機能のテスト。

## 関数詳細説明
関数の詳細な情報（引数、戻り値など）は提供されていないため、各ファイルが持つと想定される主要な関数の役割について、一般的な説明を行います。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main()`: プログラムのエントリーポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といった一連の処理を調整し、最終的なリポジトリ一覧ファイルを生成します。
-   **`src/generate_repo_list/badge_generator.py`**
    -   `generate_badge_markdown(badge_info)`: 指定されたバッジ情報に基づいて、Markdown形式のバッジ文字列を生成します。
-   **`src/generate_repo_list/config_manager.py`**
    -   `load_config(file_path)`: 指定されたYAMLファイルから設定情報を読み込み、ディクショナリとして返します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   `format_date(date_str, format_string)`: 日付文字列を指定されたフォーマットで整形します。
-   **`src/generate_repo_list/language_info.py`**
    -   `get_language_display_name(language_code)`: 言語コードから表示用の名前を取得します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_repo_list_markdown(repos_data)`: 処理されたリポジトリデータを受け取り、リポジトリ一覧のMarkdownコンテンツを生成します。
    -   `generate_repo_card_markdown(repo_data)`: 個々のリポジトリの情報を基に、そのリポジトリのカード形式のMarkdownを生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLから`project-overview.md`を読み込み、設定に基づいて概要の3行を抽出して返します。
-   **`src/generate_repo_list/readme_badge_extractor.py`**
    -   `extract_badges_from_readme(readme_content)`: READMEのコンテンツから特定の形式のバッジ情報を解析し、抽出します。
-   **`src/generate_repo_list/repository_processor.py`**
    -   `process_repositories(username, api_token, config, limit)`: GitHub APIからユーザーのリポジトリを取得し、必要な情報を抽出し、整形する一連の処理を実行します。
-   **`src/generate_repo_list/statistics_calculator.py`**
    -   `calculate_repo_statistics(repo_data)`: リポジトリのデータからスター数、フォーク数などの統計情報を計算します。
-   **`src/generate_repo_list/template_processor.py`**
    -   `render_template(template_path, data)`: 指定されたテンプレートファイルとデータを用いて、最終的なコンテンツをレンダリングします。
-   **`src/generate_repo_list/url_utils.py`**
    -   `build_github_api_url(username)`: 指定されたユーザー名に基づいてGitHub APIのエンドポイントURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-12 07:07:29 JST
