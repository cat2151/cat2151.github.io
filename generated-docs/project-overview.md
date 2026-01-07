Last updated: 2026-01-08

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、指定ユーザーのリポジトリ情報を自動で取得・処理するシステムです。
- 取得した情報から、JekyllベースのGitHub Pages向けにSEO最適化されたリポジトリ一覧のMarkdownファイルを生成します。
- これにより、GitHub Pagesサイトの検索エンジン可視性を高め、リポジトリ情報を効果的に公開することを目的としています。

## 技術スタック
- フロントエンド:
  - **Jekyll**: GitHub Pagesで利用される静的サイトジェネレーター。本プロジェクトはJekyllサイト用のMarkdownファイルを生成します。
  - **Markdown**: 生成されるリポジトリ一覧のコンテンツ形式。
- 音楽・オーディオ: 該当なし
- 開発ツール:
  - **Python**: リポジトリ情報の取得、処理、Markdown生成の中核を担うスクリプト言語です。
  - **GitHub API**: GitHub上のリポジトリ情報をプログラムから取得するために使用されます。
- テスト:
  - **pytest**: Python製のテストフレームワークで、プロジェクトの各機能が正しく動作することを確認するために使用されます。
- ビルドツール: 該当なし (Jekyllが静的サイト生成の役割を担いますが、直接的なビルドツールとしては記載しません)
- 言語機能:
  - **Pythonの標準ライブラリ**: ファイル操作、データ構造、ネットワーク通信など、Pythonの基本的な機能が利用されています。
- 自動化・CI/CD: 該当なし (現状ではローカル開発重視の構成とされており、CI/CDは導入されていません)
- 開発標準:
  - **ruff**: Pythonコードのスタイルチェックとフォーマットを自動化し、コード品質と一貫性を保つために使用されるツールです。

## ファイル階層ツリー
```
.editorconfig
.gitignore
LICENSE
README.md
_config.yml
assets/
  favicon-16x16.png
  favicon-192x192.png
  favicon-32x32.png
  favicon-512x512.png
debug_project_overview.py
generated-docs/
googled947dc864c270e07.html
index.md
issue-notes/
  10.md
  12.md
  14.md
  16.md
  2.md
  4.md
  6.md
  8.md
manifest.json
pytest.ini
requirements-dev.txt
requirements.txt
robots.txt
ruff.toml
src/
  __init__.py
  generate_repo_list/
    __init__.py
    badge_generator.py
    config.yml
    config_manager.py
    date_formatter.py
    generate_repo_list.py
    json_ld_template.json
    language_info.py
    markdown_generator.py
    project_overview_fetcher.py
    repository_processor.py
    seo_template.yml
    statistics_calculator.py
    strings.yml
    template_processor.py
    url_utils.py
test_project_overview.py
tests/
  test_config.py
  test_date_formatter.py
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明

- `README.md`: プロジェクトの目的、機能、使用方法、設定、ライセンスなど、プロジェクト全体の概要とガイドラインを記述したメインドキュメントです。
- `LICENSE`: 本プロジェクトのライセンス情報（MITライセンス）を記載しています。
- `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイルです。
- `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定します。
- `_config.yml`: Jekyllサイト全体の設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を管理します。
- `assets/`: サイトで使用されるファビコン画像（`favicon-*.png`）など、静的なアセットを格納するディレクトリです。
- `debug_project_overview.py`: プロジェクト概要取得機能 (`project_overview_fetcher.py`) のデバッグを目的とした補助スクリプトです。
- `generated-docs/`: 他のリポジトリから取得される `project-overview.md` ファイルが配置されることが想定される仮想パスです。
- `googled947dc864c270e07.html`: Google Search Consoleによるサイト所有権の確認に使用される認証ファイルです。
- `index.md`: スクリプトによって生成されるリポジトリ一覧が出力される、GitHub PagesサイトのメインページとなるMarkdownファイルです。
- `issue-notes/`: 開発中に発生した課題や検討事項、メモなどをMarkdown形式で記録するディレクトリです。
- `manifest.json`: プログレッシブウェブアプリ (PWA) の設定ファイルで、ホーム画面への追加、オフライン機能などを定義します。
- `pytest.ini`: Pythonのテストフレームワーク `pytest` の設定ファイルで、テストの実行方法やオプションを定義します。
- `requirements.txt`: プロジェクトの実行に必要なPythonパッケージとそのバージョンを記載したファイルです。
- `requirements-dev.txt`: 開発環境およびテスト環境でのみ必要なPythonパッケージとそのバージョンを記載したファイルです。
- `robots.txt`: 検索エンジンクローラーに対して、サイトのどの部分をクロール・インデックスするか指示するためのファイルです。
- `ruff.toml`: Pythonコードのリンティングとフォーマットツール `ruff` の設定ファイルで、コードスタイルのルールを定義します。
- `src/__init__.py`: `src` ディレクトリをPythonパッケージとして認識させるためのファイルです。
- `src/generate_repo_list/`: リポジトリ一覧生成ロジックをカプセル化したPythonパッケージです。
  - `src/generate_repo_list/__init__.py`: `generate_repo_list` ディレクトリをPythonサブパッケージとして認識させるためのファイルです。
  - `src/generate_repo_list/badge_generator.py`: リポジトリの各種情報（言語、ステータスなど）に応じたバッジ画像を生成するロジックを扱います。
  - `src/generate_repo_list/config.yml`: プロジェクト概要取得機能など、本システム固有の技術的パラメータを設定するためのファイルです。
  - `src/generate_repo_list/config_manager.py`: 設定ファイル (`config.yml`, `secrets.toml`など) の読み込みと管理を行うモジュールです。
  - `src/generate_repo_list/date_formatter.py`: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
  - `src/generate_repo_list/generate_repo_list.py`: プロジェクトのエントリポイントとなるメインスクリプトで、GitHub APIからリポジトリ情報を取得し、最終的なMarkdownファイルを生成します。
  - `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化 (SEO) のため、構造化データ（JSON-LD形式）のテンプレートを定義します。
  - `src/generate_repo_list/language_info.py`: GitHubリポジトリの主要言語情報などを処理し、表示に役立つ形式に変換するロジックを提供します。
  - `src/generate_repo_list/markdown_generator.py`: 処理されたリポジトリ情報に基づいて、GitHub Pages向けのMarkdownコンテンツを生成するロジックを担当します。
  - `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの `generated-docs/project-overview.md` ファイルからプロジェクト概要の3行説明を抽出・取得するモジュールです。
  - `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを、Markdown生成に適した形式に加工・整形するロジックを扱います。
  - `src/generate_repo_list/seo_template.yml`: SEO関連のメタデータやコンテンツ構造に関するテンプレート設定を定義します。
  - `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算するロジックを扱います。
  - `src/generate_repo_list/strings.yml`: UI表示メッセージや様々な文言を一元管理するための設定ファイルです。多言語対応や文言変更を容易にします。
  - `src/generate_repo_list/template_processor.py`: Markdown生成プロセスにおけるテキストテンプレートの処理を担当し、動的なコンテンツ挿入を可能にします。
  - `src/generate_repo_list/url_utils.py`: URLのパース、構築、検証など、URLに関連するユーティリティ関数を提供します。
- `test_project_overview.py`: `project_overview_fetcher.py` モジュールの機能に関するテストスクリプトです。
- `tests/`: プロジェクトの各モジュールや機能に対するユニットテスト、統合テストを格納するディレクトリです。
  - `test_config.py`: `config_manager.py` など、設定関連モジュールのテストを行います。
  - `test_date_formatter.py`: `date_formatter.py` の日付整形機能が正しく動作するかをテストします。
  - `test_environment.py`: 実行環境のセットアップや依存関係に関するテストを行います。
  - `test_integration.py`: 複数のモジュールを連携させた場合の統合的な動作をテストします。
  - `test_markdown_generator.py`: `markdown_generator.py` が正しいMarkdownを生成するかをテストします。
  - `test_project_overview_fetcher.py`: `project_overview_fetcher.py` がリポジトリ概要を正しく取得できるかをテストします。
  - `test_repository_processor.py`: `repository_processor.py` がリポジトリデータを正しく処理・整形するかをテストします。

## 関数詳細説明

本プロジェクトのソースコードから具体的な関数シグネチャは提供されていませんが、各ファイルの役割から主要な関数とその機能を推測し、以下に説明します。

- **`generate_repo_list.py` (メインスクリプト)**
  - `main(username: str, output_filepath: str, limit: Optional[int] = None) -> None`:
    - **役割**: プロジェクト全体の実行エントリポイント。GitHub APIからリポジトリ情報を取得し、処理・整形後、指定されたファイルパスにMarkdown形式のリポジトリ一覧を生成します。
    - **引数**:
      - `username` (str): GitHubユーザー名。
      - `output_filepath` (str): 生成されたMarkdownを出力するファイルのパス。
      - `limit` (Optional[int]): 処理するリポジトリ数の上限（デバッグ用）。
    - **戻り値**: なし。

- **`repository_processor.py`**
  - `fetch_repositories(username: str, github_token: str, limit: Optional[int] = None) -> List[Dict]`:
    - **役割**: GitHub APIを介して、指定されたユーザーのリポジトリ情報を取得します。
    - **引数**:
      - `username` (str): GitHubユーザー名。
      - `github_token` (str): GitHub API認証用のトークン。
      - `limit` (Optional[int]): 取得するリポジトリ数の上限。
    - **戻り値**: 取得したリポジトリ情報のリスト（辞書形式）。
  - `process_repository_data(repo_data: Dict, project_overview: Optional[str] = None) -> Dict`:
    - **役割**: 個々の生のリポジトリデータを整形し、表示に必要な情報（最終更新日、言語、スター数など）を抽出・加工します。必要に応じてプロジェクト概要を追加します。
    - **引数**:
      - `repo_data` (Dict): GitHub APIから取得した単一のリポジトリの生データ。
      - `project_overview` (Optional[str]): 取得済みのプロジェクト概要文字列。
    - **戻り値**: 整形されたリポジトリ情報（辞書形式）。

- **`markdown_generator.py`**
  - `generate_markdown_output(processed_repos: List[Dict], strings_config: Dict) -> str`:
    - **役割**: 整形済みのリポジトリ情報リストを受け取り、Jekyllの要件を満たすGitHub Pages向けMarkdown文字列を生成します。
    - **引数**:
      - `processed_repos` (List[Dict]): `repository_processor`によって処理されたリポジトリ情報のリスト。
      - `strings_config` (Dict): 表示メッセージや文言を管理する設定辞書。
    - **戻り値**: 生成されたMarkdownコンテンツの文字列。

- **`project_overview_fetcher.py`**
  - `fetch_project_overview(repo_full_name: str, config: Dict, github_token: str) -> Optional[str]`:
    - **役割**: 指定されたリポジトリ（例: `owner/repo-name`）の特定のパスにある `project-overview.md` ファイルから、プロジェクト概要の3行説明を抽出して取得します。
    - **引数**:
      - `repo_full_name` (str): リポジトリのフルネーム（例: `cat2151/my-repo`）。
      - `config` (Dict): `config.yml` からロードされた設定情報。
      - `github_token` (str): GitHub API認証用のトークン。
    - **戻り値**: 抽出されたプロジェクト概要の文字列、または取得できなかった場合は `None`。

- **`config_manager.py`**
  - `load_config(config_filepath: str) -> Dict`:
    - **役割**: 指定されたYAML設定ファイル（例: `config.yml`）を読み込み、Pythonの辞書形式で返します。
    - **引数**:
      - `config_filepath` (str): 設定ファイルのパス。
    - **戻り値**: 設定内容を格納した辞書。
  - `get_github_token() -> str`:
    - **役割**: `secrets/secrets.toml` などからGitHub APIトークンを安全に取得します。
    - **引数**: なし。
    - **戻り値**: GitHub APIトークンの文字列。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析するための具体的な情報が提供されていないため、ツリーの生成はできません。

---
Generated at: 2026-01-08 07:06:35 JST
