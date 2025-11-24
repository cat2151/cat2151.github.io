Last updated: 2025-11-25

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- 生成された情報はSEOに最適化されており、検索エンジンやLLMによるリポジトリ発見性を高めます。
- 各リポジトリの概要やステータス（アクティブ、アーカイブなど）を魅力的に表示し、サイト訪問者に提供します。

## 技術スタック
- フロントエンド:
    - **GitHub Pages (Jekyll)**: 生成されたMarkdownファイルを表示するためのプラットフォーム。JekyllによってMarkdownがHTMLに変換され、ウェブサイトとして公開されます。
    - **Markdown**: リポジトリ一覧や個別のリポジトリ概要として生成されるコンテンツ形式。構造化されたテキストでウェブコンテンツを記述します。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語。GitHub APIからの情報取得、データの加工、Markdownファイルの生成といった中核的な処理を実行します。
    - **Git**: ソースコードのバージョン管理システム。
    - **GitHub API**: GitHubからユーザーのリポジトリ情報をプログラムで取得するために使用されます。
- テスト:
    - **pytest**: Pythonコードの単体テスト、統合テストを実行するためのフレームワーク。コードの品質と信頼性を保証します。
- ビルドツール:
    - **Pythonスクリプト**: プロジェクト自体がMarkdownファイルを自動生成するスクリプトであり、この生成処理が「ビルド」機能に相当します。
    - **Jekyll**: GitHub Pages上でMarkdownファイル群を静的なHTMLサイトとして構築・公開する静的サイトジェネレータ。
- 言語機能:
    - **Python**: スクリプトの実行環境と言語仕様。`requirements.txt`で管理される外部ライブラリも活用します。
- 自動化・CI/CD:
    - **自動生成スクリプト**: このシステム自体がリポジトリ一覧の「自動生成」を行うことで、手動での更新作業を排除し、コンテンツ更新の自動化を促進します。
- 開発標準:
    - **ruff**: Pythonコードのスタイルチェックとフォーマットを自動化するツール。コードの一貫性と可読性を保ちます。
    - **.editorconfig**: 異なる開発環境やエディタ間でのコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitが追跡しないファイルやディレクトリを指定します。開発環境固有のファイルや生成物などが含まれます。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの概要、設定方法、実行方法、機能などを説明する主要なドキュメントファイルです。
- **`_config.yml`**: GitHub Pages（Jekyll）サイト全体の基本的な設定を定義するファイルです。
- **`assets/`**: ウェブサイトで使用される静的アセット（画像、ファビコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: サイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズ画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグや単体テストに使用されるスクリプトです。
- **`generated-docs/`**: プロジェクトによって生成されるドキュメントやデータが格納される場所です。
- **`index.md`**: 生成されたリポジトリ一覧の最終出力ファイル。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: プロジェクト開発中の課題やメモがMarkdown形式で記録されているディレクトリです。
    - **`*.md`**: 各課題のメモファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイル。ホーム画面アイコンや表示モードを設定します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。
- **`requirements-dev.txt`**: 開発時やテスト時に必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: 本番環境での実行に必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンター/フォーマッター`ruff`の設定ファイルです。コードスタイルの自動修正などに使用されます。
- **`src/`**: プロジェクトの主要なソースコードが格納されるディレクトリです。
    - **`__init__.py`**: Pythonパッケージを示すファイル。
    - **`generate_repo_list/`**: リポジトリ一覧生成に関する主要なロジックが格納されているパッケージです。
        - **`__init__.py`**: Pythonパッケージを示すファイル。
        - **`badge_generator.py`**: リポジトリのステータス（例: "Active", "Archived"）に応じたバッジのMarkdown文字列を生成するロジックを提供します。
        - **`config.yml`**: プロジェクトの動作に関する技術的な設定パラメータ（例: プロジェクト概要取得機能の有効/無効、対象ファイルパス、タイムアウト設定など）を定義するYAMLファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、プロジェクト全体で設定値にアクセスするための機能を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成します。
        - **`json_ld_template.json`**: 検索エンジン最適化（SEO）のために、Schema.orgのJSON-LD形式のメタデータを生成するためのテンプレートです。
        - **`language_info.py`**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示可能な形式に変換する機能を提供します。
        - **`markdown_generator.py`**: 取得したリポジトリ情報と各種メタデータに基づいて、GitHub Pages向けのMarkdownコンテンツを整形・生成する主要なロジックを担当します。
        - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動的に抽出し、取得する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータをフィルタリング、分類（例: アクティブ、アーカイブ、フォークなど）、および必要な情報に加工する機能を提供します。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算し、Markdown表示用に整形する機能を提供します。
        - **`strings.yml`**: UI表示メッセージや文言など、ユーザーに表示される静的な文字列を一元管理するためのYAMLファイルです。多言語対応や文言変更の際に利用されます。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（文字列フォーマットやJekyllのLiquidタグなど）を処理し、動的にコンテンツを埋め込む機能を提供します。
        - **`url_utils.py`**: URLの構築、検証、エンコードなど、URL操作に関連するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能のテストケースを定義するスクリプトです。
- **`tests/`**: プロジェクトのテストコードを格納するディレクトリです。
    - **`test_config.py`**: 設定管理に関するテストケースです。
    - **`test_environment.py`**: 開発環境や依存関係に関するテストケースです。
    - **`test_integration.py`**: 複数のモジュールが連携する統合テストケースです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックに関するテストケースです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能に関するテストケースです。
    - **`test_repository_processor.py`**: リポジトリ情報の処理ロジックに関するテストケースです。

## 関数詳細説明
- **`generate_repo_list.py`**:
    - **`main()`**: プログラムのエントリポイント。コマンドライン引数を解析し、GitHub APIからのリポジトリ取得、データ加工、Markdown生成の一連の流れを統括します。
    - **`_fetch_and_process_repositories(username, limit)`**: 指定されたGitHubユーザー名のリポジトリをAPI経由で取得し、`repository_processor`を使用してフィルタリング・分類処理を行います。
    - **`_generate_output_markdown(repositories, output_file)`**: 処理済みのリポジトリ情報を用いて`markdown_generator`を呼び出し、最終的なMarkdownコンテンツを指定されたファイルに出力します。
- **`badge_generator.py`**:
    - **`generate_badge(status)`**: リポジトリのステータス（例: "active", "archived", "fork"）を受け取り、それに対応する視覚的なバッジのMarkdown表現を生成して返します。
- **`config_manager.py`**:
    - **`load_config(config_path)`**: 指定されたファイルパスからYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして設定データを返します。
    - **`get_setting(key)`**: ロードされた設定データから、指定されたキーに対応する値を取得します。設定値への一元的なアクセスを提供します。
- **`markdown_generator.py`**:
    - **`generate_repository_list_markdown(repositories)`**: 処理済みのリポジトリ情報のリストを受け取り、これらを基にした全体のリポジトリ一覧のMarkdownコンテンツを生成し、返します。
    - **`_format_repository_entry(repo_data)`**: 個々のリポジトリデータを受け取り、そのリポジトリのタイトル、説明、バッジなどを含むMarkdownスニペットを生成します。
- **`project_overview_fetcher.py`**:
    - **`fetch_project_overview(repo_name, owner, config)`**: 指定されたリポジトリのURLから、設定ファイルに定義されたパスのMarkdownファイル（例: `generated-docs/project-overview.md`）をフェッチし、特定のセクションから3行の概要を抽出し、返します。
- **`repository_processor.py`**:
    - **`process_repositories(raw_repos, config)`**: GitHub APIから取得した生の（未加工の）リポジトリデータを受け取り、設定に基づいてフィルタリング、分類（例: フォークの除外、アーカイブの分類）を行い、整形されたリポジトリ情報のリストを返します。
    - **`_classify_repository(repo)`**: 個々のリポジトリオブジェクトがアクティブ、アーカイブ、フォークのどのカテゴリに属するかを判断し、その分類を返します。
- **`template_processor.py`**:
    - **`apply_template(template_string, data)`**: テンプレート文字列と、テンプレート内のプレースホルダーに埋め込むデータ辞書を受け取ります。データを使用してテンプレート内の値を置換し、最終的な文字列を生成して返します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-25 07:06:03 JST
