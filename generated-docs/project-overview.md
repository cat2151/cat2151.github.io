Last updated: 2026-08-26

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動取得するシステムです。
- 取得した情報から、GitHub Pages向けにSEO最適化されたMarkdown形式のリポジトリ一覧を生成します。
- 検索エンジンからの発見性を高め、LLMがリポジトリ参照に失敗する課題を緩和することを目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターとして、自動生成されたMarkdownファイルから最終的なWebページを構築します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語です。
    - Git: ソースコードのバージョン管理に使用されます。
    - GitHub API: リポジトリ情報（説明、言語、スター数など）の取得に使用されます。
    - requests: PythonからGitHub APIへのHTTPリクエストを送信するために使用されます。
    - PyYAML: `config.yml`, `strings.yml`, `seo_template.yml` などのYAML形式の設定ファイルを読み書きするために使用されます。
    - toml: GitHubトークンなどの秘密情報を管理する `secrets.toml` ファイルの読み込みに使用されます。
- テスト:
    - pytest: Pythonコードのユニットテストおよび統合テストを実行するためのフレームワークです。
- ビルドツール:
    - Jekyll: GitHub Pagesサイトを生成し、デプロイするために利用される静的サイトジェネレーターです。
    - requirements.txt / requirements-dev.txt: プロジェクトの依存関係にあるPythonパッケージを管理します。
- 言語機能:
    - Python標準ライブラリ: スクリプト内で広く利用される基本的なデータ処理、ファイル操作、ネットワーク通信などの機能を提供します。
- 自動化・CI/CD:
    - GitHub Actions (推測): `.github_automation/` ディレクトリに存在するスクリプト (`check_large_files.py` など) から、コード品質チェックやファイルサイズチェックといった自動化処理が継続的インテグレーション/デリバリーの一環としてGitHub Actionsで実行される可能性が示唆されます。
- 開発標準:
    - ruff: Pythonコードの高速なリントとフォーマットを行うツールです。`ruff.toml` で設定が管理されます。
    - .editorconfig: 異なるエディタやIDE間でインデントスタイル、文字コード、行末文字などのコードスタイルを統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で、インデントスタイル、文字コード、改行コードなどのコードスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するためのディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    - **`check_large_files/check-large-files.toml`**: 大容量ファイルチェック機能の設定を定義するTOMLファイルです。
    - **`check_large_files/scripts/check_large_files.py`**: 特定の閾値を超える大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリのパターンを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行方法、開発者向けのヒントなどを説明する主要なドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の共通設定を定義するファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などが設定されます。
- **`assets/`**: Jekyllサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: 異なるサイズのファビコン画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能の動作確認やデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: GitHub Pagesサイト用に生成されたMarkdownファイルなどを一時的または最終的に格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: GitHub PagesサイトのトップページとなるMarkdownファイルです。本プロジェクトのスクリプトによってリポジトリ一覧の内容がここに生成・出力されます。
- **`issue-notes/`**: 開発中の課題や検討事項に関するメモを格納するディレクトリです。
    - **`issue-notes/22.md`**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモや考察を記述したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルであり、アプリのアイコン、表示モード、起動URLなどをブラウザに伝えます。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonパッケージの依存関係を記述したファイルです。
- **`requirements.txt`**: プロジェクトの実行に最低限必要なPythonパッケージの依存関係を記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードの整形（フォーマット）と静的解析（リント）を行うツール「Ruff」の設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    - **`src/generate_repo_list/`**: GitHubリポジトリ一覧生成機能に関連するPythonモジュール群を格納するパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイルです。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語、ステータス、ライセンスなどを示す各種バッジの生成ロジックを提供するモジュールです。
        - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行に関する技術的パラメータや設定を定義するYAMLファイルです。
        - **`src/generate_repo_list/config_manager.py`**: `config.yml` などの設定ファイルを読み込み、設定値へのアクセスを管理するモジュールです。
        - **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の情報をユーザーフレンドリーな形式に整形するための機能を提供するモジュールです。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプトです。GitHub APIからの情報取得、データの処理、Markdownファイルの生成といった一連の処理を調整します。
        - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理し、表示に役立つ形式に変換する機能を提供するモジュールです。
        - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報に基づいて、Jekyllが解釈できるMarkdown形式のコンテンツを生成するモジュールです。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出し、取得する機能を提供するモジュールです。
        - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから、既存のバッジ（例: ビルドステータス、コードカバレッジ）の情報を抽出するモジュールです。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを整形し、Markdown生成に必要な情報（説明、トピック、URLなど）を準備するモジュールです。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化コンテンツのテンプレート定義を含むYAMLファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（スター数、フォーク数、コミット数など）を計算または集計する機能を提供するモジュールです。
        - **`src/generate_repo_list/strings.yml`**: UIに表示される各種メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。これにより、文言の変更や多言語対応が容易になります。
        - **`src/generate_repo_list/template_processor.py`**: 処理されたデータをJekyllなどのテンプレートエンジンが利用できる形式に変換し、テンプレートに適用する機能を提供するモジュールです。
        - **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ機能を提供するモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能をテストするためのスクリプトです。
- **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
    - **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator.py` の結合テストを行うスクリプトです。
    - **`tests/test_check_large_files.py`**: `.github_automation/check_large_files/scripts/check_large_files.py` の機能をテストするスクリプトです。
    - **`tests/test_config.py`**: 設定管理モジュール（`config_manager.py`など）の機能をテストするスクリプトです。
    - **`tests/test_date_formatter.py`**: `date_formatter.py` の日付整形機能をテストするスクリプトです。
    - **`tests/test_environment.py`**: テスト実行環境のセットアップや依存関係が正しく機能するかを検証するスクリプトです。
    - **`tests/test_integration.py`**: プロジェクトの主要なコンポーネント間の連携を検証する結合テストスクリプトです。
    - **`tests/test_markdown_generator.py`**: `markdown_generator.py` のMarkdown生成機能をテストするスクリプトです。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py` のプロジェクト概要取得機能をテストするスクリプトです。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor.py` のREADMEからのバッジ抽出機能をテストするスクリプトです。
    - **`tests/test_repository_processor.py`**: `repository_processor.py` のリポジトリデータ処理機能をテストするスクリプトです。

## 関数詳細説明
提供された情報からは具体的な関数名、引数、戻り値、機能の詳細は検出されませんでした。
唯一、`googled947dc864c270e07.html` ファイルには関数が存在しないことが示されています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-26 07:07:15 JST
