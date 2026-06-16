Last updated: 2026-06-17

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHubリポジトリ情報を自動で取得するシステムです。
- 取得した情報から、検索エンジンに最適化されたGitHub Pages用のリポジトリ一覧ページを自動生成します。
- これにより、個々のリポジトリが検索エンジンやLLMに発見されやすくなり、情報参照の利便性を高めます。

## 技術スタック
- フロントエンド: **Jekyll (GitHub Pages)**: 静的サイトジェネレーターであり、GitHub Pagesの基盤として利用され、生成されたMarkdownファイルをウェブサイトとして公開します。
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語として使用されており、リポジトリ情報の取得、処理、Markdown生成スクリプトがPythonで書かれています。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラム的に取得するために使用されます。
- テスト:
    - **pytest**: Python用のテストフレームワークであり、プロジェクトのコードの品質と信頼性を保証するために使用されます。
- ビルドツール:
    - **Markdown生成スクリプト (Python)**: GitHub APIから取得したデータを元に、Jekyllが解釈できるMarkdown形式のファイルを自動生成します。
- 言語機能:
    - **Python**: オブジェクト指向プログラミングや、強力な標準ライブラリを活用してスクリプトが構築されています。
- 自動化・CI/CD:
    - **GitHub Actions (概念)**: 直接的なCI/CDパイプラインはこのプロジェクト内に定義されていませんが、本プロジェクトが生成する情報はGitHub Actionsとの連携を想定しており、自動化されたワークフローの一部として利用されることが期待されます。
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックとフォーマットを自動化するリンターであり、コードの一貫性と品質を保ちます。
    - **EditorConfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。

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
- **`.editorconfig`**: コードエディタ間でインデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化されたタスクに関するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルが存在しないかチェックする機能関連のファイル群です。
        - **`README.md`**: `check_large_files` 機能に関する説明書です。
        - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイルです。
        - **`scripts/check_large_files.py`**: 実際に大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクト全体の概要、目的、使い方、設定方法などを説明するメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllによって構築されるGitHub Pagesサイト全体の構成設定を定義するファイルです。
- **`assets/`**: GitHub Pagesサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブに表示されるアイコン）の各種サイズです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動的に取得された「プロジェクト概要」などのドキュメントが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のための認証ファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトによってリポジトリ一覧がここに自動生成されます。
- **`issue-notes/22.md`**: 特定の課題（Issue #22）に関するメモや詳細情報が記述されているファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）として動作させるための設定を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージのリストです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行する際に必要となるPythonパッケージのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいは避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルと品質を自動的にチェック・修正するツール `ruff` の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能の中核となるモジュール群です。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成するロジックを管理します。
        - **`config.yml`**: リポジトリ一覧生成に関する様々な設定（例：プロジェクト概要の取得方法など）を定義するファイルです。
        - **`config_manager.py`**: `config.yml` などの設定ファイルを読み込み、プログラム内で利用できるように管理するモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: **このプロジェクトのメインスクリプト**です。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD）のテンプレートを提供します。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理・解析します。
        - **`markdown_generator.py`**: 取得・処理されたリポジトリ情報から、GitHub Pages用のMarkdownコンテンツを生成する役割を担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要のテキストを自動的に取得する機能を提供します。
        - **`readme_badge_extractor.py`**: 各リポジトリのREADMEファイル内に埋め込まれたバッジ（例：ビルドステータスなど）の情報を抽出します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
        - **`seo_template.yml`**: SEO関連のメタデータや、ページに含めるキーワードなどのテンプレート設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（スター数、フォーク数など）を計算する機能を提供します。
        - **`strings.yml`**: 生成されるMarkdownファイルや出力メッセージに使用される、多言語対応可能な文字列リソースを管理するファイルです。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（JekyllのLiquidなど）を処理し、動的なコンテンツを埋め込む機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能が正しく動作するかを検証するテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: `pytest` のテスト実行時に共通で使用される設定やフィクスチャを定義するファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定ファイル読み込み・管理機能のテストです。
    - **`test_date_formatter.py`**: 日付整形機能のテストです。
    - **`test_environment.py`**: 開発環境のセットアップや依存関係に関するテストです。
    - **`test_integration.py`**: システム全体の連携が正しく行われるかを検証する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ情報抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能のテストです。

## 関数詳細説明
このプロジェクトは複数のPythonファイルで構成されており、各ファイルは特定の役割を果たすための関数群を含んでいます。例えば、`generate_repo_list.py` は全体の処理を調整するメイン関数を、`repository_processor.py` はリポジトリデータの加工に関する関数を、`markdown_generator.py` はMarkdown文字列を生成する関数群をそれぞれ持っています。

しかしながら、提供された情報には個々の関数の具体的な名前、引数、戻り値、詳細な機能についての記述がないため、ここでは具体的な関数の詳細説明は割愛します。各ファイルが担う役割の中で、必要な処理が関数として実装されているとご理解ください。

## 関数呼び出し階層ツリー
```
（関数呼び出し階層に関する具体的な情報は提供されていません）

---
Generated at: 2026-06-17 07:40:54 JST
