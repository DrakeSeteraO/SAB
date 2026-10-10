from tokentype import TokenType, CHAR_TO_TOKEN, SPECIAL_CHAR_TO_TOKEN, DOUBLE_CHAR_TO_TOKEN, WORD_TO_TOKEN, RESERVED_WORDS
from sab_token import Token



class Scanner:
    def __init__(self, compile_mode: bool = True):
        if isinstance(compile_mode, bool):
            self.compile_mode = compile_mode
        else:
            raise TypeError('compile_mode must be a boolean')
        self.i = 0
        self.line = 1
        self.column = 1
        
        self.tokens = []
        self.total_tokens = []



    def increment(self, num=1):
        self.i += num
        self.column += num
    
    
    
    def scan(self, code: str = ''):
        if not isinstance(code, str):
            raise TypeError
        
        self.code = code
        self.i = 0
        self.column = 1

        while self.i < len(self.code):
            if self.code[self.i] == '#':
                self.comment_token()
            
            elif self.code[self.i] in [' ', '\n', '\t']:
                if self.code[self.i] == '\n':
                    self.line += 1
                    self.column = 0
                elif self.code[self.i] == '\t':
                    self.column += 2
                self.increment()
            
            elif self.code[self.i] in CHAR_TO_TOKEN.keys():
                self.char_token()
            
            elif self.code[self.i] in SPECIAL_CHAR_TO_TOKEN.keys():
                self.special_char_token()
            
            elif self.code[self.i] == "'":
                self.character_token()
            
            elif self.code[self.i] == '"':
                self.string_token()
            
            elif self.code[self.i].isdigit():
                self.number_token()
            
            else:
                self.word_token()
        
        self.tokens.append(Token(tokentype=TokenType.EOF,
                                 lexeme=None,
                                 literal=None,
                                 line=self.line,
                                 column=self.column))
        self.total_tokens += self.tokens
        return self.tokens
       
       
    
    def comment_token(self):
        var = self.code[self.i]
        start = self.i
        self.increment()
        try:
            while not self.code[self.i] in ['#', '\n']:
                var += self.code[self.i]
                self.increment()
                
            if self.code[self.i] == '#':
                var += self.code[self.i]
                self.increment()
                
            self.tokens.append(Token(tokentype=TokenType.COMMENT,
                                    lexeme=var,
                                    literal=None,
                                    line=self.line,
                                    column=start))
        except Exception as e:
            print(e)
            raise IndexError
    
    
                
    def char_token(self):
        cur_token = Token(tokentype=CHAR_TO_TOKEN[self.code[self.i]], 
                            lexeme=self.code[self.i], 
                            literal=None, 
                            line=self.line, 
                            column=self.column)
        self.tokens.append(cur_token)
        self.increment()
    
    
    
    def special_char_token(self):
        try:
            if self.code[self.i:self.i+2] in DOUBLE_CHAR_TO_TOKEN.keys():
                self.tokens.append(
                    Token(tokentype=DOUBLE_CHAR_TO_TOKEN[self.code[self.i:self.i+2]],
                            lexeme=self.code[self.i:self.i+2], 
                            literal=None, 
                            line=self.line, 
                            column=self.column)
                    )
                self.increment(2)
                
            else:
                self.tokens.append(
                    Token(tokentype=SPECIAL_CHAR_TO_TOKEN[self.code[self.i]],
                            lexeme=self.code[self.i], 
                            literal=None, 
                            line=self.line, 
                            column=self.column)
                    )
                self.increment()
                
        except:
            self.total_tokens.append(
                Token(tokentype=SPECIAL_CHAR_TO_TOKEN[self.code[self.i]], 
                        lexeme=self.code[self.i],
                        literal=None,
                        line=self.line,
                        column=self.column)
                )
            self.increment()
    
    
    
    def character_token(self):
        try:
            if self.code[self.i+2] == "'":
                temp = [
                    Token(tokentype=TokenType.QUOTE, 
                        lexeme="'",
                        literal=None,
                        line=self.line,
                        column=self.column),
                    Token(tokentype=TokenType.CHARACTER, 
                        lexeme=self.code[self.i+1],
                        literal=self.code[self.i+1],
                        line=self.line,
                        column=self.column+1),
                    Token(tokentype=TokenType.QUOTE, 
                        lexeme="'",
                        literal=None,
                        line=self.line,
                        column=self.column+2)                                                  
                ]
                self.tokens += temp
                self.i += 3
                if self.code[self.i-2] == '\n':
                    self.line += 1
                    self.column = 2
                elif self.code[self.i-2] == '\t':
                    self.column += 6
                else:
                    self.column += 3
            elif self.code[self.i+1] == '\\':
                temp = [
                    Token(tokentype=TokenType.QUOTE, 
                        lexeme="'",
                        literal=None,
                        line=self.line,
                        column=self.column),
                    Token(tokentype=TokenType.ESCAPE, 
                        lexeme='\\',
                        literal=None,
                        line=self.line,
                        column=self.column+1)                                                 
                ]
                self.increment(2)
                temp += [self.get_escape_val()]
                if self.code[self.i] == "'":
                    temp += Token(tokentype=TokenType.QUOTE, 
                                lexeme="'",
                                literal=None,
                                line=self.line,
                                column=self.column),
                    self.increment()
                else:
                    raise KeyError
                self.tokens += temp
            else:
                raise KeyError
        except:
            raise TypeError
    
    
    
    def get_escape_val(self):
        try:
            if self.code[self.i] in {'n', 't'}:
                temp = Token(tokentype=TokenType.CHARACTER,
                            lexeme=self.code[self.i],
                            literal=self.code[self.i],
                            line=self.line,
                            column=self.column)
                self.increment()
                return temp
            
            binary = {'0', '1'}
            hex = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
            select = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
            val = ''
            start = self.i
            temp_token = TokenType.INTEGER
            
            if self.code[self.i:self.i+2] == '0b':
                select = binary
                temp_token = TokenType.BINARY 
                self.increment(2)
                
            elif self.code[self.i:self.i+2] == '0x':
                select = hex
                temp_token = TokenType.HEXADECIMAL
                self.increment(2)
                
            while self.code[self.i].upper() in select:
                val += self.code[self.i].upper()
                self.increment()
            return Token(tokentype=temp_token,
                            lexeme=val,
                            literal=val,
                            line=self.line,
                            column=self.column - (self.i - start))
        except:
            raise IndexError
       
       
    
    def string_token(self):
        try:
            temp = [Token(tokentype=TokenType.DOUBLE_QUOTE,
                        lexeme='"',
                        literal=None,
                        line=self.line,
                        column=self.column)]    
            self.increment()
            string = ""
            start_column = self.column
            while self.code[self.i] != '"' and self.i < len(self.code):
                if self.code[self.i] == '\\':
                    temp += [Token(tokentype=TokenType.STRING,
                                lexeme=string,
                                literal=string,
                                line=self.line,
                                column=start_column),
                            Token(tokentype=TokenType.ESCAPE,
                                lexeme='\\',
                                literal=None,
                                line=self.line,
                                column=self.column)]
                    self.increment()
                    temp += [self.get_escape_val()]
                    string = ''
                    start_column = self.column
                else:
                    string += self.code[self.i]
                    self.increment()
            if self.i >= len(self.code):
                raise ValueError("Unterminated String")
            temp += [Token(tokentype=TokenType.STRING,
                           lexeme=string,
                           literal=string,
                           line=self.line,
                           column=start_column),
                     Token(tokentype=TokenType.DOUBLE_QUOTE,
                           lexeme='"',
                           literal=None,
                           line=self.line,
                           column=self.column)]
            self.increment()
            self.tokens += temp
                    
        except:
            raise IndexError
    


    def number_token(self):
        cur_token = self.get_escape_val()
        if self.code[self.i] == '.' and cur_token.type == TokenType.INTEGER:
            val = '.'
            self.increment()
            while self.code[self.i].isdigit():
                val += self.code[self.i]
                self.increment()
            cur_token = Token(tokentype=TokenType.FLOATING_POINT,
                              lexeme=cur_token.lexeme+val,
                              literal=cur_token.literal+val,
                              line=cur_token.line,
                              column=cur_token.column)
        self.tokens.append(cur_token)
    
    
    
    def word_token(self):
        for word in RESERVED_WORDS:
            try:
                if self.code[self.i:self.i+len(word)] == word and not self.code[self.i+len(word)].isalnum():
                    self.tokens.append(Token(WORD_TO_TOKEN[word],
                                             lexeme=word,
                                             literal=None,
                                             line=self.line,
                                             column=self.column))
                    self.increment(len(word))
                    return
            except:
                pass
        
        if not (self.code[self.i].isalnum() or self.code[self.i] == '_'):
            raise ValueError
        
        start = self.i
        val = ''
        try:
            while self.code[self.i].isalpha() or self.code[self.i] == '_':
                val += self.code[self.i]
                self.increment()
        except:
            pass
        
        self.tokens.append(Token(tokentype=TokenType.IDENTIFIER,
                                 lexeme=val,
                                 literal=val,
                                 line=self.line,
                                 column=start))