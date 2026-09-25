Last updated: 2026-09-26

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けのリポジトリ情報を自動で取得・整理します。
- SEO最適化されたリポジトリ一覧をMarkdown形式で生成し、サイトの検索エンジン評価を向上させます。
- 検索エンジンやLLMからの参照性を高めることで、プロジェクトの可視性と開発効率向上に貢献します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして利用), **Markdown** (生成されるコンテンツの形式)
- 音楽・オーディオ: なし
- 開発ツール: **pytest** (Python用テストフレームワーク), **ruff** (Pythonの高速Linter/Formatter)
- テスト: **pytest** (Pythonコードの単体テストおよび統合テストに使用)
- ビルドツール: **Jekyll** (GitHub Pagesが内部で使用するビルドエンジン)
- 言語機能: **Python** (プロジェクトの主要な開発言語)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation`ディレクトリの存在から、特定タスクの自動化に利用される可能性を示唆)
- 開発標準: **ruff** (コードスタイル自動修正), **.editorconfig** (IDE/エディタ間のコードスタイル統一設定)

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
- **`.editorconfig`**: エディタやIDE間でコードの整形ルール（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクト全体の目的、機能、使い方などを説明するメインのドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の動作や表示に関する設定を行うファイルです。
- **`assets/`**: サイトで使用される静的アセット（画像ファイル、ファビコンなど）を格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 各リポジトリから取得した概要などの、生成されたドキュメントや一時ファイルを格納する可能性があります。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認に使用されるファイルです。
- **`index.md`**: メインスクリプトによって生成される、リポジトリ一覧が記述されたトップページ用のMarkdownファイルです。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細を記述したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルで、ホーム画面への追加やオフライン動作に関する設定が含まれます。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの依存関係を定義するファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するのに必要なPythonライブラリの依存関係を定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールして良いか、または避けるべきかを指示するファイルです。
- **`ruff.toml`**: PythonのLinter/Formatterである`ruff`の設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージを示すファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やステータスに応じたバッジの情報を生成するロジックを扱います。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの、動的な設定値を定義するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するクラスや関数を提供します。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する一連の処理を orchestrate します。
- **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートで、SEO強化のためにWebページに埋め込まれるメタデータを定義します。
- **`src/generate_repo_list/language_info.py`**: リポジトリの言語に関する情報を処理し、表示に役立つデータを提供するモジュールです。
- **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリデータに基づいて、最終的なMarkdownコンテンツを生成するロジックを含みます。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例:`generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能です。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、表示に適した形式に加工する処理を担います。
- **`src/generate_repo_list/seo_template.yml`**: サイトのSEO（検索エンジン最適化）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を一元管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
- **`src/generate_repo_list/template_processor.py`**: Markdownや他のテキストテンプレートを読み込み、動的なデータを埋め込んで最終的な出力を作成する処理を扱います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能のテストコードです。
- **`tests/conftest.py`**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイルです。
- **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストコードです。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストコードです。
- **`tests/test_config.py`**: 設定管理機能のテストコードです。
- **`tests/test_date_formatter.py`**: 日付整形機能のテストコードです。
- **`tests/test_environment.py`**: 実行環境に関する設定や依存関係のテストコードです。
- **`tests/test_integration.py`**: プロジェクト全体の主要なフローに関する統合テストコードです。
- **`tests/test_markdown_generator.py`**: Markdown生成機能のテストコードです。
- **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコードです。
- **`tests/test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストコードです。
- **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストコードです。

## 関数詳細説明
このプロジェクトで定義されている関数の詳細な情報（引数、戻り値、具体的な実装ロジック）は提供されていません。しかし、ファイル名とプロジェクトの機能から、以下のような役割を持つ関数が存在すると推測されます。

- **`src/generate_repo_list/generate_repo_list.py`内のメイン関数**:
    - **役割**: コマンドライン引数を解析し、GitHub APIを呼び出してリポジトリ情報を取得、その情報を整形・加工し、最終的にMarkdown形式のリポジトリ一覧ファイルを出力する一連の処理を調整します。
    - **引数**: GitHubユーザー名、出力ファイルパス、処理リポジトリ数上限など。
    - **戻り値**: なし（ファイル出力が主目的）。
- **`src/generate_repo_list/badge_generator.py`内の関数**:
    - **役割**: リポジトリの言語やアーカイブ状態などに基づき、表示用のバッジ（画像URLやMarkdownスニペット）を生成します。
    - **引数**: リポジトリ情報オブジェクト（言語、アーカイブ状態など）。
    - **戻り値**: バッジのURLまたはMarkdown文字列。
- **`src/generate_repo_list/project_overview_fetcher.py`内の関数**:
    - **役割**: 特定のリポジトリ（またはローカルパス）から`generated-docs/project-overview.md`ファイルを読み込み、「プロジェクト概要」セクションの3行説明を抽出します。
    - **引数**: リポジトリ名またはファイルパス、セクションタイトル、リトライ設定など。
    - **戻り値**: 抽出された3行のプロジェクト概要（文字列のリストまたは結合された文字列）。
- **`src/generate_repo_list/markdown_generator.py`内の関数**:
    - **役割**: 処理済みのリポジトリデータを受け取り、Jekyllの要件に合わせた形で、完全なリポジトリ一覧のMarkdownコンテンツを構築します。
    - **引数**: 整形されたリポジトリ情報のリスト、SEOメタデータ、テンプレートなど。
    - **戻り値**: 生成されたMarkdownコンテンツ（文字列）。
- **`src/generate_repo_list/repository_processor.py`内の関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーション内で扱いやすいカスタムオブジェクトや辞書の形式に変換・整形します。不要な情報をフィルタリングしたり、必要な情報を追加計算したりすることもあります。
    - **引数**: GitHub APIから取得したリポジトリの生データ。
    - **戻り値**: 整形されたリポジトリ情報オブジェクト。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-26 07:12:12 JST
