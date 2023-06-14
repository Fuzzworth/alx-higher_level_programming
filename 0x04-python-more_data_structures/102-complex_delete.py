#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for key, val in a_dictionary.items():
        if value != val:
            new_dict[key] = value
    a_dictionary.clear()
    for key, val in new_dict.items():
        a_dictionary[key] = val
    return new_dict
