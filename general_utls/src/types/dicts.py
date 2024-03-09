from typing import Dict, List


class Dicts:
    @classmethod
    def remove_field_recursive(cls, data: Dict, key: str):
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
    def remove_fields_recursive(cls, data: Dict, keys: List[str]):
        assert keys
        for key in keys:
            cls.remove_field_recursive(data, key)

    @staticmethod
    def safe_read(data, path, default=None):
        keys = path.split('.')
        try:
            for key in keys:
                data = data[key]
            return data
        except (KeyError, TypeError):
            return default
