Last updated: 2026-01-28

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・処理するシステムです。
- 取得した情報から、GitHub Pages向けにSEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- これにより、検索エンジンへのインデックスを促進し、LLMによるリポジトリ参照の精度向上に貢献します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: 生成されたMarkdownファイルがデプロイされるGitHub Pagesの基盤技術。静的サイトジェネレーターとして機能します。
    - **Markdown**: 生成されるリポジトリ一覧ページの記述形式。人間が読みやすく、Webページとしても表示しやすい軽量マークアップ言語です。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語。リポジトリ情報の取得、処理、Markdown生成など、全てのロジックを担います。
    - **GitHub API**: リポジトリ情報の取得に利用する、GitHubが提供するRESTful API。
    - **YAML**: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）の記述形式。構造化されたデータを人間が読みやすい形式で定義します。
- テスト:
    - **pytest**: Python用のテストフレームワーク。コードの品質と信頼性を確保するための単体テストおよび統合テストに使用されます。
- ビルドツール:
    - **Pythonスクリプト**: 専用のビルドツールは使用せず、Pythonスクリプト（`generate_repo_list.py`）自体がリポジトリ情報の取得からMarkdown生成までの一連の処理を実行します。
- 言語機能:
    - **Python**: オブジェクト指向プログラミング、標準ライブラリ（HTTP通信、ファイルI/Oなど）、データ構造（辞書、リスト）などを活用し、スクリプトのロジックを構築しています。
- 自動化・CI/CD: 本プロジェクトは「CI/CD不要のローカル開発重視」とされており、専用の自動化・CI/CDツールは導入されていません。
- 開発標準:
    - **ruff**: Pythonコードのリンターおよびフォーマッター。コードのスタイルを自動的に修正し、品質と一貫性を保ちます。
    - **.editorconfig**: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。

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
  📖 16.md
  📖 18.md
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
  📄 test_badge_generator_integration.py
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
- **.editorconfig**: さまざまなエディタやIDE間で、インデントスタイル、文字エンコーディングなどの基本的なコーディングスタイルを統一するための設定ファイルです。
- **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。一時ファイルやログ、生成物などが含まれます。
- **LICENSE**: 本プロジェクトのライセンス情報（MITライセンス）が記述されており、利用条件や配布に関する権利を示します。
- **README.md**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、ライセンス情報など、プロジェクト全体に関する説明が記載されています。
- **_config.yml**: Jekyllサイトのグローバル設定ファイルです。サイトのタイトル、テーマ、プラグインなどの設定が含まれます。
- **assets/**: Webサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリです。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 異なるサイズで提供されるWebサイトのファビコン画像です。
- **debug_project_overview.py**: `project_overview_fetcher`モジュールからプロジェクト概要をデバッグ目的で取得・表示するための補助スクリプトです。
- **generated-docs/**: プロジェクト外のリポジトリが生成したドキュメントを配置する際に想定されるディレクトリです。このプロジェクト自身は、このディレクトリ内の`project-overview.md`ファイルを読み込む側にあります。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **index.md**: GitHub PagesサイトのルートページとなるMarkdownファイルです。このプロジェクトによってリポジトリ一覧が自動生成され、ここに書き込まれます。
- **issue-notes/**: 開発中に発生した課題や検討事項に関するメモをMarkdown形式で記録したファイル群です。
- **manifest.json**: Progressive Web App (PWA) の設定ファイルです。ホーム画面に追加される際のアイコン、表示名、表示モードなどを定義します。
- **pytest.ini**: pytestフレームワークの実行に関する設定ファイルです。テストの発見ルールやオプションなどが定義されます。
- **requirements-dev.txt**: 開発環境およびテストに必要なPythonパッケージの依存関係を記述したファイルです。
- **requirements.txt**: プロジェクトを本番環境で実行するために必要なPythonパッケージの依存関係を記述したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールすべきか、あるいはすべきでないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや除外設定などが記述されます。
- **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    - **src/__init__.py**: `src`ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **src/generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージです。
        - **src/generate_repo_list/__init__.py**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
        - **src/generate_repo_list/badge_generator.py**: リポジトリの言語やスター数などの情報を基に、Web上で表示するバッジ（例: Shields.io形式）を生成するロジックを扱います。
        - **src/generate_repo_list/config.yml**: プロジェクトの技術的な設定パラメータを定義するファイルです。特にプロジェクト概要取得機能に関する設定などが含まれます。
        - **src/generate_repo_list/config_manager.py**: YAML形式の設定ファイル（`config.yml`, `strings.yml`など）を読み込み、アプリケーション内で利用しやすい形式で管理するモジュールです。
        - **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を特定のフォーマット（例: ISO 8601、人間が読みやすい形式）に変換するためのユーティリティ関数を提供します。
        - **src/generate_repo_list/generate_repo_list.py**: プロジェクトのメイン実行スクリプトです。GitHub APIからのリポジトリ情報取得、データの加工、Markdownファイルの生成といった一連の処理を orchestrate します。
        - **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化 (SEO) のため、構造化データ（JSON-LD）を生成する際のテンプレートとして使用されます。
        - **src/generate_repo_list/language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に適した形式に整形するロジックを提供します。
        - **src/generate_repo_list/markdown_generator.py**: 処理されたリポジトリ情報を受け取り、最終的なリポジトリ一覧のMarkdownコンテンツを生成する主要なロジックを担います。
        - **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を取得し、その中から「プロジェクト概要」セクションの3行説明を抽出する機能を提供します。
        - **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、プロジェクトの状態を示すバッジ（例: ビルドステータス、カバレッジなど）の情報を解析し抽出するロジックです。
        - **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータ（JSON形式など）を、アプリケーション内で扱いやすいデータ構造に加工・整形する役割を担います。
        - **src/generate_repo_list/seo_template.yml**: サイトのメタデータやOGP (Open Graph Protocol) 設定など、検索エンジン最適化（SEO）に関連するテンプレートや設定を定義します。
        - **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算・集計するロジックを提供します。
        - **src/generate_repo_list/strings.yml**: UIに表示されるメッセージ、ラベル、説明文などの静的な文字列を管理する設定ファイルです。国際化対応の基盤にもなり得ます。
        - **src/generate_repo_list/template_processor.py**: Markdownのテンプレートファイルに、動的に生成されたデータを挿入して最終的なコンテンツを生成する処理を担います。
        - **src/generate_repo_list/url_utils.py**: URLの構築、検証、パスの結合など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher`モジュール（プロジェクト概要取得機能）の単体テストまたは結合テストを記述したファイルです。
- **tests/**: pytestフレームワークによる各種テストコードを格納するディレクトリです。
    - `test_badge_generator_integration.py`: `badge_generator`モジュールの統合テスト。バッジ生成が期待通りに機能するかを確認します。
    - `test_config.py`: `config_manager`モジュールや各種設定ファイルの読み込み、解析が正しく行われるかをテストします。
    - `test_date_formatter.py`: `date_formatter`モジュールの日付フォーマット機能が正しく動作するかをテストします。
    - `test_environment.py`: テスト実行環境の設定や依存関係が正しくセットアップされているかを確認するテストです。
    - `test_integration.py`: 主要なモジュール間の連携を含む、プロジェクト全体の重要なフローの統合テストです。
    - `test_markdown_generator.py`: `markdown_generator`モジュールが正しいMarkdown形式の出力を生成するかをテストします。
    - `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールが外部リポジトリから概要を正確に取得・抽出できるかをテストします。
    - `test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正しく抽出できるかをテストします。
    - `test_repository_processor.py`: `repository_processor`モジュールがGitHub APIレスポンスを正しく処理・整形できるかをテストします。

## 関数詳細説明
このプロジェクトでは、各Pythonファイルが特定の役割を担う関数群を提供しています。具体的な関数シグネチャは提供されていませんが、各モジュールの機能に基づき、以下の種類の関数が含まれていると推測されます。

- **`badge_generator.py`**:
    - バッジ情報を入力として、SVG形式のバッジURLを生成する関数。
    - 特定のバッジ（例：言語、スター数）のデータを整形し、生成ロジックに渡す関数。
- **`config_manager.py`**:
    - YAMLファイルを読み込み、辞書形式で設定データを返す関数。
    - 特定の設定キーに基づいて値を安全に取得する関数。
- **`date_formatter.py`**:
    - 日付オブジェクトまたは日付文字列を受け取り、指定されたフォーマットの文字列に変換する関数。
    - GitHub APIから取得したタイムスタンプを人間が読みやすい形式に整形する関数。
- **`generate_repo_list.py`**:
    - メインエントリポイントとなる関数（例: `main()`）。コマンドライン引数を解析し、一連の処理フローを制御します。
    - GitHub APIからリポジトリ一覧を取得する関数。
    - 各リポジトリデータを処理し、Markdown生成モジュールに渡す関数。
- **`language_info.py`**:
    - リポジトリの言語使用率データを受け取り、主要言語を特定したり、表示用の情報を整形する関数。
- **`markdown_generator.py`**:
    - 構造化されたリポジトリデータを受け取り、Markdown形式の文字列を生成する関数。
    - 各リポジトリの詳細セクションや、全体のリポジトリリストを構築する補助関数。
- **`project_overview_fetcher.py`**:
    - リモートのGitHubリポジトリから指定されたファイルの内容をHTTPリクエストで取得する関数。
    - 取得したファイル内容から、特定のセクションタイトル（例: "プロジェクト概要"）配下の指定された行数を抽出する関数。
    - キャッシュメカニズムを管理する関数。
- **`readme_badge_extractor.py`**:
    - READMEの内容を解析し、特定の正規表現やパターンに基づいてバッジのURLやテキストを抽出する関数。
- **`repository_processor.py`**:
    - GitHub APIから返されるリポジトリオブジェクトを受け取り、必要な情報（名前、説明、URL、言語、スター数など）を抽出・整形し、アプリケーション内部のデータモデルに変換する関数。
    - アーカイブ済み、フォーク、アクティブといったリポジトリの分類を行う関数。
- **`statistics_calculator.py`**:
    - リポジトリのリストを受け取り、総スター数、総フォーク数などの集計統計を計算する関数。
- **`template_processor.py`**:
    - テンプレート文字列やファイルを読み込み、プレースホルダーを実際のデータで置換して最終的なコンテンツを生成する関数。
- **`url_utils.py`**:
    - ベースURLとパスを結合して完全なURLを構築する関数。
    - URLが有効であるか、特定のパターンに一致するかを検証する関数。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-28 07:07:33 JST
