# Lab 2 Report: AST Printer

## By Drake Setera ##

## 1. Expression Grammar and Design Choices
My language's grammar expands upon the Lox structure, supporting a wide range of types including standard arithmetic, bitwise operations, logical comparisons, and complex literals (such as binary and hexadecimal).

**Grammar Definition:**
- expression -> literal | unary | binary | grouping ;
- literal    -> INTEGER | FLOATING_POINT | CHARACTER | STRING | BINARY | HEXADECIMAL | "NULL" | "TRUE" | "FALSE" | IDENTIFIER ;
- grouping   -> "(" expression ")" ;
- unary      -> ( "-" | "--" | "+" | "++" | "!" | "~" | "@" | "$" ) ;expression 
- binary     -> expression operator expression ;
- operator   -> "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" | "%" | "&&" | "||" | "&" | "|" | "^" | "<<" | ">>" ;

**Design Choices Relative to Lox:**
*   **Strict Type-Checking:** While the overall AST structure uses standard nodes (Binary,  Unary, Literal , and  Grouping), my implementation enforces strict operator and literal validation. By using Python's isinstance() and checking TokenType sets I have made; LITERAL_TYPES, UNARY_OPERATORS, and BINARY_OPERATORS.
*   **Expanded Token Support:** My language supports far more primitive token variants than standard Lox, incorporating C and Java-style bitwise shifts (<<, >>), and my own pointer types (@, $). Additionally I wanted primitive variable types so I added (BINARY, HEXADECIMAL).

## 2. Dependency/Setup Instructions
The tests utilize the pytest library and I manage all the external libraries using uv (so far just pytest).

**To run the test scripts:**
1. Navigate to the root directory of the repository.
2. Run the tests using pytest:
   pytest test/lab2/test_AST.py
3. Or, you can run the script directly in standard output:
   python test/lab2/test_AST.py

(Note: The test file appends "src" to the system path to ensure the interpreter can locate the AST and token classes in VS Code).

## 3. Test Cases and Printer Output
The first test is a modified version of the tree we discussed in class and the other four are random other tree variant I came up wit to test different tree structures and tokens.

All five test pass for their standard Lisp format we talked about in class; They also print the tree in Reverse Polish Notation, and finally they also print a display version of the tree so it is easy to understand the actual trees structure. 


## 4. Extra Credit Features
As mentioned previously I added two additional AST visualization features  beyond the base lab requirements.

**Feature 1: Reverse Polish Notation (RPN) Translator**
Every AST class possesses an .RPN() method that recursively translates the standard hierarchical tree into a Reverse Polish Notation.
*   **Value:** RPN completely eliminates the need for grouping parentheses and creates a highly efficient linear format for stack-based execution, additionally for unary operations I added a . before the operator, because my language doesn't use . as an operator and it allows for a potential interpreter to be able to determine if an operator is unary or binary. Without a . the interpreter wouldn't know if - is the unary or binary -.


**Feature 2: Graphical ASCII Tree Visualization**
Every AST class features a .display() method that formats the parsed hierarchy into a visual directory-style tree mapping using ├── and └── branches.
*   **Value:** It improves the debugging experience by providing an intuitive, graphical representation of the nested nodes. It also looks pretty cool.
*   **Example:** An example tree would look like this:

```
Binary:
├── Expression:
│   └── Literal: 1
├── Operator: +
└── Expression:
    └── Binary:
        ├── Expression:
        │   └── Literal: 2
        ├── Operator: *
        └── Expression:
            └── Literal: 3
```