#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math

class MagicClass:
    """Initialization of the MagicClass."""

    def __init__(self, radius=0):
        """MagicClass constructor."""
        self._radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        self._radius = radius

    def area(self):
        """Calculate the area."""
        return self._radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference."""
        return 2 * math.pi * self._radius
