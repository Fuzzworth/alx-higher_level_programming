#!/usr/bin/python3
"""
Module doc
"""
import json


def load_from_json_file(filename):
    """
    function doc
    """
    with open(filename, "r") as f:
        return json.loads(f.readline())
