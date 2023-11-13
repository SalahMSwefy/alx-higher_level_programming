#!/usr/bin/python3
"""This module contains the BaseModel class"""
import json
import os.path

class Base:
    """This class will be the “base” of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            new_list = []
        else:
            new_list = []
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(new_list))
        
        return new_list

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        new_list = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                new_list = cls.from_json_string(f.read())
            for dict in new_list:
                new_list.append(cls.create(**dict))
        return new_list
