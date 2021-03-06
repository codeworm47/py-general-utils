from datetime import datetime, timezone, timedelta
from general_utls.src.configs.config_reader import Config
import pytz
from sys import platform


class Dates:
    @staticmethod
    def now_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def now(cls):
        return datetime.now(cls.__get_time_zone())

    @staticmethod
    def today_str():
        return datetime.today().strftime('%Y-%m-%d')

    @classmethod
    def from_timestamp(cls, time_stamp: float):
        if platform.startswith("win32"):
            time_stamp = time_stamp/1000
        return datetime.fromtimestamp(time_stamp)
        #.replace(tzinfo=cls.__get_time_zone())
        #.strftime('%Y-%m-%dT%H:%M:%SZ')

    @classmethod
    def __get_time_zone(cls):
        sys_config = Config("settings/system.json")
        return pytz.timezone(sys_config.read("zone", "datetime"))
