from tokentype import *
from sab_token import Token
from expression_parser import Expression_Parser
from expression_interpreter import Expression_Interpreter
from variable import Variable, Variable_Stack



class Interpreter:
    def __init__(self, tokens: list[Token], interpret_mode=False, variables: Variable_Stack = None):
        self.tokens = [t for t in tokens if t.type != TokenType.COMMENT]
        self.cur = 0
        self.instructions = []
        self.interpret_mode = interpret_mode
        self.variables = variables if variables is not None else Variable_Stack()
    


    def parse(self):
        while not self.at_end():
            if self.match({TokenType.SEMICOLON}):
                continue
            try:
                if self.match(STATEMENT_TOKEN):
                    self.evaluate_statement()
                else:
                    self.expression_statement()
            except SyntaxError as e:
                print(f"Syntax Error: {e}")
                self.panic_mode()
            except ValueError as e:
                print(f"Runtime Error: {e}")



    def panic_mode(self):
        self.advance()
        while not self.at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return
            if self.tokens[self.cur].type in STATEMENT_TOKEN or self.tokens[self.cur].type == TokenType.RIGHT_BRACE:
                return
            self.advance()
  
  
  
    def evaluate_statement(self):
        if self.previous().type == TokenType.PRINT:
            self.print_statement()
        elif self.previous().type == TokenType.LEFT_BRACE:
            self.block_statement()
        elif self.previous().type in {TokenType.VAR,
            TokenType.INT,
            TokenType.CHAR,
            TokenType.STR,
            TokenType.FLOAT,
            TokenType.HEX,
            TokenType.BIN}:
            self.variable_declaration()
    
    
    
    def print_statement(self):
        parser = Expression_Parser(self.tokens[self.cur:])
        tree, cur = parser.parse()
        self.cur += cur
        _, result = Expression_Interpreter(self.variables).get_expression(tree)
        if isinstance(result, Variable):
            result = result.value
        
        if self.interpret_mode:
            if result is None:
                print('NULL')
            elif isinstance(result, bool):
                print('TRUE' if result else 'FALSE')
            else:
                print(result)
            
    
    
    def variable_declaration(self):
        var_type = self.previous()
        identifier = self.current()
        if identifier.type != TokenType.IDENTIFIER:
            raise SyntaxError(f"Expected variable name at line {identifier.line}, column {identifier.column}")
        self.advance()
        result = None
        if self.match({TokenType.EQUAL}):
            parser = Expression_Parser(self.tokens[self.cur:])
            tree, cur = parser.parse()
            self.cur += cur
            _, result = Expression_Interpreter(self.variables).get_expression(tree)
            if isinstance(result, Variable):
                result = result.value
        else:
            self.match({TokenType.SEMICOLON})
        self.variables.declare(var_type, identifier)
        self.variables.set_value(identifier, result)
    
    
    
    def expression_statement(self):
        parser = Expression_Parser(self.tokens[self.cur:])
        tree, cur = parser.parse()
        self.cur += cur
        _, result = Expression_Interpreter(self.variables).get_expression(tree)
    
    
    
    def block_statement(self):
        self.variables.enter_block()
        try:
            while not self.check(TokenType.RIGHT_BRACE) and not self.at_end():
                if self.match({TokenType.SEMICOLON}):
                    continue
                try:
                    if self.match(STATEMENT_TOKEN):
                        self.evaluate_statement()
                    else:
                        self.expression_statement()
                except SyntaxError as e:
                    print(f"Syntax Error: {e}")
                    self.panic_mode()
                except ValueError as e:
                    print(f"Runtime Error: {e}")
            
            if not self.match({TokenType.RIGHT_BRACE}):
                cur_token = self.current()
                raise SyntaxError(f"Expected '}}' at line {cur_token.line}, column {cur_token.column}")
        finally:
            self.variables.exit_block()
            
            
           
    def match(self, types: set[Token]):
        if self.tokens[self.cur].type in types:
            self.advance()
            return True
        return False



    def check(self, token_type: TokenType):
        if self.at_end(): return False
        return self.tokens[self.cur].type == token_type



    def advance(self):
        if not self.at_end(): self.cur += 1
        return self.previous()



    def previous(self):
        return self.tokens[self.cur - 1]
    
    
    
    def current(self):
            return self.tokens[self.cur]



    def at_end(self):
        return self.tokens[self.cur].type == TokenType.EOF