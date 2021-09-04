from unittest import TestCase

from general_utls.src.types.collections import Collections
from jsonget import json_get


class CollectionsTests(TestCase):
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
        Collections.remove_recursive(data1, 'name1')
        assert "name1" not in data1

        data2 = {
            "sample": {
                "a1": {
                    "test1": "testValue",
                    "test2": "testValue2"
                }
            }
        }

        Collections.remove_recursive(data2, 'sample.a1.test1')
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
        Collections.remove_recursive(data3, 'list.key')
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
        Collections.remove_recursive(data4, 'list.value.name')
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
        Collections.remove_recursive(data5, 'key')
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
        Collections.remove_recursive(data6, 'value.name')
        for l in data5:
            assert "name" not in l['value']
