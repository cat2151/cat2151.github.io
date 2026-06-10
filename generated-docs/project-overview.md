Last updated: 2026-06-11

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のGitHubリポジトリ一覧を自動で生成するシステムです。
- 生成されたリポジトリ一覧は、GitHub Pages（`*.github.io`）サイト向けにSEO最適化されたMarkdown形式で出力されます。
- 検索エンジンからのクロールを促進し、各リポジトリの発見性を高めることで、情報のアクセス性とLLM連携の改善を目指します。

## 技術スタック
- フロントエンド: Jekyll: GitHub Pagesで利用される静的サイトジェネレータです。本プロジェクトはJekyllが解釈できるMarkdownファイルを生成し、これによりウェブサイトとして表示されます。
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - Python: プロジェクトの主要な開発言語です。リポジトリ情報の取得、処理、Markdown生成の全てを担います。
    - YAML: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述に使用され、プロジェクトの動作パラメータや表示文言を一元管理します。
    - TOML: GitHubトークンなどの機密情報（`secrets.toml`）や、コードスタイル設定（`ruff.toml`, `check-large-files.toml`）に利用される設定ファイル形式です。
- テスト: pytest: Python製のテストフレームワークです。コードの品質と機能の正確性を保証するための自動テスト実行に使用されます。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py` が中心となり、GitHub APIからデータを取得し、最終的なMarkdownファイルを「ビルド」します。
    - Markdown: 生成される出力形式であり、JekyllによってGitHub Pagesサイトとしてレンダリングされます。
- 言語機能:
    - Python: 高レベルで汎用的なプログラミング言語です。豊富なライブラリと簡潔な構文により、迅速な開発を可能にします。
- 自動化・CI/CD:
    - GitHub Pages: 生成されたMarkdownファイルはGitHub Pagesによって自動的にウェブサイトとしてデプロイされます。
    - `check-large-files.py`: GitHub Actionsで使用される、リポジトリ内の大規模ファイルをチェックするための自動化スクリプトです。
- 開発標準:
    - ruff: Pythonコード用の高速なLinterおよびFormatterです。コードの品質と一貫性を自動的に保ちます。
    - .editorconfig: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。

## ファイル階層ツリー
```
📄 .editorconfig
📁 .github_automation/
  📁 check_large_files/
    📖 README.md
    📄 check-large-files.toml
    📁 scripts/
      📄 check_large_files.py
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
  📖 22.md
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
    📄 date_formatter.py
    📄 generate_repo_list.py
    📊 json_ld_template.json
    📄 language_info.py
    📄 markdown_generator.py
    📄 project_overview_fetcher.py
    📄 readme_badge_extractor.py
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 conftest.py
  📄 test_badge_generator_integration.py
  📄 test_check_large_files.py
  📄 test_config.py
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_readme_badge_extractor.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
-   **`.editorconfig`**: 異なる開発環境でコードのスタイル（インデント、文字コードなど）を統一するための設定ファイルです。
-   **`.github_automation/`**: GitHub Actionsのワークフローで利用される自動化スクリプトや設定を格納するディレクトリです。
    -   **`.github_automation/check_large_files/README.md`**: 大規模ファイルチェック機能に関する説明ドキュメントです。
    -   **`.github_automation/check_large_files/check-large-files.toml`**: 大規模ファイルチェックツールの設定ファイルで、チェック対象の閾値などを定義します。
    -   **`.github_automation/check_large_files/scripts/check_large_files.py`**: リポジトリ内の大規模ファイルを検出し、CIプロセスで警告またはエラーを出すPythonスクリプトです。
-   **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定するためのファイルです。
-   **`LICENSE`**: このプロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイルです。
-   **`README.md`**: プロジェクトの概要、目的、主な機能、使用方法など、全体的な情報を提供するメインドキュメントです。
-   **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。GitHub Pagesのテーマやプラグインに関する設定を定義します。
-   **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセット（画像など）を格納するディレクトリです。
    -   **`favicon-*.png`**: ブラウザのタブやブックマークなどに表示されるウェブサイトのアイコン（ファビコン）の各種サイズです。
-   **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストを目的とした補助スクリプトです。
-   **`generated-docs/`**: 本来のプロジェクトではなく、外部から参照されるドキュメントなどを配置する（このプロジェクトでは空またはプレースホルダ）ディレクトリです。
-   **`googled947dc864c270e07.html`**: Google Search Consoleによるサイトの所有権確認のために配置されるHTMLファイルです。
-   **`index.md`**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメイン出力ファイルです。GitHub Pagesのトップページとして表示されます。
-   **`issue-notes/`**: 開発中の課題や検討事項をメモとして残すためのディレクトリです。
    -   **`issue-notes/22.md`**: 特定の課題（例：Issue #22）に関する詳細なメモや情報が記述されたMarkdownファイルです。
-   **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルです。アプリの表示名やアイコンなどを定義します。
-   **`pytest.ini`**: Pythonのテストフレームワークpytestの設定ファイルです。テストの実行オプションや対象パスを定義します。
-   **`requirements-dev.txt`**: 開発環境およびテスト環境でのみ必要となるPythonパッケージの一覧です。
-   **`requirements.txt`**: プロジェクトの本番稼働に必要となるPythonパッケージの一覧です。
-   **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
-   **`ruff.toml`**: PythonコードのLinterおよびFormatterであるRuffの設定ファイルです。コーディング規約やチェックルールを定義します。
-   **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    -   **`src/generate_repo_list/`**: リポジトリ一覧生成機能のコアロジックを構成するPythonモジュール群です。
        -   **`src/generate_repo_list/badge_generator.py`**: リポジトリのプログラミング言語やスター数などを示すバッジのMarkdownを生成するスクリプトです。
        -   **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成に関する技術的パラメータ（プロジェクト概要取得の有無、対象ファイルパスなど）を設定するYAMLファイルです。
        -   **`src/generate_repo_list/config_manager.py`**: プロジェクトで使用される様々な設定ファイル（YAML、TOMLなど）の読み込みと管理を担当するスクリプトです。
        -   **`src/generate_repo_list/date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティスクリプトです。
        -   **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトです。GitHub APIからのリポジトリ情報取得、処理、そして最終的なMarkdownファイルへの出力フロー全体を制御します。
        -   **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のためにウェブページに構造化データを提供するJSON-LD形式のテンプレートです。
        -   **`src/generate_repo_list/language_info.py`**: リポジトリのプログラミング言語に関する情報を取得・処理・表示するロジックを扱います。
        -   **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータから、最終的なMarkdown形式のコンテンツを生成するスクリプトです。
        -   **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例：`generated-docs/project-overview.md`）から、プロジェクトの3行概要を抽出する機能を提供します。
        -   **`src/generate_repo_list/readme_badge_extractor.py`**: 各リポジトリのREADMEファイルから、既存のバッジ情報を抽出する機能を持つスクリプトです。
        -   **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを詳細に処理し、表示に適した形式に整形する役割を担います。
        -   **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやテンプレートを定義するためのYAMLファイルです。
        -   **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数などの統計情報を計算し、表示用に準備するスクリプトです。
        -   **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージや文言（タイトル、説明など）を一元管理するYAMLファイルです。
        -   **`src/generate_repo_list/template_processor.py`**: Markdownコンテンツ生成時に使用されるテンプレート（Jekyll構文など）の処理を行うスクリプトです。
        -   **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ機能を提供するスクリプトです。
-   **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能に関するテストコードです。
-   **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    -   **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数など、テスト実行全体で共有される設定を定義します。
    -   **`tests/test_*.py`**: 各モジュールや機能に対応する単体テストまたは統合テストのスクリプトです。

## 関数詳細説明
-   **`generate_repo_list.py`** (メインスクリプト)
    -   `main()`: スクリプトのエントリポイント。コマンドライン引数を解析し、リポジトリ情報の取得・処理、Markdown生成といった全体の処理フローを調整します。
    -   `parse_arguments()`: コマンドライン引数を解釈し、ユーザー名、出力ファイル名、処理するリポジトリ数の上限などを取得します。
    -   `generate_repository_list(username, output_file, limit=None)`: 指定されたGitHubユーザーのリポジトリ情報を取得し、各リポジトリを処理して、最終的なリポジトリ一覧のMarkdownコンテンツを生成し、指定ファイルに出力します。
-   **`repository_processor.py`**
    -   `process_repository(repo_data, config)`: GitHub APIから取得した個々のリポジトリデータを受け取り、表示に必要な情報を抽出し、整形します。これにはプロジェクト概要の取得やバッジ生成の呼び出しなどが含まれます。
-   **`project_overview_fetcher.py`**
    -   `fetch_project_overview(repo_url, config)`: 指定されたリポジトリのURLから、`config.yml`で定義されたパスにあるプロジェクト概要ファイル（例: `generated-docs/project-overview.md`）の内容を非同期で取得し、そこから3行のプロジェクト概要を抽出します。
-   **`markdown_generator.py`**
    -   `generate_markdown(repo_list_data, seo_config, strings_data)`: 処理済みのリポジトリリストデータとSEO設定、表示文言データを使用して、GitHub Pages向けのSEO最適化されたMarkdownコンテンツ全体を生成します。
-   **`badge_generator.py`**
    -   `create_badge_markdown(language, stars)`: プログラミング言語やスター数などの情報に基づいて、Markdown形式で表示されるGitHubリポジトリのバッジを生成します。

## 関数呼び出し階層ツリー
```
main() (generate_repo_list.py)
├── parse_arguments()
└── generate_repository_list(username, output_file, limit)
    ├── config_manager.load_config()
    ├── repository_processor.process_repository(repo_data, config)  # 各リポジトリに対して呼び出し
    │   ├── project_overview_fetcher.fetch_project_overview(repo_url, config)
    │   ├── badge_generator.create_badge_markdown(language, stars)
    │   └── date_formatter.format_date(timestamp)
    └── markdown_generator.generate_markdown(processed_repo_data, seo_config, strings_data)
        └── template_processor.render_template(template, data)

---
Generated at: 2026-06-11 07:41:06 JST
