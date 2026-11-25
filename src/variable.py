from tokentype import TokenType
from sab_token import Token



class Variable:
    def __init__(self, token: Token, type: TokenType, identifier: str, value = None):
        self.token = token
        self.type = type
        self.identifier = identifier
        self.value = value



class Variable_Stack():
    def __init__(self):
        self.stack = [{}]
    
    
    def declare(self, type: Token, identifier: Token):
        if identifier.literal in self.stack[-1].keys():
            raise Exception(f"Variable '{identifier.literal}' already exists")
        self.stack[-1][identifier.literal] = Variable(identifier, type.type, identifier.literal)
    
    
    def enter_block(self):
        self.stack += [{}]
    
    
    def exit_block(self):
        if len(self.stack) > 1:
            self.stack.pop(-1)
    
    
    def get_value(self, identifier: Token):
        ptr = self.find_ptr(identifier)
        return self.stack[ptr][identifier.literal].value
    
    
    def get_variable(self, identifier: Token):
        ptr = self.find_ptr(identifier)
        return self.stack[ptr][identifier.literal]
    
    
    def set_value(self, identifier: Token, value=None):
        ptr = self.find_ptr(identifier)
        self.stack[ptr][identifier.literal].value = value
    
    
    def find_ptr(self, identifier: Token):
        ptr = len(self.stack) - 1
        while ptr >= 0 and not identifier.literal in self.stack[ptr].keys():
            ptr -= 1
        
        if ptr < 0:
            raise ValueError(f"Variable '{identifier.literal}' does not exist")
        
        return ptr