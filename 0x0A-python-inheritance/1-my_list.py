#!/usr/bin/pyhton3
"""
Module docs
"""


class MyList(list):
    """
    Module that inherits from list
    """

    def __init__(self, iterable):
        """
        init

        Args:
            iterable (list): list of things
        """
        super().__init__(int(item) for item in iterable)
    def print_sorted(self):
        """
        prints a sorted list
        """
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
