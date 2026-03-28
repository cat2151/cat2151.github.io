Last updated: 2026-03-29

# 開発状況生成プロンプト（開発者向け）

## 生成するもの：
- 現在openされているissuesを3行で要約する
- 次の一手の候補を3つlistする
- 次の一手の候補3つそれぞれについて、極力小さく分解して、その最初の小さな一歩を書く

## 生成しないもの：
- 「今日のissue目標」などuserに提案するもの
  - ハルシネーションの温床なので生成しない
- ハルシネーションしそうなものは生成しない（例、無価値なtaskや新issueを勝手に妄想してそれをuserに提案する等）
- プロジェクト構造情報（来訪者向け情報のため、別ファイルで管理）

## 「Agent実行プロンプト」生成ガイドライン：
「Agent実行プロンプト」作成時は以下の要素を必ず含めてください：

### 必須要素
1. **対象ファイル**: 分析/編集する具体的なファイルパス
2. **実行内容**: 具体的な分析や変更内容（「分析してください」ではなく「XXXファイルのYYY機能を分析し、ZZZの観点でmarkdown形式で出力してください」）
3. **確認事項**: 変更前に確認すべき依存関係や制約
4. **期待する出力**: markdown形式での結果や、具体的なファイル変更

### Agent実行プロンプト例

**良い例（上記「必須要素」4項目を含む具体的なプロンプト形式）**:
```
対象ファイル: `.github/workflows/translate-readme.yml`と`.github/workflows/call-translate-readme.yml`

実行内容: 対象ファイルについて、外部プロジェクトから利用する際に必要な設定項目を洗い出し、以下の観点から分析してください：
1) 必須入力パラメータ（target-branch等）
2) 必須シークレット（GEMINI_API_KEY）
3) ファイル配置の前提条件（README.ja.mdの存在）
4) 外部プロジェクトでの利用時に必要な追加設定

確認事項: 作業前に既存のworkflowファイルとの依存関係、および他のREADME関連ファイルとの整合性を確認してください。

期待する出力: 外部プロジェクトがこの`call-translate-readme.yml`を導入する際の手順書をmarkdown形式で生成してください。具体的には：必須パラメータの設定方法、シークレットの登録手順、前提条件の確認項目を含めてください。
```

**避けるべき例**:
- callgraphについて調べてください
- ワークフローを分析してください
- issue-noteの処理フローを確認してください

## 出力フォーマット：
以下のMarkdown形式で出力してください：

```markdown
# Development Status

## 現在のIssues
[以下の形式で3行でオープン中のissuesを要約。issue番号を必ず書く]
- [1行目の説明]
- [2行目の説明]
- [3行目の説明]

## 次の一手候補
1. [候補1のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

2. [候補2のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```

3. [候補3のタイトル。issue番号を必ず書く]
   - 最初の小さな一歩: [具体的で実行可能な最初のアクション]
   - Agent実行プロンプト:
     ```
     対象ファイル: [分析/編集する具体的なファイルパス]

     実行内容: [具体的な分析や変更内容を記述]

     確認事項: [変更前に確認すべき依存関係や制約]

     期待する出力: [markdown形式での結果や、具体的なファイル変更の説明]
     ```
```


# 開発状況情報
- 以下の開発状況情報を参考にしてください。
- Issue番号を記載する際は、必ず [Issue #番号](../issue-notes/番号.md) の形式でMarkdownリンクとして記載してください。

## プロジェクトのファイル一覧
- .editorconfig
- .github/actions-tmp/.github/workflows/call-callgraph.yml
- .github/actions-tmp/.github/workflows/call-check-large-files.yml
- .github/actions-tmp/.github/workflows/call-daily-project-summary.yml
- .github/actions-tmp/.github/workflows/call-issue-note.yml
- .github/actions-tmp/.github/workflows/call-rust-fmt-commit.yml
- .github/actions-tmp/.github/workflows/call-rust-windows-cargo-check.yml
- .github/actions-tmp/.github/workflows/call-rust-windows-check.yml
- .github/actions-tmp/.github/workflows/call-translate-readme.yml
- .github/actions-tmp/.github/workflows/callgraph.yml
- .github/actions-tmp/.github/workflows/check-large-files.yml
- .github/actions-tmp/.github/workflows/check-recent-human-commit.yml
- .github/actions-tmp/.github/workflows/daily-project-summary.yml
- .github/actions-tmp/.github/workflows/issue-note.yml
- .github/actions-tmp/.github/workflows/rust-fmt-commit.yml
- .github/actions-tmp/.github/workflows/rust-windows-cargo-check.yml
- .github/actions-tmp/.github/workflows/rust-windows-check.yml
- .github/actions-tmp/.github/workflows/translate-readme.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/callgraph.ql
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/codeql-pack.lock.yml
- .github/actions-tmp/.github_automation/callgraph/codeql-queries/qlpack.yml
- .github/actions-tmp/.github_automation/callgraph/config/example.json
- .github/actions-tmp/.github_automation/callgraph/docs/callgraph.md
- .github/actions-tmp/.github_automation/callgraph/presets/callgraph.js
- .github/actions-tmp/.github_automation/callgraph/presets/style.css
- .github/actions-tmp/.github_automation/callgraph/scripts/analyze-codeql.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/callgraph-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-codeql-exists.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/check-node-version.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/common-utils.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/copy-commit-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/extract-sarif-info.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/find-process-results.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generate-html-graph.cjs
- .github/actions-tmp/.github_automation/callgraph/scripts/generateHTML.cjs
- .github/actions-tmp/.github_automation/check-large-files/README.md
- .github/actions-tmp/.github_automation/check-large-files/check-large-files.toml.default
- .github/actions-tmp/.github_automation/check-large-files/scripts/check_large_files.py
- .github/actions-tmp/.github_automation/check_recent_human_commit/scripts/check-recent-human-commit.cjs
- .github/actions-tmp/.github_automation/project_summary/docs/daily-summary-setup.md
- .github/actions-tmp/.github_automation/project_summary/prompts/development-status-prompt.md
- .github/actions-tmp/.github_automation/project_summary/prompts/project-overview-prompt.md
- .github/actions-tmp/.github_automation/project_summary/scripts/ProjectSummaryCoordinator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/DevelopmentStatusGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/GitUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/development/IssueTracker.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/generate-project-summary.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/CodeAnalyzer.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectAnalysisOrchestrator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataCollector.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectDataFormatter.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/overview/ProjectOverviewGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/BaseGenerator.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/FileSystemUtils.cjs
- .github/actions-tmp/.github_automation/project_summary/scripts/shared/ProjectFileUtils.cjs
- .github/actions-tmp/.github_automation/translate/docs/TRANSLATION_SETUP.md
- .github/actions-tmp/.github_automation/translate/scripts/translate-readme.cjs
- .github/actions-tmp/.gitignore
- .github/actions-tmp/.vscode/settings.json
- .github/actions-tmp/AGENTS.md
- .github/actions-tmp/LICENSE
- .github/actions-tmp/README.ja.md
- .github/actions-tmp/README.md
- .github/actions-tmp/_config.yml
- .github/actions-tmp/generated-docs/callgraph.html
- .github/actions-tmp/generated-docs/callgraph.js
- .github/actions-tmp/generated-docs/development-status-generated-prompt.md
- .github/actions-tmp/generated-docs/development-status.md
- .github/actions-tmp/generated-docs/project-overview-generated-prompt.md
- .github/actions-tmp/generated-docs/project-overview.md
- .github/actions-tmp/generated-docs/style.css
- .github/actions-tmp/googled947dc864c270e07.html
- .github/actions-tmp/issue-notes/10.md
- .github/actions-tmp/issue-notes/11.md
- .github/actions-tmp/issue-notes/12.md
- .github/actions-tmp/issue-notes/13.md
- .github/actions-tmp/issue-notes/14.md
- .github/actions-tmp/issue-notes/15.md
- .github/actions-tmp/issue-notes/16.md
- .github/actions-tmp/issue-notes/17.md
- .github/actions-tmp/issue-notes/18.md
- .github/actions-tmp/issue-notes/19.md
- .github/actions-tmp/issue-notes/2.md
- .github/actions-tmp/issue-notes/20.md
- .github/actions-tmp/issue-notes/21.md
- .github/actions-tmp/issue-notes/22.md
- .github/actions-tmp/issue-notes/23.md
- .github/actions-tmp/issue-notes/24.md
- .github/actions-tmp/issue-notes/25.md
- .github/actions-tmp/issue-notes/26.md
- .github/actions-tmp/issue-notes/27.md
- .github/actions-tmp/issue-notes/28.md
- .github/actions-tmp/issue-notes/29.md
- .github/actions-tmp/issue-notes/3.md
- .github/actions-tmp/issue-notes/30.md
- .github/actions-tmp/issue-notes/35.md
- .github/actions-tmp/issue-notes/38.md
- .github/actions-tmp/issue-notes/4.md
- .github/actions-tmp/issue-notes/40.md
- .github/actions-tmp/issue-notes/44.md
- .github/actions-tmp/issue-notes/57.md
- .github/actions-tmp/issue-notes/67.md
- .github/actions-tmp/issue-notes/7.md
- .github/actions-tmp/issue-notes/8.md
- .github/actions-tmp/issue-notes/9.md
- .github/actions-tmp/package-lock.json
- .github/actions-tmp/package.json
- .github/actions-tmp/src/main.js
- .github/copilot-instructions.md
- .github/workflows/call-check-large-files.yml
- .github/workflows/call-daily-project-summary.yml
- .github/workflows/call-issue-note.yml
- .github/workflows/call-translate-readme.yml
- .github/workflows/generate_repo_list.yml
- .github_automation/check_large_files/README.md
- .github_automation/check_large_files/check-large-files.toml
- .github_automation/check_large_files/scripts/check_large_files.py
- .gitignore
- LICENSE
- README.md
- _config.yml
- assets/favicon-16x16.png
- assets/favicon-192x192.png
- assets/favicon-32x32.png
- assets/favicon-512x512.png
- debug_project_overview.py
- generated-docs/project-overview-generated-prompt.md
- googled947dc864c270e07.html
- index.md
- issue-notes/22.md
- manifest.json
- pytest.ini
- requirements-dev.txt
- requirements.txt
- robots.txt
- ruff.toml
- src/__init__.py
- src/generate_repo_list/__init__.py
- src/generate_repo_list/badge_generator.py
- src/generate_repo_list/config.yml
- src/generate_repo_list/config_manager.py
- src/generate_repo_list/date_formatter.py
- src/generate_repo_list/generate_repo_list.py
- src/generate_repo_list/json_ld_template.json
- src/generate_repo_list/language_info.py
- src/generate_repo_list/markdown_generator.py
- src/generate_repo_list/project_overview_fetcher.py
- src/generate_repo_list/readme_badge_extractor.py
- src/generate_repo_list/repository_processor.py
- src/generate_repo_list/seo_template.yml
- src/generate_repo_list/statistics_calculator.py
- src/generate_repo_list/strings.yml
- src/generate_repo_list/template_processor.py
- src/generate_repo_list/url_utils.py
- test_project_overview.py
- tests/test_badge_generator_integration.py
- tests/test_check_large_files.py
- tests/test_config.py
- tests/test_date_formatter.py
- tests/test_environment.py
- tests/test_integration.py
- tests/test_markdown_generator.py
- tests/test_project_overview_fetcher.py
- tests/test_readme_badge_extractor.py
- tests/test_repository_processor.py

## 現在のオープンIssues
## [Issue #24](../issue-notes/24.md): 大きなファイルの検出: 1個のファイルが500行を超えています
以下のファイルが500行を超えています。リファクタリングを検討してください。

## 検出されたファイル

| ファイル | 行数 | 超過行数 |
|---------|------|----------|
| `tests/test_markdown_generator.py` | 595 | +95 |

## テスト実施のお願い

- リファクタリング前後にテストを実行し、それぞれのテスト失敗件数を報告してください
- リファクタリング前後のどちらかでテストがredの場合、まず別issueでtest greenにしてからリファクタリングしてください

## 推奨事項

1. 単一責任の...
ラベル: refactoring, code-quality, automated
--- issue-notes/24.md の内容 ---

```markdown

```

## ドキュメントで言及されているファイルの内容
### .github/actions-tmp/issue-notes/24.md
```md
{% raw %}
# issue Geminiが503で落ちたのでretryを実装する #24
[issues #24](https://github.com/cat2151/github-actions/issues/24)

# 何が困るの？
- 朝起きて、development statusがgenerateされてないのは困る
    - それをタスク実施のヒントにしているので
    - 毎朝generatedな状態を維持したい

# 方法
- retryを実装する
    - 現在は `this.model.generateContent(developmentPrompt);`
    - 実装後は `this.generateContent(developmentPrompt);`
    - BaseGenerator 側に、
        - generateContent関数を実装する
            - そこで、
                - `this.model.generateContent(developmentPrompt);` する
                - 503のとき、
                    - retryあり
                    - Exponential Backoff

# 結果
- 直近の実行結果をlog確認した
    - 本番で503が発生しなかったことをlog確認した
- 本番の503 testは、今回発生しなかったので、できず
- ここ1週間で2回発生しているので、次の1週間で1回発生する想定
- ソース机上確認した

# どうする？
- このissueはcloseしたほうがわかりやすい、と判断する
- 1週間503を毎日チェック、は省略とする
- もし今後503が発生したら別issueとする
- 2日チェックして503なし

# closeとする

{% endraw %}
```

### .github/actions-tmp/issue-notes/4.md
```md
{% raw %}
# issue GitHub Actions「project概要生成」を共通ワークフロー化する #4
[issues #4](https://github.com/cat2151/github-actions/issues/4)

# prompt
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
このymlファイルを、以下の2つのファイルに分割してください。
1. 共通ワークフロー       cat2151/github-actions/.github/workflows/daily-project-summary.yml
2. 呼び出し元ワークフロー cat2151/github-actions/.github/workflows/call-daily-project-summary.yml
まずplanしてください
```

# 結果、あちこちハルシネーションのあるymlが生成された
- agentの挙動があからさまにハルシネーション
    - インデントが修正できない、「失敗した」という
    - 構文誤りを認識できない
- 人力で修正した

# このagentによるセルフレビューが信頼できないため、別のLLMによるセカンドオピニオンを試す
```
あなたはGitHub Actionsと共通ワークフローのスペシャリストです。
以下の2つのファイルをレビューしてください。最優先で、エラーが発生するかどうかだけレビューてください。エラー以外の改善事項のチェックをするかわりに、エラー発生有無チェックに最大限注力してください。

--- 呼び出し元

name: Call Daily Project Summary

on:
  schedule:
    # 日本時間 07:00 (UTC 22:00 前日)
    - cron: '0 22 * * *'
  workflow_dispatch:

jobs:
  call-daily-project-summary:
    uses: cat2151/github-actions/.github/workflows/daily-project-summary.yml
    secrets:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}

--- 共通ワークフロー
name: Daily Project Summary
on:
  workflow_call:

jobs:
  generate-summary:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      issues: read
      pull-requests: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0  # 履歴を取得するため

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: |
          # 一時的なディレクトリで依存関係をインストール
          mkdir -p /tmp/summary-deps
          cd /tmp/summary-deps
          npm init -y
          npm install @google/generative-ai @octokit/rest
          # generated-docsディレクトリを作成
          mkdir -p $GITHUB_WORKSPACE/generated-docs

      - name: Generate project summary
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          NODE_PATH: /tmp/summary-deps/node_modules
        run: |
          node .github/scripts/generate-project-summary.cjs

      - name: Check for generated summaries
        id: check_summaries
        run: |
          if [ -f "generated-docs/project-overview.md" ] && [ -f "generated-docs/development-status.md" ]; then
            echo "summaries_generated=true" >> $GITHUB_OUTPUT
          else
            echo "summaries_generated=false" >> $GITHUB_OUTPUT
          fi

      - name: Commit and push summaries
        if: steps.check_summaries.outputs.summaries_generated == 'true'
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          # package.jsonの変更のみリセット（generated-docsは保持）
          git restore package.json 2>/dev/null || true
          # サマリーファイルのみを追加
          git add generated-docs/project-overview.md
          git add generated-docs/development-status.md
          git commit -m "Update project summaries (overview & development status)"
          git push

      - name: Summary generation result
        run: |
          if [ "${{ steps.check_summaries.outputs.summaries_generated }}" == "true" ]; then
            echo "✅ Project summaries updated successfully"
            echo "📊 Generated: project-overview.md & development-status.md"
          else
            echo "ℹ️ No summaries generated (likely no user commits in the last 24 hours)"
          fi
```

# 上記promptで、2つのLLMにレビューさせ、合格した

# 細部を、先行する2つのymlを参照に手直しした

# ローカルtestをしてからcommitできるとよい。方法を検討する
- ローカルtestのメリット
    - 素早く修正のサイクルをまわせる
    - ムダにgit historyを汚さない
        - これまでの事例：「実装したつもり」「エラー。修正したつもり」「エラー。修正したつもり」...（以降エラー多数）
- 方法
    - ※検討、WSL + act を環境構築済みである。test可能であると判断する
    - 呼び出し元のURLをコメントアウトし、相対パス記述にする
    - ※備考、テスト成功すると結果がcommit pushされる。それでよしとする
- 結果
    - OK
    - secretsを簡略化できるか試した、できなかった、現状のsecrets記述が今わかっている範囲でベストと判断する
    - OK

# test green

# commit用に、yml 呼び出し元 uses をlocal用から本番用に書き換える

# closeとする

{% endraw %}
```

### src/generate_repo_list/markdown_generator.py
```py
{% raw %}
"""Markdown生成モジュール (リファクタリング版)

このモジュールはMarkdownコンテンツの生成を担当します。
"""

from typing import Any, Dict, List

try:
    # 通常のパッケージインポート（本番環境用）
    from .badge_generator import BadgeGenerator
    from .date_formatter import DateFormatter
    from .statistics_calculator import StatisticsCalculator
    from .template_processor import TemplateProcessor
    from .url_utils import URLUtils
except ImportError:
    # 絶対インポート（テスト環境用）
    from badge_generator import BadgeGenerator
    from date_formatter import DateFormatter
    from statistics_calculator import StatisticsCalculator
    from template_processor import TemplateProcessor
    from url_utils import URLUtils


class MarkdownGenerator:
    """Markdown生成クラス（リファクタリング版）"""

    def __init__(self, config: Dict[str, Any], strings: Dict[str, Any], jekyll_config: Dict[str, Any] = None):
        """初期化

        Args:
            config: 設定辞書
            strings: 文字列リソース辞書
            jekyll_config: Jekyll設定辞書（オプション）
        """
        self.config = config
        self.strings = strings
        self.jekyll_config = jekyll_config or {}

        # ユーティリティクラスを初期化
        self.url_utils = URLUtils(jekyll_config)
        self.badge_generator = BadgeGenerator(config, strings, self.url_utils)
        self.stats_calculator = StatisticsCalculator(config)
        self.template_processor = TemplateProcessor()
        self.date_formatter = DateFormatter(config)

    def generate_markdown(
        self,
        username: str,
        active: List[Dict],
        archived: List[Dict],
        forks: List[Dict],
        seo_config: Dict,
        json_ld_template: Dict,
    ) -> str:
        """完全なMarkdownドキュメントを生成する

        Args:
            username: GitHubユーザー名
            active: アクティブなリポジトリ
            archived: アーカイブされたリポジトリ
            forks: フォークされたリポジトリ
            seo_config: SEO設定
            json_ld_template: JSON-LDテンプレート

        Returns:
            生成されたMarkdown文字列
        """
        print(f"\n{self.strings['console']['generating_markdown']}")

        today = self.date_formatter.format_current_date_dual_timezone()

        # 統計情報を計算
        stats = self.stats_calculator.calculate_basic_stats(active, archived, forks)
        lang_list = self.stats_calculator.get_top_languages_text(active + archived + forks)

        # 動的なOGP説明文を生成
        og_description = self.strings["seo"]["og_description_template"].format(
            total=stats["total"], total_stars=stats["total_stars"], lang_list=lang_list
        )

        # 各セクションを生成
        frontmatter = self.template_processor.generate_frontmatter(
            username, og_description, seo_config, json_ld_template, stats["total"]
        )
        stats_section = self._generate_statistics_section(active, archived, forks)
        toc = self._generate_toc()

        # メインコンテンツ生成
        main_title = self.strings["markdown"]["main_title"].format(username=username)
        last_updated = self.strings["markdown"]["last_updated"].format(date=today)

        active_section = self._generate_section(active, username=username)
        archived_section = self._generate_section(archived, "archived", username=username)
        forks_section = self._generate_fork_section(forks, username=username)

        return f"""{frontmatter}

# {main_title}

{last_updated}

{toc}

{stats_section}

---

## {self.strings["markdown"]["sections"]["active"]}

{self.strings["markdown"]["section_messages"]["ai_disclaimer"]}

{active_section}

---

## {self.strings["markdown"]["sections"]["archived"]}

{archived_section}

---

## {self.strings["markdown"]["sections"]["forks"]}

{self.strings["markdown"]["repo_details"]["fork_description"]}

{forks_section}
"""

    def _generate_toc(self) -> str:
        """目次を生成する"""
        toc_items = "\n".join(f"- {item}" for item in self.strings["markdown"]["toc_items"])
        return f"""## {self.strings["markdown"]["sections"]["toc"]}

{toc_items}

"""

    def _generate_statistics_section(self, active: List[Dict], archived: List[Dict], forks: List[Dict]) -> str:
        """統計情報セクションを生成する"""
        all_repos = active + archived + forks

        # 統計バッジを生成
        stat_badges = self.badge_generator.generate_statistics_badges(active, archived, forks)

        # 言語バッジを生成
        language_badges = self.badge_generator.generate_language_badges(all_repos)

        return f"""## {self.strings["markdown"]["sections"]["stats"]}

{stat_badges}

### {self.strings["markdown"]["stats"]["main_languages_title"]}

{language_badges}
"""

    def _generate_section(self, repos: List[Dict], section_type: str = "default", username: str = None) -> str:
        """リポジトリセクションを生成する"""
        if not repos:
            if section_type == "archived":
                return self.strings["markdown"]["section_messages"]["archived_empty"]
            return ""

        return "\n".join(self._generate_repo_item(repo, username=username) for repo in repos)

    def _generate_fork_section(self, repos: List[Dict], username: str = None) -> str:
        """フォークセクションを生成する"""
        return "\n".join(self._generate_repo_item(repo, is_fork=True, username=username) for repo in repos)

    def _generate_repo_item(self, repo: Dict, is_fork: bool = False, username: str = None) -> str:
        """個別リポジトリ項目を生成する"""
        main_url = repo["pages_url"] if repo["has_pages"] else repo["url"]
        updated_date = self.date_formatter.format_dual_timezone(repo["updated_at"])

        # 情報行を組み立て
        info_parts = [f"📅 {updated_date}"]
        info_line = " | ".join(info_parts)

        # バッジを生成
        badge_line = self.badge_generator.generate_repository_badges(repo, is_fork, username)

        # 結果を組み立て
        lines = [f"## [{repo['name']}]({main_url})"]

        # 概要情報の有無を判定
        no_description_text = self.strings["markdown"]["processing"]["no_description"]
        has_real_description = repo["description"] and repo["description"] != no_description_text

        # Overviewをリポジトリ名の次の行に表示（ラベルなし）
        # ただし、概要情報が取得できなかった場合は後で箇条書きに表示
        if has_real_description:
            lines.append(repo["description"])

        lines.append("")

        # バッジを表示
        if badge_line:
            lines.extend([badge_line, ""])

        # GitHub URL を明示的なリンクとして生成
        github_url = self.url_utils.get_github_repo_url(repo["name"], username)
        github_link = f"[{github_url}]({github_url})"

        # Pages URL も明示的なリンクとして生成（利用可能な場合）
        if repo["has_pages"]:
            pages_link = f"[{repo['pages_url']}]({repo['pages_url']})"
        else:
            pages_link = self.strings["markdown"]["processing"]["no_pages"]

        lines.extend(
            [
                f"- **{self.strings['markdown']['repo_details']['github_label']}**: {github_link}",
                f"- **{self.strings['markdown']['repo_details']['pages_label']}**: {pages_link}",
            ]
        )

        # 概要情報が取得できなかった場合は箇条書きに表示
        if not has_real_description:
            lines.append(
                f"- **{self.strings['markdown']['repo_details']['description_label']}**: {repo['description']}"
            )

        # プロジェクト概要セクションを追加（存在する場合）
        if "project_overview" in repo and repo["project_overview"]:
            lines.extend(
                [
                    "",
                    f"### {self.strings['markdown']['repo_details']['project_highlights']}",
                ]
            )
            for highlight in repo["project_overview"]:
                lines.append(highlight)

        lines.extend([f"- {info_line}", ""])

        return "\n".join(lines)

{% endraw %}
```

### tests/test_markdown_generator.py
```py
{% raw %}
#!/usr/bin/env python3
"""MarkdownGeneratorのユニットテスト

このモジュールはMarkdownGeneratorクラスの各機能をpytestでテストします。
"""

import os
import sys
from datetime import datetime
from unittest.mock import patch

import pytest

# プロジェクトルートのsrcディレクトリをパスに追加
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = os.path.join(project_root, "src", "generate_repo_list")
sys.path.insert(0, src_dir)

from markdown_generator import MarkdownGenerator  # noqa: E402


class TestMarkdownGenerator:
    """MarkdownGeneratorのテストクラス"""

    @pytest.fixture
    def mock_config(self):
        """設定のフィクスチャ"""
        return {
            "date_format": "%Y年%m月%d日",
            "statistics": {
                "top_languages_count": 3,
            },
            "language_badge": {
                "replacements": {" ": "_", "-": "--"},
                "colors": {
                    "JavaScript": "f7df1e",
                    "Python": "3776ab",
                    "Rust": "000000",
                    "HTML": "e34f26",
                    "default": "blue",
                },
            },
            "topic_badge": {"replacements": {" ": "_", "-": "--"}},
        }

    @pytest.fixture
    def mock_strings(self):
        """文字列リソースのフィクスチャ"""
        return {
            "console": {"generating_markdown": "Markdown生成中..."},
            "markdown": {
                "main_title": "{username}のGitHubリポジトリ一覧",
                "last_updated": "最終更新: {date}",
                "sections": {
                    "toc": "目次",
                    "stats": "統計情報",
                    "active": "アクティブなリポジトリ",
                    "archived": "アーカイブされたリポジトリ",
                    "forks": "フォークしたリポジトリ",
                },
                "toc_items": ["[統計情報](#統計情報)", "[アクティブなリポジトリ](#アクティブなリポジトリ)"],
                "stats": {
                    "main_languages_title": "主要言語",
                    "no_language_info": "言語情報なし",
                    "badges": {
                        "repositories": "リポジトリ",
                        "active": "アクティブ",
                        "archived": "アーカイブ",
                        "forks": "フォーク",
                        "stars": "スター",
                    },
                },
                "repo_details": {
                    "fork_description": "以下は他のリポジトリをフォークしたものです。",
                    "github_label": "GitHub",
                    "pages_label": "GitHub Pages",
                    "description_label": "説明",
                    "project_highlights": "Project Highlights",
                },
                "section_messages": {
                    "archived_empty": "アーカイブされたリポジトリはありません。",
                    "ai_disclaimer": "*注意: 一部のプロジェクトには「Project Highlights」セクションが含まれていますが、これらはAIが自動生成した内容であり、不正確な場合があります。*",
                },
                "processing": {
                    "no_pages": "Pages無し",
                    "no_description": "No description available",
                },
            },
            "seo": {
                "og_description_template": "総計{total}個のリポジトリ、{total_stars}スター、主要言語: {lang_list}",
            },
        }

    @pytest.fixture
    def generator(self, mock_config, mock_strings):
        """MarkdownGeneratorのフィクスチャ"""
        return MarkdownGenerator(mock_config, mock_strings)

    @pytest.fixture
    def sample_repos(self):
        """サンプルリポジトリデータのフィクスチャ"""
        return {
            "active": [
                {
                    "name": "active-repo",
                    "url": "https://github.com/test/active-repo",
                    "pages_url": "https://test.github.io/active-repo/",
                    "description": "アクティブなリポジトリ",
                    "archived": False,
                    "has_pages": True,
                    "fork": False,
                    "updated_at": datetime(2024, 1, 1),
                    "stargazers_count": 10,
                    "language": "Python",
                    "topics": ["test", "python"],
                }
            ],
            "archived": [
                {
                    "name": "archived-repo",
                    "url": "https://github.com/test/archived-repo",
                    "pages_url": "https://test.github.io/archived-repo/",
                    "description": "アーカイブされたリポジトリ",
                    "archived": True,
                    "has_pages": False,
                    "fork": False,
                    "updated_at": datetime(2023, 12, 1),
                    "stargazers_count": 5,
                    "language": "JavaScript",
                    "topics": ["archived"],
                }
            ],
            "forks": [
                {
                    "name": "forked-repo",
                    "url": "https://github.com/test/forked-repo",
                    "pages_url": "https://test.github.io/forked-repo/",
                    "description": "フォークされたリポジトリ",
                    "archived": False,
                    "has_pages": False,
                    "fork": True,
                    "updated_at": datetime(2023, 11, 1),
                    "stargazers_count": 0,
                    "language": "Go",
                    "topics": [],
                }
            ],
        }

    @pytest.fixture
    def mock_seo_config(self):
        """SEO設定のフィクスチャ"""
        return {
            "title": "Test Title - {username}",
            "description": "{og_description}",
            "keywords": ["github", "repositories"],
        }

    @pytest.fixture
    def mock_json_ld_template(self):
        """JSON-LDテンプレートのフィクスチャ"""
        return {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "{username}",
            "description": "{og_description}",
        }

    def test_init(self, mock_config, mock_strings):
        """初期化テスト"""
        generator = MarkdownGenerator(mock_config, mock_strings)
        assert generator.config == mock_config
        assert generator.strings == mock_strings

    def test_init_with_jekyll_config(self, mock_config, mock_strings):
        """Jekyll設定ありの初期化テスト"""
        jekyll_config = {
            "github": {
                "username": "test_user",
                "repository_url_base": "https://github.com/test_user",
            }
        }
        generator = MarkdownGenerator(mock_config, mock_strings, jekyll_config)
        assert generator.config == mock_config
        assert generator.strings == mock_strings
        assert generator.jekyll_config == jekyll_config

    def test_init_without_jekyll_config(self, mock_config, mock_strings):
        """Jekyll設定なしの初期化テスト"""
        generator = MarkdownGenerator(mock_config, mock_strings)
        assert generator.jekyll_config == {}

    def test_generate_repo_item_basic(self, generator, sample_repos):
        """基本的なリポジトリ項目生成テスト"""
        repo = sample_repos["active"][0]
        result = generator._generate_repo_item(repo, username="test")

        assert "## [active-repo]" in result
        assert "https://test.github.io/active-repo/" in result
        assert "アクティブなリポジトリ" in result
        assert "Python-3572A5" in result  # Pythonのカスタム色が含まれていることを確認
        assert "test" in result
        assert "python" in result
        assert "GitHub Pages" in result
        assert "2024年01月01日" in result

    def test_generate_repo_item_fork(self, generator, sample_repos):
        """フォークリポジトリの項目生成テスト"""
        repo = sample_repos["forks"][0]
        result = generator._generate_repo_item(repo, is_fork=True, username="test")

        assert "Fork" in result
        assert "forked-repo" in result

    def test_generate_repo_item_no_pages(self, generator, sample_repos):
        """GitHub Pages無しリポジトリの項目生成テスト"""
        repo = sample_repos["archived"][0]
        result = generator._generate_repo_item(repo, username="test")

        assert "Pages無し" in result
        assert "https://github.com/test/archived-repo" in result

    def test_generate_section_active(self, generator, sample_repos):
        """アクティブセクション生成テスト"""
        result = generator._generate_section(sample_repos["active"], username="test")
        assert "active-repo" in result
        assert len(result) > 0

    def test_generate_section_empty_archived(self, generator):
        """空のアーカイブセクション生成テスト"""
        result = generator._generate_section([], "archived")
        assert result == "アーカイブされたリポジトリはありません。"

    def test_generate_fork_section(self, generator, sample_repos):
        """フォークセクション生成テスト"""
        result = generator._generate_fork_section(sample_repos["forks"], username="test")
        assert "forked-repo" in result
        assert "Fork" in result

    def test_generate_toc(self, generator):
        """目次生成テスト"""
        result = generator._generate_toc()
        assert "## 目次" in result
        assert "[統計情報]" in result
        assert "[アクティブなリポジトリ]" in result

    def test_generate_statistics_section(self, generator, sample_repos):
        """統計情報セクション生成テスト"""
        active = sample_repos["active"]
        archived = sample_repos["archived"]
        forks = sample_repos["forks"]

        result = generator._generate_statistics_section(active, archived, forks)

        assert "## 統計情報" in result
        assert "リポジトリ-3-blue" in result  # 総数3
        assert "アクティブ-1-green" in result  # アクティブ1
        assert "アーカイブ-1-yellow" in result  # アーカイブ1
        assert "フォーク-1-purple" in result  # フォーク1
        assert "スター-15-gold" in result  # 合計スター15

    @patch("date_formatter.datetime")
    def test_generate_markdown_complete(
        self, mock_datetime, generator, sample_repos, mock_seo_config, mock_json_ld_template
    ):
        """完全なMarkdown生成テスト"""
        # 現在時刻をモック (timezone.utc を渡すため、aware datetime を返す)
        from datetime import timezone

        mock_now = datetime(2024, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
        mock_datetime.now.return_value = mock_now

        result = generator.generate_markdown(
            username="testuser",
            active=sample_repos["active"],
            archived=sample_repos["archived"],
            forks=sample_repos["forks"],
            seo_config=mock_seo_config,
            json_ld_template=mock_json_ld_template,
        )

        # フロントマターの確認
        assert "---" in result
        assert "title:" in result
        assert "testuser" in result

        # メインコンテンツの確認
        assert "# testuserのGitHubリポジトリ一覧" in result
        # 日付はUTC/JST両表記になっている
        assert "(UTC)" in result
        assert "(JST)" in result
        assert "最終更新:" in result
        assert "## 目次" in result
        assert "## 統計情報" in result
        assert "## アクティブなリポジトリ" in result
        assert "## アーカイブされたリポジトリ" in result
        assert "## フォークしたリポジトリ" in result

        # リポジトリ情報の確認
        assert "active-repo" in result
        assert "archived-repo" in result
        assert "forked-repo" in result

    def test_generate_repo_item_with_project_overview(self, generator):
        """プロジェクト概要付きリポジトリアイテム生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "project_overview": [
                "🚀 テストリポジトリの1番目の説明",
                "🔗 テストリポジトリの2番目の説明",
                "✅ テストリポジトリの3番目の説明",
            ],
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "https://github.com/testuser/test-repo" in result
        assert "**GitHub**: " in result
        assert "**GitHub Pages**: " in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # プロジェクト概要セクションの確認
        assert "### Project Highlights" in result
        assert "🚀 テストリポジトリの1番目の説明" in result
        assert "🔗 テストリポジトリの2番目の説明" in result
        assert "✅ テストリポジトリの3番目の説明" in result

    def test_generate_repo_item_without_project_overview(self, generator):
        """プロジェクト概要なしリポジトリアイテム生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            # project_overviewフィールドなし
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # プロジェクト概要セクションがないことの確認
        assert "### Project Highlights" not in result
        assert "🚀" not in result

    def test_generate_repo_item_with_readme_ja_and_pages(self, generator):
        """README.ja.md が存在しGitHub Pagesを持つリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジの確認
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "https://testuser.github.io/test-repo/README.ja.html" in result
        assert '<a href="https://testuser.github.io/test-repo/README.ja.html">' in result
        assert '<img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg">' in result

    def test_generate_repo_item_with_readme_ja_no_pages(self, generator):
        """README.ja.md が存在しGitHub Pagesを持たないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": False,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジの確認 (GitHub URLにリンク)
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "https://github.com/testuser/test-repo/blob/main/README.ja.md" in result
        assert '<a href="https://github.com/testuser/test-repo/blob/main/README.ja.md">' in result

    def test_generate_repo_item_without_readme_ja(self, generator):
        """README.ja.md が存在しないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result
        # Overview ラベルがないことを確認
        assert "**説明**:" not in result

        # Japaneseバッジがないことの確認
        assert "🇯🇵" not in result
        assert "README.ja" not in result

    def test_generate_repo_item_with_readme_en_and_pages(self, generator):
        """README.html が存在しGitHub Pagesを持つリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result

        # Englishバッジの確認
        assert "🇺🇸" in result
        assert "English" in result
        assert "https://testuser.github.io/test-repo/README.html" in result
        assert '<a href="https://testuser.github.io/test-repo/README.html">' in result
        assert '<img src="https://img.shields.io/badge/🇺🇸-English-blue.svg">' in result

    def test_generate_repo_item_with_readme_en_no_pages(self, generator):
        """README.html が存在しGitHub Pagesを持たないリポジトリの項目生成テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": False,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": False,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result
        assert "テストリポジトリ" in result

        # Englishバッジが表示されないことを確認 (GitHub Pagesが無い場合は空欄)
        assert "🇺🇸" not in result
        assert "English" not in result
        assert "README.html" not in result

    def test_generate_repo_item_with_both_readme_ja_and_en(self, generator):
        """README.ja.mdとREADME.htmlの両方が存在する場合のバッジ順序テスト"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "テストリポジトリ",
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test", "python"],
            "has_readme_ja": True,
            "has_readme_en": True,
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 両方のバッジが存在することを確認
        assert "🇯🇵" in result
        assert "Japanese" in result
        assert "🇺🇸" in result
        assert "English" in result

        # バッジの順序を確認: Japanese -> English -> GitHub Pages
        ja_badge_pos = result.find("🇯🇵")
        en_badge_pos = result.find("🇺🇸")
        pages_badge_pos = result.find("GitHub_Pages")

        assert ja_badge_pos < en_badge_pos, "Japaneseバッジが左端にあること"
        assert en_badge_pos < pages_badge_pos, "EnglishバッジがGitHub Pagesバッジの前にあること"

    def test_generate_repo_item_with_no_description(self, generator):
        """概要情報なしリポジトリの項目生成テスト（箇条書きに表示されることを確認）"""
        repo = {
            "name": "test-repo",
            "url": "https://github.com/testuser/test-repo",
            "pages_url": "https://testuser.github.io/test-repo/",
            "description": "No description available",  # 概要情報なし
            "has_pages": True,
            "archived": False,
            "fork": False,
            "updated_at": datetime(2024, 1, 15),
            "stargazers_count": 5,
            "language": "Python",
            "topics": ["test"],
        }

        result = generator._generate_repo_item(repo, username="testuser")

        # 基本情報の確認
        assert "## [test-repo]" in result

        # 概要情報がない場合は箇条書きに「Overview: No description available」が表示される
        assert "**説明**: No description available" in result

        # リポジトリ名の次の行には表示されない（空行のみ）
        lines = result.split("\n")
        repo_name_index = next(i for i, line in enumerate(lines) if "## [test-repo]" in line)
        # リポジトリ名の次の行は空行であるべき
        assert lines[repo_name_index + 1] == ""


# レガシー互換のためのメイン関数
def main():
    """テスト実行のためのメイン関数（レガシー互換）"""
    return pytest.main([__file__, "-v"])


if __name__ == "__main__":
    sys.exit(main())

{% endraw %}
```

## 最近の変更（過去7日間）
### コミット履歴:
643296b CI整頓
22dd812 Auto-update repository list - 2026-03-27
6c13edf Update project summaries (overview & development status) [auto]
6134b15 Auto-update repository list - 2026-03-26
5973547 Update project summaries (overview & development status) [auto]
2366e96 Auto-update repository list - 2026-03-25
3ef0d12 Update project summaries (overview & development status) [auto]
2fb4062 Auto-update repository list - 2026-03-24
8a27048 Update project summaries (overview & development status) [auto]
3cd54aa Auto-update repository list - 2026-03-23

### 変更されたファイル:
.github/workflows/call-check-large-files.yml
.github/workflows/check-large-files-reusable.yml
generated-docs/development-status-generated-prompt.md
generated-docs/development-status.md
generated-docs/project-overview-generated-prompt.md
generated-docs/project-overview.md
index.md


---
Generated at: 2026-03-29 07:08:23 JST
