#!/usr/bin/python3
"""
A class Square that defines a square by

Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """
    An object of square
    """
    def __init__(self, size=0):
        """
        Initializing the Square object

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, it prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
