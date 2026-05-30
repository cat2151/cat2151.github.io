Last updated: 2026-05-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を自動的に取得します。
- GitHub Pages用のMarkdown形式のリポジトリ一覧と詳細ページを生成します。
- 検索エンジン最適化とLLMからの参照性向上を目指します。

## 技術スタック
- フロントエンド: **GitHub Pages**, **Jekyll** (テーマ利用を想定), **Markdown** (出力形式), **HTML/CSS** (Jekyll経由の最終レンダリング)
- 音楽・オーディオ: なし
- 開発ツール: **GitHub API** (リポジトリ情報取得), **Git** (バージョン管理), **pip** (Pythonパッケージ管理)
- テスト: **Pytest** (Pythonのテストフレームワーク)
- ビルドツール: **Python** (スクリプト実行によるファイル生成)
- 言語機能: **Python** (メインの開発言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリにより、自動化の余地があることを示唆するが、現状はローカル開発重視)
- 開発標準: **Ruff** (Pythonコードのリンター・フォーマッター), **EditorConfig** (エディタ設定の統一)

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
- **`.editorconfig`**: 複数の開発者間でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローやスクリプトを格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明文書です。
    - **`check_large_files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などをまとめた主要な説明文書です。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。
- **`assets/`**: GitHub Pagesサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザタブに表示されるアイコン）の各種サイズです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得された `project-overview.md` など、生成されたドキュメントが一時的に配置されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページとして生成されるMarkdownファイルで、リポジトリ一覧がここに記述されます。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（Issue #22など）に関する詳細なメモです。
- **`manifest.json`**: Webアプリケーションマニフェストファイルで、PWA（Progressive Web App）機能やホーム画面アイコンの設定に利用されます。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を定義する設定ファイルです。
- **`requirements-dev.txt`**: 開発・テスト時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの実行時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびFormatterであるRuffの設定ファイルです。コード品質とスタイルを維持するために使用されます。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: `src`ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能のコアロジックを格納するサブパッケージです。
        - **`__init__.py`**: `generate_repo_list`ディレクトリをPythonサブパッケージとして識別するためのファイルです。
        - **`badge_generator.py`**: リポジトリの状態（アーカイブ、フォークなど）や言語に応じたバッジのHTML/Markdownを生成するロジックを定義します。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの動作に関する設定（例: プロジェクト概要取得の有効/無効、対象ファイルパス、タイムアウトなど）を定義します。
        - **`config_manager.py`**: `config.yml`やシークレットファイル（例: `secrets.toml`）などの設定ファイルを読み込み、管理するユーティリティモジュールです。
        - **`date_formatter.py`**: ISO形式の日付文字列を人間が読みやすい形式に整形する関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリスクリプトです。GitHub APIからリポジトリ情報を取得し、加工、最終的なMarkdownファイルの生成までの一連の処理をオーケストレートします。
        - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために構造化データを埋め込むJSON-LD形式のテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語の使用割合などの情報を取得し、整形するロジックを含みます。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報から、最終的なリポジトリ一覧や個別のリポジトリ概要のMarkdownコンテンツを生成する主要なロジックを担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出し取得する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のパターンで記述されたバッジ情報（例: ビルドステータス、ライセンスなど）を抽出するロジックです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、整形、補完する役割を持つモジュールです。
        - **`seo_template.yml`**: SEO関連のメタデータや、Markdown出力に含めるテンプレート設定を定義します。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、レポートする機能を提供します。
        - **`strings.yml`**: 生成されるMarkdownやCLI出力で使用される各種メッセージ、ラベル、文言などを一元的に管理するファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Jinja2などのテンプレートエンジンを用いて、Markdownコンテンツの動的な生成を行うためのユーティリティ関数を提供します。
        - **`url_utils.py`**: GitHub APIやリポジトリへのURLを構築するためのヘルパー関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストケースを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestのテスト実行時に共有されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の統合テストを実施します。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトのテストケースを記述します。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストケースを記述します。
    - **`test_date_formatter.py`**: `date_formatter.py`モジュールのテストケースを記述します。
    - **`test_environment.py`**: プロジェクトの実行環境や依存関係に関するテストを実施します。
    - **`test_integration.py`**: 主要なコンポーネントが連携して正しく動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールのテストケースを記述します。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールの詳細なテストケースを記述します。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールのテストケースを記述します。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールのテストケースを記述します。

## 関数詳細説明
このプロジェクトはPythonスクリプトで構成されており、多くのモジュールと関数が含まれます。主要なモジュールとそこで提供される主な関数について説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   `main()`: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連のフローを制御します。
    -   `fetch_and_process_repos(username, limit, config)`: 指定されたGitHubユーザー名のリポジトリをGitHub APIから取得し、`repository_processor`などを用いて整形・処理します。
    -   `generate_output_markdown(repositories, output_path)`: 処理済みのリポジトリ情報を受け取り、`markdown_generator`を通じて最終的なリポジトリ一覧のMarkdownファイルを指定されたパスに出力します。

-   **`src/generate_repo_list/repository_processor.py`**:
    -   `process_repository_data(repo_data, config)`: GitHub APIから取得した単一のリポジトリの生データを受け取り、必要な情報を抽出し、表示に適したデータ構造に変換します。`project_overview_fetcher`や`badge_generator`などを呼び出して情報を付加します。

-   **`src/generate_repo_list/markdown_generator.py`**:
    -   `generate_repository_list_markdown(repositories, config, strings)`: 処理済みの全リポジトリ情報から、GitHub Pagesに表示するメインのリポジトリ一覧Markdownコンテンツを生成します。
    -   `generate_repository_section(repo, config, strings)`: 特定のリポジトリの情報を基に、そのリポジトリの表示セクション（タイトル、概要、バッジなど）のMarkdownスニペットを生成します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   `fetch_project_overview(owner, repo_name, config)`: 指定されたリポジトリのGitHubリポジトリから`config.yml`で定義された`project-overview.md`ファイルを読み込み、設定されたセクション（例: "プロジェクト概要"）から3行の概要を抽出して返します。APIキャッシュ機能も利用します。

-   **`src/generate_repo_list/config_manager.py`**:
    -   `load_config(config_path)`: YAML形式の設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書オブジェクトとして返します。
    -   `load_secrets(secrets_path)`: TOML形式のシークレットファイル（例: `secrets.toml`）を読み込み、機密情報（GitHubトークンなど）を提供します。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   `generate_badges(repo)`: リポジトリのステータス（例: アーカイブ済み、フォーク、アクティブ）や主要言語に応じて、表示用のバッジ（Markdown形式）を生成します。

-   **`src/generate_repo_list/date_formatter.py`**:
    -   `format_date(iso_date_string)`: ISO 8601形式の日付文字列を、ユーザーにとって読みやすい「YYYY年MM月DD日」のような形式に変換します。

-   **`src/generate_repo_list/url_utils.py`**:
    -   `build_github_api_url(username)`: GitHub APIのユーザーリポジトリ取得エンドポイントURLを構築します。
    -   `build_github_repo_url(owner, repo_name)`: GitHub上の特定リポジトリのURL（例: `https://github.com/owner/repo_name`）を構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-31 07:24:02 JST
