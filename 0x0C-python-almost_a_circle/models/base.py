#!/usr/bin/python3
"""
Module Docs
"""
import json


class Base:
    """
    Class Docs
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Function Docs
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function Docs
        """

        if type(list_dictionaries) is list:
            if len(list_dictionaries) == 0:
                return json.dumps([])
            else:
                return json.dumps(list_dictionaries)
        elif list_dictionaries is None:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function Docs
        """

        filename = "{}.json".format(cls.__class__.__name__)
        print(filename)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(list_objs))
