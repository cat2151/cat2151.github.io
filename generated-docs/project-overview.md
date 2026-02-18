Last updated: 2026-02-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身の公開リポジトリ情報を自動的に収集します。
- 収集した情報に基づき、JekyllベースのGitHub Pagesサイト向けに最適化されたMarkdown形式のリポジトリ一覧ページを生成します。
- これにより、プロジェクトの検索エンジンでの可視性を高め、LLMによるリポジトリ参照の精度向上を支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトのレンダリングエンジンとして、生成されたMarkdownファイルを美しいWebページに変換します)
- 音楽・オーディオ: 該当なし（このプロジェクトの範疇外です）
- 開発ツール:
    - Python: プロジェクトの主要な開発言語として、リポジトリ情報の取得、処理、Markdown生成に利用されます。
    - Git: ソースコードのバージョン管理システムとして利用され、GitHubとの連携を容易にします。
    - pytest: Pythonで書かれたテストコードを実行するためのテストフレームワークです。
    - Ruff: Pythonコードのスタイルを自動的にチェックし、整形するための高速なリンター兼フォーマッターです。
    - PyYAML: YAML形式の設定ファイル（`config.yml`, `strings.yml` など）をPythonで扱うためのライブラリです。
- テスト: pytest (プロジェクトの品質と機能の正確性を保証するための単体・統合テストの実行に用いられます)
- ビルドツール: 該当なし (JekyllはGitHub Pages側で動作するため、本プロジェクト自体はMarkdown生成が主な役割です)
- 言語機能: Python (汎用的なプログラミング言語として、データ処理、API連携、ファイル操作など多岐にわたる機能を提供します)
- 自動化・CI/CD:
    - GitHub API: リポジトリのメタデータやコンテンツをプログラム的に取得するために使用されます。
    - GitHub Automation scripts: `check_large_files.py` のような補助的な自動化スクリプトが含まれ、開発ワークフローをサポートします。
- 開発標準:
    - Ruff: コードの品質と一貫性を保つためのPythonコードスタイルガイドラインを適用します。
    - Markdown: プロジェクトのドキュメントや生成されるリポジトリ一覧のコンテンツ記述に広く使用される軽量マークアップ言語です。

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  18.md
  2.md
  20.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_badge_generator_integration.py
  test_check_large_files.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードスタイル（インデント、改行コードなど）の一貫性を維持するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプト関連のファイルを格納するディレクトリです。
    -   **`check_large_files/`**: 大容量ファイルのチェックに関する機能を集めたディレクトリです。
        -   **`README.md`**: `check_large_files` 機能の説明文書です。
        -   **`check-large-files.toml`**: 大容量ファイルチェックの設定をTOML形式で定義するファイルです。
        -   **`scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
-   **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義するファイルです。
-   **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）を記述したファイルです。
-   **`README.md`**: プロジェクト全体の概要、セットアップ方法、使い方、開発者向け情報などをまとめたメインのドキュメントファイルです。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体のグローバルな設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどを設定します。
-   **`assets/`**: Webサイトで使用される画像、アイコン、CSSファイルなどの静的アセットを格納するディレクトリです。
    -   **`favicon-*.png`**: Webサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の様々なサイズを格納しています。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストを目的としたスクリプトです。
-   **`generated-docs/`**: 他のリポジトリから取得した概要や、自動生成されたドキュメントを一時的または恒久的に格納するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search ConsoleでWebサイトの所有権を確認するために使用されるHTMLファイルです。
-   **`index.md`**: 本プロジェクトによって自動生成される、リポジトリ一覧のメインのMarkdownファイルです。JekyllによってHTMLに変換され、サイトのトップページとなります。
-   **`issue-notes/`**: 課題や検討事項、特定のイシューに関するメモをMarkdown形式で記述したファイルを格納するディレクトリです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）として動作するためのメタデータを提供するJSONファイルです。アプリ名、アイコン、表示設定などを定義します。
-   **`pytest.ini`**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイルです。
-   **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてもよいか、またはクロールしないかを指示するファイルです。
-   **`ruff.toml`**: Pythonコードのリンター兼フォーマッターであるRuffの設定ファイルです。コードスタイルルールや無視するファイルを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`generate_repo_list/`**: リポジトリ一覧を生成する核心的なロジックをまとめたPythonパッケージです。
        -   **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジを生成または管理する機能を提供します。
        -   **`config.yml`**: `generate_repo_list` スクリプトの動作を制御する技術的パラメータ（例: APIリトライ設定、キャッシュ設定）を定義するファイルです。
        -   **`config_manager.py`**: 各種設定ファイル（`config.yml`, `strings.yml`など）を読み込み、アプリケーション全体で利用可能にするための設定管理機能を提供します。
        -   **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する処理全体を統括します。
        -   **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        -   **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を取得・処理する機能を提供します。
        -   **`markdown_generator.py`**: リポジトリデータから、最終的な`index.md`に組み込むためのMarkdownコンテンツを生成する機能を提供します。
        -   **`project_overview_fetcher.py`**: 各リポジトリ内の`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出する機能を提供します。
        -   **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出する機能を提供します。
        -   **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、分類（アクティブ、アーカイブ、フォークなど）する主要な処理ロジックを提供します。
        -   **`seo_template.yml`**: JekyllのFront Matterやその他のSEO関連のメタデータを生成するためのテンプレート設定を定義するファイルです。
        -   **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        -   **`strings.yml`**: UIに表示されるメッセージ、ラベル、その他のテキスト文字列を管理するためのYAMLファイルです。多言語対応や文言の一元管理に利用されます。
        -   **`template_processor.py`**: Markdownや他のテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成する機能を提供します。
        -   **`url_utils.py`**: URLの生成、解析、検証などの汎用的なURL関連ユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` の機能が正しく動作するかを検証するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体の各種テストスクリプトを格納するディレクトリです。
    -   **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストを行うスクリプトです。
    -   **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストを行うスクリプトです。
    -   **`test_config.py`**: 設定管理機能が正しく動作するかをテストするスクリプトです。
    -   **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストを行うスクリプトです。
    -   **`test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係のテストを行うスクリプトです。
    -   **`test_integration.py`**: プロジェクトの主要コンポーネント間の連携を検証する統合テストスクリプトです。
    -   **`test_markdown_generator.py`**: Markdown生成機能の正確性をテストするスクリプトです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストを行うスクリプトです。
    -   **`test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストを行うスクリプトです。
    -   **`test_repository_processor.py`**: リポジトリデータ処理機能のテストを行うスクリプトです。

## 関数詳細説明
-   **`generate_repo_list.py`**:
    -   **`main()`**: プログラムのエントリーポイント。コマンドライン引数をパースし、リポジトリ情報の取得、処理、Markdown生成、ファイル出力までの一連の流れを orchestrate します。
    -   **`_get_github_token()`**: GitHub APIへの認証に必要なトークンを安全な方法で取得する内部ヘルパー関数です。
    -   **`_fetch_repositories(username, limit, token)`**: 指定されたGitHubユーザー名のリポジトリ情報をGitHub API経由で取得します。必要に応じて取得数に制限を設けることができます。
    -   **`_process_repositories(repo_data, config, strings)`**: 取得した生のリポジトリデータを整形し、追加情報（概要、言語、統計など）を付与して、Markdown生成に適した形式に加工します。
    -   **`_generate_output_markdown(processed_repos, config, strings)`**: 処理済みのリポジトリデータと設定に基づいて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
-   **`badge_generator.py`**:
    -   **`generate_badge(badge_info)`**: 入力されたバッジ情報（テキスト、色など）に基づき、Webページに表示するためのバッジ（例: Shields.io形式）のURLやマークアップを生成します。
-   **`config_manager.py`**:
    -   **`load_config(config_path)`**: 指定されたYAML形式のファイルパスから設定情報を読み込み、Pythonの辞書オブジェクトとして返します。
    -   **`get_setting(config, key_path, default=None)`**: 読み込んだ設定辞書から、ドット区切りパス（例: `"project_overview.enabled"`）で指定された特定の設定値を取得します。
-   **`date_formatter.py`**:
    -   **`format_date_for_display(datetime_obj, format_str="%Y-%m-%d")`**: datetimeオブジェクトを受け取り、指定されたフォーマット文字列に従って、読みやすい日付文字列に変換します。
-   **`markdown_generator.py`**:
    -   **`create_repository_section(repo_data, config, strings)`**: 単一のリポジトリの情報を基に、そのリポジトリ専用のMarkdownセクション（タイトル、説明、バッジ、リンクなど）を生成します。
    -   **`create_repo_list_markdown(all_repo_data, config, strings)`**: 複数のリポジトリセクションを統合し、`index.md`として出力される最終的なリポジトリ一覧のMarkdownコンテンツを構成します。
-   **`project_overview_fetcher.py`**:
    -   **`fetch_project_overview(repo_name, github_token, config)`**: 指定されたリポジトリ名とGitHubトークン、設定に基づき、そのリポジトリの`generated-docs/project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出し返します。
-   **`repository_processor.py`**:
    -   **`process_repo_data(repo, config, github_token)`**: GitHub APIから取得した個々の生のリポジトリデータ辞書を受け取り、必要な情報を抽出し、整形し、さらに`project_overview_fetcher`などを用いて追加情報を付与します。
    -   **`classify_repository(repo)`**: リポジトリのプロパティ（例: `archived`, `fork`）に基づいて、そのリポジトリが「アクティブ」「アーカイブ」「フォーク」のいずれであるかを分類します。

## 関数呼び出し階層ツリー
```
main()
├── _get_github_token()
├── _fetch_repositories()
│   └── (GitHub API 呼び出し)
├── _process_repositories()
│   ├── repository_processor.process_repo_data()
│   │   └── project_overview_fetcher.fetch_project_overview() (オプション)
│   ├── repository_processor.classify_repository()
│   ├── language_info.get_language_details() (推測)
│   └── statistics_calculator.calculate_statistics() (推測)
└── _generate_output_markdown()
    ├── markdown_generator.create_repo_list_markdown()
    │   ├── markdown_generator.create_repository_section() (ループ内で複数回呼び出し)
    │   │   ├── badge_generator.generate_badge()
    │   │   └── date_formatter.format_date_for_display()
    │   └── template_processor.process_template() (推測)
    └── (生成されたMarkdownをファイルに書き出し)

---
Generated at: 2026-02-19 07:12:18 JST
