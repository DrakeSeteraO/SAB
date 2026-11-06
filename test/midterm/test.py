import sys

sys.path.append("src")

from scanner import Scanner
from expression_parser import Expression_Parser
from expression_interpreter import Expression_Interpreter


def main():
    code = "(0.4)"
    print(f"Input: {code}\n")

    scanner = Scanner()
    tokens = scanner.scan(code + ";")
    print("Scanning results:")
    for token in tokens:
        print(token)
    print()

    tree = Expression_Parser(tokens).parse()
    print("Lisp Representation:")
    print(str(tree))
    print()

    print("AST:")
    print(tree.display())
    print()

    print("Evaluation Order:")
    Expression_Interpreter().get_expression(tree)
    print()
    
    print("Intermediate Results:")
    print(tree.display())


if __name__ == "__main__":
    main()