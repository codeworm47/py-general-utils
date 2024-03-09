from typing import List


class Lists:
    @staticmethod
    def dict_list(list: List[object]):
        return [li.__dict__ for li in list]

    @staticmethod
    def transform(list: List[object], func):
        # assert func is callable
        return [func(li) for li in list]

    @staticmethod
    def remove_duplicates(list: List[object]):
        return [i for n, i in enumerate(list) if i not in list[:n]]
