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
    none_found = True
    start = 0
    for i in range(len(text)):

        if (ord(text[i]) == ord(".") or ord(text[i]) == ord("?") or ord(text[i]) == ord(":")):
            none_found = False
            string_to_print = text[start:i + 1].strip()
            print(f"{string_to_print}\n\n", end="")
            if (i + 1) <= (len(text) - 1):
                start = i + 1
    if none_found:
        print(text.strip(), end="")
    elif start != (len(text) - 1):
        print(text[start:len(text)].strip(), end="")
