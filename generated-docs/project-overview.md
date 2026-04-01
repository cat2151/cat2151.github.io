Last updated: 2026-04-02

# Project Overview

## プロジェクト概要
- GitHub APIを活用し、GitHub Pagesサイト向けにリポジトリ一覧を自動生成します。
- 各リポジトリの概要やバッジ、統計情報を盛り込み、SEOに最適化されたMarkdownを出力します。
- 検索エンジンやLLMからの参照性を高め、プロジェクトの可視性と開発効率の向上を目指します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pagesサイトの基盤として、本プロジェクトはJekyllが解釈可能なMarkdownコンテンツを生成します), Markdown (生成されるコンテンツ形式)
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール: Python (主要な開発言語および実行環境), GitHub API (リポジトリ情報の取得), TOML (設定ファイル形式), YAML (設定ファイル形式), `.editorconfig` (エディタの設定統一), `.github_automation/check_large_files/scripts/check_large_files.py` (大容量ファイルチェックスクリプト)
- テスト: pytest (Pythonコードのテストフレームワーク)
- ビルドツール: Jekyll (GitHub Pagesサイトの静的サイトジェネレータ。本プロジェクトはJekyll向けのMarkdownコンテンツを生成します)
- 言語機能: Python (スクリプトの記述に利用される主要なプログラミング言語)
- 自動化・CI/CD: このプロジェクト自体がGitHub Pages向けコンテンツの自動生成を行うPythonスクリプトであり、そのものが「自動化」機能を提供します。ただし、具体的なCI/CDパイプラインツール（例: GitHub Actions）は主要な構成要素としては記述されていません。
- 開発標準: ruff (Pythonコードのフォーマットと静的解析ツール)

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
- **.editorconfig**: 異なるエディタやIDEを使用する開発者間で、コードの書式設定（インデント、改行コードなど）を統一するための設定ファイルです。
- **.github_automation/**: 自動化スクリプトや関連ファイルを格納するディレクトリです。
    - **check_large_files/**: 大容量ファイルチェック機能に関連するファイルを格納します。
        - **README.md**: 大容量ファイルチェック機能の説明ドキュメントです。
        - **check-large-files.toml**: 大容量ファイルチェック機能の設定ファイルです。
        - **scripts/check_large_files.py**: 指定されたリポジトリ内の大容量ファイルを検出するPythonスクリプトです。
- **.gitignore**: Gitがバージョン管理の対象としないファイルやディレクトリのパターンを定義するファイルです。
- **LICENSE**: プロジェクトのライセンス情報（この場合はMITライセンス）を記載したファイルです。
- **README.md**: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、プロジェクトに関する包括的な情報を提供するメインドキュメントです。
- **_config.yml**: GitHub Pages（Jekyll）サイト全体の動作や設定を定義するファイルです。
- **assets/**: Webサイトで使用される画像、アイコンなどの静的アセットを格納するディレクトリです。
    - **favicon-16x16.png**, **favicon-192x192.png**, **favicon-32x32.png**, **favicon-512x512.png**: Webサイトのファビコン（ブラウザのタブやブックマークに表示されるアイコン）の各サイズ画像です。
- **debug_project_overview.py**: 各リポジトリからプロジェクト概要を取得する機能のデバッグや単体テストに利用されるスクリプトです。
- **generated-docs/**: 各リポジトリのプロジェクト概要 (`project-overview.md`) など、自動生成または参照されるドキュメントを格納することが想定されるディレクトリです。
- **googled947dc864c270e07.html**: Google Search Consoleにおけるサイト所有権の確認に使用されるファイルです。
- **index.md**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトによって生成されたリポジトリ一覧がここに出力されます。
- **issue-notes/**: 開発中の課題や特定のイシューに関するメモを格納するディレクトリです。
    - **22.md**: 特定のイシュー（例: イシュー番号22）に関する詳細なメモや検討事項を記述したMarkdownファイルです。
- **manifest.json**: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加やオフライン対応などの情報を提供します。
- **pytest.ini**: Pythonのテストフレームワークである`pytest`の設定を定義するファイルです。
- **requirements-dev.txt**: 開発環境やテスト実行時に必要となるPythonパッケージとそのバージョンを記載したファイルです。
- **requirements.txt**: プロジェクトの実行（本番環境に相当）に必要となるPythonパッケージとそのバージョンを記載したファイルです。
- **robots.txt**: 検索エンジンのクローラーに対して、サイト内のどのページをクロールしてよいか、あるいはクロールしてはならないかを指示するファイルです。
- **ruff.toml**: Pythonコードのリンター・フォーマッターである`ruff`の設定を定義するファイルです。
- **src/**: プロジェクトの主要なソースコードを格納するディレクトリです。
    - **__init__.py**: Pythonのパッケージであることを示すファイルです。
    - **generate_repo_list/**: リポジトリ一覧を生成する機能の中核となるモジュール群を格納するディレクトリです。
        - **__init__.py**: Pythonのパッケージであることを示すファイルです。
        - **badge_generator.py**: リポジトリのステータスや特性を示すバッジ（例: アクティブ、アーカイブなど）を生成するロジックを実装しています。
        - **config.yml**: リポジトリ一覧生成スクリプトの動作に関する技術的なパラメータ（例: プロジェクト概要取得の有効/無効、タイムアウト時間）を設定するファイルです。
        - **config_manager.py**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラムからアクセスできるように管理するモジュールです。
        - **date_formatter.py**: GitHub APIから取得した日付情報を、表示に適した形式に整形する機能を提供します。
        - **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインのスクリプトファイルです。
        - **json_ld_template.json**: 検索エンジン最適化 (SEO) のために、構造化データを提供するJSON-LD形式のテンプレートファイルです。
        - **language_info.py**: リポジトリで使用されているプログラミング言語に関する情報を処理（取得、集計、表示形式への変換）する機能を提供します。
        - **markdown_generator.py**: 取得したリポジトリ情報や設定に基づいて、最終的なMarkdown形式のコンテンツを生成するロジックを実装しています。
        - **project_overview_fetcher.py**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を自動で取得する機能を提供します。
        - **readme_badge_extractor.py**: リポジトリのREADMEファイルから、既存のバッジ情報などを抽出する機能を提供します。
        - **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に加工・フィルタリングする役割を担います。
        - **seo_template.yml**: Markdown生成時に、SEO関連のメタデータ（タイトル、ディスクリプションなど）を埋め込むためのテンプレート設定ファイルです。
        - **statistics_calculator.py**: 各リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
        - **strings.yml**: プロジェクト内で使用される表示メッセージや文言を一元的に管理するための設定ファイルです。
        - **template_processor.py**: Markdown生成の際に、定義されたテンプレートに変数を埋め込み、最終的な出力コンテンツを生成する機能を提供します。
        - **url_utils.py**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **test_project_overview.py**: `project_overview_fetcher.py`モジュール（プロジェクト概要取得機能）のテストを記述したスクリプトです。
- **tests/**: プロジェクト全体のテストファイルを格納するディレクトリです。
    - **conftest.py**: `pytest`のテスト実行時に共通して使用されるフィクスチャ（テストデータや環境設定）やヘルパー関数を定義するファイルです。
    - **test_badge_generator_integration.py**: バッジ生成機能の統合テストを記述したファイルです。
    - **test_check_large_files.py**: 大容量ファイルチェック機能のテストを記述したファイルです。
    - **test_config.py**: 設定ファイルの読み込みと管理機能のテストを記述したファイルです。
    - **test_date_formatter.py**: 日付フォーマット機能のテストを記述したファイルです。
    - **test_environment.py**: プロジェクトの実行環境設定に関するテストを記述したファイルです。
    - **test_integration.py**: プロジェクト全体の主要機能が連携して正しく動作するかを確認する統合テストを記述したファイルです。
    - **test_markdown_generator.py**: Markdown生成機能のテストを記述したファイルです。
    - **test_project_overview_fetcher.py**: プロジェクト概要取得機能のテストを記述したファイルです。
    - **test_readme_badge_extractor.py**: READMEからのバッジ抽出機能のテストを記述したファイルです。
    - **test_repository_processor.py**: リポジトリ情報処理機能のテストを記述したファイルです。

## 関数詳細説明
提供された情報からは、各ファイル内の具体的な関数の役割、引数、戻り値の詳細を特定できません。各ファイル名とプロジェクトの機能に基づき、推測される役割について説明します。

- **googled947dc864c270e07.html**: 関数は含まれていません。
- **src/generate_repo_list/badge_generator.py** 内の関数:
    - **役割**: リポジトリの各種情報（例: 言語、ステータス）に基づいて、視覚的なバッジ（例: Shields.io形式）を生成します。
    - **引数**: リポジトリのメタデータ、設定オプションなど。
    - **戻り値**: バッジのURLまたはMarkdown形式の文字列。
- **src/generate_repo_list/config_manager.py** 内の関数:
    - **役割**: YAMLファイル（`config.yml`, `strings.yml`など）から設定データを読み込み、プログラム全体で利用可能な形式で提供します。
    - **引数**: 設定ファイルのパス。
    - **戻り値**: 設定データを含む辞書またはオブジェクト。
- **src/generate_repo_list/date_formatter.py** 内の関数:
    - **役割**: GitHub APIから取得される日付/時刻データを、指定された形式（例: "YYYY年MM月DD日"）に整形します。
    - **引数**: 日付/時刻文字列、フォーマット指定。
    - **戻り値**: フォーマットされた日付文字列。
- **src/generate_repo_list/generate_repo_list.py** 内の関数 (メインスクリプト):
    - **役割**: GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成といったプロジェクト全体のフローを制御します。コマンドライン引数を解析し、他のモジュールを呼び出します。
    - **引数**: コマンドライン引数（`--username`, `--output`, `--limit`など）。
    - **戻り値**: なし (副作用として指定ファイルにMarkdownを出力)。
- **src/generate_repo_list/language_info.py** 内の関数:
    - **役割**: 各リポジトリで使用されているプログラミング言語の統計情報（例: 使用率）を取得し、表示に適した形式に加工します。
    - **引数**: リポジトリの言語情報（APIからの生データ）。
    - **戻り値**: 言語ごとの使用率データなど。
- **src/generate_repo_list/markdown_generator.py** 内の関数:
    - **役割**: 取得・加工されたリポジトリ情報やプロジェクト概要などを組み合わせて、最終的なMarkdown形式のリポジトリ一覧コンテンツを生成します。
    - **引数**: リポジトリデータのリスト、設定。
    - **戻り値**: 生成されたMarkdown文字列。
- **src/generate_repo_list/project_overview_fetcher.py** 内の関数:
    - **役割**: 各リポジトリの特定のパス（例: `generated-docs/project-overview.md`）にあるMarkdownファイルから、「プロジェクト概要」セクションの3行説明を抽出して取得します。
    - **引数**: リポジトリのURL、ファイルパス、抽出するセクションタイトル。
    - **戻り値**: 抽出された3行のプロジェクト概要（文字列のリスト）。
- **src/generate_repo_list/readme_badge_extractor.py** 内の関数:
    - **役割**: リポジトリのREADMEファイルの内容を解析し、既存のバッジ情報（例: ドキュメントへのリンク、ビルドステータス）を抽出します。
    - **引数**: READMEファイルのコンテンツ（文字列）。
    - **戻り値**: 抽出されたバッジ情報。
- **src/generate_repo_list/repository_processor.py** 内の関数:
    - **役割**: GitHub APIから取得した生のリポジトリデータをフィルタリングし、必要な情報を抽出し、表示に適した構造に変換します（例: フォークされたリポジトリの除外、特定の情報の追加）。
    - **引数**: GitHub APIから取得したリポジトリデータのリスト。
    - **戻り値**: 処理済みのリポジトリデータのリスト。
- **src/generate_repo_list/statistics_calculator.py** 内の関数:
    - **役割**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算または集計します。
    - **引数**: リポジトリデータ。
    - **戻り値**: 計算された統計データ。
- **src/generate_repo_list/template_processor.py** 内の関数:
    - **役割**: YAMLやJSON-LDなどのテンプレートファイルに対し、動的なデータ（リポジトリ名、URLなど）を埋め込み、最終的な出力コンテンツを生成します。
    - **引数**: テンプレートコンテンツ、埋め込むデータ。
    - **戻り値**: データが埋め込まれたコンテンツ文字列。
- **src/generate_repo_list/url_utils.py** 内の関数:
    - **役割**: URLの検証、構築、エンコード/デコードなど、URLに関連する一般的なユーティリティ機能を提供します。
    - **引数**: URL関連の文字列。
    - **戻り値**: 処理されたURL文字列。
- **.github_automation/check_large_files/scripts/check_large_files.py** 内の関数:
    - **役割**: Gitリポジトリ内のファイルサイズを検査し、設定された上限を超えるファイルがないかチェックします。
    - **引数**: リポジトリパス、サイズ上限設定。
    - **戻り値**: なし (大きいファイルがあれば警告またはエラーを出力)。
- **debug_project_overview.py** 内の関数:
    - **役割**: `project_overview_fetcher.py`が正しく動作するかを確認するための、テストまたはデバッグ用のエントリポイントや補助関数。
    - **引数**: 特定のリポジトリ名やテストデータ。
    - **戻り値**: 取得結果の表示など。
- **test_project_overview.py** および **tests/** ディレクトリ内の各テストファイル内の関数:
    - **役割**: 各モジュールや機能が期待通りに動作するか検証するためのテストケースを定義します。テスト対象の関数を呼び出し、その結果をアサート（検証）します。
    - **引数**: テスト対象の関数に応じたテストデータ。
    - **戻り値**: なし (テストフレームワークによって結果が報告される)。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-04-02 07:14:51 JST
