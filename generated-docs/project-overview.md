Last updated: 2026-07-25

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得するシステムです。
- 取得した情報に基づき、JekyllベースのGitHub Pagesサイト用にMarkdownファイルを自動生成します。
- SEOを最適化し、検索エンジンからの可視性を高めるとともに、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレータ。生成されたMarkdownファイルを美しいWebサイトとして公開するための基盤として利用されます。
- 音楽・オーディオ: 該当なし - このプロジェクトは音楽・オーディオ関連の技術を使用していません。
- 開発ツール: pytest - Pythonのテストフレームワーク。プロジェクトの各コンポーネントの動作検証に使用されます。ruff - Pythonの高速リンター/フォーマッター。コードの品質維持とスタイル統一を自動化します。
- テスト: pytest - Pythonプロジェクトの単体テスト、結合テストに利用される標準的なテストフレームワークです。
- ビルドツール: Pythonスクリプト - GitHub APIからデータを取得し、Jekyll対応のMarkdownファイルを自動生成する主要なスクリプト群です。
- 言語機能: Python - プロジェクトの主要なロジックを実装するために使用されるプログラミング言語です。
- 自動化・CI/CD: GitHub Pages - GitHubが提供する静的サイトホスティングサービス。生成されたリポジトリ一覧ページを公開するために利用されます。
- 開発標準: ruff - Pythonコードの品質と一貫性を保つためのリンターおよびフォーマッター。定義されたコーディングスタイルに準拠しているかチェックし、自動修正します。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で一貫したコードスタイル（インデント、改行など）を維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどのリポジトリ自動化スクリプトや設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明が記載されています。
    - **`.github_automation/check_large_files/check-large-files.toml`**: リポジトリ内の大容量ファイル検出に関する設定を定義します。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリ（例: ビルド成果物、一時ファイル）を指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）を明記したファイルで、プロジェクトの利用条件を示します。
- **`README.md`**: プロジェクトの概要、目的、主な機能、設定方法、テスト実行方法など、プロジェクトに関する最も重要な情報を提供する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体のグローバルな設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: Jekyllサイトで利用される画像やファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像（様々なサイズ）です。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されたプロジェクト概要などのドキュメントが格納されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページ（トップページ）となるMarkdownファイルです。ここにリポジトリ一覧が自動生成されます。
- **`issue-notes/`**: 開発中の課題や、将来的な改善点に関するメモを格納するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題や検討事項（Issue #22）に関する詳細なメモや情報が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のWebマニフェストファイルで、アプリの名前、アイコン、表示設定などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの実行オプションやパスなどを指定します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストしたファイルです。
- **`requirements.txt`**: プロジェクトを本番環境で実行するために必要なPythonパッケージの依存関係をリストしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールし、どのページをインデックスすべきかを指示するファイルです。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッター`ruff`の設定ファイルです。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するルートディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージとして`src`ディレクトリを識別するためのファイルです。
    - **`src/generate_repo_list/`**: GitHubリポジトリ一覧生成システムの主要なロジックをカプセル化するPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するためのファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例: アクティブ、アーカイブ）を示すバッジの生成ロジックを含みます。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成システムの動作に関する設定（例: プロジェクト概要取得機能の有効/無効、タイムアウト時間）を定義します。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プロジェクト内で利用可能にするためのロジックを提供します。
        - **`src/generate_repo_list/date_formatter.py`**: リポジトリの更新日時などの日付情報を、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトの中心となるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する全体のフローを制御します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のため、検索エンジンにコンテンツを理解させるためのJSON-LD形式の構造化データテンプレートです。
        - **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語の統計情報などを処理するロジックを含みます。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報から、GitHub Pages向けに整形されたMarkdownコンテンツを生成する主要なロジックを提供します。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し取得するスクリプトです。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報などを抽出するロジックを含みます。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを整形し、後続のMarkdown生成に適した形式に変換するロジックを提供します。
        - **`src/generate_repo_list/seo_template.yml`**: 生成されるMarkdownファイルのSEO関連のメタデータ（キーワード、ディスクリプションなど）を設定するためのテンプレートファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するロジックを含みます。
        - **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言などを一元的に管理し、多言語対応や文言変更を容易にするための設定ファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成において、特定のテンプレート構文（例: JekyllのLiquid）を処理し、動的なコンテンツを埋め込むためのロジックを提供します。
        - **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリのURLやGitHub PagesのURLなど、URL関連の操作（生成、解析、検証）を行うユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストや統合テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest`フレームワークでテストスイート全体に適用される共通のフィクスチャやヘルパー関数を定義するファイルです。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を検証するためのテストファイルです。
    - **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能の動作を検証するためのテストファイルです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理機能の正確性を検証するためのテストファイルです。
    - **`tests/test_date_formatter.py`**: 日付フォーマットユーティリティの正確性を検証するためのテストファイルです。
    - **`tests/test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係の検証を行うテストファイルです。
    - **`tests/test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく機能するかを検証する統合テストファイルです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能が期待通りにコンテンツを生成するかを検証するためのテストファイルです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能の正確性を検証するためのテストファイルです。
    - **`tests/test_readme_badge_extractor.py`**: READMEからバッジ情報を抽出する機能の正確性を検証するためのテストファイルです。
    - **`tests/test_repository_processor.py`**: GitHubリポジトリデータの処理機能の正確性を検証するためのテストファイルです。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数の詳細な説明（役割、引数、戻り値、具体的な機能）が含まれていません。そのため、具体的な関数名、引数、戻り値、および機能について記述することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-25 07:25:29 JST
