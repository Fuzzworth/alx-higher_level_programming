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

    def to_json(self):
        """
        function doc
        """
        return self.__dict__
