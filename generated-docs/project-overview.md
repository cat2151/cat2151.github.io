Last updated: 2025-12-18

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するPythonシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 生成されたMarkdownコンテンツがJekyllベースのGitHub Pagesサイトで表示されます。
- 音楽・オーディオ: 該当なし - このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール:
    - GitHub API (REST API): リポジトリ情報の取得に使用するWeb API。
    - Python: プロジェクトの主要な開発言語および実行環境。
    - `ruff`: Pythonコードのスタイルチェックと自動修正を行う高速リンター・フォーマッター。
- テスト: `pytest` - Pythonコードのユニットテストおよび統合テストフレームワーク。
- ビルドツール: Pythonスクリプト - `generate_repo_list.py` がリポジトリ情報からMarkdownコンテンツを生成するビルドプロセスを担います。
- 言語機能: Python言語の標準機能 - スクリプトの記述にPythonの基本的な構文とライブラリを使用します。
- 自動化・CI/CD: GitHub Pages - 生成されたコンテンツの公開プラットフォームであり、自動デプロイのターゲットとなります。
- 開発標準: `ruff` - コード品質を維持し、統一されたコーディングスタイルを強制するために使用されます。

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
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDE間でコードのフォーマット設定（インデントスタイル、文字コードなど）を統一するための設定ファイル。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイル。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使い方、ライセンスなど、プロジェクトに関する包括的な情報を提供するメインドキュメント。
- **_config.yml**: JekyllベースのGitHub Pagesサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどを定義します。
- **assets/**: サイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズ。
- **debug_project_overview.py**: `project-overview.md` ファイルからのプロジェクト概要抽出機能のデバッグを目的としたスクリプト。
- **generated-docs/**: スクリプトによって生成される可能性のあるドキュメントやデータが格納されるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: 生成されたリポジトリ一覧コンテンツを含む、GitHub Pagesサイトのメインページとして機能するMarkdownファイル。
- **issue-notes/**: 開発過程で発生した課題や検討事項、メモなどを記録したMarkdownファイルを格納するディレクトリ。
    - **10.md**, **12.md**, **14.md**, **2.md**, **4.md**, **6.md**, **8.md**: 個別の課題やメモに関する詳細な内容が記述されたファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のメタデータを提供するWebアプリケーションマニフェストファイル。ホーム画面への追加、表示モードなどを定義します。
- **pytest.ini**: `pytest` テストフレームワークの設定ファイル。テストの実行方法やプラグイン、オプションなどを指定します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **requirements.txt**: プロジェクトの本番稼働に必要なPythonパッケージとそのバージョンを記述したファイル。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するファイル。
- **ruff.toml**: `ruff` リンター・フォーマッターの設定ファイル。コードスタイルルール、無視するエラー、対象ファイルなどを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **__init__.py**: Pythonパッケージであることを示すファイル。
    - **generate_repo_list/**: リポジトリ一覧を生成するコアロジックを含むPythonパッケージ。
        - **__init__.py**: Pythonパッケージであることを示すファイル。
        - **badge_generator.py**: リポジトリに関連するバッジ（例：言語、ステータス）の情報を生成するロジックを実装。
        - **config.yml**: リポジトリ一覧生成スクリプトの実行に関する設定パラメータ（プロジェクト概要取得設定、キャッシュ設定など）を定義するYAMLファイル。
        - **config_manager.py**: `config.yml` や `secrets.toml` などの設定ファイルを読み込み、管理するためのユーティリティ。
        - **generate_repo_list.py**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD形式）のテンプレート。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するロジック。
        - **markdown_generator.py**: 取得したリポジトリ情報とテンプレートに基づいて、GitHub Pages用のMarkdownコンテンツを生成するロジック。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得するロジック。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・処理するロジック。
        - **seo_template.yml**: SEO関連のメタデータや表示設定を定義するYAMLテンプレートファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジック。
        - **strings.yml**: UIメッセージ、説明文、タイトルなど、表示されるテキストコンテンツを一元管理するためのYAMLファイル（国際化対応などに利用）。
        - **template_processor.py**: Markdown生成時に使用される各種テンプレートの読み込み、レンダリング、埋め込み処理を行うロジック。
        - **url_utils.py**: URLの検証、整形、生成など、URLに関連する様々なユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能、特にプロジェクト概要の取得ロジックに関する単体テスト。
- **tests/**: プロジェクト全体のテストファイルを格納するディレクトリ。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテスト。
    - **test_environment.py**: プロジェクトの実行環境や依存関係に関するテスト。
    - **test_integration.py**: 複数のコンポーネントが連携して正しく機能するかを確認する結合テスト。
    - **test_markdown_generator.py**: `markdown_generator.py` の機能、特にMarkdownコンテンツの正確な生成に関するテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py` の機能テスト（冗長だが、`test_project_overview.py` と同様の目的）。
    - **test_repository_processor.py**: `repository_processor.py` の機能、特にリポジトリデータ処理ロジックに関するテスト。

## 関数詳細説明
提供されたプロジェクト情報には、個々のPython関数の詳細な説明（引数、戻り値、機能）は含まれていません。そのため、具体的な関数説明は省略します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-18 07:06:12 JST
