#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
