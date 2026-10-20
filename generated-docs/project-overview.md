Last updated: 2026-10-21

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたMarkdownファイルは、Jekyllベースのウェブサイトに最適化されています。
- 検索エンジンからのクロールを促進し、LLMによるリポジトリ参照精度向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤とし、Markdown形式でコンテンツを生成します。生成されたMarkdownはJekyllによってHTMLに変換され、ウェブサイトとして表示されます。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連の技術は使用していません。
- 開発ツール: GitHub API (リポジトリ情報の取得)、ruff (Pythonコードのリンティングとフォーマット)。
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)。
- ビルドツール: Python (主要なスクリプト言語として、Markdownファイルの生成ロジックを実装)、Jekyll (GitHub Pagesのサイトビルドエンジン)。
- 言語機能: Python (バージョン3.8以降)。
- 自動化・CI/CD: GitHub Actions (リポジトリの自動チェックなど、CI/CDに利用される自動化スクリプト群を格納するディレクトリが存在)。
- 開発標準: ruff (コード品質とスタイルの一貫性を保つためのリンター/フォーマッタ)。

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
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   `.github_automation/`: GitHub Actionsなどを用いた自動化スクリプトや設定ファイルを格納するディレクトリ。
    -   `check_large_files/`: プロジェクト内の大容量ファイルを検出・管理するためのサブディレクトリ。
        -   `README.md`: `check_large_files` 機能の説明ドキュメント。
        -   `check-large-files.toml`: 大容量ファイルチェックの設定（しきい値など）。
        -   `scripts/check_large_files.py`: プロジェクト内の大容量ファイルを特定し報告するPythonスクリプト。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイル。
-   `LICENSE`: このプロジェクトのソフトウェアライセンス（MITライセンス）情報が記述されています。
-   `README.md`: プロジェクトの概要、目的、使い方、設定方法などを説明するメインドキュメント。
-   `_config.yml`: Jekyllサイト全体の設定ファイル。GitHub Pagesの挙動やサイト構成を定義します。
-   `assets/`: ウェブサイトで使用される画像、アイコン、その他の静的アセットを格納するディレクトリ。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）ファイル群。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグやテスト実行を補助するためのスクリプト。
-   `generated-docs/`: 他のリポジトリから自動取得されたドキュメント（特に`project-overview.md`）が一時的に格納される可能性のあるディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイル。
-   `index.md`: `generate_repo_list.py`スクリプトによって、生成されたリポジトリ一覧が書き込まれる最終的なMarkdownファイル。これがGitHub Pagesのトップページになります。
-   `issue-notes/22.md`: 特定のIssue（問題やタスク）に関するメモや詳細を記述するためのファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される、ウェブアプリのメタデータを定義するファイル。
-   `pytest.ini`: pytestテストフレームワークの設定ファイル。テスト実行時のオプションやプラグインを指定します。
-   `requirements-dev.txt`: 開発時やテスト時に必要なPythonライブラリの依存関係をリストアップするファイル。
-   `requirements.txt`: 本番環境でこのスクリプトを実行するために必要なPythonライブラリの依存関係をリストアップするファイル。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは除外するかを指示するファイル。
-   `ruff.toml`: PythonのリンターおよびフォーマッターであるRuffの設定ファイル。コードスタイルや品質規則を定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   `__init__.py`: Pythonパッケージの初期化ファイル。
    -   `generate_repo_list/`: リポジトリ一覧を生成する主要ロジックをカプセル化したパッケージ。
        -   `__init__.py`: Pythonサブパッケージの初期化ファイル。
        -   `badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを管理します。
        -   `config.yml`: リポジトリ一覧生成に関する各種設定（例: プロジェクト概要取得機能の有効化/無効化、対象ファイル名など）を定義するYAMLファイル。
        -   `config_manager.py`: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのモジュール。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を統括します。
        -   `json_ld_template.json`: SEO強化のため、検索エンジンが理解しやすい構造化データ（JSON-LD）のテンプレートを定義します。
        -   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立てる機能を提供します。
        -   `markdown_generator.py`: GitHub APIから取得したデータを基に、最終的なMarkdownコンテンツを構築する役割を担います。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの概要説明を自動的に取得するロジックを実装しています。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス、ライセンス）を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、スクリプトが扱いやすい形に整形・加工する役割を担います。
        -   `seo_template.yml`: SEO関連のメタ情報や設定のテンプレートを定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計する機能を提供します。
        -   `strings.yml`: ユーザーインターフェースに表示されるテキストメッセージや文言を一元的に管理するYAMLファイル。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレート（Jinja2など）を処理し、動的なデータを埋め込む機能を提供します。
        -   `url_utils.py`: URLの生成、解析、検証などのユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するための単体テストファイル。
-   `tests/`: プロジェクト全体のテストファイルを格納するディレクトリ。
    -   `conftest.py`: pytestのテスト実行時に共通で使用されるフィクスチャやヘルパー関数を定義するファイル。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの結合テスト。
    -   `test_check_large_files.py`: `check_large_files.py`スクリプトのテスト。
    -   `test_config.py`: 設定ファイル (`config.yml`など) の読み込みや解釈が正しいかを検証するテスト。
    -   `test_date_formatter.py`: 日付フォーマット機能のテスト。
    -   `test_environment.py`: 実行環境のセットアップや依存関係のテスト。
    -   `test_integration.py`: プロジェクト全体の主要なフローが正しく連携して動作するかを検証する結合テスト。
    -   `test_markdown_generator.py`: Markdown生成ロジックのテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリデータ処理ロジックのテスト。

## 関数詳細説明
提供された情報からは、個々の関数の詳細な役割、引数、戻り値、機能を分析できませんでした。
しかし、各ファイルの説明に記載されている機能が、そのファイル内の主要な関数によって提供されています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-10-21 07:11:49 JST
