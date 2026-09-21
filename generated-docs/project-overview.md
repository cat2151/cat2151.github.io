Last updated: 2026-09-22

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成し、SEOを強化するシステムです。
- GitHub APIを活用してリポジトリ情報を取得し、魅力的なMarkdownコンテンツを出力します。
- 検索エンジンやLLMからのアクセス性を高め、プロジェクトの可視性と開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (スクリプト言語), Git (バージョン管理), GitHub API (リポジトリ情報取得)
- テスト: pytest (Pythonテストフレームワーク)
- ビルドツール: Pythonスクリプト (`generate_repo_list.py` が主要な生成ツール)
- 言語機能: Python (バージョン3.x系の言語仕様と標準ライブラリ)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリから推測される自動化ワークフロー), Pythonスクリプトによる自動生成処理
- 開発標準: ruff (Pythonコードのフォーマットとリント), .editorconfig (エディター共通設定)

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
-   `.editorconfig`: 異なるエディターやIDEを使用する開発者が、統一されたコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
-   `.github_automation/`: GitHub ActionsなどのCI/CDや自動化処理に関連するスクリプトや設定を格納するディレクトリ。
    -   `check_large_files/`: 大容量ファイルをリポジトリにコミットすることを防止するためのチェックツール関連ファイル群。
        -   `README.md`: `check_large_files`ツールの説明。
        -   `check-large-files.toml`: `check_large_files`ツールの設定ファイル。
        -   `scripts/check_large_files.py`: 実際に大容量ファイルをチェックするPythonスクリプト。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイル。
-   `LICENSE`: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）。
-   `README.md`: プロジェクトの概要、目的、主な機能、セットアップ方法、実行方法、開発者向けのヒントなどを記述した、プロジェクトの顔となるドキュメント。
-   `_config.yml`: GitHub Pagesで利用されるJekyllのサイト全体の構成設定ファイル。テーマやプラグイン、カスタム変数などを定義します。
-   `assets/`: サイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグやテストを目的としたスクリプトであると推測されます。
-   `generated-docs/`: プロジェクト概要機能で参照される `project-overview.md` ファイルや、その他の生成されたドキュメントが配置される可能性のあるディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleなどでのサイト所有権確認のために配置されるHTMLファイル。来訪者向けには直接表示されませんが、サイトの信頼性維持に寄与します。
-   `index.md`: `generate_repo_list.py`スクリプトによってリポジトリ一覧が生成され、GitHub Pagesのトップページとして表示される主要なMarkdownファイル。
-   `issue-notes/`: 開発中に発生した課題や検討事項、特定のIssueに関連するメモなどを格納するディレクトリ。
    -   `22.md`: 特定のIssue (#22) に関連するメモファイルであると推測されます。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用されるマニフェストファイル。アプリのアイコン、表示名、テーマカラーなどを定義し、ユーザーがウェブサイトをデバイスにインストールする際の挙動を制御します。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの設定ファイル。テストの発見方法、実行オプション、プラグインなどを定義します。
-   `requirements-dev.txt`: 開発環境やテスト環境で必要となるPythonライブラリの依存関係を記述したファイル。
-   `requirements.txt`: プロジェクトの本番実行に必要となるPythonライブラリの依存関係を記述したファイル。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、またはクロールしてはいけないかを指示するためのファイル。SEOに影響します。
-   `ruff.toml`: Pythonの高速なLinterおよびFormatterであるRuffの設定ファイル。コードの品質と統一性を保つためのルールを定義します。
-   `src/`: プロジェクトの主要なソースコードが格納されるディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示すファイル。
    -   `generate_repo_list/`: リポジトリ一覧を生成するシステムのコアロジックを格納するパッケージ。
        -   `__init__.py`: `generate_repo_list`パッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリのステータスや技術を示すバッジの生成ロジックを実装します。
        -   `config.yml`: プロジェクト概要取得機能などの、スクリプトの技術的なパラメータを設定するYAMLファイル。
        -   `config_manager.py`: `config.yml`やシークレットファイルから設定情報を読み込み、管理するロジックを実装します。
        -   `date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプト。リポジトリ情報の取得、処理、Markdown生成の全体フローを制御します。
        -   `json_ld_template.json`: SEOを強化するために、検索エンジンがコンテンツを理解しやすくなるJSON-LD形式の構造化データテンプレート。
        -   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するロジックを実装します。
        -   `markdown_generator.py`: 整形されたリポジトリデータに基づいて、Markdown形式のコンテンツを生成するロジックを実装します。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを自動的に取得するロジックを実装します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するロジックを実装します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを加工し、必要な情報を抽出・整形する主要な処理ロジックを実装します。
        -   `seo_template.yml`: 生成されるMarkdownのSEO関連メタデータやテンプレート設定を定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算するロジックを実装します。
        -   `strings.yml`: UIに表示されるメッセージや文言を一元的に管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレートファイルの処理や、Jekyllなどの静的サイトジェネレーターで利用される可能性のあるテンプレート関連のロジックを実装します。
        -   `url_utils.py`: URLの検証、整形、構築などのユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の単体テストや統合テストを行うスクリプトであると推測されます。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリ。
    -   `conftest.py`: pytestで使用されるフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    -   `test_badge_generator_integration.py`: `badge_generator.py`の統合テスト。
    -   `test_check_large_files.py`: `.github_automation/check_large_files/scripts/check_large_files.py`のテスト。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理機能のテスト。
    -   `test_date_formatter.py`: 日付整形機能のテスト。
    -   `test_environment.py`: 環境変数やGitHubトークンなどの実行環境設定のテスト。
    -   `test_integration.py`: プロジェクト全体の主要なフローに関する統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供された情報から個々の関数の詳細なシグネチャ（引数、戻り値）は特定できませんが、ファイル名とプロジェクトの目的から推測される主要な関数とその役割を説明します。

-   **`generate_repo_list.py`**:
    -   **`main()`**: プログラムのエントリポイント。コマンドライン引数を解析し、設定の読み込み、GitHub APIからのリポジトリ情報取得、各リポジトリのデータ処理、最終的なMarkdownファイルの生成という、プロジェクト全体のフローを orchestrate します。
-   **`repository_processor.py`**:
    -   **`fetch_repositories(username)`**: 指定されたGitHubユーザー名に基づき、GitHub APIを介してそのユーザーが所有する全てのリポジトリ情報を取得します。取得したデータは後続の処理のために整形されます。
    -   **`process_repository(repo_data)`**: GitHub APIから取得した個々のリポジトリの生データを受け取り、プロジェクト概要の取得、バッジの抽出、言語情報の解析など、必要な追加情報を付与・整形し、Markdown生成に適した形式に変換します。
-   **`project_overview_fetcher.py`**:
    -   **`fetch_project_overview(repo_url, config)`**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）に存在するファイルから、プロジェクトの3行概要を抽出して返します。GitHub APIを利用してファイル内容にアクセスし、指定されたセクションをパースします。
-   **`markdown_generator.py`**:
    -   **`generate_markdown(repo_list, output_file)`**: 処理済みのリポジトリ情報リストを基に、SEOに最適化されたMarkdownコンテンツを生成します。このコンテンツは、リポジトリ一覧や各リポジトリの詳細を含む形になり、指定された出力ファイルに書き込まれます。
-   **`badge_generator.py`**:
    -   **`generate_badge(badge_info)`**: リポジトリのアクティビティ、アーカイブ状態、フォーク状態、またはその他のカスタム情報に基づいて、Markdown形式で表示されるバッジの文字列を生成します。
-   **`config_manager.py`**:
    -   **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイル（例: `config.yml`）を読み込み、設定オブジェクトとして提供します。
    -   **`get_github_token()`**: ローカル実行時に使用されるGitHub APIトークンを、設定ファイル（例: `secrets/secrets.toml`）から安全に取得します。
-   **`date_formatter.py`**:
    -   **`format_date(datetime_obj, format_string)`**: 日付と時刻のオブジェクトを受け取り、指定されたフォーマット文字列に従って人間が読みやすい形式の文字列に変換します。
-   **`url_utils.py`**:
    -   **`validate_url(url_string)`**: 与えられた文字列が有効なURLであるか検証します。
    -   **`build_repo_url(username, repo_name)`**: GitHubユーザー名とリポジトリ名から、リポジトリのURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-22 07:12:01 JST
