Last updated: 2026-06-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用してリポジトリ情報を取得し、Jekyll向けMarkdownを自動生成するシステムです。
- GitHub Pagesに公開することで、SEOを最適化し、検索エンジンやLLMによる参照性を向上させます。
- 各リポジトリの概要、技術バッジ、カテゴリ分類など、豊富な情報を自動で提供します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 静的サイトジェネレーターとして、生成されたMarkdownからウェブサイトを構築し公開します。
- 音楽・オーディオ: なし - 音楽・オーディオ関連の技術は使用していません。
- 開発ツール:
    - Python: プロジェクトの主要なスクリプト言語として、GitHub APIからのデータ取得、加工、Markdown生成に利用されます。
    - GitHub API: GitHubのリポジトリ情報（名前、説明、言語、スター数など）をプログラムから取得するためのRESTful APIです。
- テスト:
    - pytest: Pythonアプリケーションのテストフレームワーク。単体テストや結合テストの実行に利用され、コードの品質を保証します。
- ビルドツール:
    - Markdown: プロジェクトが生成する主要なコンテンツ形式であり、JekyllによってGitHub Pages上で静的サイトに変換されます。
- 言語機能:
    - YAML: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`など）の記述に用いられ、設定値の管理を容易にします。
    - TOML: シークレット情報（`secrets.toml`）や一部の設定ファイル（`ruff.toml`, `pytest.ini`）の記述に使用されます。
- 自動化・CI/CD:
    - GitHub Actions: `.github_automation`ディレクトリの存在から、補助的にコード品質チェックや自動デプロイメントなどのCI/CDワークフローに利用される可能性があります。
- 開発標準:
    - ruff: Pythonコードのフォーマットとリンティングを自動的に行い、一貫したコードスタイルと品質を維持するツールです。
    - .editorconfig: 異なるエディタやIDEを使用する開発者間で、インデントスタイルや文字コードなど、一貫したコーディング規約を強制するための設定ファイルです。

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
- **`.editorconfig`**: 複数の開発環境でコードのスタイル（インデント、改行コードなど）を統一するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsなどの自動化スクリプトや設定を格納するディレクトリです。
    - **`check_large_files/`**: リポジトリ内の大容量ファイルをチェックする機能に関連するファイル群です。
        - **`README.md`**: `check_large_files`機能に関する説明ドキュメントです。
        - **`check-large-files.toml`**: 大容量ファイルチェックツールの設定を定義するTOMLファイルです。
        - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルを検出するためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定する設定ファイルです。
- **`LICENSE`**: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- **`README.md`**: プロジェクト全体の目的、使い方、セットアップ方法などを記述したメインのドキュメントファイルです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: ウェブサイトで使用されるファビコンなどの静的アセットを格納するディレクトリです。
    - **`favicon-*.png`**: ブラウザのタブなどに表示されるサイトアイコン（ファビコン）の各種サイズ画像ファイルです。
- **`debug_project_overview.py`**: `project_overview_fetcher`モジュールの動作をデバッグするための補助スクリプトです。
- **`generated-docs/`**: 本プロジェクトによって生成されるドキュメントや、Jekyllで扱われる一時的なドキュメントを格納するためのプレースホルダーディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleでサイトの所有権を確認するために使用される検証ファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。本プロジェクトが生成するリポジトリ一覧がこのファイルに書き込まれます。
- **`issue-notes/`**: プロジェクトの課題や検討事項に関するメモを格納するディレクトリです。
    - **`22.md`**: 特定の課題（おそらくIssue番号22）に関する詳細なメモや議論が記述されたMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の定義ファイルで、ホーム画面アイコンや表示設定などを指定します。
- **`pytest.ini`**: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの実行オプションや検出ルールなどを定義します。
- **`requirements-dev.txt`**: 開発時およびテスト実行時に必要なPythonライブラリのリストを定義するファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために最低限必要なPythonライブラリのリストを定義するファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはならないかを指示するファイルです。
- **`ruff.toml`**: Pythonコードのリンター・フォーマッターである`ruff`の設定ファイルです。コードスタイルや静的解析のルールを定義します。
- **`src/`**: プロジェクトの主要なPythonソースコードを格納するディレクトリです。
    - **`__init__.py`**: `src`ディレクトリがPythonパッケージであることを示します。
    - **`generate_repo_list/`**: リポジトリ一覧を生成するロジックの中核を担うPythonパッケージです。
        - **`__init__.py`**: `generate_repo_list`ディレクトリがPythonパッケージであることを示します。
        - **`badge_generator.py`**: リポジトリのステータスや技術スタックを示すバッジ（例: アクティブ、アーカイブ、言語アイコン）を生成する機能を提供します。
        - **`config.yml`**: リポジトリ一覧生成スクリプトの動作を制御する設定（例: プロジェクト概要取得の有効/無効、ファイルパス）を定義するYAMLファイルです。
        - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、設定値にアクセスするためのユーティリティモジュールです。
        - **`date_formatter.py`**: 日付や時刻の情報を特定のフォーマットに整形するための関数を提供するモジュールです。
        - **`generate_repo_list.py`**: GitHub APIからリポジトリ情報を取得し、整形されたMarkdownファイルを指定されたパスに出力するメインの実行スクリプトです。
        - **`json_ld_template.json`**: SEO強化のため、検索エンジンに構造化データを提供するJSON-LD（Linked Data）のテンプレートを定義するファイルです。
        - **`language_info.py`**: 各プログラミング言語に関する詳細情報（例: 言語の色、アイコン）を管理・提供するモジュールです。
        - **`markdown_generator.py`**: 処理されたリポジトリ情報とテンプレートを組み合わせて、最終的なリポジトリ一覧のMarkdownコンテンツを生成するモジュールです。
        - **`project_overview_fetcher.py`**: 各リポジトリの特定のファイル（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出する機能を提供します。
        - **`readme_badge_extractor.py`**: リポジトリの`README.md`ファイルから、既存のバッジ（例: ビルドステータス、ライセンス）を検出・抽出するモジュールです。
        - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形する役割を持つモジュールです。
        - **`seo_template.yml`**: SEO関連のメタデータや、検索エンジン向けのコンテンツ生成に利用されるテンプレート設定を定義するYAMLファイルです。
        - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数などの統計情報を計算・集計するためのモジュールです。
        - **`strings.yml`**: 生成されるMarkdownやUIに表示される様々なメッセージ、ラベル、文言を集中管理するためのYAMLファイル（多言語対応を想定）。
        - **`template_processor.py`**: Markdown生成に使用されるテンプレートファイル（例: `seo_template.yml`）を読み込み、データに基づいてレンダリングする機能を提供します。
        - **`url_utils.py`**: URLの構築、検証、解析など、URLに関連する共通のユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストコードを格納するディレクトリです。
    - **`conftest.py`**: `pytest`のテスト実行において、共通のフィクスチャや設定を定義するファイルです。
    - **`test_badge_generator_integration.py`**: `badge_generator`モジュールの結合テストを行い、他のコンポーネントとの連携を確認します。
    - **`test_check_large_files.py`**: `check_large_files.py`スクリプトの機能テストを行います。
    - **`test_config.py`**: 設定ファイルの読み込みや管理機能が正しく動作するかを検証します。
    - **`test_date_formatter.py`**: 日付整形機能の単体テストを行います。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係が正しく機能するかを検証します。
    - **`test_integration.py`**: プロジェクトの主要な機能がエンドツーエンドで正しく連携し動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成機能が期待通りの出力を生成するかを検証します。
    - **`test_project_overview_fetcher.py`**: `project_overview_fetcher`モジュールがプロジェクト概要を正しく抽出するかを検証します。
    - **`test_readme_badge_extractor.py`**: `readme_badge_extractor`モジュールがREADMEからバッジ情報を正しく抽出するかを検証します。
    - **`test_repository_processor.py`**: リポジトリ情報処理機能がGitHub APIデータを正しく整形するかを検証します。

## 関数詳細説明
提供されたプロジェクト情報から具体的な関数シグネチャは検出されませんでしたが、ファイル名とプロジェクトの目的から推測される主要な関数とその役割を以下に示します。

-   **`generate_repo_list.py` (主要関数: `main` または `generate_repo_list`)**
    -   **役割**: GitHub APIからリポジトリ情報を取得し、JekyllベースのGitHub Pagesサイト用にMarkdown形式のリポジトリ一覧ファイルを生成する、プロジェクトの中心的な実行関数です。
    -   **引数**: `username` (GitHubユーザー名), `output_file` (生成されるMarkdownファイル名), `limit` (処理するリポジトリ数の上限、開発用) などを受け取ると考えられます。
    -   **戻り値**: 通常、ファイル出力が主目的であるため、明示的な値を返さない（`None`）か、処理結果のステータスコードを返すと推測されます。
    -   **機能**: 設定ファイルの読み込み、GitHub APIへのリクエスト、取得データの加工、他のモジュール（`repository_processor`, `markdown_generator`など）との連携、最終的なMarkdownファイルのディスクへの書き出しを行います。

-   **`badge_generator.py` (主要関数: `generate_badge_markdown`)**
    -   **役割**: リポジトリの特性（例: アクティブ/アーカイブ、主要言語）に応じたバッジのMarkdown文字列を生成します。
    -   **引数**: リポジトリのステータス、言語、特定のキーワードなどの情報を受け取ると考えられます。
    -   **戻り値**: 生成されたバッジのMarkdown形式の文字列を返すと推測されます。
    -   **機能**: 入力された情報に基づき、予め定義されたルールに従って適切なバッジ（例: Shields.io形式）のMarkdownを構築します。

-   **`config_manager.py` (主要関数: `load_config`, `get_setting`)**
    -   **役割**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、プログラム全体で設定値にアクセスするためのインターフェースを提供します。
    -   **引数**: `file_path` (設定ファイルのパス), `key` (取得したい設定のキー) などを受け取ると考えられます。
    -   **戻り値**: `load_config`は設定オブジェクト（辞書など）を、`get_setting`は指定されたキーの値またはデフォルト値を返すと推測されます。
    -   **機能**: YAMLファイルをパースし、アプリケーション全体から設定値を取得するためのシンプルなAPIを提供することで、設定の一元管理を実現します。

-   **`date_formatter.py` (主要関数: `format_datetime`)**
    -   **役割**: 日付や時刻の情報を、指定された形式の文字列に変換します。
    -   **引数**: `datetime_obj` (日付/時刻オブジェクト), `format_string` (出力形式を指定する文字列) などを受け取ると考えられます。
    -   **戻り値**: フォーマットされた日付時刻の文字列を返すと推測されます。
    -   **機能**: GitHub APIから取得されるISO 8601形式などの日付文字列を、ユーザーフレンドリーな表示形式に変換します。

-   **`language_info.py` (主要関数: `get_language_details`)**
    -   **役割**: プログラミング言語に関する追加情報（例: 言語ごとの表示色、関連アイコン）を提供します。
    -   **引数**: `language_name` (プログラミング言語名) を受け取ると考えられます。
    -   **戻り値**: 言語の色、ウェブサイトのリンク、アイコンパスなどを含む辞書を返すと推測されます。
    -   **機能**: 内部データストアや設定に基づいて、各言語に紐づく詳細情報を検索し提供することで、リポジトリ一覧の視覚的表現を豊かにします。

-   **`markdown_generator.py` (主要関数: `generate_repo_list_markdown`)**
    -   **役割**: 処理済みリポジトリデータのリストとテンプレート情報を使用して、最終的なリポジトリ一覧のMarkdownコンテンツを生成します。
    -   **引数**: `repositories_data` (整形されたリポジトリ情報のリスト), `template_name` (使用するテンプレートの名前) などを受け取ると考えられます。
    -   **戻り値**: 生成されたMarkdownコンテンツの文字列を返すと推測されます。
    -   **機能**: テンプレートエンジン（例: Jinja2）を利用し、リポジトリデータをテンプレートのプレースホルダーに埋め込み、見出し、バッジ、リンクなどを含む構造化されたMarkdownを構築します。

-   **`project_overview_fetcher.py` (主要関数: `fetch_project_overview_from_repo`)**
    -   **役割**: 各GitHubリポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、プロジェクトの3行概要を自動的に抽出します。
    -   **引数**: `repo_owner` (リポジトリ所有者), `repo_name` (リポジトリ名), `github_token` (GitHub API認証トークン), `config` (ファイルパスやセクションタイトルなどの設定) などを受け取ると考えられます。
    -   **戻り値**: 抽出された3行の概要を要素とするリスト（または空のリスト）を返すと推測されます。
    -   **機能**: GitHub APIを介してリポジトリのファイル内容を取得し、正規表現や文字列操作を用いて、指定されたセクション（例: "## プロジェクト概要"）の下にあるリストアイテムを解析します。

-   **`readme_badge_extractor.py` (主要関数: `extract_badges_from_readme`)**
    -   **役割**: リポジトリの`README.md`ファイルから、既に埋め込まれているバッジ（例: ビルドステータス、ライセンスバッジ）の情報を抽出します。
    -   **引数**: `readme_content` (READMEファイルの文字列コンテンツ) を受け取ると考えられます。
    -   **戻り値**: 抽出されたバッジのURLやAltテキストなどの情報を含むリストを返すと推測されます。
    -   **機能**: Markdownの画像リンク構文（`![alt text](url)`）を解析し、バッジに該当するものを識別します。

-   **`repository_processor.py` (主要関数: `process_single_repository`, `process_all_repositories`)**
    -   **役割**: GitHub APIから取得した生のリポジトリデータ（JSON形式）を、Markdown生成に適した、より構造化されたクリーンな形式に加工・整形します。
    -   **引数**: `raw_repo_data` (GitHub APIから取得した単一リポジトリのJSONデータ), `github_token` (プロジェクト概要取得などに利用) などを受け取ると考えられます。
    -   **戻り値**: 必要な情報のみが抽出・計算された、整形済みのリポジトリ情報オブジェクト（辞書など）を返すと推測されます。
    -   **機能**: 不要なフィールドの除去、言語情報の集計、最終更新日の整形、`project_overview_fetcher`からの概要取得など、複数の処理をオーケストレーションしてデータを準備します。

-   **`statistics_calculator.py` (主要関数: `calculate_repository_stats`)**
    -   **役割**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算または集計します。
    -   **引数**: `repo_data` (整形済みリポジトリデータ) を受け取ると考えられます。
    -   **戻り値**: 計算された統計情報を含む辞書を返すと推測されます。
    -   **機能**: APIから提供される数値データを基に、必要に応じて合計や平均などの簡単な集計処理を実行します。

-   **`template_processor.py` (主要関数: `load_template`, `render_template_with_data`)**
    -   **役割**: Markdown生成時に使用するテンプレートファイル（例: リポジトリごとの表示形式）を読み込み、提供されたデータに基づいてレンダリングします。
    -   **引数**: `template_path` (テンプレートファイルのパス), `data` (テンプレートに埋め込むデータ) などを受け取ると考えられます。
    -   **戻り値**: データが埋め込まれてレンダリングされた文字列を返すと推測されます。
    -   **機能**: テンプレートエンジンと連携し、プレースホルダーを実際の値に置き換えることで、動的なコンテンツ生成を可能にします。

-   **`url_utils.py` (主要関数: `build_github_repo_url`, `is_valid_url`)**
    -   **役割**: GitHubリポジトリのURL構築、一般的なURLの検証や解析など、URLに関連するユーティリティ機能を提供します。
    -   **引数**: `owner`, `repo_name` (URL構築用), `url_string` (検証用) などを受け取ると考えられます。
    -   **戻り値**: 構築された完全なURL文字列や、URLの有効性を示す真偽値を返すと推測されます。
    -   **機能**: 各リポジトリのGitHub Pagesへのリンクや、GitHubリポジトリ本体へのリンクを正確に生成します。

## 関数呼び出し階層ツリー
```
（関数呼び出し階層の分析情報は提供されていないため、表示できません。）

---
Generated at: 2026-06-08 07:27:08 JST
