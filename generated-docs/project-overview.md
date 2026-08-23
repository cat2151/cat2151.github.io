Last updated: 2026-08-24

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成するシステムです。
- GitHub APIでリポジトリ情報を取得し、SEOを意識したMarkdownファイルを生成します。
- 検索エンジンやLLMからの参照性を向上させ、開発効率を高めることを目的とします。

## 技術スタック
- フロントエンド: **GitHub Pages (Jekyll)**: 生成されたMarkdownファイルをホストし、ウェブサイトとして公開するために使用されます。**Markdown**: システムによって生成されるコンテンツの形式。
- 音楽・オーディオ: 該当なし
- 開発ツール: **GitHub API**: リポジトリ情報の取得に使用されます。**pytest**: Pythonコードのテストフレームワーク。**ruff**: Pythonコードのリンター兼フォーマッター。
- テスト: **pytest**: ユニットテストおよび結合テストの実行に利用されます。
- ビルドツール: (直接的なビルドツールはPythonスクリプトですが、間接的にJekyllがサイトをビルドします) **Pythonスクリプト**: リポジトリ情報の取得、処理、Markdown生成の主要ロジックを担います。
- 言語機能: **Python**: プロジェクトの主要なプログラミング言語。**YAML**: 設定ファイル（`config.yml`, `strings.yml`など）の記述に利用されます。**TOML**: 設定ファイル（`ruff.toml`, `secrets.toml`など）の記述に利用されます。
- 自動化・CI/CD: **GitHub Actions**: プロジェクト情報では言及がありますが、このプロジェクトの目的である「自動生成」の実行環境としても機能すると考えられます（クイックテストの文脈で「CI/CD不要のローカル開発重視」とあり、直接的なCI/CDパイプラインではない可能性もあります）。
- 開発標準: **ruff**: コードスタイルの一貫性を保ち、品質を向上させるために使用されます。

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
- `README.md`: プロジェクトの概要、目的、設定方法、実行コマンド、ライセンスなど、プロジェクトに関する包括的な情報を提供する主要なドキュメント。
- `LICENSE`: 本プロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイル。
- `_config.yml`: Jekyllサイト全体の共通設定を定義するファイル。サイトのタイトル、テーマ、プラグインなどの構成が含まれる。
- `index.md`: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧が記述されたMarkdownファイル。GitHub Pagesサイトのトップページとして機能する。
- `pytest.ini`: Pythonのテストフレームワーク `pytest` の設定ファイル。テストの発見ルール、実行オプションなどを定義する。
- `requirements.txt`: プロジェクトの実行時に必要となるPythonライブラリとそのバージョンを列挙したファイル。
- `requirements-dev.txt`: 開発およびテスト時にのみ必要となるPythonライブラリとそのバージョンを列挙したファイル。
- `ruff.toml`: Pythonのコードリンター兼フォーマッター `ruff` の設定ファイル。コードスタイル、整形ルール、チェック項目などを定義する。
- `src/generate_repo_list/generate_repo_list.py`: 本プロジェクトのメインスクリプト。GitHub APIを介してリポジトリ情報を取得し、Markdown形式のリポジトリ一覧ファイルを生成する一連の処理を制御する。
- `src/generate_repo_list/config.yml`: プロジェクト概要の取得機能（有効/無効、対象ファイル、セクション名など）やAPIのリトライ設定など、本システムの技術的なパラメータを定義する設定ファイル。
- `src/generate_repo_list/strings.yml`: 生成されるMarkdownやログメッセージなど、システムが表示する各種文言やメッセージを一元管理するための設定ファイル。多言語対応や文言の変更が容易になる。
- `src/generate_repo_list/badge_generator.py`: リポジトリのプロパティ（例: 言語、ライセンス、ステータス）に基づいて表示用のバッジ画像を生成または参照するロジックを実装したモジュール。
- `src/generate_repo_list/config_manager.py`: `config.yml` や他の設定ファイルを読み込み、設定値にアクセスするためのインターフェースを提供するモジュール。
- `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を、人間が読みやすい形式や特定のフォーマット（例: ISO 8601）に変換するためのユーティリティ関数群。
- `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化 (SEO) のためにウェブページに埋め込むJSON-LD形式の構造化データテンプレート。リポジトリ情報に合わせたメタデータを生成する。
- `src/generate_repo_list/language_info.py`: GitHubリポジトリで使用されているプログラミング言語の情報を取得し、処理・分析するためのロジックを提供するモジュール。
- `src/generate_repo_list/markdown_generator.py`: 取得・整形されたリポジトリ情報を受け取り、Jekyllの要件に合わせたMarkdown形式のコンテンツを生成する主要なロジックを実装したモジュール。
- `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキスト（3行説明）を自動的に取得する機能を提供するモジュール。
- `src/generate_repo_list/readme_badge_extractor.py`: 各リポジトリのREADMEファイルから、既存のバッジ情報（Shields.ioなど）を検出・抽出するロジックを実装したモジュール。
- `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、Markdown生成に適した内部データ構造に整形・加工する主要なロジックを含むモジュール。
- `src/generate_repo_list/seo_template.yml`: SEO関連のメタデータ（キーワード、ディスクリプションなど）やテンプレートの構造を定義する設定ファイル。
- `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数、コミット数など、各種統計情報を計算または集計するロジックを提供するモジュール。
- `src/generate_repo_list/template_processor.py`: Markdown生成時に使用するテンプレートファイル（例: リポジトリごとの表示形式）を読み込み、データに基づいて埋め込む処理を行うモジュール。
- `src/generate_repo_list/url_utils.py`: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数を提供するモジュール。
- `tests/`: 本プロジェクトの各モジュールや機能の正確性を検証するためのテストコードが格納されているディレクトリ。
- `googled947dc864c270e07.html`: Google Search Consoleでサイトの所有権を確認するために配置される静的ファイル。

## 関数詳細説明
提供されたプロジェクト情報から具体的な関数の詳細（引数、戻り値、具体的な機能）を特定できませんでした。しかし、ファイル名とその役割から、主要な処理を担う関数が存在すると推測されます。以下にその推測される役割を示します。

- `src/generate_repo_list/generate_repo_list.py` 内の関数:
    - `main()`: スクリプトのエントリーポイントとして機能し、コマンドライン引数の解析、設定の読み込み、リポジトリ情報の取得、処理、そして最終的なMarkdownファイルの生成までの全体フローをオーケストレートします。
- `src/generate_repo_list/project_overview_fetcher.py` 内の関数:
    - `fetch_project_overview(repo_url, config)`: 指定されたGitHubリポジトリのURLから、`config.yml`で設定されたパスにある`project-overview.md`ファイルを読み込み、そこから「プロジェクト概要」セクションの3行説明を抽出し返却します。
- `src/generate_repo_list/markdown_generator.py` 内の関数:
    - `generate_repository_list_markdown(repositories_data)`: 処理済みリポジトリ情報のリストを受け取り、これらを基にJekyllが解釈できる形式のMarkdown文字列を生成します。各リポジトリの詳細（タイトル、説明、バッジなど）を組み込みます。
- `src/generate_repo_list/repository_processor.py` 内の関数:
    - `process_repository(repo_raw_data, config)`: GitHub APIから取得した生のリポジトリデータ（JSON形式）を受け取り、必要な情報を抽出し、整形、フィルタリングなどを行い、Markdown生成に適した構造化されたデータ形式に変換します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-08-24 07:05:34 JST
