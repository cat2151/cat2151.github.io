Last updated: 2026-03-07

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、自身の全リポジトリ一覧を自動生成するシステムです。
- SEO対策を強化し、検索エンジンからのアクセスやLLMによる情報参照性を向上させます。
- 各リポジトリの概要、技術スタック、バッジなどを自動で取得・表示し、訪問者に魅力的な情報を提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesの基盤であり、Markdownファイルを静的サイトとしてレンダリングします)、Markdown (リポジトリ一覧の出力形式であり、JekyllでHTMLに変換されます)
- 音楽・オーディオ: N/A (該当する技術は使用されていません)
- 開発ツール: Python (主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成に使用されます)、GitHub API (GitHubからリポジトリ情報を取得するために利用されます)、Git (ソースコードのバージョン管理システム)
- テスト: pytest (Pythonコードの単体テストおよび結合テストを行うためのフレームワーク)
- ビルドツール: Pythonスクリプト (GitHub APIから取得した情報に基づき、Markdown形式のリポジトリ一覧ファイルを生成するカスタムビルドロジックを提供します)
- 言語機能: Python言語機能 (Pythonの標準的なオブジェクト指向プログラミング、データ構造、ファイルI/Oなどが利用されています)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリに自動化スクリプトが配置されており、コード品質チェックやファイルサイズの監視などに活用されます)
- 開発標準: Ruff (Pythonコードの高速リンターおよびフォーマッター。コードの一貫性と品質を保ちます)、EditorConfig (異なるエディタやIDE間でコーディングスタイルを統一するための設定ファイル)

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **.github_automation/**: GitHub Actionsなどを用いた自動化スクリプトや設定を格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルを検出するための自動化機能に関連するファイル群です。
        - **README.md**: `check_large_files`機能の概要や使用方法を説明するドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェック機能に関する設定（例: 許容するファイルサイズの上限）を定義するファイルです。
        - **scripts/check_large_files.py**: リポジトリ内の大容量ファイルを特定し、レポートするためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリ（例: ビルド生成物、一時ファイル、個人設定ファイル）を指定する設定ファイルです。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記載したファイルです。これにより、他のユーザーがどのようにコードを利用できるかが明確になります。
- **README.md**: プロジェクト全体の概要、セットアップ方法、使い方、主な機能、開発者向けのヒントなどを記述したメインのドキュメントです。
- **_config.yml**: Jekyll (GitHub Pagesの基盤) サイト全体の構成設定を定義するファイルです。テーマ、パーマリンク構造、プラグインなどの設定が含まれます。
- **assets/**: Webサイトで使用される画像、アイコン、スタイルシート、JavaScriptファイルなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: ウェブサイトのブラウザタブやブックマークに表示されるアイコン（ファビコン）の各種サイズです。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールのデバッグやテスト実行を補助するためのスクリプトです。
- **generated-docs/**: 他のリポジトリから自動的に取得・生成されたプロジェクト概要などのドキュメントが一時的に、または最終的に配置される可能性のあるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleなどのサービスでサイトの所有権を確認するために使用されるHTMLファイルです。特定のコンテンツを含み、サービスによって検証されます。
- **index.md**: `src/generate_repo_list/generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧を表示するメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
- **issue-notes/**: 開発中に発生した課題や検討事項、特定のトピックに関するメモなどを記録するためのディレクトリです。
    - **22.md**: 特定の課題や検討事項（例えば、Issue番号22に関連するメモ）を詳細に記述したMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に必要となるマニフェストファイルです。ウェブアプリをホーム画面に追加したり、オフラインで利用したりするための情報（アプリ名、アイコン、表示モードなど）を定義します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定ファイルです。テストの検出方法、プラグイン、マーカーなどの設定を定義します。
- **requirements-dev.txt**: プロジェクトの開発環境およびテスト実行に必要なPythonパッケージとそのバージョンをリストアップしたファイルです。本番環境とは異なる依存関係を含みます。
- **requirements.txt**: プロジェクトを本番環境で実行するために最低限必要なPythonパッケージとそのバージョンをリストアップしたファイルです。

- **robots.txt**: 検索エンジンのウェブクローラー（ロボット）に対して、サイトのどの部分をクロールしてもよいか、またはクロールしてはならないかを指示するテキストファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。コードスタイルのルール、無視するファイル、エラーコードなどを定義し、コード品質を自動で維持します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示す空のファイルです。
    - **generate_repo_list/**: GitHubリポジトリ一覧の自動生成機能に関するすべてのモジュールを格納するサブパッケージです。
        - **__init__.py**: `generate_repo_list`がPythonサブパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのライセンス、言語、ビルドステータスなどのバッジを生成するためのロジックを実装したスクリプトです。
        - **config.yml**: リポジトリ一覧生成スクリプトの技術的な設定パラメータ（例: プロジェクト概要取得の有効/無効、タイムアウト時間）を定義するYAML形式の設定ファイルです。
        - **config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するためのユーティリティスクリプトです。
        - **date_formatter.py**: 日付や時刻の情報を、人間が読みやすい形式や特定の出力要件に合わせて整形するためのユーティリティスクリプトです。
        - **generate_repo_list.py**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdown形式のリポジトリ一覧を生成します。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレートです。ウェブページの内容を検索エンジンに理解させやすくします。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を取得・処理し、表示可能な形式に整形するためのスクリプトです。
        - **markdown_generator.py**: 取得および処理されたリポジトリ情報から、最終的なMarkdown形式のコンテンツ（リポジトリ一覧）を生成するためのロジックを実装したスクリプトです。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で取得するためのスクリプトです。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ（例: Shields.ioのバッジ）の情報を解析・抽出するためのスクリプトです。
        - **repository_processor.py**: GitHub APIから取得した個々のリポジトリの生データを、プロジェクトの表示要件に合わせて整形・加工する役割を担うスクリプトです。
        - **seo_template.yml**: 検索エンジン最適化（SEO）のためのメタデータや構造化データの生成に使用されるテンプレートや設定を定義するYAMLファイルです。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計するためのスクリプトです。
        - **strings.yml**: アプリケーション内で表示される様々なメッセージや文言（例: ヘッダー、フッター、ボタンのテキスト）を国際化対応も考慮して一元管理するためのYAMLファイルです。
        - **template_processor.py**: Markdown生成の際に使用されるテンプレートファイルに対して、動的なデータを埋め込み、最終的な出力文字列を生成するためのスクリプトです。
        - **url_utils.py**: GitHub APIのエンドポイントURLの構築や、一般的なURLの検証・解析などのユーティリティ関数を提供するスクリプトです。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得）を検証するためのテストスクリプトです。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールが他のシステム（例: 実際のデータ取得）と連携して正しく機能するかを検証する統合テストスクリプトです。
    - **test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトの機能（大容量ファイルの検出）を検証するテストです。
    - **test_config.py**: `config_manager`モジュールや設定ファイル (`config.yml`, `ruff.toml`など) の読み込み、解析、および設定値の検証を行うテストスクリプトです。
    - **test_date_formatter.py**: `date_formatter`モジュールの日付整形機能が正しく動作するかを検証するテストスクリプトです。
    - **test_environment.py**: プロジェクトの実行環境（例: 必要な環境変数の存在、依存パッケージのインストール状態）が適切に設定されているかを検証するテストスクリプトです。
    - **test_integration.py**: `generate_repo_list.py`を含む、プロジェクトの主要なコンポーネントがエンドツーエンドで正しく連携し、期待される出力を生成するかを検証する包括的な統合テストです。
    - **test_markdown_generator.py**: `markdown_generator`モジュールが様々な入力データに対して、正しいMarkdown形式のコンテンツを生成するかを検証するテストスクリプトです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが、指定されたリポジトリから正確にプロジェクト概要をフェッチできるかを検証するテストスクリプトです。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEコンテンツからバッジ情報を正しく抽出できるかを検証するテストスクリプトです。
    - **test_repository_processor.py**: `repository_processor`モジュールがGitHub APIからの生データを適切に処理・変換できるかを検証するテストスクリプトです。

## 関数詳細説明
- **src/generate_repo_list/generate_repo_list.py**
    - **main()**: プロジェクトの主要な実行エントリポイントです。GitHub APIからリポジトリ情報を取得し、処理、そして最終的なMarkdownファイル（`index.md`）として出力する全体のオーケストレーションを行います。
        - 引数: なし (コマンドライン引数は内部で解析されます)
        - 戻り値: なし
- **src/generate_repo_list/repository_processor.py**
    - **process_repository(repo_data)**: GitHub APIから取得した個々のリポジトリの生データを受け取り、プロジェクトの表示要件（概要、バッジ、統計、言語など）に合わせて情報を抽出し、整形された辞書形式で返します。
        - 引数: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
        - 戻り値: `dict`: 整形され、表示用に最適化されたリポジトリ情報。
- **src/generate_repo_list/project_overview_fetcher.py**
    - **fetch_project_overview(repo_url, config)**: 指定されたGitHubリポジトリの特定のパス（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を非同期で取得します。設定に基づきキャッシュやリトライも考慮されます。
        - 引数: `repo_url` (str): リポジトリのGitHub URL, `config` (dict): プロジェクト概要取得に関する設定（有効/無効、ファイルパス、タイムアウトなど）。
        - 戻り値: `str` または `None`: 取得に成功した場合は概要文字列、失敗した場合は `None`。
- **src/generate_repo_list/markdown_generator.py**
    - **generate_repo_list_markdown(repositories_info, template, seo_config)**: 処理されたリポジトリ情報のリストと、使用するテンプレート、SEO設定を受け取り、それらを組み合わせて最終的なリポジトリ一覧のMarkdown文字列を生成します。
        - 引数: `repositories_info` (list): `process_repository`によって整形されたリポジトリ情報のリスト, `template` (str): Markdown生成に使用するテンプレート文字列, `seo_config` (dict): SEO関連の設定情報。
        - 戻り値: `str`: 生成されたMarkdown形式のリポジトリ一覧コンテンツ。
- **src/generate_repo_list/badge_generator.py**
    - **generate_badge_markdown(badge_type, value, style='flat')**: 指定されたバッジの種類（例: ライセンス、言語）と値に基づいて、Markdown形式で表示可能なバッジのURLと代替テキストを含む文字列を生成します。
        - 引数: `badge_type` (str): バッジのカテゴリ（例: "license", "language"）, `value` (str): バッジに表示するテキスト, `style` (str, オプション): バッジの表示スタイル（例: "flat"）。
        - 戻り値: `str`: 生成されたバッジのMarkdown文字列。
- **src/generate_repo_list/config_manager.py**
    - **load_config(config_path)**: 指定されたパスにあるYAML形式の設定ファイルを読み込み、その内容をPythonの辞書オブジェクトとして返します。
        - 引数: `config_path` (str): 読み込む設定ファイル（例: `config.yml`）のパス。
        - 戻り値: `dict`: 設定ファイルの内容を表す辞書。
- **src/generate_repo_list/date_formatter.py**
    - **format_date_for_display(iso_date_string)**: ISO 8601形式の日付文字列（GitHub APIから取得される形式）を受け取り、例えば「YYYY年MM月DD日」のような、人間が読みやすい形式に整形した日付文字列を返します。
        - 引数: `iso_date_string` (str): ISO 8601形式の日付文字列。
        - 戻り値: `str`: 整形された日付文字列。
- **src/generate_repo_list/language_info.py**
    - **get_top_languages(repo_languages_data)**: リポジトリの言語使用量データ（GitHub APIから取得）を受け取り、使用されている主要なプログラミング言語とその相対的な割合を抽出してリスト形式で返します。
        - 引数: `repo_languages_data` (dict): リポジトリの言語使用量を示す辞書。
        - 戻り値: `list`: 主要な言語情報のリスト。
- **src/generate_repo_list/readme_badge_extractor.py**
    - **extract_badges_from_readme(readme_content)**: READMEファイルのMarkdownコンテンツを受け取り、正規表現などを用いて、その中に埋め込まれている既存のバッジ（例: Shields.io形式）の情報を解析・抽出します。
        - 引数: `readme_content` (str): READMEファイルの全文コンテンツ。
        - 戻り値: `list`: 抽出されたバッジ情報（URLや代替テキストなど）のリスト。
- **src/generate_repo_list/statistics_calculator.py**
    - **calculate_repository_stats(repo_data)**: リポジトリの生データから、スター数、フォーク数、ウォッチ数、最終プッシュ日時などの主要な統計情報を抽出し、集計します。
        - 引数: `repo_data` (dict): GitHub APIから取得した単一リポジトリの生データ。
        - 戻り値: `dict`: 計算された統計情報を含む辞書。
- **src/generate_repo_list/template_processor.py**
    - **render_template(template_string, data)**: テンプレート文字列（プレースホルダーを含む）と、それに埋め込むデータ辞書を受け取り、プレースホルダーをデータで置換した最終的な文字列を生成します。
        - 引数: `template_string` (str): プレースホルダーを含むテンプレート文字列, `data` (dict): テンプレートに埋め込むキーと値のペア。
        - 戻り値: `str`: データが埋め込まれた最終的な文字列。
- **src/generate_repo_list/url_utils.py**
    - **build_github_api_url(username, endpoint)**: GitHubユーザー名とAPIエンドポイントパスを受け取り、GitHub APIの完全なURLを構築します。
        - 引数: `username` (str): GitHubユーザー名, `endpoint` (str): APIのエンドポイントパス（例: `/repos`, `/users/repos`）。
        - 戻り値: `str`: 構築されたGitHub APIのURL。
- **.github_automation/check_large_files/scripts/check_large_files.py**
    - **check_files_for_size(repo_path, config)**: 指定されたリポジトリパス内で、設定ファイルに基づいて定義された基準を超える大容量ファイルや特定の種類のファイルを検出します。
        - 引数: `repo_path` (str): チェック対象のリポジトリのファイルシステムパス, `config` (dict): 大容量ファイルチェックの設定。
        - 戻り値: `list`: 検出された大容量ファイルや問題のあるファイルのリスト。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-07 07:09:11 JST
