#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append the specified text to a file.

    Parameters:
    - filename (str): The name of the file to which
    the text will be appended.
    - text (str): The text to be appended to the file.

    Returns:
    - int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        appended = file.write(text)
    return appended
