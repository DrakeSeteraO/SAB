import sys
sys.path.append("src")



import pytest
from tokentype import TokenType
from sab_token import Token
from expression_parser import Expression_Parser



def test_1():
    tokens = [Token(TokenType.INTEGER,'1','1'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.SEMICOLON,';')]
    
    tree = Expression_Parser(tokens).parse()
    assert str(tree) == '(+ 1 2)' 



def test_2():
    tokens = [Token(TokenType.INTEGER,'1','1'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.PLUS,'-'),
              Token(TokenType.INTEGER,'3','3'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'4','4'),              
              Token(TokenType.SEMICOLON,';')]
    
    tree = Expression_Parser(tokens).parse()
    assert str(tree) == '(+ (- (+ 1 2) 3) 4)' 
    
    
    
if __name__ == '__main__':
    test_1()
    test_2()