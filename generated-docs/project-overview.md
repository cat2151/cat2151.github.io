Last updated: 2025-11-28

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、自身のGitHubリポジトリ一覧を自動で取得・生成します。
- 生成されたリポジトリ一覧はJekyllベースのGitHub Pagesサイト向けにSEO最適化されたMarkdown形式で出力されます。
- 検索エンジンによるクロールを促進し、LLMがリポジトリ情報を参照しやすくなることで開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (テストフレームワーク), ruff (Pythonコードのリンター・フォーマッター)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Python (スクリプトの実行環境および主要言語)
- 言語機能: Python (バージョン3.x系を想定)
- 自動化・CI/CD: (ローカル開発重視のため明示的なCI/CDツールは記述なし)
- 開発標準: ruff (Pythonコードのスタイルガイド強制および静的解析)

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コードなどのコードフォーマット設定を統一するためのファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: ビルド生成物、ログファイル、一時ファイルなど）を指定するためのファイルです。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。プロジェクトの利用条件を明確にします。
- **README.md**: プロジェクトの目的、機能、使い方、設定方法、実行コマンドなど、概要を説明する主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン設定などを定義します。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。`favicon`が格納されています。
- **debug_project_overview.py**: プロジェクト概要取得機能の動作を個別に確認するためのデバッグ用スクリプトです。
- **generated-docs/**: 自動生成されたドキュメントやデータが格納される場所を想定したディレクトリです（例: 各リポジトリの`project-overview.md`が参照される）。
- **index.md**: 生成されたリポジトリ一覧が書き込まれるメインのMarkdownファイルです。GitHub Pagesサイトのトップページとして機能します。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを記録するためのMarkdownファイル群が格納されているディレクトリです。
- **manifest.json**: Progressive Web App (PWA) の設定を定義するJSONファイルです。アプリの表示名、アイコン、起動方法などをブラウザに伝えます。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を記述するファイルです。
- **requirements-dev.txt**: 開発時およびテスト実行時に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: 本番環境で本プロジェクトを実行するために必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンのウェブクローラーに対し、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonの高速リンター・フォーマッターである`ruff`の設定ファイルです。コードの品質と一貫性を保つためのルールを定義します。
- **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを管理するモジュールです。
- **src/generate_repo_list/config.yml**: プロジェクト概要取得機能など、本システムの技術的なパラメータや動作設定を記述するYAML形式の設定ファイルです。
- **src/generate_repo_list/config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム全体で利用できるように管理するモジュールです。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、それを処理してMarkdown形式のリポジトリ一覧を生成する、本プロジェクトのメイン実行スクリプトです。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のため、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
- **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を取得、処理、整形するロジックを含むモジュールです。
- **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報に基づいて、最終的なMarkdownコンテンツ（リポジトリ一覧）を生成する役割を担うモジュールです。
- **src/generate_repo_list/project_overview_fetcher.py**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの概要テキストを抽出するモジュールです。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータをフィルタリング、整形、追加情報付与などの処理を行うモジュールです。
- **src/generate_repo_list/seo_template.yml**: SEO関連のメタデータや表示設定を定義するためのテンプレートファイルです。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュールです。
- **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、文言などを一元的に管理するためのYAML形式のファイルです。多言語対応や文言の一貫性を保つために利用されます。
- **src/generate_repo_list/template_processor.py**: MarkdownやJSON-LDなどのテンプレートファイルを読み込み、動的なデータで埋め込んで最終的な出力を生成するモジュールです。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールで定義されたプロジェクト概要取得機能の単体テストを記述したスクリプトです。
- **tests/**: プロジェクト全体のテストコードを格納するためのディレクトリです。
- **tests/test_config.py**: 設定ファイルの読み込みや管理機能の正確性を検証するテストケースを含むファイルです。
- **tests/test_environment.py**: 実行環境のセットアップや外部依存関係（例: 環境変数、GitHubトークン）が適切に構成されているかを検証するテストファイルです。
- **tests/test_integration.py**: プロジェクト内の複数のモジュールが連携して正しく動作するかを確認する統合テストを含むファイルです。
- **tests/test_markdown_generator.py**: `markdown_generator.py`で定義されたMarkdown生成ロジックの正確性を検証するテストファイルです。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher.py`モジュールの機能（特にリモートからのファイル内容取得と解析）を検証するテストファイルです。
- **tests/test_repository_processor.py**: `repository_processor.py`モジュールによるリポジトリデータの処理（フィルタリング、整形など）の正確性を検証するテストファイルです。

## 関数詳細説明
このプロジェクトはPythonスクリプトとして動作し、主に以下の種類の関数が利用されると推測されます。具体的な引数や戻り値はソースコードがないため一般的な説明に留まります。

- **generate_repo_list.py 内の関数**:
    - `main()`: プログラムのエントリーポイント。コマンドライン引数の解析、GitHub APIからのリポジトリ取得、データ処理、Markdown生成といった一連の処理を統括します。
    - `parse_arguments()`: コマンドライン引数（`--username`, `--output`, `--limit`など）を解析し、プログラムが利用する設定値を生成します。
- **repository_processor.py 内の関数**:
    - `fetch_repositories(username, token)`: 指定されたGitHubユーザー名と認証トークンを使用して、GitHub APIからユーザーのリポジトリ情報を取得します。
    - `process_repository_data(repositories, config)`: 取得した生のリポジトリデータに対して、フィルタリング（フォーク、アーカイブなど）、分類、追加情報の付与などの処理を行い、Markdown生成に適した形式に整形します。
- **project_overview_fetcher.py 内の関数**:
    - `fetch_project_overview(repo_url, target_file, section_title)`: 特定のリポジトリの指定されたパスにあるMarkdownファイル（例: `generated-docs/project-overview.md`）から、特定のセクション（例: "プロジェクト概要"）の3行の説明を抽出して返します。
- **markdown_generator.py 内の関数**:
    - `generate_repo_markdown(processed_repos, template_config)`: 処理済みのリポジトリ情報とテンプレート設定に基づき、GitHub Pagesサイト用のリポジトリ一覧をMarkdown形式で生成します。
- **config_manager.py 内の関数**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、その内容をPythonのデータ構造（辞書など）として提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2025-11-28 07:05:58 JST
