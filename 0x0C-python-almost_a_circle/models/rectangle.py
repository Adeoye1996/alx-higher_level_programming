#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            identity (int): The identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
            TypeError: If x or y is not an integer.
            ValueError: If x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x_coordinate = x
        self.y_coordinate = y
        super().__init__(identity)

    @property
    def width(self):
        """Returning private attribute (__width)."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must b greater than 0")
        self.__height = value

    @property
    def x_coordinate(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x_coordinate

    @x.setter
    def x_coordinate(self, value):
        if type(value) != int:
            raise TypeError("x-coordinate must be an integer")
        if value < 0:
            raise ValueError("x must be greater than or equal to 0")
        self.__x_coordinate = value

    @property
    def y_coordinate(self):
        """Get or set the y-coordinate of the Rectangle."""
        return self.__y_coordinate

    @y.setter
    def y_coordinate(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be greater than or equal to 0")
        self.__y_coordinate = value

    def area(self):
        """Calculate returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y_coordinate)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the rectangle's attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents identity attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x_coordinate = v
                elif k == "y":
                    self.y_coordinate = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "identity": self.identity,
            "width": self.width,
            "height": self.height,
            "x": self.x_coordinate,
            "y": self.y_coordinate
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.identity,
                                                       self.x_coordinate, self.y_coordinate,
                                                       self.width, self.height)
