from tokentype import *
from interpreter_tree import *



TOKEN_TO_LITERAL = {
    TokenType.INTEGER : Integer_Node,
    TokenType.FLOATING_POINT : Float_Node,
    TokenType.CHARACTER: Character_Node,
    TokenType.STRING: String_Node,
    TokenType.BINARY: Binary_Node,
    TokenType.HEXADECIMAL : Hexadecimal_Node,
    TokenType.NULL : Raw_Node,
    TokenType.TRUE : Raw_Node,
    TokenType.FALSE : Raw_Node,
    TokenType.IDENTIFIER : Variable_Node
}



LAST_LEVEL = -1 % len(EXPRESSION_PRECEDENCE)



class Parser:
    def __init__(self, expression: list):
        if not isinstance(expression, list):
            raise TypeError
        self.tokens = expression
        self.current = 0
    
    
    
    def parse(self):
        temp = self.evaluate(LAST_LEVEL)
        if not self.at_end():
            raise SyntaxError(f"Unexpected trailing token '{self.tokens[self.current].lexeme}' at line {self.tokens[self.current].line}, column {self.tokens[self.current].column}")
        self.current = 0
        return temp
    
    
    
    def evaluate(self, level: int):
        if level <= 0:
            self.match([TokenType.QUOTE, TokenType.DOUBLE_QUOTE])
            if self.match(TOKEN_TO_LITERAL.keys()):
                node = TOKEN_TO_LITERAL[self.previous().type](self.previous())
                self.match([TokenType.QUOTE, TokenType.DOUBLE_QUOTE])
                return node
            
            if self.match([TokenType.LEFT_PAREN]):
                expression = self.evaluate(LAST_LEVEL)
                self.match([TokenType.RIGHT_PAREN])
                return Grouping(expression)
            
            raise ValueError("Expected a value")
        
        
        elif level == 1:
            if self.match(UNARY_OPERATIONS.keys()):
                operator = self.previous()
                right = self.evaluate(level)
                return Unary(operator, right)
            
            return self.evaluate(level - 1)
        
        
        elif level == LAST_LEVEL - 1:
            left = self.evaluate(level - 1)
            if self.match([TokenType.QUESTION]):
                left_operator = self.previous()
                middle = self.evaluate(level - 1)
                right_operator = Token(TokenType.COLON, ':')
                right = None
                if self.match([TokenType.COLON]):
                    right_operator = self.previous()
                    right = self.evaluate(level - 1)
                return Trinary(left, left_operator, middle, right_operator, right)
            return left
            
                
        
        elif level == LAST_LEVEL:
            left = self.evaluate(level - 1)
            if self.match(EXPRESSION_PRECEDENCE[level]):
                operator = self.previous()
                right = self.evaluate(level) 
                return Binary(left, operator, right)
            return left
            
            
        else:
            left = self.evaluate(level - 1)
            while self.match(EXPRESSION_PRECEDENCE[level]):
                operator = self.previous()
                right = self.evaluate(level - 1)
                left = Binary(left, operator, right)
            
            return left
    
    
    
    def match(self, types: set[Token]):
        if self.tokens[self.current].type in types:
            self.advance()
            return True
        return False



    def check(self, token_type: TokenType):
        if self.at_end(): return False
        return self.tokens[self.current].type == token_type



    def advance(self):
        if not self.at_end(): self.current += 1
        return self.previous()



    def previous(self):
        return self.tokens[self.current - 1]



    def at_end(self):
        return self.tokens[self.current].type in [TokenType.SEMICOLON, TokenType.EOF]
    