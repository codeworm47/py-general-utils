from unittest import TestCase

from general_utls.src.types.dicts import Dicts
from jsonget import json_get


class DictsTest(TestCase):
    def test_remove_recursive(self):
        data1 = {
            "name1": "val1",
            "name2": "val2",
            "sample": {
                "a1": {
                    "test1": "testValue",
                    "test2": "testValue2"
                }
            }
        }
        Dicts.remove_field_recursive(data1, 'name1')
        assert "name1" not in data1

        data2 = {
            "sample": {
                "a1": {
                    "test1": "testValue",
                    "test2": "testValue2"
                }
            }
        }

        Dicts.remove_field_recursive(data2, 'sample.a1.test1')
        assert "test1" not in json_get(data2, "/sample/a1")

        data3 = {
            "list": [
                {
                    "key": "1",
                    "value": "2"
                },
                {
                    "key": "3",
                    "value": "4"
                }
            ]
        }
        Dicts.remove_field_recursive(data3, 'list.key')
        list = data3["list"]
        for l in list:
            assert "key" not in l

        data4 = {
            "list": [
                {
                    "key": "1",
                    "value": {
                        "name": "1",
                        "lastName": "a"
                    }
                },
                {
                    "key": "3"
                }
            ]
        }
        Dicts.remove_field_recursive(data4, 'list.value.name')
        list = data4["list"]
        assert "name" not in list[0]['value']

        data5 = [
            {
                "key": "1",
                "value": "2"
            },
            {
                "key": "3",
                "value": "4"
            }
        ]
        Dicts.remove_field_recursive(data5, 'key')
        for l in data5:
            assert "key" not in l

        data6 = [
            {
                "key": "1",
                "value": {
                    "name": "1",
                    "lastName": "a"
                }
            },
            {
                "key": "3",
                "value": {
                    "name": "2",
                    "lastName": "ab"
                }
            }
        ]
        Dicts.remove_field_recursive(data6, 'value.name')
        for l in data5:
            assert "name" not in l['value']

    def test_safe_read(self):
        d = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
        a_val = Dicts.safe_read(d, 'a')
        assert a_val == 1
        b_val = Dicts.safe_read(d, 'b.c')
        assert b_val == 2
        e_val = Dicts.safe_read(d, 'b.d.e')
        assert e_val == 3
        not_exist_key = Dicts.safe_read(d, 'f')
        assert not not_exist_key
