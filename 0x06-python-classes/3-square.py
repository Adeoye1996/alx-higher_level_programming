#!/usr/bin/python3

"""Definition of the Square class."""

class Square:
    """Body of the Square class."""

    def __init__(self, size=0):
        """Square constructor.

        Args:
            size (int): The size of the new square.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
