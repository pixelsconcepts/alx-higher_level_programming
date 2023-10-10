#!/usr/bin/python3

"""
Reads the content of a file
"""

def read_file(filename=""):
    """
    Read the contents of a file and print it.

    Parameters:
    - filename (str): The name of the file to be read.

    Returns:
    - str: The content of the file as a string.
    """
    with open(filename, encoding="utf-8") as file_content:
        content = file_content.read()

        print("{}".format(content))
