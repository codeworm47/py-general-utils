from typing import List, Callable, TypeVar, Optional, Any, Dict

T = TypeVar("T")
T2 = TypeVar("T2")


class Lists:
    @staticmethod
    def dict_list(list: List[Any]) -> List[Dict[str, Any]]:
        return [li.__dict__ for li in list]

    @staticmethod
    def transform(list: List[T], func: Callable[[T], T2]) -> List[T2]:
        return [func(li) for li in list]

    @staticmethod
    def remove_duplicates(list: List[T]) -> List[T]:
        return [i for n, i in enumerate(list) if i not in list[:n]]

    @staticmethod
    def chunk(list: List[T], size: int) -> List[List[T]]:
        return [list[i:i + size] for i in range(0, len(list), size)]

    @staticmethod
    def find(list: List[T], predicate: Callable[[T], bool], default: Any = None) -> Optional[T]:
        return next((item for item in list if predicate(item)), default)

    @staticmethod
    def filter(list: List[T], predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in list if predicate(item)]
