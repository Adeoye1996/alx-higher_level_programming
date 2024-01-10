#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace occurrences of 'search' with 'replace' in the list."""
    if my_list is None:
        return

    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list

