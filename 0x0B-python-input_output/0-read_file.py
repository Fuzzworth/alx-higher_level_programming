#!/usr/bin/python3
"""
Mod docs
"""


def read_file(filename=""):
    """
    function doc
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
