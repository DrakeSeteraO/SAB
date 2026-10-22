from tokentype import TokenType, LITERAL_TYPES, UNARY_OPERATORS, BINARY_OPERATORS
from sab_token import Token



class Expression:
    def __str__(self):
        pass
    
    def RPN(self):
        pass
    
    def display(self):
        pass



class Literal(Expression):
    def __init__(self, val_token: Token):
        if val_token.type not in LITERAL_TYPES:
            raise TypeError
        self.val_token = val_token

    def __str__(self):
        return self.val_token.lexeme
    
    def RPN(self):
        return self.val_token.lexeme
    
    def display(self):
        return f"Literal: {self.val_token.lexeme}"



class Integer_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Float_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Character_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class String_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Binary_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Hexadecimal_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Raw_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Variable_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Function_Node(Literal):
    def __init__(self, val_token):
        super().__init__(val_token)



class Grouping(Expression):
    def __init__(self, expression: Expression):
        if not isinstance(expression, Expression):
            raise TypeError
        self.expression = expression

    def __str__(self):
        return f"(group {self.expression})"
    
    def RPN(self):
        return self.expression.RPN()
    
    def display(self):
        out = f"Grouping:" +\
         "\n└── Expression:" +\
        f"\n    └── {self.expression.display().replace('\n', '\n        ')}"
        return out



class Unary(Expression):
    def __init__(self, operator: Token, expression: Expression):
        if operator.type not in UNARY_OPERATORS:
            raise TypeError
        if not isinstance(expression, Expression):
            raise TypeError
        self.operator = operator
        self.expression = expression

    def __str__(self):
        return f"({self.operator.lexeme} {self.expression})"
    
    def RPN(self):
        return f"{self.expression.RPN()} .{self.operator.lexeme}"
    
    def display(self):
        out = f"Unary:" +\
        f"\n├── Operator: {self.operator.lexeme}" +\
         "\n└── Expression:" +\
        f"\n    └── {self.expression.display().replace('\n', '\n        ')}"
        return out
    


class Binary(Expression):
    def __init__(self, left_expression: Expression, operator: Token, right_expression: Expression):
        if not isinstance(left_expression, Expression):
            raise TypeError
        if operator.type not in BINARY_OPERATORS:
            raise TypeError
        if not isinstance(right_expression, Expression):
            raise TypeError
        self.left = left_expression
        self.operator = operator
        self.right = right_expression
    
    def __str__(self):
        return f"({self.operator.lexeme} {self.left} {self.right})"
    
    def RPN(self):
        return f"{self.left.RPN()} {self.right.RPN()} {self.operator.lexeme}"
    
    def display(self):
        out = f"Binary:" +\
         "\n├── Expression:" +\
        f"\n│   └── {self.left.display().replace('\n', '\n│       ')}" +\
        f"\n├── Operator: {self.operator.lexeme}" +\
         "\n└── Expression:" +\
        f"\n    └── {self.right.display().replace('\n', '\n        ')}"
        return out    



class Trinary(Expression):
    def __init__(self, left_expression: Expression, left_operator: Token, middle_expression: Expression, right_operator: Token, right_expression: Expression):
        if not isinstance(left_expression, Expression):
            raise TypeError
        if left_operator.type != TokenType.QUESTION:
            raise TypeError
        if not isinstance(middle_expression, Expression):
            raise TypeError
        if right_operator.type != TokenType.COLON:
            raise TypeError        
        if not (isinstance(right_expression, Expression) or right_expression is None):
            raise TypeError
        self.left = left_expression
        self.left_operator = left_operator
        self.middle = middle_expression
        self.right_operator = right_operator
        self.right = right_expression
    
    def __str__(self):
        return f"({self.left_operator.lexeme} {self.left} {self.middle} {self.right})"
    
    def RPN(self):
        return f"{self.left.RPN()} {self.middle.RPN()} {self.right.RPN()} {self.left_operator.lexeme}"
    
    def display(self):
        out = f"Trinary:" +\
         "\n├── Expression:" +\
        f"\n│   └── {self.left.display().replace('\n', '\n│       ')}" +\
        f"\n├── Operator: {self.left_operator.lexeme}" +\
         "\n├── Expression:" +\
        f"\n│   └── {self.middle.display().replace('\n', '\n│       ')}" +\
        f"\n├── Operator: {self.right_operator.lexeme}" +\
         "\n└── Expression:" +\
        f"\n    └── {self.right.display().replace('\n', '\n        ')}"
        return out    