Last updated: 2025-11-13

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動で取得するシステムです。
- 取得したデータから、SEOに最適化されたGitHub Pages向けのMarkdownファイルを生成します。
- これにより、リポジトリ一覧の検索エンジンへの露出とLLMによる参照性を向上させます。

## 技術スタック
- フロントエンド:
    - **Jekyll (GitHub Pages)**: 生成されるMarkdownファイルが対象とする静的サイトジェネレータ。GitHub Pagesの基盤として利用され、本プロジェクトはJekyllサイトに組み込まれるコンテンツを生成します。
    - **Markdown**: リポジトリ一覧や各リポジトリへのリンクを含むコンテンツの出力形式。SEO最適化された構造で生成されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの中核となるスクリプト言語。GitHub APIからのデータ取得、加工、Markdown生成の全てを担います。
    - **GitHub API**: GitHubリポジトリのメタデータ（説明、スター数、言語など）をプログラムから取得するために使用されます。
- テスト:
    - **pytest**: Pythonコードのテストフレームワーク。プロジェクトの各モジュールや機能が正しく動作することを確認するために使用されます。
- ビルドツール:
    - **Pythonスクリプトによる生成**: 特定の外部ビルドツールは使用せず、Pythonスクリプト自体がリポジトリ情報の取得からMarkdownファイルの生成までの一連の処理を行います。
- 言語機能:
    - **Python**: 言語そのものの機能（標準ライブラリ、データ構造、制御フローなど）が、スクリプトの実装に利用されています。
- 自動化・CI/CD:
    - このプロジェクト自体はCI/CDを必須とせず、ローカルでの実行を重視していますが、生成された成果物はGitHub Pagesの自動デプロイフローに乗せることができます。
- 開発標準:
    - **Ruff**: Pythonコードのリンターおよびフォーマッター。コード品質とスタイルの一貫性を保つために使用されます。
    - **TOML/YAML**: 設定ファイル（`pytest.ini`, `ruff.toml`, `config.yml`, `strings.yml`, `seo_template.yml` など）の記述に用いられるデータシリアライゼーション言語。

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
-   **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を維持するための設定ファイル。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するファイル。生成物や一時ファイルなどが含まれます。
-   **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記述したファイル。
-   **`README.md`**: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、概要を説明する主要なドキュメント。
-   **`_config.yml`**: JekyllベースのGitHub Pagesサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
-   **`assets/`**: ウェブサイトで使用される静的なリソース（画像、ファビコンなど）を格納するディレクトリ。
    -   **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の異なるサイズを提供します。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能の動作を検証・デバッグするための補助的なスクリプト。
-   **`generated-docs/`**: 本システムによって生成されたドキュメント（例: 各リポジトリの概要ページなど）が出力されることが想定されるディレクトリ。
-   **`index.md`**: メインのMarkdown出力ファイル。GitHub Pagesサイトのトップページとして機能し、生成されたリポジトリ一覧がここに記述されます。
-   **`issue-notes/`**: プロジェクト開発中の課題や検討事項、メモなどをMarkdown形式で記録したファイル群。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用される設定ファイル。アプリの表示方法やアイコンなどを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークpytestの設定ファイル。テストの挙動やオプションを定義します。
-   **`requirements-dev.txt`**: 開発環境やテスト実行に必要なPythonライブラリをリストアップしたファイル。
-   **`requirements.txt`**: 本番環境でプロジェクトを実行するために必要なPythonライブラリをリストアップしたファイル。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールすべきか、またはすべきでないかを指示するファイル。SEO対策の一部です。
-   **`ruff.toml`**: PythonコードのスタイルチェックツールRuffの設定ファイル。コードの書式や潜在的な問題を検出するためのルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されるルートディレクトリ。
    -   **`src/__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイル。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成システムのコアロジックを含むPythonパッケージ。
        -   **`src/generate_repo_list/__init__.py`**: `generate_repo_list` ディレクトリがPythonパッケージであることを示すファイル。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリ情報に基づいて、言語やステータスなどのバッジを生成するロジックを管理します。
        -   **`src/generate_repo_list/config.yml`**: プロジェクト概要の取得設定など、システムが使用する技術的なパラメータを定義する設定ファイル。
        -   **`src/generate_repo_list/config_manager.py`**: YAMLなどの設定ファイルを読み込み、プログラム内で利用可能な形式で管理するモジュール。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプト。GitHub APIからのリポジトリ取得からMarkdown生成までの全体的な処理を調整します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を埋め込むためのテンプレート。
        -   **`src/generate_repo_list/language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を処理し、集計するモジュール。
        -   **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報とテンプレートに基づいて、最終的なMarkdownコンテンツを生成するロジックを実装します。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を抽出し、取得するモジュール。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形する処理を行います。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや構造化データの生成に使用されるテンプレート設定。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算するモジュール。
        -   **`src/generate_repo_list/strings.yml`**: プロジェクト内で表示されるメッセージや文言を一元的に管理するための設定ファイル。多言語対応や文言変更を容易にします。
        -   **`src/generate_repo_list/template_processor.py`**: 汎用的なテンプレート処理（文字列置換や条件分岐など）を行うためのモジュール。Markdown生成などで利用されます。
        -   **`src/generate_repo_list/url_utils.py`**: URLの構築、検証、整形など、URLに関連するユーティリティ関数を提供します。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールに関連する機能の単体テストを行うファイル。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリ。
    -   **`test_config.py`**: `config_manager.py` など、設定関連のモジュールのテスト。
    -   **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテスト。
    -   **`test_integration.py`**: 複数のモジュールが連携して動作する際の統合テスト。
    -   **`test_markdown_generator.py`**: `markdown_generator.py` の生成ロジックに関するテスト。
    -   **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` の詳細なテスト。
    -   **`test_repository_processor.py`**: `repository_processor.py` のデータ処理ロジックに関するテスト。

## 関数詳細説明
-   **`generate_repo_list.py`**
    -   `main()`: スクリプトのエントリーポイント。コマンドライン引数を解析し、リポジトリ一覧生成の処理を開始します。
    -   `generate_repo_list(username, output_file, limit)`: 指定されたユーザー名のリポジトリ情報を取得し、Markdown形式で出力ファイルに書き込む主要な関数。リポジトリ数の制限も可能です。
-   **`repository_processor.py`**
    -   `fetch_repositories(username, token)`: GitHub APIを使用して、指定されたユーザーのリポジトリ一覧を取得します。認証のためにGitHubトークンを使用します。
    -   `process_repository_data(repo_data, config, strings)`: GitHub APIから取得した生のリポジトリデータ（JSON形式）を解析し、Markdown生成に適した形式に整形します。設定や表示文言を考慮します。
-   **`markdown_generator.py`**
    -   `generate_markdown(processed_repos, config, strings, json_ld_template, seo_template)`: 処理済みのリポジトリデータと各種テンプレート・設定を基に、最終的なMarkdownコンテンツ全体を生成します。
    -   `format_repository(repo, config, strings)`: 単一のリポジトリ情報を受け取り、そのリポジトリの表示部分に対応するMarkdownスニペットを生成します。
-   **`project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_name, github_token, config)`: 指定されたリポジトリの特定のパスにある`project-overview.md`ファイルから、プロジェクト概要の3行説明を抽出し取得します。
    -   `parse_project_overview(content, section_title)`: Markdownコンテンツから指定されたセクションタイトル（例: "プロジェクト概要"）の下にある箇条書きの3行を解析して抽出します。
-   **`badge_generator.py`**
    -   `generate_badge_markdown(status)`: リポジトリのステータス（アクティブ、アーカイブ、フォークなど）に応じて、対応するバッジのMarkdownを生成します。
-   **`config_manager.py`**
    -   `load_config(config_path)`: 指定されたパスからYAMLまたはTOML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして返します。
-   **`language_info.py`**
    -   `get_language_breakdown(repo_name, github_token)`: 特定のリポジトリで使用されているプログラミング言語とその割合に関する情報をGitHub APIから取得します。
-   **`statistics_calculator.py`**
    -   `calculate_stats(repo)`: リポジトリデータからスター数、フォーク数、最終更新日などの統計情報を計算します。
-   **`template_processor.py`**
    -   `render_template(template_string, data)`: テンプレート文字列とデータ辞書を受け取り、テンプレート内のプレースホルダーをデータで置き換えてレンダリングされた文字列を返します。
-   **`url_utils.py`**
    -   `build_github_api_url(endpoint, username)`: GitHub APIのエンドポイントとユーザー名を使用して、APIリクエスト用の完全なURLを構築します。
    -   `normalize_url(url_string)`: URLを標準的な形式に整形したり、クエリパラメータを処理したりするなどのユーティリティ機能を提供します。

## 関数呼び出し階層ツリー
```
提供された情報からは具体的な関数呼び出し階層ツリーを生成できませんでした。
しかし、主要な処理の流れとしては、`src/generate_repo_list/generate_repo_list.py` 内の `generate_repo_list` 関数が中心となり、以下のモジュール群の関数を呼び出して全体処理を調整します。

- `config_manager.py`: 設定ファイルの読み込み
- `repository_processor.py`: GitHub APIからのリポジトリ取得とデータ整形
- `project_overview_fetcher.py`: 各リポジトリからの概要取得
- `language_info.py`: リポジトリの言語情報取得
- `statistics_calculator.py`: 統計情報の計算
- `badge_generator.py`: バッジの生成
- `markdown_generator.py`: 整形されたデータとテンプレートを使った最終的なMarkdownコンテンツの生成
- `template_processor.py`: 汎用的なテンプレートレンダリング
- `url_utils.py`: URL関連のユーティリティ

これらのモジュールが連携して、最終的なリポジトリ一覧Markdownファイルを生成します。

---
Generated at: 2025-11-13 07:06:36 JST
