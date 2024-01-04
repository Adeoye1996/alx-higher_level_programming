#!/usr/bin/python3

def my_addition(a, b):
    """Perform addition of two integers."""
    return a + b

def my_subtraction(a, b):
    """Perform subtraction of two integers."""
    return a - b

def my_multiplication(a, b):
    """Perform multiplication of two integers."""
    return a * b

def my_division(a, b):
    """Perform division of two integers."""
    if b != 0:
        return int(a / b)
    else:
        print("Error: Division by zero.")
        return None
