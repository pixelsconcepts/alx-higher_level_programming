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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
        - dict: A dictionary containing public attributes
        of the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
