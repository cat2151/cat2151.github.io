Last updated: 2026-11-28

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 生成されたMarkdownはSEO最適化され、検索エンジンからのアクセス性を向上させます。
- リポジトリの発見性を高め、LLMなどによる参照失敗を緩和し開発効率を向上させます。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesサイトの構築に利用される静的サイトジェネレーター。MarkdownファイルをHTMLに変換します。
    - Markdown: リポジトリ一覧の出力形式であり、コンテンツ記述に用いられます。
    - JSON-LD: 検索エンジン最適化（SEO）のために、構造化データをウェブページに埋め込むための形式です。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語として、リポジトリ情報の取得とMarkdown生成に利用されます。
    - pytest: Pythonアプリケーションのテストフレームワークとして、ユニットテストおよび統合テストの実行に用いられます。
    - ruff: Pythonコードのスタイルチェック、フォーマット、リンティングを高速に実行するためのツールです。
    - Git/GitHub: バージョン管理システムおよびリポジトリホスティングサービスとして利用され、リポジトリ情報の取得元となります。
- テスト:
    - pytest: Pythonコードの品質と信頼性を保証するためのテストフレームワークです。
- ビルドツール:
    - Jekyll: GitHub Pagesによって、Markdownファイルを静的なウェブサイトとしてビルド・公開するために使用されます。
- 言語機能:
    - Pythonの標準ライブラリ: HTTPリクエスト、ファイルI/O、データ構造操作など、多岐にわたる処理に利用されます。
    - YAML: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）の記述に用いられます。
    - TOML: ローカル実行時のGitHubトークンなど、秘密情報の管理や一部の設定ファイル（`check-large-files.toml`）に利用されます。
- 自動化・CI/CD:
    - Pythonスクリプト: `generate_repo_list.py`がリポジトリ一覧の自動生成を担い、GitHub Pagesの更新を自動化します。
    - GitHub Pages: GitHubリポジトリからウェブサイトを自動的に公開するホスティングサービスです。
- 開発標準:
    - ruff: コードの一貫性を保ち、品質を向上させるための自動フォーマットおよびリンティングツールです。
    - .editorconfig: 異なるエディタやIDE間でのコーディングスタイル（インデント、文字コードなど）の統一を図るための設定ファイルです。

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイル、文字セット、改行コードなどのコーディングスタイルを統一するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリ。
    - **.github_automation/check_large_files/**: 大容量ファイルに関するチェック機能のモジュール。
        - **.github_automation/check_large_files/README.md**: `check_large_files`機能に関する説明ドキュメント。
        - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の設定ファイル。
        - **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出し、警告するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象外とすべきファイルやディレクトリのパターンを定義するファイル。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）が記載されたファイル。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、使用方法などを説明するメインドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。テーマ、プラグイン、パーマリンク構造などを設定します。
- **assets/**: GitHub Pagesサイトで使用される静的アセット（画像、アイコンなど）を格納するディレクトリ。
    - **assets/favicon-*.png**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の各種サイズ画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher`機能の動作確認やデバッグを目的としたスクリプト。
- **generated-docs/**: 自動生成されたドキュメントや、外部リポジトリから取得したドキュメント（例：プロジェクト概要）を一時的に、または永続的に格納するディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるファイル。内容はGoogleが指定する特定の文字列を含みます。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイル。`generate_repo_list.py`スクリプトによってリポジトリ一覧が生成され、このファイルに出力されます。
- **issue-notes/**: プロジェクト開発中に発生した課題や検討事項をメモとして残すためのディレクトリ。
    - **issue-notes/22.md**: 特定の課題（Issue #22など）に関する詳細なノートや検討内容を記述したMarkdownファイル。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイル。ウェブサイトをユーザーのホーム画面に追加する際の表示設定（名前、アイコン、起動画面など）を定義します。
- **pytest.ini**: Pythonのテストフレームワーク`pytest`の設定ファイル。テスト検出パターン、実行オプション、プラグインなどを定義します。
- **requirements-dev.txt**: 開発環境およびテスト環境でのみ必要となるPythonパッケージの依存関係をリストアップしたファイル。
- **requirements.txt**: プロジェクトの実行（本番環境など）に必要となるPythonパッケージの依存関係をリストアップしたファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールすべきか、あるいは避けるべきかを指示するファイル。SEOに影響を与えます。
- **ruff.toml**: Pythonのリンターおよびフォーマッターである`ruff`の設定ファイル。コードスタイルルール、無視するファイル、フォーマットオプションなどを定義します。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリ。
    - **src/__init__.py**: Pythonのパッケージとして認識させるためのファイル。通常は空です。
    - **src/generate_repo_list/**: リポジトリ一覧を生成する機能の中核をなすPythonパッケージ。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイル。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの言語、スター数、最終更新日などの情報を基に、Markdown形式のバッジ画像を生成するための機能を提供します。
        - **src/generate_repo_list/config.yml**: プロジェクトの実行時設定（例: プロジェクト概要取得機能の有効/無効、ターゲットファイル名、リトライ回数など）を定義するファイル。
        - **src/generate_repo_list/config_manager.py**: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するためのモジュール。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を特定のフォーマット（例: 相対時間、特定の日付形式）に変換するためのユーティリティ関数を提供します。
        - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、それを処理してMarkdown形式のリポジトリ一覧ファイルを生成するメインスクリプト。
        - **src/generate_repo_list/json_ld_template.json**: SEO最適化のため、JSON-LD形式の構造化データを生成する際のテンプレートとして使用されます。
        - **src/generate_repo_list/language_info.py**: リポジトリのプログラミング言語に関する情報を取得、処理、表示するための機能を提供します。
        - **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報を受け取り、バッジ、リンク、説明などを含む整形されたMarkdown文字列を生成するモジュール。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動的に抽出する機能を提供します。
        - **src/generate_repo_list/readme_badge_extractor.py**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、ライセンス）を抽出するためのモジュール。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を解析し、必要な情報を抽出し、アプリケーションで使いやすい形式に整形する機能を提供します。
        - **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータや構造化データの生成に使用されるテンプレート設定を定義するファイル。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するための機能を提供します。
        - **src/generate_repo_list/strings.yml**: UIメッセージ、説明文、ラベルなど、アプリケーション全体で使用される表示用の文字列を管理するファイル。国際化/ローカライズに対応するために利用されます。
        - **src/generate_repo_list/template_processor.py**: Markdown生成などで使用されるテキストテンプレートを処理し、動的なデータを埋め込むための汎用的な機能を提供します。
        - **src/generate_repo_list/url_utils.py**: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `src/generate_repo_list/project_overview_fetcher.py`モジュールの機能（プロジェクト概要の取得と抽出）をテストするためのスクリプト。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリ。
    - **tests/conftest.py**: `pytest`の共通フィクスチャやヘルパー関数を定義するファイル。テスト間で共有されるリソースや設定を提供します。
    - **tests/test_badge_generator_integration.py**: `badge_generator`モジュールの統合テスト。バッジが正しく生成されるか、複数の要素が組み合わされた場合に期待通りの結果となるかを確認します。
    - **tests/test_check_large_files.py**: `.github_automation/check_large_files/scripts/check_large_files.py`スクリプトの機能をテストします。大容量ファイルが正しく検出されるかなどを検証します。
    - **tests/test_config.py**: `config_manager`モジュールが設定ファイルを正しく読み込み、値を提供するかどうかをテストします。
    - **tests/test_date_formatter.py**: `date_formatter`モジュールの日付フォーマット機能が、様々な入力に対して期待される出力を生成するかどうかをテストします。
    - **tests/test_environment.py**: テスト実行環境や依存関係が正しくセットアップされているかどうかを検証するテスト。
    - **tests/test_integration.py**: プロジェクトの主要なコンポーネントが連携して正しく機能するかを確認する統合テスト。
    - **tests/test_markdown_generator.py**: `markdown_generator`モジュールが提供されたデータから正しいMarkdown文字列を生成するかどうかをテストします。
    - **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが、指定されたファイルからプロジェクト概要を正確に抽出できるかをテストします。
    - **tests/test_readme_badge_extractor.py**: `readme_badge_extractor`モジュールがREADMEファイルからバッジ情報を正しく抽出できるかどうかをテストします。
    - **tests/test_repository_processor.py**: `repository_processor`モジュールがGitHub APIからのリポジトリデータを正しく処理し、整形できるかどうかをテストします。

## 関数詳細説明
このプロジェクトでは、主にPythonスクリプトとモジュールに機能が分割されており、以下の主要な機能を持つモジュールが存在します。具体的な関数名はコードに依存しますが、各モジュールが担う役割に基づいて主要な機能を説明します。

- **generate_repo_list.py** (メインスクリプト):
    - **役割と機能**: プロジェクトのエントリポイントであり、GitHub APIからリポジトリ情報を取得し、処理、最終的にGitHub Pages用のMarkdownファイルを生成します。コマンドライン引数（ユーザー名、出力ファイル、リポジトリ数制限など）を解析し、他のモジュールを協調させて全体の処理フローを制御します。
- **repository_processor.py**:
    - **役割と機能**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、プロジェクトで利用しやすい構造化されたデータに変換します。リポジトリのアクティブ/アーカイブ状態、フォークの有無などを判別し、カテゴリ分けを行う機能も含みます。
- **project_overview_fetcher.py**:
    - **役割と機能**: 各リポジトリ内に存在する特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明（通常は3行）を自動的に抽出します。ネットワークリクエスト（ファイルの読み込み）のタイムアウト、リトライ、および取得結果のキャッシュ機能を提供し、効率的なデータ取得を実現します。
- **markdown_generator.py**:
    - **役割と機能**: 処理・整形されたリポジトリ情報を基に、GitHub Pagesサイトに表示するためのMarkdown形式のコンテンツを生成します。リポジトリ名、説明、リンク、生成されたバッジ、プロジェクト概要などを組み合わせて、SEOを意識した構造で出力します。
- **badge_generator.py**:
    - **役割と機能**: プログラミング言語、最終更新日、スター数、ライセンスなど、リポジトリの属性に基づいて、表示用のマークダウン形式のバッジを生成します。視覚的に情報を伝えることで、ユーザーがリポジトリの概要を素早く把握できるようにします。
- **config_manager.py**:
    - **役割と機能**: `config.yml`や`strings.yml`といった設定ファイルを読み込み、アプリケーション全体で利用可能な設定オブジェクトとして管理します。これにより、ハードコードされた値を避け、設定の変更を容易にします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-11-28 07:07:54 JST
