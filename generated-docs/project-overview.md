Last updated: 2026-03-10

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動取得・処理します。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧を自動生成するシステムです。
- 検索エンジンからの参照性向上とLLMの参照失敗緩和を目指し、詳細なリポジトリ概要を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイト構築), Markdown (コンテンツ生成), HTML/CSS (生成コンテンツの表示)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), pytest (テストフレームワーク), ruff (コードリンター/フォーマッター), pip (Pythonパッケージ管理)
- テスト: pytest (ユニットテスト、結合テスト)
- ビルドツール: Pythonスクリプト (Markdownコンテンツ生成), Jekyll (GitHub Pagesサイトの最終的なビルドとデプロイ)
- 言語機能: Python (スクリプト開発), YAML (設定ファイル定義), TOML (秘密情報の管理)
- 自動化・CI/CD: GitHub Pages (自動デプロイ機能), GitHub API (リポジトリ情報の自動取得), Pythonスクリプトによる自動生成
- 開発標準: ruff (コードスタイルチェックと自動修正), .editorconfig (エディタ間のコーディングスタイル統一)

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトを格納するディレクトリです。
    -   **`check_large_files/README.md`**: `check_large_files`スクリプトの目的と使用方法を説明するドキュメントです。
    -   **`check-large_files.toml`**: `check_large_files.py`スクリプトの動作を設定するためのTOML形式の設定ファイルです。
    -   **`scripts/check_large_files.py`**: リポジトリ内の特定の基準を超える大きなファイルを検出し、通知するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方、開発ヒントなどを説明する主要なドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定ファイルです。テーマ、プラグイン、カスタム変数などが定義されます。
-   **`assets/`**: Jekyllサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
-   **`debug_project_overview.py`**: `project_overview_fetcher`モジュールによるプロジェクト概要の取得機能を個別にテスト・デバッグするためのスクリプトです。
-   **`generated-docs/`**: `generate_repo_list.py`スクリプトによって生成されるMarkdownファイルやその他のドキュメントが出力されるディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
-   **`index.md`**: 生成されたリポジトリ一覧が書き込まれる、GitHub PagesサイトのメインとなるMarkdownファイルです。JekyllによってHTMLに変換され、サイトのトップページとして表示されます。
-   **`issue-notes/`**: 開発中に発生した課題や検討事項をメモとして残すためのディレクトリです。
    -   `22.md`: 特定の課題番号に関する詳細なメモや議論が記述されています。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルです。ウェブアプリの表示名、アイコン、表示モードなどを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークである`pytest`のグローバル設定ファイルです。テストの発見ルール、プラグイン、コマンドラインオプションなどが設定されます。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`requirements.txt`**: 本番環境または実行環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいは避けるべきかを指示するファイルです。
-   **`ruff.toml`**: Pythonのコードリンター兼フォーマッターである`ruff`の設定ファイルです。コードスタイル、エラーチェックルール、自動修正オプションなどが定義されます。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するシステムのコアロジックを構成するPythonパッケージです。
        -   **`badge_generator.py`**: リポジトリのプログラミング言語、スター数、ステータス（アーカイブなど）を示すバッジをMarkdown形式で生成する機能を提供します。
        -   **`config.yml`**: `generate_repo_list`システム自体の動作を制御するためのYAML形式の設定ファイルです（例：プロジェクト概要取得機能の有効/無効、ターゲットファイル名など）。
        -   **`config_manager.py`**: YAML形式の設定ファイルやTOML形式の秘密情報ファイル（例：GitHubトークン）を読み込み、管理するためのユーティリティモジュールです。
        -   **`date_formatter.py`**: ISO 8601形式などの日付文字列を、人間が読みやすい形式に変換するための関数を提供します。
        -   **`generate_repo_list.py`**: このプロジェクトのメインとなる実行スクリプトです。コマンドライン引数を解析し、GitHub APIからのデータ取得、リポジトリ情報の処理、最終的なMarkdownファイルの生成を行います。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データを生成する際のJSON-LDテンプレートが格納されています。
        -   **`language_info.py`**: プログラミング言語に関する追加情報（表示名、色コードなど）を提供し、バッジ生成や言語統計表示に利用されます。
        -   **`markdown_generator.py`**: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツ（リポジトリ一覧、個別のリポジトリカードなど）を生成する機能を提供します。
        -   **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得・抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジ（ shields.io など）の情報を抽出し、重複を避けるなどの処理に利用します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（スター数、最終更新日、説明など）を抽出し、整形するための主要なロジックを扱います。
        -   **`seo_template.yml`**: 生成されるMarkdownファイルのSEO関連メタデータや、ページタイトル、ディスクリプションなどのテンプレート設定を定義します。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算・集計するための機能を提供します。
        -   **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言、ラベルなどを一元的に管理するためのYAMLファイルです。国際化や文言変更を容易にします。
        -   **`template_processor.py`**: Markdownテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成する機能を提供します。
        -   **`url_utils.py`**: GitHubリポジトリのURL、GitHub PagesのURL、APIエンドポイントなど、URL関連の操作や構築を行うためのユーティリティ関数を集めたモジュールです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が期待通りに動作するかを検証するためのユニットテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の結合テストを行い、複数のコンポーネントが連携して正しくバッジを生成するかを検証します。
    -   **`test_check_large_files.py`**: `check_large_files.py`スクリプトが正しく大きなファイルを検出・報告するかをテストします。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理が正しく行われるかをテストします。
    -   **`test_date_formatter.py`**: 日付フォーマット関数が様々な入力に対して正しく動作するかをテストします。
    -   **`test_environment.py`**: 実行環境のセットアップや依存関係が正しく解決されているかを検証します。
    -   **`test_integration.py`**: 主要なモジュールが連携して、エンドツーエンドのシナリオで機能するかをテストする結合テストです。
    -   **`test_markdown_generator.py`**: Markdown生成機能が期待される出力を生成するかをテストします。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`の単体テストです。
    -   **`test_readme_badge_extractor.py`**: `README.md`からバッジが正しく抽出されるかをテストします。
    -   **`test_repository_processor.py`**: リポジトリデータ処理ロジックの単体テストです。

## 関数詳細説明
このプロジェクトはPythonスクリプト群で構成されており、メインの実行スクリプト`generate_repo_list.py`が他のモジュール内の関数を呼び出して処理を進めます。

-   **`generate_repo_list.py`**
    -   **`main()`**:
        -   役割: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdownファイルの生成をオーケストレートします。
        -   引数: なし (コマンドライン引数は`argparse`で内部的に処理)。
        -   戻り値: なし。
    -   **`get_github_repos(username, limit, github_token, config)`**:
        -   役割: GitHub APIを利用して、指定されたユーザーのリポジトリ一覧を取得します。取得数制限や認証トークンを考慮します。
        -   引数:
            -   `username` (str): リポジトリを取得するGitHubユーザー名。
            -   `limit` (int, optional): 取得するリポジトリ数の上限。開発用。
            -   `github_token` (str): GitHub APIへの認証トークン。
            -   `config` (dict): プロジェクト設定。
        -   戻り値: `list` of `dict` (取得したリポジトリデータのリスト)。
    -   **`generate_markdown_output(username, output_file, repos, config, github_token)`**:
        -   役割: 処理済みのリポジトリ情報とユーザー名を受け取り、Markdown形式のコンテンツを生成して指定されたファイルに出力します。
        -   引数:
            -   `username` (str): GitHubユーザー名。
            -   `output_file` (str): 出力するMarkdownファイル名。
            -   `repos` (list): 処理済みのリポジトリデータリスト。
            -   `config` (dict): プロジェクト設定。
            -   `github_token` (str): GitHub APIへの認証トークン。
        -   戻り値: なし。

-   **`repository_processor.py`**
    -   **`process_repository(repo_data, config, github_token)`**:
        -   役割: GitHub APIから取得した生のリポジトリデータを受け取り、表示用に必要な情報（概要、バッジ、整形された日付など）を抽出し、加工して返します。
        -   引数:
            -   `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
            -   `config` (dict): プロジェクト設定。
            -   `github_token` (str): GitHub APIへの認証トークン。
        -   戻り値: `dict` (整形されたリポジトリデータ)。

-   **`project_overview_fetcher.py`**
    -   **`fetch_project_overview(repo_url, target_file, section_title, config, github_token)`**:
        -   役割: 指定されたリポジトリの特定のファイルから「プロジェクト概要」セクションを読み込み、3行の概要を抽出します。
        -   引数:
            -   `repo_url` (str): 対象リポジトリのGitHub URL。
            -   `target_file` (str): 概要が記述されているファイルパス（例: `generated-docs/project-overview.md`）。
            -   `section_title` (str): 概要を抽出するセクションのタイトル。
            -   `config` (dict): プロジェクト設定。
            -   `github_token` (str): GitHub APIへの認証トークン。
        -   戻り値: `str` (抽出された3行の概要、またはデフォルトの概要)。

-   **`markdown_generator.py`**
    -   **`generate_repository_list_markdown(processed_repos, config, strings)`**:
        -   役割: 処理済みリポジトリデータのリストを受け取り、リポジトリ一覧全体のMarkdownテキストを生成します。
        -   引数:
            -   `processed_repos` (list): 処理済みのリポジトリデータリスト。
            -   `config` (dict): プロジェクト設定。
            -   `strings` (dict): 表示文言設定。
        -   戻り値: `str` (生成されたMarkdownテキスト)。
    -   **`generate_repo_card_markdown(repo, strings)`**:
        -   役割: 単一の処理済みリポジトリデータを受け取り、そのリポジトリのカード形式のMarkdownスニペットを生成します。
        -   引数:
            -   `repo` (dict): 処理済みの単一リポジトリデータ。
            -   `strings` (dict): 表示文言設定。
        -   戻り値: `str` (生成されたMarkdownスニペット)。

-   **`badge_generator.py`**
    -   **`generate_language_badge(language, language_color)`**:
        -   役割: 指定されたプログラミング言語と色を使って、shields.io形式の言語バッジMarkdownを生成します。
        -   引数:
            -   `language` (str): プログラミング言語名。
            -   `language_color` (str): 言語バッジの色コード。
        -   戻り値: `str` (言語バッジのMarkdown)。
    -   **`generate_star_badge(stars)`**:
        -   役割: 指定されたスター数を使って、shields.io形式のスター数バッジMarkdownを生成します。
        -   引数:
            -   `stars` (int): リポジトリのスター数。
        -   戻り値: `str` (スター数バッジのMarkdown)。

-   **`config_manager.py`**
    -   **`load_config(config_path)`**:
        -   役割: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書として返します。
        -   引数: `config_path` (str): 設定ファイルのパス。
        -   戻り値: `dict` (設定データ)。
    -   **`load_secrets(secrets_path)`**:
        -   役割: 指定されたパスからTOML形式の秘密情報ファイル（例：GitHubトークン）を読み込み、辞書として返します。
        -   引数: `secrets_path` (str): 秘密情報ファイルのパス。
        -   戻り値: `dict` (秘密情報データ)。

-   **`date_formatter.py`**
    -   **`format_date(iso_date_string)`**:
        -   役割: ISO 8601形式の日付文字列を、例えば「YYYY年MM月DD日」のような、より人間が読みやすい形式に整形します。
        -   引数: `iso_date_string` (str): ISO 8601形式の日付文字列。
        -   戻り値: `str` (整形された日付文字列)。

-   **`language_info.py`**
    -   **`get_language_details(language_name)`**:
        -   役割: プログラミング言語名に基づいて、その言語の関連情報（色コード、アイコンなど）を取得します。
        -   引数: `language_name` (str): プログラミング言語名。
        -   戻り値: `dict` (言語の詳細情報)。

-   **`readme_badge_extractor.py`**
    -   **`extract_badges_from_readme(readme_content)`**:
        -   役割: リポジトリの`README.md`コンテンツから、既存のバッジ（shields.ioなど）のMarkdownスニペットを抽出します。
        -   引数: `readme_content` (str): `README.md`ファイルのテキストコンテンツ。
        -   戻り値: `list` of `str` (抽出されたバッジのMarkdownリスト)。

-   **`statistics_calculator.py`**
    -   **`calculate_repository_stats(repo_data)`**:
        -   役割: リポジトリの生データから、スター数、フォーク数、ウォッチ数などの統計情報を計算または抽出します。
        -   引数: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
        -   戻り値: `dict` (計算された統計情報)。

-   **`template_processor.py`**
    -   **`load_template(template_path)`**:
        -   役割: 指定されたパスからテンプレートファイルを読み込み、その内容を文字列として返します。
        -   引数: `template_path` (str): テンプレートファイルのパス。
        -   戻り値: `str` (テンプレートの内容)。
    -   **`render_template(template_content, data)`**:
        -   役割: テンプレート文字列とデータ（辞書）を受け取り、テンプレート内のプレースホルダーをデータで置換して最終的な文字列を生成します。
        -   引数:
            -   `template_content` (str): テンプレート文字列。
            -   `data` (dict): テンプレートに埋め込むデータ。
        -   戻り値: `str` (レンダリングされた文字列)。

-   **`url_utils.py`**
    -   **`build_repo_url(username, repo_name)`**:
        -   役割: GitHubユーザー名とリポジトリ名から、GitHub上のリポジトリURLを構築します。
        -   引数:
            -   `username` (str): GitHubユーザー名。
            -   `repo_name` (str): リポジトリ名。
        -   戻り値: `str` (リポジトリのURL)。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── config_manager.load_config()
├── config_manager.load_secrets()
├── get_github_repos() (generate_repo_list.py)
│   └── (GitHub API呼び出し)
└── generate_markdown_output() (generate_repo_list.py)
    ├── (各リポジトリに対してループ)
    │   └── repository_processor.process_repository()
    │       ├── project_overview_fetcher.fetch_project_overview()
    │       │   └── (GitHub API呼び出し: リポジトリファイル取得)
    │       ├── badge_generator.generate_language_badge()
    │       ├── badge_generator.generate_star_badge()
    │       ├── date_formatter.format_date()
    │       ├── language_info.get_language_details()
    │       ├── readme_badge_extractor.extract_badges_from_readme()
    │       ├── statistics_calculator.calculate_repository_stats()
    │       └── url_utils.build_repo_url()
    └── markdown_generator.generate_repository_list_markdown()
        ├── template_processor.load_template()
        ├── template_processor.render_template()
        └── (各処理済みリポジトリに対してループ)
            └── markdown_generator.generate_repo_card_markdown()
                └── template_processor.render_template()

---
Generated at: 2026-03-10 07:09:39 JST
