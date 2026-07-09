Last updated: 2026-07-10

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で取得するシステムです。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧Markdownを生成します。
- これにより、GitHub Pagesの検索エンジン可視性を向上させ、LLMからの参照性も高めます。

## 技術スタック
- フロントエンド: GitHub Pages, Jekyll, Markdown
    - 説明: GitHub Pagesは静的サイトホスティングサービスであり、JekyllはMarkdownなどのテキストからウェブサイトを生成するエンジンです。本プロジェクトはJekyllが解釈可能なMarkdownファイルを生成し、これによりウェブサイトとして公開されます。
- 音楽・オーディオ: (該当なし)
    - 説明: このプロジェクトでは音楽やオーディオ関連の技術は使用していません。
- 開発ツール: Python, GitHub API
    - 説明: Pythonはプロジェクトのメインスクリプト言語として使用され、リポジトリ情報の取得にはGitHub APIを利用しています。
- テスト: pytest
    - 説明: Pythonのテストフレームワークであるpytestを使用し、コードの機能が意図通りに動作することを検証しています。
- ビルドツール: (直接的なビルドツールはなし)
    - 説明: 特定のビルドツールは使用せず、Pythonスクリプトが直接Markdownファイルを生成します。最終的なウェブサイトのビルドおよびデプロイはGitHub PagesのJekyll機能に依存します。
- 言語機能: Python, YAML, TOML
    - 説明: プロジェクトの主要な開発言語はPythonです。設定ファイルにはYAML (`config.yml`, `strings.yml`など) が、秘密情報や詳細な設定にはTOML (`secrets.toml`, `ruff.toml`など) が使われています。
- 自動化・CI/CD: (ローカル開発重視)
    - 説明: 本プロジェクトはCI/CDを必須とせず、ローカルでの開発と実行を重視しています。ただし、生成されたコンテンツの公開はGitHub Pages上で行われるため、広義ではGitHub Actionsなどの自動化連携が想定されます。
- 開発標準: ruff
    - 説明: Pythonコードのリンティングとフォーマットを高速に行うツールであるruffを使用し、コードの一貫性と品質を維持するための開発標準を定めています。

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

*   **.editorconfig**: さまざまなエディタやIDEで一貫したコーディングスタイルを定義するための設定ファイルです。
*   **.github_automation/**: GitHub Actionsなどの自動化プロセスに関連するスクリプトや設定を含むディレクトリです。
    *   **check_large_files/README.md**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    *   **check_large_files/check-large-files.toml**: 大容量ファイルチェックツールの設定ファイルです。
    *   **check_large_files/scripts/check_large_files.py**: 指定されたサイズを超えるファイルを検出するPythonスクリプトです。
*   **.gitignore**: Gitでバージョン管理しないファイルやディレクトリを指定するファイルです。
*   **LICENSE**: 本プロジェクトのライセンス（MITライセンス）に関する情報が記述されています。
*   **README.md**: プロジェクトの概要、目的、主な機能、使い方、開発者向けのヒントなどが記述されたメインドキュメントです。
*   **_config.yml**: Jekyllサイト全体の構成設定を定義するファイルです。
*   **assets/**: ウェブサイトで使用される画像やアイコンなどのアセットを格納するディレクトリです。
    *   **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の異なるサイズです。
*   **debug_project_overview.py**: プロジェクト概要取得機能（`project_overview_fetcher`）のデバッグやテストを目的としたスクリプトです。
*   **generated-docs/**: 各リポジトリから取得されるプロジェクト概要ファイルが一時的に格納される可能性のあるディレクトリです。
*   **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
*   **index.md**: 生成されたリポジトリ一覧がMarkdown形式で出力され、GitHub Pagesのメインページとして機能するファイルです。
*   **issue-notes/**: 開発中に発生した課題や検討事項をメモするディレクトリです。
    *   **22.md**: 特定の課題（Issue #22）に関する詳細なメモや議論が記述されています。
*   **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン利用などの機能を提供します。
*   **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。
*   **requirements-dev.txt**: 開発時およびテスト時に必要なPythonライブラリの一覧を定義するファイルです。
*   **requirements.txt**: プロジェクトの実行に必要な本番環境用のPythonライブラリの一覧を定義するファイルです。
*   **robots.txt**: 検索エンジンクローラーに対し、サイトのどの部分をクロールすべきか、あるいはすべきでないかを指示するファイルです。
*   **ruff.toml**: Pythonのコードリンター/フォーマッターであるruffの設定ファイルです。
*   **src/**: プロジェクトのソースコードを格納するメインディレクトリです。
    *   **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するディレクトリです。
        *   **badge_generator.py**: リポジトリのバッジ画像（例: 言語、ライセンスなど）を生成または処理する機能を提供します。
        *   **config.yml**: プロジェクト概要取得機能などの技術的なパラメータや設定を定義するファイルです。
        *   **config_manager.py**: 設定ファイル（`config.yml`など）の読み込み、管理、およびアクセスを提供するモジュールです。
        *   **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        *   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式でリポジトリ一覧を生成するメインスクリプトです。
        *   **json_ld_template.json**: 検索エンジン最適化（SEO）のために使用される構造化データ（JSON-LD）のテンプレートです。
        *   **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・表示するためのロジックを含みます。
        *   **markdown_generator.py**: 取得したリポジトリ情報に基づいて、GitHub Pages用のMarkdownコンテンツを生成するロジックを提供します。
        *   **project_overview_fetcher.py**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で取得・抽出する機能を提供します。
        *   **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ（shields.ioなど）の情報を抽出するモジュールです。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリ情報を整形し、Markdown生成に適した形式に変換する主要な処理を行います。
        *   **seo_template.yml**: SEO関連のメタデータやテンプレート設定を定義するファイルです。
        *   **statistics_calculator.py**: リポジトリに関する統計情報（スター数、フォーク数など）を計算する機能を提供します。
        *   **strings.yml**: ウェブサイトに表示される各種メッセージ、ラベル、文言などを一元管理するファイルです。
        *   **template_processor.py**: Markdownテンプレートを読み込み、リポジトリ情報で埋め込んで最終的なコンテンツを生成するモジュールです。
        *   **url_utils.py**: URLの検証、整形、生成など、URLに関連するユーティリティ関数を提供します。
*   **test_project_overview.py**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
*   **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    *   **conftest.py**: pytestのテスト実行時に使用される共通のフィクスチャやヘルパー関数を定義するファイルです。
    *   **test_badge_generator_integration.py**: `badge_generator`モジュールの結合テストを行います。
    *   **test_check_large_files.py**: 大容量ファイルチェック機能のテストを行います。
    *   **test_config.py**: 設定管理（`config_manager`）関連のモジュールのテストを行います。
    *   **test_date_formatter.py**: 日付フォーマットユーティリティのテストを行います。
    *   **test_environment.py**: 実行環境に関するテストを行います。
    *   **test_integration.py**: プロジェクトの主要機能間の結合テストを行います。
    *   **test_markdown_generator.py**: Markdown生成モジュールのテストを行います。
    *   **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテストを行います。
    *   **test_readme_badge_extractor.py**: READMEからのバッジ抽出モジュールのテストを行います。
    *   **test_repository_processor.py**: リポジトリ情報処理モジュールのテストを行います。

## 関数詳細説明
プロジェクト情報から具体的な関数名、引数、戻り値の詳細は特定できませんでしたが、各ファイルが担う役割に基づいて主要な機能として説明します。

*   **src/generate_repo_list/generate_repo_list.py**: このファイルはプロジェクトのメインエントリスクリプトです。GitHub APIを通じてリポジトリ情報を取得し、取得したデータを処理して、指定された出力ファイル名でMarkdown形式のリポジトリ一覧を生成します。コマンドライン引数 (`--username`, `--output`, `--limit`など) を解析し、全体の処理フローを orchestrate します。
*   **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内に存在する特定のファイル (`generated-docs/project-overview.md`など) から、プロジェクトの概要説明を抽出し、返却する機能を提供します。GitHub APIを介してファイルのコンテンツを取得し、指定されたセクション（例: "プロジェクト概要"）から3行の要約を解析します。
*   **src/generate_repo_list/markdown_generator.py**: `repository_processor`によって整形されたリポジトリ情報と各種設定（`strings.yml`, `seo_template.yml`など）を元に、最終的なMarkdownコンテンツを構築します。Jekyllが適切にレンダリングできるように、SEO最適化された形式で情報を埋め込みます。
*   **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を受け取り、それをプロジェクト内で使いやすい形式（例: Pythonのオブジェクトや辞書）に変換・整形する役割を担います。これにより、他のモジュールが簡潔にリポジトリ情報を利用できるようになります。
*   **src/generate_repo_list/badge_generator.py**: リポジトリの言語やライセンスなどの属性に基づいた視覚的なバッジ（アイコン）の情報を生成または管理します。これらのバッジは生成されるMarkdownファイルに組み込まれ、リポジトリの特徴を一目で示すのに役立ちます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-10 07:32:46 JST
