Last updated: 2025-12-04

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト用のリポジトリ一覧を自動生成し、SEOとLLM参照性を向上させます。
- GitHub APIを利用してリポジトリ情報を取得し、JekyllベースのMarkdownファイルを生成します。
- アクティブ・アーカイブ・フォーク分類、バッジ表示、各リポジトリの概要自動取得など豊富な機能を提供します。

## 技術スタック
- フロントエンド: **GitHub Pages / Jekyll** (静的サイトのホスティング環境とサイトジェネレーター)、**Markdown** (コンテンツ記述形式)。生成されたファイルはGitHub Pages上でJekyllによって処理され、静的なウェブサイトとして公開されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: **Git** (バージョン管理システム)、**GitHub API** (リポジトリ情報の取得インターフェース)、**Python** (主要な開発言語およびスクリプト実行環境)。
- テスト: **pytest** (Python向けのテストフレームワーク)を使用し、コードの品質と信頼性を保証します。
- ビルドツール: **Python** スクリプト自体がリポジトリ一覧を生成するビルドプロセスを担います。
- 言語機能: **Python** (バージョン3.x系) がプロジェクトの核となるロジック実装に使用されています。**YAML** は設定ファイルや文字列定義に利用されています。
- 自動化・CI/CD: GitHub Pagesへのプッシュによる**Jekyll**の自動ビルドがサイト公開プロセスの一部となります。プロジェクト自体はローカル開発重視であり、このシステムを直接デプロイするCI/CDパイプラインは含まれません。
- 開発標準: **Ruff** (Pythonコードのフォーマッター兼Linter) を使用してコードスタイルを統一し、品質を維持します。**.editorconfig** ファイルにより、様々なエディタ間でのコーディングスタイルの一貫性を保ちます。

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
🌐 googled947dc864c270e07.html
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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理から特定のファイルやディレクトリを除外するための設定ファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）が記載されています。
- **`README.md`**: プロジェクトの目的、機能、使い方、設定、開発者向け情報などが記された、プロジェクトの玄関となるドキュメントです。
- **`_config.yml`**: GitHub PagesサイトのJekyll設定ファイルで、サイトのテーマやプラグイン、グローバル変数などを定義します。
- **`assets/`**: ウェブサイトで使用される静的リソース（画像、アイコンなど）を格納するディレクトリです。
    - **`favicon-*.png`**: ウェブサイトのファビコン（ブラウザのタブなどに表示される小さなアイコン）画像ファイルです。
- **`debug_project_overview.py`**: 各リポジトリからプロジェクト概要を自動取得する機能のデバッグ用途に特化したPythonスクリプトです。
- **`generated-docs/`**: 各リポジトリの `project-overview.md` など、このシステムが参照する生成済みドキュメントが配置される想定のディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどの検索エンジンツールで、ウェブサイトの所有権を確認するために配置されるファイルです。
- **`index.md`**: メインのPythonスクリプトによって自動生成されるMarkdownファイルで、GitHub Pagesサイトのトップページとしてリポジトリ一覧が表示されます。
- **`issue-notes/`**: 開発中に発生した課題や検討事項をメモとして記録するためのMarkdownファイル群が格納されています。
- **`manifest.json`**: プログレッシブウェブアプリ (PWA) としてウェブサイトを構成するための設定ファイルで、ホーム画面への追加やオフライン対応などを定義します。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を制御するための設定ファイルです。
- **`requirements-dev.txt`**: 開発環境やテスト環境で必要となるPythonパッケージとそのバージョンがリストアップされています。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonパッケージとそのバージョンがリストアップされています。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどのページをクロール・インデックスしてよいか、あるいは除外するかを指示するファイルです。
- **`ruff.toml`**: Pythonコードの整形（フォーマット）と静的解析（リンティング）ツールであるRuffの設定ファイルです。
- **`src/`**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **`__init__.py`**: `src` ディレクトリがPythonパッケージであることを示すファイルです。
    - **`generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを構成するモジュール群を格納するサブディレクトリです。
        - **`__init__.py`**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示すファイルです。
        - **`badge_generator.py`**: リポジトリの種類（アクティブ、アーカイブ、フォークなど）や言語に応じたバッジのMarkdownを生成する機能を提供します。
        - **`config.yml`**: プロジェクト概要取得機能の詳細設定（有効/無効、対象ファイルパス、リトライ回数など）を定義するYAML形式の設定ファイルです。
        - **`config_manager.py`**: YAML形式の設定ファイル（`config.yml` など）を読み込み、アプリケーション全体で設定値にアクセスするための管理機能を提供します。
        - **`generate_repo_list.py`**: このプロジェクトのメインとなる実行スクリプトです。GitHub APIからリポジトリ情報を取得し、Markdownを生成し、ファイルに書き出す一連の処理を統括します。
        - **`json_ld_template.json`**: 検索エンジン最適化 (SEO) のため、リッチスニペット表示などに利用される構造化データ (JSON-LD) のテンプレートファイルです。
        - **`language_info.py`**: 各リポジトリで使用されているプログラミング言語に関する情報を取得・処理するロジックを扱います。
        - **`markdown_generator.py`**: 取得・加工されたリポジトリデータをもとに、GitHub Pagesサイト用のMarkdownコンテンツを構築する中心的なモジュールです。
        - **`project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの3行概要を自動的に取得・抽出する機能を提供します。
        - **`repository_processor.py`**: GitHub APIを通じてユーザーのリポジトリ情報を取得し、それらをこのシステムで利用しやすい形に加工・整形する役割を担います。
        - **`seo_template.yml`**: サイトのメタディスクリプションやキーワードなど、SEOに関連するテンプレートや設定を定義するファイルです。
        - **`statistics_calculator.py`**: リポジトリ数、言語分布、更新頻度などの統計情報を計算する機能を提供します。
        - **`strings.yml`**: ユーザーインターフェースに表示されるメッセージや文言、ラベルなどを一元的に管理するためのYAML形式の設定ファイルです。
        - **`template_processor.py`**: Markdownなどのテンプレートファイルに動的なデータを埋め込み、最終的な出力を生成するテンプレートエンジン関連のロジックを提供します。
        - **`url_utils.py`**: GitHub APIエンドポイントやリポジトリURLの構築、検証など、URL関連のユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py` モジュールの機能が正しく動作するかを検証するための単体テストスクリプトです。
- **`tests/`**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    - **`test_config.py`**: `config_manager.py` など、設定ファイルの読み込み・管理機能に関するテストを行います。
    - **`test_environment.py`**: プログラムが動作する環境（例: 必要な依存関係がインストールされているか）に関するテストを行います。
    - **`test_integration.py`**: 複数のモジュールが連携して動作する際の整合性や機能を確認する統合テストを行います。
    - **`test_markdown_generator.py`**: `markdown_generator.py` モジュールが意図通りにMarkdownコンテンツを生成するかをテストします。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher.py` モジュールが正しくプロジェクト概要を抽出できるかをテストします。
    - **`test_repository_processor.py`**: `repository_processor.py` モジュールがGitHub APIからのデータを適切に処理するかをテストします。

## 関数詳細説明
- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: このスクリプトのエントリポイントです。コマンドライン引数の解析、GitHubからのリポジトリ情報取得、Markdownコンテンツの生成、そして最終的なファイルへの書き出しという一連の処理フロー全体を制御します。
    - `parse_arguments()`: コマンドラインから渡される引数（GitHubユーザー名、出力ファイル名、処理リミットなど）を解析し、後続の処理で利用できる形式で返します。
- **`src/generate_repo_list/repository_processor.py`**
    - `fetch_repositories(username, github_token, limit=None)`: 指定されたGitHubユーザー名とトークンを使用してGitHub APIを呼び出し、そのユーザーが所有する公開リポジトリのリストを取得します。`limit` オプションで取得数を制限できます。
    - `process_repository_data(repo_data)`: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を受け取り、このシステムが利用しやすいように必要な情報を抽出し、整形・加工して返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_markdown_output(repositories, config, strings)`: 整形されたリポジトリ情報のリスト、設定データ、および表示用の文字列データを受け取り、最終的なGitHub Pagesサイト用のMarkdownコンテンツ（リポジトリ一覧ページ）を生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_project_overview(repo_url, target_file, section_title, config)`: 指定されたリポジトリのURLから、`config.yml` で設定された特定のファイルパス（例: `generated-docs/project-overview.md`）の内容を取得します。そのファイルの中から、`section_title` で指定されたセクション（例: "プロジェクト概要"）の3行説明を抽出し、返します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path)`: 指定されたパスにあるYAML形式の設定ファイルを読み込み、Pythonの辞書オブジェクトとして内容を返します。
    - `get_setting(key_path, default=None)`: ロードされた設定データから、ドット区切りで指定されたキーパスに対応する設定値を取得します。値が見つからない場合に備えてデフォルト値を指定することも可能です。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge(status, language)`: リポジトリのステータス（例: アクティブ、アーカイブ、フォーク）や主要なプログラミング言語といった情報に基づいて、ウェブページに表示するためのバッジ（例: Markdown形式の画像リンク）を生成します。
- **`src/generate_repo_list/statistics_calculator.py`**
    - `calculate_repo_statistics(repositories)`: 処理されたリポジトリのリストを受け取り、リポジトリの総数、言語別の分布、更新頻度などの統計情報を計算して返します。
- **`src/generate_repo_list/template_processor.py`**
    - `render_template(template_content, data)`: プレースホルダーを含むテンプレート文字列と、それらのプレースホルダーを置き換えるためのデータ辞書を受け取り、最終的にデータが埋め込まれたコンテンツ文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**
    - `build_github_api_url(username, endpoint)`: GitHub APIのエンドポイントとユーザー名を用いて、特定のAPIリソースにアクセスするための完全なURLを構築します。
    - `normalize_url(url)`: 与えられたURL文字列を、特定の基準に従って整形またはクリーンアップします（例: 末尾のスラッシュの削除など）。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-04 07:06:46 JST
