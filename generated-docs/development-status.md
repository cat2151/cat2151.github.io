Last updated: 2025-11-17

# Development Status

## 現在のIssues
- [Issue #14](../issue-notes/14.md)と[Issue #15](../issue-notes/15.md)は、サイト全体の日付表示をUTCとJST（UTC+9）のデュアルタイムゾーンで併記することを目的としている。
- 具体的には、検索エンジン最適化のためにUTC、運用者向けにJSTでの表示が求められており、`YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)`形式での出力を目指す。
- 現在、`DateFormatter`クラスの導入が検討されており、datetimeオブジェクトをこの形式に変換する処理の実装が進められている。

## 次の一手候補
1. [Issue #15](../issue-notes/15.md) `DateFormatter`クラスの完全な実装と単体テスト
   - 最初の小さな一歩: `src/generate_repo_list/date_formatter.py`に`DateFormatter`クラスを実装し、`datetime`オブジェクトをUTCとJSTの両方に変換し、指定されたフォーマット`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`で出力するメソッドの単体テストを作成・実行する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/date_formatter.py` (新規または既存ファイルの更新)

     実行内容: `src/generate_repo_list/date_formatter.py` ファイルに `DateFormatter` クラスを完成させてください。このクラスは、タイムゾーン情報を含む`datetime`オブジェクト、および含まない`datetime`オブジェクトを正確に処理し、UTCとJST（UTC+9）の両方の時刻を`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`形式で返す`format_dual_timezone`メソッドを持つようにします。また、このメソッドの機能を確認するためのpytestによる単体テストを追加してください。

     確認事項: Pythonの`datetime`モジュールと`zoneinfo`（または`pytz`）を使用して、タイムゾーン変換が正確に行われることを確認してください。夏時間への対応は現時点では不要です。

     期待する出力: `src/generate_repo_list/date_formatter.py` ファイルの最終的なコードと、追加されたテストコードのmarkdown形式での出力。
     ```

2. [Issue #14](../issue-notes/14.md) 生成されるMarkdownコンテンツへのデュアルタイムゾーン日付の適用
   - 最初の小さな一歩: `src/generate_repo_list/markdown_generator.py` 内で、リポジトリの最終更新日など、現在日付を表示している箇所を特定し、候補1で実装された`DateFormatter`クラスをインポートして利用するよう修正する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/markdown_generator.py`, `src/generate_repo_list/repository_processor.py`

     実行内容: `src/generate_repo_list/markdown_generator.py` と `src/generate_repo_list/repository_processor.py` を分析し、Markdownコンテンツ（例: `index.md`）に日付を出力している箇所を特定してください。候補1で実装される`DateFormatter`クラスの`format_dual_timezone`メソッドを使用して、これらの日付を`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`形式で表示するよう修正してください。

     確認事項: 既存の日付フォーマットが新しいデュアルタイムゾーン表示に置き換わることを確認してください。日付データが`datetime`オブジェクトとして渡されていることを前提とします。

     期待する出力: `src/generate_repo_list/markdown_generator.py` と `src/generate_repo_list/repository_processor.py` の変更内容を示す差分または修正後のコードスニペットをmarkdown形式で出力。
     ```

3. [Issue #14](../issue-notes/14.md) JSON-LDおよびSEO関連ファイルへのデュアルタイムゾーン日付の適用
   - 最初の小さな一歩: `src/generate_repo_list/json_ld_template.json` や `src/generate_repo_list/seo_template.yml` を確認し、日付フィールドが存在する場合は、それらのフィールドがUTC形式で保持されるようにしつつ、必要であれば追加情報としてJSTを併記する計画を立てる。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/json_ld_template.json`, `src/generate_repo_list/seo_template.yml`, `src/generate_repo_list/template_processor.py`

     実行内容: `src/generate_repo_list/json_ld_template.json` と `src/generate_repo_list/seo_template.yml` を分析し、日付情報が含まれている箇所を特定してください。検索エンジン向けにUTC形式が必須であるため、これらのフィールドは引き続きUTC形式を維持します。しかし、[Issue #14](../issue-notes/14.md)で求められている「UTCとJSTを併記」の要件に基づき、もしJSON-LDスキーマやSEOテンプレートが追加情報としてJSTを許容する場合、`DateFormatter`クラスを利用してJST情報を追加する方法を検討し、変更点を提案してください。追加が難しい場合は、その理由も明記してください。

     確認事項: JSON-LDスキーマやSEOのベストプラクティスに従い、検索エンジンのクロールに悪影響を与えないことを確認してください。

     期待する出力: `json_ld_template.json`と`seo_template.yml`の分析結果、および`template_processor.py`における変更提案をmarkdown形式で出力。変更が不要または推奨されない場合はその根拠を記述してください。

---
Generated at: 2025-11-17 07:05:43 JST
