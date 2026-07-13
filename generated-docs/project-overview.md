Last updated: 2026-07-14

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得するシステムです。
- 取得した情報からJekyllベースのGitHub Pagesサイト向けに最適化されたMarkdownファイルを生成します。
- これにより、リポジトリ一覧ページのSEOを強化し、検索エンジンやLLMによる参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤とし、Markdown形式でコンテンツを生成します。最終的なウェブサイトはHTMLとして提供されます。
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連の技術は使用していません。
- 開発ツール:
    - **pytest**: Pythonコードのテストフレームワークとして利用され、機能の検証や品質保証を支援します。
    - **ruff**: Pythonの高速LinterおよびFormatterで、コードスタイルの統一と品質維持に貢献します。
- テスト: **pytest** が主にテスト実行環境として使用され、さまざまなテストスクリプト（例: ユニットテスト、統合テスト）が記述されています。
- ビルドツール: Pythonスクリプト自体がMarkdownファイルを「生成」するビルドプロセスを担います。最終的なGitHub PagesのデプロイはJekyllによって行われます。
- 言語機能:
    - **Python**: プロジェクトの主要なスクリプト言語であり、GitHub APIとの連携、データ処理、Markdown生成の全てを担います。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、設定や文言の管理を容易にします。
    - **Markdown**: 生成されるリポジトリ一覧ページのフォーマットとして使用されます。
- 自動化・CI/CD: GitHub APIを利用してリポジトリ情報を取得する自動化プロセスが核となります。CI/CDツールとして明示的な記述はないものの、`_github_automation` ディレクトリなど、自動化に向けた基盤が存在します。
- 開発標準:
    - **ruff**: コードフォーマットと静的解析により、コード品質と統一性を保証します。
    - **.editorconfig**: 異なるエディタ間でのコーディングスタイルの一貫性を保つための設定ファイルです。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイル（インデント、改行コードなど）を強制するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化タスクに関連するスクリプトや設定を格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック機能に関する説明ドキュメントです。
    - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から外すファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクト全体の概要、目的、使い方などが記述された主要な説明ドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルです。テーマ、プラグイン、変数などを定義します。
- **`assets/`**: ウェブサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-16x16.png`**, **`favicon-192x192.png`**, **`favicon-32x32.png`**, **`favicon-512x512.png`**: ウェブサイトのファビコン（サイトアイコン）として使用される様々なサイズの画像ファイルです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテスト実行に使用されるスクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得された、またはこのプロジェクトによって生成されたドキュメント（例: `project-overview.md`）が格納される可能性のあるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサービスでサイトの所有権を確認するために配置されるHTML検証ファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトでは、生成されたリポジトリ一覧が出力される主要なファイルとなります。
- **`issue-notes/22.md`**: 開発中の特定の課題（Issue #22）に関するメモや詳細を記録したファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加、オフライン機能などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出ルールやオプションを定義します。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要なPythonパッケージとそのバージョンを記載したファイルです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびFormatterであるruffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: Pythonのパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: GitHubリポジトリ一覧生成機能に関連するモジュールを格納するパッケージです。
        - **`__init__.py`**: Pythonのパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの属性（言語、ライセンスなど）に応じたバッジの生成ロジックを実装しています。
        - **`config.yml`**: プロジェクトの振る舞いを制御する各種設定（例: プロジェクト概要取得機能の有効/無効）が記述されたYAML形式の設定ファイルです。
        - **`config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを提供します。
        - **`date_formatter.py`**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        - **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルへの出力を調整します。
        - **`json_ld_template.json`**: SEO強化のためのJSON-LD（構造化データ）のテンプレートファイルです。
        - **`language_info.py`**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するロジックを実装しています。
        - **`markdown_generator.py`**: 取得したリポジトリ情報と設定に基づいて、出力用のMarkdownテキストを生成する役割を担います。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要テキストを抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報（例: ビルドステータス）を抽出するロジックを実装しています。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、必要な形式に加工・整形する主要な処理ロジックを提供します。
        - **`seo_template.yml`**: 検索エンジン最適化（SEO）に関連するメタデータやテンプレートの設定を定義したYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算する機能を提供します。
        - **`strings.yml`**: ウェブサイト上で表示される各種メッセージや文言を一元的に管理するためのYAMLファイルです。多言語対応や文言変更を容易にします。
        - **`template_processor.py`**: Markdown生成時に使用されるテンプレート（Jekyll構文など）を処理し、動的なコンテンツを埋め込む機能を提供します。
        - **`url_utils.py`**: URLの生成、解析、検証などの汎用的なURL関連ユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクトのテストコードを体系的に格納するディレクトリです。
    - **`conftest.py`**: pytestにおいて、テスト実行前に共有されるフィクスチャやヘルパー関数を定義するためのファイルです。
    - **`test_badge_generator_integration.py`**: バッジ生成モジュールの統合的な動作を検証するテストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能の正確性を検証するテストです。
    - **`test_config.py`**: 設定ファイルの読み込みや管理が正しく行われるかを検証するテストです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティの正確性を検証するテストです。
    - **`test_environment.py`**: プロジェクト実行環境（依存関係など）が適切に設定されているかを検証するテストです。
    - **`test_integration.py`**: 主要なコンポーネントが連携して動作する全体的なフローを検証する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックの正確性を検証するテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要フェッチ機能が正しく動作するかを検証するテストです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出ロジックの正確性を検証するテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理ロジックの正確性を検証するテストです。

## 関数詳細説明
提供された情報からは具体的な関数のシグネチャ（引数、戻り値）は特定できませんが、各モジュールの役割に基づき、主要な関数とその機能を説明します。

- **`src/generate_repo_list/generate_repo_list.py`**
    - **`main()`**: プロジェクトの主要なエントリーポイント。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdown形式のリポジトリ一覧ファイルを生成する一連の処理を調整します。
- **`src/generate_repo_list/badge_generator.py`**
    - **`generate_badge_markdown(repo_data)`**: リポジトリデータ(`repo_data`)を基に、言語やライセンスなどの情報を示すMarkdown形式のバッジ文字列を生成します。
- **`src/generate_repo_list/config_manager.py`**
    - **`load_config(config_path)`**: 指定されたパス(`config_path`)からYAML形式の設定ファイルを読み込み、Pythonオブジェクトとして返します。
- **`src/generate_repo_list/date_formatter.py`**
    - **`format_date(datetime_obj, format_string)`**: 日時オブジェクト(`datetime_obj`)を指定された形式(`format_string`)で整形した文字列を返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - **`generate_repo_list_markdown(repositories_data, config)`**: 処理済みのリポジトリデータのリスト(`repositories_data`)と設定(`config`)を元に、GitHub Pages用のリポジトリ一覧Markdownテキスト全体を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_name, owner, token, config)`**: 指定されたリポジトリ(`repo_name`, `owner`)から、設定(`config`)に基づいて`project-overview.md`の内容をフェッチし、プロジェクト概要の3行説明を抽出して返します。GitHubトークン(`token`)を使用します。
- **`src/generate_repo_list/repository_processor.py`**
    - **`process_repository(repo_raw_data, github_token, config)`**: GitHub APIから取得した生のリポジトリデータ(`repo_raw_data`)を受け取り、必要な情報を抽出し、整形・追加処理（例: 概要のフェッチ）を施した構造化されたリポジトリデータとして返します。GitHubトークン(`github_token`)と設定(`config`)を使用します。
- **`src/generate_repo_list/statistics_calculator.py`**
    - **`calculate_stats(repo_data)`**: リポジトリデータ(`repo_data`)からスター数、フォーク数などの統計情報を計算し、追加します。
- **`src/generate_repo_list/template_processor.py`**
    - **`render_template(template_content, context)`**: テンプレート文字列(`template_content`)とコンテキストデータ(`context`)を受け取り、テンプレートをレンダリングして最終的な文字列を生成します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-14 07:21:11 JST
