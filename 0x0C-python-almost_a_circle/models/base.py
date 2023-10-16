#!/usr/bin/python3
""" Base Class """


class Base:
    """
    Base class for managing unique identifiers.

    Attributes:
    __nb_objects (int): A private class attribute to keep track of
    the number of instances created.
    id (int): A public instance attribute representing the unique
    identifier for an instance.

    Methods:
    __init__(self, id=None): Class constructor for initializing
    instances with a unique identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance with a unique identifier.

        Args:
        id (int, optional): An optional argument representing
        the unique identifier.
        If not provided, a new identifier will be generated based on the class
        attribute __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
