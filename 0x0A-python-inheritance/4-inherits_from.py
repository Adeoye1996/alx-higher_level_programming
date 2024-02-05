#!/usr/bin/python3
"""Defines a function to check if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Checks if an obj is an inherited instance of a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an inherited istance of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
