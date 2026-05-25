Last updated: 2026-05-26

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEO最適化されたMarkdownファイルを出力します。
- 各リポジトリの概要、バッジ、分類などを表示し、検索エンジンからの可視性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll**: 静的サイトジェネレータとしてGitHub Pagesサイトの基盤となり、生成されたMarkdownファイルをHTMLに変換します。**GitHub Pages**: 生成されたコンテンツをホスティングし、公開するためのプラットフォームです。
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python**: リポジトリ情報の取得、処理、Markdown生成のメイン開発言語です。**GitHub API**: GitHubリポジトリの情報をプログラムで取得するための主要なインターフェースとして使用されます。
- テスト: **pytest**: Pythonコードの単体テストや統合テストを記述・実行するためのテストフレームワークです。
- ビルドツール: 特になし (Pythonスクリプトが直接Markdownファイルを生成するため、一般的なビルドツールは使用されていません)。
- 言語機能: **Python**: データ処理、API通信、ファイル操作など、システムの中核をなすスクリプト言語です。
- 自動化・CI/CD: **GitHub Actions**: 明示的な設定ファイルはないものの、自動化の可能性を示唆しており、将来的なスクリプトの自動実行や継続的デリバリーの基盤となり得ます。
- 開発標準: **ruff**: Pythonコードのリンターおよびフォーマッターとして、コード品質の維持とスタイルの統一に貢献します。**.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタ間でインデントスタイル、文字コードなどの基本的なコーディングスタイル設定を統一するためのファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトに関する説明ドキュメントです。
    - **`.github_automation/check_large_files/check-large-files.toml`**: `check_large_files.py`スクリプトの設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大規模ファイルをチェックするためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定、開発者向けヒントなどをまとめた主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を定義します。
- **`assets/`**: Jekyllサイトで表示される画像、アイコンなどの静的ファイルを格納するディレクトリです。
    - **`assets/favicon-16x16.png`**: サイトのファビコン（16x16ピクセル）です。
    - **`assets/favicon-192x192.png`**: サイトのファビコン（192x192ピクセル）です。
    - **`assets/favicon-32x32.png`**: サイトのファビコン（32x32ピクセル）です。
    - **`assets/favicon-512x512.png`**: サイトのファビコン（512x512ピクセル）です。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用される補助的なPythonスクリプトです。
- **`generated-docs/`**: 各リポジトリから自動取得されたドキュメント（例: プロジェクト概要）を格納するためのプレースホルダーディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: 自動生成されたリポジトリ一覧のMarkdownコンテンツが出力されるメインファイルです。Jekyllによって最終的にHTMLページとして表示されます。
- **`issue-notes/`**: プロジェクト開発中の課題やメモを記録するためのディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題に関する詳細なメモファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示名、アイコン、起動モードなどを定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの検出ルールや実行オプションを定義します。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、または避けるべきかを指示するファイルです。
- **`ruff.toml`**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルで、コードスタイルと品質に関するルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示す初期化ファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成機能の中核となるPythonモジュール群を格納するパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示す初期化ファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの技術スタックやステータスを示すバッジ（例: 言語バッジ）を生成する機能を提供します。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータや実行時設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`のような設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい形式や特定の表示形式に整形するためのユーティリティモジュールです。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する一連の処理を調整します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD）を生成するためのテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: 各リポジトリの主要なプログラミング言語に関する情報を処理し、表示や分類に利用する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータから、最終的に出力されるMarkdownコンテンツを構築するロジックをカプセル化したモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で取得するモジュールです。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を持つモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、それを分析、フィルタリング、整形して、表示に適した形式に変換する主要なロジックを格納するモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: サイト全体のSEOメタデータや、個々のリポジトリページに適用されるSEO関連の設定を定義するためのテンプレートYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: 各リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、集計する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を集中管理するYAMLファイルで、国際化/ローカライズの基盤となります。
        - **`src/generate_repo_list/template_processor.py`**: Markdownコンテンツ生成の際に使用されるテンプレート（文字列フォーマットやJinja2のようなテンプレートエンジン）を処理するモジュールです。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URL関連の様々なユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator`モジュールの複数のコンポーネントが連携して正しく動作するかを検証する統合テストです。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files.py`スクリプトの機能を検証するテストです。
    - **`tests/test_config.py`**: `config_manager`モジュールや設定ファイル (`config.yml`など) の読み込み、解析が正しく行われるかを検証するテストです。
    - **`tests/test_date_formatter.py`**: `date_formatter`モジュールの日付整形機能が正しく動作するかを検証するテストです。
    - **`tests/test_environment.py`**: 開発環境や依存関係のセットアップが適切であるかを確認するテストです。
    - **`tests/test_integration.py`**: プロジェクトの主要なフロー（APIからの情報取得からMarkdown生成まで）が全体として正しく動作するかを検証する統合テストです。
    - **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールのMarkdownコンテンツ生成ロジックが正しく動作するかを検証するテストです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールのプロジェクト概要取得機能が正しく動作するかを検証するテストです。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールのREADMEからのバッジ抽出機能が正しく動作するかを検証するテストです。
    - **`tests/test_repository_processor.py`**: `repository_processor`モジュールがリポジトリデータを正しく処理・変換するかを検証するテストです。

## 関数詳細説明
提供された情報では、個々のPythonファイルの具体的な関数シグネチャ（引数、戻り値）や詳細な実装が検出されませんでした。そのため、各関数の詳細説明を具体的に記述することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-26 07:26:24 JST
