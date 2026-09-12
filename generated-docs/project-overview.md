Last updated: 2026-09-13

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のリポジトリ情報を自動で取得・処理するシステムです。
- 取得した情報からGitHub Pagesサイト向けのSEO最適化されたリポジトリ一覧Markdownを生成します。
- 検索エンジンへのインデックス化を促進し、LLMによるリポジトリ参照の信頼性向上に貢献します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤として使用され、生成されたMarkdownファイルを静的サイトとしてビルドします。
    - **Markdown**: リポジトリ一覧の出力形式であり、JekyllによってHTMLに変換されます。
- 音楽・オーディオ: なし
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報取得およびMarkdown生成スクリプトがPyhonで実装されています。
    - **GitHub API**: GitHub上のリポジトリ情報をプログラムから取得するために使用されます。
- テスト:
    - **pytest**: Pythonコードの単体テストおよび結合テストフレームワークとして利用されています。
- ビルドツール:
    - (直接的なビルドツールはなし): Pythonスクリプト自体がMarkdownファイルを「生成」する役割を担います。JekyllはGitHub Pages側でマークダウンをHTMLにビルドします。
- 言語機能:
    - **Python**: スクリプトの記述と実行に利用されるプログラミング言語です。
- 自動化・CI/CD:
    - **GitHub Actions**: `.github_automation`ディレクトリの存在から、将来的な自動化や継続的統合の基盤として意図されています。現在のプロジェクトではローカル開発が重視されています。
- 開発標準:
    - **Ruff**: Pythonコードのスタイルチェックとフォーマットを自動化し、コード品質と一貫性を維持するために使用されます。

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
-   `.editorconfig`: 異なるエディタやIDE間でコードスタイル（インデント、エンコーディングなど）を統一するための設定ファイル。
-   `.github_automation/`: GitHub Actionsなどの自動化スクリプトを格納するディレクトリ。
    -   `check_large_files/`: 大容量ファイルチェックに関するスクリプト群を格納。
        -   `README.md`: `check_large_files`機能の概要や使用方法を説明するドキュメント。
        -   `check-large-files.toml`: 大容量ファイルチェックの具体的な設定（閾値、対象ファイルなど）を定義するTOML形式の設定ファイル。
        -   `scripts/check_large_files.py`: 指定された設定に基づき、リポジトリ内の大容量ファイルを検出するPythonスクリプト。
-   `.gitignore`: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイル。
-   `LICENSE`: プロジェクトがMITライセンスであることを明記したファイル。
-   `README.md`: プロジェクトの目的、機能、セットアップ方法、使用方法などを記述したプロジェクトのメインドキュメント。
-   `_config.yml`: Jekyllサイト全体の設定を定義するファイル。テーマ、プラグイン、変数の設定などが含まれます。
-   `assets/`: GitHub Pagesサイトで使用される画像、ファビコンなどの静的アセットを格納するディレクトリ。
    -   `favicon-*.png`: ウェブサイトのアイコンとしてブラウザのタブやブックマークに表示される画像ファイル。
-   `debug_project_overview.py`: `project_overview_fetcher`モジュールのデバッグやテスト実行に使用されるPythonスクリプト。
-   `generated-docs/`: 生成されたドキュメントや一時的に出力されたファイルを格納するためのディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleによるサイト所有権の確認に使用されるHTMLファイル。
-   `index.md`: メインの出力ファイル。`generate_repo_list.py`によって生成されたリポジトリ一覧のMarkdownコンテンツがここに書き込まれ、Jekyllによってウェブページとして公開されます。
-   `issue-notes/`: 開発中の課題やメモを管理するためのディレクトリ。
    -   `22.md`: 特定の課題（例: Issue #22）に関する詳細なノートや検討事項を記述したMarkdownファイル。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の定義ファイル。アプリのメタデータ、アイコン、表示設定などを記述します。
-   `pytest.ini`: `pytest`テストフレームワークの挙動をカスタマイズするための設定ファイル。
-   `requirements-dev.txt`: 開発およびテスト環境で必要となるPythonパッケージとそのバージョンをリストアップしたファイル。
-   `requirements.txt`: プロジェクトの実行に必要な本番環境のPythonパッケージとそのバージョンをリストアップしたファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、サイトのどの部分をクロールすべきか、またはすべきでないかを指示するファイル。
-   `ruff.toml`: Pythonの高速リンター/フォーマッターである`Ruff`の設定ファイル。コードスタイルや静的解析のルールを定義します。
-   `src/`: プロジェクトの主要なソースコードを格納するディレクトリ。
    -   `__init__.py`: Pythonパッケージであることを示すファイル。
    -   `generate_repo_list/`: リポジトリ一覧生成システムの核心部分を構成するPythonモジュール群を格納。
        -   `__init__.py`: `generate_repo_list`パッケージであることを示すファイル。
        -   `badge_generator.py`: プロジェクトの言語やステータスに応じたバッジのMarkdownを生成する機能を提供します。
        -   `config.yml`: リポジトリ一覧生成スクリプトの技術的パラメータ（例: プロジェクト概要取得機能の設定）を定義するYAML形式の設定ファイル。
        -   `config_manager.py`: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理する役割を担うモジュール。
        -   `date_formatter.py`: GitHub APIから取得した日付情報を人間が読める形式に整形する機能を提供します。
        -   `generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプト。GitHub APIからリポジトリ情報を取得し、他のモジュールを協調させてMarkdownファイルを生成します。
        -   `json_ld_template.json`: 構造化データ（JSON-LD）のテンプレートファイル。SEOを目的としたメタデータ生成に使用されます。
        -   `language_info.py`: プログラミング言語に関する情報（例: アイコン、色）を管理・取得するモジュール。
        -   `markdown_generator.py`: 処理されたリポジトリ情報から最終的なMarkdownコンテンツを構築するモジュール。
        -   `project_overview_fetcher.py`: 各リポジトリの`generated-docs/project-overview.md`からプロジェクト概要の3行説明を抽出する機能を提供します。
        -   `readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、特定のバッジ情報を抽出する機能を提供します。
        -   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に適した形式に加工・整形する役割を担います。
        -   `seo_template.yml`: SEO関連のメタデータ（タイトル、ディスクリプションなど）のテンプレートや設定を定義するYAMLファイル。
        -   `statistics_calculator.py`: リポジトリに関する様々な統計情報（例: スター数、フォーク数）を計算するモジュール。
        -   `strings.yml`: UIに表示されるメッセージや文言を一元的に管理するためのYAMLファイル。多言語対応や文言変更を容易にします。
        -   `template_processor.py`: JekyllテンプレートやMarkdownテンプレートを処理し、動的にコンテンツを埋め込む機能を提供します。
        -   `url_utils.py`: URLの構築、解析、検証など、URLに関連するユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプト。
-   `tests/`: プロジェクト全体のテストコードを格納するディレクトリ。
    -   `conftest.py`: `pytest`の共通フィクスチャやヘルパー関数を定義し、複数のテストファイルで共有可能にします。
    -   `test_badge_generator_integration.py`: `badge_generator`モジュールの結合テスト。
    -   `test_check_large_files.py`: `.github_automation/check_large_files`機能のテスト。
    -   `test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理機能のテスト。
    -   `test_date_formatter.py`: `date_formatter`モジュールの日付整形機能のテスト。
    -   `test_environment.py`: プロジェクトの実行環境に関する設定や依存関係のテスト。
    -   `test_integration.py`: システム全体の主要な連携部分の統合テスト。
    -   `test_markdown_generator.py`: `markdown_generator`モジュールのMarkdown生成機能のテスト。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールのテスト。
    -   `test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールのテスト。
    -   `test_repository_processor.py`: `repository_processor`モジュールのリポジトリ情報処理機能のテスト。

## 関数詳細説明
このプロジェクトは複数のPythonモジュールで構成されており、各モジュールが特定の役割を担う関数群を提供します。ここでは主要な処理を担うであろう関数について、その役割、引数、および戻り値を推測して説明します。

-   **`generate_repo_list.py`内のメイン処理関数 (例: `main`関数)**
    -   **役割**: プロジェクト全体のエントリポイントとして機能し、GitHub APIからのリポジトリ情報取得、データの処理、Markdownコンテンツの生成、そしてファイルへの出力という一連のプロセスをオーケストレートします。
    -   **引数**:
        -   `username` (str): GitHubユーザー名。取得対象のリポジトリ所有者を指定します。
        -   `output_file` (str): 生成されたMarkdownコンテンツを書き込むファイルパス。
        -   `limit` (int, optional): 処理するリポジトリ数の上限（開発・テスト目的）。デフォルトは無制限。
    -   **戻り値**: なし（実行結果として指定されたファイルにMarkdownが書き込まれます）。

-   **`project_overview_fetcher.py`内の概要取得関数 (例: `fetch_project_overview`)**
    -   **役割**: 指定されたGitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのプロジェクトの3行概要を抽出して返します。APIリクエストやファイル内容の解析を含みます。
    -   **引数**:
        -   `repo_full_name` (str): 対象リポジトリのフルネーム（例: "cat2151/my-repo"）。
        -   `config` (dict): `project_overview`機能に関する設定情報（`target_file`, `section_title`など）。
    -   **戻り値**: `str`または`None`。抽出された3行概要の文字列、または概要が見つからなかった/取得できなかった場合は`None`。

-   **`markdown_generator.py`内のMarkdown生成関数 (例: `generate_repo_list_markdown`)**
    -   **役割**: 処理済みのリポジトリ情報のリストを受け取り、SEOテンプレートやバッジ情報などを組み合わせて、最終的なリポジトリ一覧のMarkdownテキストを生成します。
    -   **引数**:
        -   `repositories` (list[dict]): 各リポジトリの整形済み情報を含む辞書のリスト。
        -   `config` (dict): Markdown生成に必要な設定情報。
        -   `strings` (dict): 表示に使用する文言文字列の辞書。
    -   **戻り値**: `str`。生成された完全なMarkdownコンテンツ。

-   **`repository_processor.py`内のリポジトリ情報処理関数 (例: `process_repository_data`)**
    -   **役割**: GitHub APIから取得した個々の生のリポジトリデータ（JSON形式）を受け取り、日付の整形、バッジ情報の追加、プロジェクト概要のフェッチなどを行い、ウェブページ表示に適した形式に加工・整形します。
    -   **引数**:
        -   `raw_repo` (dict): GitHub APIから取得した1つのリポジトリに関する生データ。
        -   `config` (dict): リポジトリ処理に必要な設定情報。
        -   `project_overview_fetcher` (callable): プロジェクト概要取得のための関数。
        -   `badge_generator` (callable): バッジ生成のための関数。
    -   **戻り値**: `dict`。整形され、追加情報が付与されたリポジトリデータ。

-   **`badge_generator.py`内のバッジ生成関数 (例: `generate_badge_markdown`)**
    -   **役割**: プログラミング言語やリポジトリのステータス（アクティブ、アーカイブ、フォークなど）に基づいて、対応するバッジのMarkdown形式の文字列を生成します。
    -   **引数**:
        -   `language` (str, optional): リポジトリの主要なプログラミング言語。
        -   `is_archived` (bool): リポジトリがアーカイブされているかを示す真偽値。
        -   `is_fork` (bool): リポジトリがフォークであるかを示す真偽値。
    -   **戻り値**: `str`。生成されたバッジのMarkdown文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-09-13 07:15:45 JST
