from typing import Dict


class Collections:
    @classmethod
    def remove_recursive(cls, data, key: str):
        if '.' in key:
            key_list = key.split('.')
            first_key = key_list[0]
            if isinstance(data, dict):
                if first_key in data:
                    del key_list[0]
                    cls.remove_recursive(data[first_key], '.'.join(key_list))
            if isinstance(data, list):
                for item in data:
                    cls.remove_recursive(item, '.'.join(key_list))

        else:
            if isinstance(data, dict):
                if key in data:
                    del data[key]
            if isinstance(data, list):
                for item in data:
                    if key in item:
                        del item[key]
