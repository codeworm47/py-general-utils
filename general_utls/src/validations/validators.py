def validate_numeric_value(value, min=None, max=None, include_equals_min=False, include_equals_max=False):
    def get_operand_string(operand, include_equals=False):
        if include_equals:
            return f"{operand}="
        else:
            return operand

    if min:
        cond = value > min if not include_equals_min else value >= min
        if not cond:
            upper_part = f"{get_operand_string('<', include_equals_max)} {max}"
            raise ValueError(
                f"invalid value: {value}, correct value must be {min} {get_operand_string('>', include_equals_min)} {upper_part if max else ''}")
    if max:
        cond = value < max if not include_equals_max else value <= max
        if not cond:
            lower_part = f"{min} {get_operand_string('>', include_equals_min)}"
            raise ValueError(
                f"invalid value: {value}, correct value must be {lower_part if min else ''} {get_operand_string('<', include_equals_max)} {max}")
