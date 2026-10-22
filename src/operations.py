from fractions import Fraction
from tokentype import TokenType, OPERATOR_VAL_TYPE
from sab_token import Token


def type_convert(val, new_type: object):
    is_target_bool = (new_type is bool) or (isinstance(new_type, tuple) and bool in new_type)
    is_target_int = (new_type is int) or (isinstance(new_type, tuple) and int in new_type)
    is_target_float = (new_type is float) or (isinstance(new_type, tuple) and float in new_type)

    if isinstance(val, bool):
        if is_target_bool:
            return True, val
        if is_target_int:
            return True, 1 if val else 0
        return False, val

    if isinstance(val, (int, float, Fraction)) and new_type is bool:
        return True, True if val != 0 else False

    if isinstance(val, Fraction):
        if is_target_float or is_target_int:
            return True, val
        return False, val

    if isinstance(val, new_type):
        return True, val

    return False, val


def python_unary(operator: Token, val):
    target_type = int if operator.type == TokenType.NOT else (int, float)
    can_convert, val = type_convert(val, target_type)
    if can_convert:
        res = eval(f"{operator.lexeme} ({repr(val)})")
        if isinstance(res, Fraction) and res.denominator == 1:
            res = int(res)
        return True, res
    return False, f"({operator.lexeme} {val})"


def plus_plus(operator: Token, val):
    can_convert, val = type_convert(val, (int, float))
    if can_convert:
        return True, val + 1
    return False, f"({operator.lexeme} {val})"


def minus_minus(operator: Token, val):
    can_convert, val = type_convert(val, (int, float))
    if can_convert:
        return True, val - 1
    return False, f"({operator.lexeme} {val})"


def bool_not(operator: Token, val):
    can_convert, val = type_convert(val, bool)
    if can_convert:
        return True, not val
    return False, f"({operator.lexeme} {val})"


def python_binary(operator: Token, val1, val2):
    can_convert1, val1 = type_convert(val1, OPERATOR_VAL_TYPE[operator.type])
    can_convert2, val2 = type_convert(val2, OPERATOR_VAL_TYPE[operator.type])
    if can_convert1 and can_convert2:
        try:
            if operator.type == TokenType.SLASH and isinstance(val1, (int, Fraction)) and isinstance(val2, (int, Fraction)):
                res = Fraction(val1, val2)
            else:
                res = eval(f"({repr(val1)}) {operator.lexeme} ({repr(val2)})")
            if isinstance(res, Fraction) and res.denominator == 1:
                res = int(res)
            return True, res
        except Exception:
            pass
    return False, f"({operator.lexeme} {val1} {val2})"


def bool_and(operator: Token, val1, val2):
    can_convert1, val1 = type_convert(val1, OPERATOR_VAL_TYPE[operator.type])
    can_convert2, val2 = type_convert(val2, OPERATOR_VAL_TYPE[operator.type])
    if can_convert1 and can_convert2:
        return True, bool(val1 and val2)
    return False, f"({operator.lexeme} {val1} {val2})"


def bool_or(operator: Token, val1, val2):
    can_convert1, val1 = type_convert(val1, OPERATOR_VAL_TYPE[operator.type])
    can_convert2, val2 = type_convert(val2, OPERATOR_VAL_TYPE[operator.type])
    if can_convert1 and can_convert2:
        return True, bool(val1 or val2)
    return False, f"({operator.lexeme} {val1} {val2})"


def equal_assign(operator: Token, val1, val2):
    can_convert1, val1 = type_convert(val1, OPERATOR_VAL_TYPE[operator.type])
    can_convert2, val2 = type_convert(val2, OPERATOR_VAL_TYPE[operator.type])
    if can_convert1 and can_convert2:
        return True, val2
    return False, f"({operator.lexeme} {val1} {val2})"


def op_assign(operator: Token, val1, val2):
    can_convert1, val1 = type_convert(val1, OPERATOR_VAL_TYPE[operator.type])
    can_convert2, val2 = type_convert(val2, OPERATOR_VAL_TYPE[operator.type])
    if can_convert1 and can_convert2:
        try:
            base_op = operator.lexeme[:-1]
            res = eval(f"({repr(val1)}) {base_op} ({repr(val2)})")
            if isinstance(res, Fraction) and res.denominator == 1:
                res = int(res)
            return True, res
        except Exception:
            pass
    return False, f"({operator.lexeme} {val1} {val2})"


def python_trinary(operator: Token, cond, val1, val2):
    can_convert, cond_bool = type_convert(cond, bool)
    if can_convert:
        return True, val1 if cond_bool else val2
    return False, f"({operator.lexeme} {cond} {val1} {val2})"