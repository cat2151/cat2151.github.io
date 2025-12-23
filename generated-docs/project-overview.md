Last updated: 2025-12-24

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧を自動生成するシステムです。
- GitHub APIからリポジトリ情報を取得し、SEO最適化されたJekyll対応Markdownを作成します。
- これにより、リポジトリの検索エンジンでの可視性と、LLMによる参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの表示エンジンとして利用されるフレームワーク), Markdown (生成されるコンテンツのフォーマット)
- 音楽・オーディオ: 該当なし
- 開発ツール:
    - pip: Pythonパッケージ管理ツール
    - pytest: Pythonのテストフレームワーク
    - ruff: Pythonコードのリンティングおよびフォーマットツール
- テスト: pytest (ユニットテスト、結合テスト、統合テストの実行に使用)
- ビルドツール: Python (スクリプトの実行環境として、またリポジトリ情報を処理しMarkdownを生成する主要な言語)
- 言語機能: Python (スクリプト開発の基盤言語)
- 自動化・CI/CD: GitHub Actions (生成されたMarkdownが最終的にデプロイされるGitHub Pagesのホスティング環境で利用される可能性を考慮し、システム自体はローカル実行だが間接的に関連)
- 開発標準:
    - ruff: コードスタイルの一貫性を保つためのルール設定
    - .editorconfig: 異なるエディタやIDE間で一貫したコードスタイルを維持するための設定

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
- **.editorconfig**: 異なるエディタやIDE間でコードのインデント、エンコーディングなどの基本的なフォーマットルールを統一するための設定ファイルです。
- **.gitignore**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **LICENSE**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
- **README.md**: プロジェクトの概要、目的、機能、使用方法、設定、ライセンスなど、このリポジトリに関する基本的な情報が記載されたメインドキュメントです。
- **_config.yml**: Jekyllサイト全体の構成や設定を定義するファイルです。GitHub Pagesのビルド時に利用されます。
- **assets/**: Webサイトで使用される画像、アイコン（ファビコン）、その他の静的アセットが格納されるディレクトリです。
- **debug_project_overview.py**: `project_overview`機能のデバッグ目的で使用されるスクリプトです。
- **generated-docs/**: 他のリポジトリから自動取得されたプロジェクト概要などのドキュメントを一時的、あるいはキャッシュとして格納するためのプレースホルダーディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために配置されるHTMLファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによって生成される、リポジトリ一覧が記述されたメインのMarkdownファイルです。GitHub Pagesのルートページとして機能します。
- **issue-notes/**: プロジェクト開発中に発生した課題や検討事項、メモなどをMarkdown形式で記録しているディレクトリです。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリの名前、アイコン、表示方法などを定義する設定ファイルです。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の挙動をカスタマイズするための設定ファイルです。
- **requirements-dev.txt**: 開発環境およびテスト実行に必要なPythonライブラリとそのバージョンが記述されています。
- **requirements.txt**: プロジェクトの実行（本番環境）に必要なPythonライブラリとそのバージョンが記述されています。
- **robots.txt**: 検索エンジンのクローラーに対して、Webサイトのどの部分をクロールしてもよいか、あるいはクロールしてはいけないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンティング（構文チェック）とフォーマットを行う`ruff`ツールの設定ファイルです。
- **src/__init__.py**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや技術を示すバッジ画像を生成するロジックを含むモジュールです。
- **src/generate_repo_list/config.yml**: プロジェクト概要の取得設定など、システム固有の技術的パラメータを定義するYAML形式の設定ファイルです。
- **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`など）を読み込み、管理するためのユーティリティモジュールです。
- **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdown形式のリポジトリ一覧を生成する一連の処理を実行します。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイルです。
- **src/generate_repo_list/language_info.py**: リポジトリの使用言語情報を処理し、表示に適した形式に変換するロジックを含むモジュールです。
- **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll互換のMarkdownコンテンツを生成するロジックを含むモジュールです。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動取得する機能を提供するモジュールです。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形するロジックを含むモジュールです。
- **src/generate_repo_list/seo_template.yml**: 検索エンジン最適化（SEO）に関連する表示文言やメタデータなどのテンプレート設定を定義するファイルです。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数などの統計情報を計算するロジックを含むモジュールです。
- **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、その他の静的テキストを一元管理するためのYAML形式のファイルです。
- **src/generate_repo_list/template_processor.py**: Markdown生成の際に利用されるテンプレートを処理し、動的なデータを埋め込む機能を提供するモジュールです。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、検証など、URL関連のユーティリティ関数を提供するモジュールです。
- **test_project_overview.py**: `project_overview`機能の単体テストまたは統合テストを含むスクリプトです。
- **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
- **tests/test_config.py**: `config_manager`など、設定関連のモジュールに対するテストスクリプトです。
- **tests/test_environment.py**: 実行環境のセットアップや依存関係の確認に関するテストスクリプトです。
- **tests/test_integration.py**: 複数のモジュールが連携して動作する際の結合テストを含むスクリプトです。
- **tests/test_markdown_generator.py**: `markdown_generator`モジュールが正しくMarkdownコンテンツを生成するかを検証するテストスクリプトです。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher`モジュールが正しくプロジェクト概要を取得できるかを検証するテストスクリプトです。
- **tests/test_repository_processor.py**: `repository_processor`モジュールがリポジトリ情報を正しく処理できるかを検証するテストスクリプトです。

## 関数詳細説明
プロジェクト情報に具体的な関数の詳細（関数名、引数、戻り値、機能説明）が提供されていないため、このセクションを生成できません。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-24 07:06:42 JST
