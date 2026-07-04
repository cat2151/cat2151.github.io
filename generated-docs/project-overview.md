Last updated: 2026-07-05

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のリポジトリ情報を自動的に取得するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けに最適化されたMarkdown形式のリポジトリ一覧を生成します。
- これにより、リポジトリの検索エンジンからの参照性を高め、LLMによる情報取得の精度向上を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として利用され、生成されたMarkdownファイルを美しいWebサイトとして表示), **Markdown** (リポジトリ一覧のコンテンツ形式として生成され、JekyllによってHTMLに変換されます)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (プロジェクトの主要なスクリプト言語として、GitHub APIからの情報取得、データの加工、Markdown生成を行います), **GitHub API** (リポジトリ情報、README、プロジェクト概要などを取得するための主要なデータソースです)
- テスト: **pytest** (Pythonコードのテストフレームワークとして、プロジェクトの各機能が意図通りに動作するかを検証します)
- ビルドツール: 該当するビルドツールは直接使用されていませんが、Pythonスクリプトがコンテンツの生成（ビルド）を行います。
- 言語機能: **Python** (データ処理、API通信、ファイル操作など、システム全体のロジックを実装するために使用されています)
- 自動化・CI/CD: 本プロジェクトはローカル開発を重視しており、継続的インテグレーション/デリバリーのパイプラインは現状設けられていません。
- 開発標準: **ruff** (Pythonコードのリンター兼フォーマッターとして、コードの品質と一貫性を保ちます)

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
-   **`.editorconfig`**: 異なる開発環境でコードスタイルの一貫性を保つための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    -   `check_large_files/README.md`: 大容量ファイルチェック機能に関する説明です。
    -   `check-large-files.toml`: 大容量ファイルチェック機能の設定ファイルです。
    -   `scripts/check_large_files.py`: 大容量ファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理しないファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクト全体の概要、セットアップ手順、使用方法、開発者向けヒントなどを記載したメインドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、サイトの挙動や外観に影響を与えます。
-   **`assets/`**: Jekyllサイトで使用されるfaviconなどの静的アセットを格納するディレクトリです。
-   **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグを目的としたスクリプトです。
-   **`generated-docs/`**: 各リポジトリのプロジェクト概要ファイル（`project-overview.md`）が格納されることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるファイルです。
-   **`index.md`**: メインの出力ファイルであり、このスクリプトによって生成されたリポジトリ一覧がMarkdown形式で書き込まれ、GitHub Pagesで公開されます。
-   **`issue-notes/22.md`**: プロジェクトのIssueに関するメモや詳細情報を格納するファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてウェブサイトを設定するためのマニフェストファイルです。
-   **`pytest.ini`**: Pythonのテストフレームワークである `pytest` の設定ファイルです。
-   **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージの依存関係リストです。
-   **`requirements.txt`**: プロジェクトの実行に最低限必要なPythonパッケージの依存関係リストです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツール `ruff` の設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    -   `generate_repo_list/badge_generator.py`: リポジトリの各種情報（スター数、言語など）を基にバッジ画像を生成するロジックを扱います。
    -   `generate_repo_list/config.yml`: リポジトリ一覧生成に関する具体的な設定値（例：プロジェクト概要取得機能の有効/無効、リトライ回数など）を定義します。
    -   `generate_repo_list/config_manager.py`: `config.yml` や `strings.yml` など、プロジェクトで使用される設定ファイルを読み込み、管理する役割を担います。
    -   `generate_repo_list/date_formatter.py`: GitHub APIから取得した日付データを、人間が読みやすい形式に整形するためのユーティリティ関数を提供します。
    -   `generate_repo_list/generate_repo_list.py`: プロジェクトのメインエントリスクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdownを生成します。
    -   `generate_repo_list/json_ld_template.json`: 検索エンジン最適化（SEO）のためのJSON-LD形式のメタデータテンプレートを定義します。
    -   `generate_repo_list/language_info.py`: リポジトリで使用されているプログラミング言語の統計情報（割合など）を処理・整形する機能を提供します。
    -   `generate_repo_list/markdown_generator.py`: 処理済みのリポジトリ情報から、最終的なMarkdownコンテンツを構築するロジックをカプセル化しています。
    -   `generate_repo_list/project_overview_fetcher.py`: 各リポジトリ内の `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を抽出する機能を担当します。
    -   `generate_repo_list/readme_badge_extractor.py`: リポジトリの `README.md` ファイルから、特定のバッジ情報（例えばビルドステータスなど）を抽出する機能を提供します。
    -   `generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
    -   `generate_repo_list/seo_template.yml`: サイト全体のSEO設定やメタデータに関するテンプレートを定義します。
    -   `generate_repo_list/statistics_calculator.py`: リポジトリのスター数やフォーク数などの各種統計情報を計算・集計する機能を提供します。
    -   `generate_repo_list/strings.yml`: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのファイルです。
    -   `generate_repo_list/template_processor.py`: JekyllのLiquidテンプレートやその他のMarkdownテンプレートを処理し、動的にコンテンツを生成する機能を提供します。
    -   `generate_repo_list/url_utils.py`: URLのパース、構築、検証など、URLに関連する様々なユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストを記述したスクリプトです。
-   **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest`で共通して使用されるフィクスチャやヘルパー関数を定義します。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの統合テストを行います。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストを行います。
    -   `test_config.py`: 設定ファイルの読み込みと解析に関するテストを行います。
    -   `test_date_formatter.py`: 日付整形ユーティリティのテストを行います。
    -   `test_environment.py`: 実行環境のセットアップや依存関係に関するテストを行います。
    -   `test_integration.py`: システム全体の主要なフローに関する統合テストを行います。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテストを行います。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを行います。
    -   `test_readme_badge_extractor.py`: `README`からのバッジ抽出機能のテストを行います。
    -   `test_repository_processor.py`: リポジトリデータ処理ロジックのテストを行います。

## 関数詳細説明
提供された情報では個々の関数の詳細なシグネチャ（引数、戻り値の型など）は不明ですが、ファイル名とプロジェクトの機能から推測される主要な関数の役割を以下に説明します。

-   **`generate_repo_list.py`内の主要関数 (`main`など)**
    -   **役割**: プロジェクトのエントリポイントとして機能し、コマンドライン引数を解析します。GitHub APIからのリポジトリ情報取得、データ処理、Markdownコンテンツの最終的な生成といった、システム全体のワークフローをオーケストレートします。
    -   **引数**: コマンドライン引数 (`--username`, `--output`, `--limit` など) を受け取ります。
    -   **戻り値**: 通常、スクリプトの実行成功を示すステータスコード（例: 0）を返します。
    -   **機能**: プロジェクトの主要な処理フロー全体を管理・実行します。

-   **`project_overview_fetcher.py`内の主要関数 (`fetch_overview`など)**
    -   **役割**: 指定されたリポジトリのURLと設定情報に基づき、そのリポジトリ内の`generated-docs/project-overview.md`ファイルから3行のプロジェクト概要を抽出します。API呼び出しのリトライやキャッシュ機能を持つ可能性があります。
    -   **引数**: リポジトリのURL、設定オブジェクト（`config`）などを受け取ります。
    -   **戻り値**: 抽出されたプロジェクト概要の文字列リスト、または取得失敗を示す値を返します。
    -   **機能**: 各リポジトリの簡潔な説明文を取得し、一覧表示に利用可能にします。

-   **`repository_processor.py`内の主要関数 (`process_repository`など)**
    -   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、それをMarkdown生成に適した形式に加工・整形します。言語情報、スター数、最終更新日などのメタデータ抽出や、`project_overview_fetcher`との連携も行います。
    -   **引数**: 生のリポジトリデータ（辞書形式など）、設定オブジェクトを受け取ります。
    -   **戻り値**: 整形され、表示に必要な情報が追加されたリポジトリデータ（辞書形式など）を返します。
    -   **機能**: GitHub APIからの多様なリポジトリ情報を、統一された使いやすい形式に変換します。

-   **`markdown_generator.py`内の主要関数 (`generate_markdown`など)**
    -   **役割**: 処理済みのリポジトリ情報、表示用文字列（`strings.yml`から）、SEOメタデータテンプレートを受け取り、最終的なMarkdownコンテンツを構築します。Jekyllが処理できる形式で、リポジトリ一覧、各リポジトリの詳細、SEOメタデータを含みます。
    -   **引数**: 処理済みのリポジトリデータリスト、表示用文字列データ、SEOデータなどを受け取ります。
    -   **戻り値**: 生成されたMarkdownコンテンツの文字列を返します。
    -   **機能**: 加工されたデータとテンプレートを組み合わせて、最終的なウェブページコンテンツを生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-05 07:21:13 JST
