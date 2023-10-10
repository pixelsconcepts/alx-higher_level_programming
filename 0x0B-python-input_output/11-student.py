#!/usr/bin/python3
"""
Write a class Student that defines a student by:
-first_name: Public instance attributes
-last_name: Public instance attributes
-age: Public instance attributes
"""


class Student:
    """
        Initialize a Student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Parameters:
        - attrs (list, optional): A list of attribute names to include
        in the dictionary.
          If not provided, all attributes will be included.

        Returns:
        dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            attrs = vars(self).keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]

        student_dict = {attr: getattr(self, attr) for attr in attrs}

        return student_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on
        the provided dictionary.

        Parameters:
        - json (dict): A dictionary where keys are attribute names
        and values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
