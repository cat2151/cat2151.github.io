Last updated: 2026-01-17

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト（`cat2151.github.io`）用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyllに対応したSEO最適化済みMarkdownファイルを生成します。
- これにより、リポジトリの検索エンジンからの参照性を高め、LLMによる情報参照の精度向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的コンテンツ生成), Markdown (コンテンツ記述), HTML/CSS (Jekyllが生成するウェブページの基盤)
- 音楽・オーディオ: 特になし
- 開発ツール: Python (主要開発言語), Git (バージョン管理)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Pythonスクリプト自体がMarkdownファイルを生成するビルドプロセスを担います。
- 言語機能: Python (GitHub APIとの連携、ファイル操作、文字列処理など)
- 自動化・CI/CD: (明示的なCI/CDは「不要」とされているが、GitHub PagesのデプロイにはGitHub Actionsなどが利用される可能性があります。)
- 開発標準: ruff (Pythonコードのフォーマットとリンティングを自動化し、コードスタイルを統一)

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  18.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    readme_badge_extractor.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_badge_generator_integration.py
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_readme_badge_extractor.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: エディタのコードスタイル設定を定義し、異なる開発環境間での一貫性を保ちます。
- **`.gitignore`**: Gitでバージョン管理しないファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述しています。
- **`README.md`**: プロジェクトの概要、設定方法、実行コマンド、開発者向けのヒントなどを記述したメインドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどを定義します。
- **`assets/`**: Jekyllサイトで使用される静的ファイル（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン画像ファイル群です。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ用途で使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した `project-overview.md` ファイルが一時的に保存される可能性があるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認用のファイルです。
- **`index.md`**: メインスクリプトによってGitHubリポジトリ一覧が自動生成される出力先ファイルです。Jekyllによってウェブページとして表示されます。
- **`issue-notes/`**: 開発中の課題やメモがMarkdown形式で記録されているディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のメタデータ定義ファイルで、ウェブアプリの見た目や動作を制御します。
- **`pytest.ini`**: pytestテストフレームワークの設定ファイルです。テスト実行オプションなどを定義します。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonライブラリの依存関係リストです。
- **`requirements.txt`**: 本番環境で実行する際に必要なPythonライブラリの依存関係リストです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、どの部分を避けるべきかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードフォーマッター兼リンターであるRuffの設定ファイルです。
- **`src/__init__.py`**: Pythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示す空ファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やスター数などの情報を元にバッジを生成する機能を提供します。
- **`src/generate_repo_list/config.yml`**: プロジェクト固有の設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルパスなど）を定義するファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml` や他の設定ファイルを読み込み、管理する機能を提供します。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトです。GitHub APIからのリポジトリ情報取得、処理、最終的なMarkdownファイルの生成を全体的にオーケストレートします。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためのJSON-LD形式の構造化データテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの言語情報（使用割合など）を処理し、表示に適した形式に変換する機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリ情報から、Jekyllに適したMarkdownコンテンツを生成する主要なロジックを含みます。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動で取得する機能を提供します。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に必要な形に加工する処理を担います。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやコンテンツのテンプレートを定義するファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリの星の数、フォーク数、最終更新日などの統計情報を計算する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理するファイルです。多言語対応や文言変更を容易にします。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートの読み込みや変数置換などの処理を行います。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URLに関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能の単体テストを記述したファイルです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_*.py`**: 各モジュールのテストファイル群です。

## 関数詳細説明
現時点での情報から、Pythonスクリプト内の主要な役割を持つ関数を説明します。具体的な引数や戻り値のシグネチャは提供されていないため、機能と目的を中心に記述します。

- **`generate_repo_list.py` の `main()` 関数 (またはエントリポイント)**:
    - **役割**: プロジェクト全体の実行フローを制御するメイン関数。
    - **機能**: コマンドライン引数を解析し、GitHub APIからリポジトリ情報を取得し、取得したデータを処理して、最終的にMarkdownファイルを生成する一連のプロセスをオーケストレートします。
- **`markdown_generator.py` 内の `generate_markdown_content()` 関数 (想定)**:
    - **役割**: 処理されたリポジトリ情報に基づき、整形されたMarkdown文字列を生成します。
    - **機能**: 各リポジトリのタイトル、説明、バッジ、リンク、概要などを組み合わせて、Jekyllで正しく表示される形式のMarkdownコンテンツを作成します。
- **`project_overview_fetcher.py` 内の `fetch_project_overview()` 関数 (想定)**:
    - **役割**: 特定のリポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出します。
    - **引数**: リポジトリのGitHub URL、ターゲットファイルパスなど。
    - **戻り値**: 抽出された3行のプロジェクト概要（文字列リストまたは単一文字列）。
    - **機能**: GitHub APIまたは直接のファイルアクセスを通じて指定されたコンテンツを取得し、Markdownパースロジックを用いて「プロジェクト概要」セクションから指定された行数を抽出します。
- **`repository_processor.py` 内の `process_repositories()` 関数 (想定)**:
    - **役割**: GitHub APIから取得した生のリポジトリデータの前処理と整形を行います。
    - **引数**: GitHub APIから取得したリポジトリデータのリスト。
    - **戻り値**: 処理され、整形されたリポジトリ情報のリスト。
    - **機能**: リポジトリの公開/非公開状態、フォーク、アーカイブ状況に基づいてフィルタリングし、必要な情報（名前、説明、URL、言語、更新日など）を抽出し、Markdown生成に適した形式に変換します。
- **`badge_generator.py` 内の `create_language_badge()` や `create_star_badge()` 関数 (想定)**:
    - **役割**: リポジトリの属性（例: 主要言語、スター数）に対応するマークダウン形式のバッジ文字列を生成します。
    - **引数**: 言語名、スター数など。
    - **戻り値**: バッジとして表示されるMarkdown文字列。
    - **機能**: 入力された情報に基づいて、視覚的に分かりやすいバッジのMarkdown表現を組み立てます。
- **`config_manager.py` 内の `load_config()` 関数 (想定)**:
    - **役割**: 設定ファイル (`config.yml` や `strings.yml`) を読み込み、アプリケーション全体で利用可能な設定オブジェクトを提供します。
    - **機能**: YAMLファイルをパースし、設定値をプログラムからアクセスしやすいデータ構造で返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-17 07:06:51 JST
