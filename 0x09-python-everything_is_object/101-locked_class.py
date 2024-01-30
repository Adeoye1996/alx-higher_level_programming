#!/usr/bin/python3
"""Defines a secured class."""

class RestrictedObject:
    """
    Restricts the creation of new attributes in RestrictedObject
    except for attributes named 'first_name'.
    """

    __slots__ = ["first_name"]
