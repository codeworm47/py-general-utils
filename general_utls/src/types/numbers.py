class Numbers:
    @staticmethod
    def reduce_floating_points(input: float, reduce_count: int = 2):
        return float(f'{input:.{reduce_count}f}')
