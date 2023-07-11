#!/usr/bin/python3
"""
Mod docs
"""


class Student:
    """
    class docs
    """
    def __init__(self, first_name, last_name, age):
        """
        function docs
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function doc
        """
        final_list = {}
        all_string = True
        if type(attrs) is not list:
            all_string = False

        if type(attrs) is list:
            for i in attrs:
                if type(i) != str:
                    all_string = False
        if not all_string:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    final_list[i] = self.__dict__[i]
            return final_list
