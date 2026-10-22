


def type_convert(val, new_type: object):
    if isinstance(val, bool) and isinstance(new_type, int):
        return True, 1 if val else 0
    if isinstance(val, int) and isinstance(new_type, bool):
        return True, True if val != 0 else False
    if isinstance(val, new_type):
        return True, val
    return False, None
        


def python_unary(operator: str, val: int):
    can_convert, val = type_convert(val, int)
    if can_convert:
        return True, eval(f"{operator} {val}")
    return False, f"({operator} {val})"



def plus_plus(operator, val):
    can_convert, val = type_convert(val, int)
    if can_convert:
        return True, val + 1
    return False, f"({operator} {val})"



def minus_minus(operator, val):
    can_convert, val = type_convert(val, int)
    if can_convert:
        return True, val - 1
    return False, f"({operator} {val})"



def bool_not(operator, val):
    can_convert, val = type_convert(val, bool)
    if can_convert:
        return True, not val
    return False, f"({operator} {val})"