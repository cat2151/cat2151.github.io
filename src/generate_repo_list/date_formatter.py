"""日付フォーマットモジュール

このモジュールはUTCとJSTの両方で日付を表示する機能を提供します。
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict


class DateFormatter:
    """UTC/JST両対応の日付フォーマッタークラス"""

    # JST = UTC+9時間
    JST_OFFSET_HOURS = 9

    def __init__(self, config: Dict[str, Any]):
        """初期化

        Args:
            config: 設定辞書（date_formatを含む）
        """
        self.date_format = config.get("date_format", "%Y-%m-%d")

    def format_dual_timezone(self, dt: datetime) -> str:
        """UTC と JST の両方で日付をフォーマットする

        Args:
            dt: フォーマットする日時（naive datetime の場合はUTCとして扱う）

        Returns:
            "YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)" 形式の文字列
        """
        # naive datetime の場合はUTCとして扱う
        if dt.tzinfo is None:
            dt_utc = dt.replace(tzinfo=timezone.utc)
        else:
            dt_utc = dt.astimezone(timezone.utc)

        # UTC フォーマット
        utc_str = dt_utc.strftime(self.date_format)

        # JST に変換（UTC+9時間）
        dt_jst = dt_utc + timedelta(hours=self.JST_OFFSET_HOURS)
        jst_str = dt_jst.strftime(self.date_format)

        return f"{utc_str} (UTC) / {jst_str} (JST)"

    def format_current_date_dual_timezone(self) -> str:
        """現在日時をUTCとJSTの両方でフォーマットする

        Returns:
            "YYYY-MM-DD (UTC) / YYYY-MM-DD (JST)" 形式の文字列
        """
        return self.format_dual_timezone(datetime.now(timezone.utc))
