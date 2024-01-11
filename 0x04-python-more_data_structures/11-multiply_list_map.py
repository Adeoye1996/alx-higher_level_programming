#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply each element of the list by a specified number."""
    return list(map(lambda x: x * number, my_list))
