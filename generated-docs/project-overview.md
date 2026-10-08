Last updated: 2026-10-09

# Project Overview

## プロジェクト概要
- このプロジェクトは、GitHub APIを利用してリポジトリ情報を自動取得し、JekyllベースのGitHub Pagesサイト用にMarkdownファイルとして一覧を生成します。
- GitHubのユーザーページで生じるSEO上の課題や、LLMがリポジトリ参照に失敗する問題を解決することを目指しています。
- 生成されたGitHub Pagesは検索エンジンにクロールされやすくなり、各リポジトリの可視性とアクセス性を向上させます。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pages) - 静的サイトジェネレーターとして、自動生成されたMarkdownファイルを美しいWebページとして公開するために利用されます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: メインのスクリプト言語として、GitHub APIからの情報取得、データの処理、Markdownファイルの生成などに利用されます。
    - **Git / GitHub API**: リポジトリ情報の取得元として、GitHubの公開APIおよびGitバージョン管理システムが利用されます。
    - **pytest**: Pythonコードのテストフレームワークとして、ユニットテストや統合テストの実行に用いられます。
    - **ruff**: Pythonコードのスタイルチェックおよび自動フォーマットツールとして、コード品質の維持と統一に貢献します。
- テスト:
    - **pytest**: Pythonスクリプトの機能が正しく動作するか検証するために使用されます。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py` を中心とするPythonスクリプト群が、GitHub APIから取得した情報を元にMarkdownファイルを「ビルド」する役割を担います。
    - **Jekyll**: 生成されたMarkdownファイルを静的Webサイトとして「ビルド」し、GitHub Pagesにデプロイ可能な形式に変換します。
- 言語機能:
    - **Python**: プロジェクトの主要なプログラミング言語です。
    - **Markdown**: リポジトリ一覧の出力形式として採用されており、Webコンテンツの記述に使用されます。
    - **YAML / JSON**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) やSEOメタデータ (`json_ld_template.json`) の記述に使用されます。
- 自動化・CI/CD:
    - **GitHub API**: リポジトリ情報の自動取得自体が自動化の一部です。
    - **GitHub Actions (`.github_automation` ディレクトリ)**: 直接的なCI/CDパイプラインは推奨されていませんが、`check_large_files` のようなスクリプトが存在し、将来的なGitHub Actionsによる自動化の可能性を示唆しています。
- 開発標準:
    - **ruff**: Pythonコードの統一されたコーディングスタイルを維持するためのリンター・フォーマッターです。
    - **.editorconfig**: 異なるエディタ間でのコーディングスタイルの整合性を保ちます。

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
- **`.editorconfig`**: 開発環境におけるコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメントです。
    - **`check-large-files.toml`**: 大容量ファイルチェックの設定を定義するファイルです。
    - **`scripts/check_large_files.py`**: リポジトリ内の大容量ファイルを特定するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けのヒントなどを記述した、プロジェクトの主要な説明書です。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。GitHub Pagesの挙動に影響します。
- **`assets/`**: Jekyllサイトで利用される画像やファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークなどに表示されるファビコン画像です。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグやテストに特化したPythonスクリプトです。
- **`generated-docs/`**: 各リポジトリの `project-overview.md` など、自動取得・生成されたドキュメントやデータが配置されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイルです。
- **`index.md`**: メインのリポジトリ一覧が生成され、GitHub Pagesのトップページとして表示されるMarkdownファイルです。
- **`issue-notes/22.md`**: 課題や改善点に関するメモを格納するディレクトリ内のファイルです。
- **`manifest.json`**: Progressive Web App (PWA) の設定を記述するマニフェストファイルです。アプリの表示名、アイコン、起動方法などを定義します。
- **`pytest.ini`**: pytestテストフレームワークの挙動をカスタマイズするための設定ファイルです。
- **`requirements-dev.txt`**: 開発環境で必要となるPythonパッケージとそのバージョンを列挙したファイルです。テストツールなどが含まれます。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonパッケージとそのバージョンを列挙したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールし、どのページを無視するかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コーディング規約を定義します。
- **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧を生成する主要なロジックを格納するPythonパッケージです。
    - **`__init__.py`**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示すファイルです。
    - **`badge_generator.py`**: リポジトリのプロパティ（言語、ステータスなど）に基づいてバッジ画像を生成するロジックを提供します。
    - **`config.yml`**: プロジェクト概要の取得設定など、システムの動作パラメータを定義するYAML形式の設定ファイルです。
    - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュールです。
    - **`date_formatter.py`**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: このプロジェクトのメインとなる実行スクリプトです。GitHub APIからデータを取得し、Markdownを生成する一連のプロセスを制御します。
    - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データをWebページに埋め込むためのJSON-LDテンプレートです。
    - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形する機能を提供します。
    - **`markdown_generator.py`**: 最終的なリポジトリ一覧のMarkdownコンテンツを構築・生成するロジックをカプセル化しています。
    - **`project_overview_fetcher.py`**: 各リポジトリに存在する `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出する機能を提供します。
    - **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報（例: ビルドステータスバッジ）を抽出するモジュールです。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、Markdown生成に適した形式に加工・整形する役割を担います。
    - **`seo_template.yml`**: 検索エンジン最適化 (SEO) に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計する機能を提供します。
    - **`strings.yml`**: プロジェクト内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するYAMLファイルです。多言語対応の基盤にもなり得ます。
    - **`template_processor.py`**: Markdownテンプレートに変数を埋め込んだり、条件分岐を処理したりするためのテンプレート処理機能を提供します。
    - **`url_utils.py`**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestテストフレームワークで使用される共通のフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator` モジュールの統合テストを行い、バッジ生成が期待通りに動作するかを検証します。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files` 内のスクリプトの機能を検証するテストです。
    - **`test_config.py`**: `config_manager` モジュールや設定ファイルの読み込みが正しく行われるかを検証するテストです。
    - **`test_date_formatter.py`**: `date_formatter` モジュールの日付整形機能が正しく動作するかを検証するテストです。
    - **`test_environment.py`**: プロジェクトの実行環境が適切に設定されているか（例: 必要な環境変数の存在）を検証するテストです。
    - **`test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを検証する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator` モジュールのMarkdown生成機能が期待通りの出力を生むかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールのテストです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールのテストです。
    - **`test_repository_processor.py`**: `repository_processor` モジュールのリポジトリ情報処理機能が正しく動作するかを検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には、Pythonスクリプト内の具体的な関数シグネチャや実装に関する詳細が含まれていません。そのため、ハルシネーションを避けるため、ここでは主要なファイルから推測される関数とその役割について記述します。具体的な引数、戻り値、呼び出し元などの詳細は、実際のコードベースを参照してください。

- **`src/generate_repo_list/generate_repo_list.py` 内の主要処理関数 (例: `main` や `generate_repository_list`)**
    - **役割**: プロジェクト全体のリポジトリ一覧生成プロセスを orchestrate します。GitHub APIからリポジトリ情報を取得し、整形し、最終的なMarkdownファイルを生成する一連の流れを制御します。
    - **引数**: プロジェクト情報からは具体的な引数の詳細は不明です。通常、GitHubユーザー名、出力ファイルパス、処理するリポジトリ数の上限などのコマンドライン引数や設定情報を受け取ると推測されます。
    - **戻り値**: プロジェクト情報からは具体的な戻り値の詳細は不明です。通常、処理の成功/失敗を示すステータスコードやブーリアン値を返すと考えられます。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の概要取得関数 (例: `fetch_project_overview`)**
    - **役割**: 各GitHubリポジトリの指定されたパス (`generated-docs/project-overview.md`) から、プロジェクトの3行概要を非同期で取得する機能を提供します。
    - **引数**: プロジェクト情報からは具体的な引数の詳細は不明です。通常、リポジトリのURLや名前、設定オブジェクトなどを受け取ると推測されます。
    - **戻り値**: プロジェクト情報からは具体的な戻り値の詳細は不明です。通常、抽出された3行概要のリストや文字列、または取得失敗時には空の値やエラーを示す値を返すと推測されます。

- **`src/generate_repo_list/repository_processor.py` 内のリポジトリ情報処理関数 (例: `process_repository_data`)**
    - **役割**: GitHub APIから取得した生のリポジトリデータを加工し、必要な情報を抽出し、Markdown生成に適した構造に整形します。アクティブ、アーカイブ、フォークなどの分類も担当すると推測されます。
    - **引数**: プロジェクト情報からは具体的な引数の詳細は不明です。通常、生のGitHubリポジトリデータ（辞書形式など）を受け取ると推測されます。
    - **戻り値**: プロジェクト情報からは具体的な戻り値の詳細は不明です。通常、整形されたリポジトリ情報の辞書やオブジェクトを返すと推測されます。

- **`src/generate_repo_list/markdown_generator.py` 内のMarkdown生成関数 (例: `generate_markdown`)**
    - **役割**: 処理済みのリポジトリ情報を受け取り、Jekyllのフォーマットに沿ったMarkdownコンテンツを実際に生成します。バッジや概要、リンクなどを適切に埋め込みます。
    - **引数**: プロジェクト情報からは具体的な引数の詳細は不明です。通常、整形されたリポジトリ情報のリストや、各種テンプレート・設定情報を受け取ると推測されます。
    - **戻り値**: プロジェクト情報からは具体的な戻り値の詳細は不明です。通常、生成されたMarkdown形式の文字列を返すと推測されます。

- **`src/generate_repo_list/config_manager.py` 内の設定管理関数 (例: `load_config`, `get_string`)**
    - **役割**: YAML形式の設定ファイル (`config.yml`, `strings.yml`) を読み込み、アプリケーション全体で利用可能な形式で管理・提供します。
    - **引数**: プロジェクト情報からは具体的な引数の詳細は不明です。通常、設定ファイルのパスやキーを受け取ると推測されます。
    - **戻り値**: プロジェクト情報からは具体的な戻り値の詳細は不明です。通常、設定値を示す辞書や文字列を返すと推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-09 07:13:11 JST
