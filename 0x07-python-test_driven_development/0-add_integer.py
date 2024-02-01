#!/usr/bin/python3
"""Defines a function for integer addition."""

def add_integer(a, b=98):
    """Return the result of adding two integers.
    Float arguments are typecasted to ints before addition is performed.

Raises:
    TypeError: If either of a or b is a non-integer and non-float. """
def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Float arguments are typecasted to ints before addition.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
