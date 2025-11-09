# generate repo list in cat2151.github.io

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
