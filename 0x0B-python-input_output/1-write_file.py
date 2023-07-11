#!/usr/bin/python3
"""
Mod docs
"""


def write_file(filename="", text=""):
    """
    function doc
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    return num
