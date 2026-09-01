Last updated: 2026-09-02

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、個人プロジェクトのリポジトリ情報を自動で集約します。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンやLLMからの参照性を高め、プロジェクトの可視性とアクセス性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして利用), **Markdown** (生成されるコンテンツの形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (主要な開発言語およびスクリプト実行環境), **GitHub API** (リポジトリ情報の取得), **Git** (バージョン管理システム)
- テスト: **pytest** (Python向けのテストフレームワーク)
- ビルドツール: 該当する専用のビルドツールはありません。Pythonスクリプト自体がMarkdownファイルを生成する役割を担います。
- 言語機能: **Python 3.x** (最新の言語機能とライブラリを活用)
- 自動化・CI/CD: GitHub Actions (特定の自動化スクリプト`check_large_files`を格納する`.github_automation`ディレクトリが存在しますが、CI/CDの具体的な利用は明記されていません。プロジェクトのreadmeではローカル開発重視とされています。)
- 開発標準: **ruff** (Pythonコードのリンターおよびフォーマッター), **.editorconfig** (エディタの統一的なコードスタイル設定)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルがないかチェックするための機能に関するファイル群です。
        - **README.md**: `check_large_files`機能の概要や使い方を説明するファイルです。
        - **check-large-files.toml**: `check_large_files`機能の設定を定義するファイルです。
        - **scripts/check_large_files.py**: 指定された条件で大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: 本プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **README.md**: プロジェクトの目的、機能、使い方、開発者向けヒントなどをまとめたプロジェクトの顔となるドキュメントです。
- **_config.yml**: Jekyllサイト全体のグローバルな設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどを指定します。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: 異なるサイズで提供されるサイトのファビコン画像ファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher`）のデバッグやテストに使用されるスクリプトです。
- **generated-docs/**: 自動生成されたドキュメントや、特定のプロジェクト概要ファイルなどを格納する（またはそのための参照元となる）ディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される主要なマークダウンファイルです。GitHub Pagesでリポジトリ一覧ページとして表示されます。
- **issue-notes/**: 開発中の課題やメモを記録するためのディレクトリです。
    - **22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記述したマークダウンファイルです。
- **manifest.json**: Webアプリマニフェストファイルで、PWA（Progressive Web App）としてサイトをインストールする際のメタデータを定義します。
- **pytest.ini**: Pythonテストフレームワーク`pytest`の設定を記述するファイルです。テストの発見方法や実行オプションなどを指定します。
- **requirements-dev.txt**: 開発環境やテスト環境で必要となるPythonライブラリとそのバージョンをリストアップしたファイルです（例: `pytest`, `ruff`）。
- **requirements.txt**: 本番環境でこのプロジェクトを実行するために必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンターおよびフォーマッターである`ruff`の設定を記述するファイルです。コードスタイルのルールなどを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成するための主要なPythonモジュール群を格納するディレクトリです。
        - **__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのプログラミング言語やステータスなどを示すバッジ画像を生成または準備するロジックを扱います。
        - **config.yml**: リポジトリ一覧生成システムの動作に関する設定（例: `project_overview`機能の有効/無効、対象ファイルなど）を定義するYAMLファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、プログラム内で利用しやすい形で管理する機能を提供します。
        - **date_formatter.py**: リポジトリの更新日時などの日付情報を、人間が読みやすい形式に整形するための機能を提供します。
        - **generate_repo_list.py**: 本プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、最終的なマークダウンファイルを生成する全体の流れを制御します。
        - **json_ld_template.json**: SEOを強化するために、リポジトリ情報から構造化データ（JSON-LD）を生成するためのテンプレートです。
        - **language_info.py**: GitHub APIから取得したリポジトリの言語情報を処理し、表示に利用しやすい形式に変換する機能を提供します。
        - **markdown_generator.py**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なマークダウンコンテンツを生成するコアな機能を提供します。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出し、取得する機能です。
        - **readme_badge_extractor.py**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形、フィルタリングし、後続の処理で利用しやすいデータ構造に変換する機能です。
        - **seo_template.yml**: 生成されるマークダウンファイルのSEOメタデータ（タイトル、説明など）を設定するためのテンプレートファイルです。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算、集計する機能を提供します。
        - **strings.yml**: UIに表示されるメッセージ、ラベル、その他の静的テキストを一元的に管理するためのYAMLファイルです。多言語対応の基盤にもなり得ます。
        - **template_processor.py**: マークダウン生成時に使用するテンプレートファイル（例: Jinja2テンプレートなど）の読み込み、変数置換などの処理を担います。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`で提供されるプロジェクト概要取得機能の単体テストを記述したファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **conftest.py**: `pytest`のテスト実行時に使用される共通のフィクスチャやヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator.py`の統合テストを行い、バッジが正しく生成されるかを確認します。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`の機能をテストします。
    - **test_config.py**: `config_manager.py`による設定ファイルの読み込みと管理が正しく行われるかをテストします。
    - **test_date_formatter.py**: `date_formatter.py`の日付整形機能が意図通りに動作するかをテストします。
    - **test_environment.py**: テスト実行環境や依存関係が正しく設定されているかを確認するテストです。
    - **test_integration.py**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを検証する統合テストです。
    - **test_markdown_generator.py**: `markdown_generator.py`が正しいマークダウンコンテンツを生成するかをテストします。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`がリポジトリ概要を正しく取得できるかをテストします。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor.py`がREADMEからバッジ情報を正しく抽出できるかをテストします。
    - **test_repository_processor.py**: `repository_processor.py`がGitHub APIからのリポジトリデータを正しく処理・整形できるかをテストします。

## 関数詳細説明
本プロジェクトは多くのPythonファイルで構成されており、それぞれのファイルが特定の機能を受け持つ関数群を内包しています。以下に、主要なファイルに存在するであろう関数とその役割について説明します。

-   **generate_repo_list.py**:
    -   `main()`: プロジェクト全体の実行エントリポイント。GitHub APIからの情報取得、データの処理、Markdown生成、ファイル出力までの一連の流れを制御します。
        -   **引数**: `username` (GitHubユーザー名), `output` (出力ファイルパス), `limit` (処理するリポジトリ数の上限、任意)。
        -   **戻り値**: なし。サイドエフェクトとして指定されたファイルにMarkdownを書き込みます。

-   **repository_processor.py**:
    -   `fetch_repositories(username, token, limit=None)`: 指定されたユーザー名とGitHubトークンを使用して、GitHub APIからリポジトリ情報を取得します。
        -   **引数**: `username` (対象のGitHubユーザー名), `token` (GitHub API認証トークン), `limit` (取得するリポジトリ数の上限、デフォルトなし)。
        -   **戻り値**: 取得したリポジトリ情報のリスト（辞書形式）。
    -   `process_repository_data(repo_data)`: 生のリポジトリデータを受け取り、表示に必要な情報（名前、説明、URL、言語、スター数など）に整形します。
        -   **引数**: `repo_data` (GitHub APIから取得した個々のリポジトリデータ)。
        -   **戻り値**: 整形されたリポジトリ情報の辞書。

-   **project_overview_fetcher.py**:
    -   `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリから`project-overview.md`ファイルの内容を取得し、その中からプロジェクト概要の3行説明を抽出します。
        -   **引数**: `repo_name` (リポジトリ名), `owner` (リポジトリの所有者), `config` (プロジェクト概要機能の設定)。
        -   **戻り値**: 抽出された3行のプロジェクト概要（リスト形式）または空のリスト。

-   **markdown_generator.py**:
    -   `generate_markdown(repositories_data, seo_config, strings_data)`: 処理済みのリポジトリデータ、SEO設定、表示用文字列データを使用して、最終的なMarkdownコンテンツを生成します。
        -   **引数**: `repositories_data` (処理済みリポジトリ情報のリスト), `seo_config` (SEO関連の設定), `strings_data` (表示文字列データ)。
        -   **戻り値**: 生成されたMarkdown形式の文字列。

-   **config_manager.py**:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込みます。
        -   **引数**: `config_path` (設定ファイルのパス)。
        -   **戻り値**: 読み込まれた設定内容の辞書。

-   **date_formatter.py**:
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式（例: "YYYY年MM月DD日"）に変換します。
        -   **引数**: `iso_date_string` (ISO 8601形式の日付文字列)。
        -   **戻り値**: フォーマットされた日付文字列。

-   **badge_generator.py**:
    -   `create_language_badge(language)`: 指定されたプログラミング言語に対応するバッジのMarkdownまたはURLを生成します。
        -   **引数**: `language` (プログラミング言語名)。
        -   **戻り値**: バッジのMarkdown文字列またはURL。

-   **check_large_files.py** (`.github_automation/check_large_files/scripts`内):
    -   `check_files_for_size(repo_path, config)`: 指定されたリポジトリパス内のファイルを、設定されたサイズ制限と比較してチェックします。
        -   **引数**: `repo_path` (チェック対象のリポジトリのパス), `config` (サイズ制限などの設定)。
        -   **戻り値**: 制限を超過したファイルのリスト。

上記は主要な機能を提供するであろう関数の例であり、実際には各ファイルに詳細な処理を行う補助関数が多数存在します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-02 07:11:42 JST
