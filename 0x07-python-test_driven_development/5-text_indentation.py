#!/usr/bin/python3
"""
Module to print after . ? and :
"""


def text_indentation(text):
    """
    Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        test (str): string

    Raises:
        TypeError: error
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if (ord(i) == ord(".") or ord(i) == ord("?") or ord(i) == ord(":")):
            print(i, end="")
            print("\n\n", end="")
            continue
        print(i, end="")
