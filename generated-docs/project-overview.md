Last updated: 2026-08-29

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンでのリポジトリ発見性を高め、LLMによるリポジトリ参照失敗を緩和することを目的としています。
- 各リポジトリの概要、言語、バッジ、アクティビティなどを動的に表示し、SEO最適化されたコンテンツを提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (コンテンツ生成フォーマット)
- 音楽・オーディオ: N/A
- 開発ツール: Python (主要なスクリプト言語), Pytest (テストフレームワーク), Ruff (Pythonコードリンター・フォーマッター), GitHub API (リポジトリ情報取得)
- テスト: Pytest (Pythonコードのユニットテストおよび統合テスト)
- ビルドツール: Pythonスクリプト (GitHub APIから取得したデータに基づくMarkdownファイル生成ロジック)
- 言語機能: Python (汎用プログラミング言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリから推測される自動化処理の実行環境), EditorConfig (`.editorconfig` による複数エディタでのコードスタイル統一)
- 開発標準: Ruff (Pythonコードの品質と一貫性を保証するリンティング・フォーマット), EditorConfig

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコードのインデントや文字エンコーディングなどのスタイルを統一するための設定ファイル。
-   **`.github_automation/`**: GitHub ActionsなどのCI/CDや自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    -   **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    -   **`check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイル。
    -   **`scripts/check_large_files.py`**: GitHubリポジトリ内の指定されたサイズを超えるファイルを検出するためのPythonスクリプト。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイル。
-   **`LICENSE`**: プロジェクトのライセンス情報（本プロジェクトではMITライセンス）。
-   **`README.md`**: プロジェクトの目的、機能、使い方、開発者向けのヒントなどをまとめた、プロジェクトの主要な説明ドキュメント。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。GitHub Pagesの挙動やサイトのメタデータを定義します。
-   **`assets/`**: ウェブサイトで使用する静的アセット（画像、アイコンなど）を格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示される小さなアイコン）画像ファイル群。
-   **`debug_project_overview.py`**: `project_overview` 機能（各リポジトリの概要抽出）のデバッグや単体テストを行うためのスクリプト。
-   **`generated-docs/`**: 本システムによって動的に生成されたドキュメントやデータが格納されるディレクトリ。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールによるサイト所有権確認のために使用されるHTMLファイル。
-   **`index.md`**: GitHub PagesサイトのルートページとなるMarkdownファイル。リポジトリ一覧がこのファイルに生成・出力されます。
-   **`issue-notes/22.md`**: 特定のGitHub Issue（ここではIssue #22）に関する詳細なメモや検討内容を記述したMarkdownファイル。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイル。ウェブアプリのメタデータやホーム画面への追加設定などを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイル。テストの実行オプションやパスなどを指定します。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンを列挙したファイル。
-   **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonパッケージとそのバージョンを列挙したファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、またはクロールすべきでないかを指示するファイル。
-   **`ruff.toml`**: Pythonの高速リンター・フォーマッターである`ruff`の設定ファイル。コードスタイルや潜在的なバグの検出ルールを定義します。
-   **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイル。
-   **`src/generate_repo_list/`**: リポジトリ一覧自動生成システムの主要なロジックが配置されているPythonパッケージ。
    -   **`__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
    -   **`badge_generator.py`**: リポジトリに関連するバッジ（例: 言語バッジ、ステータスバッジ）を生成または処理するロジックを実装。
    -   **`config.yml`**: リポジトリ一覧生成機能の動作を制御する技術的パラメータ（例: プロジェクト概要取得設定）を定義するYAMLファイル。
    -   **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム全体で利用するための設定管理モジュール。
    -   **`date_formatter.py`**: 日付や時刻データを特定のフォーマット（例: "YYYY-MM-DD"）に変換するユーティリティ関数を提供。
    -   **`generate_repo_list.py`**: 本プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成する一連の処理を orchestrate します。
    -   **`json_ld_template.json`**: 構造化データ（JSON-LD形式）のテンプレートファイル。SEOを強化するためにウェブページに埋め込むメタデータを定義。
    -   **`language_info.py`**: リポジトリの使用言語情報を処理し、表示に適した形式に変換する機能を提供。
    -   **`markdown_generator.py`**: 処理されたリポジトリデータとテンプレートを用いて、最終的なMarkdown形式のコンテンツを生成するモジュール。
    -   **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`など）からプロジェクト概要のテキストを抽出する機能。
    -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: 状態バッジ）を抽出するロジック。
    -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、後の処理に適したデータ構造に整形するモジュール。
    -   **`seo_template.yml`**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するYAMLファイル。
    -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計する機能を提供。
    -   **`strings.yml`**: アプリケーション内で表示されるテキストメッセージ、ラベル、説明文などを一元的に管理するYAMLファイル。多言語対応や文言変更を容易にします。
    -   **`template_processor.py`**: Markdownテンプレートファイル内のプレースホルダーを動的なデータで置き換えるなど、テンプレート処理を行うモジュール。
    -   **`url_utils.py`**: URLの構築、解析、検証など、URL操作に関連する共通ユーティリティ関数を提供。
-   **`test_project_overview.py`**: `project_overview_fetcher`モジュールに特化したテストスクリプト。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   **`conftest.py`**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイル。
    -   **`test_badge_generator_integration.py`**: `badge_generator`モジュールの統合テスト。
    -   **`test_check_large_files.py`**: `.github_automation/check_large_files`機能のテスト。
    -   **`test_config.py`**: 設定ファイル(`config.yml`など)の読み込みとパースに関するテスト。
    -   **`test_date_formatter.py`**: `date_formatter`モジュールの機能テスト。
    -   **`test_environment.py`**: プロジェクト実行環境のセットアップや依存関係に関するテスト。
    -   **`test_integration.py`**: プロジェクトの主要コンポーネント間の連携を検証する統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator`モジュールの機能テスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの機能テスト。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールの機能テスト。
    -   **`test_repository_processor.py`**: `repository_processor`モジュールの機能テスト。

## 関数詳細説明
提供されたプロジェクト情報には、具体的な関数の名前、引数、戻り値、詳細な機能に関する記述が含まれていません。そのため、ハルシネーションを避けるため、個々の関数について詳細に説明することはできません。

しかしながら、各ファイルの役割から、以下のような主要な機能（関数として実装されていると推測されるもの）が提供されていると考えられます。
-   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、その情報を処理してMarkdown形式で出力するメインの実行フローを管理する関数群。
-   **`repository_processor.py`**: GitHub APIから取得した未加工のリポジトリデータを、アプリケーションが必要とする形式に変換し、整理する関数群。
-   **`markdown_generator.py`**: 処理されたリポジトリデータと事前に定義されたテンプレートを用いて、最終的なMarkdownコンテンツを構築・生成する関数群。
-   **`project_overview_fetcher.py`**: 指定されたリポジトリ内の特定のファイルから、プロジェクトの概要テキストを非同期的に取得・抽出する関数群。
-   **`config_manager.py`**: YAML形式の設定ファイル (`config.yml`, `strings.yml` など) を読み込み、設定値をアプリケーション全体で利用可能にする関数群。
-   **`badge_generator.py`**: 各リポジトリの属性（言語、ステータスなど）に基づいて、表示用のバッジ情報を生成または取得する関数群。

これらのモジュールは、それぞれのファイル名が示す役割に応じた関数を提供し、連携してリポジトリ一覧の自動生成を実現しています。具体的な利用方法やシグネチャについては、実際のソースコードを参照してください。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-29 07:21:05 JST
