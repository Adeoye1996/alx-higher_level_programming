#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Compute the sum of unique elements in a list."""
    unique_elements = set(my_list)
    return sum(unique_elements)

