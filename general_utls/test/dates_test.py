from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from general_utls.src.configs.config_reader import Config
from general_utls.src.types.dates import Dates


class DatesTest(TestCase):
    def test_to_timestamp_utc(self):
        d = Dates.now_utc()
        ts = Dates.to_timestamp_utc(d)
        print(ts)
        d2 = Dates.from_string(Dates.from_timestamp_string_date_utc(ts, True))
        assert self.__parse_date(str(d)) == self.__parse_date(str(d2))

    @patch.object(Config, 'read', new=lambda a, b, c: "Europe/Stockholm")
    def test_to_timestamp(self):
        d = Dates.now()
        ts = Dates.to_timestamp(d)
        print(ts)
        a = Dates.from_timestamp_string_date(ts, True)
        print(a)
        d2 = Dates.from_string(a)
        assert self.__parse_date(str(d)) == self.__parse_date(str(d2))

    def test_from_string(self):
        now_utc_str = str(Dates.now_utc())
        now_str = str(Dates.now())
        now = Dates.from_string(now_str)
        now_utc = Dates.from_string(now_utc_str)
        assert now
        assert now_utc

    @classmethod
    def __parse_date(cls, d):
        date_arr = str(d).split('.')
        if len(date_arr) < 2:
            return d
        date_till_sec = date_arr[0]
        ts = date_arr[1]
        if len(ts) > 3:
            return f'{date_till_sec}.{ts[:2]}'
        return f'{date_till_sec}.{ts}'
