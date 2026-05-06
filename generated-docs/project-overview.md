Last updated: 2026-05-07

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成し、サイトのSEOとLLMによる情報参照を改善します。
- GitHub APIを活用し、リポジトリ情報からSEO最適化されたMarkdownファイルを自動生成します。
- 各リポジトリの概要やバッジ、分類などを自動で抽出し、動的なポートフォリオサイトを構築します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として、生成されたMarkdownファイルを美しいウェブページに変換します。), Markdown (自動生成されるコンテンツの記述形式であり、JekyllによってHTMLにレンダリングされます。)
- 音楽・オーディオ: (このプロジェクトでは音楽・オーディオ関連の技術は使用していません。)
- 開発ツール: Python (リポジトリ情報の取得、処理、Markdown生成を行う主要なプログラミング言語です。), TOML (設定ファイル（`pytest.ini`, `ruff.toml`など）の記述に使用されるシンプルで人間が読みやすい形式です。), YAML (プロジェクト設定（`config.yml`, `strings.yml`など）やSEOテンプレートの記述に使用されるデータシリアライゼーション形式です。)
- テスト: Pytest (Pythonコードのユニットテストおよび統合テストを実行するためのフレームワークです。)
- ビルドツール: Markdown生成 (このプロジェクト自体はJekyllのようなビルドツールではありませんが、JekyllがGitHub Pagesサイトを構築する際のコンテンツ（Markdownファイル）を生成する役割を担います。)
- 言語機能: Python (スクリプトの作成、APIとの連携、データ処理、ファイル操作など、プロジェクトの全機能の中核を成すプログラミング言語です。)
- 自動化・CI/CD: `requirements.txt` (プロジェクトの実行に必要なPythonライブラリの依存関係を管理し、環境構築の自動化を支援します。)
- 開発標準: Ruff (Pythonコードのフォーマットとリンティングを自動的に行い、コード品質と一貫性を維持するためのツールです。)

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **.github_automation/**: GitHub Actions を用いた自動化スクリプトや関連設定を格納するディレクトリです。
  - **.github_automation/check_large_files/**: 大容量ファイルに関するチェック機能のコードと設定を保持します。
    - **.github_automation/check_large_files/README.md**: `check_large_files`機能の目的や使い方を説明するドキュメントです。
    - **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェック機能の閾値や対象ファイルなどの設定を定義します。
    - **.github_automation/check_large_files/scripts/**: スクリプトファイルを格納するディレクトリです。
      - **.github_automation/check_large_files/scripts/check_large_files.py**: 指定されたリポジトリ内で容量の大きいファイルを検出するためのPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを指定するファイルです。
- **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを明示し、利用条件を定めます。
- **README.md**: プロジェクトの目的、機能、セットアップ方法、実行手順など、プロジェクトの全体像と使用法を説明する主要なドキュメントです。
- **_config.yml**: JekyllベースのGitHub Pagesサイト全体の構成設定を定義するファイルです。サイトのタイトル、テーマ、プラグイン設定などが含まれます。
- **assets/**: GitHub Pagesサイトで利用される画像ファイルやアイコンなどの静的アセットを格納するディレクトリです。
  - **assets/favicon-16x16.png**, **assets/favicon-192x192.png**, **assets/favicon-32x32.png**, **assets/favicon-512x512.png**: ウェブサイトのブラウザタブやブックマークなどに表示されるファビコン（サイトアイコン）の異なるサイズを提供します。
- **debug_project_overview.py**: 各リポジトリからプロジェクト概要を自動取得する機能のデバッグやテストを目的としたスクリプトです。
- **generated-docs/**: 他のリポジトリから自動取得されたドキュメントや生成物の一時的な格納場所として機能するディレクトリです。
- **googled947dc864c270e07.html**: Google Search ConsoleでGitHub Pagesサイトの所有権を確認するために配置されたHTMLファイルです。
- **index.md**: `generate_repo_list.py`スクリプトによってリポジトリ一覧が自動生成され、GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。
- **issue-notes/**: 開発中に発生した課題や検討事項、メモなどを格納するためのディレクトリです。
  - **issue-notes/22.md**: 特定の課題（例: Issue #22）に関する詳細なメモや解決策が記述されたMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定を定義するファイルです。ホーム画面への追加、表示モード、アイコンなどの情報が含まれます。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作をカスタマイズするための設定ファイルです。
- **requirements-dev.txt**: 開発時およびテスト実行時にのみ必要となるPythonライブラリとそのバージョンをリストアップしたファイルです。
- **requirements.txt**: プロジェクトの実行に最低限必要なPythonライブラリとそのバージョンをリストアップしたファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、どのページを避けるべきかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター兼フォーマッターであるRuffの設定を定義するファイルです。コード規約や自動修正ルールなどを設定します。
- **src/**: プロジェクトの主要なPythonソースコードを格納するルートディレクトリです。
  - **src/__init__.py**: Pythonパッケージであることを示すファイルです。
  - **src/generate_repo_list/**: GitHub Pages向けリポジトリ一覧生成機能の主要なモジュール群を格納するディレクトリです。
    - **src/generate_repo_list/__init__.py**: Pythonパッケージであることを示すファイルです。
    - **src/generate_repo_list/badge_generator.py**: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成するロジックを実装しています。
    - **src/generate_repo_list/config.yml**: リポジトリ情報の取得（APIタイムアウト、リトライ回数）やプロジェクト概要機能の有効/無効、キャッシュ設定など、メイン機能の設定を定義します。
    - **src/generate_repo_list/config_manager.py**: 複数の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、プロジェクト全体で設定を一元的に管理する機能を提供します。
    - **src/generate_repo_list/date_formatter.py**: GitHub APIから取得した日付情報を、ユーザーフレンドリーな形式に整形するための機能を提供します。
    - **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdown形式でリポジトリ一覧を出力するプロジェクトのメイン実行スクリプトです。
    - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のために、リポジトリ情報をJSON-LD形式で構造化データとして埋め込むためのテンプレートファイルです。
    - **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示可能な形式に整形する機能を提供します。
    - **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報や統計データ、バッジなどを用いて、最終的なMarkdownコンテンツを構築するロジックを実装しています。
    - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に取得する機能を提供します。
    - **src/generate_repo_list/readme_badge_extractor.py**: 各リポジトリのREADMEファイルから、既存のバッジ情報（例: ビルドステータス、カバレッジ）を抽出する機能を提供します。
    - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを整形し、Markdown生成に適した形式に加工する役割を担います。
    - **src/generate_repo_list/seo_template.yml**: 各リポジトリのリンクや説明文など、検索エンジンからの評価を高めるためのSEO関連のテンプレート設定を定義します。
    - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算し、表示に利用する機能を提供します。
    - **src/generate_repo_list/strings.yml**: UIメッセージ、ラベル、案内文など、表示されるあらゆる文字列を一元管理し、国際化対応を容易にします。
    - **src/generate_repo_list/template_processor.py**: Markdown生成時に使用されるテンプレートを処理し、動的なデータを埋め込む機能を提供します。
    - **src/generate_repo_list/url_utils.py**: URLの検証、構築、変換など、URLに関連するユーティリティ関数を集約したモジュールです。
- **test_project_overview.py**: `project_overview_fetcher.py`で実装されているプロジェクト概要自動取得機能のテストケースを記述したスクリプトです。
- **tests/**: プロジェクト全体のテストケースを格納するディレクトリです。
  - **tests/conftest.py**: pytestのテスト実行時に共有されるフィクスチャやヘルパー関数を定義するファイルです。
  - **tests/test_badge_generator_integration.py**: `badge_generator.py`の機能が他のモジュールと連携して正しく動作するかを確認する統合テストです。
  - **tests/test_check_large_files.py**: 大容量ファイル検出スクリプトの正確性を検証するテストです。
  - **tests/test_config.py**: 設定ファイルの読み込みや管理を行う`config_manager.py`の機能が正しく動作するかを検証するテストです。
  - **tests/test_date_formatter.py**: 日付整形機能の正確性を検証するテストです。
  - **tests/test_environment.py**: 開発環境や実行環境が適切に設定されているかを確認するテストです。
  - **tests/test_integration.py**: プロジェクトの主要なコンポーネントが連携して期待通りに動作するかを検証する包括的な統合テストです。
  - **tests/test_markdown_generator.py**: `markdown_generator.py`が正しいMarkdownコンテンツを生成するかを検証するテストです。
  - **tests/test_project_overview_fetcher.py**: `project_overview_fetcher.py`が正しくプロジェクト概要を取得できるかを検証するテストです。
  - **tests/test_readme_badge_extractor.py**: `readme_badge_extractor.py`がREADMEからバッジ情報を正確に抽出できるかを検証するテストです。
  - **tests/test_repository_processor.py**: `repository_processor.py`がGitHubリポジトリ情報を正しく処理・整形できるかを検証するテストです。

## 関数詳細説明
提供されたプロジェクト情報には、個々の関数名、引数、戻り値に関する具体的な詳細が含まれていません。ハルシネーションを避けるため、ここでは具体的な関数名やシグネチャについては説明を省略します。ただし、上記「ファイル詳細説明」に記載されている各ファイルの役割と機能が、それぞれ内部の関数として実装されていると推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-05-07 07:20:35 JST
