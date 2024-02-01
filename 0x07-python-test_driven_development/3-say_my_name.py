#!/usr/bin/python3
"""Defines a name-printing function."""

def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name are not strings.

        last_name (str): The last name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    full_name = " ".join([part for part in [first_name, last_name] if part])
    print("My name is {}".format(full_name))
    print("My name is {} {}".format(first_name, last_name))
