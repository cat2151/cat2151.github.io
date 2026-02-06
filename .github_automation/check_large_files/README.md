# Check Large Files Automation

このディレクトリには、大きなソースファイルを検出して GitHub Issue を自動作成する自動化スクリプトが含まれています。

## 概要

このツールは、指定された行数を超えるソースファイルを検出し、リファクタリングが必要なファイルを通知するための GitHub Issue を自動的に作成または更新します。

## ディレクトリ構成

```
.github_automation/check_large_files/
├── README.md                          # このファイル
├── check-large-files.toml             # 設定ファイル
└── scripts/
    └── check_large_files.py           # メインスクリプト
```

## 使用方法

### GitHub Actions での使用

このリポジトリには2つのワークフローが含まれています：

1. **再利用可能ワークフロー** (`.github/workflows/check-large-files-reusable.yml`)
   - 他のワークフローから呼び出すことができる汎用ワークフロー
   - 他のリポジトリからも参照可能

2. **呼び出しワークフロー** (`.github/workflows/call-check-large-files.yml`)
   - 毎日 UTC 18:00 (日本時間 03:00) に自動実行
   - 手動実行も可能 (workflow_dispatch)

### ローカルでの実行

```bash
# スクリプトを直接実行
python .github_automation/check_large_files/scripts/check_large_files.py

# 環境変数で出力先を指定
OUTPUT_DIR=/tmp/output python .github_automation/check_large_files/scripts/check_large_files.py
```

## 設定

`check-large-files.toml` で以下を設定できます：

### [settings] セクション

- `max_lines`: 閾値となる行数（デフォルト: 500）
- `issue_labels`: Issue に付けるラベルのリスト
- `issue_title`: Issue タイトルのテンプレート

### [scan] セクション

- `include_patterns`: スキャン対象のファイルパターン（glob形式）
- `exclude_patterns`: 除外するパターン（ディレクトリやファイル拡張子）
- `exclude_files`: 除外する特定のファイル

## 出力

スクリプトは以下のファイルを生成します（デフォルト: `/tmp/check-large-files-output/`）：

- `file_count.txt`: 検出されたファイル数
- `issue_title.txt`: Issue のタイトル
- `issue_body.txt`: Issue の本文
- `issue_labels.txt`: Issue のラベル（カンマ区切り）
- `issue_title_pattern.txt`: 既存 Issue 検索用のパターン
- `large_files.txt`: 検出されたファイルのリスト
- `summary.json`: 検出結果の JSON サマリー

## 他のリポジトリで使用する

この再利用可能ワークフローを他のリポジトリで使用するには：

```yaml
name: Check Large Files

on:
  schedule:
    - cron: '0 18 * * *'
  workflow_dispatch:

jobs:
  check-large-files:
    uses: cat2151/cat2151.github.io/.github/workflows/check-large-files-reusable.yml@main
```

## 要件

- Python 3.11 推奨（`tomli` により 3.11 未満の Python もサポートされます）
- GitHub Actions 実行環境

## ライセンス

このプロジェクトのライセンスに従います。
