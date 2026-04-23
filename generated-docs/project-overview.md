Last updated: 2026-04-24

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動取得してMarkdown形式で出力するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンからのクロール改善とLLMによるリポジトリ参照の精度向上を目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツの形式)
- 音楽・オーディオ: 特になし
- 開発ツール:
    - Ruff: Pythonコードのスタイルチェックと自動整形ツール。
    - pytest: Pythonのテストフレームワーク。
- テスト: pytest (ユニットテストおよび統合テストに使用されます)。
- ビルドツール: Pythonスクリプト (Markdownファイルを生成する主要なツールとして機能します)。
- 言語機能: Python (プロジェクトの主要な開発言語)。
- 自動化・CI/CD:
    - GitHub API: リポジトリ情報の取得元として使用されます。
    - `.github_automation` ディレクトリが存在しますが、CI/CDはローカル開発重視とされており、直接的なパイプラインは明示されていません。
- 開発標準: Ruff (コードの品質と一貫性を保つためのルール設定)。

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
-   `.editorconfig`: 異なるエディタやIDE間でコードスタイルの一貫性を保つための設定ファイル。
-   `.github_automation/`: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    -   `check_large_files/`: 大容量ファイルのコミットを検出・防止するための自動化スクリプト群。
        -   `README.md`: `check_large_files` 機能に関する説明。
        -   `check-large-files.toml`: 大容量ファイルチェックの設定ファイル。
        -   `scripts/check_large_files.py`: 実際に大容量ファイルをチェックするPythonスクリプト。
-   `.gitignore`: Gitが追跡しないファイルやディレクトリを指定するファイル。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
-   `README.md`: プロジェクトの概要、セットアップ、使用方法など、全体的な情報を提供するメインドキュメント。
-   `_config.yml`: Jekyllサイトの設定ファイル。GitHub Pagesの振る舞いを定義します。
-   `assets/`: サイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズのファビコン画像。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグ用途のスクリプト。
-   `generated-docs/`: 生成されたドキュメントや一時ファイルを格納するディレクトリ。特に、各リポジトリのプロジェクト概要が配置される場所として参照されます。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権確認のために配置される静的HTMLファイル。
-   `index.md`: GitHub Pagesサイトのメインページとして生成されるMarkdownファイル。リポジトリ一覧がここに表示されます。
-   `issue-notes/`: 課題や検討事項に関するメモを格納するディレクトリ。
    -   `22.md`: 特定の課題（Issue #22）に関するメモ。
-   `manifest.json`: Webアプリマニフェストファイル。プログレッシブウェブアプリ（PWA）関連の設定を含みます。
-   `pytest.ini`: pytestテストフレームワークの設定ファイル。
-   `requirements-dev.txt`: 開発およびテスト時に必要なPythonパッケージの依存関係リスト。
-   `requirements.txt`: 本番環境で必要なPythonパッケージの依存関係リスト。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールするか指示するファイル。
-   `ruff.toml`: Ruffコードリンター/フォーマッターの設定ファイル。
-   `src/`: プロジェクトのソースコードを格納するディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示すファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成機能の主要なモジュール群。
        -   `__init__.py`: `generate_repo_list`がPythonパッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリのプロパティ（言語、ステータスなど）に応じたバッジのMarkdownを生成する機能を提供します。
        -   `config.yml`: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイル。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理する機能を提供します。
        -   `date_formatter.py`: 日付や時刻のフォーマットを処理するユーティリティ機能を提供します。
        -   `generate_repo_list.py`: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成します。
        -   `json_ld_template.json`: JSON-LD形式の構造化データテンプレート。SEO最適化のために使用されます。
        -   `language_info.py`: リポジトリの言語情報に関連するデータ処理や整形機能を提供します。
        -   `markdown_generator.py`: 取得したリポジトリ情報に基づいて、Markdown形式のコンテンツを生成する機能を提供します。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイルからプロジェクト概要を抽出し、取得する機能を提供します。
        -   `readme_badge_extractor.py`: READMEファイルから特定のバッジ情報（例: ビルドステータス）を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリ情報を整形・処理し、表示に適した形式に変換する機能を提供します。
        -   `seo_template.yml`: 検索エンジン最適化（SEO）のためのメタデータや構造化データのテンプレートを定義するファイル。
        -   `statistics_calculator.py`: リポジトリに関する統計情報（スター数、フォーク数など）を計算する機能を提供します。
        -   `strings.yml`: UIに表示されるメッセージや文言を管理するためのファイル。多言語対応や文言の一元管理に利用されます。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレート（JekyllのLiquidなど）の処理を支援する機能を提供します。
        -   `url_utils.py`: URLの生成、解析、検証など、URL関連のユーティリティ機能を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`機能のテストスクリプト。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリ。
    -   `conftest.py`: pytestのフィクスチャやヘルパー関数を定義するファイル。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テスト。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテスト。
    -   `test_config.py`: 設定ファイル処理のテスト。
    -   `test_date_formatter.py`: 日付フォーマット機能のテスト。
    -   `test_environment.py`: 実行環境に関連するテスト。
    -   `test_integration.py`: 主要な機能の統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリ情報処理機能のテスト。

## 関数詳細説明
このセクションでは、主要なPythonファイルに含まれるであろう代表的な関数の役割、引数、戻り値、機能について説明します。具体的なコードスニペットがないため、ファイル名とプロジェクトの目的から推測される一般的な機能に基づいて記述します。

-   **`src/generate_repo_list/generate_repo_list.py`**
    -   `main(username: str, output_file: str, limit: Optional[int] = None) -> None`:
        -   **役割**: プロジェクト全体の実行フローを統括するエントリポイント。
        -   **引数**:
            -   `username` (str): GitHubユーザー名。
            -   `output_file` (str): 生成されたMarkdownの出力先ファイル名。
            -   `limit` (Optional[int]): 処理するリポジトリ数の上限（開発用、オプション）。
        -   **戻り値**: なし
        -   **機能**: コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成、ファイル出力までの一連のプロセスをオーケストレートします。

-   **`src/generate_repo_list/repository_processor.py`**
    -   `fetch_and_process_repositories(username: str, github_token: str, limit: Optional[int] = None) -> List[Dict[str, Any]]`:
        -   **役割**: GitHub APIからリポジトリ情報を取得し、整形処理を行います。
        -   **引数**:
            -   `username` (str): 対象のGitHubユーザー名。
            -   `github_token` (str): GitHub API認証用のパーソナルアクセストークン。
            -   `limit` (Optional[int]): 取得するリポジトリ数の上限。
        -   **戻り値**: 処理されたリポジトリ情報の辞書リスト。
        -   **機能**: GitHub APIへのリクエストを行い、レスポンスから必要なリポジトリデータを抽出し、統一された構造に変換します。

-   **`src/generate_repo_list/markdown_generator.py`**
    -   `generate_repository_list_markdown(repositories: List[Dict[str, Any]], strings_config: Dict[str, str]) -> str`:
        -   **役割**: 処理済みのリポジトリ情報に基づいて、GitHub Pages用のMarkdownコンテンツを生成します。
        -   **引数**:
            -   `repositories` (List[Dict[str, Any]]): 処理されたリポジトリ情報のリスト。
            -   `strings_config` (Dict[str, str]): 表示メッセージや文言を定義した設定。
        -   **戻り値**: 生成されたMarkdown文字列。
        -   **機能**: 各リポジトリのタイトル、説明、バッジ、リンクなどを整形し、Jekyllが解釈できるMarkdown形式に組み立てます。

-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   `get_project_overview(repo_name: str, config: Dict[str, Any]) -> Optional[List[str]]`:
        -   **役割**: 特定のリポジトリの`generated-docs/project-overview.md`から3行のプロジェクト概要を抽出します。
        -   **引数**:
            -   `repo_name` (str): 対象のリポジトリ名。
            -   `config` (Dict[str, Any]): プロジェクト概要取得に関する設定（ファイルパス、セクションタイトルなど）。
        -   **戻り値**: 3行の概要リスト、または抽出できなかった場合は`None`。
        -   **機能**: 指定されたファイルパスのリポジトリコンテンツを読み込み、設定に基づき「プロジェクト概要」セクションから指定行数を抽出します。

-   **`src/generate_repo_list/badge_generator.py`**
    -   `create_badge_markdown(label: str, message: str, color: str = 'blue') -> str`:
        -   **役割**: ラベル、メッセージ、色を指定してバッジのMarkdownスニペットを生成します。
        -   **引数**:
            -   `label` (str): バッジの左側のテキスト（例: "Language"）。
            -   `message` (str): バッジの右側のテキスト（例: "Python"）。
            -   `color` (str): バッジの色（例: "blue", "green"）。
        -   **戻り値**: 生成されたバッジのMarkdown文字列（例: `![Label](https://img.shields.io/badge/Label-Message-Color)`）。
        -   **機能**: Shields.ioのようなサービスを利用して動的なバッジ画像を生成するためのMarkdown構文を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-24 07:19:29 JST
