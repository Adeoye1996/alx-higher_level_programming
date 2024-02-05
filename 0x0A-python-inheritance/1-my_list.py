#!/usr/bin/python3
"""Custom an inherits from the list class MyList."""


class MyList(list):
    """Extends the functionality of the built-in list class with sorted printing."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
