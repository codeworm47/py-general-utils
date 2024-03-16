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

    @staticmethod
    def today_str():
        return datetime.today().strftime('%Y-%m-%d')

    @classmethod
    def today(cls):
        return date.today().strftime(cls.ISO_DATE_FORMAT)

    @classmethod
    def from_timestamp_string_date(cls, timestamp: float, is_milisec: bool, append_tz: bool = False) -> str:
        if is_milisec:
            timestamp = timestamp / 1000
        date = datetime.fromtimestamp(timestamp, cls.__get_time_zone())
        if append_tz:
            return cls.with_tz(date)
        else:
            return date.strftime(cls.ISO_DATE_FORMAT)

    @classmethod
    def from_timestamp_string_date_utc(cls, timestamp: float, is_milisec: bool) -> str:
        if is_milisec:
            timestamp = timestamp / 1000
        return datetime.utcfromtimestamp(timestamp).strftime(cls.ISO_DATE_FORMAT)

    @classmethod
    def from_timestamp(cls, timestamp: float, is_milisec: bool) -> datetime:
        if is_milisec:
            timestamp = timestamp / 1000
        return datetime.fromtimestamp(timestamp, cls.__get_time_zone())

    @classmethod
    def from_timestamp_utc(cls, timestamp: float, is_milisec: bool) -> datetime:
        if is_milisec:
            timestamp = timestamp / 1000
        return datetime.utcfromtimestamp(timestamp)

    @classmethod
    def to_timestamp(cls, date):
        local_tz = cls.__get_time_zone()
        local_date_aware = local_tz.localize(date)
        ts = local_date_aware.timestamp()
        # ts = date.strftime("%s")
        return cls.__handle_seconds_in_timestamp(ts)


    @classmethod
    def to_timestamp_utc(cls, date):
        utc_aware_date = date.replace(tzinfo=timezone.utc)
        return cls.__handle_seconds_in_timestamp(utc_aware_date.timestamp())

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

    @classmethod
    def __handle_seconds_in_timestamp(cls, timestamp):
        ts = float(timestamp)
        ts_str = str(ts)
        length = len(ts_str[:ts_str.find('.')])
        if length == 10:
            return int(ts * 1000)
        return int(ts)

