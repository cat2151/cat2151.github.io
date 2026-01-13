Last updated: 2026-01-14

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのGitHubリポジトリ情報を自動で取得・整理します。
- 取得した情報から、SEOに最適化されたGitHub Pages向けリポジトリ一覧を自動生成します。
- これにより、個々のプロジェクトの発見性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesのサイトを構築・表示するための静的サイトジェネレーターとして、生成されるMarkdownの基盤となります)
- 音楽・オーディオ: (該当なし)
- 開発ツール: Python (プロジェクトの主要な開発言語として、リポジトリ情報の取得、処理、Markdown生成スクリプトを実行します)
- テスト: Pytest (Pythonコードの単体テストおよび結合テストを行うためのフレームワークです)
- ビルドツール: PythonスクリプトによるMarkdown生成 (カスタムスクリプトがGitHub APIからデータを取得し、Markdownファイルとして出力する独自のビルドプロセスを構成します)
- 言語機能: Python (GitHub API通信、ファイルI/O、データ構造操作、YAML/TOMLファイル解析など、多くの標準および外部ライブラリ機能を利用します)
- 自動化・CI/CD: (該当なし。このプロジェクト自体はCI/CDを明示的に使用せず、ローカルでの開発・実行に重点を置いています)
- 開発標準: Ruff (Pythonコードのフォーマットとリンティングを自動的に行い、コードスタイルの一貫性を保つツールです)、EditorConfig (異なるエディタやIDE間で一貫したコーディングスタイルを定義・適用するためのファイル形式です)

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
  📖 18.md
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
    📄 readme_badge_extractor.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_badge_generator_integration.py
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
- **.editorconfig**: 異なる開発環境間で、インデントスタイル、文字コード、改行コードなどの基本的なコードスタイルを統一するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するための設定ファイルです。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **README.md**: プロジェクトの概要、目的、機能、使い方、設定方法などを記述した、プロジェクトの玄関となるドキュメントです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン設定などが含まれます。
- **assets/**: Webサイトで使用される画像、アイコン、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるウェブサイトのファビコン（サイトアイコン）ファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグやテストのために一時的に使用される可能性のあるスクリプトです。
- **generated-docs/**: GitHubリポジトリの `generated-docs/project-overview.md` など、自動生成されたドキュメントや関連ファイルを格納するディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどの所有権確認のために配置されることが多い、HTML形式の検証ファイルです。
- **index.md**: 生成されたリポジトリ一覧が書き込まれるメインのMarkdownファイルで、GitHub Pagesのトップページとして表示されます。
- **issue-notes/**: GitHubのissueに関連するメモやドラフトなどをMarkdown形式で保存するディレクトリです。
- **manifest.json**: PWA (Progressive Web App) の設定ファイルで、アプリケーション名、アイコン、表示モードなどを定義します。
- **pytest.ini**: Pytestテストフレームワークの設定ファイルです。テストの検出方法、追加オプション、マーカーなどを指定します。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記述したファイルです。`requirements.txt` の依存関係に加え、開発者向けのツールを含みます。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **generate_repo_list/**: リポジトリ一覧生成システムのコアロジックを格納するPythonパッケージです。
        - `__init__.py`: Pythonパッケージであることを示すファイルです。
        - `badge_generator.py`: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）に応じたバッジを生成するロジックを扱います。
        - `config.yml`: プロジェクトの技術的パラメータや動作設定を定義するYAML形式の設定ファイルです。
        - `config_manager.py`: `config.yml` や `strings.yml` などの設定ファイルを読み込み、設定値へのアクセスを管理するモジュールです。
        - `date_formatter.py`: 日付や時刻の情報を特定のフォーマットに変換するユーティリティ関数を提供します。
        - `generate_repo_list.py`: プロジェクトのエントリーポイントとなるメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownを生成する一連の処理を調整します。
        - `json_ld_template.json`: SEO強化のために使用されるJSON-LD形式の構造化データテンプレートです。
        - `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形する機能を提供します。
        - `markdown_generator.py`: 処理済みのリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するロジックを実装しています。
        - `project_overview_fetcher.py`: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクトの概要テキストを抽出するモジュールです。
        - `readme_badge_extractor.py`: READMEファイル内に含まれるバッジ（例: ビルドステータスバッジ）の情報を抽出する機能を提供します。
        - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、Markdown生成に適した形式に整形する役割を担います。
        - `seo_template.yml`: 検索エンジン最適化（SEO）のためのメタデータや構造化データのテンプレートを定義するYAMLファイルです。
        - `statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - `strings.yml`: UIに表示されるテキストメッセージ、文言、ラベルなどを一元的に管理するYAMLファイルです。多言語対応や文言変更を容易にします。
        - `template_processor.py`: Markdownテンプレート内の特定のプレースホルダーを実際のリポジトリデータや設定値で置き換える処理を行います。
        - `url_utils.py`: URLの生成、解析、エンコード/デコードなど、URL関連のユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py` の機能に関する単体テストを記述したファイルです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - `test_badge_generator_integration.py`: バッジ生成機能の統合テストを記述したファイルです。
    - `test_config.py`: 設定ファイルの読み込みや管理に関するテストを記述したファイルです。
    - `test_date_formatter.py`: 日付フォーマット機能のテストを記述したファイルです。
    - `test_environment.py`: テスト実行環境の設定や依存関係に関するテストを記述したファイルです。
    - `test_integration.py`: システム全体の主要な統合テストを記述したファイルで、複数のモジュールが連携して正しく動作するかを検証します。
    - `test_markdown_generator.py`: Markdown生成機能のテストを記述したファイルです。
    - `test_project_overview_fetcher.py`: プロジェクト概要取得機能のテストを記述したファイルです。
    - `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - `test_repository_processor.py`: リポジトリ情報の処理と整形機能のテストを記述したファイルです。

## 関数詳細説明
- **generate_repo_list.py**:
    - **`main()` / `generate_repo_list()`**: このスクリプトの主要な実行関数。GitHub APIからユーザーのリポジトリ情報を取得し、`repository_processor` でデータを整形、`markdown_generator` や `project_overview_fetcher` などと連携しながら、最終的に指定された出力ファイル（例: `index.md`）にMarkdown形式のリポジトリ一覧を書き出します。引数としてGitHubユーザー名、出力ファイルパス、処理リポジトリ数の上限などを受け取ります。
- **badge_generator.py**:
    - **`generate_badge(status: str) -> str`**: リポジトリの公開ステータス（例: "active", "archived", "fork"）に基づいて、対応するバッジのMarkdownまたはHTMLスニペットを生成します。引数としてステータス文字列を取り、バッジの表現文字列を返します。
- **config_manager.py**:
    - **`load_config(config_path: str) -> dict`**: 指定されたパスのYAML設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書形式で返します。
    - **`load_strings(strings_path: str) -> dict`**: 指定されたパスのYAML文字列ファイル（例: `strings.yml`）を読み込み、多言語対応やメッセージ表示用の文字列辞書を返します。
- **date_formatter.py**:
    - **`format_date(datetime_obj: datetime, format_str: str = "%Y-%m-%d") -> str`**: `datetime`オブジェクトを指定された文字列フォーマット（デフォルトはYYYY-MM-DD）に変換して返します。
- **markdown_generator.py**:
    - **`generate_markdown(repo_data: list[dict], template: str) -> str`**: 処理されたリポジトリデータのリストとMarkdownテンプレートを受け取り、それらを組み合わせて最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
- **project_overview_fetcher.py**:
    - **`fetch_project_overview(repo_url: str, file_path: str) -> str`**: 指定されたリポジトリのURLとファイルパスから、`generated-docs/project-overview.md` などの特定ファイルを読み込み、そこからプロジェクト概要の3行説明を抽出して返します。GitHub APIまたは直接HTTPリクエストを使用する可能性があります。
- **repository_processor.py**:
    - **`process_repository_data(raw_repo_list: list[dict]) -> list[dict]`**: GitHub APIから取得した生の（未加工の）リポジトリデータリストを受け取り、必要な情報（名前、説明、URL、スター数、言語など）を抽出し、Markdown生成に適した形式に整形されたリポジトリデータのリストを返します。
- **template_processor.py**:
    - **`apply_template(content: str, data: dict) -> str`**: テンプレート文字列内のプレースホルダー（例: `{{ placeholder }}`）を、提供されたデータ辞書の値に置き換える処理を実行します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-14 07:06:38 JST
