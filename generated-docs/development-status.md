Last updated: 2025-12-30

# Development Status

## 現在のIssues
- [Issue #15](../issue-notes/15.md) は、すべてのPJT日付表示をUTCとJST両方で表示するための `DateFormatter` クラス導入が計画されており、これは検索エンジン最適化と運用者利便性の向上を目的としています。
- [Issue #14](../issue-notes/14.md) は、[Issue #15](../issue-notes/15.md) と同様に、全日付表示をUTCとJSTで併記し、運用者向けJSTと検索エンジン向けUTCに対応する要望を提起しています。
- これら2つのIssueは密接に関連しており、プロジェクト全体で日付表示の一貫性を保ち、タイムゾーン情報を適切に処理することを目標としています。

## 次の一手候補
1. [Issue #15](../issue-notes/15.md): `DateFormatter` クラスのスケルトン実装
   - 最初の小さな一歩: `src/generate_repo_list/date_formatter.py` ファイルを新規作成し、`datetime` オブジェクトを受け取り、指定されたフォーマット（例: "YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"）でUTCとJST両方のタイムゾーンで日付文字列を返す `format_datetime` メソッドを持つ `DateFormatter` クラスのスケルトンを実装する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/date_formatter.py` (新規作成)

     実行内容: `DateFormatter` クラスを実装してください。このクラスは、`format_datetime(dt: datetime)` メソッドを持ち、`dt` をUTCおよびJST（UTC+9）のタイムゾーンで `"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"` 形式の文字列にフォーマットして返します。`dt` がタイムゾーン情報を持たない場合はUTCと仮定して処理します。必要なライブラリとして `pytz` または `zoneinfo` をインポートし、使用してください。

     確認事項: Pythonの `datetime` モジュールと `pytz` (または `zoneinfo`) を使用してタイムゾーン処理が適切に行われることを確認してください。また、既存のプロジェクトで同様の日付処理が行われていないか (`src/generate_repo_list/` ディレクトリ内) を軽く確認し、重複がないことを確認してください。

     期待する出力: `src/generate_repo_list/date_formatter.py` ファイルの新規作成と、上記仕様を満たすPythonコード。
     ```

2. [Issue #15](../issue-notes/15.md): `DateFormatter` クラスの単体テスト追加
   - 最初の小さな一歩: `tests/test_date_formatter.py` を新規作成し、`DateFormatter` クラスの `format_datetime` メソッドについて、タイムゾーン情報あり/なしの `datetime` オブジェクトが正確にUTCとJSTでフォーマットされることを検証するテストケースを追加する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `tests/test_date_formatter.py` (新規作成), `src/generate_repo_list/date_formatter.py`

     実行内容: `src/generate_repo_list/date_formatter.py` に実装された `DateFormatter` クラスの単体テストを `tests/test_date_formatter.py` として作成してください。`pytest` フレームワークを使用し、以下のテストケースを網羅してください:
     - タイムゾーン情報を持つ `datetime` オブジェクトが正しくフォーマットされるか。
     - タイムゾーン情報を持たない `datetime` オブジェクトがUTCと仮定されて正しくフォーマットされるか。
     - 異なる日付（例: 年末年始）でのフォーマットが正しいか。

     確認事項: `pytest` が正しく実行できる環境であることを確認してください。また、`src/generate_repo_list/date_formatter.py` が存在し、テスト対象のクラスとメソッドがアクセス可能であることを確認してください。テストはモジュール間の依存関係を最小限に抑え、純粋に `DateFormatter` の機能のみを検証するように設計してください。

     期待する出力: `tests/test_date_formatter.py` ファイルの新規作成と、`DateFormatter` の機能を検証するPythonテストコード。
     ```

3. [Issue #14](../issue-notes/14.md): 既存の日付表示箇所の特定と適用計画
   - 最初の小さな一歩: `src/generate_repo_list/` ディレクトリ内の全Pythonファイル(`*.py`)を対象に、日付や時刻に関連する文字列が出力されている箇所（例: `strftime` の使用、直接的な日付文字列結合など）を特定し、それらを `DateFormatter` クラスで置き換えるための影響範囲と具体的な修正箇所をまとめる。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/*.py` (全Pythonファイル)

     実行内容: `src/generate_repo_list/` ディレクトリ内のすべてのPythonファイルを分析し、日付や時刻を文字列として出力している箇所を特定してください。特に、`datetime` オブジェクトのフォーマット (`strftime` など) や、日付関連の情報を文字列として結合している箇所に注目してください。特定された箇所について、以下の情報をMarkdown形式でリストアップしてください:
     1. ファイルパスと行番号
     2. 現在のコードスニペット
     3. `DateFormatter` クラス (`src/generate_repo_list/date_formatter.py` に存在すると仮定) を使用して、UTC/JST併記形式に置き換えるための具体的な修正案（擬似コードでも可）

     確認事項: `datetime` オブジェクトがどのように取得され、どのコンテキストで利用されているかを理解し、`DateFormatter` を適用する際のデータ型の一貫性を確保してください。出力は `index.md` や `README.md` などの最終的な出力に影響を与える可能性のある箇所に焦点を当ててください。

     期待する出力: `current_date_usages.md` のようなMarkdownファイルとして、分析結果と修正案を生成してください。

---
Generated at: 2025-12-30 07:06:12 JST
