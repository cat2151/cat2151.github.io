Last updated: 2026-05-28

# Development Status

## 現在のIssues
オープン中のIssueはありません。

## 次の一手候補
1.  リポジトリリスト生成スクリプトの機能強化 (スター数・フォーク数の表示)
    -   最初の小さな一歩: `src/generate_repo_list/repository_processor.py` に、GitHub APIからリポジトリのスター数とフォーク数を取得するロジックを追加する。
    -   Agent実行プロンプト:
        ```
        対象ファイル: src/generate_repo_list/repository_processor.py

        実行内容: src/generate_repo_list/repository_processor.py の `fetch_repository_data` メソッド（または類似のデータ取得メソッド）を分析し、GitHub APIからリポジトリのスター数とフォーク数を取得できるように拡張する変更点をmarkdown形式で提案してください。

        確認事項: GitHub APIのレートリミット、既存のデータ構造への影響、認証方法（もし必要であれば）を確認してください。

        期待する出力: 提案された変更内容、およびそれが `repository_processor.py` にどのように統合されるかを示すコードスニペットを含むmarkdown形式の出力。
        ```

2.  開発状況レポート生成プロンプトの精度向上 (Issueがない場合の提案ロジック)
    -   最初の小さな一歩: `.github_automation/project_summary/prompts/development-status-prompt.md` の内容を読み込み、オープンIssueがない場合に「次の一手候補」をより適切に生成するための改善点を洗い出す。
    -   Agent実行プロンプト:
        ```
        対象ファイル: .github_automation/project_summary/prompts/development-status-prompt.md

        実行内容: 現在の開発状況生成プロンプトを分析し、オープンIssueがない場合に「次の一手候補」セクションがより具体的で価値のある提案（例: 定期的なリファクタリング、ドキュメント拡充、テストカバレッジ向上など）を生成できるようにするためのプロンプト修正案をmarkdown形式で記述してください。

        確認事項: ハルシネーションを避け、現在のプロジェクトの状況やファイル一覧から妥当な提案が導かれるように考慮してください。

        期待する出力: 既存のプロンプトをどのように変更すべきか、具体的な修正案と、それがどのような出力に繋がるかの期待例を含むmarkdown形式の出力。
        ```

3.  `check-large-files` の設定ファイルの実用化 (プロジェクト固有のルール提案)
    -   最初の小さな一歩: `.github_automation/check_large_files/check-large-files.toml.default` をレビューし、現在のプロジェクトのファイル一覧で特に大きなファイルをチェックすべきディレクトリやファイルタイプがないか確認する。
    -   Agent実行プロンプト:
        ```
        対象ファイル: .github_automation/check_large_files/check-large-files.toml.default

        実行内容: .github_automation/check_large_files/check-large-files.toml.default の内容と、プロジェクトのファイル一覧（特に`generated-docs/`や`assets/`ディレクトリ内のファイル）を考慮し、現在のプロジェクトに最適な`check-large-files.toml`のデフォルト設定案をmarkdown形式で提案してください。例えば、生成されたドキュメントや画像アセットに対する具体的なサイズ制限や除外パスなどを含めてください。

        確認事項: 既存のワークフローやプロジェクトの目的と矛盾しないか、現実的なファイルサイズ制限であるかを確認してください。

        期待する出力: 提案された`check-large-files.toml`の具体的な設定内容、およびその設定が推奨される理由を説明するmarkdown形式の出力。

---
Generated at: 2026-05-28 07:35:28 JST
