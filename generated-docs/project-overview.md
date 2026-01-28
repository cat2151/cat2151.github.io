Last updated: 2026-01-29

# Project Overview

## プロジェクト概要
- GitHub APIを利用し、ユーザーのリポジトリ情報を自動で取得・整理するシステムです。
- 取得した情報から、JekyllベースのGitHub Pagesサイト向けにSEO最適化されたリポジトリ一覧を自動生成します。
- これにより、プロジェクトの公開情報が検索エンジンにクロールされやすくなり、LLMなどからの参照性も向上します。

## 技術スタック
- フロントエンド:
    - **Jekyll**: GitHub Pagesの静的サイトジェネレータとして機能し、生成されたMarkdownファイルを美しいWebサイトとして表示します。
    - **Markdown**: リポジトリ一覧の出力形式として使用され、JekyllによってHTMLに変換されます。
- 音楽・オーディオ: 該当する技術は使用されていません。
- 開発ツール:
    - **Python**: プロジェクトの主要なスクリプト言語として、GitHub APIからの情報取得、データの処理、Markdownファイルの生成を担います。
    - **Git**: ソースコードのバージョン管理システムとして使用されます。
    - **Ruff**: Pythonコードのリンティングとフォーマットを自動化し、コード品質と一貫性を保ちます。
    - **pytest**: Pythonアプリケーションのテストフレームワークとして、コードの品質と信頼性を保証するための単体テストおよび統合テストに使用されます。
- テスト:
    - **pytest**: Pythonコードの自動テストを実行するためのフレームワークです。
- ビルドツール:
    - **Pythonスクリプト**: リポジトリ情報を元にMarkdownファイルを「ビルド」する主要なツールです。
    - **Jekyll**: Markdownファイルを静的Webサイトとして「ビルド」するのに貢献します。
- 言語機能:
    - **Python**: メインの開発言語です。
    - **YAML**: 設定ファイル (`config.yml`, `strings.yml`, `seo_template.yml`) の記述に使用され、設定の管理を容易にします。
    - **TOML**: シークレット情報 (`secrets.toml`) の管理に使用されます。
    - **Markdown**: 生成される出力ファイル形式であり、Jekyllサイトのコンテンツ記述にも使用されます。
- 自動化・CI/CD:
    - **GitHub API**: リポジトリ情報の自動取得を可能にする中核技術です。
    - **Pythonスクリプト**: リポジトリ一覧の生成プロセス全体を自動化します。
- 開発標準:
    - **Ruff**: コードのスタイルガイドを強制し、コードの一貫性と可読性を向上させます。

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

*   **.editorconfig**: プロジェクト全体のコーディングスタイル（インデント、改行コードなど）を定義し、複数のエディタやIDE間で一貫性を保ちます。
*   **.gitignore**: Gitのバージョン管理から除外するファイルやディレクトリ（例: 自動生成ファイル、依存関係のキャッシュ）を指定します。
*   **LICENSE**: このプロジェクトがMITライセンスの下で公開されていることを示し、利用条件を定めます。
*   **README.md**: プロジェクトの概要、機能、セットアップ方法、使い方、開発者向け情報などを記述したメインドキュメントです。
*   **_config.yml**: Jekyllサイトのグローバル設定ファイルで、サイトのタイトル、テーマ、プラグインなどの情報を設定します。
*   **assets/**: Webサイトで使用される画像、CSS、JavaScriptなどの静的ファイルを格納するディレクトリです。
    *   **favicon-*.png**: Webサイトのブラウザタブやブックマークに表示されるアイコンファイルです。
*   **debug_project_overview.py**: `project_overview_fetcher.py` モジュールなどの「プロジェクト概要」取得機能のデバッグやテストを目的とした補助スクリプトです。
*   **generated-docs/**: GitHubリポジトリ内に存在し、各リポジトリのプロジェクト概要 (`project-overview.md`) が格納されることが期待されるディレクトリです。メインシステムはこのディレクトリから概要を読み取ります。
*   **googled947dc864c270e07.html**: Google Search Consoleでサイトの所有権を確認するために使用される、Google提供の検証ファイルです。
*   **index.md**: `generate_repo_list.py` スクリプトによって自動生成される、リポジトリ一覧のメイン出力ファイルです。GitHub Pagesのトップページとして表示されます。
*   **issue-notes/**: プロジェクト開発中に発生した課題や検討事項をメモとして記録するためのMarkdownファイル群を格納するディレクトリです。
*   **manifest.json**: Progressive Web App (PWA) の設定ファイルで、Webアプリケーションの表示方法や動作（ホーム画面への追加、オフラインアクセスなど）を定義します。
*   **pytest.ini**: pytestテストフレームワークの構成ファイルで、テストの実行オプションや設定を定義します。
*   **requirements-dev.txt**: 開発環境やテスト環境で必要となるPythonの依存関係パッケージをリストアップします。
*   **requirements.txt**: プロジェクトの実行（本番環境）に必要となるPythonの依存関係パッケージをリストアップします。
*   **robots.txt**: 検索エンジンのウェブクローラーに対して、サイト内のどのページをクロールしてよいか、あるいはクロールしてはならないかを指示するファイルです。SEO対策に利用されます。
*   **ruff.toml**: Pythonのリンター兼フォーマッターであるRuffの設定ファイルです。コードスタイルのルールや自動修正の設定を定義します。
*   **src/**: プロジェクトの主要なソースコードが格納されているディレクトリです。
    *   **__init__.py**: Pythonがこのディレクトリをパッケージとして認識するために必要となるファイルです。
    *   **generate_repo_list/**: リポジトリ一覧を生成するロジックをカプセル化したサブパッケージです。
        *   **__init__.py**: `generate_repo_list` ディレクトリがPythonサブパッケージであることを示します。
        *   **badge_generator.py**: リポジトリのステータスや技術を示すバッジの生成ロジックを扱います。
        *   **config.yml**: プロジェクトの各種設定（プロジェクト概要取得機能の有効/無効、ファイルパス、タイムアウトなど）を定義する設定ファイルです。
        *   **config_manager.py**: `config.yml` や `secrets.toml` など、プロジェクトの設定ファイルを読み込み、管理する機能を提供します。
        *   **date_formatter.py**: 日付や時刻の表示形式を整形するためのユーティリティ関数を提供します。
        *   **generate_repo_list.py**: GitHub APIからリポジトリ情報を取得し、それを基にMarkdown形式のリポジトリ一覧を生成するメインスクリプトです。
        *   **json_ld_template.json**: 検索エンジン最適化 (SEO) のための構造化データ形式であるJSON-LDのテンプレートを定義します。
        *   **language_info.py**: GitHubリポジトリの言語情報を分析・処理し、表示に利用可能な形式に変換する機能を提供します。
        *   **markdown_generator.py**: 取得・整形されたリポジトリ情報を受け取り、最終的なMarkdownコンテンツ（特にリポジトリ一覧）を生成する役割を担います。
        *   **project_overview_fetcher.py**: 各GitHubリポジトリ内の `generated-docs/project-overview.md` ファイルから、プロジェクトの3行概要を自動的に取得する機能を提供します。
        *   **readme_badge_extractor.py**: リポジトリのREADMEファイルから特定のバッジ情報（例: ビルドステータス、カバレッジ）を抽出し、表示に利用する機能です。
        *   **repository_processor.py**: GitHub APIから取得した生のリポジトリデータを受け取り、それをプロジェクトの表示要件に合わせてフィルタリング、整形、追加情報（例: アクティブ/アーカイブ/フォークの分類）の付与を行う中心的な処理モジュールです。
        *   **seo_template.yml**: 検索エンジン最適化（SEO）関連のメタデータやテンプレート設定を定義するファイルです。
        *   **statistics_calculator.py**: リポジトリに関する統計情報（例: スター数、フォーク数、最終更新日時など）を計算し、表示に利用可能な形式で提供します。
        *   **strings.yml**: UIメッセージ、説明文、ラベルなど、表示されるテキストコンテンツを管理するファイルです。多言語対応や文言の変更を容易にします。
        *   **template_processor.py**: Markdownの生成において使用されるテンプレート（Jekyll Liquid構文など）を処理し、動的なコンテンツを挿入する機能を提供します。
        *   **url_utils.py**: URLの検証、構築、パースなど、URL関連の様々なユーティリティ関数を提供します。
*   **test_project_overview.py**: `project_overview_fetcher.py` モジュールの機能（プロジェクト概要の取得）をテストするためのスクリプトです。
*   **tests/**: プロジェクト全体のテストスクリプトを格納するディレクトリです。
    *   **test_badge_generator_integration.py**: `badge_generator.py` の統合テストです。
    *   **test_config.py**: 設定ファイル (`config.yml` など) の読み込みや解釈が正しく行われるかをテストします。
    *   **test_date_formatter.py**: `date_formatter.py` モジュールの日付整形機能が正しく動作するかをテストします。
    *   **test_environment.py**: テスト実行環境や依存関係が適切に設定されているかを検証します。
    *   **test_integration.py**: `generate_repo_list.py` を含む、複数のモジュール間の連携が正しく行われるかをテストする統合テストです。
    *   **test_markdown_generator.py**: `markdown_generator.py` が期待通りのMarkdownコンテンツを生成するかをテストします。
    *   **test_project_overview_fetcher.py**: `project_overview_fetcher.py` がGitHubからプロジェクト概要を正しく取得できるかをテストします。
    *   **test_readme_badge_extractor.py**: `readme_badge_extractor.py` がREADMEからバッジ情報を正しく抽出できるかをテストします。
    *   **test_repository_processor.py**: `repository_processor.py` がリポジトリ情報を正しく処理・整形できるかをテストします。

## 関数詳細説明
提供された情報には個別の関数に関する詳細が含まれていないため、具体的な関数名、引数、戻り値、機能の説明はできません。ただし、主要なモジュールが果たす機能については「ファイル詳細説明」セクションで言及しています。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした

---
Generated at: 2026-01-29 07:09:11 JST
