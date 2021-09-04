from typing import Dict, List


class Collections:
    @classmethod
    def remove_field_recursive(cls, data, key: str):
        if '.' in key:
            key_list = key.split('.')
            first_key = key_list[0]
            if isinstance(data, dict):
                if first_key in data:
                    del key_list[0]
                    cls.remove_field_recursive(data[first_key], '.'.join(key_list))
            if isinstance(data, list):
                for item in data:
                    cls.remove_field_recursive(item, '.'.join(key_list))

        else:
            if isinstance(data, dict):
                if key in data:
                    del data[key]
            if isinstance(data, list):
                for item in data:
                    if key in item:
                        del item[key]

    @classmethod
    def remove_fields_recursive(cls, data, keys: List[str]):
        assert keys
        for key in keys:
            cls.remove_field_recursive(data, key)
