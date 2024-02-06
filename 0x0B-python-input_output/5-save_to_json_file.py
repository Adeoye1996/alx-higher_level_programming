#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(obj, filename):
    """Write a phython object to a JSON file."""
    with open(filename, "w") as file:
        json.dump(obj, file)
