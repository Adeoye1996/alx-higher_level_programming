#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        self._validate_dimension(value, "height")
        self._height = value

    def _validate_dimension(self, value, dimension):
        """Validate the dimension value."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self._width + self._height) if self._width != 0 and self._height != 0 else 0

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = ['#' * self._width + '\n'] * (self._height - 1)
        rect.append('#' * self._width)
        return ''.join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self._width}, {self._height})"
