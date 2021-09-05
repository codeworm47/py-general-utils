class Booleans:
    @staticmethod
    def is_bool(value: str):
        valid_vals = ["true", "false", "0", "1"]
        _value = value.lower()
        return _value in valid_vals
