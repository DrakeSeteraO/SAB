from interpreter_tree import *
from tokentype import TokenType



class Interpreter:
    def __init__(self):
        pass



    def get_expression(self, expression: Expression):
        EXPRESSION_EVALUATION = {
            'Literal' : self.literal_operation,
            'Grouping' : self.grouping_operation
        }
        return EXPRESSION_EVALUATION[expression.__name__](expression)
        
        
        
    RAW_LITERAL = {
        'TRUE' : True,
        'FALSE' : False,
        'NULL' : None
    }




    def literal_operation(self, node: Literal):
        if isinstance(node, Integer_Node):
            return True, int(node.val_token.literal)
        if isinstance(node, Float_Node):
            return True, float(node.val_token.literal)
        if isinstance(node, (Character_Node, String_Node)):
            return True, node.val_token.literal
        if isinstance(node, Binary_Node):
            return True, int(node.val_token.literal[2:],2)
        if isinstance(node, Hexadecimal_Node):
            return True, int(node.val_token.literal[2:], 16)
        if isinstance(node, Raw_Node):
            return True, self.RAW_LITERAL[node.val_token.literal]
        if isinstance(node, Variable_Node):
            return False, node.val_token.literal
        return False, 'None'



    def grouping_operation(self, node: Grouping):
        return self.get_expression[node.expression.type](node.expression)


    def unary_operation(self, node: Unary):
        can_eval, temp = self.get_expression[node.expression.type](node.expression)
        if can_eval:
            ...
        return False, f"({node.operator} {temp})"
        
        
    def binary_operation(self, operation: TokenType, left: Expression, right: Expression):
        ...

