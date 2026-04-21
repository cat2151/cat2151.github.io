Last updated: 2026-04-22

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたMarkdownファイルはJekyllと連携し、リポジトリ情報をSEO最適化された形で公開します。
- 検索エンジンからのクロール性向上と、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: GitHub Pages (静的サイトホスティング), Jekyll (Markdownからのサイト生成), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (テストフレームワーク), ruff (コードリンター/フォーマッター)
- テスト: pytest (Pythonコードの単体・統合テスト実行)
- ビルドツール: Pythonスクリプト (リポジトリ情報取得・Markdown生成のコアロジック)
- 言語機能: Python (主要な開発言語)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリが存在し、間接的に自動化が想定されるが、プロジェクト自体はローカル開発重視と明記されている)
- 開発標準: ruff (コードスタイルの統一と品質保持)

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
-   **`.editorconfig`**: エディタのコードスタイル設定を定義し、プロジェクト全体で一貫したコーディングスタイルを強制します。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトに関連するファイルを格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルを検出・管理するための自動化スクリプト群を格納します。
        -   **`README.md`**: `check_large_files` 機能に関する説明を提供します。
        -   **`check-large-files.toml`**: `check_large_files` スクリプトの設定ファイルです。
        -   **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの概要、目的、設定方法、使用方法、開発者向けのヒントなどが記された主要なドキュメントです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、GitHub Pagesの挙動を制御します。
-   **`assets/`**: GitHub Pagesサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグや単独テストに使用されるスクリプトです。
-   **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要などのドキュメントを格納するためのプレースホルダディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: メインの出力ファイルで、自動生成されたリポジトリ一覧がMarkdown形式で格納され、GitHub Pagesのトップページとして機能します。
-   **`issue-notes/`**: プロジェクトの課題や検討事項に関するメモを格納するディレクトリです。
    -   **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや情報が記述されています。
-   **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示設定などを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の設定ファイルです。
-   **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージの依存関係をリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトの実行に必要なPythonパッケージの依存関係をリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンティングおよびフォーマットツールである`ruff`の設定ファイルです。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    -   **`generate_repo_list/`**: リポジトリ一覧を生成するコアロジックを格納するPythonパッケージです。
        -   **`__init__.py`**: `generate_repo_list` パッケージであることを示すファイルです。
        -   **`badge_generator.py`**: リポジトリの言語やライセンスなどのバッジ情報を生成するロジックを扱います。
        -   **`config.yml`**: `generate_repo_list` スクリプトの実行時設定（APIトークン、プロジェクト概要機能の有効/無効など）を定義します。
        -   **`config_manager.py`**: プロジェクトの設定ファイル（`config.yml`, `strings.yml`）を読み込み、管理するロジックです。
        -   **`date_formatter.py`**: 日付や時刻の情報を特定の形式で整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力するプロジェクトのメインスクリプトです。
        -   **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレートファイルです。
        -   **`language_info.py`**: プログラミング言語に関する追加情報や表示名を処理・管理するロジックです。
        -   **`markdown_generator.py`**: 取得および整形されたリポジトリ情報からMarkdownコンテンツを生成するロジックです。
        -   **`project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報を抽出するロジックです。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、アプリケーションで扱いやすい形式に加工・整形するロジックです。
        -   **`seo_template.yml`**: SEO関連のメタデータやテンプレート設定を定義するファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・集計するロジックです。
        -   **`strings.yml`**: アプリケーションの表示メッセージや文言を一元管理するための設定ファイルです。
        -   **`template_processor.py`**: Markdownテンプレートファイルなどを読み込み、動的にコンテンツを埋め込む処理を行うロジックです。
        -   **`url_utils.py`**: URLの操作や構築に関する共通のユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher` 機能の単体テストを行うスクリプトです。
-   **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
    -   **`conftest.py`**: `pytest` のテスト実行時に共通で使用されるフィクスチャやフックを定義するファイルです。
    -   **`test_badge_generator_integration.py`**: `badge_generator` 機能の統合テストを行います。
    -   **`test_check_large_files.py`**: `check_large_files` スクリプトのテストを行います。
    -   **`test_config.py`**: 設定ファイルの読み込みと管理に関するテストを行います。
    -   **`test_date_formatter.py`**: `date_formatter` のユーティリティ関数のテストを行います。
    -   **`test_environment.py`**: プロジェクトの実行環境に関するテストを行います。
    -   **`test_integration.py`**: プロジェクトの主要な機能間の連携をテストする統合テストです。
    -   **`test_markdown_generator.py`**: `markdown_generator` が正しくMarkdownを生成するかテストします。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher` が正しくプロジェクト概要を抽出するかテストします。
    -   **`test_readme_badge_extractor.py`**: `readme_badge_extractor` がREADMEからバッジ情報を正しく抽出するかテストします。
    -   **`test_repository_processor.py`**: `repository_processor` がリポジトリデータを正しく処理・整形するかテストします。

## 関数詳細説明
このセクションでは、プロジェクトの主要なスクリプトやモジュールが提供する役割について説明します。具体的な関数シグネチャは提供されていませんが、ファイル名とプロジェクト概要からその機能を推測します。

-   **`src/generate_repo_list/generate_repo_list.py` (メインスクリプト)**
    -   **役割**: プロジェクトの中核であり、GitHub APIからリポジトリ情報を取得し、そのデータをもとにGitHub Pagesサイト用のMarkdown形式リポジトリ一覧を生成します。
    -   **機能**: GitHub認証の管理、指定されたユーザーのリポジトリ情報の取得、取得したリポジトリデータのフィルタリングと加工、各リポジトリの詳細情報（プロジェクト概要、バッジなど）の収集、そして最終的なMarkdownコンテンツの生成とファイルへの書き出しを行います。
-   **`src/generate_repo_list/badge_generator.py`**
    -   **役割**: リポジトリに関連する様々なバッジ（例：使用言語、ライセンス、アーカイブ状態など）の情報を生成し、Markdown形式で埋め込めるように整形します。
    -   **機能**: リポジトリの属性に基づいて適切なバッジアイコンやテキストを決定し、Markdown構文で出力します。
-   **`src/generate_repo_list/config_manager.py`**
    -   **役割**: プロジェクトの設定ファイル（`config.yml`や`strings.yml`）を読み込み、アプリケーション全体で安全かつ効率的にアクセスできるように管理します。
    -   **機能**: YAMLファイルをパースし、キーと値のペアとして設定データを提供します。
-   **`src/generate_repo_list/date_formatter.py`**
    -   **役割**: 日付と時刻のデータを指定されたフォーマット（例：人間が読みやすい形式）に変換するユーティリティ機能を提供します。
    -   **機能**: APIから取得したISO形式の日付文字列などを、ウェブサイト表示に適した形式に変換します。
-   **`src/generate_repo_list/markdown_generator.py`**
    -   **役割**: 処理されたリポジトリデータに基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを構築します。
    -   **機能**: テンプレートとリポジトリデータ（タイトル、説明、バッジ、リンクなど）を組み合わせて、整形されたMarkdown文字列を生成します。
-   **`src/generate_repo_list/project_overview_fetcher.py`**
    -   **役割**: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出し取得します。
    -   **機能**: GitHub APIを介してターゲットファイルのコンテンツをフェッチし、定義されたセクションから指定された行数のテキストをパースして抽出します。キャッシュ機能も備えています。
-   **`src/generate_repo_list/repository_processor.py`**
    -   **役割**: GitHub APIから取得した生のリポジトリデータを、アプリケーションの他の部分で利用しやすい形に加工・整形します。
    -   **機能**: 必要なフィールドの抽出、データのクリーニング、アクティブ/アーカイブ/フォークの分類など、表示に必要な追加情報の計算を行います。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-22 07:18:47 JST
