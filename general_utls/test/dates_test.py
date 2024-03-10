from datetime import datetime
from unittest import TestCase

from general_utls.src.types.dates import Dates


class DatesTest(TestCase):
    def test_to_timestamp_utc(self):
        d = Dates.now_utc()
        ts = Dates.to_timestamp_utc(d)
        print(ts)
        print(len(str(ts)[:str(ts).find('.')]))
        d2 = Dates.from_string(Dates.from_timestamp_utc(ts, True))
        assert d == d2
