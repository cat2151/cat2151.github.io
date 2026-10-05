Last updated: 2026-10-06

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成し、SEOとLLMの参照性を向上させるシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、各リポジトリの概要を含むMarkdownファイルを生成します。
- 生成されたページはJekyllにより公開され、プロジェクトの情報を効果的に外部に伝達します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤)、Markdown (生成されるコンテンツ形式)、HTML/CSS (Jekyllによる最終的なウェブページ出力)
- 音楽・オーディオ: なし
- 開発ツール: Python (主要なスクリプト言語)、Pytest (単体・統合テストフレームワーク)、Ruff (コードリンターおよびフォーマッター)、YAML (設定ファイル管理)、TOML (シークレット・設定ファイル管理)
- テスト: Pytest (Pythonテストフレームワーク)
- ビルドツール: なし (JekyllによるウェブサイトのビルドはGitHub Pages側で処理)
- 言語機能: Python (GitHub APIとの連携、ファイル操作、文字列処理など)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリで示唆される大規模ファイルチェックなどの自動化処理に使用される可能性がありますが、リポジトリ一覧生成プロセス自体はローカル実行が重視されています。)
- 開発標準: Ruff (Pythonコードのスタイル統一と品質維持)

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
- **.editorconfig**: 複数の開発者が異なるエディタを使用する際に、コードのフォーマットやスタイルを統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどを用いた自動化処理に関連するファイルを格納するディレクトリ。
    - **check_large_files/**: 大容量ファイルチェックツールに関連するファイル群。
        - **README.md**: `check_large_files`ツールの説明。
        - **check-large-files.toml**: `check_large_files`ツールの設定ファイル。
        - **scripts/check_large_files.py**: 大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitが追跡しないファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
- **README.md**: プロジェクトの目的、機能、使用方法、設定、開発者向け情報などを説明するメインのドキュメント。
- **_config.yml**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を定義。
- **assets/**: GitHub Pagesサイトで利用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`機能のデバッグ目的で使用されるスクリプト。
- **generated-docs/**: 各リポジトリから取得した概要などの情報が一時的に、または最終的に格納される可能性のあるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleのサイト所有権確認用ファイル。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧を記述したメインのMarkdownファイル。Jekyllによって処理され、サイトのトップページとなる。
- **issue-notes/**: 開発中の課題やメモなどを記録するためのディレクトリ。
    - **22.md**: 特定の課題に関するメモファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブアプリの名前、アイコン、表示モードなどを定義。
- **pytest.ini**: Pytestテストフレームワークの設定ファイル。テストの検出ルールや実行オプションを定義。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonライブラリの依存関係を記述したファイル。
- **requirements.txt**: プロジェクトの実行に必要なPythonライブラリの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Ruffリンターおよびフォーマッターの設定ファイル。コードのスタイルや品質に関するルールを定義。
- **src/**: プロジェクトのソースコードを格納するメインディレクトリ。
    - **__init__.py**: Pythonパッケージを示すためのファイル。
    - **generate_repo_list/**: リポジトリ一覧生成システムの主要なモジュール群。
        - **__init__.py**: Pythonサブパッケージを示すためのファイル。
        - **badge_generator.py**: リポジトリの言語やライセンスなどのバッジ画像を生成または準備するロジック。
        - **config.yml**: `project_overview`機能などの技術的なパラメータを定義する設定ファイル。
        - **config_manager.py**: YAMLファイルからの設定読み込みと管理を行うモジュール。
        - **date_formatter.py**: GitHub APIから取得した日付情報を特定のフォーマットに整形するロジック。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成するメインスクリプト。
        - **json_ld_template.json**: 構造化データ（JSON-LD）のテンプレートファイル。SEOを強化するために使用。
        - **language_info.py**: リポジトリの主要言語に関する情報を処理し、表示に役立つ形式に変換するロジック。
        - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツを構築するロジック。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し取得するロジック。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルからバッジ（例: ビルドステータス、カバレッジ）の情報を抽出するロジック。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報に加工するモジュール。
        - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するファイル。
        - **statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算するロジック。
        - **strings.yml**: UIメッセージ、説明文、タイトルなどの表示用テキストを一元管理する設定ファイル。
        - **template_processor.py**: JekyllやMarkdownのテンプレートにデータを埋め込む処理を行うモジュール。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連のユーティリティ関数を集めたモジュール。
- **test_project_overview.py**: `project_overview_fetcher`機能の単体テストまたは統合テストスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **conftest.py**: Pytestのフィクスチャやヘルパー関数を定義するファイル。
    - **test_badge_generator_integration.py**: `badge_generator`モジュールの統合テスト。
    - **test_check_large_files.py**: `check_large_files`スクリプトのテスト。
    - **test_config.py**: 設定ファイルの読み込みと処理に関するテスト。
    - **test_date_formatter.py**: 日付フォーマット処理に関するテスト。
    - **test_environment.py**: 実行環境に関するテスト。
    - **test_integration.py**: プロジェクト全体の主要なフローに関する統合テスト。
    - **test_markdown_generator.py**: Markdown生成ロジックに関するテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールのテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor`モジュールのテスト。

## 関数詳細説明
*関数名はPythonファイルの一般的な慣例とプロジェクトの機能から推測して記述しています。*

- **generate_repo_list.py**:
    - **main()**: プログラムのエントリポイント。コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得、加工し、Markdownファイルを生成する一連の処理を orchestrate します。
        - **引数**: `username` (GitHubユーザー名), `output` (出力ファイル名), `limit` (処理するリポジトリ数の上限)
        - **戻り値**: なし
        - **機能**: GitHub APIからのデータ取得、リポジトリ情報のフィルタリングと処理、Markdown生成モジュールへのデータ渡し、最終的なファイル出力。
- **config_manager.py**:
    - **load_config(file_path: str) -> dict**: 指定されたYAMLまたはTOMLファイルから設定を読み込み、辞書形式で返します。
        - **引数**: `file_path` (設定ファイルのパス)
        - **戻り値**: 設定内容を格納した辞書
        - **機能**: 設定ファイルが存在しない場合や解析エラーの場合のハンドリングを含みます。
- **project_overview_fetcher.py**:
    - **fetch_project_overview(repo_name: str, config: dict) -> str**: 指定されたリポジトリから、設定ファイルに定義されたパスとセクションタイトルに基づいてプロジェクト概要（3行説明）を抽出します。
        - **引数**: `repo_name` (GitHubリポジトリ名), `config` (プロジェクト概要取得機能の設定)
        - **戻り値**: 抽出されたプロジェクト概要の文字列、または空文字列
        - **機能**: HTTPクライアントを用いてリポジトリからMarkdownファイルを読み込み、正規表現などを用いて特定のセクションをパースします。APIリトライやキャッシュ機能もサポート。
- **repository_processor.py**:
    - **process_repository(repo_data: dict) -> dict**: GitHub APIから取得した単一リポジトリの生データを、Markdown生成に適した形式に加工します。
        - **引数**: `repo_data` (GitHub APIから取得したリポジトリ情報を含む辞書)
        - **戻り値**: 整形されたリポジトリ情報を含む辞書
        - **機能**: 言語情報、スター数、最終更新日などの抽出、バッジ情報の追加、プロジェクト概要の取得（`project_overview_fetcher`を呼び出し）など。
- **markdown_generator.py**:
    - **generate_markdown(repositories: list[dict], template: str) -> str**: 処理されたリポジトリ情報のリストとテンプレート文字列を受け取り、最終的なMarkdownコンテンツを生成します。
        - **引数**: `repositories` (整形されたリポジトリ情報のリスト), `template` (Markdownテンプレート文字列)
        - **戻り値**: 生成されたMarkdownコンテンツの文字列
        - **機能**: テンプレートエンジン（例: Jinja2など）を使用して、リポジトリデータをテンプレートに埋め込み、Markdown形式の出力を生成します。
- **badge_generator.py**:
    - **get_badge_url(badge_type: str, value: str) -> str**: 指定されたバッジタイプと値に基づいて、Shields.ioなどのバッジサービスのURLを生成します。
        - **引数**: `badge_type` (バッジの種類、例: 'language', 'license'), `value` (バッジに表示する値)
        - **戻り値**: バッジ画像のURL
        - **機能**: プロジェクトの標準的なバッジ表示ルールに従い、動的にバッジのURLを構築します。
- **date_formatter.py**:
    - **format_date(iso_date: str) -> str**: ISO 8601形式の日付文字列を受け取り、人間が読みやすい形式に整形します。
        - **引数**: `iso_date` (ISO 8601形式の日付文字列)
        - **戻り値**: フォーマットされた日付文字列
        - **機能**: `YYYY年MM月DD日`のような形式への変換。
- **statistics_calculator.py**:
    - **calculate_repo_statistics(repo_data: list[dict]) -> dict**: リポジトリのリストから、全体の統計情報（例: 総リポジトリ数、最多言語など）を計算します。
        - **引数**: `repo_data` (整形されたリポジトリ情報のリスト)
        - **戻り値**: 計算された統計情報を含む辞書
        - **機能**: リポジトリの状態（アクティブ、アーカイブ、フォーク）ごとの集計、言語の使用頻度などを分析します。
- **url_utils.py**:
    - **create_github_repo_url(username: str, repo_name: str) -> str**: GitHubリポジトリのURLを生成します。
        - **引数**: `username` (GitHubユーザー名), `repo_name` (リポジトリ名)
        - **戻り値**: GitHubリポジトリの完全なURL
        - **機能**: GitHubのURL構造に基づき、正しいリンクを生成します。
- **check_large_files.py** (`.github_automation/check_large_files/scripts/`内):
    - **main()**: 特定の閾値を超える大容量ファイルを検出するためのスクリプトのエントリポイント。
        - **引数**: なし (設定ファイルから閾値などを読み込む)
        - **戻り値**: なし (検出結果を出力または特定のステータスコードで終了)
        - **機能**: ディレクトリ内のファイルを走査し、サイズをチェックして、設定された制限を超えるファイルを報告します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-10-06 07:12:54 JST
