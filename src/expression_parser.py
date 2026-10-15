


class Expression_Parser:
    def __init__(self, expression: str):
        if not isinstance(expression, str):
            raise TypeError
        self.expression = expression
    
    
    def parse(self):
        ...