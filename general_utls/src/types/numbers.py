from typing import Optional


class Numbers:
    @staticmethod
    def reduce_floating_points(input: float, reduce_count: int = 2):
        return float(f'{input:.{reduce_count}f}')

    def safe_int(self, input):
        if not input:
            return None
        return int(input)

    def safe_float(self, input):
        if not input:
            return None
        return float(input)
