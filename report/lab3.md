# Lab 3: Parser
**Language Name:** SAB (Subtract And Branch)

## By Drake Setera ##

## Language Overview and Design Choices

For Lab 3, I implemented a recursive descent parser to convert scanned tokens into an Abstract Syntax Tree (AST). 

My biggest design choice and difference from Lox was completely abandoning the C/Java operator precedence table in favor of Python's precedence rules. In C/Java, bitwise operators (`&`, `|`, `^`) strangely sit below equality operators (`==`). I designed SAB to treat bitwise operations strictly as math, shifting them up to sit between addition and comparisons. Because of this, an expression like `x == 3 & 4` in SAB will evaluate cleanly as `x == (3 & 4)` instead of like `(x == 3) & 4` in C/Java.

Additionally, I modularized the parser's recursive descent structure. Instead of hardcoding a separate python method for every single precedence level like Lox does, my parser passes an integer `level` down recursively and has a list of sets called: `EXPRESSION_PRECEDENCE` where the index correlates to the level. The `evaluate()` function uses an `if/elif` block to handle right-to-left associativity (Assignments, Unary) and a generalized `while` loop to handle standard left-to-right binary math.

## Expression Grammar (Precedence and Associativity)

My grammar is evaluated from the lowest precedence (1) to the highest (15).

1. **Assignment (Right-to-Left):** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `^=`, `|=`, `&=`
2. **Conditional/Ternary (Left-to-Right):** `? :` and `?`
3. **Logical OR (Left-to-Right):** `||`
4. **Logical AND (Left-to-Right):** `&&`
5. **Logical NOT (Right-to-Left):** `!`
6. **Comparisons (Left-to-Right):** `<`, `<=`, `>`, `>=`, `==`, `!=`
7. **Bitwise OR (Left-to-Right):** `|`
8. **Bitwise XOR (Left-to-Right):** `^`
9. **Bitwise AND (Left-to-Right):** `&`
10. **Bitwise Shifts (Left-to-Right):** `<<`, `>>`
11. **Additive (Left-to-Right):** `+`, `-`
12. **Multiplicative (Left-to-Right):** `*`, `/`, `%`
13. **Exponent/Power (Left-to-Right):** `**`
14. **Unary (Right-to-Left):** `++`, `--`, `+`, `-`, `~`, `@`, `$`
15. **Primary/Grouping:** `()`, Literals (Int, Float, Str, Char, Bin, Hex, True, False, Null), Identifiers

## Setup and Run Instructions

The SAB compiler runs on standard Python 3. No external packages are needed.

**To run Interactive Mode (REPL):**
Run the following from the root directory:
`python src/SAB.py`
Type an expression (e.g., `1 + 2 * 3`) and press Enter. The parser will output the AST.

**To run in Source-File Mode:**
Pass a SAB file as an argument:
`python src/SAB.py test/lab3/test_file.sab`

## Test Cases
All test cases meet expectations


## Known Limitations / Failing Tests

Currently, the parser allows arbitrary expressions on the left side of an assignment (e.g., `5 = x;` will parse successfully into an AST). Standard compilers typically restrict the left side to l-values (variables/memory addresses). I will implement this validation step in the later semantic analysis phase.

## Optional Extra Credit Features

**Feature:** Advanced C-Style Conditional (Ternary) Operator (`? :` and `?`)

I implemented the ternary operator for inline branchless programming, but I expanded it beyond standard C/Java behavior. My parser supports **two** types of ternary statements:

1. **Standard Form (`x ? y : z`):** If `x` is `TRUE`, evaluate to `y`, else evaluate to `z`.
    * **Input:** `x == 3 ? 1 + 2 : 32 / 5`
    * **Output:** `(? (== x 3) (+ 1 2) (/ 32 5))`
2. **Short Form (`x ? y`):** If `x` is `TRUE`, assign/evaluate `y`. If `FALSE`, do nothing (the variable's value stays the same / evaluates to None).
    * **Input:** `x == 3 ? 100`
    * **Output:** `(? (== x 3) 100 None)`

**Value & Effort:** Because this requires up to three operands instead of the usual one or two, it required a dedicated branch in my parser. The parser evaluates the condition, mandates a `?`, recursively parses the true branch, and then *optionally* checks for a `:` to parse a false branch. If no `:` is found, the right branch simply becomes `None`. I also created a brand new `Trinary` AST node to properly store and display this structure.

**Feature:** Added static type objects. In the future I'm planning to add static type checking, so when someone attempts to compile their code it warns them about performing binary operations on different object types. 