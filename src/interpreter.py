from tokentype import *
from sab_token import Token
from expression_parser import Expression_Parser
from expression_interpreter import Expression_Interpreter



class Interpreter:
    def __init__(self, tokens: list[Token], interpret_mode=False):
        self.tokens = tokens
        self.current = 0
        self.instructions = []
        self.interpret_mode = interpret_mode
    


    def parse(self):
        while not self.at_end():
            try:
                if self.match(STATEMENT_TOKEN):
                    self.evaluate_statement()
                else:
                    self.expression_statement()
            except (SyntaxError, ValueError) as e:
                print(f"Syntax Error: {e}")
                self.panic_mode()



    def panic_mode(self):
        self.advance()
        while not self.at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return
            if self.tokens[self.current].type in STATEMENT_TOKEN:
                return
            self.advance()
  
  
  
    def evaluate_statement(self):
        if self.previous().type == TokenType.PRINT:
            self.print_statement()
    
    
    
    def print_statement(self):
        parser = Expression_Parser(self.tokens[self.current:])
        tree, cur = parser.parse()
        self.current += cur
        _, result = Expression_Interpreter().get_expression(tree)
        
        if self.interpret_mode:
            if result is None:
                print('NULL')
            elif isinstance(result, bool):
                print('TRUE' if result else 'FALSE')
            else:
                print(result)
            
    
    
    def expression_statement(self):
        parser = Expression_Parser(self.tokens[self.current:])
        tree, cur = parser.parse()
        self.current += cur
        _, result = Expression_Interpreter().get_expression(tree)
    
    
           
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
        return self.tokens[self.current].type == TokenType.EOF