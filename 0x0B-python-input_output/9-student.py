#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of attributes for class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a function that returns the dictionary description
        with simple data structure"""
        return self.__dict__
