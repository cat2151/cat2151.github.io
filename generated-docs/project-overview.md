Last updated: 2026-03-15

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、リポジトリ情報を取得してSEOに最適化されたMarkdown形式で出力します。
- バッジ表示、アクティブ/アーカイブ/フォークによる分類、プロジェクト概要の自動取得などの機能を提供します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesで静的サイトを構築するためのジェネレータ。生成されたMarkdownファイルをHTMLに変換し、サイト表示を管理します。
    - **Markdown**: リポジトリ一覧や各リポジトリの情報を構造化されたテキスト形式で記述するために使用されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語であり、リポジトリ情報の取得、処理、Markdown生成の中核を担います。
    - **Git/GitHub**: ソースコード管理システムおよびホスティングサービスで、リポジトリ情報の取得元となります。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、柔軟な設定を可能にします。
    - **TOML**: 設定ファイル (`ruff.toml`, `secrets.toml`) の記述に使用されます。
    - **JSON**: SEO最適化のためのJSON-LDテンプレート (`json_ld_template.json`) やPWAマニフェストファイル (`manifest.json`) に使用されます。
- テスト:
    - **pytest**: Pythonアプリケーションの単体テスト、結合テスト、統合テストを実行するためのテストフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: `generate_repo_list.py` がGitHub APIからのデータ取得とMarkdownファイルの生成を主導します。
- 言語機能:
    - **Python**: モダンなスクリプト機能、ライブラリエコシステムを活用し、開発効率と保守性を高めています。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation` ディレクトリ内で、例えば大きなファイルのチェックなど、一部の自動化処理に使用される可能性があります。
- 開発標準:
    - **Ruff**: Pythonコードのリンティングとフォーマットを高速に行うツールで、コード品質と統一性を保ちます。
    - **.editorconfig**: 異なるIDEやエディタを使用する開発者間で、コードスタイル（インデント、改行など）の統一を図ります。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコードスタイルを維持するための設定ファイル。
- **`.github_automation/`**: GitHub Actionsに関連する自動化スクリプトや設定を格納するディレクトリ。
    - **`.github_automation/check_large_files/README.md`**: `check_large_files` ディレクトリの目的と使用方法を説明するドキュメント。
    - **`.github_automation/check_large_files/check-large-files.toml`**: 大きなファイルをチェックするスクリプトの設定ファイル。
    - **`.github_automation/check_large_files/scripts/check_large_files.py`**: Gitリポジトリ内の大きなファイルを検出し、管理を促すPythonスクリプト。
- **`.gitignore`**: Gitがバージョン管理の対象から除外すべきファイルやディレクトリを指定するファイル。
- **`LICENSE`**: プロジェクトがMITライセンスの下で公開されていることを示すファイル。
- **`README.md`**: プロジェクトの概要、使い方、開発者向けのヒント、コマンド例などを記載したメインドキュメント。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイル。サイトのタイトル、テーマ、プラグインなどの設定を含みます。
- **`assets/`**: GitHub Pagesサイトで使用される静的アセット（画像ファイルなど）を格納するディレクトリ。
    - **`assets/favicon-*.png`**: ウェブサイトのファビコン（ブラウザタブなどに表示されるアイコン）の各サイズ。
- **`debug_project_overview.py`**: プロジェクト概要取得機能のデバッグやテストを目的とした補助スクリプト。
- **`generated-docs/`**: 自動生成されたドキュメントやレポート、または他の処理結果が一時的に保存されるディレクトリ。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認に使用されるHTMLファイル。
- **`index.md`**: GitHub Pagesサイトのトップページとして、生成されたリポジトリ一覧が出力されるMarkdownファイル。
- **`issue-notes/22.md`**: 特定の課題や検討事項に関するメモを記録するファイル。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイル。ウェブサイトのインストール情報やオフライン動作などを定義します。
- **`pytest.ini`**: `pytest` テストフレームワークの設定ファイル。テストの発見ルールやオプションなどを定義します。
- **`requirements-dev.txt`**: 開発環境およびテスト実行に必要なPythonライブラリの依存関係リスト。
- **`requirements.txt`**: プロジェクトの本番実行に必要なPythonライブラリの依存関係リスト。
- **`robots.txt`**: 検索エンジンのウェブクローラーがウェブサイトのどのページをクロールしてよいか、またどのページをクロールすべきでないかを指示するファイル。
- **`ruff.toml`**: Pythonコードのリンティングとフォーマットに使用される `ruff` ツールの設定ファイル。
- **`src/__init__.py`**: Pythonの `src` ディレクトリがパッケージであることを示すファイル。
- **`src/generate_repo_list/`**: リポジトリ一覧を生成する主要なロジックが格納されているPythonパッケージ。
    - **`src/generate_repo_list/__init__.py`**: `generate_repo_list` パッケージがPythonパッケージであることを示すファイル。
    - **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語や状態を示すバッジ（アイコン）のMarkdownテキストを生成するロジックを管理します。
    - **`src/generate_repo_list/config.yml`**: リポジトリ一覧生成スクリプトの実行に関する技術的なパラメータ（例: プロジェクト概要取得設定、APIタイムアウト）を定義する設定ファイル。
    - **`src/generate_repo_list/config_manager.py`**: プロジェクト全体で使用される設定ファイル (`config.yml`, `strings.yml` など) を読み込み、管理するモジュール。
    - **`src/generate_repo_list/date_formatter.py`**: GitHub APIから取得した日付情報を、人間が読みやすい形式にフォーマットするためのユーティリティモジュール。
    - **`src/generate_repo_list/generate_repo_list.py`**: プロジェクトのメイン実行スクリプト。GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成をオーケストレーションします。
    - **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化 (SEO) のため、構造化データ（JSON-LD）を生成する際のテンプレート。
    - **`src/generate_repo_list/language_info.py`**: リポジトリの主要言語や使用割合など、言語に関する情報を処理し整形するモジュール。
    - **`src/generate_repo_list/markdown_generator.py`**: 処理されたリポジトリデータに基づいて、Jekyll互換のMarkdown形式のコンテンツを生成するモジュール。
    - **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要を自動的に取得する機能を提供します。
    - **`src/generate_repo_list/readme_badge_extractor.py`**: リポジトリのREADMEファイルから既存のバッジ情報を抽出し、重複を避けるなどの処理を行うモジュール。
    - **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するビジネスロジックを実装します。
    - **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータや設定を定義するためのテンプレートファイル。
    - **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するモジュール。
    - **`src/generate_repo_list/strings.yml`**: アプリケーション内で使用される表示メッセージ、文言、ラベルなどを一元的に管理するための設定ファイル。多言語対応や文言変更を容易にします。
    - **`src/generate_repo_list/template_processor.py`**: Markdown生成時に使用されるテンプレート（例: レイアウト、セクション構造）を処理し、データと結合するモジュール。
    - **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URLに関連する様々なユーティリティ関数を提供するモジュール。
- **`test_project_overview.py`**: `project_overview_fetcher` モジュールの機能（特にプロジェクト概要の取得）を検証するための単体テストスクリプト。
- **`tests/`**: プロジェクトの様々なコンポーネントに対するテストスクリプトを格納するディレクトリ。
    - **`tests/test_badge_generator_integration.py`**: `badge_generator` の機能が他のコンポーネントと正しく連携するかを確認する結合テスト。
    - **`tests/test_check_large_files.py`**: `check_large_files.py` スクリプトの正確性と機能性を検証するテスト。
    - **`tests/test_config.py`**: 設定ファイル (`config.yml`, `strings.yml` など) の読み込みとパースが正しく行われるかを確認するテスト。
    - **`tests/test_date_formatter.py`**: `date_formatter` モジュールの日付変換機能の正確性を検証するテスト。
    - **`tests/test_environment.py`**: プロジェクトの実行環境に関する設定や依存関係が適切かを確認するテスト。
    - **`tests/test_integration.py`**: システム全体の主要なフロー（API取得からMarkdown生成まで）が正しく機能するかを検証する統合テスト。
    - **`tests/test_markdown_generator.py`**: `markdown_generator` モジュールが意図した形式のMarkdownを生成するかを検証するテスト。
    - **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher` モジュールが正しくプロジェクト概要をフェッチできるかを確認するテスト。
    - **`tests/test_readme_badge_extractor.py`**: `readme_badge_extractor` モジュールがREADMEからバッジ情報を正確に抽出できるかを確認するテスト。
    - **`tests/test_repository_processor.py`**: `repository_processor` モジュールがGitHub APIからのリポジトリデータを適切に処理・整形できるかを確認するテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、各モジュール内に特定の役割を持つ関数が実装されています。具体的な関数名が提供されていないため、モジュールの役割から推測される一般的な関数の役割を説明します。

- **リポジトリ情報取得関数 (`generate_repo_list.py` 内)**:
    - **役割**: GitHub APIにアクセスし、指定されたユーザーのリポジトリ一覧や各リポジトリの詳細情報をフェッチします。
    - **引数**: GitHubユーザー名、オプションでAPIトークン、リポジトリ数の上限など。
    - **戻り値**: 取得したリポジトリデータの生JSON（またはPython辞書）リスト。
- **リポジトリデータ処理関数 (`repository_processor.py` 内)**:
    - **役割**: 取得した生のリポジトリデータから、表示に必要な情報（名前、説明、URL、言語、スター数など）を抽出し、整形します。アクティブ/アーカイブ/フォークなどの分類も行います。
    - **引数**: 生のリポジトリデータ。
    - **戻り値**: 整形され、処理に適したPython辞書のリスト。
- **Markdown生成関数 (`markdown_generator.py` 内)**:
    - **役割**: 処理済みのリポジトリデータとテンプレートを組み合わせて、Jekyllで解釈可能なMarkdown形式のコンテンツを生成します。
    - **引数**: 処理済みリポジトリデータのリスト、設定情報、テンプレート文字列。
    - **戻り値**: 生成されたMarkdown形式の文字列。
- **バッジ生成関数 (`badge_generator.py` 内)**:
    - **役割**: リポジトリの言語やその他の属性に基づいて、視覚的なバッジ（例: Python, JavaScriptなどの言語バッジ）のMarkdownコードを生成します。
    - **引数**: リポジトリの言語情報、スター数、その他のメタデータ。
    - **戻り値**: バッジを示すMarkdown文字列。
- **プロジェクト概要取得関数 (`project_overview_fetcher.py` 内)**:
    - **役割**: 各リポジトリ内の特定のファイルパス（例: `generated-docs/project-overview.md`）から、プロジェクトの3行概要テキストを抽出します。
    - **引数**: リポジトリ名、ターゲットファイルパス、セクションタイトル、設定（キャッシュ有無、リトライ回数、タイムアウト）。
    - **戻り値**: 抽出されたプロジェクト概要の文字列、またはNone。
- **設定管理関数 (`config_manager.py` 内)**:
    - **役割**: プロジェクトで使用されるYAML形式の設定ファイル (`config.yml`, `strings.yml` など) を読み込み、アプリケーション内でアクセス可能な形式で提供します。
    - **引数**: 設定ファイルのパス。
    - **戻り値**: 設定内容を格納したPython辞書。
- **日付フォーマット関数 (`date_formatter.py` 内)**:
    - **役割**: ISO 8601形式などの日付文字列を、より読みやすい任意の形式に変換します。
    - **引数**: 日付/時刻を示す文字列。
    - **戻り値**: フォーマットされた日付文字列。
- **ユーティリティ関数 (`url_utils.py`, `statistics_calculator.py` など)**:
    - **役割**: URLの構築、解析、統計計算など、共通で利用される補助的な処理を提供します。
    - **引数**: 特定の処理に必要なデータ。
    - **戻り値**: 処理結果。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-03-15 07:07:35 JST
