#!/usr/bin/python3
"""
Module doc
"""


def add_attribute(a_class, att_name, att_value):
    """
    function docs
    """
    if a_class.__slots__:
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
