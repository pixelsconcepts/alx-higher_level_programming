#!/usr/bin/python3
""" Base Class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of instances.

        Returns:
            str: A JSON-formatted string.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))
