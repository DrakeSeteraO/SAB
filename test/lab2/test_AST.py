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
#     # Tree Visualized
    assert temp.display() == """Binary:
├── Expression:
│   └── Unary:
│       ├── Operator: -
│       └── Expression:
│           └── Literal: 123
├── Operator: *
└── Expression:
    └── Grouping:
            └── Literal: 45.67"""



def test_AST_2():
    temp = Binary(
        Literal(
            Token(
                TokenType.INTEGER, "10", "10", 1, 1)),
        Token(
            TokenType.PLUS, "+", None, 1, 4),
        Literal(
            Token(
                TokenType.INTEGER, "20", "20", 1, 6)))

    # Standard Output
    assert str(temp) == '(+ 10 20)'
    
    # Reverse Polish Notation
    assert temp.RPN() == '10 20 +'

    # Tree Visualized
    assert temp.display() == """Binary:
├── Expression:
│   └── Literal: 10
├── Operator: +
└── Expression:
    └── Literal: 20"""



def test_AST_3():
    temp = Binary(
        Literal(
            Token(
                TokenType.INTEGER, "1", "1", 1, 1)),
        Token(
            TokenType.PLUS, "+", None, 1, 3),
        Binary(
            Literal(
                Token(
                    TokenType.INTEGER, "2", "2", 1, 5)),
            Token(
                TokenType.STAR, "*", None, 1, 7),
            Literal(
                Token(
                    TokenType.INTEGER, "3", "3", 1, 9))))
    
    # Standard Output
    assert str(temp) == '(+ 1 (* 2 3))'
    
    # Reverse Polish Notation
    assert temp.RPN() == '1 2 3 * +'
    
    # Tree Visualized
    assert temp.display() == """Binary:
├── Expression:
│   └── Literal: 1
├── Operator: +
└── Expression:
    └── Binary:
        ├── Expression:
        │   └── Literal: 2
        ├── Operator: *
        └── Expression:
            └── Literal: 3"""
    


def test_AST_4():
    temp = Unary(
        Token(
            TokenType.BOOL_NOT, "!", None, 1, 1),
        Grouping(
            Binary(
                Literal(
                    Token(
                        TokenType.INTEGER, "5", "5", 1, 3)),
                Token(
                    TokenType.GREATER, ">", None, 1, 5),
                Literal(
                    Token(
                        TokenType.INTEGER, "3", "3", 1, 7)))))

    # Standard Output
    assert str(temp) == '(! (group (> 5 3)))'
    
    # Reverse Polish Notation
    assert temp.RPN() == '5 3 > .!'
    
    # Tree Visualized
    assert temp.display() == """Unary:
├── Operator: !
└── Expression:
    └── Grouping:
        └── Binary:
        ├── Expression:
        │   └── Literal: 5
        ├── Operator: >
        └── Expression:
            └── Literal: 3"""



def test_AST_5():
    temp = Binary(
        Literal(
            Token(
                TokenType.STRING, '"hello"', "hello", 1, 1)),
        Token(
            TokenType.EQUAL_EQUAL, "==", None, 1, 9),
        Literal(
            Token(
                TokenType.STRING, '"world"', "world", 1, 12)))

    # Standard Output
    assert str(temp) == '(== "hello" "world")'
    
    # Reverse Polish Notation
    assert temp.RPN() == '"hello" "world" =='
    
    # Tree Visualized
    assert temp.display() == """Binary:
├── Expression:
│   └── Literal: "hello"
├── Operator: ==
└── Expression:
    └── Literal: """ + '"world"'



if __name__ == '__main__':
    test_AST_1()
    test_AST_2()
    test_AST_3()
    test_AST_4()
    test_AST_5()