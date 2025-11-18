Last updated: 2025-11-19

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してJekyll向けMarkdownファイルを生成します。
- GitHub Pagesサイトの検索エンジン最適化（SEO）を促進し、Web上の可視性を高めます。
- リポジトリの概要、バッジ、分類を表示し、ユーザーやLLMからの情報参照を容易にします。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤), Markdown (生成されるコンテンツ形式), HTML/CSS (Jekyllにより生成されるWebページの要素)
- 音楽・オーディオ: N/A
- 開発ツール: Python (スクリプト実行環境), GitHub API (リポジトリ情報取得元)
- テスト: pytest (Python向けテストフレームワーク)
- ビルドツール: N/A (PythonスクリプトがMarkdownを生成し、JekyllはGitHub Pages側でビルドを実行)
- 言語機能: Python (主要な開発言語)
- 自動化・CI/CD: N/A (ローカル開発重視であり、明示的なCI/CDは使用していません)
- 開発標準: Ruff (Pythonコードのスタイルチェックおよびフォーマッター)

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
- **.editorconfig**: 異なるエディタやIDE間でコードのインデントスタイル、文字コードなどの設定を統一するためのファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。一時ファイルやビルド成果物などが含まれます。
- **LICENSE**: プロジェクトのライセンス情報（本プロジェクトはMITライセンス）を記述したファイルです。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行方法、利用可能なオプション、ライセンス情報などを記述した主要なドキュメントファイルです。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグイン、パーマリンク構造などの設定が含まれます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - **favicon-*.png**: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
- **debug_project_overview.py**: プロジェクト概要取得機能のデバッグや単体テストを行うためのスクリプトです。
- **generated-docs/**: GitHubリポジトリの `generated-docs` ディレクトリを模倣しており、そこから各リポジトリのプロジェクト概要（`project-overview.md`）を読み取る際のテストやサンプルとして利用される可能性があります。
- **index.md**: 生成されたリポジトリ一覧のメインコンテンツとなるMarkdownファイルです。GitHub Pagesで表示されるリポジトリ一覧ページを構成します。
- **issue-notes/**: 開発中に発生した課題や検討事項、一時的なメモなどをMarkdown形式で記録するディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のWeb App Manifestファイルです。ホーム画面に追加された際の表示設定やアイコン情報などを定義します。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの実行方法やオプションなどを指定します。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonパッケージとそのバージョンを列挙したファイルです。
- **requirements.txt**: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンを列挙したファイルです。
- **robots.txt**: 検索エンジンクローラーに対して、どのページをクロールしてよいか、あるいは除外するかを指示するファイルです。
- **ruff.toml**: PythonのリンターおよびフォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成するための具体的なロジックを含むサブパッケージです。
        - **__init__.py**: `generate_repo_list` ディレクトリをPythonサブパッケージとして認識させるためのファイルです。
        - **badge_generator.py**: リポジトリの状態（例: アクティブ、アーカイブ、フォーク）に応じたバッジを生成するためのロジックを提供します。
        - **config.yml**: リポジトリ一覧生成スクリプトの技術的な動作パラメータ（例: プロジェクト概要取得設定、リトライ回数、タイムアウト）を定義する設定ファイルです。
        - **config_manager.py**: `config.yml` などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するためのモジュールです。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式で出力ファイルを生成する、このプロジェクトのメインとなる実行スクリプトです。
        - **json_ld_template.json**: 検索エンジン最適化（SEO）のために利用されるJSON-LD形式の構造化データテンプレートです。
        - **language_info.py**: GitHubリポジトリのプログラミング言語に関する情報を処理し、表示するためのロジックを提供します。
        - **markdown_generator.py**: 取得および処理されたリポジトリ情報から、Jekyllに適したMarkdownコンテンツを生成するためのモジュールです。
        - **project_overview_fetcher.py**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動的に抽出し取得するモジュールです。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、フィルタリングし、必要なメタデータを付加するなど、後続の処理に適した形式に変換するモジュールです。
        - **seo_template.yml**: 検索エンジン最適化（SEO）関連のメタデータや、Jekyllで利用するテンプレートに関する設定を記述したファイルです。
        - **statistics_calculator.py**: リポジトリ数やカテゴリごとの統計情報など、各種データを計算するためのモジュールです。
        - **strings.yml**: プロジェクト内で使用される表示メッセージ、文言、ローカライズ可能な文字列などを一元的に管理する設定ファイルです。
        - **template_processor.py**: Markdown生成の際に利用されるテンプレートを読み込み、データに基づいて動的にコンテンツを生成する処理を行うモジュールです。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連の共通ユーティリティ関数を集めたモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールに特化したテストコードを記述したファイルです。
- **tests/**: プロジェクト全体の自動テストコードを格納するディレクトリです。
    - **test_config.py**: 設定ファイルの読み込みや管理に関する機能のテストコードです。
    - **test_environment.py**: 実行環境のセットアップや依存関係のチェックなどに関するテストコードです。
    - **test_integration.py**: プロジェクトの複数のモジュールが連携して正しく動作するかを確認する統合テストコードです。
    - **test_markdown_generator.py**: `markdown_generator.py` モジュールによるMarkdown生成機能のテストコードです。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher.py` モジュールによるプロジェクト概要取得機能のテストコードです。
    - **test_repository_processor.py**: `repository_processor.py` モジュールによるリポジトリデータ処理機能のテストコードです。

## 関数詳細説明
プロジェクト情報に具体的な関数の詳細（関数名、引数、戻り値、具体的なロジック）が提供されていないため、詳細な説明は行えません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-19 07:06:08 JST
