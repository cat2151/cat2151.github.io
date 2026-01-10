Last updated: 2026-01-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたリポジトリ情報は検索エンジン最適化（SEO）され、LLMによる参照性向上に貢献します。
- 各リポジトリの概要文や技術スタックバッジを自動で取得・表示し、視認性の高いコンテンツを提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) は最終的なホスティング環境であり、出力されるMarkdownファイルがJekyllによって静的サイトとしてレンダリングされます。
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用されていません。
- 開発ツール:
    - Python: メインの開発言語であり、GitHub APIとの連携、ファイル操作、Markdown生成など、システムの中核を担います。
    - GitHub API: GitHubリポジトリのメタデータ（説明、言語、スター数など）をプログラムから取得するために使用されます。
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の読み込み・解析に利用されます。
    - toml: シークレット情報が格納されるTOML形式のファイル (`secrets.toml`) の読み込み・解析に利用されます。
- テスト:
    - pytest: Pythonコードの単体テストおよび結合テストを実行するための強力なテストフレームワークです。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py` がリポジトリ情報を取得し、Markdownファイルを生成するため、実質的なコンテンツビルドツールとして機能します。
- 言語機能:
    - Python: 高度なスクリプティング機能と豊富な標準ライブラリ、そして広範なサードパーティ製パッケージエコシステムにより、本システムの開発を支えています。
- 自動化・CI/CD: このプロジェクト自体に直接的なCI/CDパイプラインの設定は含まれていませんが、生成されるMarkdownファイルはGitHub Pagesの自動デプロイと連携して利用されることが想定されます。
- 開発標準:
    - ruff: Pythonコードのスタイルチェック（リンティング）と自動整形（フォーマット）を行うツールで、コード品質と一貫性を保ちます。
    - .editorconfig: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字コード、行末文字などの基本的なコーディングスタイルを統一するための設定ファイルです。

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
🌐 googled947dc864c270e07.html
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
  📖 16.md
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
    📄 date_formatter.py
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
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なる開発環境でコードのスタイル（インデント、エンコーディングなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitによるバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で提供されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、クイックスタートガイド、設定方法、実行方法など、プロジェクトに関する包括的な情報を提供するメインの説明ファイルです。
- **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルで、GitHub Pagesの動作に影響を与えます。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`**: ウェブサイトのアイコンとして使用される、様々なサイズのファビコン画像です。
- **`debug_project_overview.py`**: `project_overview_fetcher.py` モジュールのデバッグや単体テストに特化したスクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得されたプロジェクト概要ファイル (`project-overview.md`) が一時的に格納されることが想定されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesのルートページ（ホームページ）として機能するメインのMarkdownファイルです。このファイルに自動生成されたリポジトリ一覧が出力されます。
- **`issue-notes/`**: 開発中に発生した課題、検討事項、メモなどをMarkdown形式で記録するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するファイルで、ウェブサイトをデスクトップやモバイルのアプリのようにインストール可能にするためのメタデータを含みます。
- **`pytest.ini`**: `pytest` テストフレームワークの動作を設定するためのファイルです。テストの検出方法やオプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境で必要となるPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: 本番環境でこのシステムを実行するために必要となるPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: `ruff` リンター・フォーマッターの設定ファイルで、Pythonコードのスタイルと品質に関するルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧自動生成システムの主要なロジックを格納するPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例: アーカイブ）や使用言語を示すバッジ（画像またはテキスト）を生成するロジックを含むモジュールです。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能の設定やAPIタイムアウトなど、システムの技術的なパラメータを定義するYAML形式の設定ファイルです。
        - **`src/generate_repo_list/config_manager.py`**: システム全体で使用される設定ファイル（`config.yml`, `strings.yml`, `secrets.toml`など）の読み込み、パース、および管理を行うモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付オブジェクトを様々な形式の文字列（例: `YYYY-MM-DD`, 相対時間）に整形するためのユーティリティ関数を提供するモジュールです。
        - **`src/generate_repo_list/generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、その情報を基にMarkdown形式のリポジトリ一覧ファイルを生成する、本システムのメイン実行スクリプトです。コマンドライン引数の処理も行います。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、リポジトリ情報を構造化データ（JSON-LD）として埋め込む際のテンプレートを定義するJSONファイルです。
        - **`src/generate_repo_list/language_info.py`**: GitHubリポジトリの主要なプログラミング言語とその割合を分析し、表示に適した形式に処理するモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理済みリポジトリデータを受け取り、Jekyllが解釈できる形式のMarkdownコンテンツ（各リポジトリのエントリ、ヘッダー、フッターなど）を生成するモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 他のGitHubリポジトリ内に存在する特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要説明を自動で取得・抽出するモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリJSONデータを受け取り、それをフィルタリング、整形、必要な情報の抽出を行い、Markdown生成に適した内部データ構造に変換するモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレート構造を定義するYAMLファイルで、検索エンジンによるインデックス作成を最適化するために使用されます。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算または集計するユーティリティモジュールです。
        - **`src/generate_repo_list/strings.yml`**: システムの出力メッセージ、UIテキスト、ラベルなど、表示される各種文言を一元的に管理するためのYAMLファイルです。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成プロセスで使用されるテンプレートファイル（部分的なMarkdownスニペットなど）を読み込み、プレースホルダーを実際のデータで置き換える役割を担うモジュールです。
        - **`src/generate_repo_list/url_utils.py`**: GitHubリポジトリへのURL、APIエンドポイント、または関連する静的コンテンツのURLを生成したり解析したりするためのユーティリティ関数を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能に関するテストケースを記述したスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関する機能のテストです。
    - **`test_date_formatter.py`**: 日付フォーマット機能の正確性を検証するテストです。
    - **`test_environment.py`**: 実行環境（例: 必要な環境変数の存在）に関するテストです。
    - **`test_integration.py`**: システムの複数のコンポーネントが連携して正しく動作するかを検証する結合テストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックが正しく機能するかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能の正確性と堅牢性を検証するテストです。
    - **`test_repository_processor.py`**: GitHub APIから取得したリポジトリデータの処理ロジックを検証するテストです。

## 関数詳細説明
このセクションでは、各Pythonモジュール内で定義されている主要な関数の役割と機能について説明します。具体的な引数や戻り値の型はコードベースがないため推測せず、機能の概要に焦点を当てます。

- **`src/generate_repo_list/badge_generator.py`**:
    - **役割**: リポジトリの特性（言語、ステータスなど）を示す視覚的なバッジを生成します。
    - **機能**: 入力された情報（例: 言語名、アーカイブ状態）に基づいて、Markdown形式で表示可能なバッジの文字列（例: Shields.ioのリンク）を生成します。
- **`src/generate_repo_list/config_manager.py`**:
    - **役割**: YAMLやTOML形式の設定ファイルを読み込み、アプリケーション全体で利用可能な設定オブジェクトとして提供します。
    - **機能**: 指定されたパスから設定ファイルをパースし、設定値へのアクセスを抽象化するメソッド（例: `get_config`, `load_secrets`）を提供します。
- **`src/generate_repo_list/date_formatter.py`**:
    - **役割**: 日付および時刻データを様々な形式の文字列に変換します。
    - **機能**: `datetime` オブジェクトを受け取り、人間が読みやすい形式やISO 8601形式など、指定されたフォーマットの日付文字列を生成します。
- **`src/generate_repo_list/generate_repo_list.py`**:
    - **役割**: GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成するシステムの中心的な実行ロジックです。
    - **機能**: コマンドライン引数を解析し、GitHub API認証、リポジトリデータの取得、各処理モジュールへの委譲（データ加工、概要取得、Markdown生成）、そして結果ファイルの出力までの一連のフローを管理します。
- **`src/generate_repo_list/language_info.py`**:
    - **役割**: GitHubリポジトリの利用言語に関する情報を抽出し、統計的に処理します。
    - **機能**: リポジトリの言語ごとのバイト数データから、主要な言語とその割合を計算し、表示に適した形式（例: トップ3言語のリスト）を生成します。
- **`src/generate_repo_list/markdown_generator.py`**:
    - **役割**: 処理されたリポジトリデータとテンプレートを組み合わせて、Jekyll互換のMarkdownコンテンツを生成します。
    - **機能**: 各リポジトリの情報をテンプレートに埋め込み、見出し、リスト、リンクなどを含む最終的なMarkdown文字列全体を構築します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - **役割**: 他のGitHubリポジトリ内の特定のファイルから、プロジェクトの概要説明を自動で取得・抽出します。
    - **機能**: GitHub APIを介してリモートリポジトリのファイル内容をフェッチし、そのMarkdownコンテンツを解析して、指定されたセクション（例: `## プロジェクト概要`）から3行の説明文を抽出します。
- **`src/generate_repo_list/repository_processor.py`**:
    - **役割**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に変換・整形します。
    - **機能**: リポジトリのフィルタリング（フォーク、アーカイブなど）、必要なフィールドの抽出、URLの生成、`project_overview_fetcher` から取得した概要やバッジ情報の統合などを行います。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - **役割**: リポジトリのスター数やフォーク数などの統計情報を計算し、表示に適した形式で提供します。
    - **機能**: リポジトリの数値データを受け取り、それを集計したり、特定の基準でソートしたりする機能を提供します。
- **`src/generate_repo_list/template_processor.py`**:
    - **役割**: テンプレートファイル（Markdownスニペット、JSON-LDテンプレートなど）を読み込み、プレースホルダーを実際のデータで置き換えます。
    - **機能**: テンプレート文字列とデータ辞書を受け取り、テンプレート内の変数（例: `{{ repo_name }}`）を対応するデータで置換した最終文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**:
    - **役割**: GitHubリポジトリ関連の様々なURL（リポジトリURL、APIエンドポイントなど）を生成・解析します。
    - **機能**: ユーザー名やリポジトリ名からGitHubのWebページURLやAPIエンドポイントURLを構築したり、ファイルパスを解決したりします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。
(コードベースがないため、関数の具体的な呼び出し関係を特定できませんでした。)

---
Generated at: 2026-01-11 07:06:16 JST
