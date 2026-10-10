import sys
sys.path.append("src")



import pytest
from abstract_syntax_tree import *
from sab_token import Token



def test_AST_1():
    temp = Binary(
        Unary(
            Token(
                TokenType.MINUS, "-", None, 1, 1), 
            Literal(
                Token(
                    TokenType.INTEGER, "123","123", 1, 1))),
        Token(
            TokenType.STAR, "*", None, 1, 1),
        Grouping(
            Literal(
                Token(
                    TokenType.FLOATING_POINT, "45.67", "45.67", 1, 1))))
    
    # Standard Output
    assert str(temp) == '(* (- 123) (group 45.67))'
    
    # Reverse Polish Notation
    assert temp.RPN() == '123 .- 45.67 *'
    
    # Tree Visualized
    assert temp.display() == """Binary:
├── Expression:
│   ├── Unary:
│   ├── Operator: -
│   └── Expression:
│       └── Literal: 123
├── Operator: *
└── Expression:
    └── Grouping:
        └── Literal: 45.67"""



if __name__ == '__main__':
    test_AST_1()