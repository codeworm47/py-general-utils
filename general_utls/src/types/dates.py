from datetime import datetime, timezone
from general_utls.src.configs.config_reader import Config
import pytz


class Dates:
    @staticmethod
    def now_utc():
        return datetime.now(timezone.utc)

    @staticmethod
    def now():
        sys_config = Config("settings/system.json")
        return datetime.now(pytz.timezone(sys_config.read("zone", "datetime")))

    @staticmethod
    def today_str():
        return datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def from_timestamp(time_stamp: float):
        return datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%dT%H:%M:%SZ')
