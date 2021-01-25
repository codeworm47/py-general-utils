from datetime import datetime, timezone


class Dates:
    @staticmethod
    def now_utc():
        return datetime.now(timezone.utc)
