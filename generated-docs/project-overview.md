Last updated: 2026-08-16

# Project Overview

## プロジェクト概要
- GitHub APIを用いてリポジトリ情報を自動取得し、GitHub Pages向けに一覧を生成するシステムです。
- 検索エンジンのクロールを促進し、リポジトリの可視性を高めるSEO最適化されたMarkdownを出力します。
- 各リポジトリの概要やバッジを自動表示し、Jekyllサイトの運用を効率化します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として利用され、生成されたMarkdownをレンダリングします。), Markdown (自動生成されるコンテンツの形式です。)
- 音楽・オーディオ: (該当する技術情報はありません。)
- 開発ツール: Python (プロジェクトの主要なスクリプト言語です。), Git (バージョン管理システムとして利用されます。), GitHub (リポジトリホスティングとAPIの利用元です。), ruff (Pythonコードの品質と一貫性を保つためのリンターおよびフォーマッターです。), pytest (Python向けテストフレームワークです。)
- テスト: pytest (Pythonアプリケーションの単体テスト、統合テスト、機能テストを行うためのフレームワークです。)
- ビルドツール: Markdown生成スクリプト (Pythonスクリプト自体がGitHubリポジトリ情報からMarkdownファイルを「ビルド」し、静的サイトのコンテンツを生成します。), Jekyll (GitHub Pagesで利用される静的サイトジェネレーターで、生成されたMarkdownファイル群から最終的なウェブサイトを構築します。)
- 言語機能: Python 3.x (プロジェクトの主要なプログラミング言語として使用されています。)
- 自動化・CI/CD: GitHub Actions (`.github_automation`ディレクトリが存在し、将来的なCI/CDや自動化タスクの基盤として機能する可能性があります。ただし、現時点ではローカル開発を重視しています。)
- 開発標準: ruff (Pythonコードのスタイルチェックとフォーマットを自動化し、コード品質と一貫性を保ちます。), .editorconfig (異なるエディタやIDE間でインデントスタイルなどのコーディング設定を統一するためのファイルです。)

## ファイル階層ツリー
```
.editorconfig
.github_automation/
  check_large_files/
    README.md
    check-large-files.toml
    scripts/
      check_large_files.py
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
  22.md
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
  conftest.py
  test_badge_generator_integration.py
  test_check_large_files.py
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
- **.editorconfig**: 異なるエディタやIDE間でインデントスタイル、文字コード、改行コードなど、基本的なコーディングスタイルを一貫させるための設定ファイルです。
- **.github_automation/**: GitHub Actionsワークフローやその他の自動化スクリプトを格納するためのディレクトリです。
  - **check_large_files/**: プロジェクト内の大容量ファイルをチェックするための機能群を格納するディレクトリです。
    - **README.md**: `check_large_files`機能に関する説明や使用方法が記述されています。
    - **check-large-files.toml**: 大容量ファイルチェックのルールや閾値などを設定するためのTOML形式のファイルです。
    - **scripts/check_large_files.py**: プロジェクト内で指定されたサイズを超えるファイルを検出し、報告するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。
- **LICENSE**: プロジェクトのライセンス情報が記述されています（MITライセンス）。
- **README.md**: プロジェクトの概要、目的、主な機能、開発者向けのヒント、クイックテストの実行方法、設定ファイルの説明、実際のコマンド例、ライセンス情報など、プロジェクト全体に関する包括的な情報が記述されたメインドキュメントです。
- **_config.yml**: Jekyllサイトの設定ファイルです。GitHub Pagesのビルド挙動やサイト全体のメタデータ（タイトル、説明など）を定義します。
- **assets/**: ウェブサイトで使用される静的なアセット（画像、アイコンなど）を格納するディレクトリです。
  - **favicon-16x16.png, favicon-192x192.png, favicon-32x32.png, favicon-512x512.png**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）として使用される各種サイズの画像ファイルです。
- **debug_project_overview.py**: `project_overview`機能の動作検証やデバッグを目的とした、独立したPythonスクリプトです。
- **generated-docs/**: 他のリポジトリから自動的に取得されたドキュメント（例: `project-overview.md`）などを一時的または永続的に保存するためのディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleによるサイトの所有権確認に使用されるHTMLファイルです。
- **index.md**: GitHub PagesサイトのトップページとなるMarkdownファイルです。このプロジェクトのスクリプトによってリポジトリ一覧がここに自動生成されます。
- **issue-notes/**: プロジェクトの課題や検討事項に関するメモを格納するためのディレクトリです。
  - **22.md**: 特定の課題（例: GitHub Issue #22）に関する詳細なメモや議論、解決策などを記述したMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）のメタデータを提供するファイルです。ウェブサイトをホーム画面に追加する際のアイコン、表示名、表示モードなどを定義します。
- **pytest.ini**: `pytest`テストフレームワークの共通設定を定義するファイルです。テストの発見ルール、オプション、プラグインなどを指定できます。
- **requirements-dev.txt**: 開発環境およびテスト実行時に必要となるPythonパッケージの依存関係を記述したファイルです。
- **requirements.txt**: プロジェクトの実行環境（本番環境など）で必要となる最小限のPythonパッケージの依存関係を記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてもよいか、またはしてはいけないかを指示するファイルです。
- **ruff.toml**: `ruff`リンターおよびフォーマッターの設定ファイルです。コードの整形ルールやチェック対象の指定などを定義します。
- **src/**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
  - **__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
  - **generate_repo_list/**: リポジトリ一覧自動生成システムの主要なロジックが格納されたPythonパッケージです。
    - **__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
    - **badge_generator.py**: リポジトリに関連するバッジ（例: ビルドステータス、ライセンスなど）を生成または処理する機能を提供します。
    - **config.yml**: プロジェクト概要取得機能などの技術的なパラメータや設定値をYAML形式で定義するファイルです。
    - **config_manager.py**: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、プロジェクト全体で利用可能な形で管理する機能を提供します。
    - **date_formatter.py**: 日付や時刻の情報を指定された形式にフォーマットするためのユーティリティ関数を提供します。
    - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、取得したデータに基づいて最終的なMarkdownファイルを生成する、プロジェクトのメインスクリプトです。
    - **json_ld_template.json**: SEO最適化のために、ウェブページに構造化データを埋め込むためのJSON-LD形式のテンプレートを定義します。
    - **language_info.py**: リポジトリの使用言語に関する情報を取得・処理する機能を提供します。
    - **markdown_generator.py**: 処理されたリポジトリ情報から、最終的なMarkdownコンテンツ（リポジトリ一覧など）を組み立てる機能を提供します。
    - **project_overview_fetcher.py**: 他のリポジトリの`generated-docs/project-overview.md`ファイルから、プロジェクトの3行概要を抽出・取得する機能を提供します。
    - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報（URLやaltテキストなど）を抽出する機能を提供します。
    - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出し、整形するための機能を提供します。
    - **seo_template.yml**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するYAMLファイルです。
    - **statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算する機能を提供します。
    - **strings.yml**: UIメッセージや表示されるテキスト、文言などを一元的に管理するためのYAMLファイルです。国際化（i18n）の基盤となります。
    - **template_processor.py**: Markdown生成に使用されるテンプレートファイル（JekyllのLiquidなど）を処理し、データと結合して最終コンテンツを生成する機能を提供します。
    - **url_utils.py**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`に関連する単体テストや機能テストを記述したファイルです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
  - **conftest.py**: `pytest`のテスト実行時に共有されるフィクスチャやヘルパー関数を定義するファイルです。
  - **test_badge_generator_integration.py**: バッジ生成機能の複数のコンポーネントを組み合わせた統合テストを記述しています。
  - **test_check_large_files.py**: 大容量ファイルチェック機能（`.github_automation/check_large_files/scripts/check_large_files.py`）のテストです。
  - **test_config.py**: 設定ファイル（`config.yml`など）の読み込みや管理機能（`config_manager.py`）のテストです。
  - **test_date_formatter.py**: 日付フォーマット機能（`date_formatter.py`）のテストです。
  - **test_environment.py**: プロジェクトの実行環境や依存関係が正しく設定されているかを確認するテストです。
  - **test_integration.py**: プロジェクトの主要な機能がエンドツーエンドで正しく連携するかを検証する統合テストです。
  - **test_markdown_generator.py**: Markdown生成機能（`markdown_generator.py`）のテストです。
  - **test_project_overview_fetcher.py**: プロジェクト概要取得機能（`project_overview_fetcher.py`）のテストです。
  - **test_readme_badge_extractor.py**: READMEからのバッジ情報抽出機能（`readme_badge_extractor.py`）のテストです。
  - **test_repository_processor.py**: リポジトリ情報処理機能（`repository_processor.py`）のテストです。

## 関数詳細説明
提供された情報からは、各関数の具体的な引数、戻り値、詳細なロジックを直接分析することはできませんでした。しかし、ファイル名とその役割から、主要な機能を担うと思われる関数群を推測し、その役割を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**:
  - `main()`: プログラムのエントリーポイント。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdown生成までの一連の処理をオーケストレートします。
  - `generate_repo_list(username, output_file, limit)`: 指定されたGitHubユーザー名のリポジトリ情報を取得し、Markdown形式で出力ファイルに書き込む主要な関数。`limit`オプションで処理数を制限できます。
- **`src/generate_repo_list/badge_generator.py`**:
  - `generate_badge(badge_type, value)`: 指定されたタイプと値に基づいて、バッジのURLやマークダウン形式のバッジを生成します。
- **`src/generate_repo_list/config_manager.py`**:
  - `load_config(config_path)`: YAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
  - `get_github_token()`: `secrets.toml`などからGitHub APIトークンを安全に取得します。
- **`src/generate_repo_list/date_formatter.py`**:
  - `format_date(datetime_obj, format_str)`: 日付と時刻のオブジェクトを指定されたフォーマット文字列で整形します。
- **`src/generate_repo_list/language_info.py`**:
  - `get_language_breakdown(repo_languages)`: リポジトリの使用言語とその割合を分析し、整形された情報を返します。
- **`src/generate_repo_list/markdown_generator.py`**:
  - `generate_markdown_for_repo(repo_data)`: 個々のリポジトリデータを受け取り、そのリポジトリに関するMarkdownスニペットを生成します。
  - `generate_full_markdown(repo_list_data)`: 複数のリポジトリデータから、最終的なリポジトリ一覧のMarkdownコンテンツ全体を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**:
  - `fetch_project_overview(repo_name, github_token, config)`: 指定されたリポジトリの`generated-docs/project-overview.md`から3行のプロジェクト概要をHTTPリクエストで取得します。
- **`src/generate_repo_list/readme_badge_extractor.py`**:
  - `extract_badges_from_readme(readme_content)`: READMEのテキストコンテンツから、埋め込まれているバッジ（画像URL、リンク先、altテキストなど）を抽出します。
- **`src/generate_repo_list/repository_processor.py`**:
  - `process_repository_data(raw_repo_data, config, token)`: GitHub APIから取得した生のリポジトリデータを受け取り、Markdown生成に適した形に加工・整形します。
- **`src/generate_repo_list/statistics_calculator.py`**:
  - `calculate_repo_statistics(repo_data)`: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または抽出します。
- **`src/generate_repo_list/template_processor.py`**:
  - `render_template(template_path, data)`: 指定されたテンプレートファイルとデータを使って、最終的なテキストコンテンツをレンダリングします。
- **`src/generate_repo_list/url_utils.py`**:
  - `build_github_repo_url(username, repo_name)`: GitHubリポジトリのURLを構築します。
  - `is_valid_url(url)`: 指定された文字列が有効なURLであるかを検証します。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**:
  - `check_large_files_main()`: 大容量ファイルチェックスクリプトのメイン実行関数。設定ファイルに基づいてファイルをスキャンし、大容量ファイルを特定します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-08-16 07:07:18 JST
