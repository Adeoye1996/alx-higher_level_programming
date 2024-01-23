#!/usr/bin/python3

"""Define a custom MagicClass with bytecode specifications from Holberton."""

import math


class MagicClass:
    """Represent a circle with unique bytecode characteristics."""

    def __init__(self, radius=0):
        """Initialize a MagicClass with a specified radius.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return the circumference of the MagicClass circle."""
        return (2 * math.pi * self.__radius)
