#!/usr/bin/python3

""" Define the square module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Define the Squre class """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate and return the area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return a string representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
