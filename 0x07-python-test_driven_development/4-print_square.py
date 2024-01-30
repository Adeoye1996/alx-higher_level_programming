#!/usr/bin/python3
"""Defines a square-printing function."""

def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size != int(size):
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
