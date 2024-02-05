#!/usr/bin/python3
"""Defines available attributes lookup function."""


def lookup(obj):
    """Return a list of available attributes."""
    return (dir(obj))
