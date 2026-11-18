Last updated: 2026-11-19

# Project Overview

## プロジェクト概要
- GitHub API を活用し、GitHub Pages サイト向けのリポジトリ一覧を自動生成します。
- SEO最適化されたMarkdownファイルを生成し、リポジトリの検索エンジン可視性を向上させます。
- 各リポジトリの概要を自動取得し、LLMからの参照性向上と開発効率化に貢献します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーターで、本システムが生成するMarkdownファイルはこのJekyllによって処理されます。
    - **Markdown**: 生成されるリポジトリ一覧コンテンツの形式。JekyllによってHTMLに変換され、Webサイトとして公開されます。
- 音楽・オーディオ:
    - 特になし。このプロジェクトでは音楽やオーディオ関連の技術は使用していません。
- 開発ツール:
    - **GitHub API**: GitHubリポジトリの情報をプログラム的に取得するためのインターフェース。
    - **Python**: プロジェクトの主要なスクリプト言語で、APIアクセス、データ処理、Markdown生成に使用されます。
- テスト:
    - **pytest**: Pythonのテストフレームワーク。単体テストや統合テストの実行に用いられ、コードの品質を保証します。
- ビルドツール:
    - **Python**: リポジトリ一覧を生成するスクリプトの実行環境として機能します。
    - **Markdown**: JekyllがWebサイトとして処理するドキュメント形式を生成します。
- 言語機能:
    - **Python**: オブジェクト指向プログラミング、データ構造、ファイルI/O、HTTPリクエストなど、スクリプト開発に必要な豊富な機能を提供します。
- 自動化・CI/CD:
    - **Pythonスクリプト**: GitHub APIからの情報取得からMarkdown生成までの一連の処理を自動化し、手動での更新作業を不要にします。
- 開発標準:
    - **ruff**: PythonコードのLinterおよびフォーマッタ。コードの品質と一貫性を保ち、開発効率を向上させます。
    - **.editorconfig**: 異なる開発環境間でのコードスタイルの統一を支援し、一貫性のあるコーディングを促進します。

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
-   **.editorconfig**: コードエディタの基本的な書式設定を統一し、異なる開発環境間でのコードスタイルの一貫性を維持します。
-   **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関連するファイルを格納するディレクトリです。
    -   **check_large_files/**: 大容量ファイルのチェックに関連するツールやスクリプトを格納するディレクトリです。
        -   **README.md**: `check_large_files` ディレクトリの目的や使用方法を説明するドキュメントです。
        -   **check-large-files.toml**: 大容量ファイルチェックツールの設定ファイルです。
        -   **scripts/check_large_files.py**: 大容量ファイルをチェックするPythonスクリプトです。
-   **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するリストです。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）が記述されたファイルです。
-   **README.md**: プロジェクトの概要、目的、使用方法、設定、開発者向けヒントなどを記述したメインドキュメントです。
-   **_config.yml**: Jekyllサイト全体の基本的な設定を定義するファイルです。
-   **assets/**: Jekyllサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    -   **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイルです。
-   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
-   **generated-docs/**: GitHub APIから取得した情報に基づき自動生成されたドキュメントやデータが格納されるディレクトリです。
-   **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイルです。
-   **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。本スクリプトによってリポジトリ一覧が生成され、このファイルに出力されます。
-   **issue-notes/22.md**: 課題や検討事項に関するメモファイル（おそらくIssue #22に関連）です。
-   **manifest.json**: プログレッシブウェブアプリ (PWA) の設定やメタデータを含むWebアプリマニフェストファイルです。
-   **pytest.ini**: `pytest`テストフレームワークの設定ファイルです。
-   **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリのリストです。
-   **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonライブラリのリストです。
-   **robots.txt**: 検索エンジンクローラーに対するサイトのクロール指示を記述するファイルです。
-   **ruff.toml**: `ruff`Linterおよびフォーマッタの設定ファイルです。
-   **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示す空ファイルです。
-   **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す空ファイルです。
-   **src/generate_repo_list/badge_generator.py**: リポジトリのプロパティ（例：言語、ステータス）に基づいて視覚的なバッジを生成する機能を持つモジュールです。
-   **src/generate_repo_list/config.yml**: プロジェクト概要取得機能など、本スクリプトの技術的パラメータを設定するYAML形式のファイルです。
-   **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`や`secrets.toml`など）の読み込みと管理を行うモジュールです。
-   **src/generate_repo_list/date_formatter.py**: 日付オブジェクトを特定のフォーマットの文字列に変換する機能を提供するモジュールです。
-   **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
-   **src/generate_repo_list/json_ld_template.json**: JSON-LD形式の構造化データテンプレート。SEOのためにリポジトリ情報に付加される可能性があります。
-   **src/generate_repo_list/language_info.py**: リポジトリの言語情報を処理し、表示可能な形式に変換するモジュールです。
-   **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報とテンプレートを元に、最終的なMarkdownコンテンツを生成するモジュールです。
-   **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得するモジュールです。
-   **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を解析・抽出するモジュールです。
-   **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報を抽出する主要なロジックを担うモジュールです。
-   **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するファイルです。
-   **src/generate_repo_list/statistics_calculator.py**: スター数、フォーク数などのリポジトリ統計情報を計算または集計するモジュールです。
-   **src/generate_repo_list/strings.yml**: 表示メッセージや文言を管理するためのYAML形式の設定ファイルです。
-   **src/generate_repo_list/template_processor.py**: Markdown生成のためのテンプレート処理（例: Jinja2など）を行うモジュールです。
-   **src/generate_repo_list/url_utils.py**: URLの構築や解析など、URL関連のユーティリティ関数を提供するモジュールです。
-   **test_project_overview.py**: プロジェクト概要取得機能のテストスクリプトです。
-   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **conftest.py**: `pytest`のテスト設定やフィクスチャを定義するファイルです。
    -   **test_badge_generator_integration.py**: バッジ生成機能の統合テストコードです。
    -   **test_check_large_files.py**: 大容量ファイルチェック機能のテストコードです。
    -   **test_config.py**: 設定ファイル関連のテストコードです。
    -   **test_date_formatter.py**: 日付フォーマット機能のテストコードです。
    -   **test_environment.py**: 環境設定関連のテストコードです。
    -   **test_integration.py**: プロジェクト全体の統合テストコードです。
    -   **test_markdown_generator.py**: Markdown生成機能のテストコードです。
    -   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストコードです。
    -   **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストコードです。
    -   **test_repository_processor.py**: リポジトリ処理機能のテストコードです。

## 関数詳細説明
提供されたプロジェクト情報から具体的な関数のシグネチャ（引数、戻り値）は把握できませんが、各ファイルの役割から以下の主要な関数の機能を推測できます。

-   **src/generate_repo_list/generate_repo_list.py**
    -   **`main()`**: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得とMarkdown生成のメインプロセスを制御します。
        -   引数: 情報がありません。
        -   戻り値: 情報がありません。
    -   **`generate_repo_list(username, output_file, limit)`**: 指定されたユーザーのリポジトリ情報を取得し、整形して指定された出力ファイルにMarkdown形式で書き出す主要な処理を実行します。
        -   引数: `username` (GitHubユーザー名), `output_file` (出力ファイル名), `limit` (処理するリポジトリ数の上限、任意)。
        -   戻り値: 情報がありません (通常はNoneまたは成功ステータス)。
-   **src/generate_repo_list/repository_processor.py**
    -   **`process_repositories(repo_data)`**: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報を抽出・加工します。
        -   引数: `repo_data` (生のGitHubリポジトリデータ)。
        -   戻り値: 情報がありません (通常は整形されたリポジトリ情報のリスト)。
-   **src/generate_repo_list/markdown_generator.py**
    -   **`generate_markdown(repositories)`**: 処理されたリポジトリ情報と内部テンプレートを元に、最終的なMarkdownコンテンツを生成します。
        -   引数: `repositories` (整形されたリポジトリ情報のリスト)。
        -   戻り値: 情報がありません (通常は生成されたMarkdown文字列)。
-   **src/generate_repo_list/project_overview_fetcher.py**
    -   **`fetch_project_overview(repo_url, target_file, section_title)`**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要（3行の説明）を抽出し取得します。
        -   引数: `repo_url` (リポジトリのURL), `target_file` (概要ファイルへのパス), `section_title` (概要が含まれるセクションのタイトル)。
        -   戻り値: 情報がありません (通常は抽出された概要テキスト)。
-   **src/generate_repo_list/badge_generator.py**
    -   **`generate_badges(repo_info)`**: リポジトリのプロパティ（言語、ステータス、アーカイブなど）に基づいて視覚的なバッジ（Markdown形式の画像リンク）を生成します。
        -   引数: `repo_info` (個々のリポジトリ情報)。
        -   戻り値: 情報がありません (通常はバッジのMarkdown文字列)。
-   **src/generate_repo_list/config_manager.py**
    -   **`load_config(config_path)`**: YAML形式の設定ファイルやTOML形式のシークレットファイルを読み込み、設定情報を辞書として取得します。
        -   引数: `config_path` (設定ファイルへのパス)。
        -   戻り値: 情報がありません (通常は設定内容の辞書)。
-   **src/generate_repo_list/date_formatter.py**
    -   **`format_date(date_string)`**: ISO 8601形式などの日付文字列を、人間が読みやすい形式に変換します。
        -   引数: `date_string` (フォーマットする日付文字列)。
        -   戻り値: 情報がありません (通常はフォーマットされた日付文字列)。
-   **src/generate_repo_list/readme_badge_extractor.py**
    -   **`extract_badges_from_readme(readme_content)`**: リポジトリのREADMEファイルの内容から、既存のバッジ（例: Shields.io形式）の情報を解析・抽出します。
        -   引数: `readme_content` (READMEファイルのテキスト内容)。
        -   戻り値: 情報がありません (通常は抽出されたバッジ情報のリスト)。
-   **src/generate_repo_list/statistics_calculator.py**
    -   **`calculate_stats(repo_info)`**: スター数、フォーク数などのリポジトリ統計情報を計算または集計します。
        -   引数: `repo_info` (個々のリポジトリ情報)。
        -   戻り値: 情報がありません (通常は計算された統計情報の辞書)。
-   **src/generate_repo_list/template_processor.py**
    -   **`render_template(template_name, context)`**: 指定されたデータ (`context`) を使用してテンプレートファイル (`template_name`) をレンダリングし、最終的な出力（Markdownの一部）を生成します。
        -   引数: `template_name` (使用するテンプレートの名前), `context` (テンプレートに渡すデータ)。
        -   戻り値: 情報がありません (通常はレンダリングされた文字列)。
-   **src/generate_repo_list/url_utils.py**
    -   **`build_repo_url(owner, repo_name)`**: GitHubのユーザー名とリポジトリ名から完全なリポジトリURLを構築します。
        -   引数: `owner` (リポジトリの所有者名), `repo_name` (リポジトリ名)。
        -   戻り値: 情報がありません (通常は構築されたURL文字列)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-19 07:11:30 JST
