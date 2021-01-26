from datetime import datetime, timezone
import pytz


class Dates:
    @staticmethod
    def now_utc():
        return datetime.now(timezone.utc)

    @staticmethod
    def now_Iran():
        return datetime.now(pytz.timezone("IRST"))
