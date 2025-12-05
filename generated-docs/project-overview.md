Last updated: 2025-12-06

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を自動取得してGitHub Pagesサイト用のMarkdownファイルを生成します。
- 生成されたリポジトリ一覧ページはSEO最適化され、検索エンジンによるクロールを促進します。
- LLMがリポジトリ参照に失敗する課題を緩和し、開発効率向上に貢献することを目指します。

## 技術スタック
- フロントエンド: GitHub Pages (Jekyllベースでサイトを構築), Markdown (コンテンツ記述に使用)
- 音楽・オーディオ: 利用していません。
- 開発ツール: GitHub API (リポジトリ情報取得), pytest (テストフレームワーク), ruff (Pythonコードのリンター・フォーマッター)
- テスト: pytest (Pythonコードの単体・結合テストフレームワーク)
- ビルドツール: Jekyll (GitHub Pagesサイトのビルドに利用される静的サイトジェネレーター)
- 言語機能: Python (メインの開発言語としてスクリプトを実行)
- 自動化・CI/CD: Pythonスクリプトによる自動生成 (リポジトリ一覧の自動生成プロセス), `requirements.txt` (依存関係管理による環境自動化)
- 開発標準: ruff (コードスタイルと品質の自動チェック・修正), .editorconfig (エディタ全体でのコードスタイル統一設定)

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
  test_environment.py
  test_integration.py
  test_markdown_generator.py
  test_project_overview_fetcher.py
  test_repository_processor.py
```

## ファイル詳細説明
-   `.editorconfig`: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
-   `.gitignore`: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイル。
-   `LICENSE`: 本プロジェクトのライセンス情報（MITライセンス）が記載されています。
-   `README.md`: プロジェクトの概要、機能、セットアップ方法、使い方などが記載されたドキュメント。
-   `_config.yml`: Jekyll（GitHub Pagesの基盤）サイト全体の構成設定ファイル。
-   `assets/`: GitHub Pagesサイトで使用されるファビコンなどの静的アセットを格納するディレクトリ。
    -   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: 各サイズのウェブサイトアイコン。
-   `debug_project_overview.py`: `project_overview_fetcher`機能のデバッグ目的で使用されるスクリプト。
-   `generated-docs/`: 他のリポジトリから自動取得された`project-overview.md`ファイルなどが格納される可能性のあるディレクトリ。
-   `googled947dc864c270e07.html`: Google Search Consoleでサイト所有権を確認するために配置されるファイル。
-   `index.md`: Pythonスクリプトによって生成される、リポジトリ一覧が表示されるGitHub Pagesサイトのメインページ。
-   `issue-notes/`: 開発中に発生した課題や検討事項を記録するためのMarkdownファイル群。
-   `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に、アプリのメタデータや表示設定を定義するファイル。
-   `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイル。
-   `requirements-dev.txt`: 開発およびテスト環境で必要なPythonパッケージをリストアップしたファイル。
-   `requirements.txt`: 本番環境で必要なPythonパッケージをリストアップしたファイル。
-   `robots.txt`: 検索エンジンのクローラーに対して、どのページをクロールしてよいか、またはしてはならないかを指示するファイル。
-   `ruff.toml`: Pythonの高速リンターおよびフォーマッターである`ruff`の設定ファイル。
-   `src/`: プロジェクトの主要なソースコードが格納されているディレクトリ。
    -   `src/__init__.py`: `src`ディレクトリがPythonパッケージであることを示すファイル。
    -   `src/generate_repo_list/`: リポジトリ一覧を生成するコアロジックを格納するパッケージ。
        -   `src/generate_repo_list/__init__.py`: `generate_repo_list`ディレクトリがPythonパッケージであることを示すファイル。
        -   `src/generate_repo_list/badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ画像を生成するためのロジックを定義します。
        -   `src/generate_repo_list/config.yml`: プロジェクト概要取得機能などの技術的パラメータや設定を定義するYAMLファイル。
        -   `src/generate_repo_list/config_manager.py`: `config.yml`などの設定ファイルを読み込み、管理するためのクラスや関数を提供します。
        -   `src/generate_repo_list/generate_repo_list.py`: プロジェクトのエントリスクリプトであり、GitHub APIからリポジトリ情報を取得し、Markdownファイルを生成するメインの処理を実行します。
        -   `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化（SEO）のための構造化データ（JSON-LD）のテンプレート。
        -   `src/generate_repo_list/language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、整形するためのロジック。
        -   `src/generate_repo_list/markdown_generator.py`: 取得したリポジトリ情報に基づいて、最終的なMarkdownコンテンツを生成するためのクラスや関数を提供します。
        -   `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの`generated-docs/project-overview.md`ファイルからプロジェクト概要を自動的に取得するロジックを実装しています。
        -   `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを解析し、必要な情報を抽出・整形するためのロジック。
        -   `src/generate_repo_list/seo_template.yml`: SEO関連のメタデータやテンプレート設定を定義するYAMLファイル。
        -   `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数やフォーク数などの統計情報を計算・集計するためのロジック。
        -   `src/generate_repo_list/strings.yml`: UIに表示されるテキストメッセージ、ラベル、その他の静的文字列を一元的に管理するためのYAMLファイル。
        -   `src/generate_repo_list/template_processor.py`: Markdown生成時に使用されるテンプレート（例: Jinja2など）を処理するための共通ロジックを提供します。
        -   `src/generate_repo_list/url_utils.py`: URLの構築、解析、検証など、URL関連のユーティリティ関数を提供します。
-   `test_project_overview.py`: `project_overview_fetcher`機能のテストケースを記述したスクリプト。
-   `tests/`: プロジェクト全体のテストコードが格納されているディレクトリ。
    -   `test_config.py`: 設定ファイルの読み込みや管理に関するテストケース。
    -   `test_environment.py`: プロジェクトの実行環境や依存関係に関するテストケース。
    -   `test_integration.py`: プロジェクトの複数のコンポーネントが連携して正しく動作するかを確認する統合テスト。
    -   `test_markdown_generator.py`: Markdown生成ロジックの正確性を検証するテストケース。
    -   `test_project_overview_fetcher.py`: `project_overview_fetcher`の機能に関するテストケース。
    -   `test_repository_processor.py`: リポジトリ情報処理ロジックの正確性を検証するテストケース。

## 関数詳細説明
提供された情報からは具体的な関数を特定できませんでした。一般的なスクリプト実行とファイル操作が中心となるため、各ファイルの説明に記載された役割に沿った内部関数が存在すると推測されます。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2025-12-06 07:05:54 JST
