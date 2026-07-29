Last updated: 2026-07-30

# Project Overview

## プロジェクト概要
- GitHub Pagesサイトの検索エンジン最適化 (SEO) と可視性を向上させるシステムです。
- GitHub APIを利用してリポジトリ情報を自動取得し、動的にMarkdownページを生成します。
- 各リポジトリの魅力を伝える3行の概要文を自動表示し、訪問者に分かりやすく提示します。

## 技術スタック
- フロントエンド: GitHub Pages (JekyllベースでMarkdownファイルをレンダリング), Markdown (リポジトリ一覧のコンテンツ形式)
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - Python: プロジェクトの主要な開発言語。
    - pytest: Pythonアプリケーションのテストフレームワーク。
    - ruff: Pythonコードのリンターおよびフォーマッター。
    - pip: Pythonパッケージのインストールと依存関係管理ツール。
- テスト: pytest (ユニットテスト、統合テスト)
- ビルドツール: PythonスクリプトによるMarkdownファイル生成 (実質的なコンテンツビルド)
- 言語機能: Python (バージョン3.x系と推測)
- 自動化・CI/CD: GitHub Actions (GitHub Pagesのデプロイで利用される可能性が高いが、明示的な設定はプロジェクト情報にない), `.github_automation` ディレクトリ内のスクリプト (ファイルチェック等の自動化)
- 開発標準: ruff (コードスタイル自動修正), .editorconfig (エディタのコードスタイル統一設定)

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
-   `.editorconfig`: 異なるエディタやIDE間でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
-   `.github_automation/check_large_files/`: GitHubリポジトリ内の大容量ファイルを検出するための自動化スクリプト群を格納するディレクトリです。
    -   `README.md`: `check_large_files` ディレクトリの目的や使い方を説明するファイルです。
    -   `check-large-files.toml`: 大容量ファイルチェックの設定（しきい値など）を定義するファイルです。
    -   `scripts/check_large_files.py`: 実際にリポジトリ内のファイルを走査し、設定に基づいて大容量ファイルを特定するPythonスクリプトです。
-   `.gitignore`: Gitのバージョン管理から除外したいファイルやディレクトリのパターンを定義するファイルです。
-   `LICENSE`: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
-   `README.md`: プロジェクトの概要、目的、主な機能、設定方法、実行コマンド、開発者向けヒントなどを記述したメインのドキュメントです。
-   `_config.yml`: JekyllベースのGitHub Pagesサイト全体の動作を制御する設定ファイルです。
-   `assets/`: ウェブサイトで使用されるファビコンやその他の静的アセット（画像、アイコンなど）を格納するディレクトリです。
    -   `favicon-*.png`: ウェブサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
-   `debug_project_overview.py`: `project_overview` 機能（各リポジトリの概要取得）をデバッグするための補助スクリプトです。
-   `generated-docs/`: プロジェクトが自動生成したドキュメントや一時ファイルを格納する場所として使用されます。
-   `googled947dc864c270e07.html`: Google Search Consoleなどの検索エンジンツールで、サイトの所有権を確認するために配置されるHTMLファイルです。
-   `index.md`: GitHub PagesサイトのトップページとなるMarkdownファイルです。このファイルに自動生成されたリポジトリ一覧が組み込まれます。
-   `issue-notes/22.md`: 開発中の課題やメモを記録するためのMarkdownファイルです。具体的な課題番号「22」を示しています。
-   `manifest.json`: プログレッシブウェブアプリ (PWA) の設定を定義するマニフェストファイルです。ホーム画面への追加やオフライン対応などに利用されます。
-   `pytest.ini`: `pytest` テストフレームワークの動作設定を定義するファイルです。
-   `requirements-dev.txt`: 開発環境やテスト実行時に必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `requirements.txt`: 本番環境でこのシステムを実行するために必要となるPythonパッケージとそのバージョンをリストアップしたファイルです。
-   `robots.txt`: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはクロールしてはいけないかを指示するファイルです。
-   `ruff.toml`: Pythonコードのスタイルチェックツール `ruff` の設定ファイルです。コードの整形ルールやリンティングルールが定義されています。
-   `src/__init__.py`: `src` ディレクトリをPythonパッケージとして識別するためのファイルです。
-   `src/generate_repo_list/`: リポジトリ一覧を生成する主要なロジックが格納されているPythonパッケージです。
    -   `__init__.py`: `generate_repo_list` ディレクトリをPythonパッケージとして識別するためのファイルです。
    -   `badge_generator.py`: リポジトリの言語やスター数などの情報を元に、バッジ画像を生成または整形する機能を提供します。
    -   `config.yml`: リポジトリ一覧生成機能の動作に関する技術的なパラメータ（例: プロジェクト概要取得機能の有効/無効、対象ファイル名など）を設定するファイルです。
    -   `config_manager.py`: 設定ファイル (`config.yml` や `secrets.toml`) の読み込み、管理、アクセスを担当するモジュールです。
    -   `date_formatter.py`: 日付や時刻の情報を、人間が読みやすい形式に整形するためのユーティリティ機能を提供します。
    -   `generate_repo_list.py`: このプロジェクトのメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成する処理全体を統括します。
    -   `json_ld_template.json`: 検索エンジンのリッチスニペット表示などに利用されるJSON-LD形式の構造化データテンプレートです。
    -   `language_info.py`: リポジトリの使用言語情報を処理し、表示に適した形式に変換する機能を提供します。
    -   `markdown_generator.py`: 取得・処理されたリポジトリデータに基づいて、GitHub Pages用のMarkdownコンテンツを構築する役割を担います。
    -   `project_overview_fetcher.py`: 各リポジトリから特定のファイル（例: `generated-docs/project-overview.md`）を読み込み、プロジェクトの概要テキストを抽出する機能を提供します。
    -   `readme_badge_extractor.py`: リポジトリの `README.md` ファイルから特定のバッジ情報（CIステータス、カバレッジなど）を抽出する機能です。
    -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、必要な情報に絞り込み、整形、フィルタリングする役割を担います。
    -   `seo_template.yml`: SEO関連のメタデータやテンプレート設定を定義するファイルです。
    -   `statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算・集計する機能を提供します。
    -   `strings.yml`: UIに表示される各種メッセージや文言を一元的に管理するファイルです。多言語対応や文言の変更が容易になります。
    -   `template_processor.py`: Markdownテンプレート内のプレースホルダーを実際のデータに置き換え、最終的なコンテンツを生成する処理を担当します。
    -   `url_utils.py`: URLの検証、整形、生成など、URLに関連する様々なユーティリティ機能を提供します。
-   `test_project_overview.py`: `project_overview_fetcher` モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
-   `tests/`: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    -   `conftest.py`: `pytest` でテスト全体に共通するフィクスチャやヘルパー関数を定義するファイルです。
    -   `test_badge_generator_integration.py`: バッジ生成機能が正しく動作するかを確認する統合テストです。
    -   `test_check_large_files.py`: 大容量ファイルチェック機能の単体テストまたは結合テストです。
    -   `test_config.py`: 設定ファイル (`config.yml` など) の読み込みや解釈が正しく行われるかをテストします。
    -   `test_date_formatter.py`: 日付整形機能の様々なケースをテストします。
    -   `test_environment.py`: 開発・実行環境が正しく設定され、依存関係が満たされているかを確認するテストです。
    -   `test_integration.py`: プロジェクト全体、または主要なコンポーネント間の連携が期待通りに機能するかを検証する統合テストです。
    -   `test_markdown_generator.py`: Markdown生成機能が、適切な入力から正しいMarkdownを出力するかをテストします。
    -   `test_project_overview_fetcher.py`: プロジェクト概要の取得機能が、指定されたファイルから正確な情報を抽出できるかをテストします。
    -   `test_readme_badge_extractor.py`: `README` からバッジ情報を正しく抽出できるかをテストします。
    -   `test_repository_processor.py`: リポジトリデータの取得、整形、フィルタリング機能が正しく動作するかをテストします。

## 関数詳細説明
このプロジェクトでは、主にPythonスクリプトとして機能が実装されており、以下の主要な関数が中心的な役割を担っています。具体的な引数や戻り値の型はコードに依存しますが、一般的な役割を説明します。

-   **`generate_repo_list.py` 内の `main()` 関数**:
    -   **役割**: プロジェクトのエントリーポイントであり、リポジトリ一覧生成処理全体のオーケストレーションを行います。
    -   **機能**: コマンドライン引数をパースし、GitHub APIからリポジトリ情報を取得、取得したデータを処理、Markdownコンテンツを生成し、指定された出力ファイルに書き出す一連の流れを制御します。
    -   **引数**: コマンドラインから渡される引数（ユーザー名、出力ファイル名、制限数など）。
    -   **戻り値**: なし（ファイル出力が主な副作用）。

-   **`project_overview_fetcher.py` 内の `fetch_project_overview()` 関数**:
    -   **役割**: 各リポジトリの特定のパスにある `project-overview.md` ファイルからプロジェクト概要を抽出し、整形します。
    -   **機能**: GitHub APIを通じてリポジトリ内の指定ファイルを読み込み、定義されたセクションから3行の概要テキストを解析して取得します。
    -   **引数**: リポジトリ情報（オーナー、リポジトリ名など）、設定情報（ファイルパス、セクションタイトルなど）。
    -   **戻り値**: 抽出されたプロジェクトの概要テキスト（文字列のリストなど）。

-   **`markdown_generator.py` 内の `generate_markdown()` 関数**:
    -   **役割**: 処理済みのリポジトリデータを受け取り、最終的なGitHub Pages用のMarkdownコンテンツを生成します。
    -   **機能**: 提供されたリポジトリ情報をテンプレートと組み合わせて、SEOに適した構造化されたMarkdown形式の文字列を構築します。
    -   **引数**: 処理済みリポジトリデータのリスト、設定情報。
    -   **戻り値**: 生成されたMarkdownコンテンツ（文字列）。

-   **`repository_processor.py` 内の `process_repositories()` 関数**:
    -   **役割**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形します。
    -   **機能**: リポジトリのフィルタリング（アーカイブ、フォークなど）、必要な情報の抽出、統計情報の計算、プロジェクト概要の取得などの前処理を行います。
    -   **引数**: GitHub APIから取得した生のリポジトリデータ、設定情報。
    -   **戻り値**: 整形・処理されたリポジトリデータのリスト。

## 関数呼び出し階層ツリー
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-07-30 07:21:33 JST
