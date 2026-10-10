from tokentype import TokenType, LITERAL_TYPES, UNARY_OPERATORS, BINARY_OPERATORS



class Expression:
    def __str__(self):
        pass
    
    def RPN(self):
        pass



class Literal(Expression):
    def __init__(self, val_token: TokenType):
        if val_token not in LITERAL_TYPES:
            raise TypeError
        self.val_token = val_token

    def __str__(self):
        return self.val_token.lexeme
    
    def RPN(self):
        return self.val_token.lexeme


class Grouping(Expression):
    def __init__(self, expression: Expression):
        if not isinstance(expression, Expression):
            raise TypeError
        self.expression = expression

    def __str__(self):
        return f"(group {self.expression})"
    
    def RPN(self):
        return self.expression.RPN()


class Unary(Expression):
    def __init__(self, operator: TokenType, expression: Expression):
        if type not in UNARY_OPERATORS:
            raise TypeError
        if not isinstance(expression, Expression):
            raise TypeError
        self.operator = operator
        self.expression = expression

    def __str__(self):
        return f"({self.operator.lexeme} {self.expression})"
    
    def RPN(self):
        return f"{self.expression.RPN()} .{self.operator.lexeme}"


class Binary(Expression):
    def __init__(self, left_expression: Expression, operator: Operator, right_expression: Expression):
        if not isinstance(left_expression, Expression):
            raise TypeError
        if not isinstance(operator, BINARY_OPERATORS):
            raise TypeError
        if not isinstance(right_expression, Expression):
            raise TypeError
        self.left = left_expression
        self.operator = operator
        self.right = right_expression
    
    def __str__(self):
        return f"({self.operator} {self.left} {self.right})"
    
    def RPN(self):
        return f"{self.left.RPN()} {self.right.RPN()} {self.operator}"



class Operator(Expression):
    def __init__(self, operator: TokenType):
        if operator not in BINARY_OPERATORS:
            raise TypeError
        self.operator = operator
    
    def __str__(self):
        return self.operator.lexeme

    def RPN(self):
        return self.operator.lexeme