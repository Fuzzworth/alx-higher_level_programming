#!/usr/bin/python3
"""
Module to copy an object
"""

def copy_list(l):
    """
    function that returns a copy of a list.

    Args:
        l (list): list to copy

    Returns:
        list: copy of l
    """

    new_list = l[:]
    return new_list
