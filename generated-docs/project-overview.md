Last updated: 2026-05-22

# Project Overview

## プロジェクト概要
- GitHub Pagesサイトで個人リポジトリ一覧を自動生成し、表示するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- 検索エンジンからの可視性を高め、自身の開発実績やプロジェクト情報を効率的に共有することを目指します。

## 技術スタック
### フロントエンド
- **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトで生成されたMarkdownファイルを美しいWebページに変換するために利用されます。
- **Markdown**: リポジトリ一覧や各リポジトリの概要を記述するための軽量マークアップ言語。本システムが最終的に生成するコンテンツ形式です。

### 音楽・オーディオ
- なし

### 開発ツール
- **Python**: プロジェクトの主要なスクリプト言語。リポジトリ情報の取得、処理、Markdown生成など全てをPythonで実装しています。
- **Git/GitHub API**: リポジトリ情報の取得にGitHub APIを使用。バージョン管理はGitで行われます。

### テスト
- **pytest**: Python用のテストフレームワーク。プロジェクトの機能が正しく動作することを保証するための単体テストや統合テストに使用されます。

### ビルドツール
- **Jekyll**: GitHub Pagesの静的サイトジェネレーター。本プロジェクトで生成されたMarkdownファイルを美しいWebページに変換するために利用されます。

### 言語機能
- **Python**: プロジェクトの主要なスクリプト言語。リポジトリ情報の取得、処理、Markdown生成など全てをPythonで実装しています。

### 自動化・CI/CD
- **GitHub Pages**: GitHubリポジトリから直接Webサイトをホストするサービス。本システムで生成されたコンテンツを公開するために利用されます。

### 開発標準
- **ruff**: Pythonコードのリンターおよびフォーマッター。コードの品質を維持し、統一されたコーディングスタイルを強制するために使用されます。

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなど、GitHub上での自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    - **.github_automation/check_large_files/**: 大容量ファイルチェックに関する自動化スクリプト群。
        - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明。
        - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェックのルールや設定を定義するファイル。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの概要、使い方、設定方法などを記述した、リポジトリの顔となるマークダウンファイル。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの挙動を制御します。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的リソースを格納するディレクトリ。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズ。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ用途で使用されるPythonスクリプト。
- **generated-docs/**: プロジェクトによって自動生成されたドキュメントやコンテンツを格納するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイル。
- **index.md**: 生成されたリポジトリ一覧のメインページとなるマークダウンファイル。GitHub Pagesのトップページとして表示されます。
- **issue-notes/**: 課題管理に関するメモや詳細を格納するディレクトリ。
    - **issue-notes/22.md**: 特定の課題（Issue #22など）に関するメモや詳細を記述したマークダウンファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のメタデータを提供するマニフェストファイル。Webサイトのホーム画面追加アイコンや表示設定を定義します。
- **pytest.ini**: pytestテストフレームワークの設定ファイル。テストの実行オプションなどを指定します。
- **requirements-dev.txt**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンを記述したファイル。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonコードリンター「Ruff」の設定ファイル。コードスタイルや静的解析のルールを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **src/__init__.py**: Pythonパッケージを示すファイル。
    - **src/generate_repo_list/**: リポジトリ一覧生成機能のコアロジックを格納するパッケージ。
        - **src/generate_repo_list/__init__.py**: Pythonパッケージを示すファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリに表示するバッジ（例: 言語、ライセンス）を生成する機能を持つスクリプト。
        - **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプトの技術的な設定パラメータを定義するYAMLファイル。
        - **src/generate_repo_list/config_manager.py**: 設定ファイル（config.ymlなど）の読み込みと管理を行うスクリプト。
        - **src/generate_repo_list/date_formatter.py**: 日付フォーマットに関するユーティリティ関数を提供するスクリプト。
        - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を実行します。
        - **src/generate_repo_list/json_ld_template.json**: SEO最適化のためのJSON-LD形式の構造化データテンプレート。
        - **src/generate_repo_list/language_info.py**: リポジトリの主要言語に関する情報を処理・整形するスクリプト。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成するスクリプト。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリからプロジェクト概要を自動取得する機能を持つスクリプト。
        - **src/generate_repo_list/readme_badge_extractor.py**: READMEファイルからバッジ情報を抽出する機能を持つスクリプト。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した個々のリポジトリ情報を処理・整形するスクリプト。
        - **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリに関する統計情報（スター数、フォーク数など）を計算するスクリプト。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージや文言を管理するYAMLファイル。多言語対応や文言の一元管理に利用されます。
        - **src/generate_repo_list/template_processor.py**: Markdown生成に使用されるテンプレートファイルの処理を行うスクリプト。
        - **src/generate_repo_list/url_utils.py**: URL関連のユーティリティ関数（URLの検証、生成など）を提供するスクリプト。
- **test_project_overview.py**: プロジェクト概要取得機能の単体テストを記述したファイル。
- **tests/**: プロジェクト全体のテストファイルを格納するディレクトリ。
    - **tests/conftest.py**: pytestのテスト設定やフィクスチャを定義するファイル。
    - **tests/test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **tests/test_check_large_files.py**: 大容量ファイルチェック機能のテスト。
    - **tests/test_config.py**: 設定ファイル（config.ymlなど）の読み込みや管理機能のテスト。
    - **tests/test_date_formatter.py**: 日付フォーマットユーティリティのテスト。
    - **tests/test_environment.py**: 実行環境に関するテスト。
    - **tests/test_integration.py**: 主要機能の統合テスト。
    - **tests/test_markdown_generator.py**: Markdown生成機能のテスト。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能のテスト。
    - **tests/test_readme_badge_extractor.py**: READMEバッジ抽出機能のテスト。
    - **tests/test_repository_processor.py**: リポジトリ情報処理機能のテスト。

## 関数詳細説明
プロジェクト情報には関数の具体的な詳細情報が提供されていないため、個別の関数の役割、引数、戻り値、機能について詳細な説明はできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-22 07:32:20 JST
