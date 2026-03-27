Last updated: 2026-03-28

# Project Overview

## プロジェクト概要
- GitHub Pagesサイト向けにリポジトリ一覧を自動生成するシステムです。
- GitHub APIを活用し、リポジトリ情報からSEO最適化されたMarkdownファイルを生成します。
- 検索エンジンでの発見性を高め、LLMによるリポジトリ参照精度向上を支援します。

## 技術スタック
- フロントエンド: Jekyll (GitHub Pages) - 生成されたMarkdownファイルを静的サイトとして公開し、GitHub Pagesのプラットフォーム上で動作します。
- 音楽・オーディオ: (該当する技術はありません)
- 開発ツール:
    - Git: ソースコードのバージョン管理システムとして使用されます。
    - pytest: Pythonプロジェクトの単体テスト、統合テストを実行するためのフレームワークです。
    - ruff: Pythonコードの高速なリンターおよびフォーマッターで、コード品質と一貫性を保ちます。
    - EditorConfig: 異なるエディタやIDE間で一貫したコーディングスタイルを維持するための設定ファイル。
    - PyYAML: YAML形式の設定ファイル (`config.yml`, `strings.yml`) の読み書きに使用されるPythonライブラリ。
    - requests: GitHub APIとの通信を含むHTTPリクエストを送信するために使用されるPythonライブラリ。
    - TOML: 設定ファイル (`secrets.toml`) のフォーマットとして使用されます。
- テスト: pytest - プロジェクトの各コンポーネントが期待通りに機能するかを検証し、品質を保証するために利用されます。
- ビルドツール: (明示的なビルドツールはありませんが、) Markdown生成プロセス自体が、静的サイトのコンテンツを「ビルド」する一部とみなすことができます。
- 言語機能: Python - プロジェクトの主要なスクリプト言語であり、GitHub APIとの連携、データ処理、Markdown生成など、システムの中核を担います。
- 自動化・CI/CD: GitHub Actions - `.github_automation` ディレクトリの存在から、特定のタスクの自動化や継続的インテグレーション/デプロイメントの基盤として利用される可能性が示唆されます。
- 開発標準: ruff - コードのスタイルチェックとフォーマットを自動化し、コードの品質と可読性を統一します。EditorConfig - 開発環境全体でのコードスタイルの一貫性を保証します。

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
- `README.md`: プロジェクトの目的、機能、セットアップ方法、実行コマンド、開発者向けのヒントなどを記述した、プロジェクトの主要な説明文書です。
- `LICENSE`: このプロジェクトがMITライセンスの下で公開されていることを示すライセンス情報ファイルです。
- `_config.yml`: Jekyllサイト全体の設定ファイルであり、GitHub Pagesの動作に関する基本的な設定を定義します。
- `index.md`: GitHub Pagesサイトのトップページとして機能するMarkdownファイルで、生成されたリポジトリ一覧がここに出力されます。
- `pytest.ini`: `pytest` テストフレームワークの設定ファイルで、テストの実行オプションや挙動をカスタマイズします。
- `requirements.txt`: プロジェクトの本番環境で必要とされるPythonパッケージとそのバージョンを列挙したファイルです。
- `requirements-dev.txt`: 開発およびテスト環境で必要とされる追加のPythonパッケージを列挙したファイルです。
- `ruff.toml`: `ruff` コードリンターおよびフォーマッターの設定ファイルで、プロジェクトのコードスタイルルールを定義します。
- `src/generate_repo_list/generate_repo_list.py`: このプロジェクトのメインスクリプトであり、GitHub APIからのリポジトリ情報取得、データ処理、最終的なMarkdownファイルの生成という一連の処理をオーケストレートします。
- `src/generate_repo_list/config.yml`: プロジェクトの技術的なパラメータ（例: プロジェクト概要取得機能の有効/無効、APIタイムアウト値など）を定義する設定ファイルです。
- `src/generate_repo_list/strings.yml`: プロジェクト内で使用される各種表示メッセージや文言を管理するための設定ファイルで、文言の統一や変更を容易にします。
- `src/generate_repo_list/badge_generator.py`: リポジトリのプログラミング言語、ライセンスなどの情報に基づき、対応するバッジのMarkdownを生成するロジックを含みます。
- `src/generate_repo_list/config_manager.py`: `config.yml` や `strings.yml` といった設定ファイルを読み込み、プロジェクト内の他のモジュールが設定値にアクセスするためのユーティリティを提供します。
- `src/generate_repo_list/date_formatter.py`: 日付や時刻の情報を特定のフォーマット（例: 人間が読みやすい形式）に変換するためのユーティリティ関数を提供します。
- `src/generate_repo_list/json_ld_template.json`: 検索エンジン最適化（SEO）のために利用されるJSON-LD（Linked Data）のテンプレートです。コンテンツの意味を構造化データとして検索エンジンに伝えます。
- `src/generate_repo_list/language_info.py`: リポジトリのプログラミング言語に関する情報を処理し、表示に適した形式に変換するロジックを含みます。
- `src/generate_repo_list/markdown_generator.py`: GitHub APIから取得し処理されたリポジトリ情報に基づいて、整形されたMarkdownコンテンツを生成するコアロジックを持つファイルです。
- `src/generate_repo_list/project_overview_fetcher.py`: 各リポジトリ内の特定のファイル（`generated-docs/project-overview.md`）から、そのリポジトリの3行のプロジェクト概要を自動的に取得する機能を提供します。
- `src/generate_repo_list/readme_badge_extractor.py`: リポジトリのREADMEファイルから、特定のパターンに一致するバッジ情報やその他の情報を抽出するためのユーティリティです。
- `src/generate_repo_list/repository_processor.py`: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、整形し、後続のMarkdown生成に適した形式に変換する役割を担います。
- `src/generate_repo_list/seo_template.yml`: 検索エンジン最適化（SEO）に関する具体的な設定やテンプレートを定義するファイルです。
- `src/generate_repo_list/statistics_calculator.py`: リポジトリのスター数やフォーク数など、各種統計情報を計算または集計する機能を持つファイルです。
- `src/generate_repo_list/template_processor.py`: Markdownやその他のテキストテンプレート内のプレースホルダーを、実際のデータで置き換える処理を行うユーティリティです。
- `src/generate_repo_list/url_utils.py`: URLの操作、検証、エンコード/デコードなど、URLに関連するユーティリティ関数を提供します。
- `tests/`: プロジェクトの各モジュールや機能の単体テスト、統合テストを格納するディレクトリです。`test_*.py` ファイル群が含まれます。
- `.github_automation/check_large_files/scripts/check_large_files.py`: GitHub ActionsなどのCI/CD環境で実行され、リポジトリ内の特定のサイズを超えるファイルを検出してレポートするためのスクリプトです。
- `debug_project_overview.py`: `project_overview_fetcher` などのプロジェクト概要取得機能の動作を確認・デバッグするための補助スクリプトです。
- `test_project_overview.py`: `project_overview_fetcher` モジュールのテストケースを記述したファイルです。
- `googled947dc864c270e07.html`: Google Search Consoleによるウェブサイトの所有権確認のために配置されたファイルです。
- `manifest.json`: プログレッシブウェブアプリ（PWA）の機能を提供する際に使用されるWeb App Manifestファイルで、アプリのメタデータや表示設定を定義します。
- `robots.txt`: 検索エンジンのウェブクローラーに対して、サイトのどの部分をクロールしてもよいか、またはクロールすべきでないかを指示するファイルです。
- `assets/`: GitHub Pagesサイトで使用されるファビコン、ロゴ、画像などの静的アセットファイルを格納するディレクトリです。

## 関数詳細説明
提供された情報からは具体的な関数のシグネチャ（引数、戻り値）を抽出できませんでしたが、各ファイルの役割から推測される主要な処理内容について説明します。

- `src/generate_repo_list/generate_repo_list.py` の主要関数群:
    - 役割: プロジェクト全体の処理フローを統括し、GitHub APIからのリポジトリ情報取得、データ処理、Markdown生成を順序立てて実行します。
    - 機能: コマンドライン引数の解析、設定の読み込み、各モジュール（例: `repository_processor`, `project_overview_fetcher`, `markdown_generator`）の呼び出しを行い、最終的な出力ファイルを生成します。

- `src/generate_repo_list/repository_processor.py` の主要関数群:
    - 役割: GitHub APIから取得した生のリポジトリデータを受け取り、表示に必要な情報を抽出、整形します。
    - 機能: リポジトリの言語、スター数、最終更新日、説明などの属性を処理し、後続のMarkdown生成に適した構造化された形式に変換します。

- `src/generate_repo_list/project_overview_fetcher.py` の主要関数群:
    - 役割: 各リポジトリ内の指定されたファイル（例: `generated-docs/project-overview.md`）から、プロジェクトの概要説明を自動で抽出します。
    - 機能: GitHub APIを介してファイルを読み込み、特定のセクションタイトル（例: "プロジェクト概要"）配下にある3行の要約を解析して返します。

- `src/generate_repo_list/markdown_generator.py` の主要関数群:
    - 役割: 処理されたリポジトリ情報に基づいて、GitHub Pages向けの整形されたMarkdownコンテンツを生成します。
    - 機能: テンプレートや整形ルールに従って、リポジトリ一覧、各リポジトリの詳細、バッジなどを含む完全なMarkdown文字列を構築します。

- `src/generate_repo_list/config_manager.py` の主要関数群:
    - 役割: `config.yml` や `strings.yml` などの設定ファイルを読み込み、設定値へのアクセスをプロジェクト全体に提供します。
    - 機能: YAMLファイルのパース、デフォルト値の適用、設定値の取得と管理を行います。

- `src/generate_repo_list/badge_generator.py` の主要関数群:
    - 役割: リポジトリの属性（言語、ライセンス、ステータスなど）に対応するバッジのMarkdown形式の文字列を生成します。
    - 機能: 指定された属性に基づいて適切なバッジのURLとMarkdown形式の記述を作成します。

- `src/generate_repo_list/date_formatter.py` の主要関数群:
    - 役割: GitHub APIから取得される日付や時刻の情報を、人間が読みやすい特定の表示フォーマットに変換します。
    - 機能: 日付文字列のパース、フォーマット適用、タイムゾーン調整などを行います。

- `src/generate_repo_list/language_info.py` の主要関数群:
    - 役割: リポジトリのプログラミング言語に関する情報を処理し、表示可能な形式に変換します。
    - 機能: 主要言語の特定、言語ごとの表示調整、複数言語の表示方法などを管理します。

- `src/generate_repo_list/readme_badge_extractor.py` の主要関数群:
    - 役割: リポジトリのREADMEファイルの内容を解析し、特定のバッジ情報やその他の構造化された情報を抽出します。
    - 機能: README内の特定のパターン（例: 画像URL、リンク）に一致する文字列を検索し、取得します。

- `src/generate_repo_list/statistics_calculator.py` の主要関数群:
    - 役割: リポジトリのスター数やフォーク数など、各種統計情報を計算または集計します。
    - 機能: 取得したデータから必要な統計値を算出し、出力に適した形式で提供します。

- `src/generate_repo_list/template_processor.py` の主要関数群:
    - 役割: Markdownテンプレート内のプレースホルダー（例: `{{ repo.name }}`）を実際の内容で置き換える処理を行います。
    - 機能: 指定されたデータとテンプレートを用いて、最終的なMarkdownコンテンツを動的に組み立てます。

- `src/generate_repo_list/url_utils.py` の主要関数群:
    - 役割: URLの操作や検証に関連するユーティリティ機能を提供します。
    - 機能: URLのエンコード、デコード、正規化、パスの結合などの処理を行います。

- `.github_automation/check_large_files/scripts/check_large_files.py` の主要関数群:
    - 役割: リポジトリ内のファイルシステムを走査し、設定されたサイズ制限を超過しているファイルを検出します。
    - 機能: ファイルサイズの取得、閾値との比較、検出された大規模なファイルのリスト化とレポートを行います。

## 関数呼び出し階層ツリー
```
提供された情報からは関数呼び出し階層を分析できませんでした。

---
Generated at: 2026-03-28 07:10:31 JST
