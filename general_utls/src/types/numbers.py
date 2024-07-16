from typing import Optional


class Numbers:
    @staticmethod
    def reduce_floating_points(input: float, reduce_count: int = 2):
        if not input:
            return input
        factor = 10 ** reduce_count
        return int(input * factor) / factor

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
