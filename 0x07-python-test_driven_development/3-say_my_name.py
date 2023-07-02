#!/usr/bin/python3
"""
Module for Name
"""


def say_my_name(first_name, last_name=""):
    """
    Write a function that prints My name is <first name> <last name>

    Args:
        first_name (str): string
        last_name (str:optional): string

    Raises:
        TypeError: if not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
