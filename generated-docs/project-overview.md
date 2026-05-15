Last updated: 2026-05-16

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で収集します。
- GitHub Pagesサイト向けに、検索エンジン最適化されたリポジトリ一覧をMarkdown形式で生成します。
- これにより、プロジェクトの発見性を高め、大規模言語モデル（LLM）による参照精度を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesのベースとなる静的サイトジェネレータ)、Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: GitHub API (リポジトリ情報取得のためのインターフェース)
- テスト: pytest (Python製のテストフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ一覧のMarkdownファイルを生成)、Jekyll (GitHub Pages上でのMarkdownからHTMLへの変換)
- 言語機能: Python (主要なスクリプト言語)、YAML (設定ファイルの記述)、TOML (一部設定ファイルの記述)
- 自動化・CI/CD: Pythonスクリプトによるリポジトリ一覧の自動生成、GitHub Actions (`.github_automation`ディレクトリ内のスクリプトはCI/CDでの利用が想定されます)
- 開発標準: Ruff (Pythonコードのフォーマッター兼リンター)

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
-   **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   **.github_automation/**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
    -   **check_large_files/**: 大容量ファイル検出に関連するスクリプトと設定を格納。
        -   **README.md**: `check_large_files`機能に関する説明。
        -   **check-large-files.toml**: 大容量ファイルチェックの設定ファイル。
        -   **scripts/check_large_files.py**: 大容量ファイルを検知するためのPythonスクリプト。
-   **.gitignore**: Gitが追跡しないファイルやディレクトリを指定する設定ファイル。
-   **LICENSE**: プロジェクトのライセンス情報（MITライセンス）。
-   **README.md**: プロジェクトの概要、目的、使用方法、設定、ライセンスなどに関する主要なドキュメント。
-   **_config.yml**: Jekyllのサイト設定ファイル。GitHub Pagesのビルド動作を制御します。
-   **assets/**: サイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    -   **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: サイトのファビコン（アイコン）。
-   **debug_project_overview.py**: プロジェクト概要取得機能のデバッグに使用されるスクリプト。
-   **generated-docs/**: 各リポジトリから取得・生成されたドキュメントや概要ファイルが一時的に格納される可能性のあるディレクトリ。
-   **googled947dc864c270e07.html**: Google Search Consoleなどのサイト認証に使用されるHTMLファイル。
-   **index.md**: GitHub Pagesサイトのトップページとして、自動生成されたリポジトリ一覧が出力されるMarkdownファイル。
-   **issue-notes/**: 課題やノートを格納するディレクトリ。
    -   **22.md**: 特定の課題に関するノート。
-   **manifest.json**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイル。
-   **pytest.ini**: `pytest`テストフレームワークの共通設定ファイル。
-   **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリの依存関係を定義。
-   **requirements.txt**: プロジェクトの本番稼働に必要なPythonライブラリの依存関係を定義。
-   **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきかを指示するファイル。
-   **ruff.toml**: Pythonコードのスタイルチェックとフォーマットを行う`ruff`ツールの設定ファイル。
-   **src/**: プロジェクトのソースコードを格納するメインディレクトリ。
    -   **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    -   **generate_repo_list/**: リポジトリ一覧生成機能に関連するモジュールを格納するパッケージ。
        -   **__init__.py**: `generate_repo_list`がPythonパッケージであることを示すファイル。
        -   **badge_generator.py**: リポジトリのバッジ（例：言語、ステータス）を生成または処理するロジック。
        -   **config.yml**: リポジトリ一覧生成スクリプトの動作設定（例：プロジェクト概要取得のON/OFF）。
        -   **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するモジュール。
        -   **date_formatter.py**: 日付の表示形式を整形するユーティリティ。
        -   **generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownを生成します。
        -   **json_ld_template.json**: SEO最適化のためのJSON-LDデータ構造のテンプレート。
        -   **language_info.py**: リポジトリのプログラミング言語情報を処理するロジック。
        -   **markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを構築するロジック。
        -   **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`から概要を抽出するモジュール。
        -   **readme_badge_extractor.py**: リポジトリのREADMEからバッジ情報を抽出するロジック。
        -   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報に整形するモジュール。
        -   **seo_template.yml**: 検索エンジン最適化に関するテンプレートや設定。
        -   **statistics_calculator.py**: リポジトリの各種統計情報（スター数、フォーク数など）を計算するロジック。
        -   **strings.yml**: UI表示用のテキストやメッセージ文字列を管理する設定ファイル。
        -   **template_processor.py**: Markdown生成の際に使用するテンプレートを処理するモジュール。
        -   **url_utils.py**: URLに関するユーティリティ関数を集めたモジュール。
-   **test_project_overview.py**: プロジェクト概要取得機能のテストスクリプト。
-   **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    -   **conftest.py**: pytestのフィクスチャやプラグイン設定を定義するファイル。
    -   **test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    -   **test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
    -   **test_config.py**: 設定ファイルの読み込み・管理機能のテスト。
    -   **test_date_formatter.py**: 日付整形ユーティリティのテスト。
    -   **test_environment.py**: 実行環境のセットアップに関するテスト。
    -   **test_integration.py**: プロジェクト全体の主要機能の統合テスト。
    -   **test_markdown_generator.py**: Markdown生成機能のテスト。
    -   **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    -   **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテスト。
    -   **test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、各ファイルが特定の機能を受け持つ関数やクラスを提供しています。具体的な引数、戻り値の詳細はコード実装に依存しますが、ここでは各モジュールが提供する主要な機能について説明します。

-   **src/generate_repo_list/generate_repo_list.py 内の主要関数**:
    -   **役割**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力ファイルを生成するメインの処理を統括します。
    -   **引数**: `username` (GitHubユーザー名), `output` (出力ファイル名), `limit` (処理するリポジトリ数の上限) など。
    -   **戻り値**: 通常はNone（副作用としてファイル生成）。
    -   **機能**: コマンドライン引数を解析し、他のモジュール（`repository_processor`, `project_overview_fetcher`, `markdown_generator`など）と連携して、最終的なリポジトリ一覧Markdownファイルを作成します。

-   **src/generate_repo_list/badge_generator.py 内の主要関数/クラス**:
    -   **役割**: リポジトリの特性（言語、ライセンス、アーカイブ状態など）を示すバッジを生成または管理します。
    -   **引数**: (具体的な情報がないため、一般的な役割を説明します) リポジトリ情報、バッジの種類、スタイルなど。
    -   **戻り値**: (具体的な情報がないため、一般的な役割を説明します) バッジのMarkdown文字列またはURL。
    -   **機能**: リポジトリメタデータに基づいて、視覚的に情報を伝えるバッジを生成し、Markdownコンテンツに組み込む準備をします。

-   **src/generate_repo_list/project_overview_fetcher.py 内の主要関数/クラス**:
    -   **役割**: 各リポジトリに存在する`generated-docs/project-overview.md`ファイルから、プロジェクトの概要説明を抽出します。
    -   **引数**: (具体的な情報がないため、一般的な役割を説明します) リポジトリ名、ファイルパス、抽出するセクションタイトルなど。
    -   **戻り値**: (具体的な情報がないため、一般的な役割を説明します) 抽出された3行のプロジェクト概要。
    -   **機能**: 指定されたファイルを読み込み、設定に基づき特定のセクションからテキストをパースし、キャッシュメカニズムを介して効率的に概要を提供します。

-   **src/generate_repo_list/markdown_generator.py 内の主要関数/クラス**:
    -   **役割**: 処理されたリポジトリ情報とテンプレートを使用して、最終的なMarkdownコンテンツを生成します。
    -   **引数**: (具体的な情報がないため、一般的な役割を説明します) 処理済みリポジトリデータのリスト、テンプレートデータなど。
    -   **戻り値**: (具体的な情報がないため、一般的な役割を説明します) 生成されたMarkdown文字列。
    -   **機能**: リポジトリのメタデータ（名前、説明、言語、バッジ、概要など）をMarkdownの構造にマッピングし、Jekyllで適切にレンダリングされる形式のファイルを出力します。

-   **src/generate_repo_list/repository_processor.py 内の主要関数/クラス**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、プロジェクト内で扱いやすい形に整形・加工します。
    -   **引数**: (具体的な情報がないため、一般的な役割を説明します) GitHub APIから返されるリポジトリオブジェクト。
    -   **戻り値**: (具体的な情報がないため、一般的な役割を説明します) 構造化されたリポジトリ情報オブジェクトまたは辞書。
    -   **機能**: 取得したデータから必要なフィールドを抽出し、日付の変換や説明文の整形、ステータスの分類（アクティブ、アーカイブ、フォーク）などを行います。

-   **src/.github_automation/check_large_files/scripts/check_large_files.py 内の主要関数**:
    -   **役割**: 特定のファイルサイズ制限を超過するファイルがないかチェックします。
    -   **引数**: (具体的な情報がないため、一般的な役割を説明します) チェック対象のパス、設定ファイルなど。
    -   **戻り値**: (具体的な情報がないため、一般的な役割を説明します) チェック結果（成功/失敗）や見つかった大容量ファイルのリスト。
    -   **機能**: リポジトリ内のファイルサイズをスキャンし、`check-large-files.toml`で定義された制限と比較して、超過するファイルがあれば警告またはエラーを報告します。

## 関数呼び出し階層ツリー
```
[関数呼び出し階層を分析できませんでした]

---
Generated at: 2026-05-16 07:23:58 JST
