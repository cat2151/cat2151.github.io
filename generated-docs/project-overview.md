Last updated: 2026-07-08

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・集約するシステムです。
- 取得した情報からJekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧を自動生成します。
- GitHub Pagesをクロール対象とすることで、検索エンジンやLLMからのリポジトリ参照性を向上させ、情報発見の課題を解決します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトが生成するMarkdownファイルはJekyllによって最終的なウェブページに変換されます。
    - **Markdown**: GitHub Pagesのコンテンツ記述に使用される軽量マークアップ言語。本プロジェクトの主要な出力形式です。
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用していません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報の取得、処理、Markdown生成を行うスクリプトの実行環境です。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために使用されます。
- テスト:
    - **pytest**: Pythonアプリケーションのテストフレームワーク。プロジェクトの機能が期待通りに動作するかを検証するために使用されます。
- ビルドツール:
    - **Pythonスクリプト**: 特定のビルドツールは使用せず、Pythonスクリプト自体がGitHub APIからのデータ取得とMarkdown生成の「ビルド」プロセスを担います。
- 言語機能:
    - **Python**: GitHub APIとの連携、データ処理、ファイルI/Oなど、プロジェクトの中核機能を実装するために使用されます。
- 自動化・CI/CD:
    - **GitHub Actions (示唆)**: プロジェクト情報に明示的なCI/CDの設定はありませんが、`.github_automation`ディレクトリの存在から、将来的または補助的にGitHub Actionsのような自動化ツールが利用される可能性が示唆されます。
- 開発標準:
    - **ruff**: Pythonコードのリンターおよびフォーマッター。コード品質とスタイルの一貫性を保つために使用されます。
    - **.editorconfig**: 異なるエディタやIDE間で基本的なコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するためのディレクトリです。
    - **`check_large_files/`**: 大容量ファイルをチェックするための自動化スクリプトが含まれるサブディレクトリです。
        - **`README.md`**: `check_large_files`機能に関する説明を提供します。
        - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義します。ビルド生成物や一時ファイルなどが含まれます。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、セットアップ方法、使用方法、ライセンスなどの基本的な情報を提供するプロジェクトの顔となるドキュメントです。
- **`_config.yml`**: Jekyllサイト全体のグローバルな設定を定義するファイルです。テーマ、プラグイン、URL構造などが含まれます。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の異なるサイズを提供します。
- **`debug_project_overview.py`**: プロジェクト概要の取得機能をデバッグするための補助的なスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールでサイト所有権を検証するために使用されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトでは、生成されたリポジトリ一覧がここに出力されます。
- **`issue-notes/`**: プロジェクト開発中の特定の問題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定のイシュー番号（22）に関する詳細なメモや議論が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの表示方法や動作（ホーム画面アイコン、起動画面など）を定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルです。テストの発見方法や実行オプションなどを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージの依存関係を定義します。
- **`requirements.txt`**: プロジェクトの本番稼働に必要なPythonパッケージの依存関係を定義します。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対し、ウェブサイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: `ruff`リンターおよびフォーマッターの設定ファイルです。Pythonコードのスタイルチェックや自動修正のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すためのファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成する主要なロジックが含まれるパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージを示すためのファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを実装しています。
        - **`config.yml`**: プロジェクト概要取得機能など、アプリケーションの実行に関する技術的パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`など) の読み込みと管理を行うモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクト全体のエントリポイントとなるメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        - **`json_ld_template.json`**: SEO最適化のために、構造化データ（JSON-LD形式）のテンプレートを定義します。
        - **`language_info.py`**: リポジトリの使用言語に関する情報を取得・処理するロジックを含みます。
        - **`markdown_generator.py`**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するコアロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、取得する機能を提供します。
        - **`readme_badge_extractor.py`**: READMEファイルからバッジ情報を抽出するためのロジックを含みます。
        - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを処理し、表示に適した形式に変換する役割を担います。
        - **`seo_template.yml`**: SEO関連のメタデータやテンプレートを定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するロジックを提供します。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成におけるテンプレート処理を管理するモジュールです。
        - **`url_utils.py`**: URLの生成や解析など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能をテストするためのスクリプトです。
- **`tests/`**: プロジェクトのテストコードを格納するディレクトリです。
    - **`conftest.py`**: `pytest`のテスト設定やフィクスチャを定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを行います。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを行います。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストを行います。
    - **`test_date_formatter.py`**: 日付フォーマット機能のテストを行います。
    - **`test_environment.py`**: 実行環境の設定や依存関係に関するテストを行います。
    - **`test_integration.py`**: プロジェクト全体の主要な統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストを行います。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行います。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストを行います。
    - **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行います。

## 関数詳細説明
提供された情報からは具体的な関数の引数、戻り値、詳細な機能は直接読み取れませんでした。しかし、ファイル名からその役割を推測できます。以下に主要なモジュールと、それぞれに含まれると想定される主要関数の役割を説明します。

-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   **`main()`**:
        -   役割: プログラムのエントリポイント。コマンドライン引数を解析し、設定を読み込み、リポジトリ情報の取得からMarkdown生成までの全体フローを orchestrate します。
        -   引数: 通常はコマンドライン引数 (`--username`, `--output`, `--limit` など) を内部で処理します。
        -   戻り値: なし (あるいはプログラムの成功/失敗を示す終了コード)。
        -   機能: GitHub APIクライアントの初期化、リポジトリデータのフェッチ、各リポジトリの処理、Markdownコンテンツの生成とファイルへの書き込みを行います。

-   **`src/generate_repo_list/repository_processor.py`**:
    -   **`process_repository(repo_data)`**:
        -   役割: 個々のGitHubリポジトリの生データを整形し、Markdown生成に適した形式に変換します。
        -   引数: `repo_data` (GitHub APIから取得したリポジトリの生データ辞書)。
        -   戻り値: 整形されたリポジトリ情報 (辞書)。
        -   機能: 必要な情報の抽出、欠損データの補完、言語情報の処理、最終更新日のフォーマットなどを行います。

-   **`src/generate_repo_list/markdown_generator.py`**:
    -   **`generate_markdown(repo_list_data)`**:
        -   役割: 処理されたリポジトリのリストを受け取り、最終的なMarkdownコンテンツ文字列を生成します。
        -   引数: `repo_list_data` (処理済みリポジトリ情報のリスト)。
        -   戻り値: 生成されたMarkdownコンテンツ (文字列)。
        -   機能: テンプレートを用いてリポジトリ情報をMarkdown形式に組み込み、バッジやプロジェクト概要なども適切に配置します。

-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   **`fetch_project_overview(repo_url, config)`**:
        -   役割: 特定のリポジトリ内の指定されたパスからプロジェクト概要のテキスト（3行説明）を非同期で取得します。
        -   引数: `repo_url` (リポジトリのURL)、`config` (概要取得設定を含む設定オブジェクト)。
        -   戻り値: 抽出されたプロジェクト概要 (文字列、または取得失敗時はNone)。
        -   機能: GitHubのコンテンツAPIなどを利用してファイル内容を取得し、設定されたセクションタイトルに基づいて概要部分をパースします。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   **`generate_badge_markdown(status, type)`**:
        -   役割: リポジトリのステータス（例: アクティブ、アーカイブ）やタイプ（例: フォーク）に応じたMarkdown形式のバッジ文字列を生成します。
        -   引数: `status` (リポジトリの状態を示す文字列), `type` (リポジトリのタイプを示す文字列)。
        -   戻り値: バッジのMarkdown文字列。
        -   機能: 定義済みのバッジテンプレートに基づき、適切なバッジ画像を埋め込むMarkdownを生成します。

-   **`src/generate_repo_list/config_manager.py`**:
    -   **`load_config(config_path)`**:
        -   役割: YAML設定ファイルを読み込み、Pythonオブジェクトとして提供します。
        -   引数: `config_path` (設定ファイルへのパス)。
        -   戻り値: 設定データ (辞書またはオブジェクト)。
        -   機能: ファイルの存在チェック、YAMLパース、デフォルト値の適用などを行います。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-08 07:26:33 JST
