#!/usr/bin/python3

if __name__ == "__main__":
    """Calculate and print the sum of 1 and 2 using a custom addition function."""
    from add_0 import add

    first_number = 1
    second_number = 2
    result = add(first_number, second_number)

    print("{} + {} = {}".format(first_number, second_number, result))
