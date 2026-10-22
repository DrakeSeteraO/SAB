from interpreter_tree import *
from tokentype import TokenType, UNARY_OPERATIONS, BINARY_OPERATIONS
from operations import python_trinary, type_convert



class Interpreter:
    def __init__(self):
        pass



    def get_expression(self, expression: Expression):
        EXPRESSION_EVALUATION = {
            'Literal' : self.literal_operation,
            'Grouping' : self.grouping_operation,
            'Unary' : self.unary_operation,
            'Binary' : self.binary_operation,
            'Trinary' : self.trinary_operation
        }
        return EXPRESSION_EVALUATION[expression.type](expression)
        
        
        
    RAW_LITERAL = {
        'TRUE' : True,
        'FALSE' : False,
        'NULL' : None
    }



    def literal_operation(self, node: Literal):
        val = node.val_token.literal if node.val_token.literal is not None else node.val_token.lexeme
        if isinstance(node, Integer_Node):
            return True, int(val)
        if isinstance(node, Float_Node):
            return True, float(val)
        if isinstance(node, (Character_Node, String_Node)):
            return True, val
        if isinstance(node, Binary_Node):
            b_val = val[2:] if val.startswith(('0b', '0B')) else val
            return True, int(b_val, 2)
        if isinstance(node, Hexadecimal_Node):
            h_val = val[2:] if val.startswith(('0x', '0X')) else val
            return True, int(h_val, 16)
        if isinstance(node, Raw_Node):
            return True, self.RAW_LITERAL[val.upper()]
        if isinstance(node, Variable_Node):
            return False, val
        return False, 'None'



    def grouping_operation(self, node: Grouping):
        return self.get_expression(node.expression)



    def unary_operation(self, node: Unary):
        can_eval, temp = self.get_expression(node.expression)
        if can_eval and UNARY_OPERATIONS[node.operator.type] is not None:
            return UNARY_OPERATIONS[node.operator.type](node.operator, temp)
        return False, f"({node.operator.lexeme} {temp})"
        
        
    def binary_operation(self, node: Binary):
        can_eval1, left = self.get_expression(node.left)
        can_eval2, right = self.get_expression(node.right)
        if can_eval1 and can_eval2 and BINARY_OPERATIONS[node.operator.type] is not None:
            return BINARY_OPERATIONS[node.operator.type](node.operator, left, right)
        return False, f"({node.operator.lexeme} {left} {right})"


    def trinary_operation(self, node: Trinary):
        can_eval1, left = self.get_expression(node.left)
        can_eval2, middle = self.get_expression(node.middle)
        if node.right is not None:
            can_eval3, right = self.get_expression(node.right)
        else:
            can_eval3, right = True, None

        if can_eval1:
            can_convert, res = python_trinary(node.left_operator, left, middle, right)
            if can_convert:
                _, cond_bool = type_convert(left, bool)
                return (can_eval2 if cond_bool else can_eval3), res
        return False, f"({node.left_operator.lexeme} {left} {middle} {right})"