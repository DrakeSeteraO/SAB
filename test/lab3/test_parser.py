import sys
sys.path.append("src")



import pytest
from tokentype import TokenType
from sab_token import Token
from parser import Parser



def test_1():
    # 1 + 2;
    tokens = [Token(TokenType.INTEGER,'1','1'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.SEMICOLON,';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(+ 1 2)' 
    
    from interpreter import Interpreter
    op = Interpreter()
    print(op.get_expression(tree))



def test_2():
    # 1 + 2 - 3 + 4;
    tokens = [Token(TokenType.INTEGER,'1','1'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.PLUS,'-'),
              Token(TokenType.INTEGER,'3','3'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'4','4'),              
              Token(TokenType.SEMICOLON,';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(+ (- (+ 1 2) 3) 4)' 
    
    

def test_3():
    # -(5 / 2) * 2 + 50;
    tokens = [Token(TokenType.NOT,'~'),
              Token(TokenType.LEFT_PAREN,'('),
              Token(TokenType.INTEGER,'5','5'),
              Token(TokenType.SLASH,'/'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.RIGHT_PAREN,')'),
              Token(TokenType.STAR,'*'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.PLUS,'+'),       
              Token(TokenType.INTEGER,'50','50'),                     
              Token(TokenType.SEMICOLON,';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(+ (* (~ (group (/ 5 2))) 2) 50)' 
    
    
 
def test_4():
    # 10 >= 5 == true;
    tokens = [Token(TokenType.INTEGER, '10', '10'),
              Token(TokenType.GREATER_EQUAL, '>='),
              Token(TokenType.INTEGER, '5', '5'),
              Token(TokenType.EQUAL_EQUAL, '=='),
              Token(TokenType.TRUE, 'true', 'true'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(== (>= 10 5) true)'



def test_5():
    # 1 << 2 | 3 & 4;
    tokens = [Token(TokenType.INTEGER, '1', '1'),
              Token(TokenType.SHIFT_LEFT, '<<'),
              Token(TokenType.INTEGER, '2', '2'),
              Token(TokenType.OR, '|'),
              Token(TokenType.INTEGER, '3', '3'),
              Token(TokenType.AND, '&'),
              Token(TokenType.INTEGER, '4', '4'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(| (<< 1 2) (& 3 4))'



def test_6():
    # !true && false || x;
    tokens = [Token(TokenType.BOOL_NOT, '!'),
              Token(TokenType.TRUE, 'true', 'true'),
              Token(TokenType.AND_AND, '&&'),
              Token(TokenType.FALSE, 'false', 'false'),
              Token(TokenType.OR_OR, '||'),
              Token(TokenType.IDENTIFIER, 'x', 'x'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(|| (&& (! true) false) x)'



def test_7():
    # a = b = 10;
    tokens = [Token(TokenType.IDENTIFIER, 'a', 'a'),
              Token(TokenType.EQUAL, '='),
              Token(TokenType.IDENTIFIER, 'b', 'b'),
              Token(TokenType.EQUAL, '='),
              Token(TokenType.INTEGER, '10', '10'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(= a (= b 10))'



def test_8():
    # -5 - -3;
    # Validates that Unary negative and Binary subtraction context does not conflict
    tokens = [Token(TokenType.MINUS, '-'),
              Token(TokenType.INTEGER, '5', '5'),
              Token(TokenType.MINUS, '-'),
              Token(TokenType.MINUS, '-'),
              Token(TokenType.INTEGER, '3', '3'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(- (- 5) (- 3))'


def test_9():
    # x == 3 ? 1 + 2 + 3 : 32 / 5 + 1;
    tokens = [Token(TokenType.IDENTIFIER, 'x', 'x'),
              Token(TokenType.EQUAL_EQUAL, '=='),
              Token(TokenType.INTEGER, '3', '3'),
              Token(TokenType.QUESTION, '?'),
              Token(TokenType.INTEGER, '1', '1'),
              Token(TokenType.PLUS, '+'),
              Token(TokenType.INTEGER, '2', '2'),
              Token(TokenType.PLUS, '+'),
              Token(TokenType.INTEGER, '3', '3'),
              Token(TokenType.COLON, ':'),
              Token(TokenType.INTEGER, '32', '32'),
              Token(TokenType.SLASH, '/'),
              Token(TokenType.INTEGER, '5', '5'),
              Token(TokenType.PLUS, '+'),
              Token(TokenType.INTEGER, '1', '1'),
              Token(TokenType.SEMICOLON, ';')]
    
    tree = Parser(tokens).parse()
    assert str(tree) == '(? (== x 3) (+ (+ 1 2) 3) (+ (/ 32 5) 1))'



if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()   
    test_9()    