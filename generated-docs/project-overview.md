Last updated: 2025-12-09

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、リポジトリ情報を自動で取得・整理するシステムです。
- ユーザーのGitHub Pagesサイト向けに、検索エンジン最適化されたリポジトリ一覧Markdownファイルを生成します。
- これにより、プロジェクトの公開性とLLMからの参照性を向上させ、開発効率を高めることを目指します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesで利用される静的サイトジェネレータです。本プロジェクトが生成するMarkdownファイルをサイトとして構築する基盤となります。
    - GitHub Pages: 生成されたMarkdownコンテンツを公開するためのウェブホスティングサービスです。
    - Markdown: リポジトリ一覧ページの内容を記述するための軽量マークアップ言語です。本プロジェクトはMarkdown形式のファイルを生成します。
- 音楽・オーディオ: なし
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語です。GitHub APIとの連携、データ処理、Markdown生成の全てを担います。
    - GitHub API: GitHubのリポジトリ情報をプログラム的に取得するためのインターフェースです。
    - pytest: Pythonコードの単体テストおよび結合テストを実行するためのフレームワークです。
    - ruff: Pythonコードのスタイルチェック（リンター）と自動整形（フォーマッター）を行うツールです。
- テスト:
    - pytest: プロジェクトの品質を保証するための自動テスト実行ツールとして採用されています。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py` がコアスクリプトとして機能し、GitHub APIからのデータ取得、加工、そして最終的なMarkdownファイルの生成という一連の「ビルド」プロセスを実行します。
- 言語機能:
    - Python: プロジェクト全体で使用される主要なプログラミング言語です。
- 自動化・CI/CD:
    - なし: このプロジェクト自体はローカル開発とテストを重視しており、継続的インテグレーション/継続的デリバリー（CI/CD）パイプラインは現状では採用していません。
- 開発標準:
    - ruff: Pythonコードの品質と一貫性を保つため、自動的なコードスタイルチェックとフォーマットに利用されています。

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
-   **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
-   **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。一時ファイルや生成物などが含まれます。
-   **`LICENSE`**: プロジェクトのライセンス情報（この場合はMITライセンス）が記述されています。プロジェクトの利用条件を定めます。
-   **`README.md`**: プロジェクトの概要、目的、使い方、設定方法などが記述された中心的なドキュメントファイルです。
-   **`_config.yml`**: Jekyllサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグインなどが含まれます。
-   **`assets/`**: ウェブサイトで使用される静的なアセット（画像、ファビコンなど）を格納するディレクトリです。
    -   **`favicon-*.png`**: ウェブサイトのアイコン（ファビコン）ファイル群です。ブラウザのタブやブックマークに表示されます。
-   **`debug_project_overview.py`**: `project_overview`機能のデバッグや単体テストを目的としたスクリプトです。
-   **`generated-docs/`**: 各リポジトリのプロジェクト概要ファイル (`project-overview.md`) が配置されることを想定したディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブマスターツールで、サイトの所有権を確認するために使用される検証ファイルです。
-   **`index.md`**: メインの出力ファイルであり、GitHub Pagesサイトでリポジトリ一覧として公開される最終的なMarkdownファイルです。
-   **`issue-notes/`**: プロジェクト開発中の課題や検討事項に関するメモがMarkdown形式で格納されているディレクトリです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルです。ウェブサイトをアプリのようにインストール可能にするための情報（アプリ名、アイコン、起動URLなど）を記述します。
-   **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出方法やプラグイン設定などを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **`requirements.txt`**: プロジェクトの実行（本番環境）に必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、あるいはクロールしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: Pythonのリンター兼フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の振る舞いを定義します。
-   **`src/__init__.py`**: Pythonパッケージを示すための空のファイルです。ディレクトリがPythonパッケージとして扱われることを示します。
-   **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（例：アクティブ、アーカイブ）や言語に応じたバッジ画像を生成またはリンクを生成するロジックを管理するファイルです。
-   **`src/generate_repo_list/config.yml`**: プロジェクト固有の設定（例：プロジェクト概要取得機能の有効/無効、対象ファイル名、タイムアウト時間など）を定義するファイルです。
-   **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体で設定値にアクセスするための機能を提供するファイルです。
-   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトの主要な実行スクリプトです。GitHub APIからリポジトリ情報を取得し、各処理モジュールを呼び出して最終的なMarkdownファイルを生成します。
-   **`src/generate_repo_list/json_ld_template.json`**: SEOを強化するためのJSON-LD形式の構造化データテンプレートです。検索エンジンにリポジトリ情報をより正確に伝えるために利用されます。
-   **`src/generate_repo_list/language_info.py`**: GitHubリポジトリで使用されているプログラミング言語に関する情報を処理・解析するためのロジックを提供するファイルです。
-   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、Markdown形式のリポジトリ一覧コンテンツを生成するロジックをカプセル化したファイルです。
-   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の `generated-docs/project-overview.md` ファイルから、指定された形式でプロジェクト概要の3行説明を抽出し取得する機能を提供するファイルです。
-   **`src/generate_repo_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示用に整形・フィルタリング・追加情報付与などの処理を行うファイルです。
-   **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化データを生成するためのテンプレート設定ファイルです。
-   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するためのロジックを提供するファイルです。
-   **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを外部化し、一元管理するためのファイルです。多言語対応などにも応用可能です。
-   **`src/generate_repo_list/template_processor.py`**: Markdown生成時に、定義されたテンプレートに変数を埋め込むなどの処理を行う汎用的なテンプレート処理ロジックを提供するファイルです。
-   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関するユーティリティ機能を提供するファイルです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の動作を検証するためのテストスクリプトです。
-   **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   **`test_config.py`**: 設定ファイルの読み込みや管理機能に関するテストです。
    -   **`test_environment.py`**: 実行環境の依存関係や設定に関するテストです。
    -   **`test_integration.py`**: 複数のモジュールが連携して動作する際の統合的なテストです。
    -   **`test_markdown_generator.py`**: Markdown生成ロジックが正しく動作するかを検証するテストです。
    -   **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    -   **`test_repository_processor.py`**: リポジトリ情報処理ロジックのテストです。

## 関数詳細説明
提供された情報からは、各関数の具体的な引数や戻り値の詳細は不明です。しかし、ファイル名とその役割から、主要な機能を提供する関数が推測されます。

-   **`src/generate_repo_list/generate_repo_list.py` 内の主要関数**:
    -   **`main()`**:
        -   **役割**: プログラムのエントリポイントであり、全体の処理フローを制御します。
        -   **機能**: コマンドライン引数の解析、GitHubトークンの読み込み、リポジトリ情報の取得、各処理モジュール（リポジトリ処理、概要取得、Markdown生成など）の呼び出し、そして最終的なMarkdownファイルの出力までの一連の流れをオーケストレートします。
-   **`src/generate_repo_list/badge_generator.py` 内の関数**:
    -   **`generate_badge(...)` (仮称)**:
        -   **役割**: リポジトリの属性（言語、ステータスなど）に基づいたバッジ情報を生成します。
        -   **機能**: 入力されたリポジトリ情報から適切なバッジの種類と表示テキストを決定し、Markdown形式でのバッジ表示文字列やURLを返します。
-   **`src/generate_repo_list/config_manager.py` 内の関数**:
    -   **`load_config(...)` (仮称)**:
        -   **役割**: `config.yml` などの設定ファイルを読み込み、プログラム全体で利用可能な形式で提供します。
        -   **機能**: YAMLファイルを解析し、設定値をディクショナリやオブジェクトとして返します。設定値のバリデーションやデフォルト値の適用も行う可能性があります。
-   **`src/generate_repo_list/markdown_generator.py` 内の関数**:
    -   **`generate_markdown_content(...)` (仮称)**:
        -   **役割**: 処理済みのリポジトリデータとテンプレートを使用して、最終的なMarkdownコンテンツを生成します。
        -   **機能**: 各リポジトリ情報とプロジェクト概要を整形し、バッジやリンクなどを含んだMarkdown形式の文字列を構築します。
-   **`src/generate_repo_list/project_overview_fetcher.py` 内の関数**:
    -   **`fetch_project_overview(...)` (仮称)**:
        -   **役割**: 指定されたリポジトリの `generated-docs/project-overview.md` からプロジェクト概要の3行説明を抽出します。
        -   **機能**: GitHub APIを介して対象ファイルを読み込み、正規表現などを用いて「プロジェクト概要」セクションから指定された行数を抽出し、テキストとして返します。キャッシュ機能も含む可能性があります。
-   **`src/generate_repo_list/repository_processor.py` 内の関数**:
    -   **`process_repositories(...)` (仮称)**:
        -   **役割**: GitHub APIから取得した複数のリポジトリデータに対して、一連の処理（フィルタリング、ソート、追加情報の付与など）を適用します。
        -   **機能**: アーカイブされたリポジトリの除外、フォークされたリポジトリの識別、プロジェクト概要のフェッチ、統計情報の計算などを行い、整形されたリポジトリデータのリストを返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-09 07:06:17 JST
