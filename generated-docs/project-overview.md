Last updated: 2025-12-19

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（cat2151.github.io）向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、SEOに最適化されたMarkdownファイルを生成することで、検索エンジンやLLMからの参照性を向上させます。
- 各リポジトリの概要を自動取得・表示し、バッジ、分類、Jekyll対応で豊富な情報を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、生成されたMarkdownファイルを静的サイトとしてレンダリングします), Markdown (GitHub APIから取得した情報に基づき、コンテンツを生成するフォーマットです)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (システムの主要な開発言語です), pytest (Pythonコードの単体テストおよび統合テストに使用されるテスティングフレームワークです), ruff (Pythonコードの静的解析とフォーマットを行うLinterおよびFormatterです), GitHub API (リポジトリ情報を取得するための主要なインターフェースです)
- テスト: pytest (システムの堅牢性を確保するためのテスト実行フレームワークです)
- ビルドツール: Pythonスクリプト (リポジトリ情報の取得、解析、Markdownファイルの生成といった一連の処理を自動化するスクリプトがビルドの役割を担います)
- 言語機能: Python (オブジェクト指向プログラミング、ファイルI/O、HTTPリクエスト処理、データ構造操作など、多岐にわたる言語機能が利用されています)
- 自動化・CI/CD: (ローカル開発重視のためCI/CDの仕組みは明示されていませんが、) Pythonスクリプトの実行によりリポジトリ情報の取得とMarkdown生成が自動化されます。`requirements.txt` と `requirements-dev.txt` で依存関係の管理を自動化しています。
- 開発標準: ruff (コードの品質と一貫性を保つためのコーディング規約チェックと自動修正ツールです)

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外すべきファイルやディレクトリ（例: ビルド生成物、ログファイル、設定ファイルなど）を指定するファイルです。
- **LICENSE**: 本プロジェクトがMITライセンスの下で公開されていることを明示するファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、ライセンス情報などを記述した主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイト全体の構成設定を行うファイルで、サイトのタイトル、テーマ、プラグイン、パーマリンク構造などを定義します。
- **assets/**: サイトで使用される画像などの静的アセットを格納するディレクトリです。
  - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
- **debug_project_overview.py**: `project_overview_fetcher.py`の機能をデバッグするために使用される補助スクリプトです。
- **generated-docs/**: プロジェクトの自動概要取得機能で参照される、各リポジトリの概要説明ファイル（例: `project-overview.md`）が格納されることを想定したディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイトの所有権確認に使用されるHTMLファイルです。特に実行可能な関数やインポートはありません。
- **index.md**: 生成されたリポジトリ一覧が実際に書き込まれるGitHub PagesサイトのトップページとなるMarkdownファイルです。JekyllによってHTMLに変換されます。
- **issue-notes/**: 開発中の課題やメモなどをMarkdown形式で管理するためのディレクトリです。
- **manifest.json**: PWA (Progressive Web App) のマニフェストファイルで、ウェブサイトをデバイスのホーム画面に追加する際の表示情報（アプリ名、アイコン、表示モードなど）を定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定（テストの検出方法、追加オプションなど）を記述するファイルです。
- **requirements-dev.txt**: 開発時やテスト実行時に必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **requirements.txt**: プロジェクトの本番稼働環境で必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
- **ruff.toml**: PythonのLinterおよびFormatterであるruffの動作設定（ルール、無視するファイル、自動修正設定など）を記述するファイルです。
- **src/**: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
  - **__init__.py**: Pythonパッケージであることを示すファイルです。
  - **generate_repo_list/**: リポジトリ一覧の生成ロジックが実装されているサブパッケージです。
    - **__init__.py**: Pythonパッケージであることを示すファイルです。
    - **badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ画像を生成するロジックを含みます。
    - **config.yml**: プロジェクト概要取得機能など、システムの技術的パラメータを設定するファイルです。
    - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
    - **generate_repo_list.py**: プロジェクトのメインエントリスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイル（`index.md`など）を生成します。
    - **json_ld_template.json**: SEO最適化のために、ウェブページに構造化データを埋め込むためのJSON-LD形式のテンプレートファイルです。
    - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理・解析するためのロジックを含みます。
    - **markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyllで解釈可能なMarkdownコンテンツを生成するためのロジックを実装しています。
    - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し取得する機能を提供します。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形に整形・分類するロジックを含みます。
    - **seo_template.yml**: 検索エンジン最適化(SEO)に関連するメタデータや記述のテンプレート設定を定義するファイルです。
    - **statistics_calculator.py**: リポジトリに関する様々な統計情報（スター数、フォーク数、コミット数など）を計算するロジックを含みます。
    - **strings.yml**: UIに表示されるメッセージ、ラベル、その他のテキスト文言を一元的に管理するための設定ファイルです。
    - **template_processor.py**: Markdown生成時に使用するテンプレートの読み込み、変数置換、レンダリングなどを行うロジックを含みます。
    - **url_utils.py**: URLの検証、構築、解析など、URLに関連するユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の単体テストを行うスクリプトです。
- **tests/**: pytestによるテストスクリプトを格納するディレクトリです。
  - **test_config.py**: 設定ファイルの読み込みや管理に関するテストを含みます。
  - **test_environment.py**: 実行環境のセットアップや依存関係に関するテストを含みます。
  - **test_integration.py**: システムの複数のコンポーネントが連携して正しく動作するかを確認する統合テストを含みます。
  - **test_markdown_generator.py**: `markdown_generator.py`が正しいMarkdownコンテンツを生成するかを確認するテストを含みます。
  - **test_project_overview_fetcher.py**: `project_overview_fetcher.py`のプロジェクト概要抽出機能に関するテストを含みます。
  - **test_repository_processor.py**: `repository_processor.py`のリポジトリデータ処理ロジックに関するテストを含みます。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値、機能を詳細に特定することはできません。しかし、各Pythonファイルの役割に基づき、以下のような種類の関数が含まれると想定されます。

- **debug_project_overview.py**: プロジェクト概要取得機能のテスト実行、結果表示、エラーハンドリングなどのデバッグ用関数。
- **src/generate_repo_list/badge_generator.py**: リポジトリの言語、ステータス、ライセンスなどの情報から適切なバッジSVGを生成する関数。
- **src/generate_repo_list/config_manager.py**: YAMLファイル（`config.yml`, `strings.yml`）を読み込み、設定値を取得・設定する関数。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIを呼び出してリポジトリを取得し、各処理モジュールを連携させて最終的なMarkdownを生成するメイン実行関数。
- **src/generate_repo_list/language_info.py**: リポジトリの言語統計を解析し、主要言語や関連情報を抽出・整形する関数。
- **src/generate_repo_list/markdown_generator.py**: 複数のテンプレートとリポジトリデータを受け取り、リポジトリ一覧の各項目や全体構造のMarkdown文字列を生成する関数。
- **src/generate_repo_list/project_overview_fetcher.py**: 指定されたリポジトリの特定のファイルから「プロジェクト概要」セクションをパースし、3行の概要説明を抽出する関数。GitHub APIを通じてファイル内容を取得する機能も持つ。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータをフィルタリング（アーカイブ、フォークなど）、ソート、カテゴリ分け、および表示用に整形する関数。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計する関数。
- **src/generate_repo_list/template_processor.py**: プレースホルダーを含むテンプレート文字列を、実際のデータで置き換えるための関数。
- **src/generate_repo_list/url_utils.py**: URLの有効性を検証したり、特定のパスやクエリパラメータを付与してURLを構築したりするユーティリティ関数。
- **test_project_overview.py**: `project_overview_fetcher`のモックを用いたテストケース定義、結果アサートを行うテスト関数。
- **tests/** ディレクトリ内の各ファイル: それぞれの対象モジュール（`config_manager`, `markdown_generator`など）の機能を検証するためのテストセットアップ、テスト実行、結果検証を行うテスト関数群。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-19 07:06:56 JST
