# cat2151.github.io

GitHub Pages サイト用のリポジトリ一覧自動生成システム

## 運用上の注意

このREADME.mdはこのリポジトリに限っては、GitHub Pages表示がされません

かわりに、生成された index.md がGitHub Pagesで表示されます

## �📝 プロジェクト概要

このプロジェクトは、GitHub API を使用してリポジトリ情報を取得し、Jekyll ベースの GitHub Pages サイト用にマークダウンファイルを自動生成するシステムです。

### 主な機能

- GitHub API によるリポジトリ情報の自動取得
- SEO最適化された Markdown 生成
- バッジ付きリポジトリ表示
- アクティブ・アーカイブ・フォークによる分類
- Jekyll/GitHub Pages 対応

### 💡 開発者向けのヒント

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

2. **GitHub トークンの設定**（ローカル実行時）
   ```toml
   # secrets/secrets.toml に作成
   [github]
   token = "your_github_token_here"
   ```

### 注意事項

- **`index.md`は自動生成されるため、直接編集しないでください**
- 設定変更は `src/generate_repo_list/config.yml` で行ってください
- GitHub Actions環境では自動的にトークンが設定されます

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。
