Last updated: 2025-12-21

# Development Status

## 現在のIssues
- [Issue #14](../issue-notes/14.md) は、生成されるすべてのドキュメントの日付表示をUTCとJSTの両方で併記し、運用者と検索エンジンの双方に配慮する要件です。
- [Issue #15](../issue-notes/15.md) も同様に、日付表示をUTC/JSTの二重タイムゾーン形式で追加することを求めています。
- これらのIssueは、プロジェクト全体の日付フォーマットを一貫して改善することを目指しており、特にMarkdown生成部分への影響が想定されます。

## 次の一手候補
1.  [Issue #14](../issue-notes/14.md): 日付表示のための共通ユーティリティ関数の実装
    -   最初の小さな一歩: `src/generate_repo_list/url_utils.py` または新規ファイルに、`datetime` オブジェクトを受け取りUTCとJSTの二重形式でフォーマットするPython関数を作成する。
    -   Agent実行プロンプト:
        ```
        対象ファイル: `src/generate_repo_list/url_utils.py`

        実行内容: `datetime` オブジェクト（タイムゾーン情報を持つ）を受け取り、"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)" の形式で日付文字列を返す `format_dual_timezone_date` 関数を `src/generate_repo_list/url_utils.py` に追加してください。JSTはUTC+9としてください。

        確認事項: Pythonの `datetime` モジュールと `zoneinfo` (または `pytz` がインストールされている場合) を使用し、既存のユーティリティ関数との整合性を保ちながら実装してください。`zoneinfo` が利用できない環境の場合は `datetime.timezone.utc` を用いたオフセット計算を検討してください。

        期待する出力: `format_dual_timezone_date` 関数が追加された `src/generate_repo_list/url_utils.py` の更新された内容をmarkdown形式で出力してください。
        ```

2.  [Issue #14](../issue-notes/14.md): 生成されるMarkdown/HTMLへの日付表示の適用
    -   最初の小さな一歩: `src/generate_repo_list/markdown_generator.py` 内で日付を扱う箇所を特定し、ステップ1で作成した共通関数を呼び出してUTC/JST併記形式に更新する。
    -   Agent実行プロンプト:
        ```
        対象ファイル: `src/generate_repo_list/markdown_generator.py`

        実行内容: `src/generate_repo_list/markdown_generator.py` 内の `_generate_repository_markdown` 関数やその他の日付をMarkdownまたはHTMLに埋め込む部分を分析し、ステップ1で実装した `format_dual_timezone_date` 関数（`src/generate_repo_list/url_utils.py` に追加されたもの）を使用して、日付表示をUTCとJSTで併記する形式に変更してください。

        確認事項: 変更が `index.md` やその他の生成されるドキュメントに正しく反映されることを確認し、既存のMarkdown生成ロジックを壊さないようにしてください。また、`src/generate_repo_list/url_utils.py` から `format_dual_timezone_date` 関数を適切にインポートしてください。

        期待する出力: 日付表示ロジックが更新された `src/generate_repo_list/markdown_generator.py` の更新された内容をmarkdown形式で出力してください。
        ```

3.  [Issue #14](../issue-notes/14.md): 日付表示機能のテストと検証
    -   最初の小さな一歩: `tests/test_markdown_generator.py` に、生成されたMarkdownの日付表示が期待通りのUTC/JST併記形式になっていることを確認するテストケースを追加する。
    -   Agent実行プロンプト:
        ```
        対象ファイル: `tests/test_markdown_generator.py`

        実行内容: `src/generate_repo_list/markdown_generator.py` の日付表示変更を検証するため、`tests/test_markdown_generator.py` に新しいテスト関数を追加してください。このテストは、モックデータを使用してリポジトリ情報を生成し、`markdown_generator.py` が出力するMarkdown内の日付文字列が「YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)」の形式で正しく含まれていることをアサートします。

        確認事項: 既存のテストスイートに影響を与えず、新しいテストが機能することを確認してください。Pythonの `unittest.mock` または `pytest` の `mocker` フィクスチャを利用して、必要に応じて日付関連の関数や外部依存を適切にモックしてください。

        期待する出力: 新しいテストケースが追加された `tests/test_markdown_generator.py` の更新された内容をmarkdown形式で出力してください。

---
Generated at: 2025-12-21 07:05:45 JST
