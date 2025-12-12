Last updated: 2025-12-13

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得・整理します。
- JekyllベースのGitHub Pages向けに、SEOを考慮したリポジトリ一覧を自動生成します。
- これにより、リポジトリの検索エンジン視認性を高め、LLMによる参照失敗の緩和を目指します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの基盤として動作し、MarkdownファイルをHTMLに変換します), **Markdown** (リポジトリ一覧のコンテンツ形式として生成されます)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (プロジェクトの主要なスクリプト言語です), **YAML** (設定ファイルや文字列管理に使用されます), **TOML** (PytestやRuffの設定ファイルに使用されます), **JSON** (SEO用の構造化データテンプレートに使用されます)
- テスト: **Pytest** (Pythonコードの単体テストおよび統合テストフレームワークです)
- ビルドツール: **Pythonスクリプト** (リポジトリ情報を基にMarkdownファイルを自動生成する実質的なビルドプロセスを実行します)
- 言語機能: **Python** (ファイル操作、ネットワーク通信、文字列処理、データ構造操作などの豊富な標準機能が活用されています)
- 自動化・CI/CD: **GitHub API** (リポジトリ情報の自動取得のためにGitHubサービスと連携します), **Pythonスクリプト** (リポジトリ一覧の生成プロセスを自動化します)
- 開発標準: **Ruff** (Pythonコードの品質を保つためのリンティングおよびフォーマットツールです)

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
- **`.editorconfig`**: 複数のエディタやIDE間でコードスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定方法、開発者向けのヒントなどを記述した、プロジェクトの主要な説明文書です。
- **`_config.yml`**: Jekyllサイト全体の共通設定を定義するファイルで、GitHub Pagesの動作に影響を与えます。
- **`assets/`**: ウェブサイトで利用される静的アセット（画像、アイコンなど）を格納するディレクトリです。
  - **`favicon-*.png`**: ウェブサイトのファビコンとして利用される、様々なサイズのアイコン画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher`モジュールからプロジェクト概要を取得する機能をデバッグするための補助スクリプトです。
- **`generated-docs/`**: 生成されたドキュメントやレポート、またはキャッシュされたデータなどが格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでウェブサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして表示されるMarkdownファイルで、このシステムによって自動生成されたリポジトリ一覧が出力されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項をMarkdown形式で記録したメモファイル群を格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加情報や表示設定などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークである`pytest`の動作設定を定義するファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`requirements.txt`**: このプロジェクトのスクリプトを実行するために最低限必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてよいか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびフォーマッターである`ruff`のコードスタイル設定を定義するファイルです。
- **`src/`**: プロジェクトの主要なソースコードが配置されているディレクトリです。
  - **`__init__.py`**: Pythonパッケージを定義する際に必要となるファイルです。
  - **`src/generate_repo_list/`**: リポジトリ一覧を生成するための具体的なロジックがモジュールとして格納されているPythonパッケージです。
    - **`__init__.py`**: `generate_repo_list`パッケージの初期化ファイルです。
    - **`badge_generator.py`**: リポジトリの状態（例：アーカイブ、フォーク）に応じた視覚的なバッジのHTMLまたはMarkdownスニペットを生成するロジックを提供します。
    - **`config.yml`**: プロジェクト概要の取得設定やAPIリトライ回数など、システム動作に関する技術的パラメータを定義する設定ファイルです。
    - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム全体で利用可能な形式で管理するモジュールです。
    - **`generate_repo_list.py`**: プロジェクトのメインエントリスクリプトで、GitHub APIからのデータ取得からMarkdownファイルの生成まで、一連の処理全体を制御します。
    - **`json_ld_template.json`**: 検索エンジンの最適化（SEO）を強化するために、構造化データとして使用されるJSON-LD形式のテンプレートファイルです。
    - **`language_info.py`**: 各リポジトリのプログラミング言語情報を処理し、表示に適した形式に整形するための機能を提供します。
    - **`markdown_generator.py`**: 処理済みのリポジトリデータを受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成するロジックを担うモジュールです。
    - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出し取得するモジュールです。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリJSONデータを、Markdown生成に適した内部データ構造に変換・整形するモジュールです。
    - **`seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータや構造化コンテンツのテンプレートを定義するファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算・処理し、表示可能な形式に変換するモジュールです。
    - **`strings.yml`**: 生成されるMarkdown内の各種表示メッセージや文言（例: ヘッダー、フッター、分類ラベル）を一元的に管理する設定ファイルです。
    - **`template_processor.py`**: Markdown生成に使用するテンプレートファイルの読み込みと、プレースホルダーを実際のデータで置換する機能を提供します。
    - **`url_utils.py`**: リポジトリのGitHub URL、GitHub Pages URL、プロジェクト概要ファイルへのURLなど、さまざまなURLの生成や整形を行うユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体の自動テストコードを格納するディレクトリです。
  - **`test_config.py`**: 設定ファイルの読み込みやパース処理の正確性を検証するテストです。
  - **`test_environment.py`**: 実行環境のセットアップや外部依存関係が適切に構成されているかを検証するテストです。
  - **`test_integration.py`**: 複数のモジュール間の連携やGitHub APIとの統合が正しく機能するかを検証するテストです。
  - **`test_markdown_generator.py`**: Markdown生成ロジックが期待通りの出力を生成するかを検証するテストです。
  - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールがプロジェクト概要を正しく抽出できるかを検証するテストです。
  - **`test_repository_processor.py`**: リポジトリデータ処理ロジックがGitHub APIの生データを正確に変換・整形できるかを検証するテストです。

## 関数詳細説明
- **`badge_generator.py` モジュール内の関数**:
    - **役割**: リポジトリのステータス（例: アーカイブ、フォーク）に基づいて、適切なバッジのマークダウンまたはHTMLスニペットを生成します。
    - **機能**: リポジトリのプロパティを分析し、対応するバッジのテキストやスタイルを決定して出力します。
- **`config_manager.py` モジュール内の関数**:
    - **役割**: プロジェクトで使用されるYAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、構造化されたデータとしてアクセス可能にします。
    - **機能**: 指定されたパスからYAMLファイルをパースし、設定値の取得、更新などのインターフェースを提供します。
- **`generate_repo_list.py` モジュール内の関数**:
    - **役割**: GitHub APIからのリポジトリ情報取得、データの前処理、Markdownコンテンツの生成という一連の主要なワークフローを管理・実行します。
    - **機能**: コマンドライン引数（ユーザー名、出力ファイル、リポジトリ制限など）を解析し、他のモジュール（`repository_processor`, `markdown_generator`など）を協調させて最終的なMarkdownファイルを生成します。
- **`language_info.py` モジュール内の関数**:
    - **役割**: GitHubリポジトリから取得したプログラミング言語の利用状況を処理し、主要な言語やその表示形式を決定します。
    - **機能**: リポジトリに複数の言語が使われている場合に最も使用されている言語を特定したり、言語ごとの表示形式を調整したりします。
- **`markdown_generator.py` モジュール内の関数**:
    - **役割**: 処理済みリポジトリデータを受け取り、Jekyllの要件を満たす最終的なリポジトリ一覧のMarkdownコンテンツを構築します。
    - **機能**: テンプレートとリポジトリの詳細情報（名前、説明、言語、スター数、リンク、プロジェクト概要など）を組み合わせて、整形されたMarkdown文字列を生成し、出力ファイルに書き込みます。
- **`project_overview_fetcher.py` モジュール内の関数**:
    - **役割**: 各リポジトリ内の特定のMarkdownファイル（例: `generated-docs/project-overview.md`）から、「プロジェクト概要」セクションの3行要約を自動で取得します。
    - **機能**: GitHub APIを通じて対象ファイルのコンテンツをフェッチし、正規表現やテキスト解析を用いて指定されたセクションから説明文を抽出します。APIリクエストのキャッシュ、リトライ、タイムアウト処理もサポートします。
- **`repository_processor.py` モジュール内の関数**:
    - **役割**: GitHub APIから取得した生のリポジトリJSONデータに対し、必要な情報のフィルタリング、整形、標準化を行い、次のステップ（Markdown生成）で利用しやすい形式に変換します。
    - **機能**: 特定の条件（フォーク済み、アーカイブ済みなど）でのリポジトリ除外、日付フォーマットの変換、必要なメタデータの抽出などを行います。
- **`statistics_calculator.py` モジュール内の関数**:
    - **役割**: リポジトリのスター数やフォーク数といった統計情報を計算・集計し、表示に適した形式に処理します。
    - **機能**: 生のAPIデータから数値データを取り出し、ソートや集計、表示形式の調整などを行います。
- **`template_processor.py` モジュール内の関数**:
    - **役割**: Markdown生成に使用されるテンプレートファイル（例: ヘッダー、フッター、リポジトリごとのエントリの雛形）を読み込み、プレースホルダーを実際のデータで置き換える処理を実行します。
    - **機能**: テンプレート文字列と、そこに埋め込む変数を含むデータ辞書を受け取り、レンダリングされた最終的な文字列を返します。
- **`url_utils.py` モジュール内の関数**:
    - **役割**: GitHubリポジトリのURL、GitHub PagesサイトのURL、特定のファイルへのURLなど、プロジェクト内で使用される様々なURLを生成および整形するためのユーティリティ機能を提供します。
    - **機能**: ベースURLやリポジトリ名などの情報に基づいて、完全なURLパスを構築します。

## 関数呼び出し階層ツリー
```
```

---
Generated at: 2025-12-13 07:06:23 JST
