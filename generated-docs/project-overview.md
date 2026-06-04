Last updated: 2026-06-05

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、各リポジトリの情報からSEO最適化されたMarkdownファイルを生成します。
- 検索エンジンでの視認性向上を目指し、リポジトリの概要や分類表示でコンテンツ発見を容易にします。

## 技術スタック
- フロントエンド: Jekyll (静的サイトジェネレーターで、生成されたMarkdownファイルやテンプレートを元にGitHub Pagesを構築します。直接的なフロントエンドフレームワークではありませんが、コンテンツの表示基盤となります。), Markdown (コンテンツ記述言語として、リポジトリ一覧や各リポジトリの概要を記述するために使用されます。)
- 音楽・オーディオ: なし
- 開発ツール: Ruff (Pythonの高速なリンターおよびフォーマッター。コード品質の維持と統一されたコーディングスタイルを強制するために使用されます。)
- テスト: Pytest (Python製のテストフレームワーク。プロジェクトの各機能が正しく動作することを保証するための単体テストおよび統合テストの実行に使用されます。)
- ビルドツール: Python (メインのスクリプト言語であり、GitHub APIからのデータ取得、Markdown生成、ファイル出力といったプロジェクトの「ビルド」処理全体を実行します。)
- 言語機能: Python (汎用プログラミング言語Pythonそのものが、データ処理、API通信、ファイル操作など、プロジェクトの全ロジックを実装するために使用されます。)
- 自動化・CI/CD: GitHub Actions (このプロジェクト自体は生成システムですが、GitHub Actionsは生成されたコンテンツのデプロイや定期的な更新、あるいは本プロジェクトのテスト実行などに利用されることが想定されます。)
- 開発標準: Ruff (コードの品質を静的に分析し、指定されたコーディング規約に準拠しているかチェックするツールとして、開発標準の維持に貢献します。)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトを格納するディレクトリです。
  - **`check_large_files/`**: 大容量ファイルがないかチェックする自動化処理に関連するファイル群です。
    - **`README.md`**: `check_large_files` ディレクトリの目的と使い方を説明するファイルです。
    - **`check-large-files.toml`**: 大容量ファイルチェックの設定（しきい値など）を定義するTOML形式のファイルです。
    - **`scripts/check_large_files.py`**: 大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリ（一時ファイル、生成されたファイルなど）を指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などを説明するメインのドキュメントファイルです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイトの全体設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが設定されます。
- **`assets/`**: ウェブサイトで使用される静的なアセット（画像、ファビコンなど）を格納するディレクトリです。
  - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズです。
- **`debug_project_overview.py`**: `project_overview`機能（各リポジトリの概要取得）をデバッグするためのスクリプトです。
- **`generated-docs/`**: プロジェクトによって自動生成されるドキュメント（例：各リポジトリの概要ファイル）を格納するためのプレースホルダーディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイトの所有権を確認するために使用されるHTMLファイルです。
- **`index.md`**: 自動生成されたリポジトリ一覧が表示されるGitHub Pagesサイトのトップページ（メインのMarkdownファイル）です。
- **`issue-notes/`**: 課題やメモ、特定の機能に関する詳細な考察などを記録するディレクトリです。
  - **`22.md`**: 特定の課題（Issue #22）に関するメモや詳細が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブサイトをユーザーのデバイスにインストール可能にするための情報（アプリ名、アイコンなど）を提供します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター/フォーマッターであるRuffの設定を記述するTOML形式のファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
  - **`__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
  - **`generate_repo_list/`**: リポジトリ一覧生成に関するメインロジックを含むPythonパッケージです。
    - **`__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（画像）を生成または管理するロジックを含みます。
    - **`config.yml`**: プロジェクト固有の設定（例：プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するYAMLファイルです。
    - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理する役割を担います。
    - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: プログラムのエントリーポイントとなるスクリプトで、GitHub APIからのデータ取得からMarkdownファイルの生成まで、一連のリポジトリ一覧生成処理をオーケストレーションします。
    - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために構造化データ（JSON-LD形式）を生成するためのテンプレートファイルです。
    - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理、分析するロジックを含みます。
    - **`markdown_generator.py`**: 取得したリポジトリ情報から、SEO最適化されたMarkdown形式のコンテンツを生成する主要なロジックを提供します。
    - **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要のテキストを自動的に取得する機能を提供します。
    - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例：ビルドステータス、カバレッジなど）を抽出するロジックを含みます。
    - **`repository_processor.py`**: GitHub APIを通じてリポジトリ情報を取得し、それを内部で利用しやすい形式に整形・加工する役割を担います。
    - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算する機能を提供します。
    - **`strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
    - **`template_processor.py`**: Markdown生成時に利用されるテンプレートファイル（JekyllのLiquidテンプレートなど）を処理・レンダリングする機能を提供します。
    - **`url_utils.py`**: URLの生成、パース、検証など、URLに関連する様々なユーティリティ関数をまとめたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュール（プロジェクト概要取得機能）の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **`conftest.py`**: pytestのテスト実行時に共通して使用されるフィクスチャ（テストデータやセットアップ関数）を定義するファイルです。
  - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを記述したファイルです。
  - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを記述したファイルです。
  - **`test_config.py`**: 設定ファイル読み込み・管理機能のテストを記述したファイルです。
  - **`test_date_formatter.py`**: 日付整形機能のテストを記述したファイルです。
  - **`test_environment.py`**: 実行環境の設定や依存関係が正しく機能するかをテストするファイルです。
  - **`test_integration.py`**: 主要な機能やモジュール間の連携を含む統合テストを記述したファイルです。
  - **`test_markdown_generator.py`**: Markdown生成機能のテストを記述したファイルです。
  - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを記述したファイルです。
  - **`test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能のテストを記述したファイルです。
  - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストを記述したファイルです。

## 関数詳細説明
- **`generate_repo_list.py` 内の関数**
  - **`main()`**: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得とMarkdown生成の主要な処理フローを制御します。
    - 引数: なし (または `sys.argv` 経由でコマンドライン引数を受け取る)
    - 戻り値: なし
  - **`generate_repo_list(username, output_file, limit=None)`**: 指定されたGitHubユーザー名のリポジトリ一覧を生成し、指定された出力ファイルにMarkdown形式で書き込みます。
    - 引数: `username` (str): GitHubユーザー名, `output_file` (str): 出力するMarkdownファイル名, `limit` (int, optional): 処理するリポジトリ数の上限（開発用）
    - 戻り値: なし
- **`repository_processor.py` 内の関数**
  - **`fetch_repositories(username, token=None, limit=None)`**: GitHub APIを使用して、指定されたユーザーのリポジトリ情報を取得します。
    - 引数: `username` (str): GitHubユーザー名, `token` (str, optional): GitHubパーソナルアクセストークン, `limit` (int, optional): 取得するリポジトリ数の上限
    - 戻り値: list[dict]: 取得したリポジトリ情報のリスト
  - **`process_repository_data(repo_data)`**: 生のリポジトリデータを整形し、Markdown生成に適した形式に変換します。
    - 引数: `repo_data` (dict): GitHub APIから取得した個々のリポジトリデータ
    - 戻り値: dict: 整形されたリポジトリ情報
- **`markdown_generator.py` 内の関数**
  - **`generate_markdown_output(repositories, seo_data, strings_data)`**: 処理済みのリポジトリ情報とSEOデータ、文言データを用いて、最終的なMarkdownコンテンツを生成します。
    - 引数: `repositories` (list[dict]): 整形されたリポジトリ情報のリスト, `seo_data` (dict): SEO関連データ, `strings_data` (dict): 表示文言データ
    - 戻り値: str: 生成されたMarkdown文字列
- **`project_overview_fetcher.py` 内の関数**
  - **`fetch_project_overview(repo_name, owner, token, config)`**: 指定されたリポジトリの特定のパスからプロジェクト概要の3行説明をフェッチします。
    - 引数: `repo_name` (str): リポジトリ名, `owner` (str): リポジトリの所有者, `token` (str): GitHubトークン, `config` (dict): `project_overview`機能の設定
    - 戻り値: str: プロジェクト概要のテキスト、または空文字列
- **`config_manager.py` 内の関数**
  - **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込みます。
    - 引数: `config_path` (str): 設定ファイルのパス
    - 戻り値: dict: 読み込まれた設定データ
- **`date_formatter.py` 内の関数**
  - **`format_date(iso_date_string)`**: ISO 8601形式の日付文字列を読みやすい形式に整形します。
    - 引数: `iso_date_string` (str): ISO 8601形式の日付文字列
    - 戻り値: str: 整形された日付文字列
- **`badge_generator.py` 内の関数**
  - **`create_badge_url(label, message, color)`**: Shields.ioなどのサービスを利用して、指定されたラベル、メッセージ、色でバッジのURLを生成します。
    - 引数: `label` (str): バッジの左側のテキスト, `message` (str): バッジの右側のテキスト, `color` (str): バッジの色
    - 戻り値: str: 生成されたバッジ画像のURL
- **`url_utils.py` 内の関数**
  - **`create_github_repo_url(username, repo_name)`**: 指定されたユーザー名とリポジトリ名からGitHubリポジトリのURLを生成します。
    - 引数: `username` (str): GitHubユーザー名, `repo_name` (str): リポジトリ名
    - 戻り値: str: GitHubリポジトリのURL

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-06-05 07:34:06 JST
