Last updated: 2026-02-16

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・整理するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- GitHubユーザーページのリポジトリが検索エンジンにクロールされにくい課題を解決し、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして機能し、生成されたMarkdownファイルをHTMLとして表示), **Markdown** (リポジトリ一覧の出力形式であり、Jekyllがこれを処理してウェブページを生成します)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (主要なスクリプト言語として、GitHub APIからのデータ取得、処理、Markdown生成、設定管理などを行います), **GitHub API** (リポジトリ情報の取得元として利用されます)
- テスト: **pytest** (Pythonコードの単体テストおよび結合テストを行うためのテストフレームワークです)
- ビルドツール: **Python** (スクリプトの実行によってMarkdownファイルを生成する役割を担います)
- 言語機能: **Python** (プロジェクトのコアロジックを実装するためのプログラミング言語です)
- 自動化・CI/CD: **GitHub Actions** (`.github_automation` ディレクトリの存在から、コード品質チェックやファイルサイズの監視などの自動化ワークフローがGitHub Actionsで実行されている可能性が高いです)
- 開発標準: **ruff** (Pythonコードの高速リンター/フォーマッターとして、コードスタイルの一貫性を保ち、潜在的な問題を検出します), **.editorconfig** (異なるエディタやIDE間でコーディングスタイルを統一するための設定ファイルです)

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
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
  📖 18.md
  📖 2.md
  📖 20.md
  📖 4.md
  📖 6.md
  📖 8.md
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
-   `.editorconfig`: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   `.github_automation/`: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定を格納するディレクトリです。
    -   `check_large_files/README.md`: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    -   `check_large_files/check-large-files.toml`: 大きいファイルチェック機能の設定を定義するTOMLファイルです。
    -   `check_large_files/scripts/check_large_files.py`: リポジトリ内の特定の種類の大きいファイルを検出し、潜在的な問題を報告するためのPythonスクリプトです。
-   `.gitignore`: Gitでバージョン管理の対象外とすべきファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
-   `README.md`: プロジェクトの概要、目的、主な機能、使用方法、設定など、プロジェクト全体の詳細を説明するメインのドキュメントです。
-   `_config.yml`: Jekyllサイト全体の設定ファイルであり、GitHub Pagesの動作やウェブサイトのメタデータ、テーマなどを制御します。
-   `assets/`: ウェブサイトで使用される画像、アイコン、フォントなどの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   `debug_project_overview.py`: プロジェクト概要自動取得機能の動作確認やデバッグを目的としたスクリプトです。
-   `generated-docs/`: 他のリポジトリから取得されたプロジェクト概要ファイルや、一時的に生成されるドキュメントが格納される可能性のあるディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのウェブマスターツールでサイトの所有権を認証するために使用されるHTMLファイルです。
-   `index.md`: プロジェクトのメインスクリプトによって自動生成されるリポジトリ一覧が記述されるMarkdownファイルであり、GitHub Pagesのトップページとして表示されます。
-   `issue-notes/`: 開発中の課題、決定事項、検討中のアイデアなどをMarkdown形式で記録したメモファイル群を格納するディレクトリです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供するウェブサイトで、アプリの表示設定（ホーム画面への追加、アイコンなど）を定義するファイルです。
-   `pytest.ini`: `pytest` テストフレームワークの動作を設定するための設定ファイルです。
-   `requirements-dev.txt`: 開発環境およびテスト実行時に必要となるPythonパッケージの依存関係をリスト化したファイルです。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行するために最低限必要なPythonパッケージの依存関係をリスト化したファイルです。
-   `robots.txt`: 検索エンジンクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイルです。
-   `ruff.toml`: `ruff` コードリンターおよびフォーマッターの動作を設定するためのTOMLファイルです。
-   `src/__init__.py`: `src` ディレクトリをPythonパッケージとして識別するためのファイルです。
-   `src/generate_repo_list/`: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージです。
    -   `__init__.py`: `generate_repo_list` パッケージをPythonパッケージとして識別するためのファイルです。
    -   `badge_generator.py`: リポジトリの言語バッジやライセンスバッジなどの表示用マークダウンを生成するロジックを扱います。
    -   `config.yml`: `generate_repo_list` モジュールの特定の動作（例: プロジェクト概要取得機能の設定）を制御する設定ファイルです。
    -   `config_manager.py`: 設定ファイル（`config.yml`など）の読み込み、解析、および管理を行うモジュールです。
    -   `date_formatter.py`: 日付や時刻の情報を特定のフォーマットに変換するためのユーティリティ関数を提供します。
    -   `generate_repo_list.py`: このプロジェクトのメイン実行スクリプトであり、GitHub APIから情報を取得し、リポジトリデータを処理し、最終的なMarkdownファイルを生成する一連のプロセスを統括します。
    -   `json_ld_template.json`: JSON-LD形式の構造化データ（ウェブページのコンテンツに関する情報を検索エンジンに伝えるためのデータ）のテンプレートを提供し、SEOを強化します。
    -   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つデータを提供します。
    -   `markdown_generator.py`: 取得・処理されたリポジトリ情報から、GitHub Pages向けの整形されたMarkdownコンテンツを生成するロジックを実装しています。
    -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得・抽出する機能を担当します。
    -   `readme_badge_extractor.py`: 各リポジトリのREADMEファイル内から、特定のバッジ（ステータスバッジなど）の情報を抽出するロジックを提供します。
    -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、表示や処理に適した形式に整形・フィルタリングするロジックを扱います。
    -   `seo_template.yml`: 検索エンジン最適化（SEO）のためのメタデータや構造化データを生成する際のテンプレート設定を定義します。
    -   `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、表示に利用するためのモジュールです。
    -   `strings.yml`: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理し、国際化/地域化を容易にするためのファイルです。
    -   `template_processor.py`: Jekyllのテンプレート機能や、その他の汎用的なテキストテンプレート処理を行うためのモジュールです。
    -   `url_utils.py`: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py` モジュールに特化した単体テストまたは結合テストを行うスクリプトです。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリです。
    -   `test_badge_generator_integration.py`: バッジ生成機能の統合的な動作を確認するテストスクリプトです。
    -   `test_check_large_files.py`: 大きいファイルチェック機能のテストスクリプトです。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みと管理ロジックのテストスクリプトです。
    -   `test_date_formatter.py`: 日付フォーマットユーティリティのテストスクリプトです。
    -   `test_environment.py`: 実行環境に関する前提条件や設定のテストスクリプトです。
    -   `test_integration.py`: システム全体の主要なフローや機能の統合テストを記述したスクリプトです。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテストスクリプトです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストスクリプトです。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストスクリプトです。
    -   `test_repository_processor.py`: リポジトリデータ処理ロジックのテストスクリプトです。

## 関数詳細説明
提供された情報では個々の関数の具体的なシグネチャ（引数、戻り値）や詳細な処理内容が明示されていません。
しかし、各ファイル名とその役割から、以下のPythonモジュールにはそれぞれ関連する機能を持つ関数群が含まれていると推測されます。

-   **`src/generate_repo_list/generate_repo_list.py`**: メインの実行ロジックを含むため、GitHub APIからのリポジトリ情報の取得、取得したデータの加工・フィルタリング、Markdownコンテンツの生成、ファイルへの書き出しなどを統括する関数が含まれています。
-   **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やライセンスを示すバッジの生成に関連する関数群が含まれています。
-   **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`や`strings.yml`など）を読み込み、設定値にアクセスするための関数が含まれています。
-   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻データを指定された形式に変換するためのユーティリティ関数が含まれています。
-   **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語情報を処理し、表示に適した形式にするための関数が含まれています。
-   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報やプロジェクト概要情報から、構造化されたMarkdown文字列を生成する関数群が含まれています。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: リモートリポジトリの特定のパスからファイル内容を取得し、そこからプロジェクト概要の3行説明を抽出する関数が含まれています。
-   **`src/generate_repo_list/readme_badge_extractor.py`**: READMEファイルの内容から、既存のバッジ情報を解析・抽出する関数が含まれています。
-   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報のみを抽出し、ソートやフィルタリングを行う関数群が含まれています。
-   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算する関数が含まれています。
-   **`src/generate_repo_list/template_processor.py`**: MarkdownやJSON-LDのテンプレートに動的なデータを差し込む処理を行う関数が含まれています。
-   **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリやGitHub PagesサイトへのURLを生成、検証、または操作するユーティリティ関数が含まれています。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大きいファイルを検出・報告するためのメイン処理関数や補助関数が含まれています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-02-16 07:07:16 JST
