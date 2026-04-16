Last updated: 2026-04-17

# Project Overview

## プロジェクト概要
- GitHub APIを利用して、ユーザーのGitHubリポジトリ情報を自動で取得します。
- 取得した情報から、GitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧Markdownを自動生成します。
- 各リポジトリの概要を含め表示することで、検索エンジンやLLMからの参照性を向上させ、情報発見を容易にします。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesで静的サイトを構築するための静的サイトジェネレータ。本プロジェクトで生成されたMarkdownファイルをレンダリングするために使用されます。
    - Markdown: GitHub Pagesのリポジトリ一覧ページの内容を記述するための軽量マークアップ言語。
    - GitHub Pages: GitHubが提供する静的ウェブホスティングサービス。本プロジェクトで生成されたリポジトリ一覧ページのデプロイ先となります。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - GitHub API: GitHubのリポジトリ情報をプログラム的に取得するためのインターフェース。
    - Python: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得・加工・Markdown生成ロジックを実装しています。
    - pytest: Pythonアプリケーションのテストを効率的に実行するためのフレームワーク。
    - ruff: Pythonコードのリンティングとフォーマットを高速に行い、コード品質を維持するツール。
- テスト:
    - pytest: Pythonコードの単体テストや結合テストを実行するための堅牢なテストフレームワーク。
- ビルドツール:
    - Pythonスクリプト (`generate_repo_list.py`): GitHub APIから取得した情報に基づき、Markdownファイルを生成するカスタムビルドロジックを提供します。
    - Jekyll: 静的サイトジェネレータとして、生成されたMarkdownファイル群から最終的な静的ウェブサイトを構築します。
- 言語機能:
    - Python 3.x: プロジェクトのスクリプト開発に使用されるプログラミング言語。豊富なライブラリと高い可読性が特徴です。
- 自動化・CI/CD:
    - GitHub Actions (推測): `.github_automation` ディレクトリの存在から、GitHub Actionsを用いたリポジトリ情報の自動取得やMarkdown生成、サイト更新などの自動化処理が行われている可能性があります。
- 開発標準:
    - .editorconfig: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコードフォーマットを統一するための設定ファイル。
    - ruff: PythonコードがPEP 8などのスタイルガイドに準拠しているかチェックし、自動修正を行うことで、コードの一貫性と品質を保ちます。

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
-   **`.editorconfig`**: 異なるエディタやIDE間でコードスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   **`.github_automation/check_large_files/scripts/check_large_files.py`**: 特定の閾値を超えるサイズのファイルを検出するためのPythonスクリプト。CI/CDプロセスでのファイルサイズ管理に利用される可能性があります。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイルです。
-   **`LICENSE`**: 本プロジェクトのライセンス情報（MITライセンス）が記載されています。
-   **`README.md`**: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、全体的な情報を提供するメインドキュメントです。
-   **`_config.yml`**: Jekyllサイト全体の基本的な設定を定義するファイルです。
-   **`assets/`**: faviconなどの静的アセットを格納するディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleにおけるサイト所有権確認のために使用されるファイルです。
-   **`index.md`**: `src/generate_repo_list/generate_repo_list.py` スクリプトによって生成される、GitHubリポジトリ一覧を含むメインのMarkdownファイルです。GitHub Pagesのトップページとして機能します。
-   **`issue-notes/22.md`**: プロジェクトの開発中に記録された特定の問題や検討事項に関するノートファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータを定義するファイルです。ホーム画面に追加される際のアイコンや表示名などを指定します。
-   **`pytest.ini`**: `pytest` テストフレームワークの設定ファイルです。テストの発見ルールやオプションなどを定義します。
-   **`requirements.txt`**: このプロジェクトが実行時に依存するPythonパッケージとそのバージョンを列挙したファイルです。
-   **`requirements-dev.txt`**: 開発およびテスト時にのみ必要となるPythonパッケージとそのバージョンを列挙したファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは除外するかを指示するファイルです。
-   **`ruff.toml`**: `ruff` ツールによるPythonコードのリンティングとフォーマットに関する設定を定義するファイルです。
-   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する処理を全体的にオーケストレートします。
-   **`src/generate_repo_list/badge_generator.py`**: リポジトリに表示するバッジ（例: 言語、ステータス）を生成する機能を持つモジュールです。
-   **`src/generate_repo_list/config.yml`**: プロジェクトの実行時設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパス、タイムアウトなど）を定義するYAMLファイルです。
-   **`src/generate_repo_list/config_manager.py`**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の読み込みと管理を行うモジュールです。
-   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の書式設定を行うユーティリティモジュールです。
-   **`src/generate_repo_list/json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートを定義するファイルで、SEO強化のために使用されます。
-   **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を処理・整形するモジュールです。
-   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報と抽出した概要をもとに、SEO最適化されたMarkdown形式のコンテンツを生成するモジュールです。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出するロジックを実装するモジュールです。
-   **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEから特定のバッジ情報を抽出するモジュールです。
-   **`src/generate_repo_list/repository_processor.py`**: 個々のGitHubリポジトリ情報を処理し、整形してMarkdown生成に適したデータ構造に変換するロジックをカプセル化するモジュールです。
-   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや構造化データのテンプレートを定義するYAMLファイルです。
-   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（例: スター数、フォーク数など）を計算するモジュールです。
-   **`src/generate_repo_list/strings.yml`**: 生成されるMarkdownファイルやCLIの出力などで使用される表示メッセージや文言を管理するYAMLファイルです。
-   **`src/generate_repo_list/template_processor.py`**: Markdown生成におけるテンプレート処理（例: Jinja2などによる変数置換）を担うモジュールです。
-   **`src/generate_repo_list/url_utils.py`**: URLの生成や解析を行うユーティリティモジュールです。
-   **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。

## 関数詳細説明
※提供された情報に基づき、各ファイルの役割から主要な関数の機能を推測して記述しています。

-   **`generate_repo_list.py`**:
    -   `main()`: スクリプトのエントリポイント。コマンドライン引数を解析し、GitHubリポジトリ情報の取得、各リポジトリの処理、Markdownコンテンツの生成、そしてファイルへの出力といった一連の処理をオーケストレートします。
-   **`project_overview_fetcher.py`**:
    -   `fetch_project_overview(repo_name, owner, token, config)`: 指定されたリポジトリから `generated-docs/project-overview.md` ファイルを読み込み、設定（`section_title`など）に基づいてプロジェクト概要の3行説明を抽出して返します。GitHub APIを介したファイル内容の取得、エラー処理、およびキャッシュ管理も行います。
-   **`markdown_generator.py`**:
    -   `generate_markdown(repo_data_list, strings_config, seo_template, overview_config)`: 複数のリポジトリデータ（名前、説明、言語、概要など）を受け取り、定義されたテンプレート、文字列設定、SEO設定に基づき、リポジトリ一覧を含むMarkdown形式の文字列コンテンツを生成します。
-   **`repository_processor.py`**:
    -   `process_repository(repo_info, config)`: 単一のGitHubリポジトリの生データオブジェクトを受け取り、必要な情報を抽出し（例: 名前、URL、説明、言語、スター数、最終更新日）、さらに `project_overview_fetcher` を呼び出して概要を取得するなどして、Markdown生成に適した整形されたデータ構造に変換します。
-   **`badge_generator.py`**:
    -   `generate_badge(badge_type, value)`: 特定のタイプ（例: 言語、アクティブ/アーカイブステータス）と値に基づいて、表示用のバッジ（Markdown形式の画像リンクなど）を生成します。
-   **`config_manager.py`**:
    -   `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、Pythonディクショナリとして返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層は分析できませんでした。

---
Generated at: 2026-04-17 07:17:49 JST
