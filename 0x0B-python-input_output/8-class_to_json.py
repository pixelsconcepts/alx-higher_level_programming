#!/usr/bin/python3
"""
write a function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary with
    serializable attributes.

    Parameters:
    - obj: An instance of a class.

    Returns:
    - dict: A dictionary containing serializable attributes of the object.
    """
    attributes = obj.__dict__

    serializable_attributes = {
        key: value
        for key, value in attributes.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serializable_attributes
