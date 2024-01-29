#!/usr/bin/python3
"""Module 7-rectangle
"""


class Rectangle:
    """Rectangle class definition.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance in a constructor.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal string representation.
        """
        if self.height == 0 or self.width == 0:
            return ''
        rectangle_str = '\n'.join([str(self.print_symbol) * self.width for _ in range(self.height)])
        return rectangle_str

    def __repr__(self):
        """Return internal string representation.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Fires when a Rectangle instance is destroyed."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance.
        """
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.
        """
        self._validate_dimension(value, "height")
        self._height = value

    def _validate_dimension(self, value, dimension):
        """Validate the dimension value."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Calculates the area of a Rectangle instance.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance.
        """
        return 2 * (self.width + self.height) if self.height != 0 and self.width != 0 else 0
