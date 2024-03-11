from unittest import TestCase

from general_utls.src.types.dates import Dates
from general_utls.src.utils.hash import Hash


class HashTest(TestCase):
    def test_hash_simple_dict(self):
        d = {'a': 1234, 'b': '2', 'c': Dates.now_utc(), 'd': False}
        hash = Hash.hash_simple_dict(d)
        d['a'] = 12345
        hash2 = Hash.hash_simple_dict(d)
        hash3 = Hash.hash_simple_dict(d)
        d2 = d.copy()
        hash4 = Hash.hash_simple_dict(d2)
        assert hash != hash2
        assert hash2 == hash3
        assert hash4 == hash3 == hash2
