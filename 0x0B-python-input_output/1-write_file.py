#!/usr/bin/python3
"""
Writes content to a file
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a file.

    Parameters:
    - filename (str): The name of the file to which
    the text will be written.
    - text (str): The text to be written to the file.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return written
