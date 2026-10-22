from enum import Enum, auto



class TokenType(Enum):
    
    # Grouping
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()

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
    QUESTION = auto()

    # Two-character
    PLUS_PLUS = auto()
    MINUS_MINUS = auto()
    SHIFT_LEFT = auto()
    SHIFT_RIGHT = auto()
    STAR_STAR = auto()

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
    HEX = auto()
    BIN = auto()
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
    
    # Comment
    COMMENT = auto()
    
    # Escape
    ESCAPE = auto()
    
    # End of File
    EOF = auto()



CHAR_TO_TOKEN = {
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
    ':' : TokenType.COLON,
    '?' : TokenType.QUESTION
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
    '^=' : TokenType.XOR_EQUAL,
    '**' : TokenType.STAR_STAR
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
    'bin' : TokenType.BIN,
    'hex' : TokenType.HEX,
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



LITERAL_TYPES = {
    TokenType.NULL,
    TokenType.TRUE,
    TokenType.FALSE,
    TokenType.INTEGER,
    TokenType.FLOATING_POINT,
    TokenType.CHARACTER,
    TokenType.STRING,
    TokenType.BINARY,
    TokenType.HEXADECIMAL,
    TokenType.IDENTIFIER
}



OPERATOR_VAL_TYPE = {
    TokenType.PLUS: (int, float, str),
    TokenType.MINUS: (int, float),
    TokenType.STAR: (int, float),
    TokenType.SLASH: (int, float),
    TokenType.PERCENT: (int, float),
    TokenType.LESS: (int, float),
    TokenType.GREATER: (int, float),
    TokenType.GREATER_EQUAL: (int, float), 
    TokenType.LESS_EQUAL: (int, float),
    TokenType.BOOL_NOT_EQUAL: (int, float, str, bool),
    TokenType.AND: int,
    TokenType.OR: int,
    TokenType.XOR: int,
    TokenType.SHIFT_LEFT: int,
    TokenType.SHIFT_RIGHT: int,
    TokenType.EQUAL_EQUAL: (int, float, str, bool),
    TokenType.AND_AND: bool,
    TokenType.OR_OR: bool,
    TokenType.EQUAL: (int, float, str, bool),
    TokenType.PLUS_EQUAL: (int, float),
    TokenType.MINUS_EQUAL: (int, float),
    TokenType.MULT_EQUAL: (int, float),
    TokenType.DIV_EQUAL: (int, float),
    TokenType.MOD_EQUAL: (int, float),
    TokenType.XOR_EQUAL: int,
    TokenType.OR_EQUAL: int,
    TokenType.AND_EQUAL: int,
    TokenType.STAR_STAR: (int, float)
}



from operations import *



UNARY_OPERATIONS = {
    TokenType.PLUS: python_unary,
    TokenType.PLUS_PLUS: plus_plus,
    TokenType.MINUS: python_unary,
    TokenType.MINUS_MINUS: minus_minus,
    TokenType.NOT: python_unary,
    TokenType.BOOL_NOT: bool_not,
    TokenType.ADDRESS: None,
    TokenType.AT: None,
}



BINARY_OPERATIONS = {
    TokenType.PLUS: python_binary,
    TokenType.MINUS: python_binary,
    TokenType.STAR: python_binary,
    TokenType.SLASH: python_binary,
    TokenType.PERCENT: python_binary,
    TokenType.LESS: python_binary,
    TokenType.GREATER: python_binary,
    TokenType.GREATER_EQUAL: python_binary, 
    TokenType.LESS_EQUAL: python_binary,
    TokenType.BOOL_NOT_EQUAL: python_binary,
    TokenType.AND: python_binary,
    TokenType.OR: python_binary,
    TokenType.XOR: python_binary,
    TokenType.SHIFT_LEFT: python_binary,
    TokenType.SHIFT_RIGHT: python_binary,
    TokenType.EQUAL_EQUAL: python_binary,
    TokenType.AND_AND: bool_and,
    TokenType.OR_OR: bool_or,
    TokenType.EQUAL: equal_assign,
    TokenType.PLUS_EQUAL: op_assign,
    TokenType.MINUS_EQUAL: op_assign,
    TokenType.MULT_EQUAL: op_assign,
    TokenType.DIV_EQUAL: op_assign,
    TokenType.MOD_EQUAL: op_assign,
    TokenType.XOR_EQUAL: op_assign,
    TokenType.OR_EQUAL: op_assign,
    TokenType.AND_EQUAL: op_assign,
    TokenType.STAR_STAR: python_binary
}



EXPRESSION_PRECEDENCE = [
    {
        # Special Cases
        TokenType.LEFT_PAREN,
        TokenType.RIGHT_PAREN,
        TokenType.LEFT_BRACE,
        TokenType.RIGHT_BRACE,
        TokenType.DOT
    },
    {
        # Unary Operators
        TokenType.PLUS_PLUS,
        TokenType.MINUS_MINUS,
        TokenType.PLUS,
        TokenType.MINUS,
        TokenType.NOT,
        TokenType.BOOL_NOT,
        TokenType.ADDRESS,
        TokenType.AT
    },
    {
        TokenType.STAR_STAR  
    },
    {
        TokenType.STAR,
        TokenType.SLASH, 
        TokenType.PERCENT
    },
    {
        TokenType.PLUS,
        TokenType.MINUS,
    },
    {
        TokenType.SHIFT_LEFT,
        TokenType.SHIFT_RIGHT
    },
    {
        TokenType.AND  
    },
    {
        TokenType.XOR
    },
    {
        TokenType.OR  
    },
    {
        TokenType.LESS,
        TokenType.LESS_EQUAL, 
        TokenType.GREATER, 
        TokenType.GREATER_EQUAL,
        TokenType.EQUAL_EQUAL, 
        TokenType.BOOL_NOT_EQUAL
    },
    {
        TokenType.BOOL_NOT
    },
    {
        TokenType.AND_AND
    },
    {
        TokenType.OR_OR
    },
    {
        TokenType.QUESTION,
        TokenType.COLON  
    },
    {
        TokenType.EQUAL,
        TokenType.PLUS_EQUAL, 
        TokenType.MINUS_EQUAL,
        TokenType.MULT_EQUAL,
        TokenType.DIV_EQUAL, 
        TokenType.MOD_EQUAL,
        TokenType.XOR_EQUAL,
        TokenType.OR_EQUAL,
        TokenType.AND_EQUAL
    }    
]