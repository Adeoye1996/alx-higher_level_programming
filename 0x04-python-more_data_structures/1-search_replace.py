#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Search and replace elements in a list."""
    if my_list is None:
        return
    updated_list = [replace if element == search else element for element in my_list]
    return updated_list
