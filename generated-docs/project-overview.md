Last updated: 2026-10-12

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、検索エンジン最適化されたMarkdown形式で出力します。
- 各リポジトリの概要も自動で取得・表示し、検索性向上とLLMによる参照を支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、生成されたMarkdownファイルをレンダリングします。), Markdown (リポジトリ一覧の出力形式であり、JekyllによってHTMLに変換されます。)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (プロジェクトの主要な開発言語として、リポジトリ情報の取得・処理・Markdown生成スクリプトが記述されています。), GitHub API (リポジトリ情報を取得するためのインターフェースです。), `config.yml` (リポジトリ一覧生成機能の動作設定や技術的パラメータを定義します。), `strings.yml` (ユーザー向けメッセージや文言を一元的に管理し、国際化や表示内容の変更を容易にします。)
- テスト: `pytest` (Python用のテスティングフレームワークで、コードの品質と信頼性を保証するための単体テストや統合テストの実行に使用されます。)
- ビルドツール: 該当するビルドツールはありません（Pythonスクリプトが直接Markdownファイルを生成します）。
- 言語機能: Python (オブジェクト指向プログラミング、標準ライブラリ、外部ライブラリの利用を通じて、システムのロジックが実装されています。)
- 自動化・CI/CD: GitHub Pages (生成されたリポジトリ一覧をウェブサイトとして公開するためのホスティング環境です。), `.github_automation` (GitHub Actionsなどの自動化スクリプトが格納され、CI/CDプロセスの一部として利用される可能性があります。)
- 開発標準: `ruff` (Pythonコードの高速なLinterおよびFormatterで、コードスタイルの一貫性を保ち、潜在的なバグを検出するのに役立ちます。), `.editorconfig` (異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。)

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
-   `.editorconfig`: 開発環境全体で一貫したコーディングスタイルを維持するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトを格納するディレクトリです。
    -   `check_large_files/`: 大容量ファイルのチェックに関連するツール群を格納します。
        -   `README.md`: `check_large_files` ディレクトリの目的と使用方法を説明します。
        -   `check-large-files.toml`: 大容量ファイルチェックツールの設定を定義します。
        -   `scripts/check_large_files.py`: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
-   `.gitignore`: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定します。
-   `LICENSE`: このプロジェクトがMITライセンスの下で公開されていることを示します。
-   `README.md`: プロジェクトの全体概要、目的、使い方、設定方法などが記述された主要なドキュメントです。
-   `_config.yml`: Jekyllサイトの設定ファイルで、サイトのテーマやプラグイン、変数を定義します。
-   `assets/`: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
-   `debug_project_overview.py`: プロジェクト概要の自動取得機能をデバッグするために使用されるスクリプトです。
-   `generated-docs/`: 生成されたドキュメントや一時的なファイルを格納するためのディレクトリとして利用されることが想定されます。
-   `googled947dc864c270e07.html`: Google Search Consoleなどでのサイト所有権確認のために配置される認証ファイルです。
-   `index.md`: GitHub PagesサイトのメインページとなるMarkdownファイルです。このファイルにリポジトリ一覧が生成されます。
-   `issue-notes/22.md`: 特定の課題（Issue #22）に関するメモや詳細情報が記述されているファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータや表示設定を定義するファイルです。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの動作設定を定義するファイルです。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonの依存パッケージをリストアップしています。
-   `requirements.txt`: プロジェクトの本番稼働に必要となるPythonの依存パッケージをリストアップしています。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールし、どのページを無視するかを指示するファイルです。
-   `ruff.toml`: Pythonコードのリンター・フォーマッターであるRuffの設定を定義するファイルです。
-   `src/`: プロジェクトの主要なソースコードが格納されるディレクトリです。
    -   `__init__.py`: `src` ディレクトリがPythonパッケージであることを示します。
    -   `generate_repo_list/`: リポジトリリストの生成ロジックをカプセル化したPythonパッケージです。
        -   `__init__.py`: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        -   `badge_generator.py`: リポジトリに表示するバッジ（例：言語、ステータス）を生成するロジックを扱います。
        -   `config.yml`: リポジトリリスト生成機能に特化した設定パラメータを定義します。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリーポイントであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために利用されるJSON-LD形式のテンプレートを格納します。
        -   `language_info.py`: GitHubリポジトリの言語に関する情報を処理し、表示に役立つデータに変換します。
        -   `markdown_generator.py`: 取得したリポジトリ情報をもとに、SEOに配慮したMarkdown形式の文字列を生成するロジックを実装しています。
        -   `project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要を自動的に取得するロジックを扱います。
        -   `readme_badge_extractor.py`: リポジトリのREADMEファイルから、既存のバッジ情報などを抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報に整形する役割を担います。
        -   `seo_template.yml`: SEO関連のメタデータや構造化データを生成するためのテンプレート設定を定義します。
        -   `statistics_calculator.py`: リポジトリに関する各種統計情報（例：スター数、フォーク数）を計算するロジックを提供します。
        -   `strings.yml`: アプリケーション内で使用される表示テキストやメッセージを一元管理し、多言語対応などを容易にします。
        -   `template_processor.py`: Markdownやその他の出力形式で使用するテンプレートを処理するための汎用的なロジックを提供します。
        -   `url_utils.py`: URLの操作や検証、生成に関するユーティリティ関数を提供します。
-   `test_project_overview.py`: プロジェクト概要取得機能のテストケースが記述されたスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: pytestのテスト実行時に共有されるフィクスチャやヘルパー関数を定義します。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合テストを記述します。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストを記述します。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテストを記述します。
    -   `test_date_formatter.py`: 日付フォーマットユーティリティのテストを記述します。
    -   `test_environment.py`: プロジェクトの実行環境に関連する設定や依存関係のテストを記述します。
    -   `test_integration.py`: プロジェクトの主要機能間の連携を検証する統合テストを記述します。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテストを記述します。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを記述します。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを記述します。
    -   `test_repository_processor.py`: リポジトリ情報処理ロジックのテストを記述します。

## 関数詳細説明
提供された情報からは個々の関数の詳細な役割、引数、戻り値、機能を明確に特定できませんでした。各ファイルの主な機能については「ファイル詳細説明」セクションをご参照ください。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-12 07:12:39 JST
