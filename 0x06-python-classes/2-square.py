#!/usr/bin/python3
"""
a class Square that defines a square by

Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """
    An object of square
    """
    def __init__(self, size=0):
        """
        Innitializing the Square object
        Args:
            param1 = self
            param2 = size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__self = size
