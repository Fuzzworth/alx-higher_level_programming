#!/usr/bin/python3
"""
Module Docs
"""
from json import dumps, loads
from os.path import isfile


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

        final_list = [i.to_dictionary() for i in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(final_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Function Doc
        """

        if type(json_string) is str:
            if len(json_string) == 0:
                return []
            else:
                return json.loads(json_string)
        elif json_string is None:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Function Doc
        """

        if cls.__name__ == "Rectangle":
            dummy_obj = cls(0, 0)
        elif cls.__name__ == "Square":
            dummy_obj = cls(0)
        else:
            dummy_obj = cls()
            return dummy_obj
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """
        Function Doc
        """
        filename = "{}.json".format(cls.__name__)
        if isfile(filename):
            with open(filename, "r") as f:
                line = f.readline()
                print(line)
                final_list = cls.from_json_string(line)
            obj_list = []
            for i in final_list:
                class_created = cls.create(i);
                obj_list.append(class_created)
            return obj_list
        else:
            return []
