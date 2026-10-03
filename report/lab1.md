# Lab 1: Scanning
**Language Name:** SAB (Subtract And Branch)

## By Drake Setera ##

## Language Overview and Design Choices
The language I am making is called SAB (Subtract And Branch). I designed it to eventually compile down to machine code for a SAB emulator that I plan to improve. 

When designing my scanner, I made a few changes compared to Lox:
* **Dictionary Mapping:** Instead of using large, nested switch or if/else statements to figure out token types, I separated my tokens into Python dictionaries based on their attributes (CHAR_TO_TOKEN, SPECIAL_CHAR_TO_TOKEN, DOUBLE_CHAR_TO_TOKEN, WORD_TO_TOKEN). This makes the scan() loop much cleaner. The scanner just checks if a character is in the keys of a dictionary and maps it to the TokenType Enum.
* **Column Tracking:** The Lox we talked about in class only tracks the line number for errors. I implemented column tracking (self.column) along with the line number so I know exactly where a token or error occurs on a line.
* **Comments:** I chose to use # for comments instead of // because I prefer the style of Python comments. 
* **Additional Keywords/Operators:** Because this is for a machine code emulator, I added explicit typing keywords (int, char, str, float, bin, hex, var), so in the future the compiler can detect accidental type mismatches and bitwise operators (&, |, ^, ~, <<, >>).

## Regular Expressions
Based on my lexical rules and the implementation in scanner.py, here are the regular expressions that define SAB's tokens:

* **Identifiers:** ^[a-zA-Z_]+$ 
* **Number Literals (Integer & Floating Point):** ^[0-9]+(\.[0-9]+)?$
* **String Literals:** ^([^\\])|(\\[^\\])$ 
* **Binary Literals:** ^0b[01]+$
* **Hexadecimal Literals:** ^0x[0-9A-Fa-f]+$

## Setup and Run Instructions
There are no external dependencies required for the SAB Compiler other than a standard Python 3 installation.

**To run Interactive Mode:**
Initialize the Terminal SAB Interpreter by running the following command from the root repository directory:
```bash
python src/SAB.py
```
*After running the command, you will see a >> symbol. You can type instructions and press enter. To exit, press Ctrl + C.*

**To run in Source-File Mode:**
Pass the file you want to compile as an argument. You can pass multiple files at once.
```bash
python src/SAB.py test/lab1/test_file.sab
```

## Test Cases

### Test Case 1: Variable Declarations & Literals
* **Purpose:** Verify the scanner correctly identifies keywords, identifiers, assignment operators, and numeric/string literals, specifically testing custom binary and hex literals.
* **Source Input:**
  ```sab
  int x = 21;
  char y = 'L';
  float zee = 123.4567;
  str hello_there = "How are you today?";
  bin wowza = 0b1101;
  hex lmao = 0x6A;
  ```
* **Expected Tokens:** Correct combinations of keywords (INT, CHAR, FLOAT, STR, BIN, HEX), identifiers, EQUAL, and specific literal types (INTEGER, CHARACTER, FLOATING_POINT, STRING, BINARY, HEXADECIMAL) followed by SEMICOLON's.
* **Actual Output:** The scanner correctly tokenized all keywords, variable names, and literals (including scientific types), capturing their exact string lexemes and values.
* **Matches Expectations:** Yes

### Test Case 2: Symbols and Operators
* **Purpose:** Test all single-character and double-character lexical operators and punctuation to ensure no greedy matching errors occur (e.g., ensuring <= is matched as one token instead of < and =).
* **Source Input:**
  ```sab
  ( ) { } [ ] , . ; @ $ : + - * / % < > ! = & | ^ ~
  ++ += -- -= *= /= %= << <= >> >= != == && &= || |= ^=
  ```
* **Expected Tokens:** LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE, LEFT_BRACKET, RIGHT_BRACKET, COMMA, DOT, SEMICOLON, ADDRESS, AT, COLON, PLUS, MINUS, STAR, SLASH, PERCENT, LESS, GREATER, BOOL_NOT, EQUAL, AND, OR, XOR, NOT, PLUS_PLUS, PLUS_EQUAL, MINUS_MINUS, MINUS_EQUAL, MULT_EQUAL, DIV_EQUAL, MOD_EQUAL, SHIFT_LEFT, LESS_EQUAL, SHIFT_RIGHT, GREATER_EQUAL, BOOL_NOT_EQUAL, EQUAL_EQUAL, AND_AND, AND_EQUAL, OR_OR, OR_EQUAL, XOR_EQUAL.
* **Actual Output:** Scanner properly parsed 1-character and 2-character tokens exactly as expected.
* **Matches Expectations:** Yes

### Test Case 3: Reserved Keywords
* **Purpose:** Verify all language keywords are properly mapped to their specific token types rather than being classified generally as standard identifiers.
* **Source Input:**
  ```sab
  NULL TRUE FALSE var char int str float bin hex void if elif else for while public private print return import from
  ```
* **Expected Tokens:** Direct matches to TokenType enum (e.g., NULL, TRUE, FALSE, VAR, CHAR, INT, STR, FLOAT, BIN, HEX, VOID, IF, ELIF, ELSE, FOR, WHILE, PUBLIC, PRIVATE, PRINT, RETURN, IMPORT, FROM).
* **Actual Output:** Identified every reserved word correctly via the WORD_TO_TOKEN dictionary check before falling back to identifiers.
* **Matches Expectations:** Yes

### Test Case 4: Comments Handling
* **Purpose:** Test single-line and enclosed comment handling, and ensure code immediately following or surrounding a comment is still accurately scanned.
* **Source Input:**
  ```sab
  # This is a really cool comment

  # This is a enclosed comment # int x = 67; # Another comment
  ```
* **Expected Tokens:** COMMENT tokens containing the comment bodies. For the second line, it should evaluate COMMENT, SPACE, INT, SPACE, IDENTIFIER, SPACE, EQUAL, SPACE, INTEGER, SEMICOLON, SPACE, COMMENT.
* **Actual Output:** The scanner correctly uses # as boundaries, extracts the comment into a COMMENT token, and immediately resumes normal scanning for the code.
* **Matches Expectations:** Yes

### Test Case 5: Strings, Characters, and Escape Sequences
* **Purpose:** Test character literals, string literals, and complex escape sequences (newlines, tabs, and ascii/bin/hex conversions).
* **Source Input:**
  ```sab
  char normal_char = 'a';
  char new_line_char = '\n';
  char tab_char = '\t';
  char int_ascii_char = '\76';
  char bin_ascii_char = '\0b101';
  char hex_ascii_char = '\0xAF';

  str normal_str = "This is a normal string";
  str new_line_str = "This is a string\nWith another line";
  str tab_str = "This is a string\tWith a tab";
  str int_str = "This is a string with int_ascii: \123";
  str bin_str = "This is a string with bin_ascii: \0b10000";
  str hex_str = "This is a string with hex_ascii: \0x1F";
  ```
* **Expected Tokens:** Proper identification of QUOTE/DOUBLE_QUOTE tokens, contents as STRING or CHARACTER, and escape segments dynamically broken down into ESCAPE tokens (\) followed by the exact type of literal being escaped (INTEGER, BINARY, HEXADECIMAL, or CHARACTER for n/t).
* **Actual Output:** Correctly split strings and characters around the \ symbol and evaluated all escape values properly based on their prefixes.
* **Matches Expectations:** Yes

## Known Limitations / Failing Tests
* **Identifier digits:** Currently, word_token() only loops while self.code[self.i].isalpha() or self.code[self.i] == '_'. If an identifier has a number in it (like var1), it will stop reading at the number. 
* **Bare Excepts:** In scanner.py, there are a few bare except: blocks. If a non-lexical error occurs in Python, it might get swallowed by these blocks instead of raising a clear syntax error to the user.


## Optional Extra Credit Features
I have included a few extra features beyond the basic scanner requirements:

1. **Scientific/Base Number Literals:** I added full support for Binary (0b1010) and Hexadecimal (0xFF) number literals. In get_escape_val(), the scanner detects the 0b or 0x prefix and adjusts the allowed character set and resulting TokenType accordingly.
2. **String Escape Sequences:** My string and character parsing handles escape sequences (like \n and \t). Instead of just ignoring the backslash, it explicitly breaks them out into TokenType.ESCAPE and TokenType.CHARACTER tokens so the compiler can handle them accurately later.
3. **Column Tracking:** As mentioned in the design choices, my Token class tracks both self.line and self.column. The scanner calculates the exact column offset (accounting for spaces and tabs adding 3 columns) to provide highly accurate location data for errors.