"""DateFormatter のテスト"""

import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

# テスト対象モジュールのパスを追加
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "generate_repo_list"))

from date_formatter import DateFormatter


class TestDateFormatter:
    """DateFormatter クラスのテストスイート"""

    @pytest.fixture
    def formatter(self):
        """テスト用のフォーマッターインスタンスを作成"""
        config = {"date_format": "%Y-%m-%d"}
        return DateFormatter(config)

    @pytest.fixture
    def formatter_with_time(self):
        """時刻付きフォーマッターインスタンスを作成"""
        config = {"date_format": "%Y-%m-%d %H:%M:%S"}
        return DateFormatter(config)

    def test_init_with_config(self):
        """設定付きで初期化できることを確認"""
        config = {"date_format": "%Y/%m/%d"}
        formatter = DateFormatter(config)
        assert formatter.date_format == "%Y/%m/%d"

    def test_init_with_default(self):
        """デフォルト設定で初期化できることを確認"""
        config = {}
        formatter = DateFormatter(config)
        assert formatter.date_format == "%Y-%m-%d"

    def test_format_dual_timezone_utc_datetime(self, formatter):
        """UTC datetimeを正しくフォーマットできることを確認"""
        # UTC の 2024-01-01 00:00:00
        dt = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = formatter.format_dual_timezone(dt)

        # UTC: 2024-01-01 00:00:00 -> JST: 2024-01-01 09:00:00
        assert result == "2024-01-01 (UTC) / 2024-01-01 (JST)"

    def test_format_dual_timezone_naive_datetime(self, formatter):
        """naive datetimeをUTCとして扱うことを確認"""
        # naive datetime (タイムゾーン情報なし) は UTC として扱われる
        dt = datetime(2024, 1, 1, 0, 0, 0)
        result = formatter.format_dual_timezone(dt)

        assert result == "2024-01-01 (UTC) / 2024-01-01 (JST)"

    def test_format_dual_timezone_date_change(self, formatter):
        """日付が変わるケースを確認"""
        # UTC の 2024-01-01 20:00:00
        dt = datetime(2024, 1, 1, 20, 0, 0, tzinfo=timezone.utc)
        result = formatter.format_dual_timezone(dt)

        # UTC: 2024-01-01 -> JST: 2024-01-02 (UTC+9時間)
        assert result == "2024-01-01 (UTC) / 2024-01-02 (JST)"

    def test_format_dual_timezone_with_time(self, formatter_with_time):
        """時刻付きフォーマットを確認"""
        dt = datetime(2024, 1, 1, 15, 30, 45, tzinfo=timezone.utc)
        result = formatter_with_time.format_dual_timezone(dt)

        # UTC: 2024-01-01 15:30:45 -> JST: 2024-01-02 00:30:45
        assert result == "2024-01-01 15:30:45 (UTC) / 2024-01-02 00:30:45 (JST)"

    def test_format_current_date_dual_timezone(self, formatter):
        """現在日時のフォーマットが機能することを確認"""
        result = formatter.format_current_date_dual_timezone()

        # 結果が期待する形式であることを確認
        assert " (UTC) / " in result
        assert " (JST)" in result
        # 日付部分が YYYY-MM-DD 形式であることを確認
        parts = result.split(" (UTC) / ")
        assert len(parts) == 2
        utc_part = parts[0]
        jst_part = parts[1].replace(" (JST)", "")
        assert len(utc_part) == 10  # YYYY-MM-DD
        assert len(jst_part) == 10  # YYYY-MM-DD

    def test_jst_offset_constant(self):
        """JST オフセットが正しく設定されていることを確認"""
        assert DateFormatter.JST_OFFSET_HOURS == 9

    def test_format_dual_timezone_year_end(self, formatter):
        """年末のエッジケースを確認"""
        # UTC の 2024-12-31 23:00:00
        dt = datetime(2024, 12, 31, 23, 0, 0, tzinfo=timezone.utc)
        result = formatter.format_dual_timezone(dt)

        # UTC: 2024-12-31 -> JST: 2025-01-01 (UTC+9時間で年が変わる)
        assert result == "2024-12-31 (UTC) / 2025-01-01 (JST)"

    def test_format_dual_timezone_leap_year(self, formatter):
        """うるう年のケースを確認"""
        # UTC の 2024-02-29 20:00:00 (うるう年)
        dt = datetime(2024, 2, 29, 20, 0, 0, tzinfo=timezone.utc)
        result = formatter.format_dual_timezone(dt)

        # UTC: 2024-02-29 -> JST: 2024-03-01
        assert result == "2024-02-29 (UTC) / 2024-03-01 (JST)"

    def test_format_dual_timezone_custom_format(self):
        """カスタムフォーマットが機能することを確認"""
        config = {"date_format": "%Y年%m月%d日"}
        formatter = DateFormatter(config)
        dt = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        result = formatter.format_dual_timezone(dt)

        assert result == "2024年01月01日 (UTC) / 2024年01月01日 (JST)"
