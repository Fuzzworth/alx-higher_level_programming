#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for key, val in a_dictionary.items():
        if value != val:
            new_dict[key] = value
    return new_dict
