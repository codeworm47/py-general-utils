from typing import List


class Lists:
    @staticmethod
    def dict_list(list: List[object]):
        return [li.__dict__ for li in list]
