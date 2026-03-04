Last updated: 2026-03-05

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、個人のリポジトリ情報を自動で取得・集約するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- これにより、検索エンジンでのリポジトリの可視性を高め、大規模言語モデル（LLM）による参照精度向上に貢献します。

## 技術スタック
- フロントエンド: Jekyllは静的サイトジェネレーターとして、生成されたMarkdownファイルを美しいウェブサイトとして表示します。Markdownはリポジトリ一覧のコンテンツ形式として使用されます。
- 音楽・オーディオ: このプロジェクトでは、音楽・オーディオ関連技術は使用されていません。
- 開発ツール: Gitによるバージョン管理、GitHub APIを通じてリポジトリ情報を取得し、GitHub Pagesでウェブサイトを公開します。Pythonのテストフレームワークであるpytest、そしてPythonコードのスタイル統一と品質保持のためのRuffを使用します。
- テスト: pytestは、プロジェクト内のユニットテストおよび統合テストを実行するための標準的なフレームワークとして採用されています。
- ビルドツール: Pythonスクリプト自体がGitHub APIから情報を取得し、Jekyllで利用可能なMarkdownファイルを「ビルド」します。Jekyllは、これらのMarkdownを静的サイトとしてレンダリングします。
- 言語機能: Pythonは、GitHub APIとの連携、データ処理、Markdownファイル生成といったプロジェクトの主要ロジックを実装するための中心言語です。
- 自動化・CI/CD: GitHub Actionsが`.github_automation`ディレクトリに定義されたスクリプトを介して、コードの品質チェック（例: 大容量ファイルチェック）などの自動化プロセスを実行します。
- 開発標準: Ruffはコードの自動フォーマットとリンティングにより、一貫性のあるコードスタイルを強制し、バグを早期に検出します。`.editorconfig`ファイルは、異なる開発環境間でのコーディングスタイルの一貫性を保証します。

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
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.github_automation/`**: GitHub Actionsやその他の自動化スクリプトに関連するファイルを格納するディレクトリです。
    - **`check_large_files/README.md`**: 大容量ファイルチェック自動化機能の説明ドキュメントです。
    - **`check-large-files.toml`**: 大容量ファイルチェック機能の設定ファイルです。
    - **`scripts/check_large_files.py`**: Gitリポジトリ内の大容量ファイルをチェックするためのPythonスクリプトです。
- **`.gitignore`**: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: このプロジェクトのライセンス情報（MITライセンス）が記述されています。
- **`README.md`**: プロジェクトの概要、目的、主な機能、セットアップ方法、実行コマンド、開発者向けヒントなどが記載された主要なドキュメントです。
- **`_config.yml`**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を定義します。
- **`assets/`**: ウェブサイトで使用されるファビコンやその他の静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: 各リポジトリの`project-overview.md`からの情報取得機能をデバッグするためのスクリプトです。
- **`generated-docs/`**: 各リポジトリの`project-overview.md`ファイルが格納されることが想定されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のためのファイルです。
- **`index.md`**: このプロジェクトによって生成される、GitHub Pagesサイトのリポジトリ一覧メインページとなるMarkdownファイルです。
- **`issue-notes/22.md`**: 開発中の課題やメモを記録するためのファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）のマニフェストファイルで、ウェブアプリの名称、アイコン、表示設定などを定義します。
- **`pytest.ini`**: pytestの動作設定をカスタマイズするための設定ファイルです。
- **`requirements-dev.txt`**: 開発およびテスト環境で必要となるPythonの依存パッケージをリストアップしています。
- **`requirements.txt`**: 本番環境でこのスクリプトを実行するために必要となるPythonの依存パッケージをリストアップしています。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonのリンター/フォーマッターであるRuffの設定ファイルです。
- **`src/__init__.py`**: `src`ディレクトリをPythonパッケージとして認識させるためのファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - **`badge_generator.py`**: リポジトリの言語やステータスを示すバッジ（アイコン）を生成するロジックを扱います。
    - **`config.yml`**: プロジェクトの実行時設定（例: プロジェクト概要取得機能の有効/無効、対象ファイルなど）を定義するファイルです。
    - **`config_manager.py`**: `config.yml`や`strings.yml`などの設定ファイルを読み込み、管理する役割を担います。
    - **`date_formatter.py`**: 日付や時刻の表示形式を整形するユーティリティ関数を提供します。
    - **`generate_repo_list.py`**: プロジェクトのメインエントリーポイントとなるスクリプトで、リポジトリ情報の取得からMarkdown生成までの一連の処理を調整します。
    - **`json_ld_template.json`**: SEO向上のためにウェブページに構造化データ（JSON-LD形式）を埋め込むためのテンプレートファイルです。
    - **`language_info.py`**: GitHub APIから取得したリポジトリの言語情報を処理し、表示可能な形式に変換するロジックを扱います。
    - **`markdown_generator.py`**: 処理されたリポジトリ情報をもとに、最終的なMarkdownコンテンツを生成するロジックをカプセル化しています。
    - **`project_overview_fetcher.py`**: 各リポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要のテキストを抽出する機能を担当します。
    - **`readme_badge_extractor.py`**: リポジトリのREADMEファイルからバッジ（shields.ioなど）の情報を解析・抽出するロジックを提供します。
    - **`repository_processor.py`**: GitHub APIから取得した生のリポジトリデータを整形、フィルタリング、追加情報付与などの処理を行う中心的なモジュールです。
    - **`seo_template.yml`**: 検索エンジン最適化（SEO）のためのメタデータやテンプレート設定を定義するファイルです。
    - **`statistics_calculator.py`**: リポジトリのスター数、フォーク数、最終更新日などの統計情報を計算・集計するロジックを提供します。
    - **`strings.yml`**: アプリケーション内で使用される表示メッセージや文言を一元管理し、多言語対応や文言変更を容易にします。
    - **`template_processor.py`**: Markdownテンプレートに変数を適用し、動的なコンテンツを生成する処理を担います。
    - **`url_utils.py`**: URLの生成、解析、検証など、URLに関連する様々なユーティリティ関数を提供します。
- **`test_project_overview.py`**: `project_overview_fetcher`機能のユニットテストを記述したスクリプトです。
- **`tests/`**: プロジェクトのテストスクリプトを格納するディレクトリです。
    - **`test_badge_generator_integration.py`**: バッジ生成機能の統合テストです。
    - **`test_check_large_files.py`**: 大容量ファイルチェック機能のテストです。
    - **`test_config.py`**: 設定ファイル（`config.yml`など）の読み込みと解析に関するテストです。
    - **`test_date_formatter.py`**: 日付フォーマットユーティリティのテストです。
    - **`test_environment.py`**: 実行環境のセットアップや依存関係に関するテストです。
    - **`test_integration.py`**: プロジェクトの主要な機能が連携して正しく動作するかを確認する統合テストです。
    - **`test_markdown_generator.py`**: Markdown生成ロジックのテストです。
    - **`test_project_overview_fetcher.py`**: プロジェクト概要取得機能のテストです。
    - **`test_readme_badge_extractor.py`**: READMEからのバッジ抽出機能のテストです。
    - **`test_repository_processor.py`**: リポジトリ情報処理ロジックのテストです。

## 関数詳細説明
提供された情報からは具体的な関数シグネチャ（引数、戻り値）を抽出できませんでしたが、各ファイルの役割に基づき、主要な関数とその機能を説明します。

- **`generate_repo_list.py`**
    - **`main()`**: プロジェクト全体の実行フローを制御するメイン関数です。コマンドライン引数を解析し、リポジトリ情報の取得からMarkdownファイルの生成までの一連の処理を調整します。
        - 引数: コマンドライン引数（ユーザー名、出力ファイル名、リミットなど）。
        - 戻り値: なし（直接ファイルに出力）。
- **`repository_processor.py`**
    - **`fetch_repositories(username, token)`**: GitHub APIを介して指定されたユーザーのリポジトリ情報を取得します。
        - 引数: `username` (GitHubユーザー名), `token` (GitHub認証トークン)。
        - 戻り値: 取得したリポジトリデータのリスト。
    - **`process_repository_data(repo_data)`**: 取得したリポジトリの生データを整形し、Markdown生成に適した形式に処理します。
        - 引数: `repo_data` (生のGitHubリポジトリデータ)。
        - 戻り値: 処理済みのリポジトリ情報。
- **`markdown_generator.py`**
    - **`generate_markdown_output(repositories, template_data)`**: 処理されたリポジトリ情報とテンプレートデータを用いて、最終的なMarkdown形式の文字列を生成します。
        - 引数: `repositories` (処理済みリポジトリ情報のリスト), `template_data` (SEOテンプレートなどの追加データ)。
        - 戻り値: 生成されたMarkdown文字列。
- **`project_overview_fetcher.py`**
    - **`fetch_project_overview(repo_url, file_path, config)`**: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクト概要の3行説明を抽出します。
        - 引数: `repo_url` (リポジトリのURL), `file_path` (概要ファイルへのパス), `config` (設定オブジェクト)。
        - 戻り値: 抽出されたプロジェクト概要の文字列、または空文字列。
- **`config_manager.py`**
    - **`load_config(config_path)`**: 指定されたパスからYAML設定ファイル（例: `config.yml`, `strings.yml`）を読み込みます。
        - 引数: `config_path` (設定ファイルへのパス)。
        - 戻り値: 読み込まれた設定を格納する辞書またはオブジェクト。
- **`badge_generator.py`**
    - **`create_badge(label, message, color)`**: 指定されたラベル、メッセージ、色に基づいてバッジのMarkdownまたはURLを生成します。
        - 引数: `label` (バッジの左側のテキスト), `message` (バッジの右側のテキスト), `color` (バッジの色)。
        - 戻り値: 生成されたバッジのMarkdownまたはURL文字列。
- **`date_formatter.py`**
    - **`format_date(date_obj, format_string)`**: 日付オブジェクトを指定されたフォーマット文字列に従って整形します。
        - 引数: `date_obj` (日付オブジェクト), `format_string` (整形文字列)。
        - 戻り値: 整形された日付文字列。
- **`readme_badge_extractor.py`**
    - **`extract_badges_from_readme(readme_content)`**: リポジトリのREADMEコンテンツから、shields.ioなどのバッジのURLや情報を解析して抽出します。
        - 引数: `readme_content` (READMEファイルのテキスト内容)。
        - 戻り値: 抽出されたバッジ情報のリスト。
- **`statistics_calculator.py`**
    - **`calculate_repo_stats(repo_data)`**: リポジトリのスター数、フォーク数、ウォッチ数などの統計情報を計算し、追加します。
        - 引数: `repo_data` (単一のリポジトリデータ)。
        - 戻り値: 統計情報が追加されたリポジトリデータ。
- **`template_processor.py`**
    - **`apply_template(template_content, data)`**: 提供されたテンプレートコンテンツに変数を適用し、最終的な出力テキストを生成します。
        - 引数: `template_content` (テンプレート文字列), `data` (テンプレートに埋め込むデータ辞書)。
        - 戻り値: 変数が適用された文字列。
- **`url_utils.py`**
    - **`construct_github_repo_url(username, repo_name)`**: GitHubリポジトリへの完全なURLを構築します。
        - 引数: `username` (GitHubユーザー名), `repo_name` (リポジトリ名)。
        - 戻り値: 構築されたURL文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-05 07:10:28 JST
