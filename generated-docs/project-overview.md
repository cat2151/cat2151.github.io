Last updated: 2026-07-28

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、ユーザーのリポジトリ情報を自動取得します。
- JekyllベースのGitHub Pages向けに、SEO最適化されたリポジトリ一覧をMarkdown形式で生成します。
- 検索エンジンからの参照性向上とLLM連携を支援し、開発効率の向上を目指します。

## 技術スタック
- フロントエンド:
    - Jekyll: GitHub Pagesサイトの基盤となる静的サイトジェネレーターで、生成されたMarkdownファイルをウェブサイトとして構築します。
    - Markdown: リポジトリ一覧や各リポジトリの概要を記述する形式で、SEO最適化されたコンテンツの出力に利用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: GitHub APIからの情報取得、Markdownファイルの生成、各種ファイル処理を行う主要なプログラミング言語です。
    - GitHub API: GitHub上のリポジトリ情報をプログラム的に取得するためのインターフェースです。
- テスト:
    - pytest: Pythonプロジェクトのテストフレームワークで、スクリプトの機能が正しく動作するかを検証するために使用されます。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py` を中心としたPythonスクリプト群が、リポジトリ一覧のMarkdownファイルを自動生成する役割を担います。
- 言語機能:
    - Python: 動的型付け、豊富な標準ライブラリ、読みやすい構文などを活用し、開発の効率性を高めます。
- 自動化・CI/CD:
    - GitHub Pages: 生成されたコンテンツをホストし、ウェブサイトとして公開するサービスです。本システムはGitHub Pages上でのコンテンツ自動生成を目的としています。
- 開発標準:
    - ruff: Pythonコードのリンター・フォーマッターで、コードの品質とプロジェクト全体の統一性を保つために使用されます。

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
- **.editorconfig**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
- **.github_automation/**: GitHub Actionsなどの自動化スクリプトや関連設定を格納するディレクトリ。
- **.github_automation/check_large_files/README.md**: 大容量ファイルチェック機能のREADMEファイル。
- **.github_automation/check_large_files/check-large-files.toml**: 大容量ファイルチェックツールの設定ファイル。
- **.github_automation/check_large_files/scripts/check_large_files.py**: GitHubリポジトリ内の大容量ファイルを検出するためのPythonスクリプト。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
- **LICENSE**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）。
- **README.md**: プロジェクトの目的、セットアップ方法、使用方法、開発者向けヒントなどを記述したメインのドキュメント。
- **_config.yml**: Jekyllサイト全体の構成設定を定義するファイル。
- **assets/**: ウェブサイトで使用されるファビコンやその他の静的アセット（画像など）を格納するディレクトリ。
- **assets/favicon-*.png**: ウェブサイトのブラウザタブやブックマークに表示されるファビコン画像ファイル。
- **debug_project_overview.py**: `project_overview_fetcher` モジュールのデバッグやテスト実行を補助するためのスクリプト。
- **generated-docs/**: 他のリポジトリから取得した `project-overview.md` などのドキュメントが一時的に保存されるか、生成元となるディレクトリ。
- **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用されるHTMLファイル。
- **index.md**: `generate_repo_list.py` スクリプトによって生成される、リポジトリ一覧のメインMarkdownファイル。GitHub Pagesサイトのトップページとして機能します。
- **issue-notes/22.md**: プロジェクトの特定の課題や改善点に関するメモや詳細を記述したドキュメント。
- **manifest.json**: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータ（名前、アイコンなど）を定義するファイル。
- **pytest.ini**: Pythonのテストフレームワークであるpytestの動作設定を定義するファイル。
- **requirements-dev.txt**: 開発時やテスト時に必要なPythonパッケージの依存関係を記述したファイル。
- **requirements.txt**: プロジェクトの実行に必要なPythonパッケージの依存関係を記述したファイル。
- **robots.txt**: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
- **ruff.toml**: Pythonコードのリンター・フォーマッターであるruffの設定ファイル。コードスタイルの統一と品質保持に使用されます。
- **src/__init__.py**: `src` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/**: リポジトリ一覧生成システムの主要なロジックを格納するPythonパッケージ。
- **src/generate_repo_list/__init__.py**: `generate_repo_list` ディレクトリをPythonパッケージとして認識させるための初期化ファイル。
- **src/generate_repo_list/badge_generator.py**: リポジトリの特性（アクティブ、アーカイブなど）を示すバッジを生成または管理するロジックを実装したモジュール。
- **src/generate_repo_list/config.yml**: リポジトリ一覧生成スクリプトの実行時設定（例: プロジェクト概要取得機能のON/OFF、対象ファイルパスなど）を定義するファイル。
- **src/generate_repo_list/config_manager.py**: 設定ファイル（`config.yml`や`strings.yml`など）の読み込み、解析、管理を行うユーティリティモジュール。
- **src/generate_repo_list/date_formatter.py**: 日付や時刻の情報を整形し、人間が読みやすい形式や特定のフォーマットに変換するためのユーティリティ関数群。
- **src/generate_repo_list/generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、他のモジュールと連携してMarkdown形式のリポジトリ一覧を生成するメインの実行スクリプト。
- **src/generate_repo_list/json_ld_template.json**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）のテンプレートを定義するファイル。
- **src/generate_repo_list/language_info.py**: リポジトリが使用するプログラミング言語に関する情報を処理し、表示に適した形式に変換するロジック。
- **src/generate_repo_list/markdown_generator.py**: 取得したリポジトリ情報に基づいて、Jekyll/GitHub Pagesで表示するためのMarkdownコンテンツを生成するロジック。
- **src/generate_repo_list/project_overview_fetcher.py**: 各リポジトリから特定のパス（例: `generated-docs/project-overview.md`）にあるプロジェクト概要を取得し、その内容を解析するロジック。
- **src/generate_repo_list/readme_badge_extractor.py**: リポジトリのREADMEファイルから、CI/CDステータスやライセンスなどのバッジ情報を自動的に抽出するロジック。
- **src/generate_repo_list/repository_processor.py**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形・フィルタリングするロジック。
- **src/generate_repo_list/seo_template.yml**: サイトのSEO関連メタデータや、コンテンツに埋め込むためのSEOテンプレート設定を定義するファイル。
- **src/generate_repo_list/statistics_calculator.py**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジック。
- **src/generate_repo_list/strings.yml**: ウェブサイトや生成されるMarkdownに表示される、さまざまなテキストメッセージ、見出し、ラベルなどを一元管理するためのファイル（国際化対応などに使用）。
- **src/generate_repo_list/template_processor.py**: Markdown生成時に使用するテンプレートファイル（例: Jinja2テンプレート）を読み込み、データに基づいてレンダリングするロジック。
- **src/generate_repo_list/url_utils.py**: URLの生成、解析、正規化、検証など、URLに関連する様々なユーティリティ関数を提供。
- **test_project_overview.py**: `project_overview_fetcher.py` モジュールのテストケースを定義したスクリプト。
- **tests/**: プロジェクト全体のテストコードを格納するディレクトリ。
- **tests/conftest.py**: pytestのテストフィクスチャやプラグインを定義し、テスト環境のセットアップや共通処理を提供。
- **tests/test_badge_generator_integration.py**: `badge_generator` モジュールの機能が他のコンポーネントと正しく連携するかを検証する統合テスト。
- **tests/test_check_large_files.py**: 大容量ファイルチェック機能の正確性を検証するテスト。
- **tests/test_config.py**: 設定ファイルの読み込みやパラメータの検証など、`config_manager` モジュールに関連するテスト。
- **tests/test_date_formatter.py**: `date_formatter` モジュールの日付フォーマット機能の正確性を検証するテスト。
- **tests/test_environment.py**: 開発環境や依存関係のセットアップが正しく行われているかを確認するテスト。
- **tests/test_integration.py**: システム全体がエンドツーエンドで正しく動作するかを検証する統合テスト。
- **tests/test_markdown_generator.py**: `markdown_generator` モジュールが意図した通りのMarkdownコンテンツを生成するかを検証するテスト。
- **tests/test_project_overview_fetcher.py**: `project_overview_fetcher` モジュールがプロジェクト概要を正しく取得・解析できるかを検証するテスト。
- **tests/test_readme_badge_extractor.py**: `readme_badge_extractor` モジュールがREADMEからバッジ情報を正確に抽出できるかを検証するテスト。
- **tests/test_repository_processor.py**: `repository_processor` モジュールがリポジトリデータを適切に処理・変換できるかを検証するテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、各モジュール内に特定の役割を持つ関数群が実装されています。具体的な関数名や引数、戻り値の詳細は提供されていませんが、各モジュールの機能から推測される役割を以下に説明します。

- **`badge_generator.py` 内の関数**:
    - 役割: リポジトリのステータス（アクティブ、アーカイブ、フォークなど）や言語などの情報を基に、表示用のバッジ文字列を生成します。
    - 機能: リポジトリデータを受け取り、設定されたルールに基づいて適切なバッジのURLやMarkdown形式の文字列を返します。
- **`config_manager.py` 内の関数**:
    - 役割: プロジェクトの設定ファイル（`config.yml`, `strings.yml`など）を読み込み、アプリケーション全体で利用可能な形で管理します。
    - 機能: 指定されたパスからYAMLファイルをロードし、設定値を辞書やオブジェクトとして提供します。
- **`date_formatter.py` 内の関数**:
    - 役割: 日付や時刻の情報をさまざまな形式に整形します。
    - 機能: `datetime` オブジェクトやタイムスタンプを受け取り、例えば「YYYY/MM/DD」や「〇日前」のような表示形式の文字列を生成します。
- **`generate_repo_list.py` 内のメイン関数群**:
    - 役割: GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といった一連のプロセスをオーケストレーションします。
    - 機能: コマンドライン引数を解析し、他のモジュールの関数を呼び出してリポジトリリストの生成を制御します。
- **`language_info.py` 内の関数**:
    - 役割: リポジトリが使用するプログラミング言語に関する情報を処理し、表示に適した形式に変換します。
    - 機能: 言語ごとの使用率データなどを受け取り、主要言語のリストや視覚化のためのデータを整形します。
- **`markdown_generator.py` 内の関数**:
    - 役割: 処理されたリポジトリ情報から、GitHub Pages用の最終的なMarkdownコンテンツを生成します。
    - 機能: リポジトリデータのリストとテンプレート情報を基に、バッジ、概要、リンクなどを含む構造化されたMarkdown文字列を作成します。
- **`project_overview_fetcher.py` 内の関数**:
    - 役割: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要を抽出し、解析します。
    - 機能: リポジトリ名とファイルパスを受け取り、ファイルのコンテンツを読み込み、指定されたセクション（例: 「プロジェクト概要」）から3行の要約を抽出します。
- **`readme_badge_extractor.py` 内の関数**:
    - 役割: READMEファイルの内容から、特定のバッジ（例: ビルドステータス、ライセンス）の情報を抽出します。
    - 機能: READMEのテキストコンテンツを解析し、正規表現などを用いてバッジのURLやテキストを特定します。
- **`repository_processor.py` 内の関数**:
    - 役割: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形・フィルタリングします。
    - 機能: API応答をパースし、必要な情報を抽出し、アクティブ・アーカイブ・フォークなどの分類を行い、表示順序を調整します。
- **`statistics_calculator.py` 内の関数**:
    - 役割: リポジトリに関する統計情報（スター数、フォーク数、コミット数など）を計算します。
    - 機能: リポジトリデータを受け取り、各統計量を算出して提供します。
- **`template_processor.py` 内の関数**:
    - 役割: Markdown生成時に使用されるテンプレートファイル（例: `.yml`形式のテンプレート）を処理します。
    - 機能: テンプレートファイルを読み込み、プレースホルダーを実際のリポジトリデータに置き換えて最終的なコンテンツを生成します。
- **`url_utils.py` 内の関数**:
    - 役割: URLの生成、解析、正規化といったユーティリティ機能を提供します。
    - 機能: リポジトリ名やユーザー名からGitHub PagesのURLを構築したり、URL文字列を安全に処理したりします。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-07-28 07:25:44 JST
