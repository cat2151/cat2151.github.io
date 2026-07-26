Last updated: 2026-07-27

# Project Overview

## プロジェクト概要
- GitHub Pages向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIを利用し、リポジトリ情報からSEO最適化されたMarkdownファイルを生成します。
- 検索エンジンやLLMからの参照性を高め、リポジトリの可視性を向上させます。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの基盤となる静的サイトジェネレーターで、生成されたMarkdownファイルがJekyllによって処理されます。
    - **Markdown**: GitHub APIから取得した情報をもとに生成される出力形式であり、Jekyllサイトのコンテンツとなります。
- 音楽・オーディオ: 該当する技術はありません。
- 開発ツール:
    - **Python**: プロジェクトの主要な開発言語であり、リポジトリ情報の取得、処理、Markdown生成スクリプトに使用されています。
- テスト:
    - **Pytest**: Python製のテストフレームワークで、プロジェクトの機能テストや単体テストに利用されています。
- ビルドツール:
    - **Pythonスクリプト**: GitHub APIからデータを取得し、GitHub Pages向けのMarkdownファイルを生成する主要な処理を実行します。
- 言語機能:
    - **Pythonの標準機能**: 言語固有の高度な機能よりも、Pythonの標準的なデータ構造やファイル操作、ネットワーク通信（HTTPリクエスト）機能が活用されています。
- 自動化・CI/CD:
    - 本プロジェクト自体がGitHub Pages向けのコンテンツ生成を自動化するスクリプトとして機能します。明確なCI/CDツールは使用されていません。
- 開発標準:
    - **Ruff**: Pythonコードのフォーマットとリンティングを自動化し、コード品質と統一性を保つために使用されています。

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
- **`.editorconfig`**: 異なるエディタやIDEを使用する開発者間で、コードの書式設定（インデントスタイル、文字コードなど）を統一するための設定ファイルです。
- **`.gitignore`**: Gitがバージョン管理の対象外とするファイルやディレクトリを指定します。一時ファイルや自動生成ファイルなどをリポジトリに含めないために使用されます。
- **`LICENSE`**: プロジェクトのライセンス情報（このプロジェクトではMITライセンス）を記述したファイルです。プロジェクトの利用条件を明示します。
- **`README.md`**: プロジェクトの概要、目的、主な機能、クイックスタートガイド、開発者向けヒントなどが記述されたメインのドキュメントです。
- **`_config.yml`**: Jekyllサイト全体の構成設定ファイルです。GitHub Pagesサイトのタイトル、テーマ、プラグインなどの設定を定義します。
- **`assets/`**: faviconなどの静的アセットを格納するディレクトリです。ウェブサイトの表示に必要な画像ファイルなどが含まれます。
    - `favicon-16x16.png`, `favicon-192x192.png`, `favicon-32x32.png`, `favicon-512x512.png`: ウェブサイトのファビコン（ブラウザのタブなどに表示されるアイコン）の各種サイズです。
- **`debug_project_overview.py`**: `project_overview_fetcher`機能の動作確認やデバッグを目的としたPythonスクリプトです。
- **`generated-docs/`**: `project-overview.md`など、自動生成されたドキュメントやデータが配置されるディレクトリです。
- **`googled947dc864c270e07.html`**: Google Search Consoleのサイト所有権確認のために配置されるHTMLファイルです。
- **`index.md`**: GitHub Pagesサイトのトップページとして機能するMarkdownファイルです。このプロジェクトでは、生成されたリポジトリ一覧がここに出力されます。
- **`issue-notes/22.md`**: 特定のイシューに関するメモや詳細を記録したMarkdownファイルです。
- **`manifest.json`**: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用されるウェブマニフェストファイルです。アプリ名、アイコン、表示設定などを定義します。
- **`pytest.ini`**: PythonのテストフレームワークであるPytestの設定ファイルです。テストの発見ルール、オプション、プラグインなどを指定します。
- **`requirements-dev.txt`**: 開発環境やテスト環境でのみ必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **`requirements.txt`**: 本番環境でこのプロジェクトを実行するために必要となるPythonパッケージの依存関係をリストアップしたファイルです。
- **`robots.txt`**: 検索エンジンのクローラーに対して、ウェブサイトのどの部分をクロールしてもよいか、あるいはクロールしてはいけないかを指示するファイルです。
- **`ruff.toml`**: PythonのLinterおよびFormatterであるRuffの設定ファイルです。コードスタイル、整形ルール、静的解析のオプションを定義します。
- **`src/__init__.py`**: Pythonパッケージを示すための空のファイルです。`src`ディレクトリをPythonモジュールのルートとして認識させます。
- **`src/generate_repo_list/`**: リポジトリ一覧生成システムの主要なロジックを含むPythonパッケージです。
    - `src/generate_repo_list/__init__.py`: `generate_repo_list`ディレクトリをPythonパッケージとして認識させるためのファイルです。
    - `src/generate_repo_list/badge_generator.py`: リポジトリのステータスや技術スタックを示すバッジ（アイコン）を生成または管理するロジックを実装しています。
    - `src/generate_repo_list/config.yml`: プロジェクト概要取得機能の有効/無効、対象ファイルパス、リトライ設定など、スクリプトの動作に関する設定値を定義するYAMLファイルです。
    - `src/generate_repo_list/config_manager.py`: `config.yml`や`secrets.toml`などの設定ファイルを読み込み、管理するためのPythonモジュールです。
    - `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を特定のフォーマットに変換するユーティリティ関数を提供します。
    - `src/generate_repo_list/generate_repo_list.py`: このプロジェクトのメインスクリプトです。GitHub APIからリポジトリ情報を取得し、整形してMarkdownファイルを生成する一連の処理を制御します。
    - `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化（SEO）のために使用されるJSON-LD形式の構造化データテンプレートです。
    - `src/generate_repo_list/language_info.py`: リポジトリで使用されているプログラミング言語に関する情報を処理し、表示に役立つデータに変換する機能を提供します。
    - `src/generate_repo_list/markdown_generator.py`: 処理されたリポジトリ情報を受け取り、最終的なMarkdown形式のコンテンツを生成するロジックを実装しています。
    - `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリの特定のファイル（例: `generated-docs/project-overview.md`）からプロジェクト概要の3行説明を自動的に抽出する役割を担います。
    - `src/generate_repo_list/readme_badge_extractor.py`: リポジトリの`README.md`ファイルから、プロジェクトの状態や使用技術を示すバッジ情報を抽出する機能を提供します。
    - `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な形式に加工・整形するコアロジックを実装しています。
    - `src/generate_repo_list/seo_template.yml`: SEO関連のメタデータや、生成されるMarkdownファイルに埋め込むためのテンプレート設定を定義するYAMLファイルです。
    - `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数、フォーク数などの統計情報を計算する機能を提供します。
    - `src/generate_repo_list/strings.yml`: ユーザーインターフェースに表示されるメッセージ、ラベル、その他のテキストを多言語対応や管理しやすくするために一元管理するYAMLファイルです。
    - `src/generate_repo_list/template_processor.py`: Markdownなどのテンプレートファイルに変数を埋め込むなどの処理を行う汎用的なテンプレート処理モジュールです。
    - `src/generate_repo_list/url_utils.py`: URLの検証、構築、パースなど、URLに関連する様々なユーティリティ関数をまとめたモジュールです。
- **`test_project_overview.py`**: `project_overview_fetcher`モジュールの機能が正しく動作するかを検証するためのテストスクリプトです。
- **`tests/`**: プロジェクト全体のテストファイルを格納するディレクトリです。
    - `tests/conftest.py`: Pytestのテストフィクスチャやヘルパー関数を定義するためのファイルです。
    - `tests/test_badge_generator_integration.py`: `badge_generator`モジュールの統合テストを行います。
    - `tests/test_check_large_files.py`: `.github_automation/check_large_files`スクリプトのテストです。
    - `tests/test_config.py`: 設定ファイル（`config.yml`など）の読み込みや管理が正しく行われるかをテストします。
    - `tests/test_date_formatter.py`: `date_formatter`モジュールの日付フォーマット機能のテストです。
    - `tests/test_environment.py`: プロジェクトの実行環境に関するテストです。
    - `tests/test_integration.py`: プロジェクトの主要モジュール間の連携が正しく行われるかを検証する統合テストです。
    - `tests/test_markdown_generator.py`: `markdown_generator`モジュールが正しいMarkdownを生成するかをテストします。
    - `tests/test_project_overview_fetcher.py`: `project_overview_fetcher`モジュールのテストです。
    - `tests/test_readme_badge_extractor.py`: `readme_badge_extractor`モジュールのテストです。
    - `tests/test_repository_processor.py`: `repository_processor`モジュールがリポジトリデータを正しく処理するかをテストします。

## 関数詳細説明
提供された情報からは具体的な関数の詳細（役割、引数、戻り値など）を特定できませんでした。コードの分析によってこれらの情報が得られる可能性があります。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした
```

---
Generated at: 2026-07-27 07:21:54 JST
