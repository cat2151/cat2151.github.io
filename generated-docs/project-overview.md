Last updated: 2026-10-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたページは検索エンジンにクロールされやすく、リポジトリの発見性向上とLLMによる参照失敗の緩和に貢献します。
- 各リポジトリの概要、バッジ、分類などを自動でマークダウン形式で整形し、SEO最適化されたコンテンツを提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤)、Markdown (コンテンツ生成形式) - GitHub Pages上で動的なコンテンツを生成し、ブラウザで表示される静的サイトを構築します。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語)、PyYAML (設定ファイル読み込み)、requests (GitHub API連携) - システムの自動生成ロジックを実装し、GitHubからのデータ取得や設定管理を行います。
- テスト: pytest (テストフレームワーク) - コードの品質と機能の正確性を保証するためのテストを実行します。
- ビルドツール: なし - 専用のビルドツールは使用せず、Pythonスクリプトが直接コンテンツ生成の役割を担います。
- 言語機能: Python (スクリプト言語) - プロジェクトの自動化スクリプト全般にわたり利用されています。
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリに一部自動化スクリプトが見られますが、メインの生成はローカル実行を想定) - 現状はローカルでの開発・実行を重視していますが、一部の補助的な自動化処理に活用されます。
- 開発標準: Ruff (コードフォーマッター/リンター)、.editorconfig (コードスタイル定義) - コードの可読性と品質を保ち、開発者間での一貫したスタイルを維持するために使用されます。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化ワークフローに関連するスクリプトや設定ファイルを格納するディレクトリです。特に`check_large_files`は、リポジトリ内の大きなファイルを検出するための機能を含みます。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリ（例: ビルド生成物、ログファイル、一時ファイル）を指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記載されており、ソフトウェアの利用、配布、変更に関する条件を定めています。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、セットアップ手順などが記述された、プロジェクトの玄関となるドキュメントファイルです。
- **`_config.yml`**: Jekyllを使用するGitHub Pagesサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定を行います。
- **`assets/`**: サイトで使用される画像、CSS、JavaScriptなどの静的アセットファイルを格納するディレクトリです。ファビコンなどが含まれています。
- **`debug_project_overview.py`**: プロジェクト概要の取得機能をデバッグするために使用される補助的なスクリプトです。
- **`generated-docs/`**: 生成されたドキュメントや一時ファイルを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト認証のために配置されるHTMLファイルです。
- **`index.md`**: メインのPythonスクリプトによって、生成されたリポジトリ一覧が書き込まれる出力ファイルです。これがGitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 開発過程で発生した特定の課題や検討事項に関するメモを格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン機能など、Webサイトのアプリとしての振る舞いを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法やオプションを定義します。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: プロジェクトが本番稼働するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonの高速リンター/フォーマッターであるRuffの設定ファイルです。コードのスタイルと品質に関するルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムの中核となるPythonモジュール群です。
        - **`src/generate_repo_list/__init__.py`**: Pythonパッケージとして認識させるためのファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや特性を示すバッジ画像を生成するためのロジックを含みます。
        - **`src/generate_repo_list/config.yml`**: リポジトリ概要取得機能など、本システム固有の設定パラメータを定義するYAML形式の設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: プロジェクトの設定ファイルを読み込み、アクセスするためのユーティリティ関数を提供します。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報を、人間が読みやすい特定の形式に整形するための関数を提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を orchestrate します。
        - **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD形式）のテンプレートファイルです。SEOのために検索エンジンにリッチスニペットとして表示される情報を提供します。
        - **`src/generate_repo_list/language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理する機能を提供します。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdown形式のテキストコンテンツを生成するロジックを含みます。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出・取得する機能を提供します。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、ライセンス）を抽出する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、システムで利用しやすい形式に処理・変換する役割を担います。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータなどを定義するテンプレートファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関するコミット数、スター数などの統計情報を計算する機能を提供します。
        - **`src/generate_repo_list/strings.yml`**: サイトに表示される各種メッセージや文言を管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用されるテンプレートファイルを読み込み、データに基づいて動的に内容を埋め込む処理を行います。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、検証、パースなど、URLに関連するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能の単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`tests/conftest.py`**: pytestのテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共通して利用可能にするファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator`の統合テストです。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files`スクリプトのテストです。
    - **`tests/test_config.py`**: `config_manager`や`config.yml`の読み込みに関するテストです。
    - **`tests/test_date_formatter.py`**: `date_formatter`のテストです。
    - **`tests/test_environment.py`**: 実行環境に関する基本的なテストです。
    - **`tests/test_integration.py`**: システム全体の主要なフローに関する統合テストです。
    - **`tests/test_markdown_generator.py`**: `markdown_generator`のテストです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`のテストです。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`のテストです。
    - **`tests/test_repository_processor.py`**: `repository_processor`のテストです。

## 関数詳細説明
提供されたプロジェクト情報から、関数の具体的な引数、戻り値、詳細な機能は分析できませんでした。
しかし、ファイル名から推測される役割に基づき、それぞれのファイルに含まれる可能性のある関数の概要を説明します。

- **`badge_generator.py`**: リポジトリの活動状況や特性（例: アクティブ、アーカイブ）を示す視覚的なバッジ（アイコン）を生成するための関数群。
- **`config_manager.py`**: プロジェクト全体の設定ファイル（`config.yml`など）を読み込み、アプリケーションの他の部分から設定値にアクセスできるように管理する関数群。
- **`date_formatter.py`**: GitHub APIから取得した日付データを、表示に適した様々なフォーマット（例: "YYYY年MM月DD日", "〇日前"）に変換する関数群。
- **`generate_repo_list.py`**: プロジェクトの中核を担うメイン関数群。GitHub APIとの連携、データの取得、各処理モジュールの呼び出し、最終的なMarkdownファイルへの書き出しといった、一連の自動生成プロセスを制御します。
- **`language_info.py`**: リポジトリで使用されているプログラミング言語の種類や、その使用割合などの統計情報を取得し、整形する関数群。
- **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートをもとに、GitHub Pages用の最終的なMarkdownコンテンツを生成する関数群。
- **`project_overview_fetcher.py`**: 各リポジトリの特定のパスにある`project-overview.md`ファイルから、プロジェクトの3行概要を抽出・取得する関数群。
- **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルの内容を解析し、含まれるバッジ（例: CI/CDステータス、ライセンス）の情報を抽出する関数群。
- **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を解析し、システムの他の部分で扱いやすいオブジェクトや構造に変換する関数群。
- **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、Markdown生成時に利用可能な形式で提供する関数群。
- **`template_processor.py`**: Markdown生成のためのテンプレートファイルを読み込み、動的にデータを挿入して最終的なテキストコンテンツを組み立てる関数群。
- **`url_utils.py`**: GitHubリポジトリのURLやGitHub PagesのURLなど、URLに関連する操作（生成、検証、パース）を行うユーティリティ関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-08 07:11:49 JST
