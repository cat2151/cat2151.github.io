Last updated: 2025-11-26

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けに、ユーザーのリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用してリポジトリ情報を取得し、SEOに最適化されたMarkdownファイルを生成します。
- これにより、リポジトリの検索エンジンによるインデックス化を促進し、LLMからの参照性を向上させます。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) を基盤として、生成されたMarkdownファイルを表示します。直接的なフロントエンドフレームワークは使用せず、静的サイト生成の手法を採用しています。
- 音楽・オーディオ: このプロジェクトでは音楽・オーディオ関連技術は使用していません。
- 開発ツール:
    - Python: 主要なプログラミング言語として、リポジトリ情報の取得、処理、Markdown生成ロジックを実装しています。
    - GitHub API: リポジトリの公開情報や各リポジトリの特定のファイル（`project-overview.md`）を取得するために使用します。
- テスト:
    - pytest: Pythonコードの単体テスト、統合テストを行うためのフレームワークです。テストの自動化と品質保証に貢献します。
- ビルドツール:
    - Pythonスクリプト: `generate_repo_list.py`がリポジトリ情報の取得からMarkdown出力までを一貫して行い、実質的なコンテンツ生成（ビルド）を担います。
- 言語機能:
    - Python: メインのプログラミング言語。
    - YAML: 設定ファイル（`config.yml`, `strings.yml`, `seo_template.yml`）や、Jekyllのサイト設定（`_config.yml`）で使用されます。
    - Markdown: 生成されるリポジトリ一覧の出力形式です。Jekyllと組み合わせてウェブページとして表示されます。
    - TOML: 秘密情報（GitHubトークンなど）の管理に利用されます。
- 自動化・CI/CD:
    - 自動化スクリプト: Pythonスクリプト自体がリポジトリ一覧生成の自動化プロセスを提供します。現状はローカルでの開発・実行に重点を置いています。
- 開発標準:
    - Ruff: Pythonコードのフォーマットとリンティング（静的解析）を行うツールです。コードスタイルの一貫性を保ち、品質を向上させます。

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
📖 index.md
📁 issue-notes/
  📖 10.md
  📖 12.md
  📖 14.md
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
  📄 test_environment.py
  📄 test_integration.py
  📄 test_markdown_generator.py
  📄 test_project_overview_fetcher.py
  📄 test_repository_processor.py
```

## ファイル詳細説明
- **`.editorconfig`**: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象から除外するファイルやディレクトリを指定するファイルです。
- **`LICENSE`**: プロジェクトのライセンス情報（MITライセンス）を記載したファイルです。
- **`README.md`**: プロジェクトの目的、機能、セットアップ方法、実行方法、開発者向けのヒントなどを記述した、プロジェクトの入り口となるドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成を設定するファイルです。サイトのタイトル、テーマ、プラグインなどの設定を含みます。
- **`assets/`**: ウェブサイトで使用される画像（ファビコンなど）のような静的アセットを格納するディレクトリです。
- **`debug_project_overview.py`**: プロジェクト概要取得機能の動作確認やデバッグを目的とした補助スクリプトです。
- **`generated-docs/`**: 生成されたMarkdownファイルや関連ドキュメントが出力されることを想定したディレクトリです。
- **`index.md`**: メインのリポジトリ一覧ページとして生成されるMarkdownファイルです。GitHub Pagesで公開されます。
- **`issue-notes/`**: 開発中の課題、アイデア、メモなどを個別のMarkdownファイルとして記録しておくためのディレクトリです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の情報を定義するファイルで、ホーム画面への追加やオフライン対応などを可能にします。
- **`pytest.ini`**: Pythonのテストフレームワークであるpytestの挙動を設定するファイルです。
- **`requirements-dev.txt`**: 開発時およびテスト時に必要なPythonライブラリの依存関係を記述したファイルです。
- **`requirements.txt`**: プロジェクトを本番環境で実行するために必要なPythonライブラリの依存関係を記述したファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはいけないかを指示するファイルです。
- **`ruff.toml`**: Pythonのコードリンター/フォーマッターであるRuffの設定ファイルです。コードスタイルの自動修正や品質チェックのルールを定義します。
- **`src/__init__.py`**: `src`ディレクトリがPythonパッケージであることを示すファイルです。
- **`src/generate_repo_list/__init__.py`**: `generate_repo_list`ディレクトリがPythonサブパッケージであることを示すファイルです。
- **`src/generate_repo_list/badge_generator.py`**: リポジトリのステータス（アーカイブ、フォークなど）や言語などに応じたバッジ画像を生成またはマークダウン形式で埋め込むロジックを扱います。
- **`src/generate_repo_list/config.yml`**: プロジェクト全体の動作設定を定義するYAMLファイルです。例えば、プロジェクト概要取得機能の有効/無効、対象ファイル、タイムアウト時間などが含まれます。
- **`src/generate_repo_list/config_manager.py`**: `config.yml`やその他の設定ファイルを読み込み、プログラム全体で利用できるように管理する機能を提供します。
- **`src/generate_repo_list/generate_repo_list.py`**: このプロジェクトの中核となる実行スクリプトです。GitHub APIからリポジトリ情報を取得し、その情報を基にMarkdownファイルを生成する一連の処理を制御します。
- **`src/generate_repo_list/json_ld_template.json`**: 検索エンジン最適化（SEO）のために、構造化データ（JSON-LD形式）を埋め込む際のテンプレートファイルです。
- **`src/generate_repo_list/language_info.py`**: GitHubリポジトリのプログラミング言語情報を処理し、表示に適した形式に整形する機能を提供します。
- **`src/generate_repo_list/markdown_generator.py`**: リポジトリデータと設定に基づいて、最終的なMarkdown形式のコンテンツを生成する主要なロジックを実装しています。
- **`src/generate_repo_list/project_overview_fetcher.py`**: 各GitHubリポジトリ内の特定のファイル（例: `generated-docs/project-overview.md`）から、そのリポジトリの概要説明を自動的に取得・抽出する機能を提供します。
- **`src/generate_repo_list/repository_processor.py`**: GitHub APIを通じてリポジトリ一覧を取得し、必要なデータ（名前、説明、URLなど）を抽出し、後続処理のために整形する役割を担います。
- **`src/generate_repo_list/seo_template.yml`**: SEO関連のメタデータやキーワードなどの情報を定義するためのテンプレートファイルです。
- **`src/generate_repo_list/statistics_calculator.py`**: リポジトリに関する様々な統計情報（例: スター数、フォーク数、最終更新日など）を計算し、表示用に提供する機能です。
- **`src/generate_repo_list/strings.yml`**: プロジェクト内で使用される表示メッセージ、ラベル、文言などを一元的に管理するためのYAMLファイルです。多言語対応や文言の変更が容易になります。
- **`src/generate_repo_list/template_processor.py`**: Markdown生成において、特定のプレースホルダーを持つテンプレートに変数を埋め込むなどの処理を行う汎用的な機能を提供します。
- **`src/generate_repo_list/url_utils.py`**: URLの構築、解析、検証など、URLに関連するユーティリティ関数を集めたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher.py`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストファイルを格納するためのディレクトリです。
- **`tests/test_config.py`**: 設定ファイルの読み込みや管理が正しく行われるかを検証するテストです。
- **`tests/test_environment.py`**: 実行環境のセットアップや依存関係が適切であるかをチェックするテストです。
- **`tests/test_integration.py`**: 複数のモジュールが連携して動作する際の正しい挙動を検証する統合テストです。
- **`tests/test_markdown_generator.py`**: `markdown_generator.py`が期待通りのMarkdownコンテンツを生成するかを検証するテストです。
- **`tests/test_project_overview_fetcher.py`**: `project_overview_fetcher.py`の機能、特にリポジトリからの概要抽出が正しく行われるかを検証するテストです。
- **`tests/test_repository_processor.py`**: `repository_processor.py`がGitHub APIから取得したデータを正しく処理・整形するかを検証するテストです。

## 関数詳細説明
このプロジェクトはPythonスクリプトをベースにしており、各ファイルが特定の役割を持つ関数やクラスを内包しています。以下に主要なファイルにおける中心的な関数の役割を説明します。具体的な引数や戻り値はコードが提供されていないため、一般的な機能として記述します。

- **`src/generate_repo_list/generate_repo_list.py`**
    - `main()`: プログラムのエントリーポイントとなる関数です。コマンドライン引数の解析、GitHub APIからのリポジトリ取得、データ処理、Markdown生成、ファイル出力といった一連の処理フロー全体を orchestrate します。
- **`src/generate_repo_list/badge_generator.py`**
    - `generate_badge_markdown(repo_data)`: 指定されたリポジトリデータに基づいて、そのリポジトリの特性（例: アクティブ、アーカイブ、フォークなど）を示すMarkdown形式のバッジを生成します。
- **`src/generate_repo_list/config_manager.py`**
    - `load_config(config_path)`: 指定されたパスからYAML形式の設定ファイルを読み込み、設定オブジェクトまたは辞書として返します。
    - `get_setting(key_path, default_value=None)`: 読み込まれた設定から、指定されたキーパスに対応する設定値を取得します。
- **`src/generate_repo_list/language_info.py`**
    - `get_repository_languages(repo_name, owner_name)`: 指定されたリポジトリのプログラミング言語の使用状況をGitHub APIから取得し、その統計情報（例: 言語とバイト数の割合）を返します。
- **`src/generate_repo_list/markdown_generator.py`**
    - `generate_repo_list_markdown(repositories_data, config, strings)`: 処理済みのリポジトリデータ、設定情報、および文言データに基づいて、リポジトリ一覧の全体的なMarkdownコンテンツを生成します。
    - `_generate_repo_section(repo_data)`: 個々のリポジトリに関する詳細情報（名前、説明、リンク、概要など）を含むMarkdownセクションを生成します。
- **`src/generate_repo_list/project_overview_fetcher.py`**
    - `fetch_and_parse_project_overview(repo_name, owner_name, config)`: 指定されたリポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から「プロジェクト概要」セクションを非同期で取得し、指定された行数で要約された説明を抽出します。
- **`src/generate_repo_list/repository_processor.py`**
    - `fetch_all_repositories(username, token)`: 指定されたGitHubユーザー名とトークンを使用して、そのユーザーが所有するすべての公開リポジトリの情報をGitHub APIから取得します。
    - `process_repository_data(repo_raw_data, config)`: GitHub APIから取得した生のリポジトリデータを受け取り、プロジェクト内で利用しやすい形式に加工・整形します。
- **`src/generate_repo_list/statistics_calculator.py`**
    - `calculate_repo_statistics(repo_data)`: 指定されたリポジトリデータ（スター数、フォーク数、issue数など）に基づいて、表示用の統計情報（例: 最終更新からの経過時間）を計算します。
- **`src/generate_repo_list/template_processor.py`**
    - `apply_template(template_string, context)`: テンプレート文字列内のプレースホルダーを、提供されたコンテキストデータで置換し、最終的な文字列を生成します。
- **`src/generate_repo_list/url_utils.py`**
    - `build_github_repo_url(username, repo_name)`: 指定されたユーザー名とリポジトリ名から、GitHubリポジトリのURLを構築します。
    - `build_github_pages_url(username, repo_name)`: GitHub Pagesの慣例に従い、特定のGitHub Pages URLを構築します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-26 07:06:08 JST
