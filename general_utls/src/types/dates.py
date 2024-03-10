import time
from datetime import datetime, timezone, date
from general_utls.src.configs.config_reader import Config
from calendar import monthrange
import pytz


class Dates:
    ISO_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

    @classmethod
    def now_utc(cls):
        # return datetime.now(timezone.utc).strftime(cls.ISO_DATE_FORMAT)
        return datetime.now(timezone.utc)

    @classmethod
    def now_timestamp(cls):
        return round(time.time() * 1000)

    @classmethod
    def now(cls):
        # return datetime.now(cls.__get_time_zone()).strftime(cls.ISO_DATE_FORMAT)
        return datetime.now()

    @classmethod
    def to_date(cls, date: str):
        return datetime.strptime(date, cls.ISO_DATE_FORMAT)

    @staticmethod
    def today_str():
        return datetime.today().strftime('%Y-%m-%d')

    @classmethod
    def today(cls):
        return date.today().strftime(cls.ISO_DATE_FORMAT)

    @classmethod
    def from_timestamp(cls, time_stamp: float, is_milisec: bool, append_tz: bool = False):
        if is_milisec:
            time_stamp = time_stamp / 1000
        date = datetime.fromtimestamp(time_stamp, cls.__get_time_zone())
        if append_tz:
            return cls.with_tz(date)
        else:
            return date.strftime(cls.ISO_DATE_FORMAT)
        # .replace(tzinfo=cls.__get_time_zone())
        # .strftime('%Y-%m-%dT%H:%M:%SZ')

    @classmethod
    def to_timestamp(cls, date):
        ts = int(date.strftime("%s"))
        if len(str(ts)) == 10:
            return ts * 1000
        return ts

    @classmethod
    def to_timestamp_utc(cls, date):
        utc_aware_date = date.replace(tzinfo=timezone.utc)
        ts = float(utc_aware_date.timestamp())
        length = len(str(ts)[:str(ts).find('.')])
        if length == 10:
            return int(ts * 1000)
        return int(ts)

    @classmethod
    def from_timestamp_utc(cls, time_stamp: float, is_milisec: bool):
        if is_milisec:
            time_stamp = time_stamp / 1000
        return datetime.utcfromtimestamp(time_stamp).strftime(cls.ISO_DATE_FORMAT)

    @classmethod
    def hh_mm(cls, date):
        return date.strftime('%H:%M')

    @classmethod
    def with_tz(cls, date):
        return date.strftime(cls.ISO_DATE_FORMAT.replace('.%f', '') + ', ' + str(cls.__get_time_zone()))

    @classmethod
    def is_date(cls, dt_str):
        try:
            cls.from_string(dt_str)
        except ValueError:
            try:
                datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
            except ValueError:
                return False
            return True
        return True

    @classmethod
    def number_of_days_in_current_month(cls):
        now = cls.now()
        date_range = monthrange(now.year, now.month)
        return date_range[1]

    @classmethod
    def from_string(cls, dt_str):
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))

    @classmethod
    def __get_time_zone(cls):
        sys_config = Config("settings/system.json")
        return pytz.timezone(sys_config.read("zone", "datetime"))
