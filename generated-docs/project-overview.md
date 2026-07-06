Last updated: 2026-07-07

# Project Overview

## プロジェクト概要
- GitHub APIでリポジトリ情報を取得し、GitHub Pages向けに一覧を自動生成します。
- 生成されたマークダウンはSEOを考慮し、LLMからの参照性向上を目指します。
- 各リポジトリの概要を自動取得し、視覚的なバッジと共に効果的に表示します。

## 技術スタック
- フロントエンド: Jekyll - GitHub Pagesで静的Webサイトを生成するために使用される静的サイトジェネレータです。Pythonスクリプトが生成したMarkdownファイルをWebページとしてレンダリングします。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得からMarkdown生成までの中核処理を担います。
    - `requests`: GitHub APIとの通信を行うためのHTTPライブラリです。
    - `PyYAML`: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) を読み書きするために使用されます。
    - `toml`: TOML形式の秘密情報ファイル (`secrets.toml`) の読み書きをサポートします。
- テスト:
    - `pytest`: Pythonコードの単体テストおよび統合テストを実行するためのフレームワークです。
    - `pytest-mock`: `pytest`環境でオブジェクトのモック化を容易にするためのプラグインです。
- ビルドツール: (広義の) Jekyll - 静的サイトジェネレータとして、Pythonスクリプトが生成したコンテンツをWebサイトとして「ビルド」する役割を果たします。
- 言語機能: Python - 高レベルで汎用的なプログラミング言語であり、このプロジェクトのスクリプトの基盤となっています。
- 自動化・CI/CD: GitHub Actions (プラットフォーム) - GitHub上で自動化ワークフローを実行するための基盤です。このプロジェクトはGitHub Actionsで実行されることを想定したコンテンツを生成します。
- 開発標準:
    - `ruff`: Pythonコードのフォーマットとリンティングを自動で行い、コード品質とスタイルの一貫性を維持します。
    - `.editorconfig`: 異なるIDEやエディタ間でのコーディングスタイル（インデント、改行コードなど）の一貫性を定義します。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の閾値や除外設定を定義するTOML形式の設定ファイルです。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: プロジェクト内のリポジトリに不必要に大きなファイルがないかを検査するPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理から無視するファイルやディレクトリのパターンを定義します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、セットアップ方法、開発者向けのヒントなどが記されたメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の共通設定ファイルで、サイトのタイトル、テーマ、プラグインなどを定義します。
- **`assets/`**: Jekyllサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`assets/favicon-16x16.png`, `assets/favicon-192x192.png`, `assets/favicon-32x32.png`, `assets/favicon-512x512.png`**: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher.py`モジュールのデバッグや単体テストを行うための補助スクリプトです。
- **`generated-docs/`**: `project_overview_fetcher.py`が取得するプロジェクト概要ファイルや、その他の生成されたドキュメントを配置するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページ（トップページ）となるMarkdownファイルです。`generate_repo_list.py`によってリポジトリ一覧がこのファイルに生成されます。
- **`issue-notes/`**: 開発中の課題や調査結果、メモなどを格納するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（例: Issue #22）に関する詳細なノートや検討事項が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示方法やアイコンなどを定義します。
- **`pytest.ini`**: `pytest`テストフレームワークの設定ファイルで、テストの実行オプションや探索パスなどを指定します。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **`requirements.txt`**: プロジェクトの本番環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、または避けるべきかを指示するファイルです。
- **`ruff.toml`**: `ruff`リンターとフォーマッターの設定ファイルで、Pythonコードの静的解析ルールや整形スタイルを定義します。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: `src`ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを実装したPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして識別するためのファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例: アーカイブ済み、フォーク）を示すバッジの生成ロジックを管理します。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成に関する技術的なパラメータや機能の有効/無効設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を指定された形式に整形するためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのエントリポイントとなるメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する一連の処理を調整します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のために、Webページに構造化データを埋め込むためのJSON-LD形式のテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得・整形されたリポジトリ情報から、GitHub Pages向けのリポジトリ一覧Markdownコンテンツを生成するロジックを実装しています。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を自動的に抽出し取得する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイル内から、特定の形式で埋め込まれたバッジ情報を抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、アプリケーションが利用しやすい形式に加工・整形する役割を担います。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレートの構造を定義するYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計するモジュールです。
        - **`src/generate_repo_list/strings.yml`**: アプリケーション内で表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。
        - **`src/generate_repo_list/template_processor.py`**: 指定されたテンプレートファイル（例: Markdown、JSON）に対して、動的にデータを埋め込み、最終的な出力を生成する機能を提供します。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、解析などの操作を行うユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールのテストコードです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`tests/conftest.py`**: `pytest`のテストフィクスチャやヘルパー関数を定義し、テスト環境をセットアップするために使用されます。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator.py`の統合テストを記述したファイルです。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトのテストコードです。
    - **`tests/test_config.py`**: `config_manager.py`など、設定ファイルの読み込みと管理に関するテストを記述したファイルです。
    - **`tests/test_date_formatter.py`**: `date_formatter.py`モジュールの機能に関するテストを記述したファイルです。
    - **`tests/test_environment.py`**: 開発環境や実行環境のセットアップ、依存関係のチェックなどに関するテストです。
    - **`tests/test_integration.py`**: プロジェクト全体の主要な機能フローを検証する統合テストです。
    - **`tests/test_markdown_generator.py`**: `markdown_generator.py`モジュールのテストコードです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールのテストコードです。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールのテストコードです。
    - **`tests/test_repository_processor.py`**: `repository_processor.py`モジュールのテストコードです。

## 関数詳細説明
提供された情報には、具体的な関数のシグネチャ、引数、戻り値、詳細な機能に関する情報が含まれていません。そのため、個々の関数について詳細な説明を生成することはできません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-07 07:29:49 JST
