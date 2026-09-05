Last updated: 2026-09-06

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、JekyllベースのGitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照を促進する目的で設計されています。
- 各リポジトリの概要表示やSEO最適化されたMarkdown生成などの機能を備えています。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesで静的サイトを構築するための静的サイトジェネレーター。本プロジェクトで生成されるMarkdownがJekyllによって処理されます。
    - Markdown: GitHub Pagesで表示されるリポジトリ一覧や各リポジトリの情報を記述するための軽量マークアップ言語。
- 音楽・オーディオ: なし
- 開発ツール:
    - GitHub API: GitHub上のリポジトリ情報をプログラム的に取得するためのインターフェース。
    - Git: ソースコードのバージョン管理システム。（GitHubプロジェクトであるため暗黙的に使用されます）
- テスト:
    - pytest: Pythonで書かれたテストコードを実行するためのフレームワーク。
- ビルドツール:
    - Pythonスクリプト: GitHub APIからの情報取得、データの加工、Markdownファイルの自動生成を行う主要なロジックを担います。
- 言語機能:
    - Python: プロジェクトの主要な開発言語。GitHub APIとの連携やMarkdown生成ロジックの実装に使用されます。
- 自動化・CI/CD:
    - GitHub Actions (示唆): `.github_automation/check_large_files` ディレクトリの存在から、特定のアクション（例: 大容量ファイルチェック）がGitHub Actionsとして実行される可能性が示唆されます。ただし、本プロジェクト自体は「CI/CD不要のローカル開発重視」とされています。
- 開発標準:
    - ruff: Pythonコードの静的解析ツールおよびフォーマッター。コードスタイルの統一と品質向上に貢献します。
    - .editorconfig: 異なるエディタやIDE間で一貫したコーディングスタイルを定義するためのファイル。

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
-   `.editorconfig`: コードエディタの各種設定（インデント、文字コードなど）を統一するための設定ファイル。
-   `.github_automation/check_large_files/`: GitHub Actionsなどで実行される大容量ファイルチェック関連のスクリプトと設定を格納するディレクトリ。
    -   `README.md`: `check_large_files`機能に関する説明ドキュメント。
    -   `check-large-files.toml`: 大容量ファイルの検出ルールを設定するTOML形式の設定ファイル。
    -   `scripts/check_large_files.py`: 指定されたリポジトリ内で設定された上限を超える大容量ファイルを検出するPythonスクリプト。
-   `.gitignore`: Gitがバージョン管理の対象から除外するファイルやディレクトリのパターンを定義するファイル。
-   `LICENSE`: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
-   `README.md`: プロジェクトの概要、目的、主な機能、クイックスタートガイド、設定方法、開発者向けヒントなどを記述した、プロジェクトの顔となるドキュメント。
-   `_config.yml`: Jekyllサイト全体の挙動を設定するためのファイル。GitHub Pagesのサイト構成を定義します。
-   `assets/`: サイトで使用されるファビコン（ウェブサイトアイコン）などの静的アセットを格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトの各種サイズのファビコン画像ファイル。
-   `debug_project_overview.py`: `project_overview_fetcher`モジュールのデバッグやテスト実行に特化したスクリプト。
-   `generated-docs/`: プロジェクトによって自動生成されたドキュメント（例：各リポジトリの概要ファイル）を格納するためのプレースホルダーディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleにおけるサイト所有権の確認に使用されるHTMLファイル。
-   `index.md`: メインのGitHub Pagesサイトのトップページとして機能するMarkdownファイル。本プロジェクトにより自動生成されたリポジトリ一覧が含まれます。
-   `issue-notes/22.md`: 特定の課題（Issue #22）に関するメモや詳細を記述したファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名称、アイコン、表示モードなど）を定義するファイル。
-   `pytest.ini`: pytestフレームワークのテスト実行設定をカスタマイズするための設定ファイル。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
-   `requirements.txt`: プロジェクトの実行（本番環境）に必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
-   `robots.txt`: 検索エンジンクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいは避けるべきかを指示するファイル。
-   `ruff.toml`: Pythonコードのリンティング（静的解析）とフォーマットを行う`ruff`ツールの設定ファイル。コード品質と一貫性の維持に貢献します。
-   `src/`: プロジェクトの主要なソースコードが配置されるディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示す空ファイル。
    -   `generate_repo_list/`: GitHubリポジトリ一覧生成ロジックをカプセル化したPythonサブパッケージ。
        -   `__init__.py`: `generate_repo_list`がPythonサブパッケージであることを示すファイル。
        -   `badge_generator.py`: リポジトリの特性（言語、ライセンス、ステータスなど）に応じたバッジ（例: Shields.io形式）のMarkdown文字列を生成するモジュール。
        -   `config.yml`: プロジェクト概要の取得設定など、技術的なパラメータを定義するYAML形式の設定ファイル。
        -   `config_manager.py`: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、管理するためのユーティリティモジュール。
        -   `date_formatter.py`: 日付や時刻の情報を指定された形式（例：最終更新日）に整形するための関数を提供するモジュール。
        -   `generate_repo_list.py`: このプロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、加工してMarkdown形式で出力する一連の処理を実行します。
        -   `json_ld_template.json`: SEOを強化するために、構造化データ（JSON-LD形式）のテンプレートを定義するファイル。
        -   `language_info.py`: GitHubから取得したリポジトリのプログラミング言語情報を処理し、表示に適した形式に変換するモジュール。
        -   `markdown_generator.py`: 加工されたリポジトリデータを受け取り、SEOを考慮したMarkdown形式の文字列を生成するモジュール。
        -   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出し取得するモジュール。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータスバッジ）を抽出するためのモジュール。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、フィルタリング、必要な情報の抽出、付加情報の追加などを行って、表示に適した形式に加工するモジュール。
        -   `seo_template.yml`: SEO関連のメタデータや、Markdown生成時に使用されるSEOに配慮したテンプレート設定を定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリの星の数、フォーク数、コミット数などの統計情報を計算・集計するモジュール。
        -   `strings.yml`: サイトの表示メッセージ、ボタンの文言、カテゴリ名など、ユーザーインターフェースに関連する文字列を一元管理するためのYAMLファイル。
        -   `template_processor.py`: テンプレートファイルと動的なデータを用いて、最終的なコンテンツ（Markdownなど）を生成する汎用的なテンプレート処理モジュール。
        -   `url_utils.py`: URLの構築、パース、エンコードなど、URLに関連する様々なユーティリティ関数を提供するモジュール。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールの機能に関する単体テストスクリプト。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    -   `conftest.py`: pytestのテストフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイル。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの統合テスト。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能のテストスクリプト。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテスト。
    -   `test_date_formatter.py`: 日付フォーマット関数のテスト。
    -   `test_environment.py`: 実行環境のセットアップや依存関係に関するテスト。
    -   `test_integration.py`: プロジェクト全体のエンドツーエンドの統合テスト。
    -   `test_markdown_generator.py`: Markdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテスト。
    -   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテスト。
    -   `test_repository_processor.py`: リポジトリデータ処理機能のテスト。

## 関数詳細説明
提供された情報では個別の関数名とその詳細なシグネチャは特定できませんが、各モジュールの役割から主要な関数とその機能を推測して説明します。

-   `badge_generator.py` 内の関数:
    -   役割: リポジトリの特定の属性（言語、ライセンス、アーカイブ状態など）に基づいて、視覚的なバッジのMarkdown文字列を生成します。
    -   引数: リポジトリ情報（辞書形式）、バッジの種類やスタイル設定など。
    -   戻り値: バッジを表示するためのMarkdown形式の文字列。
    -   機能: リポジトリのメタデータを解析し、 Shields.io などのサービスを利用したバッジのURLを生成し、Markdown形式で出力します。
-   `config_manager.py` 内の関数:
    -   役割: YAML形式の設定ファイル（例: `config.yml`, `strings.yml`）を読み込み、アプリケーション内でアクセスしやすい形式（例: 辞書やオブジェクト）で提供します。
    -   引数: 読み込む設定ファイルのパス。
    -   戻り値: 設定内容を含むPythonの辞書またはオブジェクト。
    -   機能: ファイルシステムから設定ファイルを安全に読み込み、パースして、アプリケーションの他の部分が設定値にアクセスできるようにします。
-   `date_formatter.py` 内の関数:
    -   役割: 日付/時刻データを、人間が読みやすい特定の文字列形式に変換します（例: リポジトリの最終更新日）。
    -   引数: 日付/時刻オブジェクト（例: `datetime`オブジェクト）、フォーマット文字列（例: `"%Y-%m-%d"`）。
    -   戻り値: フォーマットされた日付を表す文字列。
    -   機能: 標準ライブラリの日付フォーマット機能を利用し、様々な日付表示ニーズに対応します。
-   `generate_repo_list.py` 内の関数 (メイン実行関数):
    -   役割: プロジェクト全体の処理フローを統括します。GitHub APIからのリポジトリ情報取得、データ加工、Markdown生成、ファイル出力までを実行します。
    -   引数: `username` (GitHubユーザー名), `output` (出力ファイル名), `limit` (処理するリポジトリ数の上限、開発用) など、コマンドライン引数で渡されるパラメータ。
    -   戻り値: なし（処理結果としてMarkdownファイルを出力します）。
    -   機能: `config_manager`, `repository_processor`, `project_overview_fetcher`, `markdown_generator` などの各モジュールと連携し、リポジトリ一覧の自動生成をエンドツーエンドで実行します。
-   `language_info.py` 内の関数:
    -   役割: GitHub APIから取得したリポジトリのプログラミング言語情報（使用言語とその割合）を解析し、表示に適した形式（例: 主要言語、色の情報）で提供します。
    -   引数: GitHub APIから提供される言語データ（通常は辞書形式）。
    -   戻り値: 処理された言語情報を含む辞書やリスト。
    -   機能: リポジトリの使用言語を分析し、Markdown表示やUIでの利用に適した情報を抽出・整形します。
-   `markdown_generator.py` 内の関数:
    -   役割: 構造化されたリポジトリデータを受け取り、SEO最適化されたMarkdown形式のコンテンツを生成します。
    -   引数: 処理済みリポジトリデータのリスト、SEOテンプレート情報、その他の設定。
    -   戻り値: 生成されたMarkdown文字列。
    -   機能: 適切なMarkdown構文（ヘッダー、リスト、リンク、コードブロックなど）を用いて、リポジトリ一覧ページや個々のリポジトリの詳細コンテンツを構築します。
-   `project_overview_fetcher.py` 内の関数:
    -   役割: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、「プロジェクト概要」セクションの3行説明を自動で取得・抽出します。
    -   引数: リポジトリ名、対象ファイルのパス、抽出対象セクションのタイトル、GitHubトークン、キャッシュ有効/無効設定など。
    -   戻り値: 抽出された3行の概要テキストのリスト、または取得できなかった場合はNone。
    -   機能: GitHub APIを介してリモートファイルを読み込み、指定されたセクションから内容をパースして概要を抽出します。API呼び出しの失敗時のリトライや、実行中のキャッシュ機能も備えます。
-   `readme_badge_extractor.py` 内の関数:
    -   役割: リポジトリの`README.md`ファイルの内容から、特定の形式（例: Shields.io）のバッジ情報を抽出します。
    -   引数: `README.md`ファイルのテキスト内容。
    -   戻り値: 抽出されたバッジのURLやALTテキストなどの情報を含むリスト。
    -   機能: 正規表現などを用いて、`README.md`テキスト内からバッジのMarkdownリンクを識別し、その情報を解析します。
-   `repository_processor.py` 内の関数:
    -   役割: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、アプリケーションの表示ロジックに適した内部データ構造に変換・加工します。
    -   引数: GitHub APIから返される生のリポジトリデータ、フィルタリングや処理に関する設定。
    -   戻り値: フィルタリング、整形、付加情報が追加されたリポジトリ情報のリスト。
    -   機能: リポジトリのフィルタリング（アーカイブ済み、フォークの有無など）、必要な情報の抽出、`project_overview_fetcher`による概要追加、`badge_generator`によるバッジ情報追加などを行います。
-   `statistics_calculator.py` 内の関数:
    -   役割: リポジトリの星の数、フォーク数、コミット数などの数値データを集計し、統計情報として提供します。
    -   引数: 処理済みリポジトリデータのリスト。
    -   戻り値: 計算された合計や平均などの統計データ。
    -   機能: リポジトリの活動状況や人気度に関する数値的な洞察を提供するためにデータを集計します。
-   `template_processor.py` 内の関数:
    -   役割: テンプレートファイル（例: Markdownテンプレート、JSON-LDテンプレート）と動的なデータを使用して、最終的なテキスト出力を生成します。
    -   引数: テンプレートのパスまたは文字列、テンプレートに埋め込むデータコンテキスト。
    -   戻り値: テンプレートがデータでレンダリングされた結果の文字列。
    -   機能: Liquidテンプレートエンジン（Jekyllで使われる）やJinja2のような仕組みを模倣し、コンテンツの動的な生成を可能にします。
-   `url_utils.py` 内の関数:
    -   役割: URLの構築、パース、エンコード、デコードなど、URLに関連する様々なユーティリティ機能を提供します。
    -   引数: URLの構成要素（ベースURL、パス、クエリパラメータなど）。
    -   戻り値: 処理されたURL文字列。
    -   機能: GitHubリポジトリのURL、APIエンドポイントURL、その他ウェブリンクの正確な生成と操作をサポートします。

## 関数呼び出し階層ツリー
```
# 提供された情報からは具体的な関数呼び出し階層を詳細に分析できませんでした。
# しかし、プロジェクトのメインスクリプトとその主要な依存関係から、
# 以下のような大まかな呼び出しフローが推測されます。

generate_repo_list.py (メイン実行スクリプト)
├── config_manager.py の設定読み込み関数 (初期設定のロード)
├── repository_processor.py のリポジトリ処理関数 (GitHub APIから取得したデータを加工)
│   ├── project_overview_fetcher.py の概要取得関数 (各リポジトリの概要をリモートから取得)
│   ├── readme_badge_extractor.py のバッジ抽出関数 (READMEからバッジ情報を解析)
│   └── language_info.py の言語情報処理関数 (リポジトリの言語データを整形)
├── markdown_generator.py のMarkdown生成関数 (加工済みデータからMarkdownを構築)
│   ├── badge_generator.py のバッジ生成関数 (Markdown内に埋め込むバッジを生成)
│   ├── date_formatter.py の日付フォーマット関数 (日付表示を整形)
│   └── template_processor.py のテンプレート処理関数 (Markdownテンプレートを適用)
├── statistics_calculator.py の統計計算関数 (リポジトリの統計情報を集計)
└── url_utils.py のURLユーティリティ関数 (URLの生成や操作を補助)

---
Generated at: 2026-09-06 07:10:37 JST
