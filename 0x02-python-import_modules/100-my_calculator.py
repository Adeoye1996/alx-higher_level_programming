#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    operator = sys.argv[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = map(int, sys.argv[1:4])
    result = operators[operator](a, b)

    print(f"{a} {operator} {b} = {result}")
