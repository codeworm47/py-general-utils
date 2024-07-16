from typing import Optional


class Numbers:
    @staticmethod
    def reduce_floating_points(input: float, reduce_count: int = 2):
        if not input:
            return input
        format_string = "{:." + str(reduce_count) + "f}"
        return float(format_string.format(input))

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
