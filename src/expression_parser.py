from tokentype import *
from abstract_syntax_tree import *



TOKEN_TO_LITERAL = {
    TokenType.INTEGER : Integer_Node,
    TokenType.FLOATING_POINT : Float_Node,
    TokenType.CHARACTER: Character_Node,
    TokenType.STRING: String_Node,
    TokenType.BINARY: Binary_Node,
    TokenType.HEXADECIMAL : Hexadecimal_Node,
    TokenType.NULL : Raw_Node,
    TokenType.TRUE : Raw_Node,
    TokenType.FALSE : Raw_Node
}



LAST_LEVEL = -1 % len(EXPRESSION_PRECEDENCE)



class Expression_Parser:
    def __init__(self, expression: str):
        if not isinstance(expression, str):
            raise TypeError
        self.tokens = expression
        self.current = 0
    
    
    
    def parse(self):
        return self.evaluate(LAST_LEVEL)
    
    
    
    def evaluate(self, level: int):
        if level <= 0:
            if self.match(TOKEN_TO_LITERAL.keys()):
                return TOKEN_TO_LITERAL[self.previous()](self.previous())
            
            if self.match(TokenType.LEFT_PAREN):
                inner = self.evaluate(LAST_LEVEL)
                self.match(TokenType.RIGHT_PAREN)
                return Grouping(inner)
            
            raise ValueError("Expected a value")
        
        
        if level == 1:
            if self.match(UNARY_OPERATORS):
                operator = self.previous()
                right = self.evaluate(level)
                return Unary(operator, right)
            
            return self.evaluate(level - 1)
        
        
        else:
            left = self.expression(level - 1)
            
            while self.match(EXPRESSION_PRECEDENCE[level]):
                operator = self.previous()
                right = self.evaluate(level - 1)
                left = Binary(left, operator, right)
            
            return left
    
    
    
    def match(self, types):
        if self.tokens[self.current] in types:
            self.advance()
            return True
        return False



    def check(self, token_type):
        if self.is_at_end(): return False
        return self.tokens[self.current].type == token_type



    def advance(self):
        if not self.is_at_end(): self.current += 1
        return self.previous()



    def previous(self):
        return self.tokens[self.current - 1]




    def is_at_end(self):
        return self.tokens[self.current].type == TokenType.EOF
    