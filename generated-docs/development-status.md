Last updated: 2025-11-28

# Development Status

## 現在のIssues
- [Issue #14](../issue-notes/14.md)と[Issue #15](../issue-notes/15.md)は、プロジェクト内のすべての日付表示をUTCとJSTで併記する機能の実装を目指しています。
- これは主に運用者向け（JST）と検索エンジン最適化（UTC）を目的としており、`DateFormatter`クラスの導入が計画されています。
- 最終目標は、日付が「YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)」形式で出力されるようにすることです。

## 次の一手候補
1. [Issue #15](../issue-notes/15.md): `DateFormatter`クラスの新規作成と単体テストの実装
   - 最初の小さな一歩: `src/generate_repo_list/date_formatter.py`ファイルを新規作成し、`DateFormatter`クラスのスケルトンと、指定されたフォーマット（"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"）で日付をフォーマットするメソッドを実装する。合わせて、簡単な単体テストも作成する。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/date_formatter.py` (新規作成), `tests/test_date_formatter.py` (新規作成)

     実行内容:
     1. `src/generate_repo_list/date_formatter.py`を新規作成し、`DateFormatter`クラスを実装してください。
     2. `DateFormatter`クラスは、`format_datetime_dual_timezone(dt: datetime) -> str`というメソッドを持つこと。
     3. このメソッドは、入力されたtimezone-awareな`datetime`オブジェクトを、`"YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)"`の形式の文字列に変換すること。JSTはUTC+9です。
     4. `tests/test_date_formatter.py`を新規作成し、`DateFormatter`クラスの単体テストを実装してください。具体的には、UTC時刻とJST時刻の`datetime`オブジェクトを与えた場合に、期待通りのフォーマット文字列が返されることを確認するテストケースを含めてください。

     確認事項:
     - `datetime`オブジェクトのタイムゾーン処理が正しく行われているかを確認してください。`pytz`や`zoneinfo`ライブラリの使用を検討してください（プロジェクトの既存ライブラリを優先）。
     - Pythonの標準ライブラリ（`datetime`, `zoneinfo`など）で実現可能か確認し、不必要に外部ライブラリを導入しないようにしてください。

     期待する出力:
     - `src/generate_repo_list/date_formatter.py`のファイル内容。
     - `tests/test_date_formatter.py`のファイル内容。
     ```

2. [Issue #15](../issue-notes/15.md): 生成されたリポジトリリスト内の日付表示箇所を特定しリストアップする
   - 最初の小さな一歩: `src/generate_repo_list`ディレクトリ内のPythonファイル（特に`markdown_generator.py`, `repository_processor.py`, `generate_repo_list.py`）を分析し、リポジトリの最終更新日時やコミット日時など、ユーザーに表示される可能性のある日付情報が現在どのように扱われているかを特定し、リストアップする。
   - Agent実行プロンプト:
     ```
     対象ファイル: `src/generate_repo_list/markdown_generator.py`, `src/generate_repo_list/repository_processor.py`, `src/generate_repo_list/generate_repo_list.py`

     実行内容:
     対象ファイル群を分析し、以下の観点からMarkdown形式で出力してください：
     1. 現在、最終的なMarkdown出力に含まれる日付情報（例: リポジトリの最終更新日時、コミット日時など）がどのファイルで、どの変数名で、どのようなフォーマットで扱われているかを特定する。
     2. 特定された日付情報が、`src/generate_repo_list/markdown_generator.py`で最終的にMarkdown文字列に変換される際、どのように出力されているかを確認する。
     3. 今後`DateFormatter`を適用すべき箇所を具体的にリストアップする。

     確認事項:
     - `datetime`オブジェクトがどのように生成され、どこで文字列に変換されているかに特に注意してください。
     - 依存関係として、`src/generate_repo_list/project_overview_fetcher.py`が日付情報を取得している可能性も考慮に入れてください。

     期待する出力:
     Markdown形式で、特定された日付情報のソース、現在の処理フロー、および`DateFormatter`適用候補箇所の詳細なリスト。
     ```

3. [Issue #14](../issue-notes/14.md): 既存のREADME.mdやindex.mdの日付表示を特定・確認
   - 最初の小さな一歩: プロジェクトルートの`index.md`および`README.md`を調査し、もし日付が表示されている箇所があれば、その表示形式とソースを特定する。特にJekyllのフロントマターやLiquidテンプレートで日付が使われている可能性を考慮に入れる。
   - Agent実行プロンプト:
     ```
     対象ファイル: `index.md`, `README.md`

     実行内容:
     対象ファイルを分析し、以下の観点からMarkdown形式で出力してください：
     1. `index.md`と`README.md`内に日付が表示されている箇所があるかを特定してください。
     2. もし日付表示があれば、それがどのような形式で、どこから来ている（例: フロントマター、Liquid変数、静的テキストなど）かを分析してください。
     3. これらの日付表示が、今後のUTC/JSTデュアル表示要件にどのように影響するか、あるいは既存の`DateFormatter`を適用できるかを検討し、提案を記述してください。

     確認事項:
     - Jekyllのサイト生成プロセスにおいて、日付がどのように扱われるか（例: `page.date`, `site.time`など）を考慮に入れてください。
     - 開発状況生成プロンプトの「生成しないもの」に「プロジェクト構造情報（来訪者向け情報のため、別ファイルで管理）」とあるため、その観点から分析結果を適切にまとめてください。

     期待する出力:
     Markdown形式で、`index.md`および`README.md`における日付表示の分析結果、および今後の対応に関する提案。

---
Generated at: 2025-11-28 07:06:00 JST
