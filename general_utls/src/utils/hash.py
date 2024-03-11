from typing import Dict


class Hash:
    @staticmethod
    def hash_simple_dict(d: Dict):
        return hash(frozenset(d.items()))
