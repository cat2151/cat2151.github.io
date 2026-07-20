Last updated: 2026-07-21

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・集約するシステムです。
- 取得した情報をもとにJekyll対応のMarkdownファイルを自動生成し、GitHub Pagesサイトに公開します。
- これにより、リポジトリ一覧のSEOを最適化し、検索エンジンやLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータとして利用され、生成されたMarkdownファイルをHTMLに変換します)
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - `pytest`: Pythonコードのテストフレームワークです。
    - `ruff`: Pythonコードのリンターおよびフォーマッターで、コード品質とスタイルの一貫性を保ちます。
    - `git`: バージョン管理システムです。
- テスト: `pytest` (Pythonコードのユニットテスト、結合テストに利用されます。)
- ビルドツール:
    - Pythonスクリプト: GitHub APIからデータを取得し、Markdown形式のファイルを生成するメインのビルドロジックです。
    - Jekyll (概念として): GitHub Pages上でMarkdownファイルをHTMLに変換し、Webサイトを構築する役割を担います。
- 言語機能:
    - Python: プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成などに使用されています。
- 自動化・CI/CD: (GitHub Pagesの自動デプロイはGitHubの内部機構に依存するため、明示的なツールは記載されていませんが、自動化されたプロセス上で動作します)
- 開発標準:
    - `ruff`: Pythonコードのスタイルガイドと静的解析を適用し、コード品質と可読性を維持します。
    - `.editorconfig`: 複数のエディタやIDE間でコードスタイルを統一するための設定ファイルです。

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
-   `.editorconfig`: 異なるエディタやIDEを使用しても、コードのインデントスタイルや文字コードなどのフォーマット設定を統一するための設定ファイルです。
-   `.github_automation/check_large_files/README.md`: 大容量ファイルチェック自動化機能の説明ドキュメントです。
-   `.github_automation/check_large_files/check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルで、チェック対象のファイルサイズやパスなどを定義します。
-   `.github_automation/check_large_files/scripts/check_large_files.py`: 指定されたリポジトリ内で規定サイズを超える大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリ（例: 一時ファイル、ビルド成果物、依存関係のディレクトリ）を指定します。
-   `LICENSE`: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイルです。
-   `README.md`: プロジェクトの全体概要、目的、主な機能、セットアップ方法、使い方、開発者向けのヒントなどを記述したメインドキュメントです。
-   `_config.yml`: Jekyllのサイト全体の設定ファイルです。GitHub Pagesサイトのタイトル、テーマ、プラグインなどの設定を含みます。
-   `assets/`: GitHub Pagesサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるウェブサイトのアイコン（ファビコン）画像ファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher`機能のデバッグや単体テスト実行のために使用されるPythonスクリプトです。
-   `generated-docs/`: 他のリポジトリから自動取得されたプロジェクト概要などのドキュメントが一時的、あるいは永続的に格納される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどの検索エンジンツールで、サイトの所有権を確認するために使用される検証ファイルです。
-   `index.md`: メインの実行スクリプトによって生成される、リポジトリ一覧のマークダウンファイルです。Jekyllによって処理され、GitHub Pagesのトップページとして表示されます。
-   `issue-notes/22.md`: プロジェクトの課題管理や特定のイシューに関するメモを記録するためのファイルです。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、アプリの名称、アイコン、表示設定などを定義し、ユーザーがホーム画面に追加できるようにします。
-   `pytest.ini`: `pytest`フレームワークの動作設定ファイルです。テストの検出パスや実行オプションなどを定義します。
-   `requirements-dev.txt`: 開発環境やテスト環境で必要となるPythonの依存ライブラリをリストアップしたファイルです。
-   `requirements.txt`: プロジェクトが本番環境で動作するために必要となるPythonの依存ライブラリをリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
-   `ruff.toml`: `ruff`リンター/フォーマッターの設定ファイルです。Pythonコードの静的解析ルールや自動修正の挙動を定義します。
-   `src/__init__.py`: `src`ディレクトリがPythonパッケージであることを示すファイルです。
-   `src/generate_repo_list/__init__.py`: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイルです。
-   `src/generate_repo_list/badge_generator.py`: リポジトリのステータスや技術スタックなどを視覚的に表現するバッジ（例: Markdown形式の画像リンク）を生成する機能を持つPythonスクリプトです。
-   `src/generate_repo_list/config.yml`: リポジトリ一覧生成システムの特定の機能（例: プロジェクト概要取得の有効/無効、対象ファイルパス）に関する設定を定義するファイルです。
-   `src/generate_repo_list/config_manager.py`: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で設定値を管理するためのPythonスクリプトです。
-   `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を特定の形式（例: "YYYY年MM月DD日"）に整形するユーティリティ関数を提供するPythonスクリプトです。
-   `src/generate_repo_list/generate_repo_list.py`: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する一連の処理を実行します。
-   `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレートです。
-   `src/generate_repo_list/language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理・分析するためのPythonスクリプトです。
-   `src/generate_repo_list/markdown_generator.py`: 取得したリポジトリ情報に基づいて、リポジトリ一覧や各リポジトリの詳細説明をMarkdown形式で記述する機能を担当するPythonスクリプトです。
-   `src/generate_repo_list/project_overview_fetcher.py`: 他のリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で取得する機能を持つPythonスクリプトです。
-   `src/generate_repo_list/readme_badge_extractor.py`: READMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出するためのPythonスクリプトです。
-   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、それを内部で扱いやすい形式に整形・加工する役割を持つPythonスクリプトです。
-   `src/generate_repo_list/seo_template.yml`: サイトのSEO（検索エンジン最適化）関連のメタデータやキーワードを定義するためのテンプレートファイルです。
-   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または抽出するためのPythonスクリプトです。
-   `src/generate_repo_list/strings.yml`: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を一元的に管理するための設定ファイルです。多言語対応や文言の変更が容易になります。
-   `src/generate_repo_list/template_processor.py`: Jekyllなどのテンプレートエンジンで使用されるテンプレートファイルに動的なデータを差し込み、最終的な出力（例: Markdownファイル）を生成するためのPythonスクリプトです。
-   `src/generate_repo_list/url_utils.py`: URLの構築、解析、検証など、URLに関連する様々なユーティリティ機能を提供するPythonスクリプトです。
-   `test_project_overview.py`: `project_overview_fetcher`機能のユニットテストを記述したPythonスクリプトです。
-   `tests/conftest.py`: `pytest`フレームワークで共通のフィクスチャやヘルパー関数を定義するためのファイルです。
-   `tests/test_badge_generator_integration.py`: `badge_generator`モジュールの結合テストを記述したPythonスクリプトです。
-   `tests/test_check_large_files.py`: 大容量ファイルチェック機能のテストを記述したPythonスクリプトです。
-   `tests/test_config.py`: 設定ファイルの読み込みや管理機能のテストを記述したPythonスクリプトです。
-   `tests/test_date_formatter.py`: 日付整形ユーティリティのテストを記述したPythonスクリプトです。
-   `tests/test_environment.py`: プロジェクトの実行環境や依存関係の整合性を確認するためのテストを記述したPythonスクリプトです。
-   `tests/test_integration.py`: プロジェクトの主要なコンポーネントが連携して正しく動作するかを確認する統合テストを記述したPythonスクリプトです。
-   `tests/test_markdown_generator.py`: Markdown生成機能のテストを記述したPythonスクリプトです。
-   `tests/test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを記述したPythonスクリプトです。
-   `tests/test_readme_badge_extractor.py`: READMEからバッジ情報を抽出する機能のテストを記述したPythonスクリプトです。
-   `tests/test_repository_processor.py`: リポジトリ情報処理機能のテストを記述したPythonスクリプトです。

## 関数詳細説明
このプロジェクトは複数のPythonスクリプトで構成されており、各ファイルが特定の役割を担う関数群を提供しています。以下に主要な機能とそれを担う関数について説明します。具体的な引数や戻り値の型はコードベースに依存しますが、ここではその役割に焦点を当てます。

-   **`generate_repo_list.py` (メインスクリプト)**:
    -   **役割**: プロジェクト全体のオーケストレーションを担う中心的な関数（通常は`main()`関数として実装）。コマンドライン引数を解析し、GitHub APIからのリポジトリ情報取得、各種データの処理、そして最終的なMarkdownファイルの生成までの一連の流れを制御します。
-   **`badge_generator.py`**:
    -   **役割**: リポジトリの属性（例: 使用言語、最終更新日、アーカイブ状態など）に基づいて、視覚的なバッジ（Markdown形式の画像リンクなど）を生成する関数群。これにより、リポジトリ一覧に情報を簡潔に表示します。
-   **`config_manager.py`**:
    -   **役割**: YAMLやTOML形式の設定ファイル（例: `config.yml`, `secrets.toml`）を読み込み、アプリケーション全体で利用可能な設定オブジェクトを提供する関数群。設定値の取得や検証を行います。
-   **`date_formatter.py`**:
    -   **役割**: 日付オブジェクト（例: `datetime`オブジェクト）を受け取り、指定されたフォーマット（例: "YYYY年MM月DD日"）の人間が読める文字列に整形して返す関数群。
-   **`markdown_generator.py`**:
    -   **役割**: 処理されたリポジトリ情報やプロジェクト概要データを受け取り、リポジトリ一覧の各項目や全体構成、SEOメタデータなどを含むMarkdown形式のテキストを構築する関数群。
-   **`project_overview_fetcher.py`**:
    -   **役割**: 他のリポジトリの特定のファイルパス（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要をHTTPリクエストなどで取得し、整形して返す関数群。キャッシュ機能も含む場合があります。
-   **`repository_processor.py`**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を受け取り、必要な情報（名前、説明、URL、スター数など）を抽出し、内部で扱いやすい統一されたデータ構造に変換・整形する関数群。
-   **`statistics_calculator.py`**:
    -   **役割**: リポジトリの様々な統計情報（例: フォーク数、ウォッチ数、コミット数など）を計算したり、特定の期間内の活動状況を分析するための関数群。
-   **`template_processor.py`**:
    -   **役割**: テンプレートファイル（JekyllのLiquidテンプレートなど）と動的なデータを受け取り、データをテンプレートに差し込んで最終的な文字列（MarkdownまたはHTMLの一部）を生成する関数群。
-   **`url_utils.py`**:
    -   **役割**: URLの生成、結合、解析、エンコード/デコードなど、URLに関連する様々なユーティリティ操作を提供する関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-21 07:22:34 JST
