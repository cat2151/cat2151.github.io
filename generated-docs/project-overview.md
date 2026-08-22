Last updated: 2026-08-23

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧のMarkdownファイルを自動生成します。
- これにより、GitHub Pagesが検索エンジンにクロールされやすくなり、LLMからのリポジトリ参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (静的サイトジェネレーター), Markdown (コンテンツ記述)
- 音楽・オーディオ: (このプロジェクトでは該当する技術を使用していません)
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), PyYAML (YAML設定ファイル解析), toml (TOML設定ファイル解析)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: Pythonスクリプト群 (Markdownファイル生成ロジック)
- 言語機能: Python 3.x (HTTPリクエスト、ファイル操作、文字列処理など、言語の主要機能全般)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリ内のスクリプトは、自動化タスクに使用される)
- 開発標準: ruff (Pythonコードのフォーマットとリンティング), .editorconfig (エディタ設定の統一)

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
-   `.editorconfig`: 異なるエディタやIDEを使用する開発者の間で、コードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなど、GitHub上での自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    -   `check_large_files/README.md`: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    -   `check_large_files/check-large-files.toml`: 大容量ファイルの検出設定を定義するTOMLファイルです。
    -   `check_large_files/scripts/check_large_files.py`: 指定された閾値を超える大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリ（例: 一時ファイル、ビルド成果物）を指定する設定ファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）が記述されています。
-   `README.md`: プロジェクトの概要、目的、セットアップ方法、使い方、開発者向けのヒントなどを説明する主要なドキュメントです。
-   `_config.yml`: JekyllベースのGitHub Pagesサイトの設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
-   `assets/`: サイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像ファイルです。
-   `debug_project_overview.py`: `project_overview`機能のデバッグやテストに使用されるスクリプトです。
-   `generated-docs/`: 他のリポジトリから自動生成されたドキュメント（例: プロジェクト概要）が配置される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
-   `index.md`: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトによってリポジトリ一覧がここに生成されます。
-   `issue-notes/`: 課題や議論のメモを格納するディレクトリです。
    -   `22.md`: 特定の課題（Issue #22など）に関するメモや詳細が記述されたMarkdownファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示設定（名前、アイコン、起動方法など）を定義します。
-   `pytest.ini`: `pytest`フレームワークの設定ファイルです。テスト実行時のオプションや設定を定義します。
-   `requirements-dev.txt`: 開発およびテストに必要なPythonパッケージのリストです。
-   `requirements.txt`: プロジェクトの実行に必要な本番環境向けPythonパッケージのリストです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどのページをクロールしてよいか、または除外するかを指示するファイルです。
-   `ruff.toml`: `ruff`リンター/フォーマッターの設定ファイルです。コードのスタイルルールやチェック項目を定義します。
-   `src/`: プロジェクトのソースコードを格納する主要なディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリ一覧生成システムの主要なロジックを格納するパッケージです。
        -   `__init__.py`: `generate_repo_list`パッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのステータスや言語を示すバッジ画像を生成するためのロジックを含みます。
        -   `config.yml`: プロジェクト概要取得機能などの技術的パラメータや動作設定を定義するYAML形式の設定ファイルです。
        -   `config_manager.py`: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するためのモジュールです。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: このプロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        -   `json_ld_template.json`: SEO（検索エンジン最適化）を目的としたJSON-LD形式のデータ構造テンプレートです。
        -   `language_info.py`: GitHubリポジトリの主要言語情報を処理し、表示するためのロジックを含みます。
        -   `markdown_generator.py`: 処理されたリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するコアロジックです。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを自動的に取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、バッジ情報などの特定のパターンを抽出するロジックです。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを整形、フィルタリング、追加情報付与などを行う主要な処理モジュールです。
        -   `seo_template.yml`: サイトのSEOメタデータや構造に関するテンプレート定義を格納するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのロジックです。
        -   `strings.yml`: UIに表示されるメッセージや定型文を一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレートファイルの読み込み、変数置換などの処理を行うモジュールです。
        -   `url_utils.py`: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`で提供されるプロジェクト概要取得機能の単体テストを記述したファイルです。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリです。
    -   `conftest.py`: `pytest`のテストフィクスチャやヘルパー関数を定義するためのファイルです。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テストを記述したファイルです。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストです。
    -   `test_config.py`: 設定ファイルの読み込み・管理機能のテストです。
    -   `test_date_formatter.py`: 日付整形ユーティリティのテストです。
    -   `test_environment.py`: 開発環境のセットアップや依存関係に関するテストです。
    -   `test_integration.py`: システム全体の主要な連携部分の統合テストです。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテストです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストです。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストです。
    -   `test_repository_processor.py`: リポジトリデータ処理ロジックのテストです。

## 関数詳細説明
提供された情報には、関数の具体的な役割、引数、戻り値、機能に関する詳細がありませんでした。

## 関数呼び出し階層ツリー
```
[関数呼び出し階層を分析できませんでした]

---
Generated at: 2026-08-23 07:05:46 JST
