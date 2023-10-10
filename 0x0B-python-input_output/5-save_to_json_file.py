#!/usr/bin/python3
"""
function that writes an Object to a text file,
using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the JSON representation of an object to a text file.

    Parameters:
    - my_obj (object): The Python object to be saved to the file.
    - filename (str): The name of the file where the JSON
    representation will be saved.

    Returns:
    written file
    """
    with open(filename, "w") as f:
        written_file = json.dump(my_obj, f)

        return written_file
