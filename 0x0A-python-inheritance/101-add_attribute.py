#!/usr/bin/python3
"""Function for  adding attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to which the  attribute is added.
        att (str): The name of the attribute to add.
        value (any): The value to assign to the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
