Last updated: 2025-12-27

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- GitHub Pages向けにSEO最適化されたリポジトリ一覧Markdownを生成するシステムです。
- 検索エンジンとLLMからのリポジトリ参照の可視性向上を目的としています。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレーターとして利用。本システムはJekyllが解釈するMarkdownを生成します)
- 音楽・オーディオ: 特になし
- 開発ツール:
    - **Python**: メインの開発言語として使用。GitHub APIとの連携やMarkdown生成ロジックを実装。
    - **GitHub API**: リポジトリ情報の取得に使用するWeb API。
    - **pip**: Pythonパッケージのインストールと管理に使用。
    - **TOML**: 設定ファイル（`secrets.toml`, `ruff.toml`, `pytest.ini`）の記述形式。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述形式。
- テスト:
    - **pytest**: Pythonコードのテストフレームワーク。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報の取得からMarkdown生成までの一連の処理を自動化し、最終的な`index.md`などの出力ファイルを「ビルド」します。
- 言語機能:
    - **Pythonの標準機能**: ファイルI/O、文字列処理、ネットワーク通信（HTTPリクエスト）などが活用されています。
- 自動化・CI/CD:
    - **ローカルスクリプト実行**: 明示的なCI/CDパイプラインは推奨されておらず、ローカルでのPythonスクリプト実行により自動化が図られています。
- 開発標準:
    - **ruff**: Pythonコードのリンティングおよびフォーマットツール。コード品質とスタイルの一貫性を保つために使用。
    - **.editorconfig**: 異なるエディタやIDE間でのコーディングスタイルを統一するための設定ファイル。

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
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）の一貫性を保つための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理システムが追跡しないファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、プロジェクト全体の概要を説明するメインドキュメントです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の構成と挙動を定義する設定ファイルです。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセット（画像ファイル）を格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるウェブサイトのアイコン画像ファイルです。
- **`debug_project_overview.py`**: `project_overview`機能のデバッグやテストに特化した補助スクリプトです。
- **`generated-docs/`**: 他のリポジトリから自動取得された`project-overview.md`などのドキュメントを一時的、あるいは永続的に格納する可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト所有権確認プロセスで使用される認証ファイルです。
- **`index.md`**: GitHub Pagesサイトのルートページとして表示されるMarkdownファイルで、このシステムによってリポジトリ一覧が生成され出力されます。
- **`issue-notes/`**: 開発中に発生した課題、検討事項、メモなどをMarkdown形式で整理して格納するディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリケーション名、アイコン、表示モードなどを定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルで、テストの挙動やオプションを定義します。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **`requirements.txt`**: 本番環境でこのシステムを実行するために必要となるPythonパッケージとそのバージョンを記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイトのどの部分をクロール・インデックスすべきか（またはすべきでないか）を指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンターおよびフォーマッターである`ruff`の設定ファイルで、コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonのパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成機能の中核を担うモジュール群が格納されています。
        - **`badge_generator.py`**: リポジトリのステータス（例: Active, Archived, Fork）に応じたバッジ画像を生成または管理するロジックを含みます。
        - **`config.yml`**: プロジェクト概要取得機能などの技術的なパラメータや設定値を定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml`や`secrets.toml`などの様々な設定ファイルを読み込み、プロジェクト内で利用可能な形式で管理するモジュールです。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプトで、GitHub APIからの情報取得、Markdown生成、ファイル出力までの一連の処理を統括します。
        - **`json_ld_template.json`**: SEO強化のために使用されるJSON-LD形式のテンプレートファイルで、構造化データとしてリポジトリ情報を記述します。
        - **`language_info.py`**: GitHubリポジトリの主要なプログラミング言語情報を取得し、表示用に整形するロジックを提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報に基づいて、SEOに最適化されたMarkdown形式のコンテンツ（リポジトリ一覧）を生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定ファイル（`generated-docs/project-overview.md`）から、そのリポジトリのプロジェクト概要を自動的に取得する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを処理し、表示に適した形式に変換する役割を担うモジュールです。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算または集計するモジュールです。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや各種文言を一元的に管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（例: Jinja2テンプレート）を処理し、データと結合して最終的な出力を生成するモジュールです。
        - **`url_utils.py`**: URLの生成、解析、正規化など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview`機能に特化した単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込みと管理に関するテストケースが含まれています。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストケースが含まれています。
    - **`test_integration.py`**: 複数のモジュールが連携して動作する際の統合テストケースが含まれています。
    - **`test_markdown_generator.py`**: `markdown_generator.py`モジュールの機能に関するテストケースが含まれています。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py`モジュールの機能に関するテストケースが含まれています。
    - **`test_repository_processor.py`**: `repository_processor.py`モジュールの機能に関するテストケースが含まれています。

## 関数詳細説明
プロジェクト情報から具体的な関数情報を検出できませんでした。主な機能は各ファイルの詳細説明をご参照ください。`src/generate_repo_list/generate_repo_list.py`がシステムのメイン実行スクリプトであり、その中でGitHub APIからのデータ取得、データの加工、Markdown生成といった一連の処理が関数として実装されていると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-12-27 07:06:11 JST
