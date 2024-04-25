#!/usr/bin/python3
"""
Algorithms list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not isinstance(list_of_integers, list):
        return None

    if not list_of_integers:
        return None

    peak = max(list_of_integers)
    return peak
