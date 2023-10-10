#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):

    """
    Load an object from a JSON file.

    Parameters:
    - filename (str): The name of the file containing the JSON representation.

    Returns:
    - object: The Python object represented by the JSON content of the file.
    """
    with open(filename, "r") as f:
        data = json.load(f)

    return data
