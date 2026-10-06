Last updated: 2026-10-07

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、GitHub Pages向けにMarkdownファイルを自動生成するシステムです。
- 生成されたコンテンツはSEO最適化され、検索エンジンやLLMによる参照を容易にすることを目的としています。
- Jekyll/GitHub Pagesに対応し、ユーザーのリポジトリ一覧と各リポジトリの詳細ページを自動的に公開・更新します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllサイトのホスティングプラットフォームとして利用), Markdown (自動生成されるコンテンツの形式)
- 音楽・オーディオ: (該当する技術の使用情報はありません)
- 開発ツール: Python (スクリプトの実行環境として使用), GitHub API (リポジトリ情報の取得元)
- テスト: Pytest (Pythonプロジェクトのテストフレームワーク)
- ビルドツール: Python (スクリプト自体がMarkdownファイルを「ビルド」する役割を担う)
- 言語機能: Python (プロジェクトの主要なプログラミング言語)
- 自動化・CI/CD: (このプロジェクト自体が自動化システムですが、特定のCI/CDツールを使用しているという明示的な情報はありません)
- 開発標準: Ruff (Pythonコードのリンターおよびフォーマッターとしてコード品質を維持)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリ。
- **`.github_automation/check_large_files/README.md`**: `check_large_files`スクリプトに関する説明ドキュメント。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイル。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリのパターンを指定するファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **`README.md`**: プロジェクトの概要、目的、使用方法などを説明するメインのドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイル。
- **`assets/`**: Jekyllサイトで利用される画像、アイコン、その他の静的アセットを格納するディレクトリ。
- **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）画像ファイル群。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単体テストに利用されるスクリプト。
- **`generated-docs/`**: 本システムによって生成されたドキュメントや一時ファイルを格納するためのディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権確認用のHTMLファイル。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイル。このファイルにリポジトリ一覧が自動生成されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細な情報が記述されたファイル。
- **`manifest.json`**: ウェブアプリケーションマニフェスト。プログレッシブウェブアプリ（PWA）の機能を提供する際にブラウザにサイトの情報を伝えるために使用されます。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイル。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonライブラリの依存関係リスト。
- **`requirements.txt`**: プロジェクトの本番環境で必要となるPythonライブラリの依存関係リスト。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **`ruff.toml`**: Pythonの高速なリンターRuffの設定ファイル。コードスタイルと品質を維持するために使用されます。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
- **`src/__init__.py`**: Pythonパッケージであることを示すファイル。
- **`src/generate_repo_list/`**: リポジトリ一覧自動生成システムのコアロジックを格納するパッケージ。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`パッケージであることを示すファイル。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを設定するためのYAMLファイル。
- **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）を読み込み、管理するためのモジュール。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のフォーマットを処理するためのユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式でリポジトリ一覧を生成するメインスクリプト。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレート。
- **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示するためのモジュール。
- **`src/generate_repo_list/markdown_generator.py`**: GitHub Pages用のMarkdownコンテンツを生成する機能を提供します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリから`generated-docs/project-overview.md`ファイルを読み込み、プロジェクト概要の3行説明を抽出するモジュール。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから特定のバッジ情報を抽出するためのモジュール。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形・処理し、表示に適した形式に変換するモジュール。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイル。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算するモジュール。
- **`src/generate_repo_list/strings.yml`**: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を管理するためのYAMLファイル。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成におけるテンプレートのロード、パース、レンダリングを処理するモジュール。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証などのユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールのテストコード。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
- **`tests/conftest.py`**: Pytestの共通フィクスチャやヘルパー関数を定義するファイル。
- **`tests/test_badge_generator_integration.py`**: バッジジェネレータの統合テストコード。
- **`tests/test_check_large_files.py`**: 大容量ファイルチェック機能のテストコード。
- **`tests/test_config.py`**: 設定ファイル（`config.yml`など）の読み込みや管理機能に関するテストコード。
- **`tests/test_date_formatter.py`**: 日付フォーマッタのテストコード。
- **`tests/test_environment.py`**: 実行環境に関するテストやセットアップ検証コード。
- **`tests/test_integration.py`**: システム全体のエンドツーエンドの統合テストコード。
- **`tests/test_markdown_generator.py`**: Markdown生成機能のテストコード。
- **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストコード。
- **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストコード。
- **`tests/test_repository_processor.py`**: リポジトリ情報処理機能のテストコード。

## 関数詳細説明
提供された情報からは具体的な関数の詳細（役割、引数、戻り値）を特定できませんでした。ファイル名から推測される役割は「ファイル詳細説明」セクションに記載しています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-07 07:13:15 JST
