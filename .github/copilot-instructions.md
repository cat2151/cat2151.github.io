# cat2151.github.io Copilot Instructions

## プロジェクト概要

この GitHub Pages サイトは、cat2151 の GitHub リポジトリ一覧を自動生成・表示する Jekyll サイトです。主に Python スクリプトによる自動化とSEO最適化が重要な要素となっています。

## アーキテクチャー

### 中核システム
- **`src/generate_repo_list/`**: GitHub API を使ってリポジトリ情報を取得し Markdown を生成
  - `generate_repo_list.py`: メインスクリプト (GitHub Actions / ローカル両対応)
  - `repository_processor.py`: リポジトリ分類・フィルタリング
  - `markdown_generator.py`: バッジ付きMarkdown生成
  - `config_manager.py`: 設定ファイル管理・秘匿情報処理

### Jekyll 設定
- `_config.yml`: SEO プラグイン、PWA設定、パフォーマンス最適化
- `index.md`: 自動生成されるメインページ（手動編集禁止）
- `manifest.json`: PWA マニフェスト

## 重要なワークフロー

### 自動更新システム
```yaml
# .github/workflows/generate_repo_list.yml で毎日UTC 22時実行
python src/generate_repo_list/generate_repo_list.py --username cat2151 --output index.md
```

### スクリプト再実行（短縮コマンド）
```bash
# ローカルでスクリプトを再実行する場合は1行で実行
python src/generate_repo_list/generate_repo_list.py --username cat2151 --output index.md --limit 1
```

### ローカル開発時のトークン管理
```toml
# secrets/secrets.toml (gitignore済み)
[github]
token = "your_token_here"
```

### テスト実行
```bash
pytest
```

## プロジェクト特有の規約

### リポジトリフィルタリングルール
- プライベートリポジトリは除外
- README.md が存在するもののみ含める
- fork は別セクションに分類

### バッジ生成システム
- 言語バッジ: `![Language](https://img.shields.io/badge/Language-{language}-blue)`
- トピックバッジ: 特殊文字のエスケープ処理あり (`-` → `--`, ` ` → `_`)
- GitHub Pages: 自動検出して Available バッジを追加

### 設定ファイル構造
- `config.yml`: バッジ設定、フィルタリングルール、メッセージテンプレート
- `strings.yml`: 多言語対応文字列（現在は日本語のみ）
- `seo_template.yml`: OGP、JSON-LD structured data
- `json_ld_template.json`: schema.org format metadata

## 開発時の注意点

### ファイル編集の制約
- **`index.md` は自動生成されるため直接編集禁止** - スクリプト実行時に上書きされる
- Jekyll設定の変更は `_config.yml` で行う
- リポジトリ表示ルールは `src/generate_repo_list/config.yml` で設定

### 依存関係
```bash
pip install PyGithub PyYAML  # 本番環境
pip install pytest ruff      # 開発環境
```

### コードスタイル
- Ruff 設定: 120文字、E501無視、isort有効
- Python モジュールは単一責任の原則で分割済み

### 環境分岐処理
GitHub Actions環境 → `GITHUB_TOKEN` 環境変数使用
ローカル環境 → `secrets/secrets.toml` 優先、フォールバックで環境変数

## 統合点とデータフロー

1. GitHub API → リポジトリデータ取得
2. 分類・フィルタリング → Active/Archived/Forks
3. テンプレート生成 → バッジ・統計情報付きMarkdown
4. Jekyll処理 → SEO最適化HTML
5. GitHub Actions → 自動デプロイ

新機能追加時は、この自動化チェーンを破らないよう注意してください。

## userからの指示
- もしPythonコードの変更を行ったら、userにコントロールを返す前に、以下の手順を実行してください:
  - ruff format
  - ruff check --fix --unsafe-fixes
  - pytest
