#!/usr/bin/python3
"""
Module doc
"""
import json


def class_to_json(obj):
    """
    function doc
    """
    return json.dumps(obj.__dict__)
