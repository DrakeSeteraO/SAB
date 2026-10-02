from enum import Enum, auto



class TokenType(Enum):
    
    # Grouping
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()

    # White space
    SPACE = auto()
    NEW_LINE = auto()
    TAB = auto()

    # Single-character
    EQUAL = auto()
    PLUS = auto()
    MINUS = auto()
    ADDRESS = auto()
    AT = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    COLON = auto()

    # Two-character
    PLUS_PLUS = auto()
    MINUS_MINUS = auto()
    SHIFT_LEFT = auto()
    SHIFT_RIGHT = auto()

    # Comparison
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    BOOL_NOT_EQUAL = auto()
    EQUAL_EQUAL = auto()

    # Boolean
    GREATER = auto()
    LESS = auto()
    BOOL_NOT = auto()
    AND_AND = auto()
    OR_OR = auto()
    
    # Bitwise
    NOT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()

    # Assignments
    PLUS_EQUAL = auto()
    MINUS_EQUAL = auto()
    MULT_EQUAL = auto()
    DIV_EQUAL = auto()
    XOR_EQUAL = auto()
    MOD_EQUAL = auto()
    OR_EQUAL = auto()
    AND_EQUAL = auto()

    # Types
    IDENTIFIER = auto()
    CHAR = auto()
    STR = auto()
    INT = auto()
    FLOAT = auto()
    NULL = auto()
    VAR = auto()
    VOID = auto()

    # Literals
    INTEGER = auto()
    FLOATING_POINT = auto()
    CHARACTER = auto()
    STRING = auto()
    BINARY = auto()
    HEXADECIMAL = auto()

    # Booleans
    TRUE = auto()
    FALSE = auto()

    # Keywords
    IF = auto()
    ELIF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    PRINT = auto()
    RETURN = auto()
    IMPORT = auto()
    FROM = auto()
    PUBLIC = auto()
    PRIVATE = auto()

    # Punctuation
    COMMA = auto()
    DOT = auto()
    SEMICOLON = auto()
    QUOTE = auto()
    DOUBLE_QUOTE = auto()
    HASH_TAG = auto()
    
    # Escape
    ESCAPE = auto()
    
    # End of File
    EOF = auto()



CHAR_TO_TOKEN = {
    ' ' : TokenType.SPACE,
    '\n' : TokenType.NEW_LINE,
    '\t' : TokenType.TAB,
    '(' : TokenType.LEFT_PAREN,
    ')' : TokenType.RIGHT_PAREN,
    '{' : TokenType.LEFT_BRACE,
    '}' : TokenType.RIGHT_BRACE,
    '[' : TokenType.LEFT_BRACKET,
    ']' : TokenType.RIGHT_BRACKET,
    ',' : TokenType.COMMA,
    '.' : TokenType.DOT,
    ';' : TokenType.SEMICOLON,
    '@' : TokenType.ADDRESS,
    '$' : TokenType.AT,
    ':' : TokenType.COLON
}



SPECIAL_CHAR_TO_TOKEN = {
    '+' : TokenType.PLUS,
    '-' : TokenType.MINUS,
    '*' : TokenType.STAR,
    '/' : TokenType.SLASH,
    '%' : TokenType.PERCENT,
    '<' : TokenType.LESS,
    '>' : TokenType.GREATER,
    '!' : TokenType.BOOL_NOT,
    '=' : TokenType.EQUAL,
    '&' : TokenType.AND,
    '|' : TokenType.OR,
    '^' : TokenType.XOR,
    '~' : TokenType.NOT,
}



DOUBLE_CHAR_TO_TOKEN = {
    '++' : TokenType.PLUS_PLUS,
    '+=' : TokenType.PLUS_EQUAL,
    '--' : TokenType.MINUS_MINUS,
    '-=' : TokenType.MINUS_EQUAL,
    '*=' : TokenType.MULT_EQUAL,
    '/=' : TokenType.DIV_EQUAL,
    '%=' : TokenType.MOD_EQUAL,
    '<<' : TokenType.SHIFT_LEFT,
    '<=' : TokenType.LESS_EQUAL,
    '>>' : TokenType.SHIFT_RIGHT,
    '>=' : TokenType.GREATER_EQUAL,
    '!=' : TokenType.BOOL_NOT_EQUAL,
    '==' : TokenType.EQUAL_EQUAL,
    '&&' : TokenType.AND_AND,
    '&=' : TokenType.AND_EQUAL,
    '||' : TokenType.OR_OR,
    '|=' : TokenType.OR_EQUAL,
    '^=' : TokenType.XOR_EQUAL
}



WORD_TO_TOKEN = {
    'NULL' : TokenType.NULL,
    'TRUE' : TokenType.TRUE,
    'FALSE' : TokenType.FALSE,
    'var' : TokenType.VAR,
    'char' : TokenType.CHAR,
    'int' : TokenType.INT,
    'str' : TokenType.STR,
    'float' : TokenType.FLOAT,
    'void' : TokenType.VOID,
    'if' : TokenType.IF,
    'elif' : TokenType.ELIF,
    'else' : TokenType.ELSE,
    'for' : TokenType.FOR,
    'while' : TokenType.WHILE,
    'public' : TokenType.PUBLIC,
    'private' : TokenType.PRIVATE,
    'print' : TokenType.PRINT,
    'return' : TokenType.RETURN,
    'import' : TokenType.IMPORT,
    'from' : TokenType.FROM
}

RESERVED_WORDS = [w for w in WORD_TO_TOKEN.keys()]