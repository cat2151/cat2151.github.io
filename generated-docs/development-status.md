Last updated: 2026-08-23

# Development Status

## 現在のIssues
- 現在、プロジェクトにはオープン中のIssueはありません。
- そのため、既存の自動化スクリプトやワークフローの改善に焦点を当てます。
- 特に、プロジェクトサマリー生成やリポジトリリスト生成機能の強化が考えられます。

## 次の一手候補
1. `generate_repo_list`スクリプトの機能強化と堅牢性向上 [Issue #Proposed-1](../issue-notes/Proposed-1.md)
   - 最初の小さな一歩: `src/generate_repo_list/generate_repo_list.py`内の既存のデータ取得ロジックとエラーハンドリング部分をレビューし、改善点を特定する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `src/generate_repo_list/generate_repo_list.py`

     実行内容: `generate_repo_list.py`スクリプトのデータ取得処理とエラーハンドリングメカニズムを分析し、以下の観点から改善点を提案してください：
     1) APIコール時のレートリミット処理の強化
     2) データ不整合発生時のロギングとリカバリー戦略
     3) 新しいリポジトリメタデータ（例: stars, forksなど）の追加収集可能性

     確認事項: 作業前に、`src/generate_repo_list/repository_processor.py`や`src/generate_repo_list/project_overview_fetcher.py`など、関連するデータ取得・処理モジュールとの依存関係を確認してください。

     期待する出力: 分析結果と提案された改善点をMarkdown形式で出力してください。具体的には、各改善点について、実装の方向性と期待される効果を含めてください。
     ```

2. プロジェクトサマリー生成の柔軟性向上と新しい情報源の統合 [Issue #Proposed-2](../issue-notes/Proposed-2.md)
   - 最初の小さな一歩: `DevelopmentStatusGenerator.cjs`がどのように情報を収集・整形しているかを確認し、`prompt/development-status-prompt.md`への入力としてどのようなデータが利用可能か調査する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `.github/actions-tmp/.github_automation/project_summary/scripts/development/DevelopmentStatusGenerator.cjs`, `.github/actions-tmp/.github_automation/project_summary/scripts/ProjectSummaryCoordinator.cjs`, `.github/actions-tmp/.github_automation/project_summary/prompts/development-status-prompt.md`

     実行内容: 上記ファイルを分析し、プロジェクトサマリー（開発状況）生成プロセスにおいて、既存のデータソースに加えて、どのような新しい情報源（例: 特定のファイル内容、他のワークフローの実行結果など）を統合できるか、その拡張性を評価してください。特に、プロンプトのカスタマイズ性を向上させるための構造変更案を検討してください。

     確認事項: プロンプトとスクリプト間のデータの受け渡し方法、および既存のサマリー生成ロジックへの影響を確認してください。ハルシネーションを避けるため、プロジェクト内に存在する具体的なファイルやワークフローの出力に限定して情報源を検討してください。

     期待する出力: 拡張性の評価結果と、新しい情報源を統合するための具体的な変更案（例: 設定ファイルによるプロンプトの動的調整、追加データの取得関数）をMarkdown形式で記述してください。
     ```

3. `callgraph`ワークフローの安定化とメインワークフローへの統合 [Issue #Proposed-3](../issue-notes/Proposed-3.md)
   - 最初の小さな一歩: `.github/actions-tmp/`ディレクトリ内の`callgraph.yml`とその関連スクリプトが持つ機能と、なぜこのディレクトリに配置されているのかを調査する。
   - Agent実行プロンプ:
     ```
     対象ファイル: `.github/actions-tmp/.github/workflows/callgraph.yml`, `.github/actions-tmp/.github_automation/callgraph/scripts/analyze-codeql.cjs`, `.github/actions-tmp/.github_automation/callgraph/scripts/generate-html-graph.cjs`

     実行内容: 上記`callgraph`関連ファイルを分析し、このワークフローを`.github/workflows/`に移動させ、安定版として稼働させるために必要な変更点を洗い出してください。具体的には、以下の観点から検討してください：
     1) 依存関係（Node.jsバージョン、CodeQL CLIなど）の明確化と管理
     2) 設定（例: リポジトリ名、ブランチ）の汎用化
     3) 外部から利用されるActionとしてのパッケージング要件

     確認事項: メインの`.github/workflows`ディレクトリにある他のワークフロー（例: `call-daily-project-summary.yml`）との命名規則や、依存関係の競合がないかを確認してください。また、`actions-tmp`ディレクトリの存在意義と、`callgraph`ワークフローが一時的なものとして扱われている理由を考慮に入れてください。

     期待する出力: `callgraph`ワークフローを安定化し、メインのワークフローディレクトリに統合するための移行計画をMarkdown形式で記述してください。計画には、具体的なファイルパスの変更、必要な設定の調整、およびテスト戦略を含めてください。

---
Generated at: 2026-08-23 07:05:09 JST
