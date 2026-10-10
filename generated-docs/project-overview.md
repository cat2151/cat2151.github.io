Last updated: 2026-10-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得してGitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジン最適化されたリポジトリ一覧ページと個別リポジトリへのリンクを公開し、検索性向上に貢献します。
- プロジェクト概要の自動取得、バッジ表示、多様な分類機能などを備え、Jekyll/GitHub Pagesに対応しています。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesがコンテンツをレンダリングするために利用)
- 音楽・オーディオ: 特になし
- 開発ツール:
    - Python: プロジェクトの主要開発言語
    - pytest: テストフレームワーク
    - ruff: Pythonコードのリンターおよびフォーマッター
    - Git: ソースコードのバージョン管理
- テスト:
    - pytest: Pythonコードの単体テストおよび結合テストを実行するためのフレームワーク
- ビルドツール:
    - Pythonスクリプト: GitHub APIから取得した情報に基づきMarkdownファイルを生成するカスタムスクリプト
- 言語機能:
    - Pythonの標準ライブラリ: ファイル操作、文字列処理、JSON処理など
    - requests: HTTPリクエストを送信し、GitHub APIと通信するためのライブラリ
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`など) を読み込むためのライブラリ
    - toml: TOML形式の設定ファイル (`secrets.toml`, `check-large-files.toml`など) を読み込むためのライブラリ
    - beautifulsoup4: HTMLやXML、あるいはMarkdownからデータを抽出・解析するために使用されます (特にプロジェクト概要の抽出時に利用される可能性)
    - furl: URLのパース、操作、構築を容易にするライブラリ
- 自動化・CI/CD:
    - GitHub API連携: リポジトリ情報の自動取得に利用
    - (注: 本プロジェクト自体は「CI/CD不要のローカル開発重視」と明記されており、専用のCI/CDツールは使用していません。)
- 開発標準:
    - ruff: Pythonコードのスタイルガイド強制および静的解析ツール
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル

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
- **.editorconfig**: 異なるエディタやIDE間で、インデントスタイル、文字コードなどの基本的なコーディングスタイルを一貫させるための設定ファイル。
- **.github_automation/**: GitHub Actionsや自動化スクリプトに関連するファイルを格納するディレクトリ。
    - **.github_automation/check_large_files/**: 大容量ファイルチェック機能に関連するディレクトリ。
        - **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能に関する説明文書。
        - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の設定ファイル。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報 (MITライセンス) を記載したファイル。
- **README.md**: プロジェクトの概要、セットアップ方法、使い方、開発者向け情報などをまとめた主要な説明文書。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。GitHub Pagesの動作に影響を与えます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    - **assets/favicon-*.png**: Webサイトのファビコン（ブラウザタブなどに表示される小さなアイコン）ファイル。様々なサイズが用意されています。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグ用途で使用される補助スクリプト。
- **generated-docs/**: プロジェクト実行時に生成されるMarkdownファイルやドキュメントを一時的または永続的に格納するためのディレクトリ。
- **googled947dc864c270e07.html**: Google Search ConsoleでWebサイトの所有権を確認するために配置されるHTMLファイル。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。本プロジェクトで生成されたリポジトリ一覧がここに出力されます。
- **issue-notes/**: GitHub Issuesに関連するメモや詳細情報をMarkdown形式で保存するディレクトリ。
    - **issue-notes/22.md**: 特定のIssue（例: Issue #22）に関する詳細なノートや考察を記述したファイル。
- **manifest.json**: Webアプリケーションマニフェスト。プログレッシブウェブアプリ (PWA) の設定や、ホーム画面に追加した際のアイコン、表示名などを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を定義するファイル。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを記載したファイル。
- **requirements.txt**: プロジェクトを本番環境で実行するために必要なPythonパッケージとそのバージョンを記載したファイル。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、どのページをクロールすべきか、どのページを避けるべきかなどを指示するファイル。
- **ruff.toml**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや静的解析のルールを定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイル。
    - **src/generate_repo_list/**: GitHubリポジトリ一覧を生成する主要なロジックを格納するパッケージ。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの言語やスター数などの情報を基に、表示用のバッジ（アイコン）を生成するロジックを実装したファイル。
        - **src/generate_repo_list/config.yml**: リポジトリ一覧生成機能固有の動作設定を定義するYAML形式のファイル（例: プロジェクト概要取得機能の有効・無効、対象ファイルパスなど）。
        - **src/generate_repo_list/config_manager.py**: `config.yml`や`secrets.toml`などの様々な設定ファイルを読み込み、管理するためのモジュール。
        - **src/generate_repo_list/date_formatter.py**: リポジトリの最終更新日時などを、人間が読みやすい形式に整形するための日付フォーマットロジックを提供するファイル。
        - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を調整・実行します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジンのSEOを強化するためのJSON-LD形式の構造化データテンプレート。
        - **src/generate_repo_list/language_info.py**: リポジトリが使用しているプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するロジック。
        - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報に基づいて、最終的なMarkdownコンテンツを構築・生成するロジック。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリから`generated-docs/project-overview.md`ファイルを読み込み、プロジェクトの3行概要を抽出する機能を提供するファイル。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリの`README.md`ファイルから、特定のパターンに一致するバッジ情報を抽出するためのロジック。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、アプリケーション内で扱いやすい形式に加工・処理するロジック。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化 (SEO) のためのメタデータやテンプレート設定を定義するYAMLファイル。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、オープンイシュー数などの統計情報を計算・集計するロジック。
        - **src/generate_repo_list/strings.yml**: UIに表示される各種メッセージや文言、翻訳可能な文字列などを一元的に管理するためのYAMLファイル。
        - **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレートを処理し、動的なデータを埋め込んで最終的なコンテンツをレンダリングするロジック。
        - **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ機能を提供するファイル。
- **test_project_overview.py**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **tests/conftest.py**: pytestのフィクスチャ、ヘルパー関数、テスト設定などを定義するファイル。テスト間で共通のセットアップを提供します。
    - **tests/test_badge_generator_integration.py**: `badge_generator`モジュールと他のコンポーネントとの連携を検証する統合テストスクリプト。
    - **tests/test_check_large_files.py**: `.github_automation/check_large_files.py`スクリプトの機能が期待通りに動作するかを検証するテスト。
    - **tests/test_config.py**: `config_manager`モジュールや設定ファイルの読み込みが正しく行われるかを検証するテスト。
    - **tests/test_date_formatter.py**: `date_formatter`モジュールの日付整形機能が正しく動作するかを検証するテスト。
    - **tests/test_environment.py**: プロジェクトの実行環境が正しく設定されているか、必要な依存関係が満たされているかなどを検証するテスト。
    - **tests/test_integration.py**: プロジェクトの主要なフローやモジュール間の連携を広範囲にわたって検証する統合テスト。
    - **tests/test_markdown_generator.py**: `markdown_generator`モジュールが正しいMarkdownコンテンツを生成するかを検証するテスト。
    - **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールがプロジェクト概要を正しく取得・解析できるかを検証するテスト。
    - **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正しく抽出できるかを検証するテスト。
    - **tests/test_repository_processor.py**: `repository_processor`モジュールがGitHub APIからのリポジトリデータを正しく処理・変換できるかを検証するテスト。

## 関数詳細説明
具体的な関数の詳細なシグネチャ、引数、戻り値は提供された情報からは特定できませんでしたが、各ファイルがPythonモジュールとして機能するため、その役割に基づいて以下の種類の関数が含まれていると推測されます。

- **generate_repo_list.py**: リポジトリ情報の取得、処理、Markdown生成全体をオーケストレーションする`main`関数や、主要な処理を担う関数群。
- **badge_generator.py**: リポジトリの特定の属性（言語、スター数など）から視覚的なバッジ情報を生成する関数。
- **config_manager.py**: 設定ファイル（`config.yml`, `secrets.toml`など）を読み込み、特定の設定値を取得する関数。
- **date_formatter.py**: 日付オブジェクトを受け取り、特定のフォーマット文字列に従って整形された日付文字列を返す関数。
- **language_info.py**: リポジトリの言語データを解析し、主要言語やその使用率などを算出・表示するための関数。
- **markdown_generator.py**: 構造化されたデータを受け取り、それをMarkdown形式の文字列に変換して出力する関数群。
- **project_overview_fetcher.py**: GitHub APIを通じてリモートリポジトリから`project-overview.md`をフェッチし、そこから概要テキストを抽出する関数。
- **repository_processor.py**: GitHub APIのレスポンス（生のJSONデータ）を受け取り、それをPythonオブジェクトにマッピングし、必要に応じてデータを正規化・加工する関数群。
- **statistics_calculator.py**: リポジトリデータからスター数、フォーク数、最終コミット日時などの統計情報を計算する関数。
- **template_processor.py**: テンプレートファイル（Markdownの一部など）とデータを組み合わせて最終的なコンテンツを生成する関数。
- **url_utils.py**: GitHubリポジトリのURLやAPIエンドポイントなど、URLの構築や解析を行う補助関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-11 07:12:23 JST
