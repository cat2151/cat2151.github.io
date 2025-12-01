Last updated: 2025-12-02

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・処理するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEOを考慮したMarkdown形式のリポジトリ一覧を生成します。
- 検索エンジンやLLMからのリポジトリ参照性を向上させ、情報発見と開発効率の改善を目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllによる静的サイト生成基盤), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: Python (主要なスクリプト言語), Git (バージョン管理), GitHub API (リポジトリ情報取得)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: 該当なし (Pythonスクリプトがコンテンツ生成を直接行うため、専用のビルドツールは使用していません)
- 言語機能: Python (汎用プログラミング言語、ファイルI/O、ネットワーク通信、データ処理機能)
- 自動化・CI/CD: 該当なし (現在のプロジェクトは主にローカルでの実行を想定しており、CI/CDパイプラインは明示されていません)
- 開発標準: Ruff (Pythonコードのリンターおよびフォーマッター)

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
- **`.editorconfig`**: 異なるエディタやIDE間でコードの整形ルール（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義します。ビルド生成物や一時ファイルなどが含まれます。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）を記述したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、使用方法など、全体的な情報を提供する主要なドキュメントファイルです。
- **`_config.yml`**: JekyllによってGitHub Pagesサイトを構築する際のグローバルな設定（サイトのタイトル、テーマなど）を定義するファイルです。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像ファイルなど）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）の様々なサイズを格納しています。
- **`debug_project_overview.py`**: プロジェクト概要自動取得機能の動作確認やデバッグを目的としたPythonスクリプトです。
- **`generated-docs/`**: 各リポジトリの `project-overview.md` ファイルが格納されることを想定したディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどの検索エンジンツールでウェブサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: メインスクリプトによって生成される、GitHub Pagesサイトのリポジトリ一覧ページとなるMarkdownファイルです。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録するためのMarkdown形式のファイル群が格納されています。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) のマニフェストファイルで、ウェブサイトをホーム画面に追加した際の表示情報や動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの動作に関する設定を記述するファイルです。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonパッケージの依存関係をリストしたファイルです。
- **`requirements.txt`**: プロジェクトが本番環境で実行される際に必要となるPythonパッケージの依存関係をリストしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいはクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのスタイルチェックとフォーマットを行うツールRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonパッケージの初期化ファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧を生成する機能の中核をなすPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list` パッケージの初期化ファイルです。
        - **`badge_generator.py`**: リポジトリのプロパティ（例：言語、ステータス）に基づいて表示用のバッジを生成するロジックを実装しています。
        - **`config.yml`**: プロジェクト概要の取得方法など、スクリプトの技術的な動作パラメータを設定するYAMLファイルです。
        - **`config_manager.py`**: `config.yml` や `strings.yml` といった設定ファイルを読み込み、管理するためのユーティリティ機能を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、整形して最終的なMarkdownファイルを生成する処理を統括します。
        - **`json_ld_template.json`**: 検索エンジン最適化(SEO)のために、ウェブページの内容を構造化データとして記述するJSON-LD形式のテンプレートです。
        - **`language_info.py`**: リポジトリのプログラミング言語に関する情報（主要言語、使用率など）を処理・解析する機能を提供します。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報を受け取り、指定されたフォーマットでMarkdownコンテンツを生成するロジックを実装しています。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に加工・整形する役割を担います。
        - **`seo_template.yml`**: 検索エンジン最適化(SEO)に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算し、レポートする機能を提供します。
        - **`strings.yml`**: UIメッセージ、見出し、説明文など、アプリケーション内で使用される各種文言を管理するYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に使用されるテキストテンプレートを読み込み、データに基づいてレンダリングする機能を提供します。
        - **`url_utils.py`**: GitHubリポジトリのURL構築や関連するURL操作を行うユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` のプロジェクト概要取得機能の単体テストを記述したスクリプトです。
- **`tests/`**: プロジェクト全体の各種テストスクリプトが格納されているディレクトリです。
    - **`test_config.py`**: 設定管理機能 (`config_manager.py`) のテストを行うスクリプトです。
    - **`test_environment.py`**: 実行環境に関する設定や依存関係のテストを行うスクリプトです。
    - **`test_integration.py`**: プロジェクトの複数のコンポーネントが連携して正しく動作するかを確認する統合テストスクリプトです。
    - **`test_markdown_generator.py`**: Markdown生成機能 (`markdown_generator.py`) のテストを行うスクリプトです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のテストを行うスクリプトです。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能 (`repository_processor.py`) のテストを行うスクリプトです。

## 関数詳細説明
- **`generate_repo_list.py` 内の関数**:
    - `main()`: スクリプトの主要な実行ロジックをカプセル化し、リポジトリ情報の取得、処理、Markdown生成の一連の流れをオーケストレーションします。引数解析やエラーハンドリングも担当します。
    - `parse_arguments()`: コマンドラインから渡される引数（ユーザー名、出力ファイル名、制限数など）を解析し、プログラムが使用できる形式に変換します。
- **`repository_processor.py` 内の関数**:
    - `fetch_repositories(username, limit=None)`: 指定されたGitHubユーザー名に基づき、GitHub API経由でリポジトリ一覧を取得します。必要に応じて取得数に制限を設けることができます。
    - `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要なキー情報（名前、説明、URL、言語など）を抽出し、整形されたデータ構造に変換します。
- **`markdown_generator.py` 内の関数**:
    - `generate_markdown(repo_list)`: 処理済みのリポジトリ情報のリストを受け取り、これらを整形して最終的なMarkdown形式の文字列を生成します。テンプレートエンジンや文字列操作を用いて、バッジやリンクを含むリポジトリ一覧を構築します。
- **`project_overview_fetcher.py` 内の関数**:
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLと設定情報に基づき、`generated-docs/project-overview.md` ファイルからプロジェクトの3行概要を抽出して返します。API呼び出しやファイル読み込みを伴う場合があります。
- **`config_manager.py` 内の関数**:
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、辞書としてその内容を返します。設定値のデフォルト処理やバリデーションを行うこともあります。
    - `load_strings(strings_path)`: 指定されたパスからYAML形式の文字列ファイルを読み込み、アプリケーションで使用する各種文言（例: 見出し、ラベル）を辞書として提供します。
- **`badge_generator.py` 内の関数**:
    - `generate_badges(repo_info)`: 個々のリポジトリ情報を受け取り、そのリポジトリに関連する視覚的なバッジ（例: 使用言語、アーカイブ状態を示すアイコン）のMarkdownまたはHTMLスニペットを生成します。
- **`language_info.py` 内の関数**:
    - `get_language_details(repo_info)`: リポジトリの言語に関する詳細情報（例: 主要なプログラミング言語、言語ごとのバイト数比率）を取得し、表示に適した形式に加工します。
- **`statistics_calculator.py` 内の関数**:
    - `calculate_repo_statistics(repo_info)`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を抽出し、計算して提供します。
- **`template_processor.py` 内の関数**:
    - `render_template(template_name, context)`: 指定されたテンプレートファイルとデータを組み合わせ、プレースホルダーを実際の値で置き換えて最終的な文字列（Markdownの一部など）を生成します。
- **`url_utils.py` 内の関数**:
    - `construct_repo_url(username, repo_name)`: 指定されたユーザー名とリポジトリ名から、GitHub上のリポジトリへの完全なURLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-02 07:05:59 JST
