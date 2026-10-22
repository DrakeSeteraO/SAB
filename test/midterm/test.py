import sys

sys.path.append("src")

from scanner import Scanner
from parser import Parser
from interpreter import Interpreter


def main():
    code = "(0.4)"
    print(f"Input: {code}\n")

    scanner = Scanner()
    tokens = scanner.scan(code + ";")
    print("Scanning results:")
    for token in tokens:
        print(token)
    print()

    tree = Parser(tokens).parse()
    print("Lisp Representation:")
    print(str(tree))
    print()

    print("AST:")
    print(tree.display())
    print()

    print("Evaluation Order:")
    Interpreter().get_expression(tree)
    print()
    
    print("Intermediate Results:")
    print(tree.display())


if __name__ == "__main__":
    main()