Last updated: 2025-11-24

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で取得・整形するシステムです。
- GitHub Pages向けに、検索エンジン最適化されたMarkdown形式のリポジトリ一覧を生成します。
- 検索エンジンやLLMからの参照性を向上させ、プロジェクトの認知度向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesで静的サイトを生成するためのエンジン), Markdown (コンテンツ記述言語)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: Python (主要な開発言語), GitHub API (リポジトリ情報取得のためのインターフェース), YAML (設定ファイルの記述形式)
- テスト: pytest (Pythonアプリケーションのテストフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIから取得した情報をもとにMarkdownファイルを自動生成するカスタムビルドロジック)
- 言語機能: Python (ファイルI/O、ネットワーク通信、データ処理など、スクリプトの実行環境として使用)
- 自動化・CI/CD: GitHub Actions (生成されたMarkdownのデプロイなど、継続的な統合およびデリバリーを自動化するために利用される可能性)
- 開発標準: ruff (Pythonコードのフォーマッタおよびリンターで、コード品質とスタイルの一貫性を保つために使用)

## ファイル階層ツリー
```
📄 .editorconfig
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
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 2.md
  📖 4.md
  📖 6.md
  📖 8.md
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
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
-   `.editorconfig`: 異なるテキストエディタ間での一貫したコーディングスタイルを維持するための設定ファイルです。
-   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
-   `LICENSE`: 本プロジェクトのライセンス情報（MITライセンス）を記載しています。
-   `README.md`: プロジェクトの概要、目的、セットアップ方法、使い方、設定、開発者向けのヒントなどが記述されたメインのドキュメントです。
-   `_config.yml`: Jekyllサイト全体の設定を定義するファイルで、GitHub Pagesのサイト動作に影響します。
-   `assets/`: ウェブサイトで使用されるファビコン画像などの静的アセットを格納するディレクトリです。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なる解像度のウェブサイトアイコンを提供し、デバイスやブラウザでの表示に対応します。
-   `debug_project_overview.py`: `project_overview_fetcher.py`モジュールのデバッグや単体テストを行うためのスクリプトです。
-   `generated-docs/`: リポジトリごとに自動生成されたドキュメント（例: `project-overview.md`）を格納することを想定したディレクトリです。
-   `index.md`: スクリプトによって生成されたリポジトリ一覧が書き込まれる最終的なMarkdownファイルで、GitHub Pagesのトップページとして機能します。
-   `issue-notes/`: 開発中に記録されたIssueに関連するメモや補足情報を格納するディレクトリです。
    -   `10.md`, `12.md`, `14.md`, `2.md`, `4.md`, `6.md`, `8.md`: 各Issue番号に対応する詳細なメモファイルです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のメタデータを定義し、ウェブアプリがホーム画面に追加された際の表示設定などを指定します。
-   `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイルです。
-   `requirements-dev.txt`: 開発およびテスト時に必要なPythonパッケージとそのバージョンを定義します。
-   `requirements.txt`: 本番環境でこのプロジェクトを実行する際に必要なPythonパッケージとそのバージョンを定義します。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか指示するファイルです。
-   `ruff.toml`: Pythonコードのリンターおよびフォーマッターである`ruff`の設定ファイルで、コードスタイルの自動修正やチェックルールを定義します。
-   `src/`: プロジェクトの主要なソースコードを格納するルートディレクトリです。
    -   `__init__.py`: `src`ディレクトリがPythonパッケージであることを示します。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成機能の中核を担うモジュール群を格納するパッケージです。
        -   `__init__.py`: `generate_repo_list`パッケージであることを示します。
        -   `badge_generator.py`: リポジトリの状態（例: アクティブ、アーカイブ済み、フォーク）に応じたバッジのMarkdownを生成するロジックを含みます。
        -   `config.yml`: プロジェクトの実行時設定（例: APIタイムアウト、キャッシュ設定、プロジェクト概要取得機能のON/OFF）を定義するYAMLファイルです。
        -   `config_manager.py`: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのユーティリティ関数を提供します。
        -   `generate_repo_list.py`: このプロジェクトのメインエントリーポイントとなるスクリプトで、コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成までの一連の流れを統括します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために使用される、JSON-LD形式の構造化データテンプレートです。
        -   `language_info.py`: GitHubリポジトリの言語使用に関する情報を取得し、整形するためのロジックを含みます。
        -   `markdown_generator.py`: 取得・整形されたリポジトリ情報から、最終的なMarkdownコンテンツを生成するロジックを担当します。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で取得する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを管理します。
        -   `seo_template.yml`: SEO関連のメタデータや、Markdown生成時に埋め込まれるテンプレートの内容を定義するYAMLファイルです。
        -   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算または整形するロジックを含みます。
        -   `strings.yml`: アプリケーションで表示される各種メッセージやラベルなどの文字列を一元管理するYAMLファイルです。
        -   `template_processor.py`: Markdown生成時に使用されるテンプレートを処理し、データと結合して最終的な文字列を生成するユーティリティです。
        -   `url_utils.py`: GitHub APIエンドポイントやリポジトリURLの構築など、URL関連のユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher.py`モジュールが正しく機能するかを確認するためのテストスクリプトです。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリです。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテストを含みます。
    -   `test_environment.py`: プロジェクトの実行環境や依存関係が正しく設定されているかを検証するテストです。
    -   `test_integration.py`: 複数のモジュールが連携して動作する際の統合的なテストを行います。
    -   `test_markdown_generator.py`: `markdown_generator.py`が正しいMarkdownを生成するかを検証するテストです。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher.py`が期待通りにプロジェクト概要を抽出するかをテストします。
    -   `test_repository_processor.py`: `repository_processor.py`がリポジトリデータを正しく処理・整形するかをテストします。

## 関数詳細説明
-   `generate_repo_list.py`:
    -   `main()`: プロジェクトのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連の流れをオーケストレートします。
    -   `parse_arguments()`: コマンドラインから渡される引数（例: `--username`, `--output`, `--limit`）を定義し、解析して返します。
    -   `run_generation(args)`: 解析された引数に基づき、設定の読み込み、GitHub APIからのリポジトリ取得、データ処理、Markdown生成、ファイル出力までの一連の主要な処理を実行します。
-   `config_manager.py`:
    -   `load_config(config_path)`: 指定されたYAML設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書形式で返します。
    -   `get_github_token()`: `secrets/secrets.toml`ファイルまたは環境変数からGitHub APIトークンを安全に取得します。
-   `repository_processor.py`:
    -   `fetch_repositories(username, token)`: 指定されたGitHubユーザー名とAPIトークンを使用して、そのユーザーが所有する公開リポジトリの情報をGitHub APIから取得します。
    -   `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーションの他のモジュールで扱いやすい形式に整形・フィルタリングします。
-   `project_overview_fetcher.py`:
    -   `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリから`generated-docs/project-overview.md`ファイルの内容を取得し、設定に基づいてプロジェクト概要の3行を抽出します。
    -   `extract_overview_lines(content, section_title)`: マークダウン形式のコンテンツから、特定のセクションタイトル（例: "プロジェクト概要"）以下の最初の3行を抽出します。
-   `markdown_generator.py`:
    -   `generate_markdown(repos_data, config)`: 整形されたリポジトリデータのリストと設定情報をもとに、GitHub Pages用の最終的なMarkdownコンテンツ全体を生成します。
    -   `generate_repo_section(repo, config)`: 個々のリポジトリデータを受け取り、そのリポジトリの情報を表示するためのMarkdown形式のセクション（タイトル、概要、バッジなど）を生成します。
-   `badge_generator.py`:
    -   `generate_badge(status)`: リポジトリのステータス（例: "active", "archived", "forked"）に応じて、対応するバッジのMarkdown文字列を生成します。
-   `language_info.py`:
    -   `get_language_breakdown(repo_name, owner, token)`: 指定されたリポジトリの言語使用状況をGitHub APIから取得し、主要な言語とその割合などの情報として整形して返します。
-   `statistics_calculator.py`:
    -   `calculate_repo_statistics(repo)`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算またはフォーマットし、表示に適した形式で提供します。
-   `template_processor.py`:
    -   `render_template(template_string, data)`: プレースホルダーを含むテンプレート文字列と、それらに置き換えるデータを受け取り、最終的な文字列を生成します。
-   `url_utils.py`:
    -   `build_github_api_url(endpoint, **params)`: GitHub APIのエンドポイントとクエリパラメータを受け取り、完全なAPIリクエストURLを構築します。
    -   `build_repo_url(owner, repo_name)`: GitHubリポジトリのウェブページURL（例: `https://github.com/<owner>/<repo_name>`）を構築します。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
└── parse_arguments()
└── run_generation(args)
    ├── config_manager.load_config(config_path)
    ├── config_manager.get_github_token()
    ├── repository_processor.fetch_repositories(username, token)
    │   └── url_utils.build_github_api_url(...)
    ├── (各リポジトリに対してループ)
    │   ├── repository_processor.process_repository_data(repo_data)
    │   ├── project_overview_fetcher.fetch_project_overview(repo_name, owner, config)
    │   │   └── project_overview_fetcher.extract_overview_lines(content, section_title)
    │   ├── badge_generator.generate_badge(status)
    │   ├── language_info.get_language_breakdown(repo_name, owner, token)
    │   ├── statistics_calculator.calculate_repo_statistics(repo)
    │   └── markdown_generator.generate_repo_section(repo, config)
    │       └── template_processor.render_template(template_string, data)
    └── markdown_generator.generate_markdown(repos_data, config)
        └── template_processor.render_template(template_string, data)

---
Generated at: 2025-11-24 07:06:04 JST
