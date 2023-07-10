#!/usr/bin/python3
"""
Module docs
"""


class MyList(list):
    """
    Module that inherits from list
    """

    def print_sorted(self):
        """
        prints a sorted list
        """
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
