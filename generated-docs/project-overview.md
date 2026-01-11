Last updated: 2026-01-12

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動で取得・処理するシステムです。
- JekyllベースのGitHub Pagesサイト向けに、SEO最適化されたリポジトリ一覧を生成します。
- 検索エンジンによるクロールとLLMからの参照性を向上させ、情報発見を促進します。

## 技術スタック
- フロントエンド: **Jekyll** (GitHub Pagesの静的サイトジェネレータ基盤として利用), **Markdown** (生成されるコンテンツのフォーマット), **GitHub Pages** (Webサイトのホスティング環境), **JSON-LD** (検索エンジン最適化のための構造化データ)
- 音楽・オーディオ: 該当なし
- 開発ツール: **Python** (スクリプト言語、主要なロジックを実装), **GitHub API** (リポジトリ情報の取得元), **requests** (HTTP通信ライブラリ、GitHub APIとの連携に使用と推測), **PyYAML** (YAMLファイル処理ライブラリ、設定ファイルの読み書きに使用と推測), **toml** (TOMLファイル処理ライブラリ、設定ファイルの読み書きに使用と推測)
- テスト: **pytest** (Pythonのテストフレームワーク)
- ビルドツール: **Pythonスクリプト** (プロジェクトの主要なスクリプト自体がMarkdown生成のビルドプロセスを担う)
- 言語機能: **Python言語** (特にモダンな構文や機能を使用)
- 自動化・CI/CD: **GitHub Pages** (生成されたコンテンツを自動でデプロイ・公開する環境としての側面)
- 開発標準: **ruff** (Pythonコードの高速なLinterおよびFormatter), **.editorconfig** (異なるエディタ間でのコーディングスタイル統一のための設定ファイル)

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
    📄 repository_processor.py
    📄 seo_template.yml
    📄 statistics_calculator.py
    📄 strings.yml
    📄 template_processor.py
    📄 url_utils.py
📄 test_project_overview.py
📁 tests/
  📄 test_config.py
  📄 test_date_formatter.py
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、インデントや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
- **`.gitignore`**: Gitのバージョン管理システムが追跡しないファイルやディレクトリ（例: ビルド成果物、ログファイル、ローカル設定）を指定するファイルです。
- **`LICENSE`**: このプロジェクトのソフトウェアライセンス（MITライセンス）が記述されており、利用条件や配布に関する情報を提供します。
- **`README.md`**: プロジェクトの概要、目的、機能、使用方法、設定、開発者向けヒントなどをまとめた、プロジェクトの顔となる主要ドキュメントです。
- **`_config.yml`**: JekyllベースのGitHub Pagesサイト全体の設定を定義するファイルです。テーマ、パーマリンク構造、プラグインなどが設定されます。
- **`assets/`**: GitHub Pagesサイトで使用される画像、CSS、JavaScriptなどの静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能のデバッグや単体テストを目的としたスクリプトです。
- **`generated-docs/`**: 他のリポジトリから取得した「プロジェクト概要」ファイルなどが一時的に格納される、あるいは参照されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleなどのウェブサイト認証サービスで使用されるファイルで、サイトの所有権を確認するために配置されます。
- **`index.md`**: `generate_repo_list.py`スクリプトによって最終的に生成される、リポジトリ一覧を含むメインのMarkdownファイルです。GitHub Pagesのトップページとして表示されます。
- **`issue-notes/`**: 開発中に発生した課題、検討事項、または将来の改善点などを個別のMarkdownファイルとして記録しておくためのディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）として動作させるための設定ファイルです。ホーム画面への追加、オフライン対応などの情報を含みます。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの検出方法、プラグイン、レポート形式などが定義されます。
- **`requirements-dev.txt`**: 開発時（テスト、リンティングなど）に必要となるPythonパッケージのリストです。
- **`requirements.txt`**: プロジェクトの実行に最低限必要なPythonパッケージのリストです。
- **`robots.txt`**: 検索エンジンのウェブクローラーに対して、どのページをクロールし、どのページをクロールしないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。コード規約や自動修正のルールが定義されます。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/`**: リポジトリ一覧生成のメインロジックを格納するPythonパッケージです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリの言語やスター数などの情報に基づき、Webサイトに表示するバッジのテキストやURLを生成するロジックを実装しています。
- **`src/generate_repo_list/config.yml`**: プロジェクト概要取得機能などの動作を制御するためのYAML形式の設定ファイルです。
- **`src/generate_repo_list/config_manager.py`**: YAML形式の設定ファイルを読み込み、プロジェクト全体で利用可能な設定値として管理する役割を担います。
- **`src/generate_repo_list/date_formatter.py`**: リポジトリの更新日時などの日付データを、人間が読みやすい形式や特定のロケールに合わせた形式に変換する処理を行います。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイル（リポジトリ一覧）を生成する処理を統括します。
- **`src/generate_repo_list/json_ld_template.json`**: SEOを強化するために、検索エンジンが理解しやすい形式で構造化データを記述するJSON-LDのテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: リポジトリが使用しているプログラミング言語に関する情報を取得し、表示用に処理するロジックを提供します。
- **`src/generate_repo_list/markdown_generator.py`**: 整形されたリポジトリ情報と抽出された概要を用いて、Jekyllサイトに適したMarkdown形式のコンテンツを生成するコアロジックを実装しています。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各リポジトリ内に存在する特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形に加工・整形する処理を行います。
- **`src/generate_repo_list/seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータや構造化データ（JSON-LD）のテンプレート定義を格納するYAMLファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリのスター数やフォーク数といった統計情報を計算・集計する機能を提供します。
- **`src/generate_repo_list/strings.yml`**: UIに表示されるメッセージや文言を一元管理するためのYAML形式のファイルで、国際化（i18n）の基盤にもなり得ます。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成において、特定のテンプレート（例: SEOテンプレート）を読み込み、動的なデータで埋める処理を担います。
- **`src/generate_repo_list/url_utils.py`**: URLの構築、検証、エンコードなど、URL操作に関するユーティリティ機能を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールに関する単体テストを記述したスクリプトです。
- **`tests/`**: プロジェクトの各種テストスクリプトを格納するディレクトリです。
- **`tests/test_config.py`**: 設定ファイルの読み込みや管理に関するテストを行うスクリプトです。
- **`tests/test_date_formatter.py`**: 日付フォーマット機能の正確性を検証するテストスクリプトです。
- **`tests/test_environment.py`**: 実行環境のセットアップや依存関係に関するテストを行うスクリプトです。
- **`tests/test_integration.py`**: 複数のモジュールが連携して正しく動作するかを確認する統合テストスクリプトです。
- **`tests/test_markdown_generator.py`**: Markdown生成ロジックの正確性や出力内容を検証するテストスクリプトです。
- **`tests/test_project_overview_fetcher.py`**: プロジェクト概要の取得機能に関するテストを行うスクリプトです。
- **`tests/test_repository_processor.py`**: リポジトリ情報の処理機能の正確性を検証するテストスクリプトです。

## 関数詳細説明
提供されたプロジェクト情報には具体的な関数シグネチャの詳細が含まれていないため、ファイル名とプロジェクトの機能から推測される主要な役割を持つ関数について、その機能と役割を説明します。

*   **`generate_repo_list.py`内の主要関数 (例: `main`関数や`run_generation`関数)**
    *   **役割**: プロジェクト全体のリポジトリ一覧生成プロセスを統括し、実行の起点となります。
    *   **機能**: コマンドライン引数を解析し、必要な設定を読み込みます。GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して各リポジトリを処理した後、最終的なMarkdownコンテンツを生成して指定されたファイルに出力します。

*   **`config_manager.py`内の主要関数 (例: `load_config`関数)**
    *   **役割**: YAML形式で記述された設定ファイルを読み込み、プロジェクト全体でアクセス可能な設定値を提供します。
    *   **機能**: 指定されたパスから設定ファイルを読み込み、プログラム内で利用しやすいデータ構造（例: 辞書型）として返します。設定値の妥当性検証を行う場合もあります。

*   **`repository_processor.py`内の主要関数 (例: `process_repository_data`関数)**
    *   **役割**: GitHub APIから取得した生のリポジトリデータから、Webサイト表示に必要な情報を抽出し、整形します。
    *   **機能**: リポジトリの名前、説明、URL、更新日時、主要言語、スター数などの重要な情報を抽出し、後続のMarkdown生成処理に適した形式に変換して提供します。

*   **`project_overview_fetcher.py`内の主要関数 (例: `fetch_project_overview`関数)**
    *   **役割**: 各リポジトリの特定のパスにある`project-overview.md`ファイルから、プロジェクトの簡潔な3行概要を自動で抽出します。
    *   **機能**: GitHub APIを介して対象ファイルを読み込み、指定されたセクションタイトル（例: `## プロジェクト概要`）の下にあるリスト形式の3行を解析して取得します。API呼び出しのキャッシュやリトライ処理を含む場合があります。

*   **`markdown_generator.py`内の主要関数 (例: `generate_repo_markdown`関数)**
    *   **役割**: 処理されたリポジトリ情報と抽出されたプロジェクト概要に基づいて、Jekyllサイトに適したMarkdown形式のコンテンツを生成します。
    *   **機能**: 各リポジトリのデータを受け取り、タイトル、説明、バッジ、リンク、プロジェクト概要、SEOメタデータなどを含むMarkdown形式のスニペットを構築し、一覧表示用のコンテンツを作成します。

*   **`badge_generator.py`内の主要関数 (例: `create_badges`関数)**
    *   **役割**: リポジトリの各種情報（使用言語、スター数など）に基づいて、Webサイトに表示するバッジのテキストや関連URLを生成します。
    *   **機能**: 言語アイコン、スター数、最終更新日などの視覚的な要素として機能するバッジを、MarkdownまたはHTML形式で表示可能な文字列として生成します。

*   **`date_formatter.py`内の主要関数 (例: `format_date`関数)**
    *   **役割**: リポジトリの更新日時などの日付文字列を、人間が読みやすく、特定のロケールや要件に合わせた形式に変換します。
    *   **機能**: ISO 8601形式などの標準的な日付文字列を受け取り、"YYYY年MM月DD日"や"〇時間前"のようなユーザーフレンドリーな表示形式に変換します。

*   **`language_info.py`内の主要関数 (例: `get_language_details`関数)**
    *   **役割**: リポジトリが使用しているプログラミング言語に関する詳細な情報を提供します。
    *   **機能**: 言語名に基づいて、その言語のアイコンパスや代表的なカラーコードなど、Webサイトで表示するために必要なメタデータを取得します。

*   **`statistics_calculator.py`内の主要関数 (例: `calculate_repo_stats`関数)**
    *   **役割**: リポジトリのスター数やフォーク数といった統計情報を計算または集計します。
    *   **機能**: GitHub APIから取得した生のリポジトリデータから、スターやフォークの総数を抽出し、必要に応じて特定の形式で返すことで、ランキングや概要表示に利用できるようにします。

*   **`template_processor.py`内の主要関数 (例: `apply_template`関数)**
    *   **役割**: テンプレート文字列内に定義されたプレースホルダーを、動的なデータで置き換える処理を行います。
    *   **機能**: MarkdownテンプレートやJSON-LDテンプレートを受け取り、リポジトリ名、説明、URLなどの実際のデータを挿入して、最終的なコンテンツ文字列を生成します。

*   **`url_utils.py`内の主要関数 (例: `build_github_repo_url`関数)**
    *   **役割**: GitHubリポジトリのURLやAPIエンドポイントなど、URL関連の操作を安全かつ効率的に行います。
    *   **機能**: ユーザー名、リポジトリ名、パスなどのコンポーネントから、完全なGitHub Pages URLやGitHub APIのURLを生成したり、URLのエンコードやデコードを行うユーティリティ機能を提供します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-12 07:06:19 JST
