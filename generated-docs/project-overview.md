Last updated: 2026-01-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得します。
- 取得した情報からGitHub Pages向けにSEO最適化されたリポジトリ一覧を自動生成します。
- これにより、GitHub Pagesの検索エンジンクロールとLLM参照性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (静的サイトジェネレータ) と **GitHub Pages** (ホスティングサービス)。本プロジェクトで生成されたMarkdownファイルがこれらの環境で公開され、ウェブサイトとして閲覧されます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **pytest**: Pythonコードのテストを効率的に実行するためのフレームワークです。
    - **ruff**: Pythonコードの高速なリンター兼フォーマッターで、コード品質の維持と統一に貢献します。
    - **PyYAML**: YAML形式の設定ファイル (`config.yml`, `strings.yml` など) をPythonで読み書きするためのライブラリです。
    - **toml**: TOML形式の設定ファイル (`secrets.toml` など) をPythonで読み書きするためのライブラリです。
    - **EditorConfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義・適用するためのファイル形式です。
- テスト: **pytest** を使用し、プロジェクトの機能が正しく動作することを検証します。
- ビルドツール: 特定のビルドツールは使用せず、Pythonスクリプトが直接Markdownファイルを生成します。
- 言語機能:
    - **Python**: プロジェクトの主要な開発言語です。GitHub APIとの連携、データ処理、Markdown生成など、全てのロジックをPythonで実装しています。
    - **requests**: GitHub APIと通信するために広く利用されるHTTPライブラリです。
    - **python-dateutil**: Pythonの標準datetimeモジュールを拡張し、より高度な日付・時刻解析や操作を可能にするライブラリです。
- 自動化・CI/CD: **GitHub Actions** (本システムがGitHub Pagesサイトのデプロイや更新プロセスで活用されることを想定しており、自動化された実行環境として機能します)。
- 開発標準: **ruff** (コードリンティングとフォーマットによる品質維持) および **EditorConfig** (プロジェクト全体でのコーディングスタイル統一)。

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  18.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_badge_generator_integration.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、改行コードなどの基本的なコードスタイルを統一するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリ（例: ビルド生成物、環境固有の設定ファイルなど）を指定するファイルです。
-   **`LICENSE`**: 本プロジェクトがMITライセンスの下で公開されていることを示すファイルです。利用条件や免責事項が記載されています。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、使い方、設定方法などを説明するドキュメントです。
-   **`_config.yml`**: Jekyllによって構築されるGitHub Pagesサイト全体の設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
-   **`assets/`**: ウェブサイトで使用される静的なリソース（画像、ファビコンなど）を格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザタブやブックマークに表示されるアイコン）の各サイズバージョンです。
-   **`debug_project_overview.py`**: `project_overview` 機能（各リポジトリの概要抽出）のデバッグや単体テストを行うための補助スクリプトです。
-   **`generated-docs/`**: 他のリポジトリから自動的に取得・生成されたドキュメント（例: 各リポジトリの `project-overview.md` など）を一時的、あるいは永続的に格納する目的のディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認のために配置されるHTMLファイルです。特定のコードが含まれています。
-   **`index.md`**: メインの出力ファイルであり、生成されたGitHubリポジトリ一覧がMarkdown形式で記述されるファイルです。これがGitHub Pagesでウェブページとして表示されます。
-   **`issue-notes/`**: 開発中の課題、アイデア、特定のIssueに関連するメモなどをMarkdown形式で保存しているディレクトリです。
-   **`manifest.json`**: ウェブサイトをProgressive Web App (PWA) として機能させるためのマニフェストファイルです。アプリ名、アイコン、表示モードなどのメタデータを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。テスト対象のパスや追加オプションなどが指定されます。
-   **`requirements-dev.txt`**: 本番環境では不要な、開発時やテスト時にのみ必要なPythonライブラリの依存関係をリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトが実行される本番環境で必須となるPythonライブラリの依存関係をリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいは除外すべきかを指示するファイルです。
-   **`ruff.toml`**: Pythonのリンターおよびフォーマッターであるruffの設定ファイルです。コードスタイルルール、無視するファイルなどが定義されます。
-   **`src/__init__.py`**: Pythonにおいて、ディレクトリがパッケージであることを示すための空のファイルです。
-   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すための空のファイルです。
-   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語、スター数、最終更新日などの情報に基づいて、Markdown形式のバッジを生成するロジックを担うモジュールです。
-   **`src/generate_repo_list/config.yml`**: `generate_repo_list` スクリプト自体の動作に関する技術的な設定パラメータ（例: プロジェクト概要の取得設定、タイムアウト時間など）を定義するファイルです。
-   **`src/generate_repo_list/config_manager.py`**: プロジェクト内で使用される各種設定ファイル（`config.yml`など）の読み込み、解析、および管理を行うモジュールです。
-   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、特定の書式（例: `YYYY-MM-DD`）に整形するための機能を提供するモジュールです。
-   **`src/generate_repo_list/generate_repo_list.py`**: 本プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成する全体のフローを制御します。
-   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジンの最適化（SEO）を強化するために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
-   **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語の種類や、その使用割合などの統計情報を処理するモジュールです。
-   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報や統計データに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを実装したモジュールです。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内に存在する特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの簡潔な概要説明を抽出し、取得する機能を提供するモジュールです。
-   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリの `README.md` ファイルの内容から、既存のバッジ情報（例: ビルドステータス、カバレッジなど）を解析・抽出するモジュールです。
-   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、それを整形、フィルタリング、必要な情報の追加などの処理を行うモジュールです。
-   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関連する各種テンプレート（例: メタディスクリプション、キーワードなど）や設定を定義するファイルです。
-   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終コミット日などの様々な統計データを計算・集計する機能を提供するモジュールです。
-   **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのファイルです。多言語対応や文言の統一に利用されます。
-   **`src/generate_repo_list/template_processor.py`**: マークダウンコンテンツ生成において、特定のテンプレートとデータを用いて最終的な文字列を組み立てる処理を担うモジュールです。
-   **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を集めたモジュールです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールで実装されているプロジェクト概要取得機能のテストケースを記述したスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの統合テストを担当します。
    -   `test_config.py`: 設定ファイル (`config.yml` など) の読み込みや設定値の取得に関するテストを行います。
    -   `test_date_formatter.py`: `date_formatter`モジュールの日付整形機能のテストを行います。
    -   `test_environment.py`: プロジェクトの実行環境に関する設定や依存関係の確認テストを行います。
    -   `test_integration.py`: 主要なモジュールが連携して正しく機能するかを確認する全体的な統合テストです。
    -   `test_markdown_generator.py`: `markdown_generator`モジュールが正しいMarkdownを生成するかテストします。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールがプロジェクト概要を正しく抽出できるかテストします。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールがREADMEからバッジを正しく抽出できるかテストします。
    -   `test_repository_processor.py`: `repository_processor`モジュールがリポジトリデータを適切に処理するかテストします。

## 関数詳細説明
-   **`generate_repo_list.py`内の主要関数 (`main`関数など)**
    -   役割: GitHub APIからユーザーのリポジトリ情報を取得し、取得したデータを各処理モジュール（データ整形、Markdown生成など）に渡し、最終的に指定されたファイルにリポジトリ一覧のMarkdownコンテンツを書き出します。プログラムのエントリポイントとなります。
    -   引数: GitHubユーザー名、出力ファイルパス、処理リポジトリ数制限などのコマンドライン引数。
    -   戻り値: なし（ファイル出力が主目的）。
-   **`badge_generator.py`内の主要関数 (`generate_badge`など)**
    -   役割: リポジトリのプログラミング言語、スター数、最終更新日などの情報を受け取り、それらを示すためのSVGまたはMarkdown形式のバッジ文字列を生成します。
    -   引数: リポジトリデータオブジェクトや特定の属性（例: 言語名、スター数）。
    -   戻り値: バッジを表すMarkdownまたはSVG文字列。
-   **`config_manager.py`内の主要関数 (`load_config`, `get_config_value`など)**
    -   役割: YAML形式の設定ファイルを読み込み、その内容をPythonオブジェクトとして扱えるように管理します。特定の設定値へのアクセス機能を提供します。
    -   引数: 設定ファイルのパス、設定キー。
    -   戻り値: 読み込まれた設定データ、または指定された設定キーの値。
-   **`date_formatter.py`内の主要関数 (`format_date`など)**
    -   役割: 日付オブジェクト（`datetime`型など）を受け取り、指定された書式（例: `YYYY-MM-DD`、`MMM DD, YYYY`）で文字列に変換します。
    -   引数: 日付オブジェクト、フォーマット文字列。
    -   戻り値: フォーマットされた日付文字列。
-   **`language_info.py`内の主要関数 (`get_language_stats`など)**
    -   役割: 特定のリポジトリで使用されているプログラミング言語とその使用バイト数（または割合）を取得し、統計情報として提供します。
    -   引数: リポジトリ情報。
    -   戻り値: 言語ごとの統計情報（辞書など）。
-   **`markdown_generator.py`内の主要関数 (`generate_markdown`など)**
    -   役割: 処理されたリポジトリデータとテンプレート情報を基に、最終的なリポジトリ一覧のMarkdownコンテンツ全体を構築します。
    -   引数: 処理済みリポジトリデータのリスト、設定情報。
    -   戻り値: 生成されたMarkdownコンテンツ文字列。
-   **`project_overview_fetcher.py`内の主要関数 (`fetch_project_overview`など)**
    -   役割: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）にあるファイルから、「プロジェクト概要」セクションの3行説明を抽出し、取得します。GitHub APIを介してファイル内容を読み込む場合があります。
    -   引数: GitHubリポジトリのURLまたは情報、対象ファイルパス、セクションタイトル。
    -   戻り値: 抽出されたプロジェクト概要の文字列リスト。
-   **`readme_badge_extractor.py`内の主要関数 (`extract_badges_from_readme`など)**
    -   役割: リポジトリの `README.md` ファイルの内容を解析し、そこに埋め込まれているバッジ（ビルドステータス、カバレッジなど）の情報を抽出します。
    -   引数: READMEのテキストコンテンツ。
    -   戻り値: 抽出されたバッジ情報のリスト。
-   **`repository_processor.py`内の主要関数 (`process_repository_data`など)**
    -   役割: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を受け取り、表示に必要な情報に整形・加工します。不要なリポジトリのフィルタリングや追加情報の付与も行います。
    -   引数: GitHub APIからのリポジトリデータのリスト。
    -   戻り値: 処理され、整形されたリポジトリデータのリスト。
-   **`statistics_calculator.py`内の主要関数 (`calculate_statistics`など)**
    -   役割: リポジトリのスター数、フォーク数、最終更新からの期間などの様々な統計データを計算し、リポジトリ情報に付加します。
    -   引数: リポジトリ情報。
    -   戻り値: 計算された統計情報を含むリポジトリデータ。
-   **`template_processor.py`内の主要関数 (`render_template`など)**
    -   役割: MarkdownやHTMLなどのテンプレートファイルと、そこに埋め込むためのデータを受け取り、データをテンプレートに適用して最終的な文字列コンテンツを生成します。
    -   引数: テンプレート文字列またはファイルパス、埋め込むデータ（辞書）。
    -   戻り値: レンダリングされた文字列。
-   **`url_utils.py`内の主要関数 (`build_github_api_url`, `is_valid_url`など)**
    -   役割: GitHub APIのエンドポイントURLを構築したり、与えられた文字列が有効なURLであるかを検証したりするなど、URLに関する汎用的なユーティリティ機能を提供します。
    -   引数: URLの構成要素、検証対象の文字列。
    -   戻り値: 構築されたURL文字列、またはURLの有効性を示すブール値。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-01-22 07:08:08 JST
