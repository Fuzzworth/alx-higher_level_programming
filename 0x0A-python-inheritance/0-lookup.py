#!/usr/bin/python3
"""
Module to print attributtes
"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods
    of an object

    Args:
        obj (object): Object to print contents of

    Returns:
        list: List of attributes
    """
    return dir(obj)
