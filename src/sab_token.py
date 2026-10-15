from tokentype import TokenType


class Token:
    def __init__(self, tokentype: TokenType, lexeme: str, literal = None, line: int = 0, column: int = 0):
        self.type = tokentype
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        self.column = column

    def to_string(self):
        return (
            f"<Token> | {self.type} | {self.lexeme} | {self.literal} | {self.line} | {self.column}"
        )

    def __str__(self):
        return self.to_string()