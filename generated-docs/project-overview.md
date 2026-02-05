Last updated: 2026-02-06

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、リポジトリ情報を取得・加工するシステムです。
- GitHub Pages向けに、SEO最適化されたリポジトリ一覧Markdownを自動生成します。
- 検索エンジンやLLMからのリポジトリ参照性を向上させ、開発効率を高めます。

## 技術スタック
使用している技術をカテゴリ別に整理して説明します。
- フロントエンド: 
    - **Jekyll**: GitHub Pagesの基盤となる静的サイトジェネレータ。本プロジェクトで生成されるMarkdownファイルはJekyllによって最終的なウェブページに変換されます。
    - **Markdown**: リポジトリ一覧のコンテンツを記述する軽量マークアップ言語。SEOに最適化されたMarkdownファイルが自動生成されます。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール: 
    - **GitHub API**: GitHubリポジトリ情報をプログラムで取得するために利用されるRESTful API。
- テスト: 
    - **pytest**: Python製のテストフレームワーク。プロジェクトの機能が正しく動作するかを検証するために使用されます。
- ビルドツール: 
    - **Pythonスクリプト**: 明示的なビルドツールではありませんが、Pythonスクリプト自身がMarkdownコンテンツを生成する役割を担います。最終的なGitHub PagesのビルドとデプロイはJekyllに依存します。
- 言語機能: 
    - **Python**: プロジェクトのメイン開発言語。リポジトリ情報の取得、処理、Markdown生成スクリプトがPythonで記述されています。
- 自動化・CI/CD: 本プロジェクト自体が直接自動化・CI/CDツールとして動作するわけではありません。GitHub Pagesのデプロイフローで利用される可能性があります。
- 開発標準: 
    - **ruff**: Pythonコードのリンティングおよびフォーマットツール。コードの品質と一貫したスタイルを維持するために使用されます。

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
  📖 18.md
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
各ファイルの役割と機能を詳細に説明します。

*   `.editorconfig`: 異なるエディタやIDE間で、インデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
*   `.gitignore`: Gitのバージョン管理から除外するファイルやディレクトリを指定するファイルです。
*   `LICENSE`: 本プロジェクトのライセンス情報（MITライセンス）が記述されています。
*   `README.md`: プロジェクトの概要、目的、主な機能、クイックスタートガイド、設定方法などが記述されたメインドキュメントです。
*   `_config.yml`: Jekyllサイト全体の設定ファイルです。GitHub Pagesの振る舞いを制御します。
*   `assets/`: サイトで使用される画像やファビコンなどの静的アセットが格納されるディレクトリです。
    *   `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: サイトのファビコン（ブラウザタブなどに表示されるアイコン）の異なるサイズを提供します。
*   `debug_project_overview.py`: プロジェクト概要の自動取得機能に関するデバッグやテストを行うためのスクリプトと推測されます。
*   `generated-docs/`: 生成されたドキュメントや関連ファイルが格納されるディレクトリです。特に各リポジトリの概要が記述された`project-overview.md`がここに配置されることが想定されています。
*   `googled947dc864c270e07.html`: Google Search Consoleでサイト所有権を証明するために使用される認証ファイルです。
*   `index.md`: `generate_repo_list.py`スクリプトによってリポジトリ一覧が自動生成され、出力されるGitHub Pagesのメイン（トップページ）となるMarkdownファイルです。
*   `issue-notes/`: プロジェクトの課題、検討事項、メモなどがMarkdown形式で個別に管理されているディレクトリです。
*   `manifest.json`: Web App Manifestファイル。プログレッシブウェブアプリ（PWA）として、ホーム画面への追加やアプリ風の表示設定を提供します。
*   `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイルです。テストの実行オプションや挙動を定義します。
*   `requirements-dev.txt`: 開発環境で必要となるPythonライブラリの依存関係が記述されたファイルです。
*   `requirements.txt`: 本番環境で必要となるPythonライブラリの依存関係が記述されたファイルです。
*   `robots.txt`: 検索エンジンのクローラーに対して、サイト内でクロールしてよいページとそうでないページを指示するためのファイルです。
*   `ruff.toml`: Pythonコードのリンターおよびフォーマッターである`ruff`の設定ファイルです。コードスタイルのルールや自動修正の挙動を定義します。
*   `src/`: プロジェクトのソースコードが格納されているディレクトリです。
    *   `__init__.py`: Pythonパッケージであることを示す空ファイルです。
    *   `generate_repo_list/`: リポジトリ一覧を生成するための主要なPythonモジュール群が格納されています。
        *   `__init__.py`: Pythonパッケージであることを示す空ファイルです。
        *   `badge_generator.py`: リポジトリの特性（例：言語、ステータス）を示すバッジ画像を生成または取得するためのロジックを扱います。
        *   `config.yml`: プロジェクト概要取得機能やAPI関連の設定パラメータなど、システムの動作に必要な技術的な設定を定義するファイルです。
        *   `config_manager.py`: `config.yml`などの設定ファイルを読み込み、アプリケーション全体で利用可能な形で管理するモジュールです。
        *   `date_formatter.py`: 日付や時刻の情報を指定された形式に変換し、表示するためのユーティリティ関数を提供します。
        *   `generate_repo_list.py`: プロジェクトのメインスクリプトであり、GitHub APIからリポジトリ情報を取得し、他のモジュールと連携して最終的なMarkdownファイルを生成します。
        *   `json_ld_template.json`: 構造化データ（JSON-LD形式）のテンプレートファイルです。SEOを目的としたリッチスニペットの生成に利用されると推測されます。
        *   `language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理したり、統計情報を計算したりする機能を提供します。
        *   `markdown_generator.py`: 取得したリポジトリ情報や設定に基づいて、整形されたMarkdownコンテンツを生成するロジックを担います。
        *   `project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を抽出・解析するモジュールです。
        *   `readme_badge_extractor.py`: リポジトリのREADMEファイルから特定のパターン（例：ステータスバッジ）を抽出し、解析する機能を持つモジュールです。
        *   `repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報を抽出、整形、フィルタリングするなどの処理を行います。
        *   `seo_template.yml`: SEO（検索エンジン最適化）に関連するメタデータやテンプレート設定を定義するファイルです。
        *   `statistics_calculator.py`: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算する機能を提供します。
        *   `strings.yml`: UIに表示されるメッセージや文言、ラベルなどを一元的に管理するための設定ファイルです。
        *   `template_processor.py`: Jekyllテンプレートやその他のテンプレートファイルに動的なデータを埋め込み、最終的な出力を生成するための処理を行います。
        *   `url_utils.py`: URLの構築、検証、解析、エンコーディングなど、URLに関連する様々なユーティリティ関数を提供します。
*   `test_project_overview.py`: `project_overview_fetcher.py`モジュールの機能に関する単体テストを記述したファイルです。
*   `tests/`: プロジェクトのテストコードが格納されているディレクトリです。
    *   `test_badge_generator_integration.py`: バッジ生成機能に関する統合テストを記述したファイルです。
    *   `test_config.py`: 設定ファイルの読み込みや管理機能に関するテストを記述したファイルです。
    *   `test_date_formatter.py`: 日付フォーマットユーティリティに関するテストを記述したファイルです。
    *   `test_environment.py`: 実行環境の設定や依存関係に関するテストを記述したファイルです。
    *   `test_integration.py`: システム全体の主要なフローに関する統合テストを記述したファイルです。
    *   `test_markdown_generator.py`: Markdown生成機能に関するテストを記述したファイルです。
    *   `test_project_overview_fetcher.py`: プロジェクト概要取得機能に関するテストを記述したファイルです。
    *   `test_readme_badge_extractor.py`: READMEからのバッジ抽出機能に関するテストを記述したファイルです。
    *   `test_repository_processor.py`: リポジトリ情報処理機能に関するテストを記述したファイルです。

## 関数詳細説明
プロジェクト情報から具体的な関数名は検出されませんでしたが、各モジュールの役割に基づき、想定される機能について説明します。

*   `badge_generator.py` 内の関数: リポジトリのステータスや情報を視覚的に表現するバッジの生成、URLの構築などを行う機能群。
*   `config_manager.py` 内の関数: `config.yml` や `strings.yml` などの設定ファイルを読み込み、設定値にアクセスするための機能群。
*   `date_formatter.py` 内の関数: 日付や時刻の情報を指定された形式に変換し、人間が読みやすい形式で提供するユーティリティ機能群。
*   `generate_repo_list.py` 内の関数: GitHub APIからリポジトリ情報を取得し、取得したデータを処理して最終的なMarkdownコンテンツを生成するメイン処理機能。コマンドライン引数の解析も含まれると推測されます。
*   `language_info.py` 内の関数: リポジトリで使用されているプログラミング言語の統計や表示、色付けに関する情報を処理する機能群。
*   `markdown_generator.py` 内の関数: 構造化されたデータ（リポジトリ情報など）を受け取り、指定されたフォーマットでMarkdown形式の文字列を生成する機能群。
*   `project_overview_fetcher.py` 内の関数: 指定されたパス（例: `generated-docs/project-overview.md`）のMarkdownファイルから特定のセクション（「プロジェクト概要」）を抽出し、解析する機能群。
*   `readme_badge_extractor.py` 内の関数: READMEファイルの内容を解析し、含まれるバッジ（例: ビルドステータス、ライセンス）の情報を抽出する機能群。
*   `repository_processor.py` 内の関数: GitHub APIから取得した生のリポジトリデータを受け取り、必要な情報の抽出、整形、アクティブ・アーカイブ・フォークなどの分類、ソートを行う機能群。
*   `statistics_calculator.py` 内の関数: リポジトリのスター数、フォーク数、コミット数などの統計情報を計算し、集計する機能群。
*   `template_processor.py` 内の関数: JSON-LDテンプレートやSEOテンプレートのような静的ファイルを読み込み、動的なデータ（リポジトリ情報など）で埋め込んで最終的なコンテンツを生成する機能群。
*   `url_utils.py` 内の関数: URLの構築、検証、パスの結合など、URLに関連する一般的なユーティリティ機能群。

## 関数呼び出し階層ツリー
```
プロジェクト情報から関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-02-06 07:09:25 JST
