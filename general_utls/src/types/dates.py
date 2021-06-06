from datetime import datetime, timezone, timedelta
from general_utls.src.configs.config_reader import Config
import pytz
from sys import platform


class Dates:
    UTC_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    @classmethod
    def now_utc(cls):
        return datetime.now(timezone.utc).strftime(cls.UTC_DATE_FORMAT)

    @classmethod
    def now(cls):
        return datetime.now(cls.__get_time_zone()).strftime(cls.UTC_DATE_FORMAT)

    @staticmethod
    def today_str():
        return datetime.today().strftime('%Y-%m-%d')

    @classmethod
    def from_timestamp(cls, time_stamp: float, is_milisec: bool, append_tz: bool = False):
        if is_milisec:
            time_stamp = time_stamp / 1000
        date = datetime.fromtimestamp(time_stamp, cls.__get_time_zone())
        if append_tz:
            return date.strftime(cls.UTC_DATE_FORMAT+', ' + str(cls.__get_time_zone()))
        else:
            return date.strftime(cls.UTC_DATE_FORMAT)
        # .replace(tzinfo=cls.__get_time_zone())
        # .strftime('%Y-%m-%dT%H:%M:%SZ')

    @classmethod
    def from_timestamp_utc(cls, time_stamp: float, is_milisec: bool):
        if is_milisec:
            time_stamp = time_stamp / 1000
        return datetime.fromtimestamp(time_stamp).strftime(cls.UTC_DATE_FORMAT)

    @classmethod
    def __get_time_zone(cls):
        sys_config = Config("settings/system.json")
        return pytz.timezone(sys_config.read("zone", "datetime"))
