#!/usr/bin/python3
"""This is a module that create a type class"""
import json


class Base(object):
    """The goal of it is to manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        if list_objs is None or len(list_objs) == 0:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            obj_json = cls.to_json_string(list_dict)
            file.write(obj_json)

    @staticmethod
    def from_json_string(json_string):
        """
        from json string to dictionary, Deserialization
        json_string is a string representing a list of dict
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def dummy(self):
        """Intance to help to create classmethod"""
        if self.__name__ == "Rectangle":
            return self(1, 1, 0, 0, 1)
        elif self.__name__ == "Square":
            return self(1, 0, 0, 1)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        obj = cls.dummy(cls)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
                list_objects = [cls.create(**dict) for dict in dictionaries]
                return list_objects
        except Exception:
            return []
