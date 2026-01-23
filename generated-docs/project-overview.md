Last updated: 2026-01-24

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（`<username>.github.io`）用に、自身のGitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、リポジトリ情報を取得してSEOに最適化されたMarkdownファイルを自動作成します。
- これにより、検索エンジンからの発見性を高め、リポジトリ情報をより多くの人やAIに届けます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesで動作する静的サイトジェネレーター。本プロジェクトはJekyllが消費するMarkdownファイルを生成します), Markdown (GitHub Pagesのコンテンツ形式として利用される軽量マークアップ言語です)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成に使用されます), GitHub API (リポジトリ情報の取得に使用されるGitHubの公開APIです)
- テスト: pytest (Pythonコードの単体テストおよび統合テストを記述・実行するためのフレームワークです)
- ビルドツール: なし (特定のビルドツールは使用せず、Pythonスクリプトが直接Markdownファイルを生成します)
- 言語機能: Python (汎用的なプログラミング言語であり、本プロジェクトのロジック実装に利用されています)
- 自動化・CI/CD: なし (継続的インテグレーション/デプロイの特定のツールは利用されていませんが、本システム自体が情報自動生成の自動化機能を提供します)
- 開発標準: ruff (Pythonコードのスタイルチェックと自動修正を行う高速なリンター・フォーマッターです)
- その他: YAML (設定ファイルの定義に利用されます), TOML (シークレット情報の設定ファイルに利用されます)

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **LICENSE**: プロジェクトの利用条件を定めるMITライセンス情報が記述されています。
- **README.md**: プロジェクトの概要、目的、機能、使い方、設定方法などを説明する主要なドキュメントです。
- **_config.yml**: Jekyll静的サイトジェネレーターの設定ファイルであり、サイト全体の挙動を定義します。
- **assets/**: Webサイトで使用される画像（ファビコンなど）やその他の静的ファイルを格納するディレクトリです。
    - `favicon-*.png`: サイトのタブやブックマークに表示されるアイコンファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグ用途で使用されるスクリプトです。
- **generated-docs/**: プロジェクト概要取得機能で参照される、各リポジトリの概要ファイル（`project-overview.md`など）が配置される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイト所有権確認のために配置されるHTMLファイルです。
- **index.md**: プロジェクトによって自動生成される、リポジトリ一覧のコンテンツが記述されるメインのMarkdownファイルです。
- **issue-notes/**: 開発中に発生した課題やその検討に関するメモを格納するディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、アプリの表示方法や動作を定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの実行設定を記述するファイルです。
- **requirements-dev.txt**: 開発時やテスト実行時に必要なPythonパッケージとその依存関係を定義するファイルです。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージとその依存関係を定義するファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールしてよいか、あるいは避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのスタイルチェックと自動修正を行うツール「ruff」の設定ファイルです。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - `__init__.py`: Pythonパッケージであることを示すファイルです。
    - `generate_repo_list/`: リポジトリ一覧生成ロジックを格納するパッケージです。
        - `__init__.py`: このディレクトリがPythonパッケージであることを示します。
        - `badge_generator.py`: リポジトリの各種情報（言語、ステータスなど）に対応するバッジのMarkdownを生成するロジックが含まれます。
        - `config.yml`: プロジェクト概要取得機能などの技術的パラメータを設定するためのYAML形式の設定ファイルです。
        - `config_manager.py`: YAML形式の設定ファイルを読み込み、管理するためのモジュールです。
        - `date_formatter.py`: 日付や時刻の表示形式を整形するための関数群が含まれます。
        - `generate_repo_list.py`: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する主要な処理を実行します。
        - `json_ld_template.json`: 検索エンジン最適化のためのJSON-LD形式のテンプレートファイルです。
        - `language_info.py`: リポジトリの言語に関する情報を処理・整形するロジックが含まれます。
        - `markdown_generator.py`: 取得・整形されたリポジトリ情報から、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックが含まれます。
        - `project_overview_fetcher.py`: 各リポジトリから指定された `project-overview.md` ファイルを読み込み、プロジェクトの3行概要を抽出する機能を提供します。
        - `readme_badge_extractor.py`: READMEファイルから特定のバッジ情報を抽出するロジックが含まれます。
        - `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報（言語、スター数、最終更新日など）を抽出し、整形する主要ロジックが含まれます。
        - `seo_template.yml`: SEO関連のメタデータや設定を定義するYAML形式のテンプレートファイルです。
        - `statistics_calculator.py`: リポジトリに関する統計情報（例: スター総数、フォーク総数など）を計算するロジックが含まれます。
        - `strings.yml`: アプリケーション内で使用される表示メッセージや文言を管理するためのYAML形式の設定ファイルです。
        - `template_processor.py`: Markdown生成時に利用されるテンプレートの処理ロジックが含まれます。
        - `url_utils.py`: URLに関連するユーティリティ関数（生成、解析など）が含まれます。
- **test_project_overview.py**: プロジェクト概要取得機能のテストコードです。
- **tests/**: pytestによって実行されるテストスクリプト群が格納されているディレクトリです。
    - `test_*.py`: 各モジュールや機能に対応するテストケースが記述されています。

## 関数詳細説明
本プロジェクトはPythonスクリプトで構成されており、多くの処理はモジュール内の関数として実装されています。
具体的な引数や戻り値の詳細はコードを参照する必要がありますが、ファイル名から推測される主要な関数とその役割は以下の通りです。

- **`generate_repo_list.py` 内の主要関数**:
    - **役割**: GitHub APIから指定されたユーザーのリポジトリ情報を取得し、その情報に基づいてJekyll/GitHub Pages向けのMarkdownファイルを生成するメインの処理を実行します。
    - **機能**: API認証、リポジトリデータの取得、データ整形、Markdownへの変換、ファイル出力などを統括します。

- **`badge_generator.py` 内の主要関数**:
    - **役割**: リポジトリの言語、アーカイブ状態、フォーク状態などの属性に基づき、対応するバッジのMarkdown文字列を生成します。
    - **機能**: 特定の条件に応じてSVGバッジやテキストバッジの形式を決定し、Markdownリンクと結合して出力します。

- **`config_manager.py` 内の主要関数**:
    - **役割**: `config.yml` や `strings.yml` などのYAML形式の設定ファイルを読み込み、設定値を提供します。
    - **機能**: 設定ファイルのパス解決、内容のパース、デフォルト値の提供などを行い、他のモジュールが設定にアクセスできるようにします。

- **`date_formatter.py` 内の主要関数**:
    - **役割**: GitHub APIから取得される日付文字列を、人間が読みやすい形式や特定のロケールに合わせた形式に整形します。
    - **機能**: 日付フォーマットの変換、タイムゾーン処理など。

- **`markdown_generator.py` 内の主要関数**:
    - **役割**: 処理されたリポジトリ情報とテンプレート（`seo_template.yml`など）を使用して、最終的なリポジトリ一覧のMarkdownコンテンツを構築します。
    - **機能**: 各リポジトリのエントリ作成、全体構造の組み立て、SEOメタデータの埋め込みなど。

- **`project_overview_fetcher.py` 内の主要関数**:
    - **役割**: 各リポジトリ内にある特定のパス（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に取得・抽出します。
    - **機能**: ファイルのダウンロード、指定セクションのパース、概要行の抽出、キャッシュ処理など。

- **`repository_processor.py` 内の主要関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を受け取り、表示に必要な情報（リポジトリ名、説明、言語、スター数、最終更新日、URLなど）を抽出し、整形します。
    - **機能**: 不要な情報のフィルタリング、データ型変換、表示用プロパティの追加など。

- **`statistics_calculator.py` 内の主要関数**:
    - **役割**: 処理対象のリポジトリ群全体の統計情報（例: 総スター数、総フォーク数、最も多い言語など）を計算します。
    - **機能**: リポジトリデータの集計、特定のメトリクスの計算。

- **`template_processor.py` 内の主要関数**:
    - **役割**: Markdown生成時に使用されるテンプレートを処理し、動的なデータをテンプレートのプレースホルダーに差し込みます。
    - **機能**: テンプレートエンジンのラッパー、変数置換処理。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-01-24 07:05:56 JST
