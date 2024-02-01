#!/usr/bin/python3
"""Defines a name-printing function."""

<<<<<<< HEAD

=======
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
<<<<<<< HEAD
        last_name (str, optional): The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name are not strings.
=======
        last_name (str): The last name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

<<<<<<< HEAD
    full_name = " ".join([part for part in [first_name, last_name] if part])
    print("My name is {}".format(full_name))
=======
    print("My name is {} {}".format(first_name, last_name))
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
