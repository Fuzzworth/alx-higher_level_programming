#!/usr/bin/python3
"""
Module doc
"""


def add_attribute(a_class, att_name, att_value):
    """
    function docs
    """
    eval("{}.{} = {}".format(a_class, att_name, att_value))
