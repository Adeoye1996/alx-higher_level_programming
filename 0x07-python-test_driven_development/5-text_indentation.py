#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
<<<<<<< HEAD
    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
=======
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
>>>>>>> 16ef7107f839f934cd843d2a351906b545b9759b

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
