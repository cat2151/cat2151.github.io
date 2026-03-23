Last updated: 2026-03-24

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、公開リポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEO最適化されたMarkdown形式で出力します。
- リポジトリの発見性を高め、検索エンジンやLLMによる参照の課題を緩和することを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: (このプロジェクトには該当する技術はありません)
- 開発ツール: Python (主要な開発言語), GitHub API (リポジトリ情報取得), requests (HTTPリクエストライブラリ), PyYAML (設定ファイル読み込み)
- テスト: pytest (Python用テストフレームワーク)
- ビルドツール: (自身がMarkdownファイルを生成するシステムであるため、特定のビルドツールは使用していません)
- 言語機能: Pythonの標準ライブラリ（ファイル操作、文字列処理など）
- 自動化・CI/CD: (ローカル開発重視の構成ですが、`.github_automation` ディレクトリでファイルサイズチェック等の自動化スクリプトが含まれます)
- 開発標準: Ruff (Pythonコードのフォーマッター/リンター), .editorconfig (エディタのコードスタイル統一設定)

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
- **`.editorconfig`**: 複数の開発者やエディタ間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化されたワークフローやスクリプトを格納するディレクトリです。
    - **`check_large_files/README.md`**: `check_large_files` 機能の概要を説明するドキュメントです。
    - **`check_large_files/check-large-files.toml`**: 大容量ファイルチェックツールの設定ファイルです。
    - **`check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリ（例: ビルド成果物、一時ファイル）を指定する設定ファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスで公開されていることを示すファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定方法などを説明するメインのドキュメントです。
- **`_config.yml`**: Jekyllで構築されるGitHub Pagesサイト全体の動作設定を定義するファイルです。
- **`assets/`**: GitHub Pagesサイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザのタブに表示されるアイコン）の各サイズ画像です。
- **`debug_project_overview.py`**: 各リポジトリからプロジェクト概要を自動取得する機能のデバッグ用途で使われるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやコンテンツが配置されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有者認証に使用されるHTMLファイルです。
- **`index.md`**: メインのMarkdownファイルで、生成されたリポジトリ一覧のコンテンツが記述されます。これがGitHub Pagesのトップページになります。
- **`issue-notes/`**: プロジェクト開発中に発生した課題や検討事項を記録するメモファイルが格納されるディレクトリです。
    - **`22.md`**: 特定の課題（例: Issue #22）に関する詳細なメモです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）を定義するマニフェストファイルで、ウェブサイトをデスクトップやモバイルのアプリのように見せるための情報を提供します。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の動作を設定するためのファイルです。
- **`requirements-dev.txt`**: プロジェクトの開発時やテスト時に必要なPythonライブラリのリストです。
- **`requirements.txt`**: プロジェクトが実行される本番環境で最低限必要なPythonライブラリのリストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールし、どのページをクロールしないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックや自動修正を行うツール`Ruff`の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧を生成する主要なロジックを含むPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
        - **`badge_generator.py`**: GitHubリポジトリのステータスや情報を示すバッジを生成または処理するロジックが含まれています。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの実行時設定（例: GitHub APIの振る舞い、プロジェクト概要取得機能の有効/無効）を定義するファイルです。
        - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム全体で利用できるように管理するモジュールです。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理を実行します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、コンテンツの構造化データ（JSON-LD形式）を定義するためのテンプレートファイルです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理するためのロジックが含まれています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報をもとに、GitHub Pages用のMarkdownコンテンツを生成する主要なモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動的に取得するロジックを提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、バッジ（例: ビルドステータス、ライセンス）の情報を抽出するロジックです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を担います。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータ（タイトル、ディスクリプションなど）を生成する際のテンプレート設定ファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日時などの統計情報を計算・集計するロジックです。
        - **`strings.yml`**: プログラム内で使用される各種メッセージや文言（例: 見出し、説明文）を一元的に管理するためのファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: JekyllやMarkdownのテンプレートファイルを読み込み、動的なデータを埋め込んで最終的なコンテンツを生成するモジュールです。
        - **`url_utils.py`**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の複数の要素を組み合わせた統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェックスクリプトの単体テストまたは統合テストです。
    - **`test_config.py`**: 設定ファイル読み込みや管理機能のテストです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストです。
    - **`test_environment.py`**: プロジェクトの実行環境が適切に設定されているかを検証するテストです。
    - **`test_integration.py`**: プロジェクトの主要なフローや複数のモジュールにまたがる統合的なテストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックのテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: `README.md`からのバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリデータ処理ロジックのテストです。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py` の主要関数**:
    - **`main()`**: プログラムのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得、処理、Markdown生成の一連のフローを制御・実行します。
        - 引数: なし (コマンドライン引数は内部で解析)
        - 戻り値: なし (ファイル出力が主な副作用)
        - 機能: 設定読み込み、GitHub APIからのリポジトリ取得、各リポジトリのデータ加工、Markdownコンテンツ生成、ファイル書き込みを行います。
- **`src/generate_repo_list/repository_processor.py` の主要関数**:
    - **`fetch_repositories(username, token, config)`**: 指定されたGitHubユーザー名と認証トークンを使用して、GitHub APIからユーザーのリポジトリ情報を取得します。
        - 引数: `username` (str): GitHubユーザー名, `token` (str): GitHub認証トークン, `config` (dict): 設定情報
        - 戻り値: `list`: 取得したリポジトリデータのリスト
        - 機能: GitHub REST APIを呼び出し、リポジトリの一覧と詳細データを取得し、エラーハンドリングを行います。
    - **`process_repository_data(repo_data, config, fetcher)`**: 取得した生のリポジトリデータを整形し、Markdown生成に適した形式に変換します。各リポジトリの概要取得もここで行われます。
        - 引数: `repo_data` (dict): 単一リポジトリのGitHub APIレスポンス, `config` (dict): 設定情報, `fetcher` (ProjectOverviewFetcher): プロジェクト概要取得モジュールのインスタンス
        - 戻り値: `dict`: 処理済みのリポジトリ情報（Markdown生成用）
        - 機能: 日付フォーマット、言語情報処理、プロジェクト概要取得などを統合し、表示に必要な情報を整理します。
- **`src/generate_repo_list/project_overview_fetcher.py` の主要関数**:
    - **`fetch_project_overview(repo_url, config)`**: 指定されたリポジトリURLから、設定ファイルに指定されたパスにあるプロジェクト概要ファイル (`project-overview.md`) を読み込み、その内容（特に3行説明）を抽出します。
        - 引数: `repo_url` (str): リポジトリのベースURL, `config` (dict): 設定情報
        - 戻り値: `str` または `None`: 抽出されたプロジェクト概要のテキスト、または取得できなかった場合は`None`
        - 機能: HTTPリクエストでファイルをフェッチし、Markdownを解析して特定のセクションからテキストを抽出します。
- **`src/generate_repo_list/markdown_generator.py` の主要関数**:
    - **`generate_markdown(repositories_data, config, strings)`**: 処理済みのリポジトリデータのリストと設定・文言データを用いて、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
        - 引数: `repositories_data` (list): 処理済みリポジトリ情報のリスト, `config` (dict): 設定情報, `strings` (dict): 表示文言
        - 戻り値: `str`: 生成されたMarkdownコンテンツ
        - 機能: テンプレートとデータを使って動的にMarkdownを組み立て、SEOメタデータや各リポジトリの表示要素を配置します。
- **`src/generate_repo_list/config_manager.py` の主要関数**:
    - **`load_config(config_path)`**: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonの辞書形式で返します。
        - 引数: `config_path` (str): 設定ファイルのパス
        - 戻り値: `dict`: 読み込まれた設定
        - 機能: YAMLファイルをパースし、設定値をプログラムで使用可能な形式にします。
    - **`load_strings(strings_path)`**: 指定されたパスからYAML形式の文言ファイルを読み込み、Pythonの辞書形式で返します。
        - 引数: `strings_path` (str): 文言ファイルのパス
        - 戻り値: `dict`: 読み込まれた文言
        - 機能: YAMLファイルをパースし、表示メッセージをプログラムで使用可能な形式にします。

## 関数呼び出し階層ツリー
```
このプロジェクトの関数呼び出し階層は、自動分析では特定できませんでした。
しかし、主要な実行フローは以下のようになります（概念的な階層）。

`generate_repo_list.py` の `main()` 関数が起点となり、
各モジュール内の主要な関数を連携して呼び出します。

main()
  ├─ config_manager.load_config()
  ├─ config_manager.load_strings()
  ├─ repository_processor.fetch_repositories()
  │    └─ (内部でGitHub APIを呼び出し)
  ├─ (各リポジトリに対してループ)
  │    ├─ repository_processor.process_repository_data()
  │    │    ├─ project_overview_fetcher.fetch_project_overview()
  │    │    │    └─ (内部でHTTPリクエストとMarkdown解析)
  │    │    ├─ date_formatter.format_date()
  │    │    ├─ readme_badge_extractor.extract_badges_from_readme()
  │    │    └─ statistics_calculator.calculate_repository_statistics()
  │    └─ (処理済みデータをリストに追加)
  └─ markdown_generator.generate_markdown()
       └─ template_processor.render_template()
       └─ badge_generator.generate_badge_markup()
  └─ (生成されたMarkdownコンテンツをファイルに書き出し)

---
Generated at: 2026-03-24 07:11:09 JST
