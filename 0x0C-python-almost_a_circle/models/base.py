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
