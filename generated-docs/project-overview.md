Last updated: 2026-08-15

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、リポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、SEOを意識したMarkdown形式で出力を生成します。
- 検索エンジンからのクロール改善とLLMの参照精度向上を目的としています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤として利用)、Markdown (生成されるコンテンツの形式)
- 音楽・オーディオ: このプロジェクトには関連する技術は使用されていません。
- 開発ツール: GitHub API (リポジトリ情報の取得)、pytest (テストフレームワーク)、ruff (コードフォーマッタ、リンター)
- テスト: pytest (Pythonコードの単体・統合テストに使用)
- ビルドツール: Python (スクリプト実行環境)、YAML (設定ファイルの記述)、JSON (JSON-LDテンプレートやデータ形式)
- 言語機能: Python (プロジェクトの主要な開発言語)
- 自動化・CI/CD: Pythonスクリプトによる自動生成 (ローカル実行を重視しており、明示的なCI/CDツールは使用されていません)
- 開発標準: ruff (コード品質とスタイルの統一を保証)

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
- **`.github_automation/check_large_files/`**: 大容量ファイルをチェックするための自動化スクリプト群を格納するディレクトリ。
    - **`README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメント。
    - **`check-large-files.toml`**: 大容量ファイルチェックのルールや設定を定義するファイル。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定する設定ファイル。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定など、全体の情報を提供するメインドキュメント。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの挙動に影響します。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるウェブサイトのファビコン画像群。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のテストやデバッグを目的としたスクリプト。
- **`generated-docs/`**: 本プロジェクトによって生成されたドキュメントやデータが格納される場所。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイル。
- **`index.md`**: `generate_repo_list.py` スクリプトによって生成され、GitHub PagesのトップページとなるMarkdownファイル。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関する詳細なメモや解決策が記述されたファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）として機能するための設定を定義するマニフェストファイル。
- **`pytest.ini`**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイル。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイル。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを列挙したファイル。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットを担うRuffツールの設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **`__init__.py`**: Pythonパッケージであることを示すファイル。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧を生成するメインロジックを含むパッケージ。
        - **`__init__.py`**: Pythonサブパッケージであることを示すファイル。
        - **`badge_generator.py`**: リポジトリのステータスや技術を示すバッジ画像を生成するロジックを実装。
        - **`config.yml`**: `generate_repo_list` 機能に関する詳細な設定（例: プロジェクト概要取得設定など）を定義。
        - **`config_manager.py`**: `config.yml` などの設定ファイルを読み込み、管理するモジュール。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供。
        - **`generate_repo_list.py`**: プロジェクトの中核となるスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD）を生成する際のテンプレート。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に活用。
        - **`markdown_generator.py`**: リポジトリ情報をもとに、GitHub Pages用のMarkdown形式のコンテンツを生成するロジック。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイルからプロジェクト概要の3行説明を抽出し取得する機能。
        - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を解析・抽出する機能。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整理・加工し、表示に適した形に変換するロジック。
        - **`seo_template.yml`**: 生成されるMarkdownファイルのSEO関連メタデータ（タイトル、説明など）のテンプレートを定義。
        - **`statistics_calculator.py`**: リポジトリの星の数、フォーク数などの統計情報を計算するロジック。
        - **`strings.yml`**: アプリケーション内で使用される表示メッセージや各種文言を一元管理するためのファイル。
        - **`template_processor.py`**: Jekyllなどのテンプレートシステムで使用されるファイルの処理を行うロジック。
        - **`url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要取得）を検証するためのテストスクリプト。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **`conftest.py`**: pytestテストランナーのためのフィクスチャやヘルパー関数を定義するファイル。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合的な動作を確認するテスト。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能の正確性を検証するテスト。
    - **`test_config.py`**: 設定ファイルの読み込みと処理が正しく行われるかを検証するテスト。
    - **`test_date_formatter.py`**: 日付整形機能の正確性を検証するテスト。
    - **`test_environment.py`**: 開発・実行環境のセットアップが適切であるかを検証するテスト。
    - **`test_integration.py`**: 主要なコンポーネントが連携して動作するかを検証する統合テスト。
    - **`test_markdown_generator.py`**: Markdown生成ロジックの正確性を検証するテスト。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能の動作を検証するテスト。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能の正確性を検証するテスト。
    - **`test_repository_processor.py`**: リポジトリデータ処理ロジックの正確性を検証するテスト。

## 関数詳細説明
提供された情報には、個別の関数の詳細なリストやその役割、引数、戻り値に関する情報が含まれていないため、具体的な説明はできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-08-15 07:06:16 JST
