Last updated: 2026-07-31

# Development Status

## 現在のIssues
オープン中のIssueはありません。

## 次の一手候補
1. 自動生成プロンプトの品質向上
   - 最初の小さな一歩: `development-status-prompt.md` と `project-overview-prompt.md` の内容を比較し、重複する指示や改善の余地がないか初期分析を行います。
   - Agent実行プロンプト:
     ```
     対象ファイル: .github/actions-tmp/.github_automation/project_summary/prompts/development-status-prompt.md
                   .github/actions-tmp/.github_automation/project_summary/prompts/project-overview-prompt.md

     実行内容: 上記の2つのプロンプトファイルを分析し、以下の観点から改善点を提案してください：
               1. 各プロンプトの目的と現状の出力形式の整合性
               2. ハルシネーションを避けるための指示の明確さ
               3. 共通化できる、またはより汎用的な指示がないか
               4. 現在のガイドライン（本プロンプト）との一貫性

     確認事項: プロンプトの変更が既存のプロジェクトサマリー生成ワークフロー（call-daily-project-summary.yml）に与える影響を確認してください。特に、出力フォーマットの崩れや意図しない情報の生成がないことを確認します。

     期待する出力: 改善提案をmarkdown形式で出力してください。具体的には、各プロンプトファイルに対する具体的な修正案、およびその修正が期待する効果を含めてください。
     ```

2. リポジトリリスト生成スクリプトのテストカバレッジ向上
   - 最初の小さな一歩: `src/generate_repo_list/` ディレクトリ内の主要なロジックを含むPythonファイルを特定し、既存のテストファイル（例: `tests/test_repository_processor.py`）と比較してテストが手薄なモジュールをリストアップします。
   - Agent実行プロンプト:
     ```
     対象ファイル: src/generate_repo_list/*.py
                   tests/*.py

     実行内容: `src/generate_repo_list/` ディレクトリ内のPythonスクリプトについて、既存の `tests/` ディレクトリ内のテストファイルのテストカバレッジを分析してください。特に、テストが不足しているか、全くテストケースがない関数やクラスを特定し、その機能に対する簡単なテストケースのアイデアを提案してください。

     確認事項: 分析対象のファイルは、リポジトリリスト生成の主要なロジックを担っていることを確認してください。また、既存のテストコードの構造と命名規則を尊重したテストケースのアイデアであることを確認します。

     期待する出力: Markdown形式で、テストカバレッジが低いと判断されたファイルと、それぞれに対して追加すべきテストケースの簡単な概要（例: テスト対象関数、テストすべきシナリオ）を記述してください。
     ```

3. GitHub Actions `callgraph` の導入ガイド作成
   - 最初の小さな一歩: `.github/actions-tmp/.github/workflows/callgraph.yml` ファイルをレビューし、`callgraph` Actionが外部プロジェクトで利用される際に必要となる入力パラメータ、シークレット、およびその他の設定要件を洗い出します。
   - Agent実行プロンプト:
     ```
     対象ファイル: .github/actions-tmp/.github/workflows/callgraph.yml
                   .github/actions-tmp/.github_automation/callgraph/README.md
                   .github/actions-tmp/.github_automation/callgraph/docs/callgraph.md

     実行内容: 上記ファイルを分析し、外部プロジェクトがGitHub Actions `callgraph` を自身のワークフローに導入するために必要な手順を明確にしてください。以下の観点を必ず含めてください：
               1) 必須入力パラメータとその設定方法
               2) 必須シークレット（例: GEMINI_API_KEY など、もし必要であれば）の登録手順
               3) ファイル配置の前提条件（例: codeql-queriesの配置など）
               4) 外部プロジェクトでの利用時に必要な追加設定や考慮事項

     確認事項: `callgraph.yml` が再利用可能なワークフローとして設計されていることを前提に分析を進めてください。また、既存の関連ドキュメント（callgraph.mdなど）との整合性を確認し、重複や矛盾がないようにしてください。

     期待する出力: 外部プロジェクトが `callgraph` Actionを導入する際の手順書をmarkdown形式で生成してください。手順は具体的で、コピー＆ペーストで利用できるようなYAMLスニペットを含めるとより良いです。
     ```

---
Generated at: 2026-07-31 07:25:18 JST
