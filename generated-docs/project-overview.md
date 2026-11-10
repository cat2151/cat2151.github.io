Last updated: 2026-11-11

# Project Overview

## プロジェクト概要
- GitHub API を活用し、GitHub Pages サイト用のリポジトリ一覧を自動生成するシステムです。
- 検索エンジンに最適化されたマークダウンコンテンツを生成し、GitHubユーザーページの問題を解消します。
- 各リポジトリの概要表示、バッジ、分類機能などを備え、開発プロジェクトの情報公開を強化します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pages で静的サイトを構築するための静的サイトジェネレータ。生成されたMarkdownファイルをHTMLとして公開する基盤です。
    - **Markdown**: リポジトリ情報やプロジェクト概要などを記述し、JekyllによってHTMLに変換される軽量マークアップ言語です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **pytest**: Pythonアプリケーションのテストフレームワーク。プロジェクトの各モジュールの機能テストや統合テストに利用されます。
    - **ruff**: Pythonコードのリンターおよびフォーマッター。コードの品質維持とスタイル統一を自動化します。
    - **GitHub API**: GitHubリポジトリの情報をプログラムから取得するためのインターフェース。このプロジェクトの主要なデータソースです。
- テスト:
    - **pytest**: Pythonコードの単体テスト、統合テストの実行に用いられます。
- ビルドツール:
    - **Python**: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得、Markdown生成、ファイル処理などの自動化スクリプトを実行します。
    - **Jekyll**: 静的サイトのビルド（MarkdownからHTMLへの変換）を行います。
- 言語機能:
    - **Python**: メインのプログラミング言語。
    - **YAML**: `config.yml`, `strings.yml`, `seo_template.yml` などの設定ファイルや文言管理に使用されます。
    - **TOML**: `pytest.ini`, `ruff.toml`, `check-large-files.toml`, `secrets.toml` などの設定ファイルやシークレット管理に使用されます。
    - **JSON**: `json_ld_template.json`, `manifest.json` などのデータフォーマットに使用されます。
- 自動化・CI/CD:
    - **GitHub Actions (関連)**: 直接的なCI/CDは含まれませんが、`.github_automation` ディレクトリの存在から、将来的または関連プロジェクトでのGitHub Actionsによる自動化が意識されています。
- 開発標準:
    - **ruff**: `ruff.toml` にてPythonコードのスタイルガイドやリンティングルールが定義され、コード品質の均一化に貢献します。
    - **.editorconfig**: 複数の開発者やエディタ間でのコードスタイルの一貫性を保つための設定ファイルです。

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
-   `.editorconfig`: 異なる開発環境間でのコードスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    -   `check_large_files/`: 特定のリポジトリ内の大容量ファイルをチェックするサブプロジェクトです。
        -   `README.md`: `check_large_files` 機能の目的や使用方法を説明するドキュメントです。
        -   `check-large_files.toml`: `check_large_files` スクリプトの動作設定を定義するファイルです。
        -   `scripts/check_large_files.py`: 大容量ファイルを検出・報告するためのPythonスクリプトです。
-   `.gitignore`: Gitによってバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: このプロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
-   `README.md`: プロジェクト全体の概要、セットアップ手順、基本的な使用方法、機能などについて説明する主要なドキュメントです。
-   `_config.yml`: Jekyllサイト全体のグローバル設定を定義するファイルです。サイトのタイトル、テーマ、プラグイン設定などが含まれます。
-   `assets/`: ウェブサイトで使用される静的リソース（ファビコン、画像など）を格納するディレクトリです。
    -   `favicon-*.png`: 各種デバイスやブラウザで使用されるサイトのアイコン（ファビコン）画像ファイルです。
-   `debug_project_overview.py`: `project_overview_fetcher` モジュールのデバッグやテスト実行のために使用されるスクリプトです。
-   `generated-docs/`: 他のリポジトリから自動取得された `project-overview.md` などのドキュメントが一時的または最終的に格納される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサービスでサイトの所有権を確認するために使用されるHTMLファイルです。
-   `index.md`: `generate_repo_list.py` スクリプトによって生成される、GitHubリポジトリ一覧を記述したメインのMarkdownファイルです。Jekyllによってウェブページとして公開されます。
-   `issue-notes/22.md`: プロジェクトの特定の課題や改善点に関するメモを記述したファイルです。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの情報を提供します。
-   `pytest.ini`: `pytest` テストフレームワークの動作に関する設定（テスト検出パス、プラグイン、マーカーなど）を定義するファイルです。
-   `requirements-dev.txt`: 開発およびテスト時に必要なPythonパッケージの依存関係をリストアップしたファイルです。
-   `requirements.txt`: プロジェクトの本番運用時に必要なPythonパッケージの依存関係をリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイト内のどのページをクロールすべきか、どのページを避けるべきかを指示するファイルです。
-   `ruff.toml`: Pythonコードのリンターおよびフォーマッターである`ruff`の設定ファイルです。コードスタイルや静的解析のルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成機能の主要なモジュール群を格納するパッケージです。
        -   `__init__.py`: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
        -   `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを扱います。
        -   `config.yml`: `generate_repo_list.py` スクリプトの動作パラメータや、`project_overview` 機能の設定などを定義するファイルです。
        -   `config_manager.py`: `config.yml` などの設定ファイルを読み込み、設定値にアクセスするためのインターフェースを提供するモジュールです。
        -   `date_formatter.py`: 日付や時刻のフォーマット、変換に関するユーティリティ関数を提供するモジュールです。
        -   `generate_repo_list.py`: プロジェクトのメインエントリーポイントとなるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
        -   `json_ld_template.json`: 構造化データ（JSON-LD形式）のテンプレートファイルで、SEO最適化のためにリポジトリ情報に付加されます。
        -   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つデータを提供するモジュールです。
        -   `markdown_generator.py`: リポジトリデータに基づいて、SEO最適化されたMarkdown形式のコンテンツを生成するロジックをカプセル化したモジュールです。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、ライセンス）を抽出するロジックを扱います。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を整形・加工して、後のMarkdown生成プロセスで利用できるようにするモジュールです。
        -   `seo_template.yml`: SEO関連のメタ情報やテンプレート設定を定義するファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算・集計するロジックを扱います。
        -   `strings.yml`: UIの表示メッセージ、ラベル、その他のテキストを多言語対応や管理しやすくするために集約したファイルです。
        -   `template_processor.py`: Jekyllテンプレートやその他のマークアップテンプレートを処理し、動的なコンテンツを埋め込むための汎用的なロジックを提供します。
        -   `url_utils.py`: URLの構築、解析、検証など、URLに関連するユーティリティ関数を提供するモジュールです。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールの機能に関する具体的なテストケースを記述したスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest` のフィクスチャやヘルパー関数など、テスト実行時に共通で利用される設定を定義するファイルです。
    -   `test_badge_generator_integration.py`: `badge_generator` モジュールの統合テストを行うスクリプトです。
    -   `test_check_large_files.py`: `check_large_files` 機能のテストを行うスクリプトです。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテストを行うスクリプトです。
    -   `test_date_formatter.py`: `date_formatter` モジュールのテストを行うスクリプトです。
    -   `test_environment.py`: プロジェクトの実行環境に関するテストを行うスクリプトです。
    -   `test_integration.py`: 主要なモジュール間の連携を含む、より広範囲な統合テストを行うスクリプトです。
    -   `test_markdown_generator.py`: `markdown_generator` モジュールのテストを行うスクリプトです。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher` モジュールのテストを行うスクリプトです。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor` モジュールのテストを行うスクリプトです。
    -   `test_repository_processor.py`: `repository_processor` モジュールのテストを行うスクリプトです。

## 関数詳細説明
提供された情報では、各ファイルの具体的な関数名、引数、戻り値が詳細に記述されていません。ハルシネーションを避けるため、ここでは各モジュールが提供するであろう主要な機能について抽象的に説明します。

-   **`src/generate_repo_list/badge_generator.py`**:
    -   役割: リポジトリの技術スタック、ステータス、ライセンスなどの情報を元に、適切なバッジ（例: Markdown形式の画像リンク）を生成する機能を提供します。
    -   機能: バッジの種類に応じたSVG/PNG画像のURL決定、Markdown形式での出力。
-   **`src/generate_repo_list/config_manager.py`**:
    -   役割: 設定ファイル (`config.yml` など) を読み込み、設定値に安全かつ一貫した方法でアクセスするための機能を提供します。
    -   機能: YAMLファイルのパース、設定値の取得メソッド、デフォルト値の適用。
-   **`src/generate_repo_list/date_formatter.py`**:
    -   役割: 日付や時刻データを指定された形式でフォーマットする機能を提供します。
    -   機能: `datetime` オブジェクトから特定の文字列形式への変換、Jekyllが解釈できる形式への調整。
-   **`src/generate_repo_list/generate_repo_list.py`**:
    -   役割: プロジェクト全体のメインスクリプトであり、GitHub APIからのデータ取得からMarkdownファイルの生成までの一連の処理を統括します。
    -   機能: コマンドライン引数の解析、GitHub API呼び出し、リポジトリデータの処理、Markdownコンテンツの結合とファイル出力。
-   **`src/generate_repo_list/language_info.py`**:
    -   役割: リポジトリのプログラミング言語に関する統計情報（使用割合など）を処理し、表示に適した形式に変換する機能を提供します。
    -   機能: 言語データの集計、視覚化のためのデータ準備。
-   **`src/generate_repo_list/markdown_generator.py`**:
    -   役割: 処理されたリポジトリデータを受け取り、SEOを意識した構造化されたMarkdownコンテンツを生成する機能を提供します。
    -   機能: Markdownヘッダー、リスト、リンク、埋め込みコードなどの生成。
-   **`src/generate_repo_list/project_overview_fetcher.py`**:
    -   役割: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`など）から、プロジェクトの概要説明を自動で抽出する機能を提供します。
    -   機能: リモートファイルの取得（HTTPリクエスト）、Markdownコンテンツのパース、指定セクションからのテキスト抽出、キャッシュ管理。
-   **`src/generate_repo_list/readme_badge_extractor.py`**:
    -   役割: リポジトリの `README.md` ファイルの内容を解析し、含まれるバッジ情報を抽出する機能を提供します。
    -   機能: Markdownテキストの解析、バッジパターン（例: `![alt](url)`）の識別と抽出。
-   **`src/generate_repo_list/repository_processor.py`**:
    -   役割: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、アプリケーション内で扱いやすいデータ構造に整形・変換する機能を提供します。
    -   機能: 必須フィールドの抽出、データ型変換、アクティブ/アーカイブ/フォークの分類。
-   **`src/generate_repo_list/statistics_calculator.py`**:
    -   役割: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する機能を提供します。
    -   機能: 統計データの集計ロジック、合計値や平均値の算出。
-   **`src/generate_repo_list/template_processor.py`**:
    -   役割: YAMLやJSONなどのテンプレートファイルを使用して、動的にコンテンツを生成する汎用的な機能を提供します。
    -   機能: テンプレートの読み込み、プレースホルダー置換、条件付きコンテンツ生成。
-   **`src/generate_repo_list/url_utils.py`**:
    -   役割: URLの構築、解析、検証など、URLに関連するユーティリティ機能を提供します。
    -   機能: URLエンコード/デコード、絶対URL/相対URLの解決。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-11 07:08:02 JST
