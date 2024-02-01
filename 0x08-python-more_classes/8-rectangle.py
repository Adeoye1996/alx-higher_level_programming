#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        Rectangle.number_of_instances += 1
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
        """Set the width of the Rectangle."""
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self._width for _ in range(self._height)])

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# Example usage:
# rectangle1 = Rectangle(3, 4)
# print(rectangle1.area())
# print(rectangle1.perimeter())
# print(rectangle1)
# del rectangle1
# print(Rectangle.number_of_instances)
