from datetime import datetime
from typing import Dict
import json
import hashlib


class Hash:
    @staticmethod
    def hash_simple_dict(d: Dict):
        return hash(frozenset(d.items()))

    @staticmethod
    def hash_dict(d: Dict):
        def date_wise_converter(o):
            if isinstance(o, datetime):
                return o.__str__()
            return o

        dict_str = json.dumps(d, sort_keys=True, default=date_wise_converter)
        hash_obj = hashlib.sha256()
        hash_obj.update(dict_str.encode('utf-8'))
        return hash_obj.hexdigest()
