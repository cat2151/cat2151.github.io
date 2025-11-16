Last updated: 2025-11-17

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのGitHub Pages向けにリポジトリ一覧Markdownを自動生成するシステムです。
- SEOを考慮し、各リポジトリの概要も取得表示することで、検索エンジンでの発見性を高めます。
- Jekyll/GitHub Pagesに対応しており、LLMがリポジトリ参照に失敗する課題の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll/GitHub Pages** (生成されるMarkdownをホスト), **Markdown** (リポジトリ一覧の出力形式), **HTML/CSS** (生成されるページで利用)
- 音楽・オーディオ: (該当なし)
- 開発ツール: **pytest** (テストフレームワーク), **ruff** (Pythonコードのリンター/フォーマッター), **GitHub API** (リポジトリ情報取得)
- テスト: **pytest** (Pythonコードのテスト実行)
- ビルドツール: **Python** (スクリプト実行環境), **Jekyll** (GitHub Pagesの静的サイトジェネレーター、本プロジェクトが生成するMarkdownのホスト環境)
- 言語機能: **Python** (主要な開発言語)
- 自動化・CI/CD: (このプロジェクト自体のCI/CDは「ローカル開発重視」とされており、明示的に利用はされていません。ただし、他のリポジトリ管理にGitHub Actionsの利用が言及されています。)
- 開発標準: **ruff** (コードスタイルと品質の統一)

## ファイル階層ツリー
```
📄 .editorconfig
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
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.gitignore**: Gitが追跡しないファイルやディレクトリを指定するファイルです。ビルド生成物や一時ファイルなどが含まれます。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、使用方法、設定、開発者向け情報などを説明するプロジェクトの顔となるドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesの基本的な挙動を制御します。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: サイトのアイコンとして使用される各種サイズのファビコン画像ファイルです。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグや単体テストを行うためのスクリプトと推測されます。
- **generated-docs/**: 生成されたドキュメントや一時ファイルを格納するためのディレクトリと推測されます。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、GitHubリポジトリの一覧を含むメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: プロジェクトの課題、メモ、検討事項などをMarkdown形式で記録したファイル群を格納するディレクトリです。
- **manifest.json**: Webアプリケーションマニフェストファイルで、PWA（Progressive Web App）としてWebサイトをインストール可能にするためのメタデータを提供します。
- **pytest.ini**: pytestテストフレームワークの設定ファイルです。テストの発見方法や実行オプションなどが定義されます。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記載したファイルです。
- **requirements.txt**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてよいか、あるいはクロールすべきでないかを指示するファイルです。
- **ruff.toml**: RuffというPythonリンター/フォーマッターの設定ファイルです。コードスタイルの規則や自動修正の設定が定義されます。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧生成ロジックの主要なモジュール群をまとめたPythonパッケージです。
        - **__init__.py**: `generate_repo_list`がPythonパッケージであることを示します。
        - **badge_generator.py**: リポジトリの各種情報（言語、ライセンスなど）に基づいてバッジ画像を生成するロジックを実装しています。
        - **config.yml**: プロジェクト概要の取得設定など、アプリケーションの動作に関する技術的パラメータを定義するYAML形式の設定ファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するロジックを提供します。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を統括します。
        - **json_ld_template.json**: SEOのために構造化データ（JSON-LD形式）を生成する際のテンプレートとなるJSONファイルです。
        - **language_info.py**: リポジトリの主要言語に関する情報を取得・処理するロジックが含まれています。
        - **markdown_generator.py**: 取得したリポジトリ情報やプロジェクト概要などを元に、最終的なMarkdown形式のコンテンツを生成するロジックを実装しています。
        - **project_overview_fetcher.py**: 各GitHubリポジトリ内にある特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動的に抽出し取得する機能を提供します。
        - **repository_processor.py**: GitHub APIを通じてユーザーのリポジトリ情報を取得し、必要なデータに加工・整形する役割を担います。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータや記述のテンプレートを定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックを提供します。
        - **strings.yml**: UIに表示されるメッセージ、見出し、説明文など、アプリケーションで使用される各種テキスト文字列を集中管理するYAMLファイルです。
        - **template_processor.py**: Markdown生成やJSON-LD生成において、テンプレートファイルに変数を埋め込むなどの処理を行う汎用的なテンプレート処理ロジックです。
        - **url_utils.py**: URLの生成、解析、正規化など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher`モジュールに関する単体テストを定義するスクリプトです。
- **tests/**: プロジェクトのテストスクリプトを格納するディレクトリです。
    - **test_config.py**: 設定ファイルの読み込みや管理機能に関するテストが含まれます。
    - **test_environment.py**: テスト実行環境や依存関係が正しく設定されているかを確認するテストが含まれます。
    - **test_integration.py**: 複数のモジュールが連携して正しく動作するかを確認する統合テストが含まれます。
    - **test_markdown_generator.py**: Markdownコンテンツ生成ロジックの正確性を検証するテストが含まれます。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`が正しくプロジェクト概要を取得できるかを検証するテストです。
    - **test_repository_processor.py**: リポジトリ情報の取得と処理ロジックの正確性を検証するテストです。

## 関数詳細説明
プロジェクト情報には具体的な関数シグネチャが提供されていないため、ファイル名と説明から推測される主要な関数とその役割について説明します。

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main()`**: スクリプトのエントリポイント。コマンドライン引数を解析し、リポジトリ一覧生成の主要な処理フローを orchestrate します。
        - 引数: なし (またはコマンドライン引数を内部で処理)
        - 戻り値: なし (または処理成功/失敗を示すステータスコード)
    - **`parse_arguments()`**: コマンドライン引数（ユーザー名、出力ファイル名、リポジトリ制限など）を解析し、設定オブジェクトとして返します。
        - 引数: なし (または生のコマンドライン引数リスト)
        - 戻り値: 引数からパースされた設定を含む辞書またはオブジェクト
    - **`generate_repo_list(config)`**: 指定された設定に基づいて、GitHub APIからリポジトリ情報を取得し、Markdownを生成して指定されたファイルに出力する主要な処理を実行します。
        - 引数: `config` (設定オブジェクト/辞書)
        - 戻り値: なし (または処理成功/失敗を示すブール値)

- **`src/generate_repo_list/repository_processor.py`**
    - **`fetch_repositories(username, token, limit=None)`**: 指定されたGitHubユーザー名のリポジトリをGitHub APIから取得します。
        - 引数: `username` (str), `token` (str, GitHub API認証トークン), `limit` (int, 取得するリポジトリ数の上限, オプション)
        - 戻り値: 取得したリポジトリデータのリスト (辞書のリスト)
    - **`process_repository_data(repo_data)`**: 生のリポジトリデータを受け取り、表示に適した形式に加工・整形します。
        - 引数: `repo_data` (辞書, 個々のリポジトリの生データ)
        - 戻り値: 処理済みのリポジトリ情報を含む辞書

- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_name, owner, file_path, config)`**: 指定されたリポジトリ内の特定のファイルからプロジェクト概要の3行説明を抽出して取得します。
        - 引数: `repo_name` (str), `owner` (str), `file_path` (str, 概要ファイルへのパス), `config` (設定オブジェクト)
        - 戻り値: プロジェクト概要のテキスト (str) または None

- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_markdown_for_repository(repository_info)`**: 単一のリポジトリ情報からMarkdown形式の表示スニペットを生成します。
        - 引数: `repository_info` (辞書, 処理済みリポジトリ情報)
        - 戻り値: 生成されたMarkdown文字列
    - **`generate_full_markdown_output(all_repositories_info, template_data)`**: 全リポジトリ情報とテンプレートデータを使用して、最終的な`index.md`の内容となるMarkdown文字列全体を生成します。
        - 引数: `all_repositories_info` (リスト, 全リポジトリの処理済み情報), `template_data` (辞書, ページ全体のテンプレートに渡すデータ)
        - 戻り値: 完成したMarkdownドキュメントの文字列

- **`src/generate_repo_list/badge_generator.py`**
    - **`generate_badge_markdown(label, message, color)`**: 指定された情報から、Markdown形式で表示されるバッジの文字列を生成します。
        - 引数: `label` (str), `message` (str), `color` (str)
        - 戻り値: バッジのMarkdown文字列

- **`src/generate_repo_list/config_manager.py`**
    - **`load_config(file_path)`**: 指定されたパスのYAML設定ファイルを読み込み、Pythonオブジェクトとして返します。
        - 引数: `file_path` (str, 設定ファイルへのパス)
        - 戻り値: 設定内容を示す辞書またはオブジェクト

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-17 07:05:43 JST
