#!usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of attributes for class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a function that returns the dictionary description
        with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
