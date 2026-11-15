Last updated: 2026-11-16

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動的に取得します。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧と詳細Markdownファイルを生成します。
- これにより、リポジトリの検索エンジンでの発見性を高め、LLMによる参照失敗の課題を緩和します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤として使用され、MarkdownファイルをHTMLサイトに変換します。
    - **Markdown**: 生成されるリポジトリ一覧のコンテンツフォーマット。SEO最適化を意識した構造で出力されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **GitHub API**: リポジトリ情報（説明、言語、星の数など）をプログラムで取得するための主要なインターフェースです。
    - **Git**: バージョン管理システム。プロジェクトのソースコード管理に使用されます。
    - **VS Code**: （推測）高機能なコードエディタとして開発に利用されている可能性があります。
- テスト:
    - **pytest**: Pythonのテスティングフレームワーク。プロジェクトの機能が期待通りに動作するかを検証するために使用されます。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py`が、リポジトリ情報の取得からMarkdownファイル生成までの一連の処理を実行するスクリプトとして機能します。
    - **Jekyll**: GitHub Pages側で最終的なウェブサイトのビルドを行います。
- 言語機能:
    - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報の取得とMarkdown生成ロジックを実装しています。
    - **YAML**: `config.yml`や`strings.yml`など、設定ファイルや多言語対応の文言管理に使用されます。
    - **TOML**: `secrets/secrets.toml`でGitHubトークンなどの機密情報を安全に管理するために使用されます。
- 自動化・CI/CD:
    - **GitHub Actions**: (`.github_automation`ディレクトリから推測) GitHub上でのワークフロー自動化に利用され、コードの品質チェックやデプロイプロセスの自動化に貢献している可能性があります。
- 開発標準:
    - **Ruff**: Pythonコードのリンティングとフォーマットを自動的に行うツール。一貫したコードスタイルを維持し、コード品質を向上させます。
    - **EditorConfig**: 異なるエディタやIDE間でコーディングスタイル（インデント、改行など）を統一するためのファイルフォーマットです。

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
- **`.editorconfig`**: 異なる開発環境（エディタ、IDE）間でコーディングスタイル（インデント、文字コードなど）を統一するための設定ファイルです。
- **`.github_automation/check_large_files/README.md`**: `.github_automation/check_large_files`ディレクトリの目的や使用方法を説明するドキュメントです。
- **`.github_automation/check_large_files/check-large-files.toml`**: 大きなファイルのチェック機能に関する設定ファイルです。
- **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きなファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクト全体の概要、目的、使い方、主な機能などを説明する主要なドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバルな設定ファイルです。サイトのタイトル、テーマ、プラグインなどが定義されます。
- **`assets/`**: サイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各サイズが含まれます。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグ目的で使用されるスクリプトです。
- **`generated-docs/`**: 自動生成されたドキュメントやデータが配置されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのサイト所有権確認に使用されるHTMLファイルです。
- **`index.md`**: メインのMarkdownファイルで、通常は生成されたリポジトリ一覧が出力されるエントリーポイントとなります。
- **`issue-notes/22.md`**: 特定のイシュー（ここではイシュー番号22）に関するメモや詳細情報が記述されているMarkdownファイルです。
- **`manifest.json`**: ウェブアプリケーションマニフェストファイル。プログレッシブウェブアプリ（PWA）の機能やインストール時の動作を定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの設定ファイルです。テストの検出ルールやオプションを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト環境でのみ必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: プロジェクトの本番環境で必要なPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、どのページをクロールすべきでないかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正に関する設定を定義します。
- **`src/__init__.py`**: `src`ディレクトリをPythonパッケージとして認識させるためのファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータスや技術を示すバッジ画像を生成するロジックを実装しています。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの技術的なパラメータや全体設定を定義するYAMLファイルです。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`などの設定ファイルを読み込み、管理するためのロジックを実装しています。
- **`src/generate_repo_list/date_formatter.py`**: 日付や時刻のフォーマット変換に関する機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成する一連の処理をオーケストレーションします。
- **`src/generate_repo_list/json_ld_template.json`**: SEO最適化のためのJSON-LD（構造化データ）のテンプレートです。
- **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語情報などを処理・整形するロジックを実装しています。
- **`src/generate_repo_list/markdown_generator.py`**: 取得したリポジトリ情報から、SEO最適化されたMarkdown形式のコンテンツを生成する機能を提供します。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を自動取得するロジックを実装しています。
- **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから特定のバッジ情報を抽出する機能です。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形し、後続の処理で扱いやすい形式に変換する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタ情報やテンプレートを定義するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する統計情報（星の数、フォーク数など）を計算する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: サイトで表示されるメッセージや文言を管理するためのYAMLファイルです。多言語対応や文言の一元管理に利用されます。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成などで使用されるテンプレートを処理し、動的なデータを埋め込む機能を提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供します。
- **`test_project_overview.py`**: プロジェクト概要取得機能に関する単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
    - **`tests/conftest.py`**: pytestのフィクスチャやヘルパー関数を定義し、複数のテストファイルで共有するためのファイルです。
    - **`tests/test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`tests/test_check_large_files.py`**: 大きなファイルチェック機能のテストです。
    - **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストです。
    - **`tests/test_date_formatter.py`**: 日付フォーマット機能のテストです。
    - **`tests/test_environment.py`**: 実行環境に関するテストです。
    - **`tests/test_integration.py`**: プロジェクトの主要機能間の統合テストです。
    - **`tests/test_markdown_generator.py`**: Markdown生成機能のテストです。
    - **`tests/test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`tests/test_readme_badge_extractor.py`**: READMEバッジ抽出機能のテストです。
    - **`tests/test_repository_processor.py`**: リポジトリデータ処理機能のテストです。

## 関数詳細説明
提供されたプロジェクト情報からは、個々の関数の具体的な引数、戻り値、詳細なロジックまでは分析できませんでした。しかし、各ファイル名から推測される役割に基づき、以下の通り一般的な説明を提供します。

- **`src/generate_repo_list/generate_repo_list.py`内の関数**:
    - **役割**: GitHub APIとの連携、リポジトリ情報の取得、取得したデータを処理してMarkdownコンテンツを生成し、指定されたファイルに出力する一連のメイン処理を調整します。
    - **機能**: コマンドライン引数の解析、設定の読み込み、他のモジュールの関数呼び出しによるデータフローの制御などが含まれると推測されます。
- **`src/generate_repo_list/badge_generator.py`内の関数**:
    - **役割**: 各リポジトリの言語やステータス（アーカイブ、フォークなど）に応じたバッジ（例: Shield.io形式）を生成します。
    - **機能**: 言語名やプロパティに基づいてバッジのテキスト、色、リンクなどを決定し、Markdown形式のバッジ文字列を返すことが考えられます。
- **`src/generate_repo_list/config_manager.py`内の関数**:
    - **役割**: `config.yml`などの設定ファイルを読み込み、アプリケーション内で利用可能なPythonオブジェクトに変換し、設定値へのアクセスを提供します。
    - **機能**: YAMLファイルのパース、デフォルト値の設定、設定値のバリデーションなどが含まれると推測されます。
- **`src/generate_repo_list/date_formatter.py`内の関数**:
    - **役割**: GitHub APIから取得される日付文字列（例: ISO 8601形式）を、ユーザーフレンドリーな形式やJekyllが扱いやすい形式に変換します。
    - **機能**: 日付のパース、指定されたフォーマット文字列への変換などが考えられます。
- **`src/generate_repo_list/markdown_generator.py`内の関数**:
    - **役割**: 処理されたリポジトリデータを受け取り、Jekyllの要件やSEOのベストプラクティスに沿ったMarkdown形式のコンテンツを生成します。
    - **機能**: リポジトリごとの情報の整形、Markdownの構文（ヘッダー、リスト、リンクなど）の構築、テンプレートへのデータ挿入などが含まれます。
- **`src/generate_repo_list/project_overview_fetcher.py`内の関数**:
    - **役割**: 各リポジトリ内の特定のパス（例: `generated-docs/project-overview.md`）から「プロジェクト概要」セクションの3行説明を抽出し、取得します。
    - **機能**: GitHub APIを利用したファイル内容のフェッチ、Markdownコンテンツの解析、指定されたセクションからのテキスト抽出などが含まれると推測されます。
- **`src/generate_repo_list/repository_processor.py`内の関数**:
    - **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーションの他の部分で扱いやすい形式（例: カスタムオブジェクトや辞書）に変換し、必要な情報を抽出・整形します。
    - **機能**: データのフィルタリング（例: アーカイブ、フォークの分類）、特定のフィールドの抽出、URLの生成などが含まれます。
- **`src/generate_repo_list/statistics_calculator.py`内の関数**:
    - **役割**: リポジトリの星の数、フォーク数、最終更新日などの統計情報を計算または集計します。
    - **機能**: リポジトリリスト全体の統計集計、個々のリポジトリプロパティの数値処理などが考えられます。
- **`src/generate_repo_list/template_processor.py`内の関数**:
    - **役割**: Markdownやその他のテキストコンテンツを生成する際に、動的なデータをテンプレートに埋め込むための処理を行います。
    - **機能**: プレースホルダーの置換、条件分岐、ループ処理など、シンプルなテンプレートエンジンの機能を提供することが考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-11-16 07:07:08 JST
