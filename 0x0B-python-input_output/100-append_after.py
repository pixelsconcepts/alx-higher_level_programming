#!/usr/bin/python3
"""
function that inserts a line of text to a file, after each
line containing a specific string
"""
def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing
    a specific string in a file.

    Parameters:
    - filename (str): The name of the file.
    - search_string (str): The specific string to search for in each line.
    - new_string (str): The line of text to insert after each
    line containing the search string.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
