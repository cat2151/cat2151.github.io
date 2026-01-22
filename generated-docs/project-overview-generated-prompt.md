Last updated: 2026-01-23


# プロジェクト概要生成プロンプト（来訪者向け）

## 生成するもの：
- projectを3行で要約する
- プロジェクトで使用されている技術スタックをカテゴリ別に整理して説明する
- プロジェクト全体のファイル階層ツリー（ディレクトリ構造を図解）
- プロジェクト全体のファイルそれぞれの説明
- プロジェクト全体の関数それぞれの説明
- プロジェクト全体の関数の呼び出し階層ツリー

## 生成しないもの：
- Issues情報（開発者向け情報のため）
- 次の一手候補（開発者向け情報のため）
- ハルシネーションしそうなもの（例、存在しない機能や計画を勝手に妄想する等）

## 出力フォーマット：
以下のMarkdown形式で出力してください：

```markdown
# Project Overview

## プロジェクト概要
[以下の形式で3行でプロジェクトを要約]
- [1行目の説明]
- [2行目の説明]
- [3行目の説明]

## 技術スタック
[使用している技術をカテゴリ別に整理して説明]
- フロントエンド: [フロントエンド技術とその説明]
- 音楽・オーディオ: [音楽・オーディオ関連技術とその説明]
- 開発ツール: [開発支援ツールとその説明]
- テスト: [テスト関連技術とその説明]
- ビルドツール: [ビルド・パース関連技術とその説明]
- 言語機能: [言語仕様・機能とその説明]
- 自動化・CI/CD: [自動化・継続的統合関連技術とその説明]
- 開発標準: [コード品質・統一ルール関連技術とその説明]

## ファイル階層ツリー
```
[プロジェクトのディレクトリ構造をツリー形式で表現]
```

## ファイル詳細説明
[各ファイルの役割と機能を詳細に説明]

## 関数詳細説明
[各関数の役割、引数、戻り値、機能を詳細に説明]

## 関数呼び出し階層ツリー
```
[関数間の呼び出し関係をツリー形式で表現]
```
```


以下のプロジェクト情報を参考にして要約を生成してください：

## プロジェクト情報
名前: 
説明: # generate repo list in cat2151.github.io

GitHub Pages サイト用のリポジトリ一覧自動生成システム

と、生成された cat2151.github.io 用 repo list

## �📝 プロジェクト概要

このプロジェクトは、GitHub API を使用してリポジトリ情報を取得し、Jekyll ベースの GitHub Pages サイト用にマークダウンファイルを自動生成するシステムです。

### これまでの課題と対策

#### 背景

GitHubのユーザーページ（`https://github.com/<username>`）は、検索エンジンのクロール対象になりづらい傾向があります。
そのため、そこに紐づくリポジトリ一覧や各リポジトリのページも、検索結果に表示されにくい場合があります。
さらに、その結果、ClaudeなどのLLMが検索エンジン依存の参照をするとき、リポジトリを参照できず、開発効率に影響が出ることもあります。

#### 対策

この問題を回避するため、GitHub Pages `<username>.github.io` 側に以下を自動生成する仕組みを作成しました。

- GitHubリポジトリ一覧ページ
- 各リポジトリに対応する GitHub Pages (`<username>.github.io/<repo>`) へのリンク

これにより、GitHub Pages 側（`github.io`ドメイン）が検索エンジンにクロールされやすくなり、
各リポジトリの内容やリンクもインデックスされやすくなり、LLMがリポジトリ参照に失敗することがある問題の緩和が期待されます。

### 主な機能

- GitHub API によるリポジトリ情報の自動取得
- SEO最適化された Markdown 生成
- バッジ付きリポジトリ表示
- アクティブ・アーカイブ・フォークによる分類
- **プロジェクト概要自動取得**: 各リポジトリの `generated-docs/project-overview.md` から3行の魅力的な説明を自動取得・表示
- Jekyll/GitHub Pages 対応

### 💡 開発者向けのヒント

- このREADMEはあまり整備されていません。「で、なんのために、まず何をやれば動かせるの？」がわかりづらそうです。今後の課題です
- テスト実行前に `ruff check . --fix` でコードスタイルを自動修正
- 新機能追加時は対応するテストも追加してください
- CI/CD不要のローカル開発重視の構成

### 🚀 クイックテスト実行

```powershell
pytest
```

### ⚙️ 設定ファイル

- `pytest.ini`: pytest設定
- `ruff.toml`: コードスタイル設定
- `requirements.txt`: 本番依存関係
- `requirements-dev.txt`: 開発・テスト依存関係
- `src/generate_repo_list/config.yml`: プロジェクト概要取得機能などの技術的パラメータ
- `src/generate_repo_list/strings.yml`: 表示メッセージ・文言管理

## � 実際の生成コマンド

### 基本的な生成コマンド

```powershell
# リポジトリ一覧を生成してindex.mdに出力
python src/generate_repo_list/generate_repo_list.py --username cat2151 --output index.md

# 開発時（最初の1件のみ処理で高速テスト）
python src/generate_repo_list/generate_repo_list.py --username cat2151 --output index.md --limit 1
```

### 利用可能なオプション

| オプション | 説明 | 例 |
|------------|------|-----|
| `--username` | GitHub ユーザー名（必須） | `cat2151` |
| `--output` | 出力ファイル名（必須） | `index.md` |
| `--limit` | 処理するリポジトリ数の上限（開発用） | `1` |

### 実行前の準備

1. **GitHub トークンの設定**（ローカル実行時）
   ```toml
   # secrets/secrets.toml に作成
   [github]
   token = "your_github_token_here"
   ```

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

## 🎯 プロジェクト概要機能

### 概要
各リポジトリの `generated-docs/project-overview.md` ファイルから「プロジェクト概要」セクションの3行説明を自動取得し、リポジトリ一覧に表示する機能です。

### 対象フォーマット

```markdown
## プロジェクト概要
- 🚀 プロジェクトごとのGitHub Actions管理をもっと楽に
- 🔗 共通化されたワークフローで、どのプロジェクトからも呼ぶだけでOK
- ✅ メンテは一括、プロジェクト開発に集中できます
```

### 設定

config.ymlでの制御:

```yaml
project_overview:
  enabled: true  # 機能のON/OFF
  target_file: "generated-docs/project-overview.md"  # 対象ファイル
  section_title: "プロジェクト概要"  # 抽出対象セクション
  max_retries: 1  # API失敗時のリトライ回数
  timeout_seconds: 10  # タイムアウト時間
  enable_cache: true  # 同一実行内でのキャッシュ
```


依存関係:
{}

## ファイル階層ツリー
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

## ファイル詳細分析
**googled947dc864c270e07.html** (1行, 53バイト)
  - 関数: なし
  - インポート: なし

## 関数呼び出し階層
関数呼び出し階層を分析できませんでした

## プロジェクト構造（ファイル一覧）
README.md
googled947dc864c270e07.html
index.md
issue-notes/10.md
issue-notes/12.md
issue-notes/14.md
issue-notes/16.md
issue-notes/18.md
issue-notes/2.md
issue-notes/4.md
issue-notes/6.md
issue-notes/8.md
manifest.json
src/generate_repo_list/json_ld_template.json

上記の情報を基に、プロンプトで指定された形式でプロジェクト概要を生成してください。
特に以下の点を重視してください：
- 技術スタックは各カテゴリごとに整理して説明
- ファイル階層ツリーは提供された構造をそのまま使用
- ファイルの説明は各ファイルの実際の内容と機能に基づく
- 関数の説明は実際に検出された関数の役割に基づく
- 関数呼び出し階層は実際の呼び出し関係に基づく


---
Generated at: 2026-01-23 07:06:37 JST
