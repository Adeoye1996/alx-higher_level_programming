#!/usr/bin/python3
"""Define a text file insertion module"""


def append_after(filename="", search_string="", new_string=""):
    """class body.
    Args:
        filename (str): The name of the file.
        search_strin (str): The string to search for within file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
