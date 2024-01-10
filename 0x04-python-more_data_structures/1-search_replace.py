#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Search and replace elements in a list."""
    if my_list is None:
        return

    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace

    return my_list

