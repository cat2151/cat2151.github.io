Last updated: 2026-07-20

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、自身のGitHub Pagesサイト向けにリポジトリ一覧を自動生成します。
- 検索エンジンやLLMからの参照性を高め、リポジトリ情報の発見・利用を促進します。
- 各リポジトリの概要、バッジ、分類などを自動抽出し、SEO最適化されたMarkdown形式で出力します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの静的サイトジェネレータ), Markdown (生成される出力形式)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), pytest (テストフレームワーク), Ruff (コードリンター/フォーマッター)
- テスト: pytest (Pythonコードの単体テストおよび結合テストに使用)
- ビルドツール: 直接的なビルドツールは使用されていません。PythonスクリプトがMarkdownファイルを生成し、JekyllがGitHub Pagesのビルド環境で利用されます。
- 言語機能: Python (スクリプト開発言語), YAML (設定ファイル定義), TOML (設定ファイル定義)
- 自動化・CI/CD: `.github_automation` ディレクトリが存在しますが、プロジェクト自体はローカル開発重視でCI/CDは強調されていません。
- 開発標準: Ruff (コードの整形と品質維持のための静的解析ツール)

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを定義する設定ファイル。
- **`.github_automation/`**: GitHub関連の自動化スクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大容量ファイルチェックの設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記載したファイル。
- **`README.md`**: プロジェクトの概要、目的、使用方法、設定、ライセンスなど、プロジェクトに関する包括的な情報を提供するメインドキュメント。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の挙動を制御する設定ファイル。
- **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリ。
    - **`favicon-*.png`**: ウェブサイトのブラウザタブやブックマークなどに表示されるアイコンファイル。
- **`debug_project_overview.py`**: `project_overview_fetcher`モジュールのデバッグやテストに特化したスクリプト。
- **`generated-docs/`**: 生成されたドキュメントや一時ファイルを格納するためのディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用ファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。自動生成されたリポジトリ一覧がここに格納されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項をメモとして格納するディレクトリ。
    - **`issue-notes/22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモや考察を記録したファイル。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定を定義し、ウェブアプリの見た目や動作をカスタマイズするためのファイル。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するためのファイル。
- **`requirements-dev.txt`**: 開発環境やテスト実行時に必要となるPythonライブラリとそのバージョンを定義するファイル。
- **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonライブラリとそのバージョンを定義するファイル。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイル。
- **`ruff.toml`**: PythonのコードリンターおよびフォーマッターであるRuffの設定ファイル。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイル。
    - **`src/generate_repo_list/`**: リポジトリ一覧を生成する機能の中核となるPythonパッケージ。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイル。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの状態（アクティブ、アーカイブなど）に応じたバッジのマークダウンを生成するロジックを実装。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的パラメータを定義する設定ファイル。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するユーティリティモジュール。
        - **`src/generate_repo_list/date_formatter.py`**: 日付の表示形式を整形するための関数群を提供。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、整形してMarkdownを生成する一連の処理を統括。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のためのJSON-LD形式の構造化データテンプレート。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの使用言語に関する情報を処理し、集計する機能を提供。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得・処理されたリポジトリ情報から、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成する。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を自動取得する機能。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIからのリポジトリ情報の取得、フィルタリング、必要なデータ形式への加工を行う。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連の設定やテンプレートを定義するYAMLファイル。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する様々な統計情報（例: スター数、フォーク数など）を計算する。
        - **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するYAMLファイル。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成に使用するテンプレートファイルを読み込み、データに基づいてレンダリング処理を行う。
        - **`src/generate_repo_list/url_utils.py`**: GitHub APIやリポジトリへのURL構築に関するユーティリティ関数を提供。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの単体テストを記述したファイル。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共通して利用するためのファイル。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator`の統合テスト。
    - **`tests/test_check_large_files.py`**: `check_large_files.py`スクリプトのテスト。
    - **`tests/test_config.py`**: 設定ファイル (`config.yml` など) の読み込みとパースに関するテスト。
    - **`tests/test_date_formatter.py`**: `date_formatter`モジュールの機能テスト。
    - **`tests/test_environment.py`**: テスト実行環境のセットアップや依存関係に関するテスト。
    - **`tests/test_integration.py`**: プロジェクト全体の主要なフローに関する統合テスト。
    - **`tests/test_markdown_generator.py`**: `markdown_generator`モジュールの機能テスト。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールの機能テスト。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールの機能テスト。
    - **`tests/test_repository_processor.py`**: `repository_processor`モジュールの機能テスト。

## 関数詳細説明
*   **`src/generate_repo_list/generate_repo_list.py`**
    *   **`main()`**: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成という一連のフローを制御します。
    *   **`parse_arguments()`**: コマンドラインから `--username`, `--output`, `--limit` などの引数を解析し、設定オブジェクトとして返します。
*   **`src/generate_repo_list/repository_processor.py`**
    *   **`fetch_repositories(username, token)`**: GitHub APIを通じて指定されたユーザー名のリポジトリ一覧を取得します。認証のためにGitHubトークンを使用します。
    *   **`process_repository(repo_data)`**: GitHub APIから取得した個々のリポジトリデータを受け取り、必要な情報（名前、説明、URL、言語など）を抽出し、整形します。
*   **`src/generate_repo_list/project_overview_fetcher.py`**
    *   **`get_project_overview(repo_url, config)`**: 指定されたリポジトリの特定のファイル (`generated-docs/project-overview.md`) から、プロジェクト概要の3行説明をネットワーク経由で取得し、抽出します。
*   **`src/generate_repo_list/markdown_generator.py`**
    *   **`generate_markdown(repo_list, template_data)`**: 処理されたリポジトリ情報のリストとテンプレートデータに基づいて、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成します。
*   **`src/generate_repo_list/badge_generator.py`**
    *   **`create_badge(status)`**: リポジトリの状態（例: アクティブ、アーカイブ、フォークなど）を示すマークダウン形式のバッジ文字列を生成します。
*   **`src/generate_repo_list/config_manager.py`**
    *   **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
*   **`src/generate_repo_list/date_formatter.py`**
    *   **`format_date(date_string)`**: 日付文字列を受け取り、指定されたフォーマット（例: "YYYY年MM月DD日"）で整形された日付文字列を返します。
*   **`src/generate_repo_list/language_info.py`**
    *   **`get_language_breakdown(repo_data)`**: リポジトリの使用言語情報を分析し、各言語のバイト数や比率などの内訳を計算します。
*   **`src/generate_repo_list/readme_badge_extractor.py`**
    *   **`extract_badges_from_readme(readme_content)`**: READMEファイルのコンテンツから、特定のパターンに合致するバッジ情報（例: リンクや画像URL）を抽出します。
*   **`src/generate_repo_list/statistics_calculator.py`**
    *   **`calculate_repo_statistics(repo_list)`**: リポジトリのリスト全体に対して、合計スター数、フォーク数、最終更新日などの統計情報を計算します。
*   **`src/generate_repo_list/template_processor.py`**
    *   **`render_template(template_path, data)`**: 指定されたテンプレートファイル（例: Markdownテンプレート）に、提供されたデータを適用して最終的なコンテンツを生成します。
*   **`src/generate_repo_list/url_utils.py`**
    *   **`build_github_api_url(username)`**: GitHub APIのユーザーリポジトリエンドポイントのURLを構築します。
    *   **`build_repo_url(username, repo_name)`**: 特定のGitHubリポジトリのウェブURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-20 07:19:51 JST
