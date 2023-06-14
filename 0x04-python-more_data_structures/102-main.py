#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in a_dictionary.items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
