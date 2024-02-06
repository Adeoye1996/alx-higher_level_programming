#!/usr/bin/python3
"""Demostrates the usage of the to_json_string function."""
import json


def to_json_string(my_obj):
    """Serialize an object to a JSON-formatted string."""
    return json.dumps(my_obj)
