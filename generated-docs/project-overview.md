Last updated: 2025-11-20

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHubユーザーページの検索エンジンでの見つけにくさという課題を解決します。
- GitHub APIから情報を取得し、SEOに最適化されたMarkdownファイルを自動で作成します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤とし、生成されたMarkdownファイルと組み合わせることで、静的なウェブサイトとしてリポジトリ一覧を表示します。来訪者はWebブラウザを通じて閲覧します。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連技術は使用されていません。
- 開発ツール:
    - pytest: Pythonで書かれたテストコードを実行するためのフレームワークです。
    - ruff: Pythonコードのスタイルと品質を自動的にチェック・修正する高速なリンターです。
    - Git: ソースコードのバージョン管理システムで、変更履歴を追跡し、複数人での開発を支援します。
    - GitHub API: GitHubのリポジトリ情報をプログラムから取得するために使用されます。
- テスト: pytest が主要なテストフレームワークとして利用されており、コードの品質と信頼性を保証します。
- ビルドツール: Pythonスクリプトが実質的なビルドツールとして機能し、GitHub APIから取得したデータを元にMarkdownファイルを生成します。
- 言語機能: Python が主要なプログラミング言語として使用されており、データの取得、処理、ファイル生成など、システムの核となるロジックを実装しています。
- 自動化・CI/CD: GitHub Actionsの利用が示唆されており、リポジトリ一覧の自動生成プロセスなどを自動化する可能性を秘めています。
- 開発標準: ruff を使用してPythonコードのスタイルを統一し、可読性と保守性を高めています。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定します。これにより、生成ファイルや一時ファイルなどがリポジトリに含まれないようにします。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示します。これにより、プロジェクトの利用、変更、配布に関する条件が明確になります。
- **`README.md`**: プロジェクトの概要、目的、主な機能、使い方、設定方法、開発者向けのヒントなどが記載された、プロジェクトの玄関となるドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の動作を制御する設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
- **`assets/`** ディレクトリ: ウェブサイトで使用されるファビコン（ブラウザのタブに表示されるアイコン）などの静的な画像ファイルを格納します。
- **`debug_project_overview.py`**: 各リポジトリの概要取得機能（`project-overview.md`からの情報抽出）をデバッグするための補助スクリプトです。
- **`generated-docs/`** ディレクトリ: このシステムによって自動生成されたドキュメントやデータが格納される場所です。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このファイルにリポジトリ一覧が自動生成されます。
- **`issue-notes/`** ディレクトリ: 開発中に検討された課題やその解決策、関連するメモなどをMarkdown形式で記録したファイル群です。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）としてサイトを機能させるための設定ファイルです。ホーム画面への追加やオフライン対応などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。テストの検出方法やプラグインなどが指定されます。
- **`requirements-dev.txt`**: 開発やテスト環境でのみ必要となるPythonライブラリの一覧です。
- **`requirements.txt`**: プロジェクトを実行する上で必要となるPythonライブラリの一覧です。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、または除外すべきかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行うツールRuffの設定ファイルです。コーディング規約の違反を検出し、修正を促します。
- **`src/`** ディレクトリ: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`generate_repo_list/`** ディレクトリ: リポジトリ一覧を生成するシステムの主要なロジックが含まれています。
        - **`badge_generator.py`**: GitHubリポジトリの言語やステータスに応じたバッジ（アイコン）を生成するロジックを扱います。
        - **`config.yml`**: プロジェクトの挙動を制御する技術的なパラメータ（例: プロジェクト概要取得機能の有効/無効、タイムアウト設定など）を定義する設定ファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体で設定値を利用できるように管理する役割を担います。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、その情報を元にMarkdown形式のリポジトリ一覧を生成する、このシステムのメイン実行スクリプトです。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を生成するためのテンプレートファイルです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つ形式に変換するロジックを提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報や設定に基づいて、最終的なMarkdown形式のコンテンツを生成するコアロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動的に抽出する役割を担います。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、このシステムで扱いやすい形に加工・整形する処理を行います。
        - **`seo_template.yml`**: サイト全体のSEO設定や、特定のページに適用するメタデータなどを定義するテンプレートファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数など、統計的な情報を計算・集計する機能を提供します。
        - **`strings.yml`**: プロジェクト内で使用される表示メッセージや文言（例: 見出し、説明文など）を管理するファイルです。これにより、文言の統一や将来的な多言語対応が容易になります。
        - **`template_processor.py`**: Jekyllなどの静的サイトジェネレータで使用されるテンプレートファイルを処理し、動的なコンテンツを埋め込むなどの機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証など、URLに関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py`で実装されたプロジェクト概要取得機能の正確性を検証するためのテストスクリプトです。
- **`tests/`** ディレクトリ: プロジェクトの各コンポーネントや機能の正しい動作を保証するためのテストコードが格納されています。
    - **`test_config.py`**: 設定ファイルの読み込みや管理に関するテストを行います。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストを行います。
    - **`test_integration.py`**: 複数のコンポーネントが連携して正しく動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックが期待通りに動作し、正しいMarkdown形式が出力されるかをテストします。
    - **`test_project_overview_fetcher.py`**: 各リポジトリからのプロジェクト概要抽出機能のテストを行います。
    - **`test_repository_processor.py`**: GitHubリポジトリ情報の処理と加工が正しく行われるかをテストします。

## 関数詳細説明
このプロジェクトでは、主要なPythonファイルが特定の役割を担っています。提供された情報からは具体的な関数名やその詳細な引数、戻り値を特定できませんが、各ファイルの役割に基づいて、どのような種類の関数が存在するかを以下に説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
    - 主に、GitHub APIからの情報取得、取得したデータの処理、最終的なMarkdownファイル生成までの一連のフローを制御する**メイン実行関数**が含まれていると想定されます。コマンドライン引数を解析し、他のモジュールの関数を呼び出す役割を持ちます。
- **`src/generate_repo_list/badge_generator.py`**:
    - リポジトリの特性（例：言語、アクティブ状態、アーカイブ状態）に基づいて、視覚的なバッジ（アイコン）を生成するための**バッジ生成関数**が含まれていると想定されます。これらの関数は、特定の情報を受け取り、Markdown形式のバッジ文字列を返すでしょう。
- **`src/generate_repo_list/config_manager.py`**:
    - `config.yml`などの設定ファイルを読み込み、その内容をプログラム内で利用可能な形式で提供するための**設定読み込み関数**や**設定値取得関数**が含まれていると想定されます。
- **`src/generate_repo_list/markdown_generator.py`**:
    - 取得および処理されたリポジトリ情報を受け取り、それを構造化されたMarkdownテキストに変換するための**Markdown生成関数**が含まれていると想定されます。例えば、各リポジトリのセクションや全体のリポジトリ一覧を生成する関数などです。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
    - 各GitHubリポジトリ内の特定のパス（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出するための**概要取得関数**や**ファイル内容解析関数**が含まれていると想定されます。GitHub APIを通じてファイルのコンテンツを取得する処理も担うでしょう。
- **`src/generate_repo_list/repository_processor.py`**:
    - GitHub APIから受け取ったリポジトリの生データを、このシステムで扱いやすいようにフィルター、ソート、追加情報の付与などを行う**リポジトリ情報処理関数**が含まれていると想定されます。
- **`src/generate_repo_list/statistics_calculator.py`**:
    - リポジトリのスター数やフォーク数、最終更新日などの統計情報を計算したり、集計したりするための**統計計算関数**が含まれていると想定されます。
- **`src/generate_repo_list/template_processor.py`**:
    - Jekyllなどの静的サイトジェネレータのテンプレートを処理し、動的にコンテンツを埋め込むための**テンプレート処理関数**が含まれていると想定されます。
- **`src/generate_repo_list/url_utils.py`**:
    - URLの構築、検証、エンコード・デコードなど、URL操作に関する一般的なユーティリティ機能を提供する**URL操作関数**が含まれていると想定されます。

各関数は、それぞれのファイルが担う主要な機能を実現するために設計されており、引数として必要なデータを受け取り、処理結果を戻り値として提供することで連携します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-11-20 07:06:14 JST
