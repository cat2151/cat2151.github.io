Last updated: 2026-11-25

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、GitHubリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll対応のMarkdownファイルを生成します。
- 検索エンジンからの発見性を高め、各リポジトリの概要を一覧で表示し、アクセス性を向上させます。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyllベース)** (生成されるリポジトリ一覧サイトのホスティング環境、Markdownから静的サイトを生成), **Markdown** (リポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Python** (主要なスクリプト言語), **GitHub API** (リポジトリ情報取得元), **PyYAML** (YAML設定ファイルの解析), **requests** (HTTPリクエストライブラリ), **toml** (TOML設定ファイルの解析)
- テスト: **pytest** (Pythonコードのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (`generate_repo_list.py` が主要なリポジトリ一覧生成処理を実行)
- 言語機能: **Python** (汎用プログラミング言語としてプロジェクト全体で使用)
- 自動化・CI/CD: **GitHub Actions** (プロジェクト概要にて言及されており、将来的または部分的に自動化ワークフローで活用される可能性), **シェルスクリプト** (Pythonスクリプトの実行など)
- 開発標準: **ruff** (Pythonコードのリンターおよびフォーマッター), **.editorconfig** (エディタ間のコードスタイル統一設定)

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
- **.editorconfig**: 異なる開発環境間でのコーディングスタイルの一貫性を保つための設定ファイル。
- **.github_automation/**: GitHub関連の自動化スクリプトや設定をまとめるディレクトリ。
    - **check_large_files/**: Gitリポジトリ内の大容量ファイルを検出するための機能群。
        - **README.md**: `check_large_files` 機能の説明ドキュメント。
        - **check-large-files.toml**: 大容量ファイル検出機能の具体的な設定（閾値など）。
        - **scripts/**: `check_large_files` の実行スクリプトを格納。
            - **check_large_files.py**: 大容量ファイルを識別し、警告するためのPythonスクリプト。
- **.gitignore**: Gitのバージョン管理から除外すべきファイルやディレクトリを指定する設定ファイル。
- **LICENSE**: 本プロジェクトがMITライセンスで公開されていることを示すライセンス情報ファイル。
- **README.md**: プロジェクトの目的、主要機能、設定方法、実行方法など、全体概要を説明する主要ドキュメント。
- **_config.yml**: Jekyll (GitHub Pages) サイト全体の構成設定を定義するファイル。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的リソースを格納するディレクトリ。
    - **favicon-*.png**: Webサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズ。
- **debug_project_overview.py**: プロジェクト概要取得機能 (`project_overview_fetcher`) のデバッグや個別の動作確認に使用されるスクリプト。
- **generated-docs/**: 何らかの生成物（ドキュメントなど）を一時的に格納するためのディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイト所有権の確認に使用される検証ファイル。
- **index.md**: GitHub Pagesサイトのトップページとして機能するMarkdownファイル。生成されたリポジトリ一覧が出力される。
- **issue-notes/**: 開発中に発生した課題やメモを記録するためのディレクトリ。
    - **22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや解決策の検討が記述されたファイル。
- **manifest.json**: Webアプリマニフェスト。PWA（プログレッシブウェブアプリ）の動作に必要なメタデータ（ホーム画面アイコン、表示モードなど）を定義。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの設定ファイル。テストの実行オプションやパスなどを指定。
- **requirements-dev.txt**: 開発時およびテスト時に必要となるPythonライブラリとそのバージョンを定義するファイル。
- **requirements.txt**: プロジェクトの本番稼働に最低限必要なPythonライブラリとそのバージョンを定義するファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいは避けるべきかを指示するファイル。
- **ruff.toml**: Pythonコードの静的解析ツール/フォーマッターであるRuffの設定ファイル。コードスタイルルールやエラー検出ルールを定義。
- **src/**: プロジェクトの主要なソースコードが格納されるディレクトリ。
    - **__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるためのファイル。
    - **generate_repo_list/**: リポジトリ一覧を生成する機能の中核をなすPythonパッケージ。
        - **__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるためのファイル。
        - **badge_generator.py**: リポジトリの言語やステータスを示すバッジ画像を生成するロジックを実装したモジュール。
        - **config.yml**: `generate_repo_list` パッケージ特有の技術的パラメータ（例: プロジェクト概要取得設定）を定義する設定ファイル。
        - **config_manager.py**: `config.yml` や `strings.yml` などの設定ファイルを読み込み、管理するためのモジュール。
        - **date_formatter.py**: 日付や時刻データをユーザーフレンドリーな形式に変換するためのユーティリティモジュール。
        - **generate_repo_list.py**: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIから情報を取得し、最終的なMarkdownファイルを生成する。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ (JSON-LD) のテンプレートを定義するファイル。
        - **language_info.py**: GitHubリポジトリの言語情報を解析し、利用しやすい形式で提供するモジュール。
        - **markdown_generator.py**: 取得・整形されたリポジトリ情報から、Jekyll互換のMarkdownコンテンツを生成するロジックを実装。
        - **project_overview_fetcher.py**: 各リポジトリの特定のファイルからプロジェクト概要を自動的に抽出し、取得するモジュール。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから既存のバッジ情報を抽出し、再利用するためのモジュール。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを処理し、必要な情報に整形・加工するモジュール。
        - **seo_template.yml**: SEOを強化するためのメタデータや構造化データのテンプレート設定を定義するファイル。
        - **statistics_calculator.py**: リポジトリのスター数やフォーク数などの統計情報を計算し、整形するモジュール。
        - **strings.yml**: UI表示テキストやエラーメッセージなど、各種文言を一元管理するための設定ファイル。
        - **template_processor.py**: Markdown生成時に使用するテンプレートファイルを読み込み、データに基づいて埋め込み処理を行うモジュール。
        - **url_utils.py**: URLの生成、解析、検証など、URL関連のユーティリティ機能を提供するモジュール。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールの単体テストを記述したファイル。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
    - **conftest.py**: pytestのフィクスチャ（テストヘルパー関数など）を定義し、複数のテストファイルで共有するためのファイル。
    - **test_badge_generator_integration.py**: `badge_generator` モジュールの機能が期待通りに連携するかを確認する統合テスト。
    - **test_check_large_files.py**: 大容量ファイル検出スクリプト (`check_large_files.py`) のテスト。
    - **test_config.py**: 設定ファイルの読み込みや管理を行うモジュール (`config_manager.py`) のテスト。
    - **test_date_formatter.py**: `date_formatter` モジュールのテスト。
    - **test_environment.py**: 開発環境や実行環境のセットアップが正しく行われているかを検証するテスト。
    - **test_integration.py**: プロジェクトの主要な機能がエンドツーエンドで正しく動作するかを確認する統合テスト。
    - **test_markdown_generator.py**: `markdown_generator` モジュールのテスト。
    - **test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールのテスト。
    - **test_readme_badge_extractor.py**: `readme_badge_extractor` モジュールのテスト。
    - **test_repository_processor.py**: `repository_processor` モジュールのテスト。

## 関数詳細説明
提供された情報からは、プロジェクト内の具体的な関数名とその詳細を特定できませんでした。しかし、各Pythonファイル（例: `badge_generator.py`, `generate_repo_list.py` など）が特定の機能を持つモジュールとして設計されており、内部的に複数の関数が連携して動作すると考えられます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-11-25 07:07:54 JST
