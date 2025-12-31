Last updated: 2026-01-01

# Development Status

## 現在のIssues
- [Issue #15](../issue-notes/15.md)と[Issue #14](../issue-notes/14.md)は、プロジェクト内で生成される全てのコンテンツの日付表示をUTCとJSTのデュアルタイムゾーン形式に統一するタスクです。
- これは、人間が読みやすいJSTと検索エンジンに最適化されたUTCの両方を併記し、情報の利便性とSEOの両立を目指しています。
- 新しい`DateFormatter`クラスの導入により、`YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)`形式への変換ロジックが検討されており、実装フェーズに移行しています。

## 次の一手候補
1. [Issue #15](../issue-notes/15.md) `DateFormatter`クラスの新規作成と単体テストの実装
   - 最初の小さな一歩: `src/generate_repo_list/date_formatter.py`に`DateFormatter`クラスの骨格を作成し、`format_dual_timezone`メソッドが指定された形式で日付を返すよう実装する。同時に、このメソッドの挙動を検証する`tests/test_date_formatter.py`を作成する。
   - Agent実行プロンプト:
     ```
     対象ファイル: src/generate_repo_list/date_formatter.py (新規作成), tests/test_date_formatter.py (新規作成)

     実行内容:
     1. `src/generate_repo_list/date_formatter.py`に`DateFormatter`クラスを定義し、`datetime`オブジェクトを引数にとり、`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`形式の文字列を返す`format_dual_timezone`メソッドを実装してください。この際、UTCとJST(UTC+9)への正確なタイムゾーン変換を含めてください。
     2. `tests/test_date_formatter.py`を新規作成し、`DateFormatter.format_dual_timezone`メソッドの機能を確認するユニットテストを記述してください。特に、異なる日付や時刻、タイムゾーンでの変換が正確に行われることを検証するテストケースを含めてください。

     確認事項:
     - Pythonの`datetime`モジュール、`pytz`ライブラリ（またはPython 3.9+の`zoneinfo`）を使用してタイムゾーン処理を適切に行うこと。
     - 日付が夏時間の影響を受けないことを確認し、一貫したタイムゾーン変換ロジックを適用すること。
     - テストは`pytest`フレームワークに準拠した形式で記述すること。

     期待する出力:
     - `src/generate_repo_list/date_formatter.py`のファイル内容。
     - `tests/test_date_formatter.py`のファイル内容。
     ```

2. [Issue #14](../issue-notes/14.md) Markdown生成処理における日付表示の`DateFormatter`への置き換え
   - 最初の小さな一歩: `src/generate_repo_list/markdown_generator.py`を分析し、現在日付を出力している箇所を特定する。`DateFormatter`クラスをインポートし、これらの日付文字列生成を`format_dual_timezone`メソッドの呼び出しに置き換える。
   - Agent実行プロンプト:
     ```
     対象ファイル: src/generate_repo_list/markdown_generator.py

     実行内容:
     1. `src/generate_repo_list/markdown_generator.py`内の全てのファイルについて、日付情報をMarkdown文字列として生成している箇所を特定してください。
     2. 特定された箇所で、`src/generate_repo_list/date_formatter.py`に実装された`DateFormatter`クラスをインポートし、その`format_dual_timezone`メソッドを使用して日付表示を`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`形式に変換するよう修正してください。
     3. 変換対象となる日付オブジェクトが`datetime`型であることを確認し、必要に応じて変換処理を追加してください。

     確認事項:
     - `DateFormatter`クラスが既に存在し、正しく動作することを前提とします。
     - `markdown_generator.py`が生成するMarkdownファイルのレイアウトや内容に予期せぬ変更がないことを確認してください。
     - 既存のテストスイート（例: `tests/test_markdown_generator.py`）に変更が影響を与えないか、または追加のテストが必要か検討してください。

     期待する出力:
     - 修正後の`src/generate_repo_list/markdown_generator.py`のファイル内容。
     - 変更を検証するための追加テストに関する推奨事項（もしあれば）。
     ```

3. [Issue #14](../issue-notes/14.md) JSON-LD及びSEOテンプレートにおける日付表示の統一調査と計画
   - 最初の小さな一歩: `src/generate_repo_list/json_ld_template.json`、`src/generate_repo_list/seo_template.yml`、および関連する処理ファイル（例: `template_processor.py`）を調査し、日付情報をどのように扱っているか、また`DateFormatter`を適用可能か判断する。
   - Agent実行プロンプト:
     ```
     対象ファイル: src/generate_repo_list/json_ld_template.json, src/generate_repo_list/seo_template.yml, src/generate_repo_list/template_processor.py, src/generate_repo_list/project_overview_fetcher.py

     実行内容:
     1. 上記対象ファイル群を分析し、日付情報（例えば、更新日、公開日など）を定義、取得、またはテンプレートに埋め込んでいる箇所を特定してください。
     2. 特定された箇所について、[Issue #14](../issue-notes/14.md)および[Issue #15](../issue-notes/15.md)の要件であるUTC/JSTデュアルタイムゾーン表示を適用する必要があるかを判断してください。
     3. 必要であると判断された場合、`DateFormatter`クラスの導入方法や、テンプレートの構造変更の有無を含めた具体的な修正計画をMarkdown形式で提案してください。

     確認事項:
     - JSON-LDやSEOテンプレートは機械可読性が重要であるため、日付フォーマットの変更がこれらのスキーマ定義と矛盾しないか慎重に確認すること。
     - テンプレートに日付が直接記述されている場合と、動的に埋め込まれる場合の両方を考慮すること。
     - 変更がサイトのSEOに悪影響を与えないよう、既存の仕様との整合性を重視すること。

     期待する出力:
     - 日付情報を取り扱っている箇所の一覧と、それらに対する`DateFormatter`適用要否の判断結果。
     - 適用が必要な場合の具体的な修正計画（ファイルパス、修正概要、考慮事項）を記述したMarkdownドキュメント。

---
Generated at: 2026-01-01 07:06:53 JST
