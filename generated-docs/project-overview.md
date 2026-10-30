Last updated: 2026-10-31

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してGitHub Pagesサイト用のMarkdownファイルを生成します。
- SEO最適化されたリポジトリ一覧ページと、各リポジトリの概要を自動取得し表示します。
- これにより、GitHub Pages経由での検索エンジンクロールを促進し、LLMによるリポジトリ参照の精度向上を目指します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyll)**: 生成されたMarkdownファイルをホストし、ウェブサイトとして公開するために使用されます。**Markdown**: 生成されるリポジトリ一覧のコンテンツ形式として使用されます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: **Git**: バージョン管理システムとしてコードの変更履歴を管理します。**GitHub**: プロジェクトのリポジトリホスティング、API提供元として使用されます。**secrets.toml**: GitHubトークンなどの機密情報をローカルで安全に管理するために使用されます。
- テスト: **pytest**: Pythonアプリケーションのテストフレームワークとして、ユニットテストおよび結合テストを実行するために使用されます。
- ビルドツール: **Python**: リポジトリ情報の取得、Markdownファイルの生成といった主要な処理を実行するためのスクリプト言語および実行環境です。
- 言語機能: **Python (requests, argparse, pyyaml, toml)**: GitHub APIとの連携、コマンドライン引数の解析、YAML/TOML形式の設定ファイル読み込みなどに使用されるPythonのライブラリ群です。
- 自動化・CI/CD: **Pythonスクリプト**: GitHub APIを介してリポジトリ情報を自動で取得し、指定された形式のMarkdownファイルを自動生成するプロセス自体が自動化の中心です。
- 開発標準: **ruff**: Pythonコードの整形とリンティングを自動化し、コード品質と一貫性を維持するために使用されます。**.editorconfig**: 異なるエディタやIDE間でコードスタイルの一貫性を保つための設定ファイルです。

## ファイル階層ツリー
```
📄 .editorconfig
📁 .github_automation/
  📁 check_large_files/
    📖 README.md
    📄 check-large_files.toml
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
-   `.editorconfig`: さまざまなエディタやIDE間でコードのフォーマットスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   `.github_automation/`: GitHubに関連する自動化スクリプトや設定を格納するディレクトリです。
    -   `check_large_files/`: 大容量ファイルをチェックするためのスクリプト群です。
        -   `README.md`: `check_large_files`スクリプトの目的と使用方法を説明するドキュメントです。
        -   `check-large-files.toml`: `check_large_files.py`スクリプトの設定を定義するTOML形式のファイルです。
        -   `scripts/check_large_files.py`: 指定された設定に基づき、リポジトリ内の大容量ファイルを検出するPythonスクリプトです。
-   `.gitignore`: Gitでバージョン管理しないファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクトの概要、セットアップ手順、使用方法、主な機能などを記述したメインのドキュメントファイルです。
-   `_config.yml`: Jekyllサイトのグローバル設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが含まれます。
-   `assets/`: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ブラウザのタブなどに表示されるアイコン）の異なるサイズを提供します。
-   `debug_project_overview.py`: `project_overview_fetcher`機能のデバッグや単体テストを行うための補助スクリプトです。
-   `generated-docs/`: 他のリポジトリから自動的に取得・生成されたドキュメント（例: 各リポジトリの`project-overview.md`）を格納するためのプレースホルダーディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権を確認するためにGoogleから提供される認証ファイルです。
-   `index.md`: `generate_repo_list.py`スクリプトによって生成されるGitHubリポジトリ一覧のメイン出力ファイルです。Jekyllによってウェブページとして表示されます。
-   `issue-notes/`: 課題や検討事項に関するメモを格納するディレクトリです。
    -   `22.md`: 特定の課題（Issue #22）に関するメモや詳細を記述したMarkdownファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の情報を記述するファイルです。ホーム画面に追加される際のアイコンや表示設定などを定義します。
-   `pytest.ini`: pytestテストフレームワークの設定ファイルです。テストの実行方法やレポート形式などを指定します。
-   `requirements-dev.txt`: 開発環境でのみ必要となるPythonパッケージとそのバージョンを定義するファイルです。
-   `requirements.txt`: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを定義するファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいはしてはならないかを指示するファイルです。
-   `ruff.toml`: PythonコードのリンティングおよびフォーマットツールであるRuffの設定ファイルです。コードスタイルやルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成システムのメインロジックが格納されるパッケージです。
        -   `__init__.py`: Pythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（画像）を生成するロジックを管理します。
        -   `config.yml`: リポジトリ情報取得機能（例：プロジェクト概要取得機能）などのシステム固有の技術的パラメータを設定するYAMLファイルです。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するユーティリティモジュールです。
        -   `date_formatter.py`: 日付や時刻の情報を特定の形式に整形するための機能を提供します。
        -   `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイル (`index.md`) を生成するメインの実行スクリプトです。
        -   `json_ld_template.json`: 検索エンジン最適化 (SEO) のためのJSON-LDデータ構造のテンプレートを定義します。
        -   `language_info.py`: 各リポジトリで使用されているプログラミング言語に関する情報を処理・分析する機能を提供します。
        -   `markdown_generator.py`: 取得したリポジトリ情報から、GitHub Pages用にSEO最適化されたMarkdownコンテンツを生成するロジックを実装します。
        -   `project_overview_fetcher.py`: 各リポジトリ内の特定のファイル (`generated-docs/project-overview.md`など) からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
        -   `readme_badge_extractor.py`: 各リポジトリのREADMEファイルから、既存のバッジ情報を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIを介してリポジトリ情報を取得し、アクティブ、アーカイブ、フォークなどのカテゴリに分類する主要な処理ロジックを含みます。
        -   `seo_template.yml`: Markdown生成時に適用されるSEO関連のメタデータや構造に関するテンプレート設定を定義します。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算・集計する機能を提供します。
        -   `strings.yml`: UIの表示メッセージ、Markdown内の固定文言、ラベルなどを一元的に管理するYAMLファイルです。
        -   `template_processor.py`: Markdown生成の際に、特定のテンプレート構造にデータを埋め込むための処理を行います。
        -   `url_utils.py`: URLの生成、解析、検証など、URL関連のユーティリティ機能を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`機能のユニットテストおよび統合テストを記述したファイルです。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリです。
    -   `conftest.py`: pytestのフィクスチャ（テスト実行前に準備されるデータやリソース）を定義するファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの結合テストを記述します。
    -   `test_check_large_files.py`: `.github_automation/check_large_files`スクリプトのテストを記述します。
    -   `test_config.py`: `config_manager`モジュールおよび設定ファイルの読み込みに関するテストを記述します。
    -   `test_date_formatter.py`: `date_formatter`モジュールのテストを記述します。
    -   `test_environment.py`: 環境変数や外部依存関係のテストを記述します。
    -   `test_integration.py`: プロジェクト全体の主要な処理フローの結合テストを記述します。
    -   `test_markdown_generator.py`: `markdown_generator`モジュールのテストを記述します。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールのテストを記述します。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールのテストを記述します。
    -   `test_repository_processor.py`: `repository_processor`モジュールのテストを記述します。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数に関する詳細情報（役割、引数、戻り値、機能）が含まれていないため、これらの項目を具体的に説明することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-31 07:07:32 JST
