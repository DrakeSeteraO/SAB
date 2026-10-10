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
        temp = self.expression.display()
        temp = 'Grouping:\n    └── ' + temp.replace('\n','\n    ')
        return temp



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
        temp1 = f"Unary:\n├── Operator: {self.operator.lexeme}\n└── Expression:"
        temp2 = '\n    └── '+ self.expression.display().replace('\n', '\n    ')
        return temp1 + temp2 
    


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
        temp1 = '\n│   └── '+self.left.display().replace('\n', '\n│       ')
        temp2 = '\n    └── '+self.right.display().replace('\n', '\n        ')
        out = f"Binary:\n├── Expression:{temp1}" +\
            f"\n├── Operator: {self.operator.lexeme}" +\
            f"\n└── Expression:{temp2}"
        return out