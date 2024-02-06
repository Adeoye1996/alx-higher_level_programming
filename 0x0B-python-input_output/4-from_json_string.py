#!/usr/bin/python3
# 6-from_json_string.py
"""Defines JSON-to-object function."""
import json


def from_json_string(json_string):
    """Return the Python object representation of a JSON string."""
    return json.loads(json_string)
