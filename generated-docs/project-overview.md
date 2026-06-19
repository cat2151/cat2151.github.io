Last updated: 2026-06-20

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で取得・整理するシステムです。
- JekyllベースのGitHub Pages向けに、SEOを意識したリポジトリ一覧をMarkdownで生成します。
- これにより、リポジトリの検索エンジンからの発見性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyll)**: 静的サイトジェネレータJekyllを基盤としたGitHub Pagesでコンテンツを公開します。**Markdown**: リポジトリ一覧のコンテンツ記述形式として使用されます。
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python**: メインの開発言語としてスクリプトを作成します。**GitHub API**: リポジトリ情報を取得するためのインターフェースとして利用されます。
- テスト: **pytest**: Pythonコードの単体テスト、結合テストフレームワークとして使用されます。
- ビルドツール: このプロジェクト自体はMarkdownファイルを「生成」するため、特定のビルドツールは直接使用しません。JekyllはGitHub Pages側で動作します。
- 言語機能: **Python**: オブジェクト指向プログラミング、標準ライブラリ、およびサードパーティライブラリを活用しています。
- 自動化・CI/CD: **GitHub Automation (`.github_automation/`)**: 特定の自動化スクリプト（例: 大容量ファイルチェック）が格納されており、開発プロセスの一部を自動化します。
- 開発標準: **Ruff**: Pythonコードのフォーマットとリンティングツールとして、コード品質と一貫性を保ちます。**.editorconfig**: 複数のエディタやIDE間でコードスタイルを統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なる開発環境間でのコードスタイルの一貫性を保つための設定ファイルです。
- **`.github_automation/`**: GitHub上での特定の自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能の目的と使用方法を説明するドキュメントです。
    - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルで、チェック対象の基準などを定義します。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、使用方法、クイックテスト手順などを説明するメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトルやテーマなどを定義します。
- **`assets/`**: ウェブサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: サイトのブラウザタブやブックマークなどに表示されるファビコン画像です。
- **`debug_project_overview.py`**: プロジェクト概要自動取得機能の動作確認やデバッグを目的としたスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや一時ファイルを格納するためのディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイルです。
- **`index.md`**: GitHub APIから取得したリポジトリ情報に基づいて生成される、GitHub Pagesサイトのリポジトリ一覧メインページです。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記述したファイルを格納するディレクトリです。
    - **`22.md`**: 特定の課題に関する詳細なメモや議論が記述されたファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、アプリのホーム画面アイコンや表示モードなどを定義します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルで、テストの実行オプションなどを指定します。
- **`requirements-dev.txt`**: 開発環境およびテストに必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードフォーマッター兼リンターであるRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能のコアモジュールを格納するディレクトリです。
        - **`__init__.py`**: Pythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（例：shields.io形式）を生成または処理する機能を提供します。
        - **`config.yml`**: リポジトリ一覧生成機能（特にプロジェクト概要取得など）に関する設定パラメータを定義するYAMLファイルです。
        - **`config_manager.py`**: プロジェクト全体で使用される各種設定ファイル（`config.yml`など）を読み込み、管理するためのモジュールです。
        - **`date_formatter.py`**: 日付や時刻の情報を整形し、人間が読みやすい形式に変換するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を実行します。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語の情報を取得、処理、集計するためのモジュールです。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、Jekyllの要件に合わせたMarkdownコンテンツを生成するロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出し、取得するモジュールです。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例：CI/CDステータス、ライセンス）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報に整形・加工（フィルタリング、分類など）を行うモジュールです。
        - **`seo_template.yml`**: サイトの検索エンジン最適化（SEO）関連のメタデータやキーワードなどのテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（スター数、フォーク数、最終更新日時など）を計算・集計するためのモジュールです。
        - **`strings.yml`**: プロジェクト内で表示されるメッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルで、国際化（i18n）や文言の統一に利用されます。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jinja2などのテンプレートエンジンを想定）の読み込み、レンダリング処理を行うモジュールです。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュール（プロジェクト概要取得機能）の単体テストや結合テストを記述したスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`conftest.py`**: pytestのフィクスチャ定義やテストランナーのフックを記述するファイルで、テストの共通設定を行います。
    - **`test_badge_generator_integration.py`**: `badge_generator.py`の統合テストを実行し、バッジ生成が期待通りに行われるかを確認します。
    - **`test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py`のテストスクリプトです。
    - **`test_config.py`**: `config_manager.py`など、設定ファイルの読み込みと管理に関する機能のテストです。
    - **`test_date_formatter.py`**: `date_formatter.py`モジュールのテストで、日付フォーマットが正しく機能するか検証します。
    - **`test_environment.py`**: 実行環境の設定や依存関係が正しく準備されているかを検証するテストです。
    - **`test_integration.py`**: プロジェクトの主要なコンポーネントが連携して正しく動作するかを検証する統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールのテストで、Markdownコンテンツが正しく生成されるかを確認します。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールのテストで、プロジェクト概要の取得と抽出が正しく行われるかを検証します。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor.py`モジュールのテストで、READMEからのバッジ抽出機能が正しく動作するかを確認します。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールのテストで、リポジトリデータの処理と整形が期待通りに行われるかを検証します。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: メインのエントリポイント関数。コマンドライン引数の解析、設定の読み込み、GitHub APIからのリポジトリ情報取得、リポジトリの処理、Markdownファイルの生成といった全体のフローを制御します。
- **`src/generate_repo_list/repository_processor.py`**
    - `process_repository(repo_data, config)`: GitHub APIから取得した単一のリポジトリデータを引数として受け取り、表示に適した形式に加工・整形します。プロジェクト概要の取得などもこの処理の中で行われます。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name, owner, file_path, config)`: 指定されたリポジトリ（`repo_name`と`owner`で特定）内の`file_path`にあるマークダウンファイルから「プロジェクト概要」セクションを抽出し、その内容を返します。設定（`config`）に基づき、キャッシュやリトライ処理も行われます。
- **`src/generate_repo_list/markdown_generator.py`**
    - `create_repository_list_markdown(repos_list, config, strings)`: 処理済みのリポジトリ情報のリスト（`repos_list`）を受け取り、Jekyllのフォーマットに合わせた最終的なMarkdownコンテンツ文字列を生成します。設定（`config`）や表示文言（`strings`）も考慮します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path)`: 指定されたパス（`config_path`）にあるYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして提供します。これにより、スクリプト全体で設定にアクセスできるようになります。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge_markdown(repo_info)`: 処理されたリポジトリ情報（`repo_info`）に基づいて、リポジトリに関連するバッジ（例：言語バッジ、スター数バッジ）のMarkdown形式の記述を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-06-20 07:23:49 JST
