Last updated: 2025-11-23

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、自身のGitHubリポジトリ一覧を自動生成します。
- 生成されたリポジトリ一覧は、JekyllベースのGitHub Pagesサイトに最適化されています。
- 検索エンジンからの発見性を高め、LLMがリポジトリ情報を参照しやすくなることを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレーターとして利用し、生成されたMarkdownコンテンツを表示します), Markdown (生成されるコンテンツのフォーマットです)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: pytest (Pythonコードのテストを実行するためのフレームワークです), ruff (Pythonコードの品質を維持し、スタイルを統一するためのリンターおよびフォーマッターです)
- テスト: pytest (Pythonコードの単体テスト、結合テストを実行するためのフレームワークです)
- ビルドツール: Python (プロジェクトのスクリプト実行環境として、GitHub APIからのデータ取得やMarkdownファイルの生成処理を行います)
- 言語機能: Python (プロジェクトの主要な開発言語です)
- 自動化・CI/CD: このプロジェクト自体はローカルでの開発・実行を重視していますが、生成されたコンテンツはGitHub Pagesで利用されるため、間接的にGitHub Actionsなどと連携してデプロイされることを想定しています。
- 開発標準: ruff (Pythonコードの品質と一貫性を保証するためのツールです)

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
-   `.editorconfig`: 異なる開発環境間でコードのインデントや文字エンコーディングなど、一貫したコーディングスタイルを適用するための設定ファイルです。
-   `.gitignore`: Gitのバージョン管理から除外すべきファイルやディレクトリ（例: ビルド成果物、一時ファイル、個人設定など）を指定するファイルです。
-   `LICENSE`: このプロジェクトがMITライセンスの下で提供されていることを示すライセンス情報ファイルです。
-   `README.md`: プロジェクトの概要、目的、主な機能、セットアップ方法、使用方法、ライセンスなどの包括的な情報を提供する主要なドキュメントファイルです。
-   `_config.yml`: Jekyllサイト全体の設定を定義するファイルで、サイトのタイトル、テーマ、プラグインなどの構成情報を含みます。
-   `assets/`: ウェブサイトで使用される静的なアセット（画像、アイコン、CSSファイルなど）を格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示される小さなアイコン）として使用される画像ファイル群です。
-   `debug_project_overview.py`: プロジェクト概要取得機能のデバッグやテストを目的とした補助スクリプトです。
-   `generated-docs/`: 他のリポジトリから取得した`project-overview.md`などのドキュメントを一時的にキャッシュしたり、参照したりするためのディレクトリです。
-   `index.md`: このスクリプトによって生成される主要な出力ファイルで、GitHub Pagesサイトのリポジトリ一覧ページとして機能するMarkdownファイルです。
-   `issue-notes/`: 開発中の特定の課題や検討事項に関するメモをMarkdown形式で記録したファイル群を格納するディレクトリです。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリがデバイスのホーム画面に追加された際の表示方法や挙動を定義します。
-   `pytest.ini`: Pythonのテストフレームワークであるpytestの動作設定を定義するファイルです。
-   `requirements-dev.txt`: プロジェクトの開発およびテストフェーズでのみ必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   `requirements.txt`: プロジェクトが本番環境で実行されるために必要となるPythonパッケージの依存関係をリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、あるいはクロールすべきでないかを指示するファイルです。SEO対策に利用されます。
-   `ruff.toml`: Pythonコードのスタイルチェックと自動フォーマットを行うツール「Ruff」の設定ファイルです。
-   `src/`: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    -   `__init__.py`: Pythonパッケージを識別するための特殊なファイルで、`src`ディレクトリをPythonパッケージとして扱います。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成機能の中核をなすモジュール群を格納するパッケージディレクトリです。
        -   `__init__.py`: `generate_repo_list`パッケージを識別するためのファイルです。
        -   `badge_generator.py`: リポジトリのステータス（例: アクティブ、アーカイブ）や言語に応じた表示バッジの生成ロジックを管理するファイルです。
        -   `config.yml`: リポジトリ一覧生成スクリプトの動作に関する設定パラメータ（例: プロジェクト概要取得の有効/無効、タイムアウト値など）を定義するYAMLファイルです。
        -   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理する機能を提供するファイルです。
        -   `generate_repo_list.py`: このプロジェクトのメインエントリーポイントとなるスクリプトです。GitHub APIからリポジトリ情報を取得し、加工して最終的なMarkdownファイルを生成する一連の処理を実行します。
        -   `json_ld_template.json`: 検索エンジン最適化（SEO）のために、リポジトリ情報をJSON-LD形式の構造化データとして埋め込むためのテンプレートファイルです。
        -   `language_info.py`: GitHubリポジトリのプログラミング言語情報を解析、集計、整形する機能を提供するファイルです。
        -   `markdown_generator.py`: 取得・加工されたリポジトリデータに基づいて、Jekyll互換のMarkdown形式のコンテンツを生成するロジックを含むファイルです。
        -   `project_overview_fetcher.py`: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの簡潔な概要説明を自動的に抽出し取得する機能を提供するファイルです。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に整形・フィルタリングするロジックを含むファイルです。
        -   `seo_template.yml`: サイトのSEOメタデータや、生成されるMarkdownファイルに挿入されるSEO関連の要素を定義するYAMLテンプレートファイルです。
        -   `statistics_calculator.py`: リポジトリに関するさまざまな統計情報（例: スター数、フォーク数）を計算する機能を提供するファイルです。
        -   `strings.yml`: アプリケーション内で表示される様々なテキストメッセージや文言を一元的に管理するためのYAMLファイルです。これにより、文言の変更や多言語対応が容易になります。
        -   `template_processor.py`: Markdown生成時に使用されるLiquidテンプレートなどの処理、データバインディングを行う機能を提供するファイルです。
        -   `url_utils.py`: URLの構築、検証、エンコードなどのURLに関連するユーティリティ関数を集めたファイルです。
-   `test_project_overview.py`: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するためのテストコードです。
-   `tests/`: プロジェクトの各種モジュールや機能に対するテストスクリプトが格納されているディレクトリです。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関する機能のテストです。
    -   `test_environment.py`: 環境設定や依存関係が正しく設定されているかを検証するテストです。
    -   `test_integration.py`: `generate_repo_list`パッケージ内の複数のモジュールが連携して正しく動作するかを検証する統合テストです。
    -   `test_markdown_generator.py`: Markdown生成ロジックが期待通りの出力を生成するかを検証するテストです。
    -   `test_project_overview_fetcher.py`: プロジェクト概要の取得ロジックが正しく動作するかを検証するテストです。
    -   `test_repository_processor.py`: リポジトリ情報の加工ロジックが正しく動作するかを検証するテストです。

## 関数詳細説明
提供された情報では個々の関数の具体的な詳細（引数、戻り値、実装）は不明確であるため、各ファイルが担う主要な役割に基づいて想定される機能単位で説明します。

-   **`generate_repo_list.py`内の主要関数 (例: `main`関数)**
    -   **役割**: プロジェクト全体の実行フローを制御し、GitHub APIからのリポジトリ情報取得、データ加工、Markdown生成の一連のプロセスをオーケストレートします。
    -   **引数**: コマンドライン引数（例: `username`, `output`, `limit`など）を解析し、内部処理に渡します。
    -   **戻り値**: 通常はNoneですが、処理の成功/失敗を示すステータスコードを返す場合があります。
    -   **機能**: 設定の読み込み、GitHub APIクライアントの初期化、リポジトリ情報のフェッチ、各データ処理モジュールへの委譲、最終的なMarkdownファイルの書き出しを行います。

-   **`config_manager.py`内の主要関数 (例: `load_config`)**
    -   **役割**: YAML形式の設定ファイルを読み込み、アプリケーションが利用できるデータ構造に変換します。
    -   **引数**: 設定ファイルのパスなどが想定されます。
    -   **戻り値**: 読み込まれた設定内容を含む辞書やオブジェクト。
    -   **機能**: 指定されたパスからYAMLファイルを解析し、設定情報を安全に取得・提供します。

-   **`repository_processor.py`内の主要関数 (例: `process_repositories`)**
    -   **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に整形・フィルタリングします。
    -   **引数**: 生のGitHubリポジトリデータ（JSON形式など）。
    -   **戻り値**: 整形され、必要な情報のみが抽出されたリポジトリデータのリスト。
    -   **機能**: リポジトリの公開/非公開、フォーク、アーカイブ状態に基づいてフィルタリングを行い、必要な属性（名前、説明、言語、スター数など）を抽出・標準化します。

-   **`project_overview_fetcher.py`内の主要関数 (例: `fetch_project_overview`)**
    -   **役割**: 特定のリポジトリ内の指定されたファイル（`generated-docs/project-overview.md`）から、プロジェクトの概要説明を抽出します。
    -   **引数**: リポジトリ名、ファイルパス、抽出対象のセクションタイトルなど。
    -   **戻り値**: 抽出された3行のプロジェクト概要（文字列のリスト）。
    -   **機能**: GitHub APIを介してリポジトリコンテンツを取得し、Markdownファイルを解析して指定されたセクションからテキストを抽出します。キャッシュ機能やリトライ処理も含まれます。

-   **`markdown_generator.py`内の主要関数 (例: `generate_markdown`)**
    -   **役割**: 整形されたリポジトリデータを用いて、GitHub Pages向けのMarkdownコンテンツを生成します。
    -   **引数**: 処理済みのリポジトリデータのリスト、テンプレート情報、その他の表示オプション。
    -   **戻り値**: 生成されたMarkdown文字列。
    -   **機能**: 提供されたリポジトリ情報とテンプレートに基づいて、見出し、リスト、バッジ、リンクなどを含む構造化されたMarkdownドキュメントを構築します。

-   **`badge_generator.py`内の主要関数 (例: `get_status_badge`)**
    -   **役割**: リポジトリの状態（アクティブ、アーカイブなど）に応じて、表示用のバッジ情報を生成します。
    -   **引数**: リポジトリのステータス情報。
    -   **戻り値**: バッジのテキスト、色、URLなどの情報を含むオブジェクトまたは辞書。
    -   **機能**: 定義されたルールに基づき、リポジトリの状態を視覚的に表現するバッジデータを生成します。

-   **`template_processor.py`内の主要関数 (例: `render_template`)**
    -   **役割**: Markdown生成に使用されるテンプレートに動的なデータを適用し、最終的なコンテンツをレンダリングします。
    -   **引数**: テンプレート文字列またはファイルパス、テンプレートに埋め込むデータ辞書。
    -   **戻り値**: データが適用された結果の文字列。
    -   **機能**: テンプレートエンジン（Pythonの`jinja2`などが考えられる）を利用して、データとテンプレートを結合します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析するための具体的な情報が提供されていないため、ツリーを生成することはできません。

---
Generated at: 2025-11-23 07:06:08 JST
