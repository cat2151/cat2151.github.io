Last updated: 2025-12-28

# Project Overview

## プロジェクト概要
- GitHub APIを用いてリポジトリ情報を取得し、GitHub Pages用のMarkdownファイルを自動生成するシステムです。
- 検索エンジンからのクロール対象となりづらいGitHubユーザーページの問題を緩和し、リポジトリのSEOを向上させます。
- 自動生成されるリポジトリ一覧ページは、バッジ表示、分類、各リポジトリ概要の自動取得などの機能を持ちます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤として利用され、生成されたMarkdownファイルを静的サイトとしてレンダリングします。
    - **Markdown**: リポジトリ一覧や各リポジトリへのリンクを含むコンテンツの記述に用いられます。
    - **HTML/CSS**: 生成される最終的なGitHub Pagesサイトの表示に利用されます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、GitHub APIとの連携、データ処理、Markdown生成のロジックを実装しています。
    - **GitHub API**: リポジトリ名、説明、言語、スター数などの公開情報を取得するために使用されます。
    - **Ruff**: Pythonコードのスタイルチェックと自動フォーマットを行うツールで、コード品質の維持に貢献します。
- テスト:
    - **pytest**: Python用のテストフレームワークであり、ユニットテスト、結合テスト、統合テストの実行に利用され、コードの信頼性を確保します。
- ビルドツール:
    - **Pythonスクリプト**: プロジェクト自体がMarkdownファイルを「ビルド」（生成）する役割を担います。
- 言語機能:
    - **Pythonの標準ライブラリ**: ファイルI/O、HTTPリクエスト（`requests`ライブラリなどを使用）、データ構造操作などに広く利用されます。
- 自動化・CI/CD:
    - **GitHub Pages**: 生成された静的サイトをホストし、GitHubリポジトリへのプッシュをトリガーに自動デプロイが可能です。
- 開発標準:
    - **Ruff**: Pythonコードの統一されたスタイルと品質を強制するために使用されます。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定します。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載しています。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けヒントなどを記述した主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を管理します。
- **`assets/`**: サイトで使用される画像ファイル（ファビコンなど）を格納するディレクトリです。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのアイコンファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストに使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した `project-overview.md` など、動的に生成されたドキュメントを格納する可能性があります。
- **`googled947dc864c270e07.html`**: Google Search Consoleによるサイト所有権の確認に使用されるファイルです。
- **`index.md`**: 生成されたGitHubリポジトリ一覧のメインページとなるMarkdownファイルで、サイトのトップページに表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項、メモなどを記録したMarkdownファイル群です。
    - `10.md`, `12.md`, `14.md`, `2.md`, `4.md`, `6.md`, `8.md`: 特定の課題やメモに対応するファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコン、表示設定など）を定義するファイルです。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテストの実行に必要なPythonライブラリの依存関係を定義しています。
- **`requirements.txt`**: プロジェクトの実行に必要なPythonライブラリの依存関係を定義しています。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイルです。
- **`ruff.toml`**: PythonコードのフォーマッタおよびリンターであるRuffの設定ファイルで、コードスタイルのルールを定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`src/__init__.py`**: Pythonパッケージを示すファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
        - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示します。
        - **`src/generate_repo_list/badge_generator.py`**: リポジトリのプロパティ（言語、ライセンスなど）に基づいて表示用のバッジを生成するロジックを扱います。
        - **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの、実行時の技術的なパラメータを設定するファイルです。
        - **`src/generate_repo_list/config_manager.py`**: 設定ファイル（`config.yml`など）の読み込みと管理を行うロジックを提供します。
        - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメイン実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成します。
        - **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のため、JSON-LD形式で構造化データを埋め込む際のテンプレートファイルです。
        - **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語やその他の言語関連情報を処理・整形するロジックを扱います。
        - **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から、GitHub Pages向けのMarkdownコンテンツを生成するロジックを実装しています。
        - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの `generated-docs/project-overview.md` からプロジェクト概要を自動取得する機能を提供します。
        - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に処理するロジックです。
        - **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレート設定を定義するファイルです。
        - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算するロジックを扱います。
        - **`src/generate_repo_list/strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言を管理するためのファイルで、国際化/ローカライズに対応できます。
        - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレートの処理（変数置換など）を行うロジックです。
        - **`src/generate_repo_list/url_utils.py`**: URLの構築、正規化、解析など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher.py` の機能を検証するためのテストスクリプトです。
- **`tests/`**: プロジェクトの各モジュールや機能に対するテストスクリプトを格納するディレクトリです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理ロジックのテストを行います。
    - **`test_environment.py`**: 開発環境や依存関係が正しく設定されているかを検証するテストです。
    - **`test_integration.py`**: 複数のモジュールが連携して正しく動作するかを検証する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックの正確性を検証するテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要の取得と解析ロジックを検証するテストです。
    - **`test_repository_processor.py`**: GitHub APIから取得したリポジトリデータの処理ロジックを検証するテストです。

## 関数詳細説明
- **`generate_repo_list.py`**:
    - `main()`: このスクリプトのエントリポイント。GitHub APIからリポジトリ情報を取得し、整形処理、Markdown生成、最終出力までの一連のプロセスを制御します。
- **`badge_generator.py`**:
    - `generate_badge(repo_data)`: リポジトリのメタデータ（言語、ライセンスなど）を引数にとり、Markdown形式のバッジ文字列を生成して返します。
- **`config_manager.py`**:
    - `load_config(filepath)`: YAML形式の設定ファイルパスを引数にとり、その内容を辞書として読み込んで返します。
    - `get_setting(config, key_path)`: 設定辞書とキーパス（例: `project_overview.enabled`）を引数にとり、対応する設定値を取得します。
- **`markdown_generator.py`**:
    - `generate_repository_markdown(repo_info)`: 単一のリポジトリ情報（辞書形式）を引数にとり、そのリポジトリのMarkdown形式での表示部分（タイトル、説明、バッジ、リンクなど）を生成して返します。
    - `generate_repo_list_markdown(repos_data)`: 複数のリポジトリ情報（リスト形式）を引数にとり、それらをまとめたリポジトリ一覧全体のMarkdownコンテンツを生成して返します。
- **`project_overview_fetcher.py`**:
    - `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLと設定情報を引数にとり、そのリポジトリ内の `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出し、文字列として返します。
- **`repository_processor.py`**:
    - `process_repository_data(raw_data)`: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を引数にとり、Markdown生成に必要な情報（名前、説明、URL、言語、スター数など）に整形して返します。
- **`statistics_calculator.py`**:
    - `calculate_repo_statistics(repo_data)`: リポジトリデータ（例: スター数、フォーク数）を引数にとり、必要に応じて統計情報を計算し、追加のデータとして返します。
- **`template_processor.py`**:
    - `apply_template(template_string, context)`: テンプレート文字列と置換コンテキスト（辞書）を引数にとり、テンプレート内のプレースホルダーをコンテキストの値で置き換えた文字列を返します。
- **`url_utils.py`**:
    - `build_github_api_url(username, endpoint)`: GitHubユーザー名とAPIエンドポイントを引数にとり、完全なGitHub APIのURLを構築して返します。
    - `normalize_url(url_string)`: URL文字列を引数にとり、正規化されたURLを返します（例: 末尾のスラッシュの有無を統一）。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-28 07:05:45 JST
