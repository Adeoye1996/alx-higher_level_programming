#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    Restricts the creation of new attributes in RestrictedObject
    except for attributes named 'first_name'.
    """

    __slots__ = ["first_name"]
