import sys
sys.path.append("src")



import pytest
from tokentype import TokenType
from sab_token import Token
from expression_parser import Expression_Parser



def test_1():
    # 1 + 2;
    tokens = [Token(TokenType.INTEGER,'1','1'),
              Token(TokenType.PLUS,'+'),
              Token(TokenType.INTEGER,'2','2'),
              Token(TokenType.SEMICOLON,';')]
    
    tree = Expression_Parser(tokens).parse()
    assert str(tree) == '(+ 1 2)' 



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
    
    tree = Expression_Parser(tokens).parse()
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
    
    tree = Expression_Parser(tokens).parse()
    assert str(tree) == '(+ (* (~ (group (/ 5 2))) 2) 50)' 
    
    
        
if __name__ == '__main__':
    test_1()
    test_2()
    test_3()