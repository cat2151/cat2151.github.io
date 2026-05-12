Last updated: 2026-05-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身の全リポジトリ情報を自動で取得・整形するシステムです。
- 取得した情報からJekyllベースのGitHub Pagesサイト向けにSEO最適化されたMarkdownファイルを生成します。
- ユーザーページのリポジトリが検索エンジンにクロールされにくい課題を解決し、リポジトリの発見性とLLMからの参照性を向上させます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレータとして使用され、生成されたMarkdownファイルをHTMLサイトに変換します。
    - **Markdown**: リポジトリ一覧や各リポジトリの概要ページを記述するための軽量マークアップ言語で、本プロジェクトで自動生成されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - **GitHub API**: リポジトリの公開情報（名前、説明、言語、スター数など）をプログラムから取得するために使用されます。
    - **GitHub Secrets**: ローカルでのGitHubトークン管理に推奨されるメカニズムです。
- テスト:
    - **pytest**: Pythonアプリケーションのテストフレームワーク。コードの品質と信頼性を確保するための自動テストに使用されます。
- ビルドツール:
    - **Jekyll**: GitHub Pagesのビルドエンジンとして機能し、生成されたMarkdownファイルを最終的なウェブサイトに変換します。
- 言語機能:
    - **Python**: プロジェクトの主要な開発言語であり、GitHub APIからのデータ取得、処理、Markdown生成のロジックが実装されています。
- 自動化・CI/CD:
    - **GitHub Actions**: プロジェクト内で大規模ファイルをチェックするスクリプト（`check_large_files`）の自動実行など、特定の自動化タスクに使用される可能性があります。ただし、CI/CDはローカル開発重視のため、活発には使用されていません。
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックとフォーマットを自動化するためのツールで、コードの一貫性と品質を保ちます。
    - **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイルです。

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
- **`.editorconfig`**: 複数の開発者が異なるエディタを使用する際に、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsや関連する自動化スクリプトを格納するためのディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files`スクリプトの目的や使用方法を説明するドキュメントです。
    - **`check-large-files.toml`**: `check_large_files.py`スクリプトが参照する設定ファイルで、チェック対象のファイルサイズ閾値などを定義します。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大規模なファイルを検出し、管理に役立てるためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使い方などが記載されている、プロジェクトの玄関となるドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: GitHub Pagesサイトで利用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各サイズに対応する画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` の機能をデバッグしたり、単体で動作確認したりするためのスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した概要などのドキュメントが自動生成されて格納されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイトの所有権を確認するために使用されることが多いファイルです。
- **`index.md`**: GitHub Pagesサイトのメインページ（トップページ）のMarkdownファイルです。このファイルに生成されたリポジトリ一覧が出力されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22など）に関するメモや詳細情報が記述されているドキュメントです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブサイトをデスクトップやモバイルのアプリケーションのように見せるための情報（アイコン、表示モードなど）を含みます。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルで、テストの挙動やオプションを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの本番稼働時に必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonリンター/フォーマッターである`ruff`の設定ファイルで、コードの品質基準や自動修正ルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`__init__.py`**: Pythonパッケージの初期化ファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`パッケージの初期化ファイルです。
        - **`badge_generator.py`**: リポジトリの言語やステータスなどを示すバッジ（アイコン）を生成するロジックを実装しています。
        - **`config.yml`**: プロジェクト概要の取得設定やAPIに関する技術的なパラメータを定義する設定ファイルです。
        - **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`やシークレットファイル）の読み込みと管理を行うモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整します。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ（JSON-LD形式）のテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するモジュールです。
        - **`markdown_generator.py`**: 処理されたリポジトリデータから、最終的なMarkdown形式のコンテンツを生成する役割を担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出するモジュールです。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出し、再利用可能にするモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、プロジェクトで利用しやすい形式に加工・整形するモジュールです。
        - **`seo_template.yml`**: SEO関連のメタデータや構造化データを生成するためのテンプレート設定ファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算し、表示用に提供するモジュールです。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元的に管理するための設定ファイルです。
        - **`template_processor.py`**: テンプレートエンジンを利用して、Markdownコンテンツの最終的なレンダリングを行うモジュールです。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトをまとめたディレクトリです。
    - **`conftest.py`**: `pytest`の共通フィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の統合テストで、他のモジュールとの連携を含めた動作を検証します。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトが意図通りに機能するかを検証するテストです。
    - **`test_config.py`**: `config_manager.py`など、設定ファイルの読み込みや管理機能が正しく動作するかを検証するテストです。
    - **`test_date_formatter.py`**: `date_formatter.py`の関数が正しく日付をフォーマットするかを検証するテストです。
    - **`test_environment.py`**: プロジェクトが動作する環境設定や依存関係が適切であるかを確認するテストです。
    - **`test_integration.py`**: システム全体または主要なコンポーネント間の連携を検証する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`が正しくMarkdownコンテンツを生成するかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`の機能が正確に動作するかを検証するテストです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`がREADMEからバッジ情報を正しく抽出できるかを検証するテストです。
    - **`test_repository_processor.py`**: `repository_processor.py`がGitHub APIから取得したデータを適切に処理・整形できるかを検証するテストです。

## 関数詳細説明
- **`generate_repo_list.py`**:
    - **`main()`**: プロジェクトの実行エントリポイント。GitHub APIからのリポジトリ取得、データ処理、Markdown生成といった主要な処理フローを統括します。
- **`badge_generator.py`**:
    - **`generate_badge(repo_data: dict) -> str`**: 指定されたリポジトリデータに基づいて、そのリポジトリに関連するバッジ（例: 言語、スター数、ステータスなど）のMarkdown文字列を生成します。
- **`config_manager.py`**:
    - **`load_config(config_path: str) -> dict`**: 指定されたパスからYAMLまたはTOML形式の設定ファイルを読み込み、辞書形式で設定データを返します。
- **`date_formatter.py`**:
    - **`format_date(datetime_obj: datetime, format_str: str) -> str`**: `datetime`オブジェクトを指定されたフォーマット文字列（例: `"%Y-%m-%d"`）に従って整形し、文字列として返します。
- **`markdown_generator.py`**:
    - **`generate_markdown(repo_list: list) -> str`**: 処理済みのリポジトリデータのリストを受け取り、それらを基にGitHub Pages用のリポジトリ一覧のMarkdownコンテンツ全体を生成します。
- **`project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_url: str, config: dict) -> str`**: 指定されたリポジトリのURLから、`config`で指定されたパスにあるプロジェクト概要ファイル（例: `generated-docs/project-overview.md`）を取得し、その中から特定のセクションの概要テキストを抽出して返します。
- **`repository_processor.py`**:
    - **`process_repository(repo_raw_data: dict) -> dict`**: GitHub APIから直接取得した生のリポジトリデータ（辞書形式）を受け取り、プロジェクトのMarkdown生成に適した形式に加工・整形して返します。
- **`template_processor.py`**:
    - **`render_template(template_name: str, context: dict) -> str`**: 指定されたテンプレート名と、テンプレートに渡すコンテキストデータ（辞書形式）を使用して、最終的なテキスト（例: Markdown）をレンダリングして返します。

## 関数呼び出し階層ツリー
```
現状、この情報は提供されていません。

---
Generated at: 2026-05-13 07:30:14 JST
