Last updated: 2026-11-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧のMarkdownファイルを自動生成します。
- これにより、検索エンジンによるサイトのクロールを促進し、リポジトリの可視性を高めます。
- 各リポジトリの概要自動取得や分類表示など、Jekyll/GitHub Pagesと連携した多彩な機能を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータ), Markdown (コンテンツ生成フォーマット)
- 音楽・オーディオ: 該当技術は使用していません。
- 開発ツール: Python (主要なプログラミング言語), Git (バージョン管理システム), GitHub API (リポジトリ情報取得)
- テスト: pytest (Python用テストフレームワーク)
- ビルドツール: なし (PythonスクリプトがMarkdownファイルを生成します)
- 言語機能: Python (オブジェクト指向プログラミング、標準ライブラリを活用)
- 自動化・CI/CD: GitHub Actions (大規模ファイルチェックなどの自動化処理に利用)
- 開発標準: ruff (Pythonコードのフォーマットとリンティング), .editorconfig (エディタ設定の統一)

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
- **.editorconfig**: 異なる開発環境間でのコーディングスタイル (インデント、改行コードなど) を統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsを用いた自動化スクリプト群を格納するディレクトリ。
    - **.github_automation/check_large_files/**: 大規模ファイルの存在をチェックする自動化機能のディレクトリ。
        - **.github_automation/check_large_files/README.md**: 大規模ファイルチェック機能に関する説明文書。
        - **.github_automation/check_large_files/check-large-files.toml**: 大規模ファイルチェックの設定（しきい値など）。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 大規模ファイルを実際に検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）。
- **README.md**: プロジェクトの概要、セットアップ方法、使い方などが記述されたメインのドキュメント。
- **_config.yml**: Jekyllのサイト全体設定ファイル。GitHub Pagesサイトの動作に影響を与えます。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリ。
    - **favicon-16x16.png**: 16x16ピクセルのファビコン画像。
    - **favicon-192x192.png**: 192x192ピクセルのファビコン画像。
    - **favicon-32x32.png**: 32x32ピクセルのファビコン画像。
    - **favicon-512x512.png**: 512x512ピクセルのファビコン画像。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプト。
- **generated-docs/**: 各リポジトリから自動取得されたプロジェクト概要ファイルが配置されることを想定したディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイル。
- **index.md**: `generate_repo_list.py`によってリポジトリ一覧が生成され、GitHub Pagesのトップページとして表示されるMarkdownファイル。
- **issue-notes/**: 課題や検討事項に関するメモを格納するディレクトリ。
    - **issue-notes/22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや検討内容。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイル。ホーム画面に追加されるアプリのメタデータを提供します。
- **pytest.ini**: pytestフレームワークのテスト設定ファイル。テストの検出方法や実行オプションを定義します。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストアップしたファイル。
- **requirements.txt**: 本番環境でプロジェクトを実行するために必要なPythonパッケージの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは除外するかを指示するファイル。
- **ruff.toml**: PythonコードのリンティングおよびフォーマットツールであるRuffの設定ファイル。コード品質とスタイルを統一します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **src/__init__.py**: Pythonパッケージとして`src`ディレクトリを認識させるためのファイル。
    - **src/generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するパッケージ。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`パッケージを初期化するためのファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの言語やスター数などのバッジ画像を生成するロジックが含まれています。
        - **src/generate_repo_list/config.yml**: プロジェクト概要取得機能などの技術的パラメータを設定するファイル。
        - **src/generate_repo_list/config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理する機能を提供します。
        - **src/generate_repo_list/date_formatter.py**: 日付情報を特定の形式にフォーマットするためのユーティリティが含まれています。
        - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインスクリプトです。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のためのJSON-LD形式のメタデータテンプレート。
        - **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理・表示するロジックが含まれています。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報からMarkdown形式のコンテンツを生成する機能を提供します。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動取得するロジックが含まれています。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能を提供します。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、必要な情報に加工するロジックが含まれています。
        - **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータ（タイトル、説明など）を定義するためのテンプレートファイル。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージや文言を国際化・一元管理するためのファイル。
        - **src/generate_repo_list/template_processor.py**: Jekyllのテンプレートエンジンと連携し、Markdownコンテンツを最終的な形式に加工する機能を提供します。
        - **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証などのユーティリティ関数が含まれています。
- **test_project_overview.py**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) の単体テストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **tests/conftest.py**: pytestの共通フィクスチャやヘルパー関数を定義するファイル。
    - **tests/test_badge_generator_integration.py**: バッジ生成機能の統合テスト。
    - **tests/test_check_large_files.py**: 大規模ファイルチェック機能のテスト。
    - **tests/test_config.py**: 設定ファイル管理機能のテスト。
    - **tests/test_date_formatter.py**: 日付フォーマット機能のテスト。
    - **tests/test_environment.py**: 実行環境に関するテスト。
    - **tests/test_integration.py**: プロジェクト全体の主要機能の統合テスト。
    - **tests/test_markdown_generator.py**: Markdown生成機能のテスト。
    - **tests/test_project_overview_fetcher.py**: プロジェクト概要取得機能の単体テスト。
    - **tests/test_readme_badge_extractor.py**: READMEバッジ抽出機能のテスト。
    - **tests/test_repository_processor.py**: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供された情報では個々の関数の具体的なシグネチャや詳細なリストは特定できませんでしたが、各ファイルの役割から以下の通り説明します。

- **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内で設定されたしきい値を超える大規模ファイルを検出するための主要な関数群が含まれています。
- **debug_project_overview.py**: プロジェクト概要の取得と表示機能をテスト・デバッグするためのエントリーポイント関数やヘルパー関数が含まれています。
- **googled947dc864c270e07.html**: このファイルはHTML形式であり、実行可能な関数は含まれていません。
- **src/generate_repo_list/badge_generator.py**: リポジトリの各種情報（言語、スター数など）からバッジのURLやMarkdownを生成する関数群が含まれています。
- **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`, `strings.yml`）をロードし、その値を管理・取得するための関数群が含まれています。
- **src/generate_repo_list/date_formatter.py**: 日付オブジェクトを人間が読める形式や特定の出力形式に変換する関数群が含まれています。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、その情報を加工して最終的なMarkdownファイルを生成するプロセス全体を制御する主要な関数群が含まれています。
- **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形に整形する関数群が含まれています。
- **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリデータに基づいて、Jekyll互換のMarkdown形式の文字列を構築する関数群が含まれています。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のパスにある`project-overview.md`ファイルからプロジェクト概要の3行説明を安全にフェッチする関数群が含まれています。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEコンテンツから既存のバッジ（シールドなど）の情報を解析・抽出する関数群が含まれています。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリオブジェクトを受け取り、プロジェクト内で扱いやすい形に変換・整形する関数群が含まれています。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する関数群が含まれています。
- **src/generate_repo_list/template_processor.py**: YAMLやJSONのテンプレートデータとリポジトリ情報を組み合わせて、出力コンテンツを生成する関数群が含まれています。
- **src/generate_repo_list/url_utils.py**: URLの構築、検証、エンコード・デコードなど、URL操作に関するユーティリティ関数群が含まれています。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュール内の関数が正しく動作するかを検証するためのテスト関数群が含まれています。
- **tests/conftest.py**: テスト実行時に共通で利用されるpytestのフィクスチャ（テストデータやセットアップ/ティアダウン処理）を定義する関数群が含まれています。
- **tests/test_badge_generator_integration.py**: `badge_generator.py`の統合テストケースを定義する関数群が含まれています。
- **tests/test_check_large_files.py**: 大規模ファイルチェックロジックが期待通りに機能するかを検証するテスト関数群が含まれています。
- **tests/test_config.py**: 設定ファイルの読み込み、デフォルト値の適用、値の取得などが正しく行われるかを検証するテスト関数群が含まれています。
- **tests/test_date_formatter.py**: 日付フォーマット関数が各種入力に対して正しく動作するかを検証するテスト関数群が含まれています。
- **tests/test_environment.py**: プロジェクトの実行環境（Pythonバージョン、依存関係など）が適切であるかを検証するテスト関数群が含まれています。
- **tests/test_integration.py**: 主要なコンポーネントが連携して正しく機能するかを検証する、より広範囲な統合テスト関数群が含まれています。
- **tests/test_markdown_generator.py**: Markdown生成関数が異なるリポジトリ情報に対して正しいMarkdownを生成するかを検証するテスト関数群が含まれています。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher.py`のロジックが、さまざまなシナリオ（ファイルが存在しない、形式が異なるなど）で正しく機能するかを検証するテスト関数群が含まれています。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor.py`の関数がREADMEから正確にバッジ情報を抽出できるかを検証するテスト関数群が含まれています。
- **tests/test_repository_processor.py**: `repository_processor.py`の関数がGitHub APIのレスポンスを正しく処理・整形できるかを検証するテスト関数群が含まれています。

## 関数呼び出し階層ツリー
```
提供された情報では関数呼び出し階層を特定できませんでした。

---
Generated at: 2026-11-10 07:07:14 JST
