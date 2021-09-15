class Booleans:
    @staticmethod
    def is_bool(value: str):
        valid_vals = ["true", "false", "0", "1", "yes", "no", "y", "n"]
        _value = value.lower()
        return _value in valid_vals

    @classmethod
    def eval(cls, value: str) -> bool:
        if not cls.is_bool(value):
            return False
        _value = value.lower()
        trues = ["true", "1", "yes", "y"]

        if _value in trues:
            return True
        else:
            return False
