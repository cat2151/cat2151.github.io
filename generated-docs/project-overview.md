Last updated: 2026-11-03

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動的に取得します。
- 取得した情報からGitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownを生成します。
- これにより、ユーザーのGitHub Pagesサイトの検索エンジンインデックス改善を促進します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトのフレームワークとして), Markdown (リポジトリ一覧生成フォーマット), HTML (生成されるページの基盤)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (主要なスクリプト言語), GitHub API (リポジトリ情報取得), Git (バージョン管理)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得とMarkdown生成のカスタムビルドプロセス)
- 言語機能: Pythonの標準ライブラリと外部ライブラリ (ファイル操作、HTTPリクエスト、データ処理、文字列操作など)
- 自動化・CI/CD: GitHub Pages (静的サイトのホスティング), GitHub Actions (ファイルサイズチェックなどの自動化ワークフロー)
- 開発標準: Ruff (Pythonコードの整形とリンティングツール), .editorconfig (エディタ全体でのコードスタイル統一設定)

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
- **.editorconfig**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いたリポジトリの自動化処理に関するスクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: GitHubリポジトリ内の大規模ファイルを検出し、管理するための機能関連ファイルです。
        - **README.md**: `check_large_files`機能の目的、使用方法、設定について説明するドキュメントです。
        - **check-large-files.toml**: `check_large_files`スクリプトの動作を制御するための設定ファイルです。
        - **scripts/check_large_files.py**: 指定されたしきい値を超える大規模ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（この場合MITライセンス）が記載されています。
- **README.md**: プロジェクトの目的、主な機能、セットアップ方法、実行コマンド、開発者向け情報など、プロジェクト全体に関する概要説明が記述されています。
- **_config.yml**: Jekyllサイトの基本的な設定（テーマ、プラグイン、変数など）を定義するファイルで、GitHub Pagesの動作に影響を与えます。
- **assets/**: GitHub Pagesサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の様々なサイズが格納されています。
- **debug_project_overview.py**: `project_overview`機能の動作検証やデバッグのために使用されるスクリプトです。
- **generated-docs/**: 各リポジトリから取得・生成されたドキュメント（特に`project-overview.md`など）が配置される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成されたリポジトリ一覧のコンテンツが出力されるメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを記録するためのディレクトリです。
    - **22.md**: 特定の課題（Issue #22など）に関する詳細なメモや解決策が記述されているMarkdownファイルです。
- **manifest.json**: Progressive Web App (PWA) の設定ファイルで、ホーム画面への追加、アプリの表示設定などを定義します。
- **pytest.ini**: pytestフレームワークの実行設定（テストファイルの発見パターン、プラグイン、レポートオプションなど）を定義するファイルです。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **requirements.txt**: プロジェクトが本番環境で実行される際に最低限必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてよいか、どの部分を避けるべきかを指示するファイルです。
- **ruff.toml**: PythonコードのリンターおよびフォーマッターであるRuffの設定ファイルです。コードの品質と一貫性を保つために使用されます。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: Pythonパッケージであることを示す空のファイルです。
    - **generate_repo_list/**: GitHubリポジトリ一覧生成のコアロジックを格納するPythonパッケージです。
        - **__init__.py**: Pythonパッケージであることを示す空のファイルです。
        - **badge_generator.py**: リポジトリに表示するバッジ（例: 言語バッジ、ステータスバッジ）を生成するロジックが含まれています。
        - **config.yml**: プロジェクト概要取得機能など、主要な機能の技術的パラメータを設定するYAMLファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
        - **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数が含まれています。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成するメインの実行スクリプトです。
        - **json_ld_template.json**: 構造化データ（JSON-LD形式）のテンプレートファイルで、検索エンジン最適化(SEO)のために使用されます。
        - **language_info.py**: リポジトリが使用しているプログラミング言語に関する情報を処理し、表示するためのロジックが含まれています。
        - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックです。
        - **project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動的に取得するロジックです。
        - **readme_badge_extractor.py**: 各リポジトリの`README.md`ファイルから特定のバッジ情報を抽出するためのロジックです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、表示に必要な情報に加工する主要なロジックです。
        - **seo_template.yml**: 生成されるMarkdownファイルのSEO関連のメタデータ（タイトル、説明など）のテンプレート設定です。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックです。
        - **strings.yml**: UIに表示される各種メッセージや文言を集中管理するYAMLファイルで、国際化/ローカライズに利用できます。
        - **template_processor.py**: Markdown生成の際に使用されるテンプレートエンジン（Jinja2など）を介して、コンテンツをレンダリングするロジックです。
        - **url_utils.py**: GitHubリポジトリへのリンクやAPIエンドポイントなど、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`で実装されているプロジェクト概要取得機能のテストコードです。
- **tests/**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **conftest.py**: pytestの共通フィクスチャやヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: `badge_generator.py`の統合テストコードです。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`のテストコードです。
    - **test_config.py**: `config_manager.py`など、設定関連のロジックのテストコードです。
    - **test_date_formatter.py**: `date_formatter.py`のテストコードです。
    - **test_environment.py**: テスト実行環境に関する設定やチェックを行うテストコードです。
    - **test_integration.py**: プロジェクトの主要なコンポーネントが連携して動作するかを検証する統合テストコードです。
    - **test_markdown_generator.py**: `markdown_generator.py`のテストコードです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`のテストコードです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor.py`のテストコードです。
    - **test_repository_processor.py**: `repository_processor.py`のテストコードです。

## 関数詳細説明
- **googled947dc864c270e07.html**: このファイルには関数は含まれていません。
- **src/generate_repo_list/generate_repo_list.py**:
    - `main()`: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成するプロジェクトの主要な実行関数。
- **src/generate_repo_list/badge_generator.py**:
    - `generate_badge(language: str, count: int) -> str`: 特定の言語や統計情報に基づいて、Markdown形式のバッジ文字列を生成します。
- **src/generate_repo_list/config_manager.py**:
    - `load_config(file_path: str) -> dict`: 指定されたYAMLファイルパスから設定を読み込み、辞書として返します。
    - `get_value(config: dict, key_path: str, default=None)`: 設定辞書から指定されたキーパスの値を取得します。
- **src/generate_repo_list/date_formatter.py**:
    - `format_date(iso_date_string: str) -> str`: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形して返します。
- **src/generate_repo_list/markdown_generator.py**:
    - `generate_repository_list_markdown(repositories: list[dict], config: dict, strings: dict) -> str`: 処理されたリポジトリ情報のリストを受け取り、Jekyllと互換性のあるリポジトリ一覧のMarkdownコンテンツを生成します。
- **src/generate_repo_list/project_overview_fetcher.py**:
    - `fetch_project_overview(repo_url: str, config: dict, cache_enabled: bool = True) -> Optional[list[str]]`: GitHubリポジトリのURLと設定を受け取り、`generated-docs/project-overview.md`から3行のプロジェクト概要をフェッチします。
- **src/generate_repo_list/readme_badge_extractor.py**:
    - `extract_badges_from_readme(readme_content: str) -> list[str]`: リポジトリのREADMEコンテンツから、Markdown形式のバッジリンクを抽出し、リストとして返します。
- **src/generate_repo_list/repository_processor.py**:
    - `fetch_repositories(username: str, github_token: str, limit: Optional[int] = None) -> list[dict]`: 指定されたGitHubユーザー名とトークンを使用して、GitHub APIからリポジトリ情報を取得します。
    - `process_repository_data(repo_data: dict, config: dict) -> dict`: GitHub APIから取得した単一のリポジトリデータを受け取り、表示に必要な形式に加工・整形します。
- **src/generate_repo_list/statistics_calculator.py**:
    - `calculate_language_statistics(repositories: list[dict]) -> dict`: リポジトリのリストから、使用されているプログラミング言語の統計情報（使用割合など）を計算します。
- **src/generate_repo_list/template_processor.py**:
    - `render_template(template_path: str, context: dict) -> str`: 指定されたテンプレートファイルパスとコンテキスト辞書を使用して、Jinja2などのテンプレートエンジンでコンテンツをレンダリングします。
- **src/generate_repo_list/url_utils.py**:
    - `build_github_api_url(username: str) -> str`: GitHubユーザー名に基づいて、リポジトリ情報を取得するためのGitHub APIエンドポイントURLを構築します。
    - `build_github_pages_url(username: str, repo_name: str) -> str`: GitHub PagesのURLを構築します。
- **.github_automation/check_large_files/scripts/check_large_files.py**:
    - `main()`: リポジトリ内のファイルサイズをチェックし、設定された閾値を超えるファイルを報告する主要な実行関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-03 07:08:19 JST
