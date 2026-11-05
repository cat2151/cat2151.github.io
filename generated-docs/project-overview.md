Last updated: 2026-11-06

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、JekyllベースのGitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 生成された一覧は検索エンジンにクロールされやすく、LLMによるリポジトリ参照精度向上に貢献します。
- SEO最適化されたMarkdown生成や、各リポジトリの概要自動取得機能などを提供します。

## 技術スタック
- フロントエンド:
    -   Jekyll: GitHub Pagesで静的サイトを構築するためのフレームワークです。
    -   Markdown: 生成されるリポジトリ一覧ページの出力形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    -   GitHub API: GitHubからリポジトリ情報をプログラム的に取得するためのインターフェースです。
- テスト:
    -   pytest: Pythonアプリケーションのテストを記述・実行するためのフレームワークです。
- ビルドツール: 該当する技術は使用されていません（JekyllがGitHub Pages上で自動的にサイトをビルドします）。
- 言語機能:
    -   Python: プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得、処理、Markdown生成に利用されています。
- 自動化・CI/CD:
    -   GitHub Pages: Jekyllサイトのホスティングと、変更があった際のサイト再デプロイを自動で行うGitHubのサービスです。
- 開発標準:
    -   Ruff: Pythonコードのフォーマットとリンティングを高速に行うツールで、コード品質と一貫性を保ちます。
    -   .editorconfig: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
-   `.editorconfig`: 異なる開発環境間でのコードスタイルの一貫性を保証するための設定ファイルです。
-   `.github_automation/check_large_files/`: 大容量ファイルの存在をチェックし、リポジトリサイズを管理するための自動化スクリプト群を格納します。
    -   `README.md`: `check_large_files` 機能に関する説明を提供します。
    -   `check-large-files.toml`: 大容量ファイルチェックの設定（例: 許容サイズ閾値）を定義します。
    -   `scripts/check_large_files.py`: 実際にリポジトリ内のファイルを走査し、設定に基づき大容量ファイルを検出するPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理システムが追跡しないファイルやディレクトリを指定するファイルです。
-   `LICENSE`: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス条項が記載されています。
-   `README.md`: プロジェクトの概要、目的、主な機能、使用方法、開発者向けのヒントなどをまとめたメインのドキュメントです。
-   `_config.yml`: Jekyllサイト全体の構成設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を管理します。
-   `assets/`: GitHub Pagesサイトで使用されるファビコンなどの静的アセットファイルを格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
-   `debug_project_overview.py`: `project_overview` 機能の動作を検証・デバッグするための補助スクリプトです。
-   `generated-docs/`: 各リポジトリから取得される`project-overview.md`など、自動生成または参照されるドキュメントを配置する想定のディレクトリです。
-   `googled947dc864c270e07.html`: Google Search Consoleによるサイトの所有権確認に使用される認証ファイルです。
-   `index.md`: プロジェクトによって自動生成される、GitHub Pagesサイトのリポジトリ一覧メインページとなるMarkdownファイルです。
-   `issue-notes/22.md`: 特定の課題（例: GitHub Issue #22）に関するメモや詳細な議論を記録するためのMarkdownファイルです。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ウェブアプリの表示方法や動作を定義します。
-   `pytest.ini`: `pytest` テストフレームワークの動作を設定するためのファイルです。
-   `requirements-dev.txt`: 開発環境やテスト実行時に必要となるPythonパッケージの依存関係をリスト化したファイルです。
-   `requirements.txt`: プロジェクトの実行（本番環境）に最低限必要となるPythonパッケージの依存関係をリスト化したファイルです。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、または除外すべきかを指示するファイルです。
-   `ruff.toml`: `Ruff` リンター/フォーマッターの動作設定を定義するファイルで、コードスタイルルールを管理します。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージであることを示すファイルです。
    -   `generate_repo_list/`: リポジトリリスト生成機能の中核をなすモジュール群です。
        -   `__init__.py`: Pythonパッケージであることを示すファイルです。
        -   `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを含みます。
        -   `config.yml`: リポジトリリスト生成処理の具体的な設定（例: project_overview機能の有効/無効、対象ファイルパス）を定義します。
        -   `config_manager.py`: `config.yml` ファイルの読み込みと管理を行うモジュールです。
        -   `date_formatter.py`: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成するメインのスクリプトです。
        -   `json_ld_template.json`: 検索エンジン最適化(SEO)のために構造化データを埋め込む際に使用されるJSON-LD形式のテンプレートです。
        -   `language_info.py`: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するモジュールです。
        -   `markdown_generator.py`: 取得したリポジトリ情報や概要データをもとに、Markdown形式のコンテンツを生成するロジックを含みます。
        -   `project_overview_fetcher.py`: 各GitHubリポジトリから `generated-docs/project-overview.md` ファイルの内容を取得し、概要を抽出する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出し、解析するモジュールです。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、アプリケーションが利用しやすい形式に加工・処理する役割を担います。
        -   `seo_template.yml`: SEO関連のメタデータや構造化データに関するテンプレート設定を定義します。
        -   `statistics_calculator.py`: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算するモジュールです。
        -   `strings.yml`: アプリケーション内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するためのファイルです。
        -   `template_processor.py`: Markdownなどのテンプレートを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成するモジュールです。
        -   `url_utils.py`: URLの操作、生成、検証などのユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールの機能に関する単体テストを記述したファイルです。
-   `tests/`: プロジェクトの様々なコンポーネントに対するテストコードを格納するディレクトリです。
    -   `conftest.py`: `pytest` で共有されるフィクスチャやヘルパー関数を定義するファイルです。
    -   `test_badge_generator_integration.py`: バッジ生成機能の結合テストを行うファイルです。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストを行うファイルです。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテストを行うファイルです。
    -   `test_date_formatter.py`: 日付整形ユーティリティのテストを行うファイルです。
    -   `test_environment.py`: プロジェクトの実行環境に関するテストを行うファイルです。
    -   `test_integration.py`: プロジェクトの主要な機能が連携して正しく動作するかを確認する結合テストを行うファイルです。
    -   `test_markdown_generator.py`: Markdown生成機能のテストを行うファイルです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを行うファイルです。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを行うファイルです。
    -   `test_repository_processor.py`: リポジトリデータ処理機能のテストを行うファイルです。

## 関数詳細説明
提供された情報からは個別の関数の具体的な引数、戻り値、詳細な機能を特定できませんが、プロジェクトの各Pythonファイルは、そのファイル名が示す役割に対応する関数群で構成されていると推測されます。

例えば：
-   `src/generate_repo_list/generate_repo_list.py`: リポジトリ一覧生成の全体フローをオーケストレートする`main`関数（またはそれに相当するエントリポイント）を含むと考えられます。この関数は、GitHub APIからのデータ取得、データの処理、Markdown生成、ファイル出力などの主要なステップを順に呼び出す役割を担うでしょう。
-   `src/generate_repo_list/badge_generator.py`: バッジのデータ（例: 言語、ライセンス）を受け取り、それに対応するMarkdown形式のバッジ文字列を生成する関数（例: `generate_badge_markdown`）が含まれていると推測されます。
-   `src/generate_repo_list/project_overview_fetcher.py`: 特定のリポジトリ（またはURL）とファイルパスを指定して、そのコンテンツを読み込み、設定されたセクションタイトルに基づいてプロジェクトの概要（3行の説明）を抽出する関数（例: `fetch_project_overview`）が含まれると考えられます。
-   `src/generate_repo_list/markdown_generator.py`: 処理されたリポジトリデータを受け取り、SEO情報、バッジ、概要などを含んだ最終的なリポジトリ一覧のMarkdownテキストを構築する関数（例: `generate_repository_list_markdown`）があるでしょう。

これらのファイルは、それぞれが特定のタスクをカプセル化した関数を提供し、`generate_repo_list.py` のようなメインスクリプトによって連携して呼び出されることで、全体としてリポジトリ一覧自動生成システムを構成しています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-06 07:08:10 JST
