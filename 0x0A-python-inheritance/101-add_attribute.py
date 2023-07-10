#!/usr/bin/python3
"""
Module doc
"""


def add_attribute(a_class, att_name, att_value):
    """
    function docs
    """
    if '__slots__' in dir(a_class):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
