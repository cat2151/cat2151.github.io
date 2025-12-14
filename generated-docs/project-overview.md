Last updated: 2025-12-15

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIとMarkdownを活用し、SEO最適化されたページを効率的に作成します。
- 各リポジトリの概要を自動取得し、情報アクセスとLLM参照の改善を目指します。

## 技術スタック
- フロントエンド: **Jekyll** - GitHub Pagesの静的サイトジェネレータとして機能し、生成されたMarkdownファイルをHTMLページとして公開します。
- 音楽・オーディオ: (該当なし)
- 開発ツール:
    - **Python**: プロジェクトの主要なプログラミング言語であり、GitHub APIからのデータ取得とMarkdown生成の中核を担います。
    - **GitHub API**: リポジトリ情報（名前、説明、言語など）をプログラム的に取得するために使用されます。
    - **Markdown**: 生成されるリポジトリ一覧ページのフォーマットとして使用され、JekyllによってHTMLに変換されます。
    - **Git/GitHub**: ソースコードのバージョン管理とプロジェクトのホスティングに利用されます。
- テスト: **pytest** - Pythonコードのユニットテストおよび統合テストを実行するためのフレームワークです。
- ビルドツール: (Pythonスクリプトによる生成が主であり、別途ビルドツールは明示されていません。Jekyllの処理はGitHub Pagesに依存します。)
- 言語機能: **Pythonの標準ライブラリおよび構文** - ファイル操作、APIリクエスト、データ処理など、Pythonの基本的な機能が利用されています。
- 自動化・CI/CD: (「CI/CD不要のローカル開発重視の構成」とされており、現時点では特定の自動化・CI/CDツールは使用していません。)
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックと自動修正を行うためのツールです。
    - **.editorconfig**: 複数のエディタやIDE間でコードの書式設定を統一するための設定ファイルです。

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
- **.editorconfig**: プロジェクト全体でコードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定します。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、クイックスタートガイド、設定方法、ライセンスなどの基本情報を提供します。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
- **assets/**: Webサイトで使用される画像などの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: 各種サイズのファビコン画像ファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能のテストやデバッグを目的とした補助スクリプトです。
- **generated-docs/**: リポジトリごとの `project-overview.md` など、生成されるドキュメントやデータが格納されることを想定したディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイトの所有権確認に使用されるHTMLファイルです。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される主要なMarkdownファイルであり、GitHub Pagesサイトのリポジトリ一覧ページとして機能します。
- **issue-notes/**: 開発中に発生した課題や検討事項に関するメモをMarkdown形式で格納するディレクトリです。
    - **[番号].md**: 個別の課題やメモの内容を記述したファイルです。
- **manifest.json**: Webアプリマニフェストファイルで、Webサイトをプログレッシブウェブアプリ（PWA）として利用する際のメタデータを提供します。
- **pytest.ini**: pytestフレームワークの動作設定を定義するファイルです。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonコードリンター・フォーマッターであるruffの設定ファイルです。
- **src/**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
    - **src/__init__.py**: `src` ディレクトリをPythonパッケージとして識別するためのファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧生成ロジックのコア部分を含むPythonパッケージです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして識別するためのファイルです。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの状態（例: アクティブ、アーカイブ、フォーク）に応じたバッジのMarkdownを生成するロジックを実装しています。
        - **src/generate_repo_list/config.yml**: プロジェクト概要取得機能などの技術的なパラメータや設定値をYAML形式で定義するファイルです。
        - **src/generate_repo_list/config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        - **src/generate_repo_list/generate_repo_list.py**: このプロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する一連の処理を制御します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化のために使用されるJSON-LD形式の構造化データテンプレートです。
        - **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形式に変換するロジックを提供します。
        - **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリデータから、最終的なMarkdownコンテンツ（特にリポジトリ一覧の各項目）を生成する役割を担います。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクトの3行概要を自動的に取得するロジックを実装しています。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報の抽出、整形、フィルタリング、追加データ（例: 概要）の取得連携などを行うモジュールです。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化（SEO）に関連する設定やテンプレートを定義するYAMLファイルです。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリに関する統計情報（例: スター数、フォーク数など）を計算するロジックを提供します。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキストを多言語対応や一元管理のために定義するYAMLファイルです。
        - **src/generate_repo_list/template_processor.py**: Markdown生成におけるテンプレートの適用や処理を担当する汎用モジュールです。
        - **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を集めたモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（特にプロジェクト概要の取得）を検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のユニットテストや統合テストを格納するディレクトリです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを記述しています。
    - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを記述しています。
    - **test_integration.py**: 各モジュール間の連携を含む、より広範な統合テストを記述しています。
    - **test_markdown_generator.py**: Markdown生成ロジックの正確性を検証するテストです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールの機能に関する詳細なテストです。
    - **test_repository_processor.py**: リポジトリ情報の処理ロジックの正確性を検証するテストです。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャ（引数、戻り値）を特定できませんでしたが、ファイル名とプロジェクトの機能から主要な関数の役割と機能を推測します。

- **`src/generate_repo_list/generate_repo_list.py` 内の主要関数 (`main` 関数相当)**
    - **役割**: GitHubユーザーのリポジトリ情報を取得し、指定されたオプションに基づいて整形し、Markdownファイルとして出力するメイン処理を実行します。
    - **機能**: GitHub APIからのリポジトリデータ取得、各リポジトリに対する `project_overview_fetcher` や `repository_processor` の呼び出し、`markdown_generator` を用いたコンテンツの構築、および結果のファイル書き込みを調整します。
    - **引数**: `--username` (GitHubユーザー名), `--output` (出力ファイル名), `--limit` (処理するリポジトリ数の上限) などのコマンドライン引数。
    - **戻り値**: なし (副作用としてファイル生成を行います)。

- **`src/generate_repo_list/badge_generator.py` 内の関数 (`generate_badges` 相当)**
    - **役割**: リポジトリの特定の属性（例: アクティブ、アーカイブ、フォーク）に基づいて、対応するMarkdown形式のバッジ文字列を生成します。
    - **機能**: 入力されたリポジトリ情報から状態を判別し、適切なバッジのアイコンとテキストを含むMarkdownスニペットを返します。
    - **引数**: リポジトリの状態を示すブール値や文字列など。
    - **戻り値**: 生成されたバッジのMarkdown文字列。

- **`src/generate_repo_list/project_overview_fetcher.py` 内の関数 (`fetch_project_overview` 相当)**
    - **役割**: 特定のGitHubリポジトリから、設定されたパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要を非同期に取得します。
    - **機能**: GitHub APIを介してターゲットファイルの内容を読み込み、指定されたセクションタイトル (`プロジェクト概要`) の下の3行を解析・抽出します。キャッシュ機能も備えています。
    - **引数**: リポジトリオーナー名、リポジトリ名、ターゲットファイルのパス、セクションタイトル、リトライ設定、タイムアウト設定、キャッシュ有効化フラグ。
    - **戻り値**: 抽出された3行のプロジェクト概要のリスト (文字列のリスト)、または取得に失敗した場合は空のリストやNone。

- **`src/generate_repo_list/markdown_generator.py` 内の関数 (`generate_repo_markdown` 相当)**
    - **役割**: 処理済みの単一リポジトリ情報を受け取り、そのリポジトリを表示するためのMarkdownコンテンツスニペットを生成します。
    - **機能**: リポジトリ名、説明、言語、バッジ、取得されたプロジェクト概要などをテンプレートに沿って整形し、個々のリポジトリ表示ブロックを構成するMarkdown文字列を返します。
    - **引数**: 整形済みリポジトリ情報を表すオブジェクトまたは辞書。
    - **戻り値**: 単一リポジトリの表示に対応するMarkdown文字列。

- **`src/generate_repo_list/repository_processor.py` 内の関数 (`process_repository_data` 相当)**
    - **役割**: GitHub APIから取得した生のリポジトリデータを受け取り、アプリケーションの他のモジュール（例: `markdown_generator`）が利用しやすい形式に整形・加工します。
    - **機能**: 生データからの必要なフィールドの抽出、データのクリーンアップ、追加情報（例: プロジェクト概要のフェッチ結果）の統合、およびフィルタリングを行います。
    - **引数**: GitHub APIから返された生のリポジトリデータ（辞書またはJSONオブジェクト）。
    - **戻り値**: 整形され、追加情報が付与されたリポジトリ情報オブジェクトまたは辞書。

## 関数呼び出し階層ツリー
```
関数呼び出し階層はプロジェクト情報から分析できませんでした。

---
Generated at: 2025-12-15 07:05:51 JST
