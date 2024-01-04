#!/usr/bin/python3

if __name__ == "__main__":
    # Assign values to variables a and b on separate lines
    a = 1
    b = 2

    # Import the add function from add_0.py
    from add_0 import add

    # Use the print function with string format to display integers
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
