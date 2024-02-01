#!/usr/bin/python3
<<<<<<< HEAD

"""Define a square-printing function."""


def print_square(size):
    """Prints a square pattern with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("Input size must be an integer")
    if size < 0:
        raise ValueError("Input size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
=======
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
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
