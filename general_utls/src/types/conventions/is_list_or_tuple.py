from collections.abc import Sequence


def is_list_or_tuple(data) -> bool:
    return isinstance(data, Sequence)
