#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string:
"""
import json
from io import StringIO


def from_json_string(my_str):
    """
    Deserialize a JSON string to a Python object.

    Parameters:
    - my_str (str): The JSON string to be deserialized.

    Returns:
    - object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
