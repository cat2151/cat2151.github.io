Last updated: 2026-08-22

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成し、検索エンジンからの可視性を高めます。
- GitHub APIを活用し、各リポジトリの概要やバッジを含むSEO最適化されたMarkdownを作成します。
- これにより、LLMがリポジトリ情報を参照しやすくなり、開発効率向上に貢献します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの静的サイトジェネレータ), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当なし
- 開発ツール: pytest (Pythonテストフレームワーク), ruff (Pythonリンター), Git (バージョン管理システム)
- テスト: pytest (ユニットテストおよび統合テストフレームワーク)
- ビルドツール: Jekyll (GitHub Pagesによって使用される静的サイトジェネレータ)
- 言語機能: Python (主要なスクリプト言語), YAML (設定ファイル管理), TOML (設定ファイル管理)
- 自動化・CI/CD: GitHub Actions (`.github_automation` ディレクトリから、特定の自動化スクリプト実行に利用されている可能性)
- 開発標準: ruff (Pythonコードの静的解析とスタイル強制), .editorconfig (エディタ間でのコードスタイル統一)

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
- **`.editorconfig`**: 異なるエディタやIDE間で、タブやスペースの幅、改行コードなどの基本的なコードスタイルを統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリです。
    - **`check_large_files/`**: 大容量ファイルを検出・管理するためのツールと設定が含まれます。
        - **`README.md`**: `check_large_files` ツールの目的と使用方法を説明するドキュメントです。
        - **`check-large-files.toml`**: `check_large_files` スクリプトの動作設定を定義するTOML形式の設定ファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリのパターンを定義するファイルです。
- **`LICENSE`**: プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクトの目的、機能、使用方法、設定、ライセンスなどを概説する主要なドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の挙動や設定を定義するファイルで、GitHub Pagesの構築に利用されます。
- **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブやブックマークに表示されるウェブサイトのアイコン画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher` 機能のデバッグやテストに特化した補助スクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントや、外部リポジトリから取得した概要ファイルなどを格納するディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権を確認するために配置されるHTMLファイルです。
- **`index.md`**: 生成されたリポジトリ一覧が格納されるMarkdownファイルで、GitHub Pagesのルートページとして機能します。
- **`issue-notes/22.md`**: 特定の課題（Issue）に関する詳細なメモや解決策の検討などを記録したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの表示設定などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワーク `pytest` の設定ファイルで、テストの挙動をカスタマイズします。
- **`requirements-dev.txt`**: プロジェクトの開発およびテストにのみ必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: プロジェクトを本番環境で実行するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター `ruff` の設定ファイルで、コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なPythonソースコードが格納されているディレクトリです。
    - **`src/__init__.py`**: Pythonがこのディレクトリをパッケージとして認識するために必要なファイルです。
    - **`src/generate_repo_list/`**: リポジトリ一覧生成システムのメインロジックを含むPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させます。
        - **`badge_generator.py`**: リポジトリの言語、スター数などの情報を視覚的なバッジとして生成する機能を提供します。
        - **`config.yml`**: プロジェクト概要の取得設定など、システムの技術的パラメータを定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、プログラム内で利用するためのインターフェースを提供します。
        - **`date_formatter.py`**: 日付や時刻の情報を特定の形式に整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、Markdown形式でリポジトリ一覧を生成する、このプロジェクトの中心的なスクリプトです。
        - **`json_ld_template.json`**: 構造化データ（JSON-LD）のテンプレートファイルで、検索エンジン最適化（SEO）のために利用されます。
        - **`language_info.py`**: リポジトリの使用言語に関する情報を処理し、整形するためのロジックを提供します。
        - **`markdown_generator.py`**: 取得および加工されたデータから、SEOに最適化されたMarkdownコンテンツを生成する機能を提供します。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出し取得します。
        - **`readme_badge_extractor.py`**: リポジトリの `README.md` ファイルから特定のバッジ情報（ビルドステータスなど）を抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIから取得した個々のリポジトリデータを受け取り、必要な情報に加工・整形する役割を担います。
        - **`seo_template.yml`**: 生成されるMarkdownのSEO関連メタデータやテンプレート構造を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算し、レポートするための機能を提供します。
        - **`strings.yml`**: 生成されるMarkdownコンテンツで使用される各種メッセージや文言を一元管理するためのYAMLファイルです。
        - **`template_processor.py`**: Markdown生成時に使用するテンプレートファイル（例: Jinja2テンプレート）を処理し、データと結合して最終コンテンツをレンダリングします。
        - **`url_utils.py`**: URLの検証、構築、パースなど、URL操作に関するユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher` 機能が正しく動作するかを確認するためのユニットテストファイルです。
- **`tests/`**: プロジェクト全体のテストコードが格納されているディレクトリです。
    - **`conftest.py`**: `pytest` のテスト実行時に共通して使用されるフィクスチャやヘルパー関数を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator` モジュールの統合テストを実行し、複数のコンポーネント連携を確認します。
    - **`test_check_large_files.py`**: `check_large_files.py` スクリプトの機能が期待通りに動作するかを検証するテストです。
    - **`test_config.py`**: 設定ファイル（`config.yml`, `strings.yml` など）の読み込みと管理機能が正しく動作するかを検証するテストです。
    - **`test_date_formatter.py`**: `date_formatter` モジュールの日付整形機能が正しく動作するかを検証するテストです。
    - **`test_environment.py`**: プロジェクトの実行環境や依存関係が正しく設定されているかを確認するテストです。
    - **`test_integration.py`**: 主要なモジュールやコンポーネントが連携して正しく機能するかを検証する、広範囲な統合テストです。
    - **`test_markdown_generator.py`**: `markdown_generator` モジュールのMarkdown生成機能が正しく動作するかを検証するテストです。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher` が外部リポジトリから概要を正しく取得できるかを検証するテストです。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor` がREADMEからバッジ情報を正確に抽出できるかを検証するテストです。
    - **`test_repository_processor.py`**: `repository_processor` がGitHubリポジトリデータを正しく加工・整形できるかを検証するテストです。

## 関数詳細説明
- **`generate_repo_list.py`**
    - `main()`: プログラムのエントリポイント。コマンドライン引数をパースし、リポジトリ一覧生成の主要なロジックを呼び出します。
    - `generate_repo_list(username, output_file, limit)`: 指定されたユーザー名のリポジトリ情報をGitHub APIから取得し、指定されたファイルにMarkdown形式のリポジトリ一覧を生成します。
- **`project_overview_fetcher.py`**
    - `fetch_project_overview(repo_name, owner, config)`: 指定されたリポジトリから `generated-docs/project-overview.md` ファイルを読み込み、設定に基づき3行のプロジェクト概要を抽出して返します。
- **`badge_generator.py`**
    - `generate_badge(label, message, color)`: 指定されたラベル、メッセージ、色でMarkdown形式のバッジ文字列を生成します。
- **`markdown_generator.py`**
    - `generate_markdown(repo_data_list, strings_config, seo_template)`: 処理されたリポジトリデータのリストと設定情報をもとに、GitHub Pages用の最終的なMarkdownコンテンツを生成します。
- **`repository_processor.py`**
    - `process_repository(repo_info, config)`: GitHub APIから取得した生のリポジトリ情報を受け取り、表示に必要な形式に加工・整形します。プロジェクト概要の取得などもここから呼び出されます。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**
    - `main()`: スクリプトのエントリポイント。設定ファイルを読み込み、リポジトリ内の大容量ファイルを検出します。
    - `check_files(config)`: 設定ファイルで定義されたルールに基づき、リポジトリ内のファイルのサイズをチェックします。
- **`config_manager.py`**
    - `load_config(file_path)`: 指定されたパスからYAMLまたはTOML形式の設定ファイルを読み込み、辞書として返します。
    - `get_setting(config_data, key_path, default=None)`: 読み込んだ設定データから指定されたキーパスの値を取得します。
- **`date_formatter.py`**
    - `format_date(iso_date_string)`: ISO 8601形式の日付文字列を受け取り、読みやすい形式に整形して返します。
- **`language_info.py`**
    - `get_language_details(language_stats)`: リポジトリの言語統計情報から、主要な言語とその割合などを抽出し、整形された情報として返します。
- **`readme_badge_extractor.py`**
    - `extract_badges_from_readme(readme_content)`: READMEのMarkdownコンテンツから特定のパターンに合致するバッジ情報を抽出し、リストとして返します。
- **`statistics_calculator.py`**
    - `calculate_statistics(repo_list)`: リポジトリのリストを受け取り、合計スター数やフォーク数などの統計情報を計算して返します。
- **`template_processor.py`**
    - `render_template(template_path, context)`: 指定されたテンプレートファイル（例: Jinja2）を、与えられたコンテキストデータでレンダリングし、最終的な文字列を生成します。
- **`url_utils.py`**
    - `construct_repo_url(username, repo_name)`: GitHubユーザー名とリポジトリ名から、リポジトリのURLを構築します。
    - `validate_url(url_string)`: 指定された文字列が有効なURLであるかを検証します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-22 07:06:30 JST
