#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance in a constructor."""
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal string representation."""
        if self._height == 0 or self._width == 0:
            return ''
        rec_str = (str(self.print_symbol) * self._width + '\n') * self._height
        return rec_str.rstrip('\n')

    def __repr__(self):
        """Return internal a string representation of a Rectangle instance."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Fires when a rectangle is destroyed."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance."""
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance."""
        self._validate_dimension(value, "height")
        self._height = value

    def _validate_dimension(self, value, dimension):
        """Validates the dimension value."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Calculates the area of a Rectangle instance."""
        return self._width * self._height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance."""
        return 2 * (self._width + self._height) if self._height != 0 and self._width != 0 else 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size."""
        return cls(size, size)
