from typing import Optional


class Numbers:
    @staticmethod
    def reduce_floating_points(input: float, reduce_count: int = 2):
        return float(f'{input:.{reduce_count}f}')

    @staticmethod
    def safe_int(input: Optional[int]):
        if not input:
            return None
        return int(input)

    @staticmethod
    def safe_float(input: Optional[float]):
        if not input:
            return None
        return float(input)
